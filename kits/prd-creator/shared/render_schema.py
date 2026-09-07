from __future__ import annotations

from typing import Any


class ProjectionError(ValueError):
    """Raised when render-data does not match the canonical projection schema."""


TOP_LEVEL_FIELDS = {
    "approved_requirement_sha256",
    "canonical_content_sha256",
    "document",
    "overview",
    "gameplay_flow",
    "global_development",
    "packages",
}
DOCUMENT_FIELDS = {
    "title",
    "subtitle",
    "description",
    "document_type",
    "version",
    "brand",
    "brand_mark",
    "languages",
}
OVERVIEW_FIELDS = {
    "project_context",
    "main_experience",
    "document_scope",
    "intended_use",
    "facts",
    "journey",
    "main_systems",
}
FLOW_FIELDS = {"id", "title", "eyebrow", "narrative_context", "beats", "next_destination", "terms"}
GLOBAL_FIELDS = {"id", "title", "subtitle", "overview", "flow", "requirements", "notes", "terms"}
PACKAGE_FIELDS = {"id", "package_label", "title", "acceptance", "gameplay", "level_design", "developer", "terms"}
GAMEPLAY_FIELDS = {
    "context",
    "main_objective",
    "result",
    "purpose",
    "gameplay_time",
    "start_condition",
    "end_condition",
    "blocked_or_fail_condition",
    "result_model",
    "player_flow",
}
RESULT_MODEL_FIELDS = {"mode", "summary"}
LEVEL_FIELDS = {"overview", "flow", "requirements", "notes"}
DEVELOPER_FIELDS = {"overview", "flow", "requirements", "scoring", "completion_data", "reset", "reset_result", "notes"}
SCORING_FIELDS = {
    "produces_score",
    "score_name",
    "scale",
    "components",
    "formula",
    "summary",
    "timer_start",
    "timer_stop",
    "no_score_condition",
    "duplicate_prevention",
    "final_result_relationship",
    "player_facing_display",
    "telemetry_export",
}
COMPLETION_FIELDS = {
    "produces_score",
    "completion_name",
    "summary",
    "valid_completion_condition",
    "recorded_data",
    "interrupted_completion_behavior",
    "duplicate_prevention",
    "handoff_result",
    "final_result_relationship",
    "player_facing_display",
    "telemetry_export",
}
TERM_FIELDS = {"key", "label", "definition", "aliases", "roles"}


