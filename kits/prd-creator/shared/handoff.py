from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .paths import ProjectPathError, normalize_project_ref
from .state import StateError, load_mapping, require_scalar

HANDOFF_REF_FIELDS = (
    "content",
    "render_data",
    "html",
    "context",
    "index",
    "acceptance",
    "handoff",
)
HANDOFF_FIELDS = {"status", "accepted_prd_version", *HANDOFF_REF_FIELDS}


@dataclass(frozen=True)
class HandoffState:
    status: str
    accepted_prd_version: str
    refs: dict[str, str]


def load_handoff_state(path: Path) -> HandoffState:
    state = load_mapping(path, owner="handoff-state.yaml")
    unknown = sorted(set(state) - HANDOFF_FIELDS)
    if unknown:
        raise StateError(
            "handoff-state.yaml contains unsupported field(s): " + ", ".join(unknown)
        )
    status = require_scalar(state, "status", owner="handoff-state.yaml")
    version = require_scalar(state, "accepted_prd_version", owner="handoff-state.yaml")
    refs: dict[str, str] = {}
    for field in HANDOFF_REF_FIELDS:
        raw = require_scalar(state, field, owner="handoff-state.yaml")
        try:
            refs[field] = normalize_project_ref(raw, owner=f"handoff-state.yaml.{field}")
        except ProjectPathError as exc:
            raise StateError(str(exc)) from exc
    return HandoffState(status=status, accepted_prd_version=version, refs=refs)
