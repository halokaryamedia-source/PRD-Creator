from pathlib import Path
import re

ROOT = Path('.')
PROJECT = ROOT / 'workspace/active/the-clockwork-vault'
ASSETS = PROJECT / 'work/asset-requirements.md'
VOICES = PROJECT / 'work/voice-requirements.md'
RENDERER = ROOT / 'kits/project-document-generator/renderer/production_assets_objective.py'
SRC = PROJECT / 'state/source-inventory.yaml'
REQ = PROJECT / 'state/requirement-register.yaml'

# Reader-facing names: remove internal mechanic wording.
RENAMES = {
    'Objective 1 Instruction Panel': 'Resonance Engine Entrance Message',
    'First Rollback Message': 'Ring One Power-Loss Message',
    'Second Rollback Message': 'Ring Two Power-Loss Message',
}

FUNCTIONS = {
    'Custodian Vex': 'Guide NPC used for story, warnings, and completion dialogue.',
    'Gremlin': 'Sabotage character used in the final Gallery crossing and the Workshop.',
    'Custodian Key': 'Opening key used to unlock the first seal.',
    'Resonance Engine Entrance Message': 'Tells the player the missing clues are somewhere in the chamber without giving the solution.',
    'Partial Door Target Display': 'Shows Middle = Brown. Left, Right, and Pulse remain unknown.',
    'Scattered Clue Book Set': 'Provides 12 books: 2 rule notes, 8 useful clues, and 2 decoys.',
    'Broken Gallery Entrance Message': 'Tells the player to use the old supplies and repair only marked gaps.',
    'First Crossing Message': 'Tells the player more than one route can work without revealing which ones.',
    'Second Crossing Message': 'Tells the player only one route can work without naming it.',
    "Gremlin's Wager Message": 'Explains the final crossing: choose a path and reach halfway before time runs out.',
    'Crossing Failure Messages': 'Shows a short message when a crossing fails or Gremlin removes a route.',
    'Repair Gap Markers': 'Marks the gaps where the player is allowed to place repair blocks.',
    'Gallery Challenge Warning Sound': "Signals the start of Gremlin's final Gallery crossing.",
    'Echo Pebble': 'Thrown at wall sensors and selected hanging stones.',
    'Wall Laser Sensor': 'Laser trap that blocks the path and can be disabled with the Echo Pebble.',
    'Laser Blocker Stone': 'Hanging stone that drops into a laser beam and blocks it.',
    'Swinging Axe Trap': 'Ceiling trap that swings across the corridor.',
    'Floor Trap': 'Floor trap that activates when the player steps on it.',
    'Warden Halls Entrance Message': 'Introduces the Warden Halls and hints that the Echo Pebble works on wall sensors.',
    'Echo Pebble HUD': 'Shows whether the Echo Pebble is ready.',
    'Power Generator': 'Power source for the Orrery network.',
    '90-Degree Rotator Junction': 'L-shaped junction the player rotates to redirect power.',
    'Orrery Ring': 'Ring mechanism used for Ring 1, Ring 2, and Ring 3.',
    'Workshop Entrance Message': 'Tells the player to carry power from the Generator through all three rings.',
    'Orrery Ring Status': 'Shows one current power state for each Orrery ring: POWERED or NO POWER.',
    'Route Swap Message': 'Tells the player the old route is blocked and another route is open.',
    'Ring One Power-Loss Message': "Tells the player Ring One lost power after Gremlin's sabotage.",
    'Ring Two Power-Loss Message': "Tells the player Ring Two lost power after Gremlin's sabotage.",
    'Clockwork Wayfinder': 'Reward item shown after the vault is restored.',
    'Vault Restored Message': 'Confirms the vault is restored and points the player to the open gateway.',
}