def validate_projection_schema(data: dict[str, Any]) -> None:
    """Validate the one supported render-data field shape.

    Projection data is already a resolved representation of canonical PRD meaning.
    Unknown keys, historical aliases, and renderer-side semantic synthesis are rejected
    here so downstream rendering stays deterministic and intentionally boring.
    """

    if not isinstance(data, dict):
        raise ProjectionError("render-data root must be an object")
    _allow_only(data, TOP_LEVEL_FIELDS, "render_data")
    _required_sha(data, "approved_requirement_sha256", "render_data")
    _required_sha(data, "canonical_content_sha256", "render_data")

    document = _mapping(data, "document", "render_data")
    _allow_only(document, DOCUMENT_FIELDS, "document")
    for field in ("title", "document_type", "version"):
        _required(document, field, "document")

    overview = _mapping(data, "overview", "render_data")
    _allow_only(overview, OVERVIEW_FIELDS, "overview")
    for field in ("project_context", "main_experience", "document_scope", "intended_use"):
        _required(overview, field, "overview")
    facts = _list(overview, "facts", "overview", nonempty=True)
    for index, fact in enumerate(facts):
        current = _as_mapping(fact, f"overview.facts[{index}]")
        _allow_only(current, {"key", "label", "value"}, f"overview.facts[{index}]")
        for field in ("key", "label", "value"):
            _required(current, field, f"overview.facts[{index}]")
    _validate_simple_flow(_list(overview, "journey", "overview", nonempty=True), "overview.journey")
    _validate_title_description_items(
        _list(overview, "main_systems", "overview", nonempty=True),
        "overview.main_systems",
    )

    gameplay_flow = _list(data, "gameplay_flow", "render_data", nonempty=True)
    for index, flow in enumerate(gameplay_flow):
        current = _as_mapping(flow, f"gameplay_flow[{index}]")
        _allow_only(current, FLOW_FIELDS, f"gameplay_flow[{index}]")
        for field in ("id", "title", "narrative_context", "next_destination"):
            _required(current, field, f"gameplay_flow[{index}]")
        beats = _list(current, "beats", f"gameplay_flow[{index}]", nonempty=True)
        _validate_title_description_items(beats, f"gameplay_flow[{index}].beats")
        _validate_terms(current.get("terms", []), f"gameplay_flow[{index}].terms")

    global_development = _list(data, "global_development", "render_data", nonempty=True)
    for index, section in enumerate(global_development):
        current = _as_mapping(section, f"global_development[{index}]")
        _allow_only(current, GLOBAL_FIELDS, f"global_development[{index}]")
        for field in ("id", "title", "overview"):
            _required(current, field, f"global_development[{index}]")
        _validate_simple_flow(
            _list(current, "flow", f"global_development[{index}]", nonempty=True),
            f"global_development[{index}].flow",
        )
        _validate_requirement_groups(
            _list(current, "requirements", f"global_development[{index}]", nonempty=True),
            f"global_development[{index}].requirements",
            kind="development",
        )
        _validate_notes(current.get("notes", []), f"global_development[{index}].notes")
        _validate_terms(current.get("terms", []), f"global_development[{index}].terms")

    packages = _list(data, "packages", "render_data", nonempty=True)
    seen_ids: set[str] = set()
    for package_index, package in enumerate(packages):
        current = _as_mapping(package, f"packages[{package_index}]")
        context = f"packages[{package_index}]"
        _allow_only(current, PACKAGE_FIELDS, context)
        for field in ("id", "title", "package_label"):
            _required(current, field, context)
        package_id = str(current["id"])
        if package_id in seen_ids:
            raise ProjectionError(f"duplicate package id: {package_id}")
        seen_ids.add(package_id)
        _list(current, "acceptance", context, nonempty=True)

        gameplay = _mapping(current, "gameplay", context)
        _allow_only(gameplay, GAMEPLAY_FIELDS, f"{context}.gameplay")
        for field in (
            "context",
            "main_objective",
            "result",
            "purpose",
            "gameplay_time",
            "start_condition",
            "end_condition",
            "blocked_or_fail_condition",
        ):
            _required(gameplay, field, f"{context}.gameplay")
        result_model = _mapping(gameplay, "result_model", f"{context}.gameplay")
        _allow_only(result_model, RESULT_MODEL_FIELDS, f"{context}.gameplay.result_model")
        mode = str(_required(result_model, "mode", f"{context}.gameplay.result_model")).strip()
        if mode not in {"scored", "completion_only"}:
            raise ProjectionError(f"{context}.gameplay.result_model.mode must be 'scored' or 'completion_only'")
        _required(result_model, "summary", f"{context}.gameplay.result_model")
        _validate_player_flow(
            _list(gameplay, "player_flow", f"{context}.gameplay", nonempty=True),
            f"{context}.gameplay.player_flow",
        )

        level = _mapping(current, "level_design", context)
        _allow_only(level, LEVEL_FIELDS, f"{context}.level_design")
        _required(level, "overview", f"{context}.level_design")
        _validate_simple_flow(
            _list(level, "flow", f"{context}.level_design", nonempty=True),
            f"{context}.level_design.flow",
        )
        _validate_requirement_groups(
            _list(level, "requirements", f"{context}.level_design", nonempty=True),
            f"{context}.level_design.requirements",
            kind="level",
        )
        _validate_notes(level.get("notes", []), f"{context}.level_design.notes")

        developer = _mapping(current, "developer", context)
        _allow_only(developer, DEVELOPER_FIELDS, f"{context}.developer")
        _required(developer, "overview", f"{context}.developer")
        _validate_simple_flow(
            _list(developer, "flow", f"{context}.developer", nonempty=True),
            f"{context}.developer.flow",
        )
        _validate_requirement_groups(
            _list(developer, "requirements", f"{context}.developer", nonempty=True),
            f"{context}.developer.requirements",
            kind="development",
        )
        _required(developer, "reset", f"{context}.developer")
        _required(developer, "reset_result", f"{context}.developer")
        _validate_notes(developer.get("notes", []), f"{context}.developer.notes")
        _validate_result_contract(developer, mode, f"{context}.developer")
        _validate_terms(current.get("terms", []), f"{context}.terms")


