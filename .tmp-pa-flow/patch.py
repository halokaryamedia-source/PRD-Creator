from __future__ import annotations

from pathlib import Path

ROOT = Path('.')
PROJECT = ROOT / 'workspace/active/the-clockwork-vault'


def patch_voice_renderer() -> None:
    path = ROOT / 'kits/project-document-generator/renderer/production_assets.py'
    text = path.read_text(encoding='utf-8')
    if 'def parse_voice_requirement_flows(' in text:
        return
    needle = '\ndef _voice_for(cast: dict[str, str], speaker: str) -> str:\n'
    if needle not in text:
        raise SystemExit('production_assets.py insertion point not found')
    addition = '''\n\ndef parse_voice_requirement_flows(path: Path) -> dict[str, str]:\n    if not path.is_file():\n        return {}\n\n    flows: dict[str, str] = {}\n    current_id: str | None = None\n    for raw in path.read_text(encoding="utf-8").splitlines():\n        line = raw.rstrip()\n        match = ENTRY_RE.match(line)\n        if match:\n            current_id = match.group(1)\n            continue\n        if current_id and line.startswith("- Flow:"):\n            flow = line.split(":", 1)[1].strip()\n            if not flow:\n                raise ValueError(f"Voice requirement Flow is empty for: {current_id}")\n            flows[current_id] = flow\n    return flows\n'''
    path.write_text(text.replace(needle, addition + needle, 1), encoding='utf-8')


ASSET_FLOWS = {
    ('Global / Shared Assets', 'Custodian Vex'): '01 — Shared Characters',
    ('Global / Shared Assets', 'Gremlin'): '01 — Shared Characters',
    ('The Antechamber', 'Custodian Key'): '01 — Arrival & Briefing',
    ('The Antechamber', 'First Objective Prompt'): '02 — Take Key & Open Seal',
    ('The Antechamber', 'First Seal Activation'): '02 — Take Key & Open Seal',
    ('The Resonance Engine', 'Objective 1 Instruction Panel'): '01 — Read Partial Target',
    ('The Resonance Engine', 'Partial Door Target Display'): '01 — Read Partial Target',
    ('The Resonance Engine', 'Pillar State Labels'): '03 — Experiment with Pillars',
    ('The Resonance Engine', 'Scattered Clue Book Set'): '02 — Search Clues',
    ('The Resonance Engine', 'Pillar Interaction Feedback'): '03 — Experiment with Pillars',
    ('The Resonance Engine', 'Resonance Engine Restoration'): '04 — Complete & Transition',
    ('The Broken Gallery', 'Objective 2 Instruction Panel'): '01 — Enter & Learn Route Loop',
    ('The Broken Gallery', 'Level 1 Brief'): '02 — Level 1',
    ('The Broken Gallery', 'Level 2 Brief'): '03 — Level 2',
    ('The Broken Gallery', 'Level 3 Time-Challenge Brief'): '04 — Level 3 Time Challenge',
    ('The Broken Gallery', 'Route Failure Message'): '05 — Retry / Route Closure',
    ('The Broken Gallery', 'Valid Placement Markers'): '01 — Enter & Learn Route Loop',
    ('The Broken Gallery', 'Level 3 Time-Challenge Cue'): '04 — Level 3 Time Challenge',
    ('The Broken Gallery', 'Level Retry Reset'): '05 — Retry / Route Closure',
    ('The Broken Gallery', 'Gremlin Route-Closed Event'): '05 — Retry / Route Closure',
    ('The Warden Halls', 'Echo Pebble'): '01 — Learn Trap Rules',
    ('The Warden Halls', 'Wall Laser Sensor'): '02 — Use Echo Pebble',
    ('The Warden Halls', 'Laser Blocker Stone'): '02 — Use Echo Pebble',
    ('The Warden Halls', 'Swinging Axe Trap'): '01 — Learn Trap Rules',
    ('The Warden Halls', 'Objective 3 Instruction Panel'): '01 — Learn Trap Rules',
    ('The Warden Halls', 'Echo Pebble Cooldown Indicator'): '02 — Use Echo Pebble',
    ('The Warden Halls', 'Trap Warning Readability'): '01 — Learn Trap Rules',
    ('The Warden Halls', 'Trap Hit Feedback'): '03 — Hazard Contact & Recovery',
    ('The Warden Halls', 'Checkpoint Recovery'): '03 — Hazard Contact & Recovery',
    ("The Gremlin's Workshop", 'Power Generator'): '01 — Learn Network / Ring 1',
    ("The Gremlin's Workshop", '90-Degree Rotator Junction'): '01 — Learn Network / Ring 1',
    ("The Gremlin's Workshop", 'Orrery Ring'): '02 — Extend to Ring 2',
    ("The Gremlin's Workshop", 'Objective 4 Instruction Panel'): '01 — Learn Network / Ring 1',
    ("The Gremlin's Workshop", 'Ring Progress Display'): '02 — Extend to Ring 2',
    ("The Gremlin's Workshop", 'First Sabotage Message'): '03 — Route Swap Sabotage',
    ("The Gremlin's Workshop", '50% Sabotage Message'): '04 — 50% Rollback',
    ("The Gremlin's Workshop", '80% Sabotage Message'): '05 — 80% Rollback',
    ("The Gremlin's Workshop", 'Ring 2 Route-Swap Sabotage'): '03 — Route Swap Sabotage',
    ("The Gremlin's Workshop", '50% Rotator Sabotage'): '04 — 50% Rollback',
    ("The Gremlin's Workshop", '80% Rotator Sabotage'): '05 — 80% Rollback',
    ("The Gremlin's Workshop", 'Great Orrery Restoration'): '06 — Restore Great Orrery',
    ('Vault Restored', 'Clockwork Wayfinder'): '01 — Restoration Payoff & Reward',
    ('Vault Restored', 'Completion Message'): '02 — Return Home',
    ('Vault Restored', 'Vault Awakening and Exit Reveal'): '01 — Restoration Payoff & Reward',
}

