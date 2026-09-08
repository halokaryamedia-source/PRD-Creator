#!/usr/bin/env python3
"""Thin mechanical operator CLI for PRD-Creator project workflows."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
KIT_ROOT = ROOT / "kits" / "prd-creator"
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from browser_verify import BrowserVerifyError  # noqa: E402
from browser_verify import verify as verify_browser
from renderer.delivery import build_delivery  # noqa: E402
from shared.state import StateError  # noqa: E402
from validator import api as prd_api  # noqa: E402
from validator import validate_handoff as handoff_validator  # noqa: E402
from validator import voice_validation  # noqa: E402


def _first_issue(result: dict[str, Any]) -> dict[str, Any] | None:
    issues = result.get("issues")
    if isinstance(issues, list):
        for issue in issues:
            if isinstance(issue, dict):
                return {
                    key: issue[key]
                    for key in ("code", "owner", "message", "path", "field", "line", "severity")
                    if key in issue and issue[key] not in (None, "")
                }
    errors = result.get("errors")
    if isinstance(errors, list) and errors:
        return {
            "code": "UNSTRUCTURED_VALIDATION_ERROR",
            "owner": "unknown",
            "message": str(errors[0]),
        }
    return None


def _domain(result: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": str(result.get("status") or "fail"),
        "first_issue": _first_issue(result),
    }


def _not_present() -> dict[str, Any]:
    return {"status": "not_present", "first_issue": None}


def _blocked_by(upstream: str) -> dict[str, Any]:
    return {"status": f"blocked_by_{upstream}", "first_issue": None}


def status_payload(project: Path) -> dict[str, Any]:
    project = project.resolve()
    prd_result = prd_api.validate(project)
    prd = _domain(prd_result)

    handoff_state = project / "state" / "handoff-state.yaml"
    voice_state = project / "state" / "voice-state.yaml"

    if prd["status"] != "pass":
        handoff = _blocked_by("prd") if handoff_state.is_file() else _not_present()
        voice = _blocked_by("prd") if voice_state.is_file() else _not_present()
    else:
        if handoff_state.is_file():
            handoff_result = handoff_validator.validate(project)
            handoff = _domain(handoff_result)
        else:
            handoff = _not_present()

        if voice_state.is_file():
            if handoff["status"] == "fail":
                voice = _blocked_by("handoff")
            else:
                voice = _domain(voice_validation.validate(project))
        else:
            voice = _not_present()

    first_issue = next(
        (stage["first_issue"] for stage in (prd, handoff, voice) if isinstance(stage.get("first_issue"), dict)),
        None,
    )
    blocked = first_issue is not None or any(
        str(stage["status"]).startswith("blocked_by_") for stage in (prd, handoff, voice)
    )

    if first_issue is not None:
        owner = str(first_issue.get("owner") or "unknown")
        code = str(first_issue.get("code") or "unknown")
        location = str(first_issue.get("path") or "").strip()
        field = str(first_issue.get("field") or "").strip()
        if field:
            location = f"{location}:{field}" if location else field
        target = f" at {location}" if location else ""
        next_action = f"Fix the first wrong owner {owner} ({code}){target}, then rerun status."
    elif handoff["status"] == "not_present":
        next_action = "PRD mechanical validation passes. Handoff state is not present; no handoff readiness is claimed."
    elif voice["status"] == "not_present":
        next_action = "PRD handoff validation passes. Voice state is not present; no Voice readiness is claimed."
    else:
        next_action = "All present mechanical validation stages pass."

    return {
        "project": project.name,
        "mechanical_status": "blocked" if blocked else "clear",
        "prd": prd,
        "handoff": handoff,
        "voice": voice,
        "first_issue": first_issue,
        "next_action": next_action,
    }


def _print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def _print_status(payload: dict[str, Any]) -> None:
    print(f"Project: {payload['project']}")
    print(f"Mechanical: {str(payload['mechanical_status']).upper()}")
    for label in ("prd", "handoff", "voice"):
        stage = payload[label]
        print(f"{label.upper()}: {str(stage['status']).upper()}")
    issue = payload.get("first_issue")
    if isinstance(issue, dict):
        code = issue.get("code", "unknown")
        owner = issue.get("owner", "unknown")
        message = issue.get("message", "")
        print(f"First issue: {code} [{owner}] {message}")
        location = str(issue.get("path") or "").strip()
        field = str(issue.get("field") or "").strip()
        if location or field:
            suffix = f":{field}" if field else ""
            print(f"Location: {location}{suffix}")
    print(f"Next: {payload['next_action']}")


def _relative_outputs(project: Path, outputs: dict[str, Path]) -> dict[str, str]:
    project = project.resolve()
    rendered: dict[str, str] = {}
    for label, path in outputs.items():
        resolved = path.resolve()
        try:
            rendered[label] = resolved.relative_to(project).as_posix()
        except ValueError:
            rendered[label] = resolved.as_posix()
    return rendered


def _result_exit(result: dict[str, Any]) -> int:
    _print_json(result)
    return 0 if result.get("status") == "pass" else 1


def _current_prd_html(project: Path) -> Path:
    data_path = project / "work" / "render-data.json"
    raw = json.loads(data_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("render-data root must be an object")
    document = raw.get("document")
    if not isinstance(document, dict):
        raise ValueError("render-data.document must be an object")
    version = str(document.get("version") or "").strip()
    if not version:
        raise ValueError("render-data.document.version is required")
    return project / "output" / f"v{version}" / "prd.html"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    status_parser = subparsers.add_parser("status", help="show compact mechanical project status and first wrong owner")
    status_parser.add_argument("project", type=Path)
    status_parser.add_argument("--json", action="store_true", dest="as_json")

    browser_parser = subparsers.add_parser(
        "browser",
        help="verify the current validated PRD in real Chrome and emit visual/runtime evidence",
    )
    browser_parser.add_argument("project", type=Path)
    browser_parser.add_argument("--screenshot", type=Path, help="optional PNG evidence path")

    for command, help_text in (
        ("build", "build the canonical versioned delivery bundle"),
        ("validate", "run canonical PRD validation"),
        ("handoff", "run canonical PRD handoff validation"),
        ("voice", "run canonical Voice validation"),
    ):
        command_parser = subparsers.add_parser(command, help=help_text)
        command_parser.add_argument("project", type=Path)

    args = parser.parse_args()
    project = args.project.resolve()

    try:
        if args.command == "status":
            payload = status_payload(project)
            if args.as_json:
                _print_json(payload)
            else:
                _print_status(payload)
            return 1 if payload["mechanical_status"] == "blocked" else 0
        if args.command == "build":
            outputs = build_delivery(project)
            _print_json({"status": "pass", "outputs": _relative_outputs(project, outputs)})
            return 0
        if args.command == "validate":
            return _result_exit(prd_api.validate(project))
        if args.command == "browser":
            current_prd = prd_api.validate(project)
            if current_prd.get("status") != "pass":
                return _result_exit(current_prd)
            screenshot = args.screenshot.resolve() if args.screenshot is not None else None
            return _result_exit(verify_browser(_current_prd_html(project), screenshot))
        if args.command == "handoff":
            return _result_exit(handoff_validator.validate(project))
        if args.command == "voice":
            return _result_exit(voice_validation.validate(project))
    except (BrowserVerifyError, OSError, StateError, ValueError, json.JSONDecodeError) as exc:
        print(f"PRD OPERATOR FAILED: {exc}", file=sys.stderr)
        return 2

    parser.error(f"unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