BRIEFS = {
    'Custodian Vex': 'Clockwork custodian NPC. Needs the idle, speaking, pointing, alert, and completion animations used by the story.',
    'Gremlin': 'Small clockwork gremlin NPC. Needs movement, sabotage, taunt, and defeated reactions used in the map.',
    'Custodian Key': 'Distinct key item for the opening pedestal and pickup.',
    'Repair Gap Markers': 'Simple marker or prop placed on repairable gaps. It must stand out from normal blocks without using debug text.',
    'Gallery Challenge Warning Sound': 'Short mechanical warning sound with a mischievous feel. No spoken dialogue.',
    'Echo Pebble': 'Small ordinary stone used as the throwable item. Use the same simple stone look in hand and as a projectile.',
    'Wall Laser Sensor': 'Wall-mounted mechanical laser emitter with a visible beam. It needs clear active and disabled looks.',
    'Laser Blocker Stone': 'Stone hanging above selected laser paths. It drops into the beam and stays there as the blocker.',
    'Swinging Axe Trap': 'Large double-sided axe hanging from the ceiling with a left-right swing animation.',
    'Floor Trap': 'Floor-mounted trap that looks different from normal floor blocks. It needs a ready look and a triggered look.',
    'Power Generator': 'Central power machine with a clear output side. It needs powered and unpowered looks.',
    '90-Degree Rotator Junction': 'Compact L-shaped junction with two perpendicular connections. It rotates in 90-degree steps and needs powered and unpowered looks.',
    'Orrery Ring': 'Clockwork ring mechanism with powered and unpowered looks and the motion used during final restoration.',
    'Clockwork Wayfinder': 'Distinct reward item shown at the end of the map.',
}

MOMENTS = {
    'Custodian Vex': 'Used Across the Map',
    'Gremlin': 'Used Across the Map',
    'Custodian Key': 'Entering the Antechamber',
    'Custodian Key Prompt': 'Opening the First Seal',
    'Resonance Engine Entrance Message': 'Entering the Resonance Engine',
    'Partial Door Target Display': 'Throughout the Resonance Engine',
    'Scattered Clue Book Set': 'Searching the Chamber',
    'Broken Gallery Entrance Message': 'Entering the Broken Gallery',
    'First Crossing Message': 'First Crossing',
    'Second Crossing Message': 'Second Crossing',
    "Gremlin's Wager Message": "Gremlin's Final Crossing",
    'Crossing Failure Messages': 'Crossing Failed / Route Lost',
    'Repair Gap Markers': 'Throughout the Broken Gallery',
    'Gallery Challenge Warning Sound': "Gremlin's Final Crossing",
    'Echo Pebble': 'Throughout the Warden Halls',
    'Wall Laser Sensor': 'Throughout the Warden Halls',
    'Laser Blocker Stone': 'Throughout the Warden Halls',
    'Swinging Axe Trap': 'Throughout the Warden Halls',
    'Floor Trap': 'Throughout the Warden Halls',
    'Warden Halls Entrance Message': 'Entering the Warden Halls',
    'Echo Pebble HUD': 'Throughout the Warden Halls',
    'Power Generator': "Throughout Gremlin's Workshop",
    '90-Degree Rotator Junction': "Throughout Gremlin's Workshop",
    'Orrery Ring': "Throughout Gremlin's Workshop",
    'Workshop Entrance Message': "Entering Gremlin's Workshop",
    'Orrery Ring Status': "Throughout Gremlin's Workshop",
    'Route Swap Message': 'Gremlin Changes the Route',
    'Ring One Power-Loss Message': 'Ring One Loses Power',
    'Ring Two Power-Loss Message': 'Ring Two Loses Power',
    'Clockwork Wayfinder': 'Vault Restored',
    'Vault Restored Message': 'Way Home',
}

VOICE_FOR = {
    'VO-ANTE-01': 'Introduces the vault, the Great Orrery, and why the player must continue.',
    'VO-ANTE-02': 'Reminds the player to use the Custodian Key on the first seal.',
    'VO-RES-01': 'Adds story context to the Resonance Engine and hints that the missing clues are still in the chamber.',
    'VO-GAL-01': 'Introduces the collapsed Gallery and hints that Gremlin has been there.',
    'VO-GAL-02': 'Gremlin challenges the player before the final Gallery crossing.',
    'VO-WARD-01': 'Introduces the Wardens and hints that the Echo Pebble works on wall sensors.',
    'VO-WARD-02': 'Closes the Warden Halls and points the player toward the Workshop.',
    'VO-WORK-01': 'Introduces the Workshop as the heart of the Great Orrery.',
    'VO-GREM-01': 'Gremlin taunts the player after changing the route.',
    'VO-WORK-02': 'Vex reacts when Ring Two loses power.',
    'VO-GREM-02': "Gremlin taunts the player after knocking an earlier power line out.",
    'VO-WORK-03': 'Vex reacts when Ring One loses power.',
    'VO-GREM-03': 'Gremlin taunts the player after sabotaging the network again.',
    'VO-WORK-04': 'Vex reacts when Ring Two loses power again.',
    'VO-GREM-04': 'Gremlin reacts when the player restores the full Orrery network.',
    'VO-END-01': 'Vex confirms the vault is restored and presents the reward.',
    'VO-END-02': 'Vex gives the final farewell and points the player to the open gateway.',
}

