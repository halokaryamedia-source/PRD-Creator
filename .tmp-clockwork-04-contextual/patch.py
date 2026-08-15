from pathlib import Path
import re

ROOT = Path('.')
PROJECT = ROOT / 'workspace/active/the-clockwork-vault'
ASSET = PROJECT / 'work/asset-requirements.md'
VOICE_REQ = PROJECT / 'work/voice-requirements.md'
SOURCE = PROJECT / 'state/source-inventory.yaml'
REQ = PROJECT / 'state/requirement-register.yaml'
RENDERER = ROOT / 'kits/project-document-generator/renderer/production_assets_objective.py'

# Presentation metadata only. Gameplay truth remains owned by Development/source requirements.
GROUPS = {
('Global / Shared Assets','Custodian Vex'): ('01 — Shared Characters','Throughout the full adventure.'),
('Global / Shared Assets','Gremlin'): ('01 — Shared Characters','Broken Gallery final crossing and Objective 4 sabotage moments.'),
('The Antechamber','Custodian Key'): ('01 — Opening Story','Antechamber opening and the first seal.'),
('The Antechamber','Custodian Key Prompt'): ('02 — Open First Seal','After the opening briefing, until the first seal opens.'),
('The Antechamber','Resonance Engine Seal Opening'): ('02 — Open First Seal','When the Custodian Key is accepted by the first seal.'),
('The Resonance Engine','Objective 1 Instruction Panel'): ('01 — Chamber Guidance','When the player enters the Resonance Engine.'),
('The Resonance Engine','Partial Door Target Display'): ('01 — Chamber Guidance','Throughout Objective 1.'),
('The Resonance Engine','Scattered Clue Book Set'): ('02 — Clue Set','Throughout the chamber search.'),
('The Resonance Engine','Pillar Lamp Feedback'): ('03 — Pillar Interaction','Whenever the player tests a pillar control.'),
('The Resonance Engine','Resonance Engine Restoration'): ('04 — Completion','When the complete pillar state is solved.'),
('The Broken Gallery','Broken Gallery Entrance Message'): ('01 — Shared Gallery Assets','When the player first enters the Broken Gallery.'),
('The Broken Gallery','Repair Gap Markers'): ('01 — Shared Gallery Assets','Across all three Gallery crossings.'),
('The Broken Gallery','First Crossing Message'): ('02 — First Crossing','At the first Gallery crossing.'),
('The Broken Gallery','Second Crossing Message'): ('03 — Second Crossing','At the second Gallery crossing.'),
('The Broken Gallery',"Gremlin's Wager Message"): ('04 — Gremlin’s Wager','Before the final Gallery crossing begins.'),
('The Broken Gallery','Gremlin Wager Cue'): ('04 — Gremlin’s Wager','When the final crossing becomes timed.'),
('The Broken Gallery','Crossing Failure Messages'): ('05 — Path Failure','After a Gallery crossing fails.'),
('The Broken Gallery','Gremlin Path Collapse'): ('05 — Path Failure','When Gremlin takes a failed final path away.'),
('The Warden Halls','Echo Pebble'): ('01 — Core Trap Kit','Throughout the Warden Halls.'),
('The Warden Halls','Wall Laser Sensor'): ('01 — Core Trap Kit','Across all Warden levels.'),
('The Warden Halls','Laser Blocker Stone'): ('01 — Core Trap Kit','Selected laser encounters.'),
('The Warden Halls','Swinging Axe Trap'): ('01 — Core Trap Kit','Across the Warden Halls.'),
('The Warden Halls','Floor Trap'): ('01 — Core Trap Kit','Across the Warden Halls.'),
('The Warden Halls','Warden Halls Entrance Message'): ('02 — Player Communication','When the player enters the Warden Halls.'),
('The Warden Halls','Echo Pebble HUD'): ('02 — Player Communication','While the Echo Pebble is available.'),
('The Warden Halls','Warden Hit Effects'): ('04 — Gameplay Feedback','Whenever a laser, floor trap, or axe hits the player.'),
('The Warden Halls','Warden Recovery'): ('04 — Gameplay Feedback','When Warden hazards defeat the player.'),
("The Gremlin's Workshop",'Power Generator'): ('01 — Core Network Kit','Throughout Objective 4.'),
("The Gremlin's Workshop",'90-Degree Rotator Junction'): ('01 — Core Network Kit','Throughout Objective 4.'),
("The Gremlin's Workshop",'Orrery Ring'): ('01 — Core Network Kit','Throughout Objective 4.'),
("The Gremlin's Workshop",'Orrery Ring Status'): ('01 — Core Network Kit','Throughout Objective 4.'),
("The Gremlin's Workshop",'Workshop Entrance Message'): ('02 — Workshop Intro','When the player enters the Workshop.'),
("The Gremlin's Workshop",'Route Swap Message'): ('03 — Gremlin Route Swap','When Gremlin blocks the old route after Ring Two.'),
("The Gremlin's Workshop",'Gremlin Route Swap'): ('03 — Gremlin Route Swap','When the route-swap sabotage occurs.'),
("The Gremlin's Workshop",'First Rollback Message'): ('04 — First Sabotage','When Ring One loses power from Gremlin’s first rollback.'),
("The Gremlin's Workshop",'First Rollback Sabotage'): ('04 — First Sabotage','At the first authored rollback event.'),
("The Gremlin's Workshop",'Second Rollback Message'): ('05 — Second Sabotage','When Ring Two loses power from Gremlin’s second rollback.'),
("The Gremlin's Workshop",'Second Rollback Sabotage'): ('05 — Second Sabotage','At the second authored rollback event.'),
("The Gremlin's Workshop",'Great Orrery Restoration'): ('06 — Final Restoration','When the full power network is restored.'),
('Vault Restored','Clockwork Wayfinder'): ('01 — Finale','During the final reward reveal.'),
('Vault Restored','Vault Restored Message'): ('01 — Finale','When the restored gateway opens.'),
('Vault Restored','Vault Awakening Sequence'): ('01 — Finale','Immediately after the Great Orrery is restored.'),
}

