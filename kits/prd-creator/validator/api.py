from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

from shared.issues import Issue
from shared.render_schema import validate_projection_schema

from . import prd_validation_engine as engine

PROCESS_LEAK_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("Golden HTML/reference language", re.compile(r"\bGolden\s+(?:HTML|Sample|Reference|page structure)\b", re.I)),
    ("PRD-Creator/internal artifact", re.compile(r"\b(?:PRD-Creator|render-data(?:\.json)?|final\.html|content\.md)\b", re.I)),
    ("visible page-role narration", re.compile(r"\b(?:Gameplay Overview|Level Design|Developer)\s+page\b", re.I)),
    ("document-contract narration", re.compile(r"\b(?:three-page contract|document order remains|content lock)\b", re.I)),
    ("role-label dump", re.compile(r"\bGameplay Overview:\s.*\bLevel Design:\s.*\bDeveloper:", re.I | re.S)),
)
GENERIC_GLOBAL_RULE_RE = re.compile(r"^\s*Global Rule\s+\d+\s*$", re.I)
GENERIC_NOTE_RE = re.compile(r"^\s*Important(?:\s+(?:Build|Development))?\s+Note(?:\s+\d+)?\s*$", re.I)


def _iter_strings(value: Any, path: str = "render_data") -> Iterable[tuple[str, str]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield from _iter_strings(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _iter_strings(child, f"{path}[{index}]")
    elif isinstance(value, str):
        yield path, value


def _localized_text(value: Any) -> str:
    if isinstance(value, dict):
        value = value.get("en") or value.get("id") or ""
    return str(value or "").strip()


def _note_errors(items: Any, context: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(items, list):
        return errors
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"{context}[{index}] must use a semantic title + description")
            continue
        title_text = _localized_text(item.get("title"))
        description_text = _localized_text(item.get("description"))
        if GENERIC_NOTE_RE.fullmatch(title_text):
            errors.append(f"{context}[{index}].title is generic: {title_text!r}")
        if not title_text or not description_text:
            errors.append(f"{context}[{index}] requires canonical title and description")
    return errors


def content_purity_errors(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
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
            title = _localized_text(item.get("title"))
            if GENERIC_GLOBAL_RULE_RE.fullmatch(title):
                errors.append(
                    f"overview.main_systems[{index}].title is generic: {title!r}; name the actual gameplay invariant"
                )

    for index, item in enumerate(data.get("global_development", [])):
        if isinstance(item, dict):
            errors.extend(_note_errors(item.get("notes"), f"global_development[{index}].notes"))

    for index, package in enumerate(data.get("packages", [])):
        if not isinstance(package, dict):
            continue
        level = package.get("level_design")
        developer = package.get("developer")
        if isinstance(level, dict):
            errors.extend(_note_errors(level.get("notes"), f"packages[{index}].level_design.notes"))
        if isinstance(developer, dict):
            errors.extend(_note_errors(developer.get("notes"), f"packages[{index}].developer.notes"))
    return list(dict.fromkeys(errors))


def _append_check(
    result: dict[str, Any],
    name: str,
    errors: list[str],
    success: str,
    *,
    issue: Issue | None = None,
) -> None:
    result.setdefault("checks", []).append(
        {
            "check": name,
            "status": "fail" if errors else "pass",
            "detail": "; ".join(errors) if errors else success,
        }
    )
    if errors:
        result.setdefault("errors", []).append(f"{name}: " + "; ".join(errors))
        if issue is not None:
            result.setdefault("issues", []).append(issue.as_dict())
        result["status"] = "fail"


def validate(project: Path) -> dict[str, Any]:
    """Run the one canonical complete mechanical PRD validation pipeline."""
    project = project.resolve()
    result = engine.validate(project)
    data_path = project / "work" / "render-data.json"
    if not data_path.is_file():
        return result
    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return result
    if not isinstance(data, dict):
        return result

    projection_errors: list[str] = []
    try:
        validate_projection_schema(data)
    except ValueError as exc:
        projection_errors.append(str(exc))
    _append_check(
        result,
        "canonical_projection_schema",
        projection_errors,
        "render-data uses one canonical field shape with no retired compatibility aliases",
        issue=Issue(
            "PRD_PROJECTION_SCHEMA_INVALID",
            "flow3.projection",
            "; ".join(projection_errors) or "render-data projection schema is invalid",
            path="work/render-data.json",
        ),
    )

    requirement_path = project / "state" / "requirement-register.yaml"
    requirement_binding_errors: list[str] = []
    if not requirement_path.is_file():
        requirement_binding_errors.append("state/requirement-register.yaml is missing")
    else:
        actual_requirement_sha = hashlib.sha256(requirement_path.read_bytes()).hexdigest()
        declared_requirement_sha = str(data.get("approved_requirement_sha256") or "").strip().casefold()
        if declared_requirement_sha != actual_requirement_sha:
            requirement_binding_errors.append(
                "render-data.approved_requirement_sha256 does not match the exact current approved requirement-register bytes"
            )
    _append_check(
        result,
        "render_data_matches_approved_requirements",
        requirement_binding_errors,
        "render-data is bound to the exact approved Flow 2 requirement revision",
        issue=Issue(
            "PRD_PROJECTION_REQUIREMENT_STALE",
            "flow3.projection",
            "; ".join(requirement_binding_errors)
            or "render-data is stale relative to the approved requirement revision",
            path="work/render-data.json",
            field="approved_requirement_sha256",
        ),
    )

    purity = content_purity_errors(data)
    _append_check(
        result,
        "content_purity",
        purity,
        "no project/document-process leakage or generic note-card data detected",
        issue=Issue(
            "PRD_CONTENT_PURITY_FAILED",
            "flow3.content",
            "; ".join(purity) or "visible project content contains process leakage",
            path="work/render-data.json",
        ),
    )
    return result
