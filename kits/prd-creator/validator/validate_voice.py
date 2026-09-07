#!/usr/bin/env python3
"""Mechanically validate the current Voice lifecycle and consolidated HTML binding."""
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

from shared.lifecycle import VoiceState, require_voice_state_for
from shared.state import StateError, load_mapping, require_scalar
from shared.topology import owner_targets, production_page_id
from shared.voice import VoiceEntry, VoiceProduction, VoiceRequirement, parse_production, parse_requirements, selected_voice

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SOURCE_PRD_REVISION_RE = re.compile(r"(?mi)^\s*Source PRD revision:\s*(\S+)\s*$")
SOURCE_REQUIREMENTS_RE = re.compile(
    r"(?mi)^\s*Source Voice Requirements:\s*(\S+)\s*/\s*(.+?)\s*\|\s*sha256:([0-9a-f]{64})\s*$"
)
META_RE_TEMPLATE = r'<meta\s+content="([0-9a-f]{64})"\s+name="{name}"\s*/?>'
FLOW7_STATUSES = {"voice_script_ready", "voice_validation", "needs_revision", "voice_delivery_ready"}


def _load_render_data(project: Path) -> tuple[dict[str, Any], str]:
    path = project / "work" / "render-data.json"
    if not path.is_file():
        raise ValueError("Current render-data.json is missing for Voice revision identity")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Current render-data.json root must be an object")
    document = data.get("document")
    if not isinstance(document, dict):
        raise ValueError("Current render-data.json must contain document metadata")
    revision = str(document.get("version") or "").strip()
    if not revision:
        raise ValueError("Current render-data document.version is required for Voice")
    return data, revision


def validate_revision_identity(
    project: Path,
    requirements_path: Path,
    production_path: Path,
    voice_state: VoiceState,
    current_revision: str,
) -> list[str]:
    issues: list[str] = []
    handoff_path = project / voice_state.source_handoff
    if not handoff_path.is_file():
        return [f"Voice source_handoff does not exist: {voice_state.source_handoff}"]
    handoff_state = load_mapping(handoff_path, owner="handoff-state.yaml")
    handoff_status = require_scalar(handoff_state, "status", owner="handoff-state.yaml")
    accepted_revision = require_scalar(handoff_state, "accepted_prd_version", owner="handoff-state.yaml")
    if handoff_status != "handoff_ready":
        issues.append(f"Upstream PRD handoff status is {handoff_status!r}, expected 'handoff_ready'")

    req_revisions = SOURCE_PRD_REVISION_RE.findall(requirements_path.read_text(encoding="utf-8"))
    requirements_revision = req_revisions[0].strip() if len(req_revisions) == 1 else ""
    if len(req_revisions) != 1:
        issues.append("voice-requirements.md must define exactly one Source PRD revision")

    source_matches = SOURCE_REQUIREMENTS_RE.findall(production_path.read_text(encoding="utf-8"))
    if len(source_matches) != 1:
        issues.append(
            "voice-production.md must define exactly one Source Voice Requirements binding with revision, canonical path, and sha256"
        )
        script_revision = script_path = script_sha = ""
    else:
        script_revision, script_path, script_sha = (part.strip() for part in source_matches[0])

    for label, value in {
        "voice-state source_prd_revision": voice_state.source_prd_revision,
        "voice-requirements Source PRD revision": requirements_revision,
        "voice-production Source Voice Requirements revision": script_revision,
        "current render-data document.version": current_revision,
    }.items():
        if value != accepted_revision:
            issues.append(f"{label}={value!r}, expected current accepted PRD revision {accepted_revision!r}")

    if voice_state.canonical_prd != "work/content.md":
        issues.append(f"voice-state canonical_prd={voice_state.canonical_prd!r}, expected 'work/content.md'")
    if voice_state.requirements != "work/voice-requirements.md":
        issues.append(
            f"voice-state requirements={voice_state.requirements!r}, expected 'work/voice-requirements.md'"
        )
    if voice_state.production != "work/voice-production.md":
        issues.append(f"voice-state production={voice_state.production!r}, expected 'work/voice-production.md'")
    if script_path and script_path != "work/voice-requirements.md":
        issues.append(
            f"voice-production Source Voice Requirements path={script_path!r}, expected 'work/voice-requirements.md'"
        )
    actual_req_sha = hashlib.sha256(requirements_path.read_bytes()).hexdigest()
    if script_sha and (SHA256_RE.fullmatch(script_sha) is None or script_sha != actual_req_sha):
        issues.append(
            "voice-production Source Voice Requirements sha256 does not match current work/voice-requirements.md bytes"
        )

    expected_html = f"output/v{accepted_revision}/prd.html"
    if voice_state.project_html and voice_state.project_html != expected_html:
        issues.append(f"voice-state project_html={voice_state.project_html!r}, expected {expected_html!r}")
    if voice_state.status == "voice_delivery_ready" and voice_state.project_html != expected_html:
        issues.append("voice_delivery_ready requires the current consolidated project_html path")
    return issues


def validate_owner_identity(
    render_data: dict[str, Any],
    requirements: dict[str, VoiceRequirement],
    production: VoiceProduction,
) -> list[str]:
    issues: list[str] = []
    valid_owners = owner_targets(render_data)
    for requirement in requirements.values():
        if requirement.owner_id not in valid_owners:
            issues.append(
                f"Voice requirement {requirement.voice_id} Owner ID does not match accepted PRD topology: {requirement.owner_id}"
            )

    production_by_id: dict[str, tuple[str, VoiceEntry]] = {}
    for section in production.sections:
        if section.owner_id not in valid_owners:
            issues.append(f"Voice Production Owner ID does not match accepted PRD topology: {section.owner_id}")
        for entry in section.entries:
            production_by_id[entry.voice_id] = (section.owner_id, entry)

    if set(requirements) != set(production_by_id):
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
    if len(matches) != 1:
        return ""
    return matches[0]