VOICE_GROUPS = {
'VO-ANTE-01': ('01 — Opening Story','When the player first enters the Antechamber.'),
'VO-ANTE-02': ('02 — Open First Seal','If the first seal is still closed after the opening briefing.'),
'VO-RES-01': ('01 — Chamber Guidance','When the player enters the Resonance Engine.'),
'VO-GAL-01': ('01 — Shared Gallery Assets','When the player first enters the Broken Gallery.'),
'VO-GAL-02': ('04 — Gremlin’s Wager','Before the final Gallery crossing begins.'),
'VO-WARD-01': ('03 — Voice','When the player enters the Warden Halls.'),
'VO-WARD-02': ('05 — Transition','After the final Warden section is cleared.'),
'VO-WORK-01': ('02 — Workshop Intro','When the player first sees the Orrery power system.'),
'VO-GREM-01': ('03 — Gremlin Route Swap','When Gremlin blocks the old route.'),
'VO-WORK-02': ('03 — Gremlin Route Swap','Immediately after Ring Two loses power.'),
'VO-GREM-02': ('04 — First Sabotage','When Gremlin breaks the earlier line to Ring One.'),
'VO-WORK-03': ('04 — First Sabotage','Immediately after the first sabotage.'),
'VO-GREM-03': ('05 — Second Sabotage','When Gremlin breaks the earlier line to Ring Two.'),
'VO-WORK-04': ('05 — Second Sabotage','Immediately after the second sabotage.'),
'VO-GREM-04': ('06 — Final Restoration','When the Great Orrery begins to wake.'),
'VO-END-01': ('01 — Finale','After the Great Orrery and vault systems are restored.'),
'VO-END-02': ('01 — Finale','When the gateway home is open.'),
}