VOICE_MOMENT = {
    'VO-ANTE-01': 'Entering the Antechamber',
    'VO-ANTE-02': 'Opening the First Seal',
    'VO-RES-01': 'Entering the Resonance Engine',
    'VO-GAL-01': 'Entering the Broken Gallery',
    'VO-GAL-02': "Gremlin's Final Crossing",
    'VO-WARD-01': 'Entering the Warden Halls',
    'VO-WARD-02': 'Warden Halls Cleared',
    'VO-WORK-01': "Entering Gremlin's Workshop",
    'VO-GREM-01': 'Gremlin Changes the Route',
    'VO-WORK-02': 'Gremlin Changes the Route',
    'VO-GREM-02': 'Ring One Loses Power',
    'VO-WORK-03': 'Ring One Loses Power',
    'VO-GREM-03': 'Ring Two Loses Power',
    'VO-WORK-04': 'Ring Two Loses Power',
    'VO-GREM-04': 'Orrery Restored',
    'VO-END-01': 'Vault Restored',
    'VO-END-02': 'Way Home',
}


def set_field(body: str, label: str, value: str) -> str:
    pat = re.compile(rf'(?m)^{re.escape(label)}:.*$')
    line = f'{label}: {value}'
    if pat.search(body):
        return pat.sub(line, body, count=1)
    # Place reader-facing fields directly after Flow where possible.
    m = re.search(r'(?m)^Flow:.*$', body)
    if m:
        return body[:m.end()] + '\n' + line + body[m.end():]
    return line + '\n' + body


def remove_fields(body: str, labels: list[str]) -> str:
    for label in labels:
        body = re.sub(rf'(?m)^{re.escape(label)}:.*\n?', '', body)
    return body


def patch_assets() -> None:
    text = ASSETS.read_text(encoding='utf-8')
    for old, new in RENAMES.items():
        text = text.replace(old, new)

    pat = re.compile(r'(?ms)^#### (.+?)\n(.*?)(?=^#### |^### |^## |\Z)')
    out = []
    pos = 0
    seen = set()
    for m in pat.finditer(text):
        name = m.group(1).strip()
        body = m.group(2)
        out.append(text[pos:m.start()])
        seen.add(name)
        if name in FUNCTIONS:
            body = set_field(body, 'Function', FUNCTIONS[name])
        if name in MOMENTS:
            body = set_field(body, 'Moment', MOMENTS[name])
        body = remove_fields(body, ['Asset Brief', 'Visual Brief', 'Audio Brief', 'Size'])
        if name in BRIEFS:
            label = 'Audio Brief' if name == 'Gallery Challenge Warning Sound' else 'Visual Brief'
            body = set_field(body, label, BRIEFS[name])
        out.append(f'#### {name}\n{body}')
        pos = m.end()
    out.append(text[pos:])
    text = ''.join(out)

    # Clearer player-facing ring states: one state is shown at a time in game.
    text = re.sub(
        r'(?ms)(#### Orrery Ring Status\n.*?Content:\n```text\n).*?(\n```)',
        r'\1RING 1 · POWERED\nRING 1 · NO POWER\n\nRING 2 · POWERED\nRING 2 · NO POWER\n\nRING 3 · POWERED\nRING 3 · NO POWER\2',
        text,
        count=1,
    )
    text = re.sub(
        r'(?ms)(#### Ring One Power-Loss Message\n.*?Content:\n```text\n).*?(\n```)',
        r'\1RING ONE LOST POWER\n\nGremlin knocked the power line out.\nRestore Ring One.\2',
        text,
        count=1,
    )
    text = re.sub(
        r'(?ms)(#### Ring Two Power-Loss Message\n.*?Content:\n```text\n).*?(\n```)',
        r'\1RING TWO LOST POWER\n\nGremlin struck the power line again.\nRestore Ring Two.\2',
        text,
        count=1,
    )
    ASSETS.write_text(text, encoding='utf-8')


