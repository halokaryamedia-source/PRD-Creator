from __future__ import annotations

from typing import Any


class ProjectionError(ValueError):
    """Raised when render-data does not match the canonical projection schema."""


RETIRED_ALIASES = {
    "map_type",
    "display_title",
    "context_label",
    "group_title",
    "objects",
    "requirement",
    "requirements",
    "expected_result",
    "gameplay_function",
    "game_purpose",
    "estimated_time",
    "duration",
    "scoring_summary",
    "size",
    "dimensions",
    "number",
    "build_and_visual",
    "term",
    "stage",
    "trigger",
    "behavior",
    "note",
}


def validate_projection_schema(data: dict[str, Any]) -> None:
    """Reject ambiguity before deterministic rendering.

    The projection contract intentionally chooses one key per semantic meaning. This
    function is not a full semantic validator; it prevents compatibility aliases and
    renderer-side inference from becoming an accidental second schema.
    """

    if not isinstance(data, dict):
        raise ProjectionError("render-data root must be an object")
    _reject_aliases(data, "render_data")

    document = _mapping(data, "document", "render_data")
    _required(document, "title", "document")
    _required(document, "document_type", "document")
    _required(document, "version", "document")

    overview = _mapping(data, "overview", "render_data")
    for field in ("project_context", "main_experience", "document_scope", "intended_use"):
        _required(overview, field, "overview")
    _list(data, "gameplay_flow", "render_data", nonempty=True)
    _list(data, "global_development", "render_data", nonempty=True)
    packages = _list(data, "packages", "render_data", nonempty=True)

    for package_index, package in enumerate(packages):
        if not isinstance(package, dict):
            raise ProjectionError(f"packages[{package_index}] must be an object")
        context = f"packages[{package_index}]"
        _required(package, "id", context)
        _required(package, "title", context)
        _required(package, "package_label", context)
        gameplay = _mapping(package, "gameplay", context)
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
        _list(gameplay, "player_flow", f"{context}.gameplay", nonempty=True)

        level = _mapping(package, "level_design", context)
        _required(level, "overview", f"{context}.level_design")
        _list(level, "flow", f"{context}.level_design", nonempty=True)
        _list(level, "requirements", f"{context}.level_design", nonempty=True)

        developer = _mapping(package, "developer", context)
        _required(developer, "overview", f"{context}.developer")
        _list(developer, "flow", f"{context}.developer", nonempty=True)
        _list(developer, "requirements", f"{context}.developer", nonempty=True)
        _required(developer, "reset", f"{context}.developer")
        _required(developer, "reset_result", f"{context}.developer")

    _validate_requirement_shape(data)


def _validate_requirement_shape(data: dict[str, Any]) -> None:
    for section_index, section in enumerate(data.get("global_development", [])):
        if not isinstance(section, dict):
            continue
        _validate_groups(section.get("requirements"), f"global_development[{section_index}].requirements", "title")
    for package_index, package in enumerate(data.get("packages", [])):
        if not isinstance(package, dict):
            continue
        level = package.get("level_design")
        if isinstance(level, dict):
            _validate_groups(level.get("requirements"), f"packages[{package_index}].level_design.requirements", "object")
        developer = package.get("developer")
        if isinstance(developer, dict):
            _validate_groups(developer.get("requirements"), f"packages[{package_index}].developer.requirements", "title")


def _validate_groups(value: Any, context: str, item_title_key: str) -> None:
    if not isinstance(value, list):
        raise ProjectionError(f"{context} must be an array")
    for group_index, group in enumerate(value):
        if not isinstance(group, dict):
            raise ProjectionError(f"{context}[{group_index}] must be an object")
        _required(group, "title", f"{context}[{group_index}]")
        items = _list(group, "items", f"{context}[{group_index}]", nonempty=True)
        for item_index, item in enumerate(items):
            if not isinstance(item, dict):
                raise ProjectionError(f"{context}[{group_index}].items[{item_index}] must be an object")
            item_context = f"{context}[{group_index}].items[{item_index}]"
            _required(item, item_title_key, item_context)
            if item_title_key == "object":
                for field in ("area_size", "build_and_visual_requirements", "gameplay_function"):
                    _required(item, field, item_context)
            else:
                for field in ("details", "result"):
                    _required(item, field, item_context)


def _reject_aliases(value: Any, path: str) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in RETIRED_ALIASES:
                raise ProjectionError(f"{path}.{key} is a retired projection alias; use the canonical schema field")
            _reject_aliases(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_aliases(child, f"{path}[{index}]")


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