def insert_floor_trap(text: str) -> str:
    if '\n#### Floor Trap\n' in text:
        return text
    start = text.index('\n## The Warden Halls\n')
    end = text.index('\n## The Gremlin', start)
    chunk = text[start:end]
    marker = '\n### UI & Information\n'
    if marker not in chunk:
        raise SystemExit('Warden UI marker not found')
    block = '''\n#### Floor Trap\nFlow: 01 — Enter the Warden Halls\nFor: The ground hazard the player must avoid.\nRequirement: Create one readable floor-trap treatment with Armed, Triggered, and Reset states. It must stay visually distinct from wall sensors and must never suggest that Echo Pebble can disable it. Exact damage and status effects remain in 03 Development.\nUsage: Distributed across the Warden levels as an avoid-only ground hazard.\n'''
    chunk = chunk.replace(marker, block + marker, 1)
    return text[:start] + chunk + text[end:]


def add_asset_metadata(text: str) -> str:
    lines = text.splitlines()
    out = []
    section = ''
    entry = ''
    i = 0
    seen = set()
    while i < len(lines):
        line = lines[i]
        if line.startswith('## '):
            section = line[3:].strip()
            entry = ''
            out.append(line); i += 1; continue
        if line.startswith('#### '):
            entry = line[5:].strip()
            out.append(line); i += 1; continue
        if entry and line.startswith('Flow:'):
            out.append(line)
            key = (section, entry)
            if key not in GROUPS:
                raise SystemExit(f'missing Group/Used mapping: {key}')
            group, used = GROUPS[key]
            # Remove stale metadata if already present on a rerun.
            j = i + 1
            while j < len(lines) and (lines[j].startswith('Group:') or lines[j].startswith('Used:')):
                j += 1
            out.append(f'Group: {group}')
            out.append(f'Used: {used}')
            seen.add(key)
            i = j
            continue
        out.append(line); i += 1
    missing = set(GROUPS) - seen
    if missing:
        raise SystemExit('mapped assets not found: ' + ', '.join(map(str, sorted(missing))))
    return '\n'.join(out) + '\n'


def patch_assets():
    text = ASSET.read_text(encoding='utf-8')
    text = insert_floor_trap(text)
    text = text.replace('Uses: Custodian Vex; Echo Pebble; Wall Laser Sensor; Swinging Axe Trap; Warden Halls Entrance Message',
                        'Uses: Custodian Vex; Echo Pebble; Wall Laser Sensor; Swinging Axe Trap; Floor Trap; Warden Halls Entrance Message')
    text = text.replace('Uses: Warden Hit Effects; Checkpoint Recovery; active Warden checkpoint',
                        'Uses: Warden Hit Effects; Warden Recovery; active Warden checkpoint')
    ASSET.write_text(add_asset_metadata(text), encoding='utf-8')


def patch_voice_requirements():
    lines = VOICE_REQ.read_text(encoding='utf-8').splitlines()
    out=[]; current=None; seen=set(); i=0
    entry_re=re.compile(r'^###\s+(VO-[A-Z0-9-]+)\s+[—-]')
    while i < len(lines):
        line=lines[i]
        m=entry_re.match(line)
        if m:
            current=m.group(1)
            out.append(line); i+=1; continue
        if current and line.startswith('- Flow:'):
            out.append(line)
            if current not in VOICE_GROUPS:
                raise SystemExit(f'missing voice Group/Used mapping: {current}')
            group, used=VOICE_GROUPS[current]
            j=i+1
            while j < len(lines) and (lines[j].startswith('- Group:') or lines[j].startswith('- Used:')):
                j+=1
            out.append(f'- Group: {group}')
            out.append(f'- Used: {used}')
            seen.add(current); i=j; continue
        out.append(line); i+=1
    if set(VOICE_GROUPS)-seen:
        raise SystemExit('voice metadata missing IDs: '+', '.join(sorted(set(VOICE_GROUPS)-seen)))
    VOICE_REQ.write_text('\n'.join(out)+'\n', encoding='utf-8')


