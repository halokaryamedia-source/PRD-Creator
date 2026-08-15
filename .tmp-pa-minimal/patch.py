from __future__ import annotations

import re
from pathlib import Path

ROOT = Path('.')
PROJECT = ROOT / 'workspace/active/the-clockwork-vault'
OBJ = ROOT / 'kits/project-document-generator/renderer/production_assets_objective.py'
VOICE_RENDER = ROOT / 'kits/project-document-generator/renderer/production_assets.py'
ASSET = PROJECT / 'work/asset-requirements.md'
VOICE_REQ = PROJECT / 'work/voice-requirements.md'
SOURCE = PROJECT / 'state/source-inventory.yaml'
REQ = PROJECT / 'state/requirement-register.yaml'

FLOW_FOR = {
    ('Global / Shared Assets', '01 — Shared Characters'): 'Shared character assets used whenever Vex or Gremlin appears.',
    ('The Antechamber', '01 — Arrival & Briefing'): 'Opening character and key assets before the first objective starts.',
    ('The Antechamber', '02 — Take Key & Open Seal'): 'Key prompt, reminder, and seal-opening presentation.',
    ('The Resonance Engine', '01 — Read Partial Target'): 'Show the objective instructions and incomplete target when Objective 1 starts.',
    ('The Resonance Engine', '02 — Search Clues'): 'Provide the scattered book clues used to infer the missing target information.',
    ('The Resonance Engine', '03 — Experiment with Pillars'): 'Make pillar identity, color feedback, and pulse state readable while testing controls.',
    ('The Resonance Engine', '04 — Complete & Transition'): 'Confirm the solved pillar state and open the route to the Broken Gallery.',
    ('The Broken Gallery', '01 — Enter & Learn Route Loop'): 'Teach the search, repair, and checkpoint loop used throughout the Gallery.',
    ('The Broken Gallery', '02 — Level 1'): 'Present the Level 1 route choice and 12-block crossing rule.',
    ('The Broken Gallery', '03 — Level 2'): 'Present the Level 2 route choice and 20-block + 3-ladder rule.',
    ('The Broken Gallery', '04 — Level 3 Time Challenge'): 'Present the 50% timed-route challenge and its warning cue.',
    ('The Broken Gallery', '05 — Retry / Route Closure'): 'Explain local retry and clearly show when a failed Level 3 route closes.',
    ('The Warden Halls', '01 — Learn Trap Rules'): 'Introduce the Echo Pebble and distinguish laser, floor, and axe hazards.',
    ('The Warden Halls', '02 — Use Echo Pebble'): 'Support valid Pebble interactions, laser disable, blocker stones, and cooldown feedback.',
    ('The Warden Halls', '03 — Hazard Contact & Recovery'): 'Show trap-hit feedback and checkpoint recovery after gameplay health reaches zero.',
    ('The Warden Halls', '04 — Complete & Transition'): 'Close the Warden section and direct the player toward the Workshop.',
    ("The Gremlin's Workshop", '01 — Learn Network / Ring 1'): 'Teach the L-rotator rule and establish the first powered connection.',
    ("The Gremlin's Workshop", '02 — Extend to Ring 2'): 'Show live ring status while the same network extends to Ring 2.',
    ("The Gremlin's Workshop", '03 — Route Swap Sabotage'): 'Show and explain the Gremlin route-swap event after Ring 2.',
    ("The Gremlin's Workshop", '04 — 50% Rollback'): 'Show the first rollback when two Generator-to-Ring-1 rotators are changed.',
    ("The Gremlin's Workshop", '05 — 80% Rollback'): 'Show the second rollback when three Ring-1-to-Ring-2 rotators are changed.',
    ("The Gremlin's Workshop", '06 — Restore Great Orrery'): 'Present the final continuous-power success and Great Orrery restoration.',
    ('Vault Restored', '01 — Restoration Payoff & Reward'): 'Present the restored vault, Vex closing moment, and Clockwork Wayfinder reward.',
    ('Vault Restored', '02 — Return Home'): 'Tell the player the gateway is open and direct the final return route.',
}

