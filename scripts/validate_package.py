#!/usr/bin/env python3
"""Validate Production Document Builder YAML/JSON files.

Structural validation uses JSON Schema Draft 2020-12.
Semantic validation checks rules that JSON Schema cannot express safely.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any, Iterable

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource


SCHEMA_BY_BASENAME = {
    "project-state.yaml": "project-state.schema.json",
    "project-state.json": "project-state.schema.json",
    "decision-log.yaml": "decision-log.schema.json",
    "decision-log.json": "decision-log.schema.json",
    "assumptions.yaml": "assumptions.schema.json",
    "assumptions.json": "assumptions.schema.json",
    "project-content.yaml": "project-content.schema.json",
    "project-content.json": "project-content.schema.json",
    "complete-game-map.yaml": "project-content.schema.json",
    "complete-game-map.json": "project-content.schema.json",
    "multi-stage-game.yaml": "project-content.schema.json",
    "multi-stage-game.json": "project-content.schema.json",
    "single-gameplay.yaml": "project-content.schema.json",
    "single-gameplay.json": "project-content.schema.json",
    "game-system-module.yaml": "project-content.schema.json",
    "game-system-module.json": "project-content.schema.json",
    "specialized-gameplay-design.yaml": "project-content.schema.json",
    "specialized-level-design.yaml": "project-content.schema.json",
    "specialized-developer.yaml": "project-content.schema.json",
    "specialized-scoring-data.yaml": "project-content.schema.json",
    "specialized-audit.yaml": "project-content.schema.json",
    "scoring.yaml": "scoring.schema.json",
    "scoring.json": "scoring.schema.json",
    "completion-data.yaml": "completion-data.schema.json",
    "completion-data.json": "completion-data.schema.json",
    "glossary.yaml": "glossary.schema.json",
    "glossary.json": "glossary.schema.json",
    "audit-report.yaml": "audit-report.schema.json",
    "audit-report.json": "audit-report.schema.json",
    "render-report.yaml": "render-report.schema.json",
    "render-report.json": "render-report.schema.json",
    "manifest.yaml": "manifest.schema.json",
    "manifest.json": "manifest.schema.json",
}


class ValidationIssue:
    def __init__(self, code: str, message: str, path: str = "$") -> None:
        self.code = code
        self.message = message
        self.path = path

    def __str__(self) -> str:
        return f"[{self.code}] {self.path}: {self.message}"


def load_data(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RuntimeError(f"Cannot read {path}: {exc}") from exc

    try:
        if path.suffix.lower() == ".json":
            return json.loads(text)
        return yaml.safe_load(text)
    except (json.JSONDecodeError, yaml.YAMLError) as exc:
        raise RuntimeError(f"Cannot parse {path}: {exc}") from exc


def load_schemas(schema_dir: Path) -> tuple[dict[str, dict[str, Any]], Registry]:
    schemas: dict[str, dict[str, Any]] = {}
    resources: list[tuple[str, Resource[Any]]] = []

    for path in sorted(schema_dir.glob("*.json")):
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        schema_id = schema.get("$id")
        if not schema_id:
            raise RuntimeError(f"Schema has no $id: {path}")
        if schema_id in schemas:
            raise RuntimeError(f"Duplicate schema $id: {schema_id}")
        schemas[schema_id] = schema
        resources.append((schema_id, Resource.from_contents(schema)))

    return schemas, Registry().with_resources(resources)


def path_text(error_path: Iterable[Any]) -> str:
    result = "$"
    for part in error_path:
        if isinstance(part, int):
            result += f"[{part}]"
        else:
            result += f".{part}"
    return result


def structural_issues(
    data: Any,
    schema_id: str,
    schemas: dict[str, dict[str, Any]],
    registry: Registry,
) -> list[ValidationIssue]:
    if schema_id not in schemas:
        return [ValidationIssue("UNKNOWN_SCHEMA", f"Schema not found: {schema_id}")]

    validator = Draft202012Validator(
        schemas[schema_id],
        registry=registry,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
    errors = sorted(
        validator.iter_errors(data),
        key=lambda err: (list(err.absolute_path), err.message),
    )
    return [
        ValidationIssue("SCHEMA", error.message, path_text(error.absolute_path))
        for error in errors
    ]


def duplicate_values(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def iter_section_leaves(node: Any, path: str = "$.sections") -> Iterable[tuple[str, dict[str, Any]]]:
    if not isinstance(node, dict):
        return
    if "status" in node:
        yield path, node
        return
    for key, value in node.items():
        yield from iter_section_leaves(value, f"{path}.{key}")


def semantic_scoring(data: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    scale = data.get("scale", {})
    minimum = scale.get("minimum")
    maximum = scale.get("maximum")
    if isinstance(minimum, (int, float)) and isinstance(maximum, (int, float)):
        if minimum >= maximum:
            issues.append(
                ValidationIssue(
                    "SCORE_RANGE",
                    "Score minimum must be lower than score maximum.",
                    "$.scale",
                )
            )

    components = data.get("components", [])
    weights = [item.get("weight") for item in components if isinstance(item, dict)]
    if weights and all(isinstance(weight, (int, float)) for weight in weights):
        total = sum(weights)
        if not math.isclose(total, 100.0, abs_tol=1e-9):
            issues.append(
                ValidationIssue(
                    "SCORE_WEIGHT_TOTAL",
                    f"Score component weights total {total:g}%; expected 100%.",
                    "$.components",
                )
            )

    ids = [item.get("id") for item in components if isinstance(item, dict) and item.get("id")]
    for duplicate in sorted(duplicate_values(ids)):
        issues.append(
            ValidationIssue(
                "DUPLICATE_COMPONENT_ID",
                f"Duplicate score component ID: {duplicate}",
                "$.components",
            )
        )

    for index, item in enumerate(data.get("critical_inputs", [])):
        if not isinstance(item, dict):
            continue
        if item.get("blocking") and item.get("status") != "approved":
            issues.append(
                ValidationIssue(
                    "OPEN_SCORING_INPUT",
                    "A blocking scoring input is not approved.",
                    f"$.critical_inputs[{index}]",
                )
            )
    return issues


def semantic_decisions(data: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    decisions = data.get("decisions", [])
    ids = [item.get("id") for item in decisions if isinstance(item, dict) and item.get("id")]
    id_set = set(ids)

    for duplicate in sorted(duplicate_values(ids)):
        issues.append(
            ValidationIssue(
                "DUPLICATE_DECISION_ID",
                f"Duplicate Decision ID: {duplicate}",
                "$.decisions",
            )
        )

    approved_topics: dict[tuple[str, str], str] = {}
    for index, item in enumerate(decisions):
        if not isinstance(item, dict):
            continue
        decision_id = item.get("id", f"index-{index}")
        status = item.get("status")
        key = (str(item.get("scope")), str(item.get("topic")))

        if status == "approved":
            previous = approved_topics.get(key)
            if previous:
                issues.append(
                    ValidationIssue(
                        "DUPLICATE_APPROVED_TOPIC",
                        f"Two active approved decisions exist for {key[0]}/{key[1]}: "
                        f"{previous} and {decision_id}.",
                        f"$.decisions[{index}]",
                    )
                )
            else:
                approved_topics[key] = decision_id

        superseded_by = item.get("superseded_by")
        if superseded_by and superseded_by not in id_set:
            issues.append(
                ValidationIssue(
                    "UNKNOWN_SUPERSEDING_DECISION",
                    f"superseded_by references unknown Decision ID: {superseded_by}",
                    f"$.decisions[{index}].superseded_by",
                )
            )

        supersedes = item.get("supersedes")
        if supersedes and supersedes not in id_set:
            issues.append(
                ValidationIssue(
                    "UNKNOWN_SUPERSEDED_DECISION",
                    f"supersedes references unknown Decision ID: {supersedes}",
                    f"$.decisions[{index}].supersedes",
                )
            )
    return issues


def semantic_assumptions(data: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    assumptions = data.get("assumptions", [])
    ids = [item.get("id") for item in assumptions if isinstance(item, dict) and item.get("id")]
    for duplicate in sorted(duplicate_values(ids)):
        issues.append(
            ValidationIssue(
                "DUPLICATE_ASSUMPTION_ID",
                f"Duplicate Assumption ID: {duplicate}",
                "$.assumptions",
            )
        )
    return issues


def semantic_glossary(data: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    terms = data.get("terms", [])
    ids = [item.get("id") for item in terms if isinstance(item, dict) and item.get("id")]

    for duplicate in sorted(duplicate_values(ids)):
        issues.append(
            ValidationIssue(
                "DUPLICATE_TERM_ID",
                f"Duplicate glossary term ID: {duplicate}",
                "$.terms",
            )
        )

    owner: dict[tuple[str, str, str], tuple[str, str]] = {}
    for index, item in enumerate(terms):
        if not isinstance(item, dict):
            continue
        scope = str(item.get("scope", ""))
        term_id = str(item.get("id", f"index-{index}"))
        term = item.get("term", {})
        definition = item.get("definition", {})
        aliases = item.get("aliases", {})

        for language in ("id", "en"):
            candidates: list[str] = []
            if isinstance(term, dict) and term.get(language):
                candidates.append(str(term[language]))
            if isinstance(aliases, dict):
                candidates.extend(str(value) for value in aliases.get(language, []))

            for candidate in candidates:
                key = (scope.casefold(), language, candidate.strip().casefold())
                current_definition = str(definition.get(language, "")).strip()
                if key in owner:
                    previous_id, previous_definition = owner[key]
                    if previous_id != term_id:
                        if previous_definition != current_definition:
                            issues.append(
                                ValidationIssue(
                                    "GLOSSARY_COLLISION",
                                    f"'{candidate}' has conflicting definitions in scope "
                                    f"'{scope}' ({previous_id} and {term_id}).",
                                    f"$.terms[{index}]",
                                )
                            )
                        else:
                            issues.append(
                                ValidationIssue(
                                    "GLOSSARY_DUPLICATE_LABEL",
                                    f"'{candidate}' is assigned to multiple term IDs in scope "
                                    f"'{scope}' ({previous_id} and {term_id}).",
                                    f"$.terms[{index}]",
                                )
                            )
                else:
                    owner[key] = (term_id, current_definition)
    return issues


def semantic_project_state(data: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    workflow = data.get("workflow", {})
    questions = data.get("open_questions", [])
    blockers = data.get("blockers", [])
    errors = data.get("errors", [])

    question_ids = {item.get("id") for item in questions if isinstance(item, dict)}
    error_ids = {item.get("id") for item in errors if isinstance(item, dict)}
    valid_sources = question_ids | error_ids

    for index, blocker in enumerate(blockers):
        if isinstance(blocker, dict) and blocker.get("source") not in valid_sources:
            issues.append(
                ValidationIssue(
                    "UNKNOWN_BLOCKER_SOURCE",
                    f"Blocker source does not exist: {blocker.get('source')}",
                    f"$.blockers[{index}].source",
                )
            )

    if workflow.get("content_frozen"):
        if workflow.get("content_status") != "frozen":
            issues.append(
                ValidationIssue(
                    "FROZEN_STATUS_MISMATCH",
                    "content_frozen is true but content_status is not frozen.",
                    "$.workflow",
                )
            )
        if blockers:
            issues.append(
                ValidationIssue(
                    "FROZEN_WITH_BLOCKERS",
                    "Frozen content cannot contain active blockers.",
                    "$.blockers",
                )
            )
        for index, question in enumerate(questions):
            if isinstance(question, dict) and question.get("blocking") and question.get("status") not in {"closed", "approved"}:
                issues.append(
                    ValidationIssue(
                        "FROZEN_WITH_BLOCKING_QUESTION",
                        "Frozen content contains an unresolved blocking question.",
                        f"$.open_questions[{index}]",
                    )
                )
        for index, error in enumerate(errors):
            if isinstance(error, dict) and error.get("blocking") and error.get("status") != "resolved":
                issues.append(
                    ValidationIssue(
                        "FROZEN_WITH_BLOCKING_ERROR",
                        "Frozen content contains an unresolved blocking error.",
                        f"$.errors[{index}]",
                    )
                )
        for path, section in iter_section_leaves(data.get("sections", {})):
            if section.get("status") not in {"approved", "frozen"}:
                issues.append(
                    ValidationIssue(
                        "FROZEN_WITH_UNREADY_SECTION",
                        f"Section status is {section.get('status')}; expected approved or frozen.",
                        path,
                    )
                )

    if workflow.get("html_status") == "approved" and workflow.get("final_status") == "not_approved":
        issues.append(
            ValidationIssue(
                "HTML_FINAL_STATUS_MISMATCH",
                "Approved HTML cannot have final_status not_approved.",
                "$.workflow",
            )
        )

    if workflow.get("final_status") != "delivered" and data.get("next_step") is None:
        issues.append(
            ValidationIssue(
                "MISSING_NEXT_STEP",
                "A non-delivered project must have one primary next_step.",
                "$.next_step",
            )
        )
    return issues


def collect_packages(data: dict[str, Any]) -> list[dict[str, Any]]:
    development = data.get("development", {})
    result: list[dict[str, Any]] = []
    if not isinstance(development, dict):
        return result
    for key in ("packages", "stage_packages"):
        value = development.get(key)
        if isinstance(value, list):
            result.extend(item for item in value if isinstance(item, dict))
    gameplay_package = development.get("gameplay_package")
    if isinstance(gameplay_package, dict):
        result.append(gameplay_package)
    return result


def iter_source_refs(node: Any, path: str = "$") -> Iterable[tuple[str, dict[str, Any]]]:
    if isinstance(node, dict):
        refs = node.get("source_refs")
        if isinstance(refs, list):
            for index, ref in enumerate(refs):
                if isinstance(ref, dict):
                    yield f"{path}.source_refs[{index}]", ref
        for key, value in node.items():
            if key != "source_refs":
                yield from iter_source_refs(value, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from iter_source_refs(value, f"{path}[{index}]")


def iter_term_refs(node: Any, path: str = "$") -> Iterable[tuple[str, str]]:
    if isinstance(node, dict):
        terms = node.get("terms")
        if isinstance(terms, list):
            for index, term_id in enumerate(terms):
                if isinstance(term_id, str):
                    yield f"{path}.terms[{index}]", term_id
        for key, value in node.items():
            if key != "terms":
                yield from iter_term_refs(value, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from iter_term_refs(value, f"{path}[{index}]")


def semantic_project_content(
    data: dict[str, Any],
    assumptions: dict[str, Any] | None = None,
    glossary: dict[str, Any] | None = None,
    decisions: dict[str, Any] | None = None,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    packages = collect_packages(data)
    package_ids = [item.get("id") for item in packages if item.get("id")]
    package_id_set = set(package_ids)

    for duplicate in sorted(duplicate_values(package_ids)):
        issues.append(
            ValidationIssue(
                "DUPLICATE_PACKAGE_ID",
                f"Duplicate package ID: {duplicate}",
                "$.development",
            )
        )

    for index, package in enumerate(packages):
        target = package.get("handoff_to")
        if target and target not in package_id_set:
            issues.append(
                ValidationIssue(
                    "UNKNOWN_HANDOFF_TARGET",
                    f"Package handoff_to references unknown package: {target}",
                    f"$.development.packages[{index}].handoff_to",
                )
            )

    flow = data.get("gameplay_flow", [])
    flow_ids = [item.get("id") for item in flow if isinstance(item, dict) and item.get("id")]
    for duplicate in sorted(duplicate_values(flow_ids)):
        issues.append(
            ValidationIssue(
                "DUPLICATE_FLOW_ID",
                f"Duplicate Gameplay Flow ID: {duplicate}",
                "$.gameplay_flow",
            )
        )

    overview = data.get("overview")
    if isinstance(overview, dict):
        known_journey = set(flow_ids) | package_id_set
        for index, journey_id in enumerate(overview.get("journey_overview", [])):
            if journey_id not in known_journey:
                issues.append(
                    ValidationIssue(
                        "UNKNOWN_JOURNEY_ITEM",
                        f"Journey item is not present in Gameplay Flow or packages: {journey_id}",
                        f"$.overview.journey_overview[{index}]",
                    )
                )

    if data.get("document", {}).get("status") == "frozen" and assumptions is not None:
        assumption_status = {
            item.get("id"): item.get("status")
            for item in assumptions.get("assumptions", [])
            if isinstance(item, dict)
        }
        for path, ref in iter_source_refs(data):
            if ref.get("type") == "assumption":
                ref_id = ref.get("ref")
                if assumption_status.get(ref_id) != "confirmed":
                    issues.append(
                        ValidationIssue(
                            "UNCONFIRMED_ASSUMPTION_IN_FROZEN_CONTENT",
                            f"Frozen content references unconfirmed assumption: {ref_id}",
                            path,
                        )
                    )

    if glossary is not None:
        term_ids = {
            item.get("id")
            for item in glossary.get("terms", [])
            if isinstance(item, dict) and item.get("id")
        }
        for path, term_id in iter_term_refs(data):
            if term_id not in term_ids:
                issues.append(
                    ValidationIssue(
                        "UNKNOWN_GLOSSARY_TERM",
                        f"Content references unknown glossary term: {term_id}",
                        path,
                    )
                )

    if decisions is not None:
        decision_ids = {
            item.get("id")
            for item in decisions.get("decisions", [])
            if isinstance(item, dict) and item.get("id")
        }
        for path, ref in iter_source_refs(data):
            if ref.get("type") == "decision" and ref.get("ref") not in decision_ids:
                issues.append(
                    ValidationIssue(
                        "UNKNOWN_DECISION_REF",
                        f"Content references unknown Decision ID: {ref.get('ref')}",
                        path,
                    )
                )

    score_names: list[str] = []
    for package in packages:
        developer = package.get("developer")
        if not isinstance(developer, dict):
            continue
        score = developer.get("scoring")
        if isinstance(score, dict):
            score_names.append(json.dumps(score.get("score_name", {}), sort_keys=True))
            issues.extend(semantic_scoring(score))
    for duplicate in sorted(duplicate_values(score_names)):
        issues.append(
            ValidationIssue(
                "DUPLICATE_SCORE_NAME",
                f"Duplicate score name in project: {duplicate}",
                "$.development",
            )
        )
    return issues


def semantic_audit_report(data: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    findings = data.get("findings", [])
    summary = data.get("summary", {})
    counts = {"critical": 0, "major": 0, "minor": 0, "suggestion": 0}
    for finding in findings:
        if not isinstance(finding, dict):
            continue
        severity = finding.get("severity")
        if severity in counts and finding.get("status") not in {"resolved", "rejected", "replaced"}:
            counts[severity] += 1
    for key, count in counts.items():
        if summary.get(key) != count:
            issues.append(
                ValidationIssue(
                    "AUDIT_SUMMARY_MISMATCH",
                    f"summary.{key} is {summary.get(key)} but active findings contain {count}.",
                    f"$.summary.{key}",
                )
            )
    status = data.get("audit", {}).get("status")
    if status == "passed" and (summary.get("critical", 0) or summary.get("major", 0)):
        issues.append(
            ValidationIssue(
                "AUDIT_PASSED_WITH_BLOCKERS",
                "Audit status cannot be passed while Critical or Major findings remain.",
                "$.audit.status",
            )
        )
    return issues


def semantic_render_report(data: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    status = data.get("render", {}).get("status")
    structure = data.get("structure", {})
    content = data.get("content", {})
    languages = data.get("languages", {})
    glossary = data.get("glossary", {})
    if status == "success":
        blockers = {
            "missing required sections": content.get("missing_required_sections", 0),
            "unresolved placeholders": content.get("unresolved_placeholders", 0),
            "missing Indonesian translations": languages.get("id_missing", 0),
            "missing English translations": languages.get("en_missing", 0),
            "unmatched critical terms": glossary.get("unmatched_critical_terms", 0),
            "duplicate IDs": structure.get("duplicate_ids", 0),
            "broken links": structure.get("broken_links", 0),
            "unreachable pages": structure.get("unreachable_pages", 0),
        }
        for label, count in blockers.items():
            if isinstance(count, int) and count > 0:
                issues.append(
                    ValidationIssue(
                        "SUCCESS_WITH_RENDER_BLOCKER",
                        f"Render status is success but {label} = {count}.",
                        "$.render.status",
                    )
                )
    return issues


def semantic_manifest(data: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    required_pages = {"gameplay_overview", "level_design", "developer"}
    pages = set(data.get("content_benchmark", {}).get("pages", []))
    if data.get("content_benchmark", {}).get("package") == "quarry" and pages != required_pages:
        issues.append(
            ValidationIssue(
                "INCOMPLETE_QUARRY_BENCHMARK",
                "The Quarry benchmark must cover gameplay_overview, level_design, and developer.",
                "$.content_benchmark.pages",
            )
        )
    return issues


def semantic_issues(
    schema_id: str,
    data: dict[str, Any],
    context: dict[str, dict[str, Any]] | None = None,
) -> list[ValidationIssue]:
    context = context or {}
    if schema_id == "scoring.schema.json":
        return semantic_scoring(data)
    if schema_id == "decision-log.schema.json":
        return semantic_decisions(data)
    if schema_id == "assumptions.schema.json":
        return semantic_assumptions(data)
    if schema_id == "glossary.schema.json":
        return semantic_glossary(data)
    if schema_id == "project-state.schema.json":
        return semantic_project_state(data)
    if schema_id == "project-content.schema.json":
        return semantic_project_content(
            data,
            assumptions=context.get("assumptions"),
            glossary=context.get("glossary"),
            decisions=context.get("decisions"),
        )
    if schema_id == "audit-report.schema.json":
        return semantic_audit_report(data)
    if schema_id == "render-report.schema.json":
        return semantic_render_report(data)
    if schema_id == "manifest.schema.json":
        return semantic_manifest(data)
    return []


def validate_data(
    data: Any,
    schema_id: str,
    schemas: dict[str, dict[str, Any]],
    registry: Registry,
    context: dict[str, dict[str, Any]] | None = None,
) -> list[ValidationIssue]:
    structural = structural_issues(data, schema_id, schemas, registry)
    if structural:
        return structural
    if not isinstance(data, dict):
        return [ValidationIssue("ROOT_TYPE", "Root value must be an object.")]
    return semantic_issues(schema_id, data, context=context)


def detect_schema(path: Path) -> str | None:
    return SCHEMA_BY_BASENAME.get(path.name)


def find_workspace_file(root: Path, names: list[str]) -> Path | None:
    candidates: list[Path] = []
    for name in names:
        candidates.extend(
            [
                root / name,
                root / "state" / name,
                root / "content" / name,
                root / "audits" / name,
                root / "output" / name,
            ]
        )
    for path in candidates:
        if path.is_file():
            return path
    return None


def validate_workspace(
    root: Path,
    schemas: dict[str, dict[str, Any]],
    registry: Registry,
) -> list[tuple[Path, list[ValidationIssue]]]:
    files = {
        "project_state": find_workspace_file(root, ["project-state.yaml", "project-state.json"]),
        "decisions": find_workspace_file(root, ["decision-log.yaml", "decision-log.json"]),
        "assumptions": find_workspace_file(root, ["assumptions.yaml", "assumptions.json"]),
        "project_content": find_workspace_file(root, ["project-content.yaml", "project-content.json"]),
        "glossary": find_workspace_file(root, ["glossary.yaml", "glossary.json"]),
        "manifest": find_workspace_file(root, ["manifest.yaml", "manifest.json"]),
    }

    loaded: dict[str, dict[str, Any]] = {}
    for key, path in files.items():
        if path is not None:
            data = load_data(path)
            if isinstance(data, dict):
                loaded[key] = data

    context = {
        "assumptions": loaded.get("assumptions", {}),
        "glossary": loaded.get("glossary", {}),
        "decisions": loaded.get("decisions", {}),
    }

    results: list[tuple[Path, list[ValidationIssue]]] = []
    for key, path in files.items():
        if path is None:
            continue
        schema_id = detect_schema(path)
        if schema_id is None:
            continue
        issues = validate_data(load_data(path), schema_id, schemas, registry, context=context)
        results.append((path, issues))
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--schema-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "schemas",
        help="Directory containing JSON Schema files.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    file_parser = subparsers.add_parser("file", help="Validate one YAML or JSON file.")
    file_parser.add_argument("path", type=Path)
    file_parser.add_argument("--schema", help="Schema ID. Detected from filename when omitted.")
    file_parser.add_argument("--assumptions", type=Path)
    file_parser.add_argument("--glossary", type=Path)
    file_parser.add_argument("--decisions", type=Path)

    workspace_parser = subparsers.add_parser("workspace", help="Validate a project workspace.")
    workspace_parser.add_argument("path", type=Path)

    args = parser.parse_args()

    try:
        schemas, registry = load_schemas(args.schema_dir)

        if args.command == "file":
            schema_id = args.schema or detect_schema(args.path)
            if not schema_id:
                print("ERROR: Could not detect schema. Use --schema.", file=sys.stderr)
                return 2
            context: dict[str, dict[str, Any]] = {}
            for key in ("assumptions", "glossary", "decisions"):
                context_path = getattr(args, key)
                if context_path:
                    loaded = load_data(context_path)
                    if isinstance(loaded, dict):
                        context[key] = loaded
            issues = validate_data(
                load_data(args.path),
                schema_id,
                schemas,
                registry,
                context=context,
            )
            if issues:
                print(f"FAILED: {args.path}")
                for issue in issues:
                    print(f"- {issue}")
                return 1
            print(f"PASSED: {args.path}")
            return 0

        results = validate_workspace(args.path, schemas, registry)
        if not results:
            print("FAILED: No recognized workspace files found.")
            return 1

        failed = False
        for path, issues in results:
            if issues:
                failed = True
                print(f"FAILED: {path}")
                for issue in issues:
                    print(f"- {issue}")
            else:
                print(f"PASSED: {path}")
        return 1 if failed else 0

    except (RuntimeError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
