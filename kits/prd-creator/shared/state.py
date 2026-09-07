from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml


class StateError(ValueError):
    """Raised when a persisted state document is missing required structure."""


def load_mapping(path: Path, *, owner: str | None = None) -> dict[str, Any]:
    label = owner or path.name
    if not path.is_file():
        raise StateError(f"missing state file: {path}")
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise StateError(f"{label} is not valid YAML: {exc}") from exc
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
    if isinstance(value, (dict, list)) or value is None:
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
    if isinstance(value, (dict, list)):
        raise StateError(f"{key} must be a scalar")
    return str(value).strip()


def require_bool(mapping: Mapping[str, Any], key: str, *, owner: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise StateError(f"{owner}.{key} must be a boolean")
    return value


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
