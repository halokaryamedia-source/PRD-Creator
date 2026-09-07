from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from .state import StateError, load_mapping, require_scalar

VOICE_STATUSES = {
    "pending_extraction",
    "needs_upstream_decision",
    "voice_requirements_ready",
    "no_voice_required",
    "blocked",
    "voice_script_ready",
    "voice_validation",
    "needs_revision",
    "voice_delivery_ready",
}
VOICE_STATE_KEYS = {
    "status",
    "source_handoff",
    "source_prd_revision",
    "canonical_prd",
    "requirements",
    "production",
    "project_html",
}


@dataclass(frozen=True)
class VoiceState:
    status: str
    source_handoff: str
    source_prd_revision: str
    canonical_prd: str
    requirements: str
    production: str
    project_html: str


def load_voice_state(path: Path) -> VoiceState:
    state = load_mapping(path, owner="voice-state.yaml")
    unknown = sorted(set(state) - VOICE_STATE_KEYS)
    if unknown:
        raise StateError(
            "voice-state.yaml contains retired/unknown lifecycle field(s): " + ", ".join(unknown)
        )
    status = require_scalar(state, "status", owner="voice-state.yaml")
    if status not in VOICE_STATUSES:
        raise StateError(f"voice-state.yaml.status={status!r} is not a supported Voice lifecycle status")
    return VoiceState(
        status=status,
        source_handoff=require_scalar(state, "source_handoff", owner="voice-state.yaml"),
        source_prd_revision=require_scalar(state, "source_prd_revision", owner="voice-state.yaml"),
        canonical_prd=_optional_path(state, "canonical_prd", "work/content.md"),
        requirements=_optional_path(state, "requirements", "work/voice-requirements.md"),
        production=_optional_path(state, "production", "work/voice-production.md"),
        project_html=_optional_path(state, "project_html", ""),
    )


def require_voice_state_for(statuses: set[str], path: Path) -> VoiceState:
    state = load_voice_state(path)
    if state.status not in statuses:
        raise StateError(
            f"voice-state.yaml.status={state.status!r}, expected one of: {', '.join(sorted(statuses))}"
        )
    return state


def _optional_path(state: Mapping[str, object], key: str, default: str) -> str:
    value = state.get(key)
    if value is None:
        return default
    if isinstance(value, (dict, list, bool)):
        raise StateError(f"voice-state.yaml.{key} must be a scalar path")
    text = str(value).strip()
    return text or default
