#!/usr/bin/env python3
"""Validate that Flow 5 is entering from the current accepted PRD handoff."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

EXPECTED_REFS = {
    "content": "work/content.md",
    "render_data": "work/render-data.json",
    "html": "output/final.html",
    "acceptance": "work/acceptance.md",
    "handoff": "output/team-handoff.md",
}
ACCEPTANCE_REQUIRED = {
    "Status": {"handoff_ready"},
    "Mechanical": {"PASS"},
    "Visual sanity": {"PASS", "NOT PROVEN"},
    "New Reader": {"PASS"},
    "Level Designer": {"PASS"},
    "Developer": {"PASS"},
    "Project Consistency": {"PASS"},
    "Critical": {"0"},
    "Major": {"0"},
}


def scalar_values(text: str, key: str) -> list[str]:
    pattern = re.compile(rf"(?m)^\s*{re.escape(key)}:\s*(.*?)\s*(?:#.*)?$")
    values: list[str] = []
    for raw in pattern.findall(text):
        value = raw.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1].strip()
        values.append(value)
    return values


def one_scalar(text: str, key: str) -> str:
    values = scalar_values(text, key)
    if len(values) != 1 or not values[0]:
        raise ValueError(f"handoff-state.yaml must define exactly one non-empty {key}")
    return values[0]


def acceptance_values(text: str, label: str) -> list[str]:
    pattern = re.compile(rf"(?mi)^\s*{re.escape(label)}:\s*(.*?)\s*$")
    return [value.strip() for value in pattern.findall(text)]


def validate_acceptance(path: Path) -> tuple[bool, str]:
    if not path.is_file():
        return False, f"missing acceptance artifact: {path}"

    text = path.read_text(encoding="utf-8")
    failures: list[str] = []
    for label, allowed in ACCEPTANCE_REQUIRED.items():
        values = acceptance_values(text, label)
        if len(values) != 1 or not values[0]:
            failures.append(f"{label} must appear exactly once with a non-empty value")
            continue
        value = values[0]
        if value not in allowed:
            failures.append(f"{label}={value!r}, expected one of {sorted(allowed)}")

    if failures:
        return False, "; ".join(failures)
    return True, "acceptance.md authorizes handoff_ready with no Critical/Major blocker"


def validate(project: Path) -> dict[str, Any]:
    state_path = project / "state" / "handoff-state.yaml"
    data_path = project / "work" / "render-data.json"
    acceptance_path = project / "work" / "acceptance.md"
    errors: list[str] = []
    checks: list[dict[str, str]] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"check": name, "status": "pass" if ok else "fail", "detail": detail})
        if not ok:
            errors.append(f"{name}: {detail}")

    check("handoff_state_exists", state_path.is_file(), str(state_path))
    check("render_data_exists", data_path.is_file(), str(data_path))
    if errors:
        return {"status": "fail", "errors": errors, "checks": checks}

    try:
        state_text = state_path.read_text(encoding="utf-8")
        status = one_scalar(state_text, "status")
        accepted_version = one_scalar(state_text, "accepted_prd_version")
    except (OSError, ValueError) as exc:
        errors.append(f"handoff_state: {exc}")
        return {"status": "fail", "errors": errors, "checks": checks}

    check(
        "handoff_status_ready",
        status == "handoff_ready",
        "handoff_ready" if status == "handoff_ready" else f"status is {status!r}, expected 'handoff_ready'",
    )

    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"render_data_json: {exc}")
        return {"status": "fail", "errors": errors, "checks": checks}

    doc = data.get("document") if isinstance(data, dict) else None
    current_version = str(doc.get("version") or "").strip() if isinstance(doc, dict) else ""
    check(
        "current_prd_version_present",
        bool(current_version),
        f"current document.version is {current_version!r}" if current_version else "render-data.document.version is required for handoff",
    )
    check(
        "handoff_revision_matches_current_prd",
        bool(current_version) and accepted_version == current_version,
        f"accepted_prd_version={accepted_version!r}, current document.version={current_version!r}",
    )

    refs_ok = True
    ref_details: list[str] = []
    for field, expected in EXPECTED_REFS.items():
        try:
            actual = one_scalar(state_text, field)
        except ValueError as exc:
            refs_ok = False
            ref_details.append(str(exc))
            continue
        if actual != expected:
            refs_ok = False
            ref_details.append(f"{field}={actual!r}, expected {expected!r}")
            continue
        target = project / expected
        if not target.is_file():
            refs_ok = False
            ref_details.append(f"missing referenced artifact: {expected}")

    check(
        "handoff_artifact_references_current",
        refs_ok,
        "handoff-state points to the current canonical PRD/acceptance/handoff paths"
        if refs_ok
        else "; ".join(ref_details),
    )

    acceptance_ok, acceptance_detail = validate_acceptance(acceptance_path)
    check("acceptance_allows_handoff", acceptance_ok, acceptance_detail)

    return {"status": "pass" if not errors else "fail", "errors": errors, "checks": checks}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="workspace/active/<project> directory")
    args = parser.parse_args()
    result = validate(args.project)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