def patch_renderer():
    text=RENDERER.read_text(encoding='utf-8')
    text=text.replace('    flow: str = ""\n    for_text: str = ""', '    flow: str = ""\n    group: str = ""\n    used: str = ""\n    for_text: str = ""', 1)
    text=text.replace('                if meta.startswith("Flow:"):\n                    entry.flow = meta.split(":", 1)[1].strip()\n                elif meta.startswith("For:"):',
                      '                if meta.startswith("Flow:"):\n                    entry.flow = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Group:"):\n                    entry.group = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Used:"):\n                    entry.used = meta.split(":", 1)[1].strip()\n                elif meta.startswith("For:"):',1)
    text=text.replace('            if not entry.for_text:\n                raise ValueError(f"Production Asset is missing For: {entry.title}")',
                      '            if not entry.group:\n                entry.group = entry.flow\n            if not entry.used:\n                entry.used = entry.usage or entry.flow\n            if not entry.for_text:\n                raise ValueError(f"Production Asset is missing For: {entry.title}")',1)
    text=text.replace('        "Swinging Axe Trap": "MODEL / ANIMATION",', '        "Swinging Axe Trap": "MODEL / ANIMATION",\n        "Floor Trap": "MODEL / PRESENTATION",',1)

    # Replace compact row renderer to show contextual Used + Purpose.
    start=text.index('def _asset_html(')
    end=text.index('\n\ndef _voice_html(', start)
    asset_func='''def _asset_html(entry: AssetEntry, page_id: str) -> str:\n    copy_id = f"{page_id}-asset-copy-{slug(entry.title)}"\n    type_label = _category_label(entry.category, entry.title)\n    actions = ""\n    detail = ""\n    if entry.content:\n        actions = _copy_button(copy_id, "Copy Text")\n        short_copy = len(entry.content) <= 320 and entry.content.count("\\n") <= 7\n        if short_copy:\n            detail = (\n                '<div class="pa-row-copy pa-row-copy-open">'\n                f'<pre class="pa-content" id="{copy_id}">{esc(entry.content)}</pre>'\n                '</div>'\n            )\n        else:\n            detail = (\n                '<details class="pa-row-details">'\n                '<summary>View Text</summary>'\n                f'<pre class="pa-content" id="{copy_id}">{esc(entry.content)}</pre>'\n                '</details>'\n            )\n    return (\n        '<article class="pa-row">'\n        '<div class="pa-row-main">'\n        f'<span class="pa-type">{esc(type_label)}</span>'\n        '<div class="pa-row-info">'\n        f'<h4>{esc(entry.title)}</h4>'\n        f'<p class="pa-meta"><span>Used</span>{esc(entry.used)}</p>'\n        f'<p class="pa-meta"><span>Purpose</span>{esc(entry.for_text)}</p>'\n        '</div>'\n        f'<div class="pa-row-actions">{actions}</div>'\n        '</div>'\n        f'{detail}'\n        '</article>'\n    )\n'''
    text=text[:start]+asset_func+text[end:]

    # Replace voice renderer signature/body.
    start=text.index('def _voice_html(')
    end=text.index('\n\ndef _shared_voice_cast_html', start)
    voice_func='''def _voice_html(\n    entry: voice.VoiceEntry,\n    doc: voice.VoiceProduction,\n    for_text: str,\n    used_text: str,\n) -> str:\n    prompt_id = f"voice-prompt-{slug(entry.voice_id)}"\n    selected_voice = voice._voice_for(doc.cast, entry.speaker)\n    return (\n        '<article class="pa-row pa-row-voice">'\n        '<div class="pa-row-main">'\n        '<span class="pa-type pa-type-voice">VOICE</span>'\n        '<div class="pa-row-info">'\n        f'<h4>{esc(entry.speaker)} — {esc(entry.title)}</h4>'\n        f'<p class="pa-meta"><span>Used</span>{esc(used_text)}</p>'\n        f'<p class="pa-meta"><span>Purpose</span>{esc(for_text)}</p>'\n        f'<small>{esc(selected_voice)} · {esc(entry.duration)}</small>'\n        '</div>'\n        '<div class="pa-row-actions">'\n        f'<button class="voice-copy-button" data-voice-copy="{esc(prompt_id)}" type="button">'\n        '<span class="voice-copy-label">Copy Prompt</span></button>'\n        '</div>'\n        '</div>'\n        '<details class="pa-row-details pa-voice-details">'\n        '<summary>View Prompt</summary>'\n        f'<pre class="voice-script-text" id="{esc(prompt_id)}">{esc(entry.performance)}</pre>'\n        f'<div class="voice-script-display">{voice._performance_html(entry.performance)}</div>'\n        '</details>'\n        '</article>'\n    )\n'''
    text=text[:start]+voice_func+text[end:]

    # Add generic voice metadata parser and group display helper before _pages_and_nav.
    marker='\ndef _pages_and_nav('
    helper='''\ndef _parse_voice_requirement_field(path: Path, label: str) -> dict[str, str]:\n    values: dict[str, str] = {}\n    current: str | None = None\n    entry_re = re.compile(r"^###\\s+([A-Za-z0-9][A-Za-z0-9-]*)\\s+[—-]")\n    for raw in path.read_text(encoding="utf-8").splitlines():\n        line = raw.rstrip()\n        match = entry_re.match(line)\n        if match:\n            current = match.group(1)\n            continue\n        prefix = f"- {label}:"\n        if current and line.startswith(prefix):\n            value = line.split(":", 1)[1].strip()\n            if value:\n                values[current] = value\n    return values\n\n\ndef _group_display(label: str) -> str:\n    return re.sub(r"^\\s*\\d+\\s*[—-]\\s*", "", label).strip()\n\n'''
    text=text.replace(marker, helper+marker,1)

    # Extend function args.
    text=text.replace('    voice_for: dict[str, str],\n) -> tuple[str, str]:', '    voice_for: dict[str, str],\n    voice_groups: dict[str, str],\n    voice_used: dict[str, str],\n) -> tuple[str, str]:',1)

    # Replace grouping/render core from grouped_assets through before index assignment.
    core_start=text.index('        grouped_assets: dict[str, list[AssetEntry]] = {}')
    core_end=text.index('\n        index = len(pages)', core_start)
    core='''        grouped_assets: dict[str, list[AssetEntry]] = {}\n        for entry in asset_entries:\n            grouped_assets.setdefault(entry.group, []).append(entry)\n\n        grouped_voices: dict[str, list[voice.VoiceEntry]] = {}\n        for entry in voice_entries:\n            group = voice_groups.get(entry.voice_id)\n            if not group:\n                raise ValueError(f"Voice requirement Group missing for canonical production entry: {entry.voice_id}")\n            grouped_voices.setdefault(group, []).append(entry)\n\n        group_titles = sorted(set(grouped_assets) | set(grouped_voices), key=_flow_sort_key)\n\n        body = (\n            '<header class="pa-shell">'\n            '<small>Production Assets</small>'\n            f'<h2>{esc(meta.title)}</h2><strong>{i18n(meta.package_label)}</strong>'\n            '<p class="pa-section-note">Concrete production assets and exact in-game copy. Mechanics stay in 03 Development.</p>'\n            '</header>'\n        )\n        if key == voice._title_key(SHARED_SECTION):\n            body += _shared_voice_cast_html(voice_doc)\n\n        if len(group_titles) > 1:\n            body += '<nav class="pa-group-nav" aria-label="Production groups"><span>Jump to</span>'\n            for group_title in group_titles:\n                group_id = f"{meta.page_id}-group-{slug(group_title)}"\n                body += f'<a href="#{esc(group_id)}">{esc(_group_display(group_title))}</a>'\n            body += '</nav>'\n\n        for group_title in group_titles:\n            group_id = f"{meta.page_id}-group-{slug(group_title)}"\n            body += (\n                f'<div class="pa-group" id="{esc(group_id)}">'\n                f'<h3>{esc(_group_display(group_title))}</h3>'\n                '<div class="pa-rows">'\n            )\n            for entry in grouped_assets.get(group_title, []):\n                body += _asset_html(entry, meta.page_id)\n            for entry in grouped_voices.get(group_title, []):\n                for_text = voice_for.get(entry.voice_id)\n                used_text = voice_used.get(entry.voice_id)\n                if not for_text or not used_text:\n                    raise ValueError(f"Voice requirement For/Used missing for canonical production entry: {entry.voice_id}")\n                if voice_doc is None:\n                    raise ValueError("Voice entry exists without Voice Production document.")\n                body += _voice_html(entry, voice_doc, for_text, used_text)\n            body += '</div></div>'\n'''
    text=text[:core_start]+core+text[core_end:]

    # Replace CSS block with visible vertical group layout; no tabs/hiding.
    style_start=text.index("OBJECTIVE_STYLE = r'''<style id=\"production-assets-objective-style\">")
    style_end=text.index("</style>'''", style_start)+len("</style>'''")
    style="""OBJECTIVE_STYLE = r'''<style id=\"production-assets-objective-style\">\n.pa-shell{margin:0 0 14px}\n.pa-shell>small{display:block;margin-bottom:6px;color:var(--blue);font-size:.62rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase}\n.pa-shell h2{margin:0;color:var(--navy);font-size:1.9rem;line-height:1.12;letter-spacing:-.025em}\n.pa-shell>strong{display:block;margin:5px 0 7px;color:var(--amber);font-size:.69rem;letter-spacing:.06em;text-transform:uppercase}\n.pa-section-note{max-width:78ch;margin:0;color:var(--muted);font-size:.72rem;line-height:1.45}\n.pa-cast{margin:14px 0 18px;border:1px solid var(--line);border-radius:5px;overflow:hidden}\n.pa-cast-head{display:flex;align-items:baseline;gap:10px;padding:9px 12px;background:var(--soft);border-bottom:1px solid var(--line)}\n.pa-cast-head span{color:var(--navy);font-size:.72rem;font-weight:850;text-transform:uppercase;letter-spacing:.06em}.pa-cast-head p{margin:0;color:var(--muted);font-size:.69rem}\n.pa-cast-row{display:grid;grid-template-columns:minmax(120px,.8fr) minmax(0,2fr) auto;gap:12px;align-items:center;padding:9px 12px;border-top:1px solid var(--line);font-size:.72rem}.pa-cast-row:first-child{border-top:0}.pa-cast-row strong{color:var(--navy)}.pa-cast-row small{color:var(--muted)}\n.pa-group-nav{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin:14px 0 2px;padding-bottom:10px;border-bottom:1px solid var(--line)}\n.pa-group-nav>span{margin-right:3px;color:var(--muted);font-size:.61rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em}\n.pa-group-nav a{display:inline-flex;padding:5px 8px;border:1px solid var(--line);border-radius:3px;color:var(--navy);background:var(--paper);font-size:.64rem;font-weight:750;text-decoration:none}.pa-group-nav a:hover,.pa-group-nav a:focus-visible{border-color:var(--blue);color:var(--blue);outline:0}\n.pa-group{scroll-margin-top:72px;margin-top:22px}.pa-group+.pa-group{padding-top:18px;border-top:2px solid var(--line)}\n.pa-group h3{margin:0 0 8px;color:var(--navy);font-size:1.04rem;line-height:1.25;text-transform:none}\n.pa-rows{border-top:1px solid #cbd7dd}.pa-row{border-bottom:1px solid #cbd7dd;background:var(--paper)}\n.pa-row-main{display:grid;grid-template-columns:122px minmax(0,1fr) auto;gap:13px;align-items:start;padding:12px 8px}\n.pa-type{display:inline-flex;align-items:center;width:max-content;max-width:116px;padding:4px 7px;border-radius:3px;background:var(--soft);color:var(--blue);font-size:.59rem;font-weight:900;letter-spacing:.055em;line-height:1.25;text-transform:uppercase}.pa-type-voice{color:#9a5a0a;background:#fff5df}\n.pa-row-info h4{margin:0 0 5px;color:var(--navy);font-size:.87rem;line-height:1.3;text-transform:none}.pa-row-info small{display:block;margin-top:5px;color:var(--muted);font-size:.62rem}\n.pa-meta{display:grid;grid-template-columns:54px minmax(0,1fr);gap:7px;margin:2px 0;color:#52616a;font-size:.7rem;line-height:1.4}.pa-meta span{color:var(--blue);font-size:.56rem;font-weight:850;letter-spacing:.05em;text-transform:uppercase}\n.pa-row-actions{display:flex;align-items:center;gap:6px;justify-content:flex-end;padding-top:1px}\n.pa-copy-button,.pa-row .voice-copy-button{display:inline-flex;align-items:center;justify-content:center;min-height:28px;padding:6px 8px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .57rem/1 var(--font);letter-spacing:.04em;text-transform:uppercase;cursor:pointer;white-space:nowrap}.pa-copy-button:hover,.pa-copy-button:focus-visible,.pa-row .voice-copy-button:hover,.pa-row .voice-copy-button:focus-visible{background:var(--blue);border-color:var(--blue);outline:0}\n.pa-row-copy,.pa-row-details{margin:0 8px 10px 143px}.pa-row-details{padding-top:0}.pa-row-details summary{display:inline-flex;cursor:pointer;color:var(--blue);font-size:.66rem;font-weight:800;margin:0 0 7px;user-select:none}\n.pa-content,.pa-row .voice-script-text{margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:3px;background:#f8fafb;color:var(--navy);font:700 .76rem/1.52 var(--font);white-space:pre-wrap;overflow-wrap:anywhere}.pa-row .voice-script-text{display:block!important;border-left-color:var(--amber)}\n.pa-row .voice-script-display{margin-top:7px;padding:8px 0 0;border-top:1px solid var(--line)}.pa-row .voice-performance-tag{font-size:.57rem}.pa-row .voice-script-line{font-size:.75rem;line-height:1.5}.pa-row .voice-script-gap{height:6px}\nbody.theme-dark .pa-row{background:#17262d}body.theme-dark .pa-type{background:#1d2f37}.theme-dark .pa-type-voice{background:#3a2c14;color:#ffd488}body.theme-dark .pa-meta,body.theme-dark .pa-section-note{color:#c8d7dc}body.theme-dark .pa-content,body.theme-dark .pa-row .voice-script-text{background:#1d2f37;color:#e8eff3}\n@media(max-width:760px){.pa-row-main{grid-template-columns:1fr auto}.pa-type{grid-column:1}.pa-row-info{grid-column:1/-1;grid-row:2}.pa-row-actions{grid-column:2;grid-row:1}.pa-row-copy,.pa-row-details{margin-left:8px}.pa-cast-row{grid-template-columns:1fr}.pa-meta{grid-template-columns:50px minmax(0,1fr)}}\n@media print{.pa-group-nav,.pa-copy-button,.pa-row .voice-copy-button{display:none!important}.pa-row,.pa-group{break-inside:avoid}}\n</style>'''"""
    text=text[:style_start]+style+text[style_end:]

    # Remove tab click handling from copy script by replacing whole script.
    script_start=text.index("OBJECTIVE_COPY_SCRIPT = r'''<script id=\"production-assets-flow-copy-script\">")
    script_end=text.index("</script>'''", script_start)+len("</script>'''")
    script="""OBJECTIVE_COPY_SCRIPT = r'''<script id=\"production-assets-flow-copy-script\">(function(){\n  function fallbackCopy(text){var area=document.createElement('textarea');area.value=text;area.setAttribute('readonly','');area.style.position='fixed';area.style.opacity='0';document.body.appendChild(area);area.select();try{document.execCommand('copy');}finally{document.body.removeChild(area);}}\n  document.addEventListener('click',function(event){var button=event.target.closest('[data-pa-copy]');if(!button)return;var source=document.getElementById(button.getAttribute('data-pa-copy'));if(!source)return;var text=source.textContent||'';var label=button.querySelector('.pa-copy-label');var original=label?label.textContent:'Copy';var done=function(){button.classList.add('is-copied');if(label)label.textContent='Copied ✓';else button.textContent='Copied ✓';setTimeout(function(){button.classList.remove('is-copied');if(label)label.textContent=original;else button.textContent=original;},1400);};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done,function(){fallbackCopy(text);done();});}else{fallbackCopy(text);done();}});\n})();</script>'''"""
    text=text[:script_start]+script+text[script_end:]

    # Parse Group/Used for Voice and pass into renderer.
    old='''    voice_for = voice.parse_voice_requirement_for(requirements_path) if has_voice else {}\n    source = output.read_text(encoding="utf-8")'''
    new='''    voice_for = voice.parse_voice_requirement_for(requirements_path) if has_voice else {}\n    voice_groups = _parse_voice_requirement_field(requirements_path, "Group") if has_voice else {}\n    voice_used = _parse_voice_requirement_field(requirements_path, "Used") if has_voice else {}\n    source = output.read_text(encoding="utf-8")'''
    if old not in text: raise SystemExit('augment voice field marker missing')
    text=text.replace(old,new,1)
    old='pages, nav = _pages_and_nav(render_data, assets, voice_doc, triggers, voice_flows, voice_for)'
    new='pages, nav = _pages_and_nav(render_data, assets, voice_doc, triggers, voice_flows, voice_for, voice_groups, voice_used)'
    if old not in text: raise SystemExit('pages call marker missing')
    text=text.replace(old,new,1)
    RENDERER.write_text(text, encoding='utf-8')