def patch_voices() -> None:
    text = VOICES.read_text(encoding='utf-8')
    pat = re.compile(r'(?ms)^### (VO-[A-Z0-9-]+)\s+[—-].*?\n(.*?)(?=^### |^## |\Z)')
    out = []
    pos = 0
    for m in pat.finditer(text):
        vid = m.group(1)
        full = m.group(0)
        body_start = full.find('\n') + 1
        head = full[:body_start]
        body = full[body_start:]
        out.append(text[pos:m.start()])
        if vid in VOICE_FOR:
            body = re.sub(r'(?m)^- For:.*$', f'- For: {VOICE_FOR[vid]}', body, count=1)
        if vid in VOICE_MOMENT:
            body = re.sub(r'(?m)^- Moment:.*$', f'- Moment: {VOICE_MOMENT[vid]}', body, count=1)
        out.append(head + body)
        pos = m.end()
    out.append(text[pos:])
    VOICES.write_text(''.join(out), encoding='utf-8')


def patch_renderer() -> None:
    text = RENDERER.read_text(encoding='utf-8')

    # Optional Size support. It is rendered only when a real value exists; never as a placeholder.
    text = text.replace('    asset_brief: str = ""\n    moment: str = ""', '    asset_brief: str = ""\n    size: str = ""\n    moment: str = ""', 1)
    text = text.replace('    asset_brief: str\n    moment: str', '    asset_brief: str\n    size: str\n    moment: str', 1)
    parse_anchor = '''                elif meta.startswith("Asset Brief:"):\n                    entry.asset_brief = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Moment:"):'''
    parse_repl = '''                elif meta.startswith("Asset Brief:") or meta.startswith("Visual Brief:") or meta.startswith("Audio Brief:"):\n                    entry.asset_brief = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Size:"):\n                    entry.size = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Moment:"):'''
    if parse_anchor not in text:
        raise SystemExit('renderer brief parser anchor not found')
    text = text.replace(parse_anchor, parse_repl, 1)
    text = text.replace('        asset_brief=entry.asset_brief,\n        moment=entry.moment,', '        asset_brief=entry.asset_brief,\n        size=entry.size,\n        moment=entry.moment,', 1)
    text = text.replace('        function_text=function_text or "Story or character audio for this gameplay moment.", asset_brief="",\n        moment=', '        function_text=function_text or "Story or character audio for this gameplay moment.", asset_brief="", size="",\n        moment=', 1)

    # Reader-facing title is based on the existing section role; no objective-specific hardcoding.
    helper = '''\ndef _reader_section_title(meta: SectionPresentation) -> str:\n    label = txt(meta.package_label)["en"].strip()\n    name = meta.title.strip()\n    if label.casefold().startswith("objective"):\n        name = re.sub(r"^The\\s+", "", name, flags=re.I)\n        return f"{label} · {name}"\n    if label.casefold() == "introduction":\n        return f"Introduction · {name}"\n    if label.casefold() == "ending":\n        return f"Ending · {name}"\n    if label.casefold() == "shared":\n        return "Shared Assets"\n    return f"{label} · {name}" if label else name\n\n'''
    marker = '\ndef _build_item_html(item: ProductionItem) -> str:\n'
    if helper.strip() not in text:
        text = text.replace(marker, helper + marker, 1)

    # Replace item rendering: type above title; visual/audio brief labels are explicit; voice prompt is formatted.
    render_pat = re.compile(r'(?ms)^def _build_item_html\(item: ProductionItem\) -> str:\n.*?\n(?=def _moment_html)')
    render_new = '''def _build_item_html(item: ProductionItem) -> str:\n    exact = ""\n    if item.content:\n        if item.is_voice:\n            target = "voice-prompt-" + item.item_id.split("-build-")[-1]\n            exact = (\n                '<div class="pa-exact pa-audio-prompt"><div class="pa-exact-head">'\n                f'<span>Prompt</span>{_copy_button(target, "Copy Prompt")}</div>'\n                f'<pre class="voice-script-text" id="{esc(target)}">{esc(item.content)}</pre>'\n                f'<div class="voice-script-display">{voice._performance_html(item.content)}</div></div>'\n            )\n        else:\n            target = f"{item.item_id}-copy"\n            exact = (\n                '<div class="pa-exact"><div class="pa-exact-head">'\n                f'<span>Player Text</span>{_copy_button(target, "Copy Text")}</div>'\n                f'<pre class="pa-content" id="{esc(target)}">{esc(item.content)}</pre></div>'\n            )\n\n    meta = '<div class="pa-build-meta-row"><b>Function</b><span>'+esc(item.function_text)+'</span></div>'\n    if item.is_voice:\n        meta += '<div class="pa-build-meta-row"><b>Voice Preset</b><span>'+esc(item.selected_voice)+'</span></div>'\n        meta += '<div class="pa-build-meta-row"><b>ElevenLabs Model</b><span>Eleven v3</span></div>'\n        meta += '<div class="pa-build-meta-row"><b>Estimated Duration</b><span>'+esc(item.duration)+'</span></div>'\n    elif item.asset_brief:\n        brief_label = 'Audio Brief' if item.type_label.upper() == 'AUDIO' else 'Visual Brief'\n        meta += '<div class="pa-build-meta-row"><b>'+brief_label+'</b><span>'+esc(item.asset_brief)+'</span></div>'\n        if item.size:\n            meta += '<div class="pa-build-meta-row"><b>Size</b><span>'+esc(item.size)+'</span></div>'\n\n    type_class = 'pa-type-' + slug(item.type_label)\n    cls = "pa-row pa-row-voice" if item.is_voice else "pa-build-row pa-row"\n    return (\n        f'<article class="{cls}" id="{esc(item.item_id)}">'\n        f'<div class="pa-build-head"><span class="pa-type {type_class}">{esc(item.type_label)}</span>'\n        f'<h4>{esc(item.title)}</h4></div>'\n        f'<div class="pa-build-meta">{meta}</div>{exact}</article>'\n    )\n\n'''
    text, n = render_pat.subn(render_new, text, count=1)
    if n != 1:
        raise SystemExit('renderer item render block not found')

    # Remove duplicate body label and use professional section title.
    body_old = '''        body = (\n            '<header class="pa-shell"><small>Production Assets</small>'\n            f'<h2>{esc(meta.title)}</h2><strong>{i18n(meta.package_label)}</strong></header>'\n            '<div class="pa-moments">' + _moment_html(items) + '</div>'\n        )'''
    body_new = '''        body = (\n            '<header class="pa-shell">'\n            f'<h2>{esc(_reader_section_title(meta))}</h2></header>'\n            '<div class="pa-moments">' + _moment_html(items) + '</div>'\n        )'''
    if body_old not in text:
        raise SystemExit('renderer body header anchor not found')
    text = text.replace(body_old, body_new, 1)

    # Replace Production Assets CSS with a cleaner vertical layout and distinct resource accents.
    css_pat = re.compile(r"(?ms)^OBJECTIVE_STYLE = r'''<style id=\"production-assets-objective-style\">.*?</style>'''\n")
    css_new = '''OBJECTIVE_STYLE = r\'''<style id="production-assets-objective-style">\n.pa-shell{margin:0 0 18px}.pa-shell h2{margin:0;color:var(--navy);font-size:1.72rem;line-height:1.14;letter-spacing:-.02em}.pa-moments{display:grid;gap:22px}.pa-moment+.pa-moment{padding-top:20px;border-top:1px solid var(--line)}.pa-moment-head{display:flex;align-items:baseline;gap:9px;margin-bottom:8px}.pa-moment-head>span{color:var(--amber);font-size:.62rem;font-weight:900}.pa-moment-head h3{margin:0;color:var(--navy);font-size:1.07rem;text-transform:none}.pa-build-list{border-top:1px solid #cbd7dd}.pa-build-row,.pa-row-voice{padding:13px 10px;border-bottom:1px solid #cbd7dd;background:var(--paper);break-inside:avoid}.pa-build-head{display:flex;flex-direction:column;align-items:flex-start;gap:5px}.pa-type{display:inline-flex;padding:4px 8px;border-radius:3px;background:var(--soft);color:var(--blue);font-size:.64rem;font-weight:900;letter-spacing:.06em;text-transform:uppercase}.pa-type-audio{background:#fff3dc;color:#8a4e00}.pa-type-ui-text{background:#eaf4fb;color:#145d83}.pa-type-model{background:#eaf6ef;color:#2d6847}.pa-type-item{background:#f0effa;color:#51458c}.pa-type-particle{background:#f5edf8;color:#74457e}.pa-build-head h4{margin:0;color:var(--navy);font-size:.94rem;line-height:1.3;text-transform:none}.pa-build-meta{display:grid;gap:8px;margin-top:10px}.pa-build-meta-row{display:block;color:#52616a;font-size:.74rem;line-height:1.48}.pa-build-meta-row b{display:block;margin-bottom:2px;color:var(--navy);font-size:.61rem;font-weight:900;letter-spacing:.035em;text-transform:uppercase}.pa-exact{margin-top:10px}.pa-exact-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:5px}.pa-exact-head>span{color:var(--blue);font-size:.61rem;font-weight:900;text-transform:uppercase}.pa-audio-prompt .pa-exact-head>span{color:#9a5a0a}.pa-copy-button{min-height:27px;padding:5px 8px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .56rem/1 var(--font);text-transform:uppercase}.pa-content{margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:3px;background:#f8fafb;color:var(--navy);font:700 .76rem/1.52 var(--font);white-space:pre-wrap}.pa-row-voice .voice-script-text{display:none!important}.pa-row-voice .voice-script-display{margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--amber);border-radius:3px;background:#f8fafb}.pa-row-voice .voice-performance-tag{display:inline-flex;margin:0 0 5px;padding:2px 6px;border-radius:3px;background:#fff0d2;color:#965700;font-size:.65rem;font-weight:900}.pa-row-voice .voice-script-line{color:var(--navy);font-size:.76rem;line-height:1.55}.pa-row-voice .voice-script-gap{height:6px}body.theme-dark .pa-build-row,body.theme-dark .pa-row-voice{background:#17262d}body.theme-dark .pa-build-meta-row{color:#c8d7dc}body.theme-dark .pa-row-voice .voice-script-display,body.theme-dark .pa-content{background:#1d2f37;color:#e8eff3}body.theme-dark .pa-type-audio{background:#3b2c13;color:#ffd284}@media print{.pa-copy-button{display:none!important}}\n</style>\'''\n'''
    text, n = css_pat.subn(css_new, text, count=1)
    if n != 1:
        raise SystemExit('renderer css block not found')

    RENDERER.write_text(text, encoding='utf-8')