COPY_ADDITIONS = {
    ('The Resonance Engine', 'Pillar State Labels'): 'LEFT\nMIDDLE\nRIGHT\n\nSTEADY\nPULSE',
    ('The Broken Gallery', 'Valid Placement Markers'): 'BUILD HERE',
    ('The Warden Halls', 'Trap Warning Readability'): 'LASER SENSOR · PEBBLE WORKS\nHANGING STONE · PEBBLE WORKS\nFLOOR TRAP · AVOID\nSWINGING AXE · TIME YOUR MOVE',
}


def patch_asset_requirements() -> None:
    path = PROJECT / 'work/asset-requirements.md'
    lines = path.read_text(encoding='utf-8').splitlines()
    out: list[str] = []
    section = ''
    seen: set[tuple[str, str]] = set()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('## '):
            section = line[3:].strip()
            out.append(line)
            i += 1
            continue
        if line.startswith('#### '):
            title = line[5:].strip()
            key = (section, title)
            if key not in ASSET_FLOWS:
                raise SystemExit(f'missing asset flow mapping: {key}')
            seen.add(key)
            chunk = [line]
            i += 1
            while i < len(lines) and not lines[i].startswith(('## ', '### ', '#### ')):
                chunk.append(lines[i])
                i += 1
            if not any(row.startswith('Flow:') for row in chunk[1:]):
                chunk.insert(1, f'Flow: {ASSET_FLOWS[key]}')
            extra = COPY_ADDITIONS.get(key)
            if extra and not any(row.strip() == 'Content:' for row in chunk):
                while chunk and not chunk[-1].strip():
                    chunk.pop()
                chunk += ['', 'Content:', '```text', *extra.splitlines(), '```', '']
            out.extend(chunk)
            continue
        out.append(line)
        i += 1
    missing = sorted(set(ASSET_FLOWS) - seen)
    if missing:
        raise SystemExit(f'asset entries not found for flow mapping: {missing}')
    path.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')


