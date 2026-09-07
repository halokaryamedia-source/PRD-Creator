from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from .paths import ProjectPathError, normalize_project_ref
from .state import StateError, load_mapping, require_scalar

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
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
    "source_prd_sha256",
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
    source_prd_sha256: str
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
    source_prd_sha256 = require_scalar(state, "source_prd_sha256", owner="voice-state.yaml").casefold()
    if SHA256_RE.fullmatch(source_prd_sha256) is None:
        raise StateError("voice-state.yaml.source_prd_sha256 must be a lowercase SHA-256 digest")
    return VoiceState(
        status=status,
        source_handoff=_required_path(state, "source_handoff"),
        source_prd_revision=require_scalar(
            state,
            "source_prd_revision",
            owner="voice-state.yaml",
        ),
        source_prd_sha256=source_prd_sha256,
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


def _required_path(state: Mapping[str, object], key: str) -> str:
    raw = require_scalar(state, key, owner="voice-state.yaml")
    try:
        return normalize_project_ref(raw, owner=f"voice-state.yaml.{key}")
    except ProjectPathError as exc:
        raise StateError(str(exc)) from exc


def _optional_path(state: Mapping[str, object], key: str, default: str) -> str:
    value = state.get(key)
    if value is None:
        raw = default
    elif isinstance(value, (dict, list, bool)):
        raise StateError(f"voice-state.yaml.{key} must be a scalar path")
    else:
        raw = str(value).strip() or default
    if not raw:
        return ""
    try:
        return normalize_project_ref(raw, owner=f"voice-state.yaml.{key}")
    except ProjectPathError as exc:
        raise StateError(str(exc)) from exc