def patch_authority() -> None:
    src = SRC.read_text(encoding='utf-8')
    if 'id: SRC-018' not in src:
        src += '''\n\n  - id: SRC-018\n    type: instruction\n    role: authoritative\n    status: current\n    origin: user\n    inspection: full\n    summary: User approved the final humanized Section 04 direction. Production Assets must read like short production notes written by a person: literal, concise, and free of AI-style filler, invented visual traits, or unnecessary taxonomy. Echo Pebble is an ordinary stone, not magical. Every objective uses the same moment-first layout. Visual resources use only Function plus a direct Visual Brief; Size is optional and may appear only when a real approved Minecraft-scale value is known. Do not show generic States, Position, Orientation, Reuse, placeholder size, or similar metadata. Animation or visual changes are described directly inside the Visual Brief when they are part of the model. UI / TEXT keeps exact player-facing copy. AUDIO dialogue keeps Function, Voice Preset, ElevenLabs Model, Estimated Duration, and exact Prompt; performance-direction tags must be visually distinct from spoken dialogue. AUDIO without dialogue uses Function plus a short Audio Brief. Resource type must be visually prominent above the resource title. Moment names and resource names must be reader-friendly rather than internal mechanic labels. Duplicate Production Assets headings are not allowed. Section 03 Development remains unchanged.\n'''
        SRC.write_text(src, encoding='utf-8')

    req = REQ.read_text(encoding='utf-8')
    if 'id: REQ-024' not in req:
        req += '''\n\n  - id: REQ-024\n    area: production-assets\n    statement: Section 04 is a universal, humanized, moment-first production brief. Use plain, literal language and remove AI-style filler, speculative visual details, and unnecessary metadata. Echo Pebble is a normal stone. Visual resources render as TYPE, resource name, Function, Visual Brief, and optional Size only when a real approved size exists; animation and visual changes stay in the Visual Brief rather than generic States/Position/Orientation/Reuse fields. UI / TEXT renders Function plus exact player copy. AUDIO dialogue renders Function, Voice Preset, ElevenLabs Model, Estimated Duration, and exact Prompt with performance-direction tags visually separated from spoken lines; non-dialogue AUDIO renders Function plus Audio Brief. Type appears above the resource title. Moment and asset names use reader-friendly gameplay wording, not internal labels such as Rollback. The body must not duplicate the Production Assets page header. Section 03 Development is frozen and must not be edited by Section 04 work.\n    provenance: [SRC-018]\n    evidence_status: approved\n    recovery_class: none\n    approval_status: not_required\n    impact: high\n'''
        REQ.write_text(req, encoding='utf-8')


patch_assets()
patch_voices()
patch_renderer()
patch_authority()
print('humanized 04 polish prepared')