ASSET_FOR = {
    'Custodian Vex': 'Main guide NPC for briefings, warnings, guidance, and the ending.',
    'Gremlin': 'Mischievous sabotage character used in authored disruption moments.',
    'Custodian Key': 'Opening progression item used to unlock the Resonance Engine seal.',
    'First Objective Prompt': 'Tell the player to take the Custodian Key and use it on the first seal.',
    'First Seal Activation': 'Make successful key use and the Objective 1 entrance opening unmistakable.',
    'Objective 1 Instruction Panel': 'Give the player the exact Objective 1 instructions without revealing the hidden solution.',
    'Partial Door Target Display': 'Show only Middle = Brown while Left, Right, and Pulse remain unknown.',
    'Pillar State Labels': 'Keep LEFT, MIDDLE, RIGHT and STEADY/PULSE states easy to read.',
    'Scattered Clue Book Set': 'Provide the 12 approved books used to infer the missing target information.',
    'Pillar Interaction Feedback': 'Show the immediate lamp result of lever and pressure-plate changes.',
    'Resonance Engine Restoration': 'Confirm Objective 1 completion and direct attention to the next route.',
    'Objective 2 Instruction Panel': 'Give the repeated Gallery loop: search barrels, repair marked gaps, reach checkpoint.',
    'Level 1 Brief': 'Tell the player the Level 1 route-count and 12-block requirement.',
    'Level 2 Brief': 'Tell the player the Level 2 route-count and 20-block + 3-ladder supply.',
    'Level 3 Time-Challenge Brief': 'Tell the player all routes initially work and 50% progress is required before time expires.',
    'Route Failure Message': 'Tell the player whether the active level resets or a Level 3 route is permanently lost for the run.',
    'Valid Placement Markers': 'Mark exactly where bridge blocks and ladders may be placed.',
    'Level 3 Time-Challenge Cue': 'Clearly signal the start of the Level 3 progress deadline.',
    'Level Retry Reset': 'Show a local level retry without making it feel like a full objective failure.',
    'Gremlin Route-Closed Event': 'Make the failed route visibly unavailable while alternatives remain readable.',
    'Echo Pebble': 'Reusable throwable tool for valid wall-laser and hanging-stone interactions.',
    'Wall Laser Sensor': 'Readable Pebble target with active and 4-second disabled states.',
    'Laser Blocker Stone': 'Alternate laser solution that drops into the beam after a valid Pebble hit.',
    'Swinging Axe Trap': 'Ceiling timing hazard with readable swing, hit, knockback, and reset states.',
    'Objective 3 Instruction Panel': 'Give the exact Pebble, laser, floor-trap, axe, and cooldown rules.',
    'Echo Pebble Cooldown Indicator': 'Show whether the unlimited Echo Pebble is READY or RECHARGING.',
    'Trap Warning Readability': 'Label hazard types only where the environment alone is not clear enough.',
    'Trap Hit Feedback': 'Make laser, floor, and axe hits visually distinguishable.',
    'Checkpoint Recovery': 'Return the player safely to the active Warden checkpoint after gameplay health reaches zero.',
    'Power Generator': 'Main power source with clear offline, live, and interrupted states.',
    '90-Degree Rotator Junction': 'Reusable L-junction showing route direction and powered/unpowered state.',
    'Orrery Ring': 'Reusable Ring 1–3 milestone asset with clear inactive and powered states.',
    'Objective 4 Instruction Panel': 'Give the exact continuous-network rule from Generator through Ring 3.',
    'Ring Progress Display': 'Show current live power state for Ring 1, Ring 2, and Ring 3.',
    'First Sabotage Message': 'Tell the player the old route is blocked and another path has opened.',
    '50% Sabotage Message': 'Tell the player Generator → Ring 1 lost alignment and two rotators changed.',
    '80% Sabotage Message': 'Tell the player Ring 1 → Ring 2 lost alignment and three rotators changed.',
    'Ring 2 Route-Swap Sabotage': 'Visually swap the active and alternate routes and show the resulting power loss.',
    '50% Rotator Sabotage': 'Visually turn exactly two earlier Generator → Ring 1 rotators out of alignment.',
    '80% Rotator Sabotage': 'Visually turn exactly three earlier Ring 1 → Ring 2 rotators out of alignment.',
    'Great Orrery Restoration': 'Show all rings synchronizing, power reaching the Orrery, and the exit beginning to open.',
    'Clockwork Wayfinder': 'One-time cosmetic completion reward shown in the ending.',
    'Completion Message': 'Confirm the vault is restored and direct the player to the open return route.',
    'Vault Awakening and Exit Reveal': 'Deliver the final restoration payoff, exit reveal, Vex moment, and reward handoff.',
}