VOICE_FLOWS = {
    'VO-ANTE-01': '01 — Arrival & Briefing',
    'VO-ANTE-02': '02 — Take Key & Open Seal',
    'VO-RES-01': '01 — Read Partial Target',
    'VO-GAL-01': '01 — Enter & Learn Route Loop',
    'VO-GAL-02': '04 — Level 3 Time Challenge',
    'VO-WARD-01': '01 — Learn Trap Rules',
    'VO-WARD-02': '04 — Complete & Transition',
    'VO-WORK-01': '01 — Learn Network / Ring 1',
    'VO-GREM-01': '03 — Route Swap Sabotage',
    'VO-WORK-02': '03 — Route Swap Sabotage',
    'VO-GREM-02': '04 — 50% Rollback',
    'VO-WORK-03': '04 — 50% Rollback',
    'VO-GREM-03': '05 — 80% Rollback',
    'VO-WORK-04': '05 — 80% Rollback',
    'VO-GREM-04': '06 — Restore Great Orrery',
    'VO-END-01': '01 — Restoration Payoff & Reward',
    'VO-END-02': '02 — Return Home',
}


def patch_voice_requirements() -> None:
    path = PROJECT / 'work/voice-requirements.md'
    lines = path.read_text(encoding='utf-8').splitlines()
    out: list[str] = []
    current_id: str | None = None
    seen: set[str] = set()
    for line in lines:
        if line.startswith('### '):
            current_id = line.split(' ', 2)[1]
            if current_id in VOICE_FLOWS:
                seen.add(current_id)
            out.append(line)
            continue
        out.append(line)
        if current_id in VOICE_FLOWS and line.startswith('- Trigger:'):
            if not (out and len(out) >= 2 and out[-2].startswith('- Flow:')):
                out.append(f'- Flow: {VOICE_FLOWS[current_id]}')
    missing = sorted(set(VOICE_FLOWS) - seen)
    if missing:
        raise SystemExit(f'voice IDs not found for flow mapping: {missing}')
    # De-duplicate Flow lines if this patch is ever replayed.
    cleaned: list[str] = []
    last_flow_for_entry = False
    for line in out:
        if line.startswith('### '):
            last_flow_for_entry = False
        if line.startswith('- Flow:'):
            if last_flow_for_entry:
                continue
            last_flow_for_entry = True
        cleaned.append(line)
    path.write_text('\n'.join(cleaned).rstrip() + '\n', encoding='utf-8')


def append_authority_state() -> None:
    source_path = PROJECT / 'state/source-inventory.yaml'
    source = source_path.read_text(encoding='utf-8')
    if 'id: SRC-009' not in source:
        source += '''\n  - id: SRC-009\n    type: instruction\n    role: authoritative\n    status: current\n    origin: user\n    inspection: full\n    summary: User requested Production Assets to be gameplay-flow-first rather than category-first. Each gameplay flow must combine every relevant implementation need in one place, including exact copy-ready UI text, Voice prompt text, audio cues, visual/presentation behavior, and models. Category labels are secondary only. Production Assets must provide quick-jump interaction and Copy actions so developers can go directly to the flow and production text they need.\n'''
        source_path.write_text(source, encoding='utf-8')

    req_path = PROJECT / 'state/requirement-register.yaml'
    req = req_path.read_text(encoding='utf-8')
    if 'id: REQ-017' not in req:
        req += '''\n  - id: REQ-017\n    area: production-assets\n    statement: Production Assets must be organized by gameplay flow within each objective/section, not by asset category. Each flow presents all implementation needs together; UI/player-facing strings and Voice prompts provide exact copy-ready text with Copy actions, while audio, visual/presentation, and model requirements show their implementation context/trigger in the same flow. Category names remain secondary badges. Pages provide quick-jump navigation to gameplay flows and may provide Copy Flow Text for all copy-ready content in that flow.\n    provenance: [SRC-009]\n    evidence_status: approved\n    recovery_class: none\n    approval_status: not_required\n    impact: high\n'''
        req_path.write_text(req, encoding='utf-8')


patch_voice_renderer()
patch_asset_requirements()
patch_voice_requirements()
append_authority_state()
print('Production Assets flow-first patch applied')
