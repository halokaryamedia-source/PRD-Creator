from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .state import StateError, load_mapping, require_scalar

HANDOFF_FIELDS = {"status", "accepted_prd_version"}


@dataclass(frozen=True)
class HandoffState:
    status: str
    accepted_prd_version: str


def load_handoff_state(path: Path) -> HandoffState:
    state = load_mapping(path, owner="handoff-state.yaml")
    unknown = sorted(set(state) - HANDOFF_FIELDS)
    if unknown:
        raise StateError("handoff-state.yaml contains unsupported field(s): " + ", ".join(unknown))
    status = require_scalar(state, "status", owner="handoff-state.yaml")
    version = require_scalar(state, "accepted_prd_version", owner="handoff-state.yaml")
    return HandoffState(status=status, accepted_prd_version=version)