VOICE_FOR = {
    'VO-ANTE-01': 'Opening briefing that explains the vault, Great Orrery, and four-system restoration goal.',
    'VO-ANTE-02': 'Short reminder if the player has not used the Custodian Key on the first seal.',
    'VO-RES-01': 'Objective 1 briefing for the partial target, scattered books, and pillar experimentation.',
    'VO-GAL-01': 'Gallery briefing for barrels, marked placements, limited supplies, and local retry.',
    'VO-GAL-02': 'Level 3 warning that explains the halfway threshold and route-loss consequence.',
    'VO-WARD-01': 'Warden briefing for Pebble targets, cooldown, laser disable, floor traps, and axes.',
    'VO-WARD-02': 'Short transition line after the final Warden checkpoint.',
    'VO-WORK-01': 'Workshop briefing for the Generator, L-rotators, and continuous Ring 1 → Ring 3 network.',
    'VO-GREM-01': 'Gremlin taunt when the Ring 2 route swap occurs.',
    'VO-WORK-02': 'Vex recovery guidance immediately after the route swap.',
    'VO-GREM-02': 'Gremlin taunt when the 50% rollback breaks the first connection.',
    'VO-WORK-03': 'Vex guidance to repair Generator → Ring 1 after the first rollback.',
    'VO-GREM-03': 'Gremlin taunt when the 80% rollback breaks the second connection.',
    'VO-WORK-04': 'Vex guidance to repair Ring 1 → Ring 2 after the second rollback.',
    'VO-GREM-04': 'Gremlin reaction when the player restores the full network despite sabotage.',
    'VO-END-01': 'Main completion speech after the Great Orrery and vault systems are restored.',
    'VO-END-02': 'Final navigation cue directing the player through the open gateway.',
}


def patch_voice_renderer() -> None:
    text = VOICE_RENDER.read_text(encoding='utf-8')
    if 'def parse_voice_requirement_for(' not in text:
        needle = '\ndef _voice_for(cast: dict[str, str], speaker: str) -> str:\n'
        addition = '''\n\ndef parse_voice_requirement_for(path: Path) -> dict[str, str]:\n    if not path.is_file():\n        return {}\n    values: dict[str, str] = {}\n    current_id: str | None = None\n    for raw in path.read_text(encoding="utf-8").splitlines():\n        line = raw.rstrip()\n        match = ENTRY_RE.match(line)\n        if match:\n            current_id = match.group(1)\n            continue\n        if current_id and line.startswith("- For:"):\n            value = line.split(":", 1)[1].strip()\n            if value:\n                values[current_id] = value\n    return values\n'''
        if needle not in text:
            raise SystemExit('voice renderer insertion point missing')
        text = text.replace(needle, addition + needle, 1)
        VOICE_RENDER.write_text(text, encoding='utf-8')


