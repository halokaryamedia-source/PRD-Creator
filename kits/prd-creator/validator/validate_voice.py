#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from shared.state import StateError, load_mapping, require_scalar
from shared.voice import VoiceEntry, VoiceRequirement, parse_production, parse_requirements

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SOURCE_PRD_REVISION_RE = re.compile(r"(?mi)^\s*Source PRD revision:\s*(\S+)\s*$")
SOURCE_REQUIREMENTS_RE = re.compile(
    r"(?mi)^\s*Source Voice Requirements:\s*(\S+)\s*/\s*(.+?)\s*\|\s*sha256:([0-9a-f]{64})\s*$"
)


def validate_revision_identity(project: Path, req: Path, scr: Path, state: Path) -> list[str]:
    issues: list[str] = []
    voice_state = load_mapping(state, owner="voice-state.yaml")
    source_handoff = require_scalar(voice_state, "source_handoff", owner="voice-state.yaml")
    source_prd_revision = require_scalar(voice_state, "source_prd_revision", owner="voice-state.yaml")
    project_html = require_scalar(voice_state, "project_html", owner="voice-state.yaml")

    handoff_path = project / source_handoff
    if not handoff_path.is_file():
        return [f"Voice source_handoff does not exist: {source_handoff}"]
    handoff_state = load_mapping(handoff_path, owner="handoff-state.yaml")
    handoff_status = require_scalar(handoff_state, "status", owner="handoff-state.yaml")
    accepted_revision = require_scalar(handoff_state, "accepted_prd_version", owner="handoff-state.yaml")
    if handoff_status != "handoff_ready":
        issues.append(f"Upstream PRD handoff status is {handoff_status!r}, expected 'handoff_ready'")

    render_data_path = project / "work" / "render-data.json"
    current_revision = ""
    if not render_data_path.is_file():
        issues.append("Current render-data.json is missing for Voice revision identity")
    else:
        try:
            data = json.loads(render_data_path.read_text(encoding="utf-8"))
            document = data.get("document") if isinstance(data, dict) else None
            current_revision = str(document.get("version") or "").strip() if isinstance(document, dict) else ""
        except json.JSONDecodeError as exc:
            issues.append(f"Current render-data.json is invalid: {exc}")

    req_revisions = SOURCE_PRD_REVISION_RE.findall(req.read_text(encoding="utf-8"))
    if len(req_revisions) != 1:
        issues.append("voice-requirements.md must define exactly one Source PRD revision")
        requirements_revision = ""
    else:
        requirements_revision = req_revisions[0].strip()

    source_matches = SOURCE_REQUIREMENTS_RE.findall(scr.read_text(encoding="utf-8"))
    if len(source_matches) != 1:
        issues.append(
            "voice-production.md must define exactly one Source Voice Requirements binding with revision, canonical path, and sha256"
        )
        script_revision = script_path = script_sha = ""
    else:
        script_revision, script_path, script_sha = (part.strip() for part in source_matches[0])

    for label, value in {
        "voice-state source_prd_revision": source_prd_revision,
        "voice-requirements Source PRD revision": requirements_revision,
        "voice-production Source Voice Requirements revision": script_revision,
        "current render-data document.version": current_revision,
    }.items():
        if value != accepted_revision:
            issues.append(f"{label}={value!r}, expected current accepted PRD revision {accepted_revision!r}")

    if script_path and script_path != "work/voice-requirements.md":
        issues.append(
            f"voice-production Source Voice Requirements path={script_path!r}, expected 'work/voice-requirements.md'"
        )
    actual_req_sha = hashlib.sha256(req.read_bytes()).hexdigest()
    if script_sha and (SHA256_RE.fullmatch(script_sha) is None or script_sha != actual_req_sha):
        issues.append(
            "voice-production Source Voice Requirements sha256 does not match current work/voice-requirements.md bytes"
        )

    expected_html = f"output/v{accepted_revision}/prd.html"
    if project_html != expected_html:
        issues.append(f"voice-state project_html={project_html!r}, expected {expected_html!r}")
    return issues