def validate_project_html(
    path: Path,
    render_data: dict[str, Any],
    requirements_path: Path,
    production_path: Path,
    requirements: dict[str, VoiceRequirement],
    production: VoiceProduction,
) -> list[str]:
    source = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if 'id="production-assets-style"' not in source:
        issues.append("Project HTML missing Production Assets presentation")
    if "Production Assets" not in source or "production-assets-nav" not in source:
        issues.append("Project HTML missing Production Assets Voice navigation")

    actual_requirements_sha = hashlib.sha256(requirements_path.read_bytes()).hexdigest()
    actual_production_sha = hashlib.sha256(production_path.read_bytes()).hexdigest()
    if _meta_sha(source, "voice-requirements-sha256") != actual_requirements_sha:
        issues.append("Project HTML is stale relative to current voice-requirements.md bytes")
    if _meta_sha(source, "voice-production-sha256") != actual_production_sha:
        issues.append("Project HTML is stale relative to current voice-production.md bytes")

    entries = {
        entry.voice_id: (section.owner_id, entry)
        for section in production.sections
        for entry in section.entries
    }
    if source.count('class="pa-row pa-row-voice"') != len(entries):
        issues.append("Project HTML compact Voice row count differs from canonical production")

    section_blocks: dict[str, str] = {}
    for match in re.finditer(r'<section\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</section>', source, re.S | re.I):
        section_blocks[match.group(1)] = match.group(2)

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
        prompt_id = f"voice-prompt-{voice_id.lower()}"
        pattern = re.compile(
            rf'<pre class="voice-script-text" id="{re.escape(prompt_id)}">(.*?)</pre>', re.S
        )
        matches = pattern.findall(block)
        if len(matches) != 1:
            issues.append(f"Project HTML must contain exact Voice prompt panel once for {voice_id} in {page_id}")
            continue
        actual = html.unescape(matches[0])
        if actual != entry.performance:
            issues.append(f"Project HTML performance text differs from canonical production for {voice_id}")
        identity = html.escape(f"{entry.speaker} — {entry.title}", quote=True)
        if identity not in block:
            issues.append(f"Project HTML missing compact Voice identity for {voice_id}")
        if html.escape(requirement.moment, quote=True) not in block:
            issues.append(f"Project HTML missing canonical production moment for {voice_id}")
    return issues


def validate_delivery_selection(production: VoiceProduction, state: VoiceState) -> list[str]:
    if state.status != "voice_delivery_ready":
        return []
    issues: list[str] = []
    speakers = sorted({entry.speaker for section in production.sections for entry in section.entries})
    for speaker in speakers:
        selection = selected_voice(production.cast, speaker)
        if not selection:
            issues.append(f"voice_delivery_ready requires a Voice Cast selection/profile for speaker: {speaker}")
    return issues


def validate(project: Path) -> dict[str, Any]:
    state_path = project / "state" / "voice-state.yaml"
    voice_state = require_voice_state_for(FLOW7_STATUSES, state_path)
    requirements_path = project / voice_state.requirements
    production_path = project / voice_state.production
    missing = [
        str(path.relative_to(project))
        for path in (requirements_path, production_path)
        if not path.is_file()
    ]
    if missing:
        raise ValueError("missing files: " + ", ".join(missing))

    render_data, current_revision = _load_render_data(project)
    requirements = parse_requirements(requirements_path)
    production = parse_production(production_path)
    issues = validate_revision_identity(
        project,
        requirements_path,
        production_path,
        voice_state,
        current_revision,
    )
    issues.extend(validate_owner_identity(render_data, requirements, production))
    issues.extend(validate_delivery_selection(production, voice_state))

    html_path = project / voice_state.project_html if voice_state.project_html else None
    if html_path is not None and html_path.is_file():
        issues.extend(
            validate_project_html(
                html_path,
                render_data,
                requirements_path,
                production_path,
                requirements,
                production,
            )
        )
    elif voice_state.status == "voice_delivery_ready":
        issues.append("voice_delivery_ready requires current consolidated project HTML")

    return {
        "status": "pass" if not issues else "fail",
        "errors": issues,
        "voice_status": voice_state.status,
        "requirements": len(requirements),
        "script_entries": sum(len(section.entries) for section in production.sections),
        "sections": len(production.sections),
        "project_html": "passed" if html_path is not None and html_path.is_file() and not issues else "not_provided_or_failed",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="workspace/active/<project> directory")
    args = parser.parse_args()
    try:
        result = validate(args.project)
    except (OSError, StateError, ValueError, json.JSONDecodeError) as exc:
        print(f"VOICE VALIDATION FAILED: {exc}", file=sys.stderr)
        return 2
    if result["status"] == "fail":
        print("VOICE VALIDATION FAILED")
        for issue in result["errors"]:
            print("- " + str(issue))
        return 1
    print("VOICE VALIDATION PASS")
    print(
        f"requirements={result['requirements']} script_entries={result['script_entries']} sections={result['sections']}"
    )
    print(f"project_html={result['project_html']}")
    print("semantic_and_visual_review=required")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