def append_authority():
    src=SOURCE.read_text(encoding='utf-8')
    if 'id: SRC-015' not in src:
        src += '''\n\n  - id: SRC-015\n    type: instruction\n    role: authoritative\n    status: current\n    origin: user\n    inspection: full\n    summary: User superseded the tab-hidden Production Assets presentation. Section 04 must keep every production requirement visible and use hybrid contextual grouping rather than forcing every objective into gameplay-flow tabs. Grouping follows how assets are actually used: shared/objective-wide kits, meaningful phases/crossings, or specific authored events. Each production item must state concise Used and Purpose context; exact UI/Text and Voice remain copy-ready; navigation may use visible anchor links only and must never hide other groups. Objective 3 specifically needs a Core Trap Kit including the Floor Trap as a concrete production asset.\n'''
        SOURCE.write_text(src, encoding='utf-8')
    req=REQ.read_text(encoding='utf-8')
    if 'id: REQ-021' not in req:
        req += '''\n\n  - id: REQ-021\n    area: production-assets\n    statement: Section 04 is a contextual production checklist, not a flow mirror or hidden-tab interface. All production groups remain visible on the page. Use hybrid grouping based on actual production use: shared/objective-wide kits, distinct phases/crossings only when they materially differ, and specific authored events such as sabotage or completion. Every production deliverable shows literal type, asset name, concise Used context, and concise Purpose. Exact UI/Text and Voice remain copy-ready. Anchor navigation may scroll to groups but must not hide content. Do not force Objective 3 into artificial flow groups; present its Core Trap Kit, Player Communication, Voice, Gameplay Feedback, and Transition directly, including Floor Trap as a concrete asset.\n    provenance: [SRC-015]\n    evidence_status: approved\n    recovery_class: none\n    approval_status: not_required\n    impact: high\n'''
        REQ.write_text(req, encoding='utf-8')


patch_assets()
patch_voice_requirements()
patch_renderer()
append_authority()
print('contextual Production Assets patch prepared')
