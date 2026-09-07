from __future__ import annotations

import re
from pathlib import Path, PurePosixPath


class ProjectPathError(ValueError):
    """Raised when a persisted project-relative path escapes its workspace."""


def normalize_project_ref(ref: str, *, owner: str = "project path") -> str:
    value = str(ref or "").strip()
    if not value:
        raise ProjectPathError(f"{owner} must be a non-empty project-relative path")
    if "\x00" in value:
        raise ProjectPathError(f"{owner} contains a NUL byte")
    if "\\" in value:
        raise ProjectPathError(f"{owner} must use canonical POSIX separators")
    if re.match(r"^[A-Za-z]:/", value) or value.startswith("//"):
        raise ProjectPathError(f"{owner} must not use an absolute Windows/UNC path")

    pure = PurePosixPath(value)
    if pure.is_absolute():
        raise ProjectPathError(f"{owner} must be project-relative")
    if any(part in {"", ".", ".."} for part in pure.parts):
        raise ProjectPathError(f"{owner} contains a non-canonical path segment")
    normalized = pure.as_posix()
    if normalized != value:
        raise ProjectPathError(f"{owner} must already be normalized as {normalized!r}")
    return normalized


def resolve_project_path(
    project: Path,
    ref: str,
    *,
    owner: str = "project path",
    must_exist: bool = False,
) -> Path:
    normalized = normalize_project_ref(ref, owner=owner)
    root = project.resolve()
    candidate = (root / normalized).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ProjectPathError(f"{owner} escapes the project workspace: {ref!r}") from exc
    if must_exist and not candidate.exists():
        raise ProjectPathError(f"{owner} does not exist: {normalized}")
    return candidate
