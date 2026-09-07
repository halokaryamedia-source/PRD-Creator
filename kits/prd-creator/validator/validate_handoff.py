#!/usr/bin/env python3
"""Validate that Flow 5 is entering from the current accepted PRD handoff."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
if __package__ in (None, ""):
    if str(KIT_ROOT) not in sys.path:
        sys.path.insert(0, str(KIT_ROOT))
    from validator import api as prd_api
else:
    from . import api as prd_api

from shared.handoff import load_handoff_state
from shared.paths import ProjectPathError, resolve_project_path
from shared.state import StateError

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ACCEPTANCE_REQUIRED = {
    "Status": {"handoff_ready"},
    "Mechanical": {"PASS"},
    "Semantic Readiness": {"PASS"},
    "Material Conservation": {"PASS"},
    "Visual sanity": {"PASS", "NOT PROVEN"},
    "Critical": {"0"},
    "Major": {"0"},
}
ACCEPTED_RENDER_LABEL = "Accepted Render Data SHA256"
ACCEPTED_ASSET_LABEL = "Accepted Asset Requirements SHA256"


def acceptance_values(text: str, label: str) -> list[str]:
    pattern = re.compile(rf"(?mi)^\s*{re.escape(label)}:\s*(.*?)\s*$")
    return [value.strip() for value in pattern.findall(text)]


def validate_acceptance(
    path: Path,
    expected_render_sha: str,
    expected_asset_sha: str,
) -> tuple[bool, str]:
    if not path.is_file():
        return False, f"missing acceptance artifact: {path}"

    text = path.read_text(encoding="utf-8")
    failures: list[str] = []
    for label, allowed in ACCEPTANCE_REQUIRED.items():
        values = acceptance_values(text, label)
        if len(values) != 1 or not values[0]:
            failures.append(f"{label} must appear exactly once with a non-empty value")
            continue
        if values[0] not in allowed:
            failures.append(f"{label}={values[0]!r}, expected one of {sorted(allowed)}")

    render_values = acceptance_values(text, ACCEPTED_RENDER_LABEL)
    if len(render_values) != 1 or SHA256_RE.fullmatch(render_values[0]) is None:
        failures.append(f"{ACCEPTED_RENDER_LABEL} must appear exactly once as a sha256 hex digest")
    elif render_values[0] != expected_render_sha:
        failures.append(
            f"{ACCEPTED_RENDER_LABEL}={render_values[0]!r}, expected current render-data sha256 {expected_render_sha!r}"
        )

    asset_values = acceptance_values(text, ACCEPTED_ASSET_LABEL)
    if len(asset_values) != 1:
        failures.append(f"{ACCEPTED_ASSET_LABEL} must appear exactly once")
    elif asset_values[0] != "none" and SHA256_RE.fullmatch(asset_values[0]) is None:
        failures.append(f"{ACCEPTED_ASSET_LABEL} must be 'none' or a sha256 hex digest")
    elif asset_values[0] != expected_asset_sha:
        failures.append(
            f"{ACCEPTED_ASSET_LABEL}={asset_values[0]!r}, expected current asset requirements binding {expected_asset_sha!r}"
        )

    if failures:
        return False, "; ".join(failures)
    return (
        True,
        "acceptance.md authorizes the exact current render-data and non-Voice asset-requirements revisions",
    )


def expected_refs(version: str) -> dict[str, str]:
    base = f"output/v{version}"
    return {
        "content": "work/content.md",
        "render_data": "work/render-data.json",
        "html": f"{base}/prd.html",
        "context": f"{base}/context.md",
        "index": f"{base}/index.json",
        "acceptance": "work/acceptance.md",
        "handoff": "output/README.md",
    }


def validate(project: Path) -> dict[str, Any]:
    project = project.resolve()
    state_path = project / "state" / "handoff-state.yaml"
    data_path = project / "work" / "render-data.json"
    acceptance_path = project / "work" / "acceptance.md"
    asset_path = project / "work" / "asset-requirements.md"
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
        state = load_handoff_state(state_path)
    except (OSError, StateError) as exc:
        errors.append(f"handoff_state: {exc}")
        return {"status": "fail", "errors": errors, "checks": checks}

    check(
        "handoff_status_ready",
        state.status == "handoff_ready",
        "handoff_ready"
        if state.status == "handoff_ready"
        else f"status is {state.status!r}, expected 'handoff_ready'",
    )

    current_prd = prd_api.validate(project)
    current_prd_ok = current_prd.get("status") == "pass"
    current_prd_errors = [str(item) for item in current_prd.get("errors", [])]
    check(
        "current_prd_complete_validation",
        current_prd_ok,
        "canonical PRD validation passes, including Flow 2 approval, projection schema, content purity, and freshness"
        if current_prd_ok
        else "; ".join(current_prd_errors[:5]) or "canonical PRD validation failed",
    )

    try:
        data_bytes = data_path.read_bytes()
        data = json.loads(data_bytes.decode("utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"render_data_json: {exc}")
        return {"status": "fail", "errors": errors, "checks": checks}

    current_render_sha = hashlib.sha256(data_bytes).hexdigest()
    current_asset_sha = hashlib.sha256(asset_path.read_bytes()).hexdigest() if asset_path.is_file() else "none"
    doc = data.get("document") if isinstance(data, dict) else None
    current_version = str(doc.get("version") or "").strip() if isinstance(doc, dict) else ""
    check(
        "current_prd_version_present",
        bool(current_version),
        f"current document.version is {current_version!r}"
        if current_version
        else "render-data.document.version is required for handoff",
    )
    check(
        "current_prd_version_semantic",
        bool(SEMVER_RE.fullmatch(current_version)),
        f"current document.version is {current_version!r}; expected X.Y.Z",
    )
    check(
        "handoff_revision_matches_current_prd",
        bool(current_version) and state.accepted_prd_version == current_version,
        f"accepted_prd_version={state.accepted_prd_version!r}, current document.version={current_version!r}",
    )

    refs_ok = True
    ref_details: list[str] = []
    refs = expected_refs(current_version) if SEMVER_RE.fullmatch(current_version) else {}
    if not refs:
        refs_ok = False
        ref_details.append("cannot resolve versioned handoff paths until document.version uses X.Y.Z")
    else:
        for field, expected in refs.items():
            actual = state.refs.get(field, "")
            if actual != expected:
                refs_ok = False
                ref_details.append(f"{field}={actual!r}, expected {expected!r}")
                continue
            try:
                resolve_project_path(
                    project,
                    actual,
                    owner=f"handoff-state.yaml.{field}",
                    must_exist=True,
                )
            except ProjectPathError as exc:
                refs_ok = False
                ref_details.append(str(exc))
    check(
        "handoff_artifact_references_current",
        refs_ok,
        "handoff-state uses canonical project-relative paths for the current PRD bundle"
        if refs_ok
        else "; ".join(ref_details),
    )

    delivery_ok = bool(refs)
    delivery_details: list[str] = []
    if refs:
        try:
            context_text = resolve_project_path(project, refs["context"], must_exist=True).read_text(encoding="utf-8")
            readme_text = resolve_project_path(project, refs["handoff"], must_exist=True).read_text(encoding="utf-8")
            index_data = json.loads(
                resolve_project_path(project, refs["index"], must_exist=True).read_text(encoding="utf-8")
            )
            index_project = index_data.get("project") if isinstance(index_data, dict) else None
            index_version = (
                str(index_project.get("prd_version") or "").strip()
                if isinstance(index_project, dict)
                else ""
            )
            if f"PRD Version: v{current_version}" not in context_text:
                delivery_ok = False
                delivery_details.append("context.md PRD version does not match current document.version")
            if f"Current PRD Version: `v{current_version}`" not in readme_text:
                delivery_ok = False
                delivery_details.append("output/README.md current version does not match document.version")
            if index_version != current_version:
                delivery_ok = False
                delivery_details.append(
                    f"index.json project.prd_version={index_version!r}, expected {current_version!r}"
                )
        except (OSError, ProjectPathError, json.JSONDecodeError) as exc:
            delivery_ok = False
            delivery_details.append(f"delivery metadata unreadable: {exc}")
    check(
        "delivery_revision_matches_current_prd",
        delivery_ok,
        "context.md, index.json, and output/README.md identify the current PRD revision"
        if delivery_ok
        else "; ".join(delivery_details) or "delivery metadata could not be verified",
    )

    acceptance_ok, acceptance_detail = validate_acceptance(
        acceptance_path,
        current_render_sha,
        current_asset_sha,
    )
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