def patch_objective_renderer() -> None:
    text = OBJ.read_text(encoding='utf-8')
    text = text.replace('    flow: str = ""\n    requirement: str = ""', '    flow: str = ""\n    for_text: str = ""\n    requirement: str = ""', 1)
    text = text.replace('class FlowDefinition:\n    title: str\n    trigger:', 'class FlowDefinition:\n    title: str\n    for_text: str = ""\n    trigger:', 1)
    text = text.replace('                if meta.startswith("Trigger:"):', '                if meta.startswith("For:"):\n                    flow.for_text = meta.split(":", 1)[1].strip()\n                    list_mode = None\n                elif meta.startswith("Trigger:"):', 1)
    text = text.replace('            if not flow.trigger:\n                raise ValueError', '            if not flow.for_text:\n                raise ValueError(f"Gameplay Flow is missing For: {current_section.title} / {flow_title}")\n            if not flow.trigger:\n                raise ValueError', 1)
    text = text.replace('                if meta.startswith("Flow:"):\n                    entry.flow = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Requirement:"):', '                if meta.startswith("Flow:"):\n                    entry.flow = meta.split(":", 1)[1].strip()\n                elif meta.startswith("For:"):\n                    entry.for_text = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Requirement:"):', 1)
    text = text.replace('            if not entry.requirement:\n                raise ValueError(f"Production Asset is missing Requirement: {entry.title}")', '            if not entry.for_text:\n                raise ValueError(f"Production Asset is missing For: {entry.title}")\n            if not entry.requirement:\n                raise ValueError(f"Production Asset is missing Requirement: {entry.title}")', 1)

    start = text.index('def _purpose_text(')
    end = text.index('\ndef _pages_and_nav(', start)
    compact_helpers = '''def _category_label(category: str) -> str:\n    return {\n        "3D Models": "Model",\n        "UI & Information": "UI",\n        "Audio": "Audio",\n        "Visual Effects & Presentation": "VFX",\n    }.get(category, category)\n\n\ndef _asset_html(entry: AssetEntry, page_id: str) -> str:\n    copy_id = f"{page_id}-asset-copy-{slug(entry.title)}"\n    content = ""\n    if entry.content:\n        copy_label = "Player Text" if entry.category == "UI & Information" else "Copy-ready Text"\n        pre = f'<pre class="pa-content" id="{copy_id}">{esc(entry.content)}</pre>'\n        if len(entry.content) > 650 or entry.content.count("\\n") > 12:\n            pre = (\n                '<details class="pa-copy-details">'\n                '<summary>View Text</summary>' + pre + '</details>'\n            )\n        content = (\n            '<div class="pa-copy-block">'\n            '<div class="pa-copy-head">'\n            f'<span>{esc(copy_label)}</span>'\n            f'{_copy_button(copy_id, "Copy Text")}</div>'\n            f'{pre}</div>'\n        )\n    return (\n        '<article class="pa-asset-card">'\n        '<div class="pa-asset-head">'\n        f'<span class="pa-type-badge">{esc(_category_label(entry.category))}</span>'\n        f'<h4>{esc(entry.title)}</h4></div>'\n        f'<p class="pa-for"><span>For</span>{esc(entry.for_text)}</p>'\n        f'{content}</article>'\n    )\n\n\n'''
    text = text[:start] + compact_helpers + text[end+1:]

    # Add voice_for argument and obtain data.
    text = text.replace('    voice_flows: dict[str, str],\n) -> tuple[str, str]:', '    voice_flows: dict[str, str],\n    voice_for: dict[str, str],\n) -> tuple[str, str]:', 1)

    # Replace header block.
    old_header_start = text.index('        body = (\n            f\'<header class="pa-shell')
    old_header_end = text.index('\n\n        if voice_section and voice_doc:', old_header_start)
    new_header = '''        body = (\n            f'<header class="pa-shell {"voice-objective-shell" if voice_section else ""}">'\n            '<small>Production Assets</small>'\n            f'<h2>{esc(meta.title)}</h2><strong>{i18n(meta.package_label)}</strong>'\n            '<p class="pa-section-note">Assets and copy-ready content for this gameplay section. See 03 Development for mechanic and implementation details.</p>'\n            '</header>'\n        )'''
    text = text[:old_header_start] + new_header + text[old_header_end:]

    # Replace per-flow rendering block through before page creation.
    loop_start = text.index('        for flow_title in flow_titles:\n            flow = flow_defs[flow_title]')
    loop_end = text.index('\n\n        index = len(pages)', loop_start)
    new_loop = '''        for flow_title in flow_titles:\n            flow = flow_defs[flow_title]\n            flow_assets = grouped_assets.get(flow_title, [])\n            flow_voices = grouped_voices.get(flow_title, [])\n            flow_id = f"{meta.page_id}-flow-{slug(flow_title)}"\n            body += (\n                f'<div class="pa-flow" id="{flow_id}">'\n                '<div class="pa-flow-head">'\n                '<span>Gameplay Flow</span>'\n                f'<h3>{esc(flow_title)}</h3>'\n                f'<p><b>For</b>{esc(flow.for_text)}</p></div>'\n                '<div class="pa-assets">'\n            )\n            for entry in flow_assets:\n                body += _asset_html(entry, meta.page_id)\n            for entry in flow_voices:\n                trigger = triggers.get(entry.voice_id)\n                if not trigger:\n                    raise ValueError(\n                        f"Voice requirement Trigger missing for canonical production entry: {entry.voice_id}"\n                    )\n                for_text = voice_for.get(entry.voice_id)\n                if not for_text:\n                    raise ValueError(f"Voice requirement For missing for canonical production entry: {entry.voice_id}")\n                line_index, line_total = voice_positions[entry.voice_id]\n                body += (\n                    '<div class="pa-voice-inline">'\n                    '<span class="pa-type-badge">Voice</span>'\n                    f'<p class="pa-for"><span>For</span>{esc(for_text)}</p>'\n                    + voice._entry_html(\n                        entry,\n                        voice_number,\n                        line_index,\n                        line_total,\n                        meta.package_label,\n                        trigger,\n                    )\n                    + '</div>'\n                )\n                voice_number += 1\n            body += '</div></div>'\n'''
    text = text[:loop_start] + new_loop + text[loop_end:]

    # Replace style block.
    style_start = text.index("OBJECTIVE_STYLE = r'''<style id=\"production-assets-objective-style\">")
    style_end = text.index("</style>'''", style_start) + len("</style>'''")
    style = r'''OBJECTIVE_STYLE = r'''<style id="production-assets-objective-style">
