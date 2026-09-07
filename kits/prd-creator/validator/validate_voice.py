#!/usr/bin/env python3
"""Mechanically validate the current Voice lifecycle from Flow 5 through Flow 7."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
if __package__ in (None, ""):
    if str(KIT_ROOT) not in sys.path:
        sys.path.insert(0, str(KIT_ROOT))
    from validator import validate_handoff as handoff_validator
else:
    from . import validate_handoff as handoff_validator

from shared.handoff import load_handoff_state
from shared.lifecycle import VoiceState, load_voice_state
from shared.paths import ProjectPathError, resolve_project_path
from shared.state import StateError
from shared.topology import owner_targets, production_page_id
from shared.voice import (
    VoiceEntry,
    VoiceProduction,
    VoiceRequirement,
    parse_production,
    parse_requirements,
    selected_voice,
)

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SOURCE_PRD_REVISION_RE = re.compile(r"(?mi)^\s*Source PRD revision:\s*(\S+)\s*$")
SOURCE_REQUIREMENTS_RE = re.compile(
    r"(?mi)^\s*Source Voice Requirements:\s*(\S+)\s*/\s*(.+?)\s*\|\s*sha256:([0-9a-f]{64})\s*$"
)
META_RE_TEMPLATE = r'<meta\s+content="([0-9a-f]{64})"\s+name="{name}"\s*/?>'
REQUIREMENTS_READY_STATUSES = {"voice_requirements_ready"}
SCRIPT_STATUSES = {"voice_script_ready", "voice_validation", "needs_revision", "voice_delivery_ready"}
VALIDATABLE_STATUSES = REQUIREMENTS_READY_STATUSES | SCRIPT_STATUSES | {"no_voice_required"}
VOICE_ACCEPTANCE_REQUIRED = {
    "Status": {"voice_delivery_ready"},
    "Mechanical": {"PASS"},
    "Voice Script Readiness": {"PASS"},
    "Communication Conservation": {"PASS"},
    "Project HTML Visual": {"PASS", "NOT PROVEN"},
    "Critical": {"0"},
    "Major": {"0"},
}
VOICE_ACCEPTED_SHA_LABEL = "Accepted Voice Production SHA256"


def _load_render_data(project: Path) -> tuple[dict[str, Any], str, str]:
    path = project / "work" / "render-data.json"
    if not path.is_file():
        raise ValueError("Current render-data.json is missing for Voice revision identity")
    raw = path.read_bytes()
    data = json.loads(raw.decode("utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Current render-data.json root must be an object")
    document = data.get("document")
    if not isinstance(document, dict):
        raise ValueError("Current render-data.json must contain document metadata")
    revision = str(document.get("version") or "").strip()
    if not revision:
        raise ValueError("Current render-data document.version is required for Voice")
    return data, revision, hashlib.sha256(raw).hexdigest()


def _accepted_revision(project: Path, voice_state: VoiceState) -> tuple[str, list[str]]:
    issues: list[str] = []
    upstream = handoff_validator.validate(project)
    if upstream.get("status") != "pass":
        detail = "; ".join(str(item) for item in upstream.get("errors", [])[:5]) or "unknown handoff failure"
        issues.append("Upstream PRD handoff validation failed: " + detail)

    try:
        handoff_path = resolve_project_path(
            project,
            voice_state.source_handoff,
            owner="voice-state.yaml.source_handoff",
            must_exist=True,
        )
        handoff = load_handoff_state(handoff_path)
    except (ProjectPathError, StateError) as exc:
        return "", [*issues, str(exc)]
    if handoff.status != "handoff_ready":
        issues.append(f"Upstream PRD handoff status is {handoff.status!r}, expected 'handoff_ready'")
    return handoff.accepted_prd_version, issues


def _state_identity_issues(
    voice_state: VoiceState,
    accepted_revision: str,
    current_revision: str,
    current_render_sha: str,
) -> list[str]:
    issues: list[str] = []
    if voice_state.source_handoff != "state/handoff-state.yaml":
        issues.append(
            f"voice-state source_handoff={voice_state.source_handoff!r}, expected 'state/handoff-state.yaml'"
        )
    for label, value in {
        "voice-state source_prd_revision": voice_state.source_prd_revision,
        "current render-data document.version": current_revision,
    }.items():
        if value != accepted_revision:
            issues.append(f"{label}={value!r}, expected current accepted PRD revision {accepted_revision!r}")
    if voice_state.source_prd_sha256 != current_render_sha:
        issues.append(
            "voice-state source_prd_sha256 does not match current accepted work/render-data.json bytes"
        )
    canonical = {
        "canonical_prd": "work/content.md",
        "requirements": "work/voice-requirements.md",
        "production": "work/voice-production.md",
    }
    for field, expected in canonical.items():
        actual = getattr(voice_state, field)
        if actual != expected:
            issues.append(f"voice-state {field}={actual!r}, expected {expected!r}")
    expected_html = f"output/v{accepted_revision}/prd.html"
    if voice_state.project_html and voice_state.project_html != expected_html:
        issues.append(f"voice-state project_html={voice_state.project_html!r}, expected {expected_html!r}")
    return issues


def _requirements_revision_issues(path: Path, accepted_revision: str) -> list[str]:
    revisions = SOURCE_PRD_REVISION_RE.findall(path.read_text(encoding="utf-8"))
    if len(revisions) != 1:
        return ["voice-requirements.md must define exactly one Source PRD revision"]
    current = revisions[0].strip()
    if current != accepted_revision:
        return [f"voice-requirements Source PRD revision={current!r}, expected {accepted_revision!r}"]
    return []


def _requirements_owner_issues(
    render_data: dict[str, Any],
    requirements: dict[str, VoiceRequirement],
) -> list[str]:
    valid_owners = owner_targets(render_data)
    return [
        f"Voice requirement {requirement.voice_id} Owner ID does not match accepted PRD topology: {requirement.owner_id}"
        for requirement in requirements.values()
        if requirement.owner_id not in valid_owners
    ]


def _production_binding_issues(
    requirements_path: Path,
    production_path: Path,
    accepted_revision: str,
) -> list[str]:
    matches = SOURCE_REQUIREMENTS_RE.findall(production_path.read_text(encoding="utf-8"))
    if len(matches) != 1:
        return [
            "voice-production.md must define exactly one Source Voice Requirements binding with revision, canonical path, and sha256"
        ]
    revision, source_path, source_sha = (part.strip() for part in matches[0])
    issues: list[str] = []
    if revision != accepted_revision:
        issues.append(
            f"voice-production Source Voice Requirements revision={revision!r}, expected {accepted_revision!r}"
        )
    if source_path != "work/voice-requirements.md":
        issues.append(
            f"voice-production Source Voice Requirements path={source_path!r}, expected 'work/voice-requirements.md'"
        )
    actual_sha = hashlib.sha256(requirements_path.read_bytes()).hexdigest()
    if SHA256_RE.fullmatch(source_sha) is None or source_sha != actual_sha:
        issues.append(
            "voice-production Source Voice Requirements sha256 does not match current work/voice-requirements.md bytes"
        )
    return issues


def _production_parity_issues(
    render_data: dict[str, Any],
    requirements: dict[str, VoiceRequirement],
    production: VoiceProduction,
) -> list[str]:
    issues: list[str] = []
    valid_owners = owner_targets(render_data)
    production_by_id: dict[str, tuple[str, VoiceEntry]] = {}
    for section in production.sections:
        if section.owner_id not in valid_owners:
            issues.append(f"Voice Production Owner ID does not match accepted PRD topology: {section.owner_id}")
        for entry in section.entries:
            production_by_id[entry.voice_id] = (section.owner_id, entry)

    missing = sorted(set(requirements) - set(production_by_id))
    extra = sorted(set(production_by_id) - set(requirements))
    if missing:
        issues.append("Script missing Voice IDs: " + ", ".join(missing))
    if extra:
        issues.append("Script has extra Voice IDs: " + ", ".join(extra))

    for voice_id in sorted(set(requirements) & set(production_by_id)):
        requirement = requirements[voice_id]
        owner_id, entry = production_by_id[voice_id]
        if owner_id != requirement.owner_id:
            issues.append(
                f"Owner ID mismatch for {voice_id}: production={owner_id!r}, requirement={requirement.owner_id!r}"
            )
        if requirement.voice_type.casefold() != entry.voice_type.casefold():
            issues.append(f"Type mismatch for {voice_id}")
        if requirement.speaker.casefold() != entry.speaker.casefold():
            issues.append(f"Speaker mismatch for {voice_id}")
    return issues


def _meta_sha(source: str, name: str) -> str:
    matches = re.findall(META_RE_TEMPLATE.format(name=re.escape(name)), source, flags=re.I)
    return matches[0] if len(matches) == 1 else ""


def _html_issues(
    path: Path,
    render_data: dict[str, Any],
    requirements_path: Path,
    production_path: Path,
    requirements: dict[str, VoiceRequirement],
    production: VoiceProduction,
) -> list[str]:
    source = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if 'id="production-assets-style"' not in source or 'id="production-assets-script"' not in source:
        issues.append("Project HTML missing current Production Assets presentation resources")
    if "Production Assets" not in source or "production-assets-nav" not in source:
        issues.append("Project HTML missing Production Assets Voice navigation")

    requirements_sha = hashlib.sha256(requirements_path.read_bytes()).hexdigest()
    production_sha = hashlib.sha256(production_path.read_bytes()).hexdigest()
    if _meta_sha(source, "voice-requirements-sha256") != requirements_sha:
        issues.append("Project HTML is stale relative to current voice-requirements.md bytes")
    if _meta_sha(source, "voice-production-sha256") != production_sha:
        issues.append("Project HTML is stale relative to current voice-production.md bytes")

    entries = {
        entry.voice_id: (section.owner_id, entry)
        for section in production.sections
        for entry in section.entries
    }
    if source.count('class="pa-row pa-row-voice"') != len(entries):
        issues.append("Project HTML compact Voice row count differs from canonical production")

    section_blocks = {
        match.group(1): match.group(2)
        for match in re.finditer(
            r'<section\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</section>',
            source,
            re.S | re.I,
        )
    }
    for voice_id, requirement in requirements.items():
        pair = entries.get(voice_id)
        if pair is None:
            continue
        owner_id, entry = pair
        page_id = production_page_id(render_data, owner_id)
        block = section_blocks.get(page_id, "")
        if not block:
            issues.append(f"Project HTML missing Production Assets page for Voice owner {owner_id}: {page_id}")
            continue
        if f'data-moment-id="{html.escape(requirement.moment_id, quote=True)}"' not in block:
            issues.append(f"Project HTML missing canonical Moment ID for {voice_id}: {requirement.moment_id}")
        prompt_id = f"voice-prompt-{voice_id.lower()}"
        matches = re.findall(
            rf'<pre class="voice-script-text" id="{re.escape(prompt_id)}">(.*?)</pre>',
            block,
            flags=re.S,
        )
        if len(matches) != 1:
            issues.append(f"Project HTML must contain exact Voice prompt panel once for {voice_id} in {page_id}")
            continue
        if html.unescape(matches[0]) != entry.performance:
            issues.append(f"Project HTML performance text differs from canonical production for {voice_id}")
        identity = html.escape(f"{entry.speaker} — {entry.title}", quote=True)
        if identity not in block:
            issues.append(f"Project HTML missing compact Voice identity for {voice_id}")
    return issues


def _delivery_selection_issues(production: VoiceProduction, state: VoiceState) -> list[str]:
    if state.status != "voice_delivery_ready":
        return []
    speakers = sorted({entry.speaker for section in production.sections for entry in section.entries})
    return [
        f"voice_delivery_ready requires a Voice Cast selection/profile for speaker: {speaker}"
        for speaker in speakers
        if not selected_voice(production.cast, speaker)
    ]


def _acceptance_values(text: str, label: str) -> list[str]:
    pattern = re.compile(rf"(?mi)^\s*{re.escape(label)}:\s*(.*?)\s*$")
    return [value.strip() for value in pattern.findall(text)]


def _voice_acceptance_issues(project: Path, production_path: Path, state: VoiceState) -> list[str]:
    if state.status != "voice_delivery_ready":
        return []
    path = project / "work" / "voice-acceptance.md"
    if not path.is_file():
        return ["voice_delivery_ready requires work/voice-acceptance.md"]
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    for label, allowed in VOICE_ACCEPTANCE_REQUIRED.items():
        values = _acceptance_values(text, label)
        if len(values) != 1 or values[0] not in allowed:
            issues.append(f"Voice Acceptance {label} must appear exactly once with one of {sorted(allowed)}")
    values = _acceptance_values(text, VOICE_ACCEPTED_SHA_LABEL)
    actual_sha = hashlib.sha256(production_path.read_bytes()).hexdigest()
    if len(values) != 1 or SHA256_RE.fullmatch(values[0]) is None:
        issues.append(f"{VOICE_ACCEPTED_SHA_LABEL} must appear exactly once as a SHA-256 digest")
    elif values[0] != actual_sha:
        issues.append("Voice Acceptance is stale relative to current voice-production.md bytes")
    return issues


def validate(project: Path) -> dict[str, Any]:
    project = project.resolve()
    state_path = project / "state" / "voice-state.yaml"
    voice_state = load_voice_state(state_path)
    if voice_state.status not in VALIDATABLE_STATUSES:
        raise StateError(
            f"Voice validation cannot claim readiness for status {voice_state.status!r}; expected one of: "
            + ", ".join(sorted(VALIDATABLE_STATUSES))
        )

    render_data, current_revision, current_render_sha = _load_render_data(project)
    accepted_revision, issues = _accepted_revision(project, voice_state)
    issues.extend(
        _state_identity_issues(
            voice_state,
            accepted_revision,
            current_revision,
            current_render_sha,
        )
    )

    if voice_state.status == "no_voice_required":
        return _result(voice_state, issues, 0, 0, 0, "not_applicable")

    requirements_path = resolve_project_path(
        project,
        voice_state.requirements,
        owner="voice-state.yaml.requirements",
        must_exist=True,
    )
    requirements = parse_requirements(requirements_path)
    issues.extend(_requirements_revision_issues(requirements_path, accepted_revision))
    issues.extend(_requirements_owner_issues(render_data, requirements))

    if voice_state.status in REQUIREMENTS_READY_STATUSES:
        return _result(voice_state, issues, len(requirements), 0, 0, "not_required_yet")

    production_path = resolve_project_path(
        project,
        voice_state.production,
        owner="voice-state.yaml.production",
        must_exist=True,
    )
    production = parse_production(production_path)
    issues.extend(_production_binding_issues(requirements_path, production_path, accepted_revision))
    issues.extend(_production_parity_issues(render_data, requirements, production))
    issues.extend(_delivery_selection_issues(production, voice_state))

    html_state = "not_provided"
    if voice_state.project_html:
        try:
            html_path = resolve_project_path(
                project,
                voice_state.project_html,
                owner="voice-state.yaml.project_html",
                must_exist=True,
            )
        except ProjectPathError as exc:
            issues.append(str(exc))
            html_state = "missing"
        else:
            html_issues = _html_issues(
                html_path,
                render_data,
                requirements_path,
                production_path,
                requirements,
                production,
            )
            issues.extend(html_issues)
            html_state = "passed" if not html_issues else "failed"
    elif voice_state.status == "voice_delivery_ready":
        issues.append("voice_delivery_ready requires project_html in voice-state.yaml")
        html_state = "missing"

    issues.extend(_voice_acceptance_issues(project, production_path, voice_state))
    return _result(
        voice_state,
        issues,
        len(requirements),
        sum(len(section.entries) for section in production.sections),
        len(production.sections),
        html_state,
    )


def _result(
    state: VoiceState,
    issues: list[str],
    requirements: int,
    entries: int,
    sections: int,
    html_state: str,
) -> dict[str, Any]:
    return {
        "status": "pass" if not issues else "fail",
        "errors": issues,
        "voice_status": state.status,
        "requirements": requirements,
        "script_entries": entries,
        "sections": sections,
        "project_html": html_state,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="workspace/active/<project> directory")
    args = parser.parse_args()
    try:
        result = validate(args.project)
    except (OSError, ProjectPathError, StateError, ValueError, json.JSONDecodeError) as exc:
        print(f"VOICE VALIDATION FAILED: {exc}", file=sys.stderr)
        return 2
    if result["status"] == "fail":
        print("VOICE VALIDATION FAILED")
        for issue in result["errors"]:
            print("- " + str(issue))
        return 1
    print("VOICE VALIDATION PASS")
    print(
        f"status={result['voice_status']} requirements={result['requirements']} "
        f"script_entries={result['script_entries']} sections={result['sections']}"
    )
    print(f"project_html={result['project_html']}")
    print("semantic_and_visual_review=required")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
