from __future__ import annotations

from typing import Any


class ProjectionError(ValueError):
    """Raised when render-data does not match the canonical projection schema."""


def validate_projection_schema(data: dict[str, Any]) -> None:
    """Validate the one supported render-data field shape.

    This is intentionally narrower than the historical renderer helpers. A valid
    projection must already contain the meaning needed by presentation; renderer-side
    alias recovery or cross-role semantic synthesis is not part of the contract.
    """

    if not isinstance(data, dict):
        raise ProjectionError("render-data root must be an object")

    document = _mapping(data, "document", "render_data")
    _reject_keys(document, {"map_type"}, "document")
    for field in ("title", "document_type", "version"):
        _required(document, field, "document")

    overview = _mapping(data, "overview", "render_data")
    for field in ("project_context", "main_experience", "document_scope", "intended_use"):
        _required(overview, field, "overview")
    facts = _list(overview, "facts", "overview", nonempty=True)
    for index, fact in enumerate(facts):
        current = _as_mapping(fact, f"overview.facts[{index}]")
        for field in ("key", "label", "value"):
            _required(current, field, f"overview.facts[{index}]")
    _validate_simple_flow(_list(overview, "journey", "overview", nonempty=True), "overview.journey")
    systems = _list(overview, "main_systems", "overview", nonempty=True)
    _validate_title_description_items(systems, "overview.main_systems")

    gameplay_flow = _list(data, "gameplay_flow", "render_data", nonempty=True)
    for index, flow in enumerate(gameplay_flow):
        current = _as_mapping(flow, f"gameplay_flow[{index}]")
        _reject_keys(current, {"display_title", "context_label"}, f"gameplay_flow[{index}]")
        for field in ("id", "title", "narrative_context", "next_destination"):
            _required(current, field, f"gameplay_flow[{index}]")
        beats = _list(current, "beats", f"gameplay_flow[{index}]", nonempty=True)
        _validate_title_description_items(beats, f"gameplay_flow[{index}].beats")
        _validate_terms(current.get("terms", []), f"gameplay_flow[{index}].terms")

    global_development = _list(data, "global_development", "render_data", nonempty=True)
    for index, section in enumerate(global_development):
        current = _as_mapping(section, f"global_development[{index}]")
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
        for field in ("id", "title", "package_label"):
            _required(current, field, context)
        package_id = str(current["id"])
        if package_id in seen_ids:
            raise ProjectionError(f"duplicate package id: {package_id}")
        seen_ids.add(package_id)
        _list(current, "acceptance", context, nonempty=True)

        gameplay = _mapping(current, "gameplay", context)
        _reject_keys(
            gameplay,
            {"overview", "game_purpose", "estimated_time", "duration", "scoring_summary"},
            f"{context}.gameplay",
        )
        for field in (
            "context",
            "main_objective",
            "result",
            "purpose",
            "gameplay_time",
            "start_condition",
            "end_condition",
            "blocked_or_fail_condition",
            "scoring_criteria",
        ):
            _required(gameplay, field, f"{context}.gameplay")
        _validate_player_flow(
            _list(gameplay, "player_flow", f"{context}.gameplay", nonempty=True),
            f"{context}.gameplay.player_flow",
        )

        level = _mapping(current, "level_design", context)
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

        _validate_terms(current.get("terms", []), f"{context}.terms")


def _validate_simple_flow(items: list[Any], context: str) -> None:
    for index, item in enumerate(items):
        current = _as_mapping(item, f"{context}[{index}]")
        _reject_keys(current, {"stage", "trigger", "details", "action", "behavior"}, f"{context}[{index}]")
        for field in ("title", "description"):
            _required(current, field, f"{context}[{index}]")


def _validate_player_flow(items: list[Any], context: str) -> None:
    for index, item in enumerate(items):
        current = _as_mapping(item, f"{context}[{index}]")
        _reject_keys(current, {"stage", "description", "details", "behavior"}, f"{context}[{index}]")
        for field in ("title", "action", "result"):
            _required(current, field, f"{context}[{index}]")


def _validate_title_description_items(items: list[Any], context: str) -> None:
    for index, item in enumerate(items):
        current = _as_mapping(item, f"{context}[{index}]")
        _reject_keys(current, {"label", "details", "note"}, f"{context}[{index}]")
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
        _reject_keys(current_group, {"group_title", "objects"}, f"{context}[{group_index}]")
        _required(current_group, "title", f"{context}[{group_index}]")
        items = _list(current_group, "items", f"{context}[{group_index}]", nonempty=True)
        for item_index, item in enumerate(items):
            current = _as_mapping(item, f"{context}[{group_index}].items[{item_index}]")
            item_context = f"{context}[{group_index}].items[{item_index}]"
            if kind == "level":
                _reject_keys(
                    current,
                    {"title", "size", "dimensions", "requirements", "details", "result"},
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
                        _reject_keys(
                            child_map,
                            {"title", "size", "requirements", "details", "result"},
                            f"{item_context}.children[{child_index}]",
                        )
                        for field in ("object", "area_size", "build_and_visual", "gameplay_function"):
                            _required(child_map, field, f"{item_context}.children[{child_index}]")
            else:
                _reject_keys(
                    current,
                    {"requirement", "requirements", "expected_result", "gameplay_function", "object"},
                    item_context,
                )
                for field in ("title", "details", "result"):
                    _required(current, field, item_context)


def _validate_terms(value: Any, context: str) -> None:
    if value in (None, []):
        return
    if not isinstance(value, list):
        raise ProjectionError(f"{context} must be an array")
    for index, item in enumerate(value):
        current = _as_mapping(item, f"{context}[{index}]")
        _reject_keys(current, {"term"}, f"{context}[{index}]")
        for field in ("key", "label", "definition"):
            _required(current, field, f"{context}[{index}]")


def _reject_keys(container: dict[str, Any], keys: set[str], context: str) -> None:
    found = sorted(keys & set(container))
    if found:
        raise ProjectionError(
            f"{context} uses retired projection field(s) {found}; use the canonical field shape"
        )


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