.pa-shell{margin:0 0 12px}
.pa-shell>small{display:block;margin-bottom:6px;color:var(--blue);font-size:.62rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase}
.pa-shell h2{margin:0;color:var(--navy);font-size:1.9rem;line-height:1.12;letter-spacing:-.025em}
.pa-shell>strong{display:block;margin:5px 0 8px;color:var(--amber);font-size:.69rem;letter-spacing:.06em;text-transform:uppercase}
.pa-section-note{max-width:80ch;margin:0;color:var(--muted);font-size:.72rem;line-height:1.45}
.pa-flow-nav{display:flex;gap:7px;flex-wrap:wrap;margin:14px 0 2px}
.pa-flow-nav a{display:inline-flex;align-items:center;min-height:29px;padding:6px 9px;border:1px solid var(--line);border-radius:3px;background:var(--paper);color:var(--navy);font-size:.66rem;font-weight:750;text-decoration:none}
.pa-flow-nav a:hover,.pa-flow-nav a:focus-visible{border-color:var(--blue);color:var(--blue);outline:0}
.pa-flow{scroll-margin-top:74px;margin-top:20px;padding-top:2px}
.pa-flow+.pa-flow{padding-top:21px;border-top:2px solid var(--line)}
.pa-flow-head{margin-bottom:9px}
.pa-flow-head>span{display:block;margin-bottom:2px;color:var(--amber);font-size:.58rem;font-weight:850;letter-spacing:.08em;text-transform:uppercase}
.pa-flow-head h3{margin:0;color:var(--navy);font-size:1.1rem;line-height:1.25;text-transform:none}
.pa-flow-head p{margin:5px 0 0;color:#52616a;font-size:.75rem;line-height:1.45}
.pa-flow-head p b,.pa-for>span{margin-right:6px;color:var(--blue);font-size:.58rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase}
.pa-assets{display:grid;gap:8px}
.pa-asset-card,.pa-voice-inline{padding:12px 13px;border:1px solid #d8e1e5;border-radius:4px;background:var(--paper);break-inside:avoid}
.pa-asset-head{display:flex;align-items:center;gap:8px}
.pa-type-badge{display:inline-flex;align-items:center;min-height:20px;padding:2px 6px;border-radius:2px;background:var(--soft);color:var(--blue);font-size:.56rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase}
.pa-asset-head h4{margin:0;color:var(--navy);font-size:.93rem;line-height:1.3;text-transform:none}
.pa-for{margin:6px 0 0;color:#52616a;font-size:.75rem;line-height:1.45}
.pa-copy-block{margin-top:9px}
.pa-copy-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:5px}
.pa-copy-head>span{color:var(--blue);font-size:.57rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase}
.pa-content{margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:2px;background:#f8fafb;color:var(--navy);font:700 .78rem/1.5 var(--font);white-space:pre-wrap;overflow-wrap:anywhere}
.pa-copy-details{margin:0}
.pa-copy-details summary{cursor:pointer;color:var(--blue);font-size:.68rem;font-weight:800;margin:2px 0 6px}
.pa-copy-button{display:inline-flex;align-items:center;justify-content:center;min-height:28px;padding:6px 8px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .58rem/1 var(--font);letter-spacing:.045em;text-transform:uppercase;cursor:pointer;white-space:nowrap}
.pa-copy-button:hover,.pa-copy-button:focus-visible{border-color:var(--blue);background:var(--blue);outline:0}
.pa-copy-button.is-copied{border-color:var(--green);background:var(--green)}
.pa-voice-setup-block{margin:10px 0 0}
.pa-voice-inline>.pa-type-badge{margin-bottom:0}
.pa-voice-inline .voice-script-card{margin-top:7px;border:0;border-top:1px solid var(--line);border-radius:0}
.pa-voice-inline .voice-script-index,.pa-voice-inline .voice-script-position,.pa-voice-inline .voice-script-context{display:none!important}
.pa-voice-inline .voice-script-card-head{padding:10px 0 8px}
.pa-voice-inline .voice-script-display{padding:11px 0 2px;border-top:1px solid var(--line)}
.pa-voice-inline .voice-script-heading h4{font-size:.91rem}
body.theme-dark .pa-section-note,body.theme-dark .pa-flow-head p,body.theme-dark .pa-for{color:#c8d7dc}
body.theme-dark .pa-type-badge{background:#1d2f37}
body.theme-dark .pa-asset-card,body.theme-dark .pa-voice-inline{border-color:#405761;background:#17262d}
body.theme-dark .pa-content{background:#1d2f37;color:#e8eff3}
@media(max-width:760px){.pa-copy-head{align-items:flex-start}.pa-flow-nav{gap:5px}}
@media print{.pa-flow-nav,.pa-copy-button{display:none!important}.pa-asset-card,.pa-voice-inline,.pa-flow{break-inside:avoid}}
</style>''' '''
    # strip accidental outer spaces from raw construction
    style = style.strip()
    text = text[:style_start] + style + text[style_end:]

    # Parse voice For values and pass them through.
    text = text.replace('    voice_flows = voice.parse_voice_requirement_flows(requirements_path) if has_voice else {}', '    voice_flows = voice.parse_voice_requirement_flows(requirements_path) if has_voice else {}\n    voice_for = voice.parse_voice_requirement_for(requirements_path) if has_voice else {}', 1)
    text = text.replace('    pages, nav = _pages_and_nav(render_data, assets, voice_doc, triggers, voice_flows)', '    pages, nav = _pages_and_nav(render_data, assets, voice_doc, triggers, voice_flows, voice_for)', 1)
    OBJ.write_text(text, encoding='utf-8')


def patch_asset_source() -> None:
    lines = [line for line in ASSET.read_text(encoding='utf-8').splitlines() if not line.startswith('For:')]
    out: list[str] = []
    section = ''
    asset_title: str | None = None
    for line in lines:
        if line.startswith('## '):
            section = line[3:].strip()
            asset_title = None
        if line.startswith('#### '):
            asset_title = line[5:].strip()
        out.append(line)
        if line.startswith('### Gameplay Flow '):
            flow = line[len('### Gameplay Flow '):].strip()
            value = FLOW_FOR.get((section, flow))
            if not value:
                raise SystemExit(f'missing flow For mapping: {section} / {flow}')
            out.append(f'For: {value}')
        elif line.startswith('Flow:') and asset_title:
            value = ASSET_FOR.get(asset_title)
            if not value:
                raise SystemExit(f'missing asset For mapping: {asset_title}')
            out.append(f'For: {value}')
    ASSET.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')


def patch_voice_source() -> None:
    lines = [line for line in VOICE_REQ.read_text(encoding='utf-8').splitlines() if not line.startswith('- For:')]
    out: list[str] = []
    current_id: str | None = None
    for line in lines:
        m = re.match(r'^###\s+([A-Za-z0-9][A-Za-z0-9-]*)\s+[—-]\s+', line)
        if m:
            current_id = m.group(1)
        out.append(line)
        if line.startswith('- Flow:') and current_id:
            value = VOICE_FOR.get(current_id)
            if not value:
                raise SystemExit(f'missing voice For mapping: {current_id}')
            out.append(f'- For: {value}')
    VOICE_REQ.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')


def patch_authority() -> None:
    source = SOURCE.read_text(encoding='utf-8')
    if 'id: SRC-011' not in source:
        source = source.rstrip() + '''\n  - id: SRC-011\n    type: instruction\n    role: authoritative\n    status: current\n    origin: user\n    inspection: full\n    summary: User requested a more concise Production Assets presentation. Development already owns mechanic and implementation detail, so Production Assets should avoid repeating Trigger, Player Experience, Implementation Checklist, Done When, or long context. Each gameplay flow should show only a short For statement, then the asset name/type, a short For statement explaining its purpose, and exact copy-ready player text or Voice prompt when applicable. Quick Jump remains useful; Copy Flow Text remains excluded.\n'''
        SOURCE.write_text(source, encoding='utf-8')
    req = REQ.read_text(encoding='utf-8')
    pattern = re.compile(r'(  - id: REQ-017\n    area: production-assets\n    statement: ).*?(\n    provenance: )')
    replacement = (r'\1Production Assets is a concise companion to Development rather than a second implementation specification. Organize by gameplay flow and retain Quick Jump, but show only a short For statement for the flow, then each asset with its secondary type badge, name, and short For statement. Exact player-facing text and Voice prompts keep their per-item Copy actions. Do not show duplicated Trigger, Player Experience, Implementation Checklist, Done When, long objective context, asset-count summaries, asset numbering, category-first grouping, or Copy Flow Text.\2')
    req, count = pattern.subn(replacement, req, count=1)
    if count != 1:
        raise SystemExit('REQ-017 replacement failed')
    req = req.replace('provenance: [SRC-009, SRC-010]', 'provenance: [SRC-009, SRC-010, SRC-011]', 1)
    REQ.write_text(req, encoding='utf-8')


patch_voice_renderer()
patch_objective_renderer()
patch_asset_source()
patch_voice_source()
patch_authority()
print('concise Production Assets patch applied')
