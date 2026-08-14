#!/usr/bin/env python3
"""Validate that Flow 5 is entering from the current accepted PRD handoff."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
ACCEPTANCE_REQUIRED = {
    "Status": {"handoff_ready"},
    "Mechanical": {"PASS"},
    "Semantic Readiness": {"PASS"},
    "Material Conservation": {"PASS"},
    "Visual sanity": {"PASS", "NOT PROVEN"},
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
    return True, "acceptance.md authorizes handoff_ready with Mechanical, Semantic Readiness, Material Conservation, and no Critical/Major blocker"


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
        "current_prd_version_semantic",
        bool(SEMVER_RE.fullmatch(current_version)),
        f"current document.version is {current_version!r}; expected X.Y.Z",
    )
    check(
        "handoff_revision_matches_current_prd",
        bool(current_version) and accepted_version == current_version,
        f"accepted_prd_version={accepted_version!r}, current document.version={current_version!r}",
    )

    refs_ok = True
    ref_details: list[str] = []
    refs = expected_refs(current_version) if SEMVER_RE.fullmatch(current_version) else {}
    if not refs:
        refs_ok = False
        ref_details.append("cannot resolve versioned handoff paths until document.version uses X.Y.Z")
    else:
        for field, expected in refs.items():
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
        "handoff-state points to canonical PRD inputs plus the current versioned prd/context/index bundle"
        if refs_ok
        else "; ".join(ref_details),
    )

    delivery_ok = bool(refs)
    delivery_details: list[str] = []
    if refs:
        try:
            context_text = (project / refs["context"]).read_text(encoding="utf-8")
            readme_text = (project / refs["handoff"]).read_text(encoding="utf-8")
            index_data = json.loads((project / refs["index"]).read_text(encoding="utf-8"))
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
        except (OSError, json.JSONDecodeError) as exc:
            delivery_ok = False
            delivery_details.append(f"delivery metadata unreadable: {exc}")
    check(
        "delivery_revision_matches_current_prd",
        delivery_ok,
        "context.md, index.json, and output/README.md identify the current PRD revision"
        if delivery_ok
        else "; ".join(delivery_details) or "delivery metadata could not be verified",
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