def _validate_result_contract(developer: dict[str, Any], mode: str, context: str) -> None:
    scoring = developer.get("scoring")
    completion = developer.get("completion_data")
    if mode == "scored":
        if not isinstance(scoring, dict) or completion not in (None, {}):
            raise ProjectionError(f"{context} must define scoring only when result_model.mode=scored")
        _allow_only(scoring, SCORING_FIELDS, f"{context}.scoring")
        if scoring.get("produces_score") is not True:
            raise ProjectionError(f"{context}.scoring.produces_score must be true")
        for field in (
            "score_name",
            "timer_start",
            "timer_stop",
            "no_score_condition",
            "duplicate_prevention",
            "final_result_relationship",
            "player_facing_display",
            "telemetry_export",
        ):
            _required(scoring, field, f"{context}.scoring")
        components = scoring.get("components")
        if components not in (None, []):
            if not isinstance(components, list):
                raise ProjectionError(f"{context}.scoring.components must be an array")
            for index, item in enumerate(components):
                component = _as_mapping(item, f"{context}.scoring.components[{index}]")
                _allow_only(component, {"name", "weight", "rule"}, f"{context}.scoring.components[{index}]")
                for field in ("name", "weight", "rule"):
                    _required(component, field, f"{context}.scoring.components[{index}]")
        elif not scoring.get("formula") and not scoring.get("summary"):
            raise ProjectionError(f"{context}.scoring requires components or explicit formula/summary")
        return

    if not isinstance(completion, dict) or scoring not in (None, {}):
        raise ProjectionError(f"{context} must define completion_data only when result_model.mode=completion_only")
    _allow_only(completion, COMPLETION_FIELDS, f"{context}.completion_data")
    if completion.get("produces_score") is not False:
        raise ProjectionError(f"{context}.completion_data.produces_score must be false")
    for field in (
        "completion_name",
        "valid_completion_condition",
        "recorded_data",
        "interrupted_completion_behavior",
        "duplicate_prevention",
        "handoff_result",
        "final_result_relationship",
        "player_facing_display",
        "telemetry_export",
    ):
        _required(completion, field, f"{context}.completion_data")


def _validate_simple_flow(items: list[Any], context: str) -> None:
    for index, item in enumerate(items):
        current = _as_mapping(item, f"{context}[{index}]")
        _allow_only(current, {"step", "title", "description"}, f"{context}[{index}]")
        for field in ("title", "description"):
            _required(current, field, f"{context}[{index}]")


def _validate_player_flow(items: list[Any], context: str) -> None:
    for index, item in enumerate(items):
        current = _as_mapping(item, f"{context}[{index}]")
        _allow_only(current, {"step", "title", "action", "result"}, f"{context}[{index}]")
        for field in ("title", "action", "result"):
            _required(current, field, f"{context}[{index}]")


def _validate_title_description_items(items: list[Any], context: str) -> None:
    for index, item in enumerate(items):
        current = _as_mapping(item, f"{context}[{index}]")
        _allow_only(current, {"title", "description"}, f"{context}[{index}]")
        for field in ("title", "description"):
            _required(current, field, f"{context}[{index}]")


