from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml
from yaml.nodes import MappingNode


class StateError(ValueError):
    """Raised when a persisted machine-state document violates its YAML contract."""

    def __init__(self, message: str, *, line: int | None = None) -> None:
        self.line = line
        super().__init__(message)


class _UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys instead of overwriting them."""


def _construct_unique_mapping(
    loader: _UniqueKeyLoader,
    node: MappingNode,
    deep: bool = False,
) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        line = key_node.start_mark.line + 1
        try:
            duplicate = key in mapping
        except TypeError as exc:
            raise StateError("YAML mapping keys must be hashable scalars", line=line) from exc
        if duplicate:
            raise StateError(f"duplicate YAML mapping key: {key!r}", line=line)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def load_mapping(path: Path, *, owner: str | None = None) -> dict[str, Any]:
    label = owner or path.name
    if not path.is_file():
        raise StateError(f"missing state file: {path}")
    try:
        value = yaml.load(path.read_text(encoding="utf-8"), Loader=_UniqueKeyLoader)
    except StateError as exc:
        if exc.line is not None:
            raise StateError(f"{label}:{exc.line}: {exc}", line=exc.line) from exc
        raise
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        line = mark.line + 1 if mark is not None else None
        location = f" at line {line}" if line is not None else ""
        raise StateError(f"{label} is not valid YAML{location}: {exc}", line=line) from exc
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise StateError(f"{label} root must be a mapping")
    return dict(value)


def require_scalar(
    mapping: Mapping[str, Any],
    key: str,
    *,
    owner: str,
) -> str:
    if key not in mapping:
        raise StateError(f"{owner} must define non-empty {key}")
    value = mapping[key]
    if isinstance(value, (dict, list, bool)) or value is None:
        raise StateError(f"{owner}.{key} must be a scalar")
    text = str(value).strip()
    if not text:
        raise StateError(f"{owner} must define non-empty {key}")
    return text


def optional_scalar(
    mapping: Mapping[str, Any],
    key: str,
    *,
    default: str = "",
) -> str:
    value = mapping.get(key)
    if value is None:
        return default
    if isinstance(value, (dict, list, bool)):
        raise StateError(f"{key} must be a scalar")
    return str(value).strip()


def require_bool(mapping: Mapping[str, Any], key: str, *, owner: str) -> bool:
    if key not in mapping or not isinstance(mapping[key], bool):
        raise StateError(f"{owner} must define exactly one {key} boolean")
    return bool(mapping[key])


def list_of_mappings(
    mapping: Mapping[str, Any],
    key: str,
    *,
    owner: str,
) -> list[dict[str, Any]]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise StateError(f"{owner}.{key} must be an array")
    result: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise StateError(f"{owner}.{key}[{index}] must be a mapping")
        result.append(dict(item))
    return result