def validate_state(path: Path) -> str:
    state = load_mapping(path, owner="voice-state.yaml")
    status = require_scalar(state, "status", owner="voice-state.yaml")
    allowed = {"voice_script_ready", "voice_validation", "needs_revision", "voice_delivery_ready"}
    if status not in allowed:
        raise ValueError(
            f"Flow 7 cannot validate status {status}; expected one of: {', '.join(sorted(allowed))}"
        )
    return status


def validate_project_html(
    path: Path,
    sections: list[str],
    script: dict[str, VoiceEntry],
    requirements: dict[str, VoiceRequirement],
) -> list[str]:
    del requirements
    source = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if 'id="production-assets-style"' not in source:
        issues.append("Project HTML missing Production Assets presentation")
    if "Production Assets" not in source or "production-assets-nav" not in source:
        issues.append("Project HTML missing Production Assets Voice navigation")
    if source.count('class="pa-row pa-row-voice"') != len(script):
        issues.append("Project HTML compact Voice row count differs from canonical script")

    for section in sections:
        plain = re.sub(r"^\s*\d+\.\s*", "", section).strip()
        if plain and html.escape(plain, quote=True) not in source:
            issues.append(f"Project HTML missing Voice gameplay section: {plain}")

    for voice_id, entry in script.items():
        prompt_id = f"voice-prompt-{voice_id.lower()}"
        pattern = re.compile(
            rf'<pre class="voice-script-text" id="{re.escape(prompt_id)}">(.*?)</pre>', re.S
        )
        matches = pattern.findall(source)
        if len(matches) != 1:
            issues.append(f"Project HTML must contain exact Voice prompt panel once for {voice_id}")
            continue
        actual = html.unescape(matches[0])
        if actual != entry.performance:
            issues.append(f"Project HTML performance text differs from canonical script for {voice_id}")
        identity = html.escape(f"{entry.speaker} — {entry.title}", quote=True)
        if identity not in source:
            issues.append(f"Project HTML missing compact Voice identity for {voice_id}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Mechanically validate current Voice requirements/script and derived project HTML presentation."
    )
    parser.add_argument("project", type=Path, help="workspace/active/<project> directory")
    args = parser.parse_args()
    project = args.project
    req = project / "work/voice-requirements.md"
    scr = project / "work/voice-production.md"
    state = project / "state/voice-state.yaml"

    missing = [str(path.relative_to(project)) for path in (req, scr, state) if not path.is_file()]
    if missing:
        print("VOICE VALIDATION FAILED: missing files: " + ", ".join(missing), file=sys.stderr)
        return 2

    try:
        validate_state(state)
        requirements = parse_requirements(req, require_trigger=True)
        production = parse_production(scr)
        sections = [section.title for section in production.sections]
        script = {
            entry.voice_id: entry
            for section in production.sections
            for entry in section.entries
        }
        issues = validate_revision_identity(project, req, scr, state)

        if set(requirements) != set(script):
            missing_ids = sorted(set(requirements) - set(script))
            extra_ids = sorted(set(script) - set(requirements))
            if missing_ids:
                issues.append("Script missing Voice IDs: " + ", ".join(missing_ids))
            if extra_ids:
                issues.append("Script has extra Voice IDs: " + ", ".join(extra_ids))
        for voice_id in sorted(set(requirements) & set(script)):
            if requirements[voice_id].voice_type.casefold() != script[voice_id].voice_type.casefold():
                issues.append(f"Type mismatch for {voice_id}")
            if requirements[voice_id].speaker.casefold() != script[voice_id].speaker.casefold():
                issues.append(f"Speaker mismatch for {voice_id}")

        voice_state = load_mapping(state, owner="voice-state.yaml")
        html_ref = require_scalar(voice_state, "project_html", owner="voice-state.yaml")
        html_path = project / html_ref
        if html_path.is_file():
            issues.extend(validate_project_html(html_path, sections, script, requirements))

        if issues:
            print("VOICE VALIDATION FAILED")
            for issue in issues:
                print("- " + issue)
            return 1
        print("VOICE VALIDATION PASS")
        print(
            f"requirements={len(requirements)} script_entries={len(script)} sections={len(sections)}"
        )
        print("project_html=" + ("passed" if html_path.is_file() else "not_provided"))
        print("semantic_and_visual_review=required")
        return 0
    except (OSError, StateError, ValueError) as exc:
        print(f"VOICE VALIDATION FAILED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
