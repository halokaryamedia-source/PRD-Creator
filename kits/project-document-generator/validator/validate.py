#!/usr/bin/env python3
"""Mechanical Flow 4 validation for the exact approved Golden PRD projection."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

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
PREVIEW_APPROVED_RE = re.compile(r"(?mi)^\s*preview_approved:\s*(true|false)\s*(?:#.*)?$")
_BASE_FLOW2_READINESS = _engine.flow2_readiness

# These are explicit generator/document-process phrases that have no place in a
# project PRD. Keep this list narrow: it catches observed leakage without
# turning normal project vocabulary (for example a gameplay "rule template")
# into a false positive.
PROCESS_LEAK_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("Golden HTML/reference language", re.compile(r"\bGolden\s+(?:HTML|Sample|Reference|page structure)\b", re.I)),
    ("PRD-Creator/internal artifact", re.compile(r"\b(?:PRD-Creator|render-data(?:\.json)?|final\.html|content\.md)\b", re.I)),
    ("visible page-role narration", re.compile(r"\b(?:Gameplay Overview|Level Design|Developer)\s+page\b", re.I)),
    ("document-contract narration", re.compile(r"\b(?:three-page contract|document order remains|content lock)\b", re.I)),
    ("role-label dump", re.compile(r"\bGameplay Overview:\s.*\bLevel Design:\s.*\bDeveloper:", re.I | re.S)),
)
GENERIC_GLOBAL_RULE_RE = re.compile(r"^\s*Global Rule\s+\d+\s*$", re.I)
GENERIC_NOTE_RE = re.compile(r"^\s*Important(?:\s+(?:Build|Development))?\s+Note(?:\s+\d+)?\s*$", re.I)


def flow2_readiness(path: Path) -> tuple[bool, str]:
    ready, detail = _BASE_FLOW2_READINESS(path)
    if not ready:
        return ready, detail

    text = path.read_text(encoding="utf-8")
    preview_flags = PREVIEW_APPROVED_RE.findall(text)
    if len(preview_flags) > 1:
        return False, "intake-state.yaml must define preview_approved at most once"
    if preview_flags and preview_flags[0].lower() != "true":
        return False, "Flow 2 Simple Chat Preview is not approved: preview_approved=false"
    if preview_flags:
        return True, detail + "; Simple Chat Preview is approved"
    return True, detail


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


def _iter_strings(value: Any, path: str = "render_data") -> Iterable[tuple[str, str]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield from _iter_strings(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _iter_strings(child, f"{path}[{index}]")
    elif isinstance(value, str):
        yield path, value


def _note_errors(items: Any, context: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(items, list):
        return errors
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(
                f"{context}[{index}] must use a semantic title + description; "
                "plain note strings render as generic Important Note cards"
            )
            continue
        title = item.get("title") or item.get("label")
        description = item.get("description") or item.get("details") or item.get("note")
        title_text = str(title or "").strip()
        if GENERIC_NOTE_RE.fullmatch(title_text):
            errors.append(f"{context}[{index}].title is generic: {title_text!r}")
        if not title_text or not str(description or "").strip():
            errors.append(f"{context}[{index}] requires a semantic title and description")
    return errors


def content_purity_errors(data: dict[str, Any]) -> list[str]:
    """Reject observed AI-slop/process leakage before it reaches the final HTML.

    This is intentionally not a prose-quality or length score. It blocks only
    concrete process leakage and generic note-card behavior; semantic Humanize
    remains a Flow 4 review responsibility.
    """
    errors: list[str] = []

    # Project/process leakage: scan actual values, not field names.
    for path, text in _iter_strings(data):
        for label, pattern in PROCESS_LEAK_PATTERNS:
            if pattern.search(text):
                errors.append(f"{path}: {label}: {text[:180]!r}")
                break

    overview = data.get("overview")
    if isinstance(overview, dict):
        for index, item in enumerate(overview.get("main_systems", [])):
            if not isinstance(item, dict):
                continue
            title = str(item.get("title") or "").strip()
            if GENERIC_GLOBAL_RULE_RE.fullmatch(title):
                errors.append(
                    f"overview.main_systems[{index}].title is generic: {title!r}; "
                    "name the actual gameplay invariant"
                )

    for index, item in enumerate(data.get("global_development", [])):
        if isinstance(item, dict):
            errors.extend(_note_errors(item.get("notes"), f"global_development[{index}].notes"))

    for index, pkg in enumerate(data.get("packages", [])):
        if not isinstance(pkg, dict):
            continue
        level = pkg.get("level_design")
        developer = pkg.get("developer")
        if isinstance(level, dict):
            errors.extend(_note_errors(level.get("notes"), f"packages[{index}].level_design.notes"))
        if isinstance(developer, dict):
            errors.extend(_note_errors(developer.get("notes"), f"packages[{index}].developer.notes"))

    # Avoid noisy duplicates when one long value triggers the same practical issue.
    return list(dict.fromkeys(errors))


_engine.flow2_readiness = flow2_readiness
_engine.expected_page_ids = expected_page_ids
_engine.document_composition_errors = document_composition_errors


def validate(project: Path) -> dict[str, Any]:
    result = _engine.validate(project)

    data_path = project / "work" / "render-data.json"
    if not data_path.is_file():
        return result

    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        # Core validator already owns missing/invalid render-data reporting.
        return result
    if not isinstance(data, dict):
        return result

    purity = content_purity_errors(data)
    result.setdefault("checks", []).append(
        {
            "check": "content_purity",
            "status": "fail" if purity else "pass",
            "detail": "; ".join(purity) if purity else "no project/document-process leakage or generic note-card data detected",
        }
    )
    if purity:
        result.setdefault("errors", []).append("content_purity: " + "; ".join(purity))
        result["status"] = "fail"
    return result


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
