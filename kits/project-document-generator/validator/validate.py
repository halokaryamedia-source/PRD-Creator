#!/usr/bin/env python3
"""Mechanical Flow 4 validation for the exact approved Golden PRD projection."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _engine  # noqa: E402

GOLDEN_GLOBAL_PAGE_IDS = {
    "development-overview": "development-overview",
    "game-system": "shared-systems",
    "data-reset": "shared-data-reset",
    "gameplay-development": "phase-development",
}


def _global_page_id(item: dict[str, Any]) -> str:
    return GOLDEN_GLOBAL_PAGE_IDS.get(item.get("id"), f'global-{item.get("id", "section")}')


def expected_page_ids(data: dict[str, Any]) -> list[str]:
    ids = ["summary"]
    for index, item in enumerate(data.get("gameplay_flow", [])):
        ids.append("flow-start" if index == 0 else f'flow-{item["id"]}')
    ids += [_global_page_id(item) for item in data.get("global_development", [])]
    for pkg in data.get("packages", []):
        package_id = pkg["id"]
        ids += [
            f"dev-{package_id}-requirement",
            f"dev-{package_id}-level",
            f"dev-{package_id}-developer",
        ]
    return ids


def document_composition_errors(data: dict[str, Any], facts: Any) -> list[str]:
    failures: list[str] = []
    packages = {pkg["id"]: pkg for pkg in data.get("packages", [])}

    def require(section_id: str, required: set[str]) -> None:
        available = facts.section_classes.get(section_id, set())
        missing = sorted(required - available)
        if missing:
            failures.append(f"{section_id} missing {missing}")

    for index, item in enumerate(data.get("gameplay_flow", [])):
        section_id = "flow-start" if index == 0 else f'flow-{item["id"]}'
        required = {"clean-visible", "story-page", "story-flow"}
        source_terms = item.get("terms", []) if index == 0 else packages.get(item["id"], {}).get("terms", [])
        if source_terms:
            required.add("quarry-definition-list")
        require(section_id, required)

    for item in data.get("global_development", []):
        require(
            _global_page_id(item),
            {
                "professional-only",
                "quarry-package-page",
                "phase-package-page",
                "global-development-page",
                "package-tabs",
                "section-context",
                "quarry-development-flow",
                "quarry-dev-table",
                "quarry-note-grid",
            },
        )

    for pkg in data.get("packages", []):
        package_id = pkg["id"]
        require(
            f"dev-{package_id}-requirement",
            {
                "professional-only",
                "quarry-package-page",
                "phase-package-page",
                "role-gameplay-overview",
                "package-tabs",
                "phase-context-grid",
                "quarry-overview-table",
                "quarry-sequence",
            },
        )
        require(
            f"dev-{package_id}-level",
            {
                "professional-only",
                "quarry-package-page",
                "phase-package-page",
                "package-tabs",
                "section-context",
                "quarry-design-flow",
                "quarry-build-table",
                "quarry-note-grid",
            },
        )
        require(
            f"dev-{package_id}-developer",
            {
                "professional-only",
                "quarry-package-page",
                "phase-package-page",
                "package-tabs",
                "section-context",
                "quarry-development-flow",
                "quarry-development-table",
                "quarry-score-summary",
                "quarry-note-grid",
            },
        )

    return failures


_engine.expected_page_ids = expected_page_ids
_engine.document_composition_errors = document_composition_errors
validate = _engine.validate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="workspace/active/<project> directory")
    parser.add_argument("--output", type=Path, help="optional JSON result path")
    args = parser.parse_args()
    result = validate(args.project)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
