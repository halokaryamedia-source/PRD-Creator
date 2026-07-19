#!/usr/bin/env python3
"""Run validation, rendering, HTML audit, packaging, and state update."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


def find_file(root: Path, candidates: list[str]) -> Path | None:
    for candidate in candidates:
        path = root / candidate
        if path.is_file():
            return path
    return None


def run(command: list[str], cwd: Path | None = None) -> None:
    result = subprocess.run(command, cwd=cwd, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed ({result.returncode}): {' '.join(command)}")


def load_validator(path: Path):
    spec = importlib.util.spec_from_file_location("pdb_validate_package", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load validator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def relative_or_name(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.name


def update_project_state(
    state_path: Path,
    workspace: Path,
    html_path: Path,
    zip_path: Path,
    report_path: Path,
    audit_path: Path,
    html_version: str,
) -> None:
    state = yaml.safe_load(state_path.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    state["workflow"]["current_phase"] = "delivery"
    state["workflow"]["html_status"] = "approved"
    state["workflow"]["final_status"] = "approved_for_delivery"
    state["versions"]["html"] = html_version
    state.setdefault("artifacts", {})["html"] = {
        "latest": {
            "version": html_version,
            "path": relative_or_name(html_path, workspace),
            "status": "approved",
            "checksum": sha256(html_path),
            "created_at": now,
        }
    }
    state["artifacts"]["zip"] = {
        "latest": {
            "version": html_version,
            "path": relative_or_name(zip_path, workspace),
            "status": "approved",
            "checksum": sha256(zip_path),
            "created_at": now,
        }
    }
    audits = state["artifacts"].setdefault("audits", {})
    audits["html"] = {
        "latest": {
            "version": html_version,
            "path": relative_or_name(audit_path, workspace),
            "status": "passed",
            "checksum": sha256(audit_path),
            "created_at": now,
        }
    }
    audits["render"] = {
        "latest": {
            "version": html_version,
            "path": relative_or_name(report_path, workspace),
            "status": "passed",
            "checksum": sha256(report_path),
            "created_at": now,
        }
    }
    state["next_step"] = {
        "action": "Review the approved delivery artifacts",
        "reason": "Rendering and Final HTML Audit have passed.",
        "target_phase": "delivery",
        "target_flow": None,
    }
    state_path.write_text(yaml.safe_dump(state, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--html-version", default="1.0")
    parser.add_argument("--template-version", default="1.0")
    parser.add_argument("--schema-version", default="0.1")
    parser.add_argument("--golden-sample-version", default="aftershock-1.0")
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument(
        "--equivalence-audit",
        choices=("not_run", "passed", "failed"),
        default="not_run",
        help="Result of the separate semantic EN/ID equivalence review. Final delivery requires 'passed'.",
    )
    parser.add_argument("--no-state-update", action="store_true")
    args = parser.parse_args()

    package_root = Path(__file__).resolve().parents[1]
    workspace = args.workspace.resolve()
    output_dir = (args.output_dir or workspace / "output").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    content = find_file(workspace, ["content/project-content.yaml", "project-content.yaml", "content/project-content.json", "project-content.json"])
    glossary = find_file(workspace, ["content/glossary.yaml", "glossary.yaml", "content/glossary.json", "glossary.json"])
    decisions = find_file(workspace, ["state/decision-log.yaml", "decision-log.yaml", "state/decision-log.json", "decision-log.json"])
    assumptions = find_file(workspace, ["state/assumptions.yaml", "assumptions.yaml", "state/assumptions.json", "assumptions.json"])
    state = find_file(workspace, ["state/project-state.yaml", "project-state.yaml", "state/project-state.json", "project-state.json"])
    if not content:
        print("PIPELINE FAILED: project-content file not found.", file=sys.stderr)
        return 2

    document = yaml.safe_load(content.read_text(encoding="utf-8"))["document"]
    document_id = document["id"]
    html_path = output_dir / f"{document_id}-production-document-v{args.html_version}.html"
    report_path = output_dir / f"render-report-v{args.html_version}.yaml"
    audit_path = output_dir / f"html-audit-v{args.html_version}.md"
    screenshots_dir = output_dir / "screenshots"
    zip_path = output_dir / f"{document_id}-production-document-v{args.html_version}.zip"

    try:
        run([sys.executable, str(package_root / "scripts" / "validate_package.py"), "--schema-dir", str(package_root / "schemas"), "workspace", str(workspace)])

        render_cmd = [
            sys.executable,
            str(package_root / "scripts" / "render_document.py"),
            str(content),
            "--output", str(html_path),
            "--template-dir", str(package_root / "templates"),
            "--schema-dir", str(package_root / "schemas"),
            "--template-version", args.template_version,
            "--schema-version", args.schema_version,
            "--golden-sample-version", args.golden_sample_version,
            "--html-version", args.html_version,
        ]
        for flag, path in (("--glossary", glossary), ("--decisions", decisions), ("--assumptions", assumptions), ("--project-state", state)):
            if path:
                render_cmd.extend([flag, str(path)])
        run(render_cmd)

        audit_cmd = [
            sys.executable,
            str(package_root / "scripts" / "validate_html.py"),
            str(html_path),
            "--content", str(content),
            "--report", str(report_path),
            "--audit-md", str(audit_path),
            "--equivalence-audit", args.equivalence_audit,
        ]
        if glossary:
            audit_cmd.extend(["--glossary", str(glossary)])
        if not args.no_browser:
            audit_cmd.extend(["--browser", "--screenshots-dir", str(screenshots_dir)])
        run(audit_cmd)

        run([
            sys.executable,
            str(package_root / "scripts" / "package_output.py"),
            "--html", str(html_path),
            "--report", str(report_path),
            "--audit", str(audit_path),
            "--zip", str(zip_path),
            "--screenshots-dir", str(screenshots_dir),
            "--root-name", f"{document_id}-production-document-v{args.html_version}",
        ])

        validator = load_validator(package_root / "scripts" / "validate_package.py")
        schemas, registry = validator.load_schemas(package_root / "schemas")
        report_data = validator.load_data(report_path)
        report_issues = validator.validate_data(report_data, "render-report.schema.json", schemas, registry)
        if report_issues:
            raise RuntimeError("Render report validation failed: " + "; ".join(str(issue) for issue in report_issues))

        if state and not args.no_state_update:
            update_project_state(state, workspace, html_path, zip_path, report_path, audit_path, args.html_version)
            state_data = validator.load_data(state)
            state_issues = validator.validate_data(state_data, "project-state.schema.json", schemas, registry)
            if state_issues:
                raise RuntimeError("Updated Project State is invalid: " + "; ".join(str(issue) for issue in state_issues))

        result = {
            "status": "approved_for_delivery",
            "html": str(html_path),
            "zip": str(zip_path),
            "render_report": str(report_path),
            "html_audit": str(audit_path),
            "zip_sha256": sha256(zip_path),
            "project_state_updated": bool(state and not args.no_state_update),
        }
        result_path = output_dir / "pipeline-result.json"
        result_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result, indent=2))
        return 0
    except (RuntimeError, OSError, KeyError, TypeError, yaml.YAMLError) as exc:
        print(f"PIPELINE FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
