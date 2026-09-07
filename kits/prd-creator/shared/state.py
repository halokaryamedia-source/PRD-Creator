from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml


class StateError(ValueError):
    """Raised when a machine-owned YAML state file violates its contract."""


def load_yaml_mapping(path: Path, *, required: bool = True) -> dict[str, Any]:
    if not path.is_file():
        if required:
            raise StateError(f"missing state file: {path}")
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise StateError(f"invalid YAML in {path}: {exc}") from exc
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise StateError(f"{path.name} root must be a mapping")
    return dict(data)


def require_text(mapping: Mapping[str, Any], key: str, *, owner: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip():
        raise StateError(f"{owner}.{key} must be a non-empty string")
    return value.strip()


def require_bool(mapping: Mapping[str, Any], key: str, *, owner: str) -> bool:
    value = mapping.get(key)
    if key not in mapping or not isinstance(value, bool):
        raise StateError(f"{owner} must define exactly one {key} boolean")
    return value


def optional_text(mapping: Mapping[str, Any], key: str) -> str:
    value = mapping.get(key)
    return value.strip() if isinstance(value, str) else ""


def require_list(mapping: Mapping[str, Any], key: str, *, owner: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise StateError(f"{owner}.{key} must be an array")
    return value


def require_mapping(value: Any, *, owner: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise StateError(f"{owner} must be a mapping")
    return dict(value)