def _validate_notes(value: Any, context: str) -> None:
    if value in (None, []):
        return
    if not isinstance(value, list):
        raise ProjectionError(f"{context} must be an array")
    _validate_title_description_items(value, context)


def _validate_requirement_groups(value: list[Any], context: str, *, kind: str) -> None:
    for group_index, group in enumerate(value):
        current_group = _as_mapping(group, f"{context}[{group_index}]")
        _allow_only(current_group, {"title", "items"}, f"{context}[{group_index}]")
        _required(current_group, "title", f"{context}[{group_index}]")
        items = _list(current_group, "items", f"{context}[{group_index}]", nonempty=True)
        for item_index, item in enumerate(items):
            current = _as_mapping(item, f"{context}[{group_index}].items[{item_index}]")
            item_context = f"{context}[{group_index}].items[{item_index}]"
            if kind == "level":
                _allow_only(
                    current,
                    {"code", "object", "subtitle", "area_size", "build_and_visual", "gameplay_function", "children"},
                    item_context,
                )
                for field in ("object", "area_size", "build_and_visual", "gameplay_function"):
                    _required(current, field, item_context)
                children = current.get("children", [])
                if children:
                    if not isinstance(children, list):
                        raise ProjectionError(f"{item_context}.children must be an array")
                    for child_index, child in enumerate(children):
                        child_map = _as_mapping(child, f"{item_context}.children[{child_index}]")
                        child_context = f"{item_context}.children[{child_index}]"
                        _allow_only(
                            child_map,
                            {"code", "object", "area_size", "build_and_visual", "gameplay_function"},
                            child_context,
                        )
                        for field in ("object", "area_size", "build_and_visual", "gameplay_function"):
                            _required(child_map, field, child_context)
            else:
                _allow_only(current, {"code", "title", "details", "result"}, item_context)
                for field in ("title", "details", "result"):
                    _required(current, field, item_context)


def _validate_terms(value: Any, context: str) -> None:
    if value in (None, []):
        return
    if not isinstance(value, list):
        raise ProjectionError(f"{context} must be an array")
    for index, item in enumerate(value):
        current = _as_mapping(item, f"{context}[{index}]")
        _allow_only(current, TERM_FIELDS, f"{context}[{index}]")
        for field in ("key", "label", "definition"):
            _required(current, field, f"{context}[{index}]")


def _allow_only(container: dict[str, Any], allowed: set[str], context: str) -> None:
    unknown = sorted(set(container) - allowed)
    if unknown:
        raise ProjectionError(f"{context} contains unsupported projection field(s): {', '.join(unknown)}")


def _as_mapping(value: Any, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ProjectionError(f"{context} must be an object")
    return value


def _mapping(container: dict[str, Any], key: str, context: str) -> dict[str, Any]:
    value = container.get(key)
    if not isinstance(value, dict):
        raise ProjectionError(f"{context}.{key} must be an object")
    return value


def _list(container: dict[str, Any], key: str, context: str, *, nonempty: bool = False) -> list[Any]:
    value = container.get(key)
    if not isinstance(value, list):
        raise ProjectionError(f"{context}.{key} must be an array")
    if nonempty and not value:
        raise ProjectionError(f"{context}.{key} must not be empty")
    return value


def _required(container: dict[str, Any], key: str, context: str) -> Any:
    if key not in container or container[key] in (None, "", [], {}):
        raise ProjectionError(f"{context}.{key} is required")
    return container[key]


def _required_sha(container: dict[str, Any], key: str, context: str) -> str:
    value = str(_required(container, key, context)).strip().casefold()
    if len(value) != 64 or any(char not in "0123456789abcdef" for char in value):
        raise ProjectionError(f"{context}.{key} must be a lowercase SHA-256 digest")
    return value
