from pathlib import Path
import re

PROJECT = Path('workspace/active/the-clockwork-vault')
ASSET = PROJECT / 'work/asset-requirements.md'
VOICE = PROJECT / 'work/voice-requirements.md'
SOURCE = PROJECT / 'state/source-inventory.yaml'
REQ = PROJECT / 'state/requirement-register.yaml'

REMOVE_ASSETS = {
    'Pillar Lamp Feedback',
    'Warden Hit Effects',
    'Warden Recovery',
}

TYPE_OVERRIDES = {
    'Custodian Vex': 'ENTITY / MODEL',
    'Gremlin': 'ENTITY / MODEL',
    'Custodian Key': 'ITEM',
    'Echo Pebble': 'ITEM / PROJECTILE',
    'Wall Laser Sensor': 'ENTITY / MODEL',
    'Laser Blocker Stone': 'ENTITY / MODEL',
    'Swinging Axe Trap': 'ENTITY / MODEL',
    'Floor Trap': 'ENTITY / MODEL',
    'Repair Gap Markers': 'BLOCK / PROP',
    'Power Generator': 'ENTITY / MODEL',
    '90-Degree Rotator Junction': 'ENTITY / MODEL',
    'Orrery Ring': 'ENTITY / MODEL',
    'Clockwork Wayfinder': 'ITEM',
}

CREATE_OVERRIDES = {
    'Custodian Vex': 'Create one reusable Custodian Vex NPC/model setup.',
    'Gremlin': 'Create one reusable Gremlin NPC/model setup.',
    'Custodian Key': 'Create one reusable Custodian Key item setup.',
    'Echo Pebble': 'Create one reusable throwable Echo Pebble item/projectile setup.',
    'Wall Laser Sensor': 'Create one reusable wall-mounted laser sensor setup.',
    'Laser Blocker Stone': 'Create one reusable hanging blocker-stone setup.',
    'Swinging Axe Trap': 'Create one reusable ceiling-mounted swinging axe trap setup.',
    'Floor Trap': 'Create one reusable floor-trap setup.',
    'Repair Gap Markers': 'Create one reusable marker treatment for repairable Gallery gaps.',
    'Power Generator': 'Create one reusable power-generator setup for the Orrery network.',
    '90-Degree Rotator Junction': 'Create one reusable rotator-junction setup.',
    'Orrery Ring': 'Create one reusable Orrery Ring setup used for all three rings.',
    'Clockwork Wayfinder': 'Create one Clockwork Wayfinder reward item/model.',
}

INCLUDES = {
    'Custodian Vex': 'NPC model/texture; idle and speaking states; required authored character animations.',
    'Gremlin': 'Character model/texture; appearance/movement states; sabotage and reaction animations.',
    'Custodian Key': 'Item appearance; readable pickup/pedestal state; accepted state at the first seal.',
    'Echo Pebble': 'Inventory/held appearance; projectile appearance; readable valid-hit response.',
    'Wall Laser Sensor': 'Sensor model/texture; visible laser beam; active and disabled states; attached animation/sound only when part of this same setup.',
    'Laser Blocker Stone': 'Stone model/texture; hanging state; drop/block animation.',
    'Swinging Axe Trap': 'Axe model/texture; ceiling mount; swing animation; reset state.',
    'Floor Trap': 'Trap model/visual; armed, triggered, and reset states.',
    'Repair Gap Markers': 'Visible environment marker treatment for valid repair positions.',
    'Power Generator': 'Model/texture; offline, live, and interrupted states; attached energy/sound only when part of this same setup.',
    '90-Degree Rotator Junction': 'Junction model/texture; four orientations; powered/unpowered states; rotation animation.',
    'Orrery Ring': 'Ring model/texture; inactive/powered states; motion used during final restoration.',
    'Clockwork Wayfinder': 'Reward item/model appearance; readable reward reveal state.',
}

USED = {
    'Custodian Vex': 'Across the story wherever Custodian Vex appears.',
    'Gremlin': 'During the Broken Gallery challenge and Workshop sabotage moments.',
    'Custodian Key': 'At the opening pedestal and first seal.',
    'Custodian Key Prompt': 'When the player must take the Custodian Key.',
    'Resonance Engine Seal Opening': 'When the Custodian Key is accepted by the first seal.',
    'Objective 1 Instruction Panel': 'When the Resonance Engine objective begins.',
    'Partial Door Target Display': 'Throughout Resonance Engine solving.',
    'Scattered Clue Book Set': 'While the player searches the Resonance Engine chamber for clues.',
    'Resonance Engine Restoration': 'When all three pillar states are correct.',
    'Broken Gallery Entrance Message': 'When the player enters the Broken Gallery.',
    'First Crossing Message': 'When the first Gallery crossing becomes active.',
    'Second Crossing Message': 'When the second Gallery crossing becomes active.',
    "Gremlin's Wager Message": 'When the final Gallery crossing begins.',
    'Crossing Failure Messages': 'When a Gallery crossing attempt fails or a final route is lost.',
    'Repair Gap Markers': 'Throughout all Broken Gallery crossings.',
    'Gremlin Wager Cue': 'When the final Gallery crossing begins.',
    'Gremlin Path Collapse': 'When Gremlin removes a failed route in the final Gallery crossing.',
    'Echo Pebble': 'Throughout the Warden Halls.',
    'Wall Laser Sensor': 'At laser encounters throughout the Warden Halls.',
    'Laser Blocker Stone': 'At selected laser encounters that use the blocker-stone solution.',
    'Swinging Axe Trap': 'At axe encounters throughout the Warden Halls.',
    'Floor Trap': 'At floor-trap encounters throughout the Warden Halls.',
    'Warden Halls Entrance Message': 'When the player enters the Warden Halls.',
    'Echo Pebble HUD': 'While the Echo Pebble is available.',
    'Power Generator': 'Throughout the Gremlin Workshop objective.',
    '90-Degree Rotator Junction': 'Throughout the Gremlin Workshop objective.',
    'Orrery Ring': 'Throughout the Gremlin Workshop objective.',
    'Workshop Entrance Message': 'When the player enters the Gremlin Workshop.',
    'Orrery Ring Status': 'Throughout the Gremlin Workshop objective.',
    'Route Swap Message': 'Immediately after Gremlin changes the route.',
    'First Rollback Message': 'When the first sabotage makes Ring One lose power.',
    'Second Rollback Message': 'When the second sabotage makes Ring Two lose power.',
    'Gremlin Route Swap': 'When Gremlin blocks the old route after Ring Two restoration.',
    'First Rollback Sabotage': 'During the first sabotage on the final route.',
    'Second Rollback Sabotage': 'During the second sabotage on the final route.',
    'Great Orrery Restoration': 'When the full Orrery network is restored.',
    'Clockwork Wayfinder': 'During the final reward reveal.',
    'Vault Restored Message': 'When the return gateway is open.',
    'Vault Awakening Sequence': 'After the Great Orrery is restored.',
}

MOMENT = {
    'Custodian Vex': 'Throughout Project',
    'Gremlin': 'Throughout Project',
    'Custodian Key': 'Objective Start',
    'Custodian Key Prompt': 'Take Key & Open Seal',
    'Resonance Engine Seal Opening': 'Take Key & Open Seal',
    'Objective 1 Instruction Panel': 'Objective Start',
    'Partial Door Target Display': 'Throughout Objective',
    'Scattered Clue Book Set': 'Search the Chamber',
    'Resonance Engine Restoration': 'Objective Complete',
    'Broken Gallery Entrance Message': 'Objective Start',
    'First Crossing Message': 'First Crossing',
    'Second Crossing Message': 'Second Crossing',
    "Gremlin's Wager Message": "Gremlin's Wager — final crossing",
    'Crossing Failure Messages': 'Crossing Failure / Route Lost',
    'Repair Gap Markers': 'Throughout Objective',
    'Gremlin Wager Cue': "Gremlin's Wager — final crossing",
    'Gremlin Path Collapse': 'Crossing Failure / Route Lost',
    'Echo Pebble': 'Throughout Objective',
    'Wall Laser Sensor': 'Throughout Objective',
    'Laser Blocker Stone': 'Throughout Objective',
    'Swinging Axe Trap': 'Throughout Objective',
    'Floor Trap': 'Throughout Objective',
    'Warden Halls Entrance Message': 'Objective Start',
    'Echo Pebble HUD': 'Throughout Objective',
    'Power Generator': 'Throughout Objective',
    '90-Degree Rotator Junction': 'Throughout Objective',
    'Orrery Ring': 'Throughout Objective',
    'Workshop Entrance Message': 'Objective Start',
    'Orrery Ring Status': 'Throughout Objective',
    'Route Swap Message': 'Route Swap — after Ring Two restoration',
    'First Rollback Message': 'First Sabotage — final route',
    'Second Rollback Message': 'Second Sabotage — final route',
    'Gremlin Route Swap': 'Route Swap — after Ring Two restoration',
    'First Rollback Sabotage': 'First Sabotage — final route',
    'Second Rollback Sabotage': 'Second Sabotage — final route',
    'Great Orrery Restoration': 'Objective Complete',
    'Clockwork Wayfinder': 'Restoration Payoff',
    'Vault Restored Message': 'Way Home',
    'Vault Awakening Sequence': 'Restoration Payoff',
}

VOICE_USED = {
    'VO-ANTE-01': 'When the story begins in the Antechamber.',
    'VO-ANTE-02': 'While the player still needs to use the Custodian Key.',
    'VO-RES-01': 'When the Resonance Engine objective begins.',
    'VO-GAL-01': 'When the player enters the Broken Gallery.',
    'VO-GAL-02': 'When the final Gallery crossing begins.',
    'VO-WARD-01': 'When the player enters the Warden Halls.',
    'VO-WARD-02': 'After the final Warden section is cleared.',
    'VO-WORK-01': 'When the player enters the Gremlin Workshop.',
    'VO-GREM-01': 'During the route-swap sabotage.',
    'VO-WORK-02': 'Immediately after the route-swap sabotage.',
    'VO-GREM-02': 'During the first sabotage on the final route.',
    'VO-WORK-03': 'Immediately after the first sabotage.',
    'VO-GREM-03': 'During the second sabotage on the final route.',
    'VO-WORK-04': 'Immediately after the second sabotage.',
    'VO-GREM-04': 'When the full Orrery network is restored.',
    'VO-END-01': 'During the final restoration payoff.',
    'VO-END-02': 'When the gateway home is open.',
}

VOICE_MOMENT = {
    'VO-ANTE-01': 'Objective Start',
    'VO-ANTE-02': 'Take Key & Open Seal',
    'VO-RES-01': 'Objective Start',
    'VO-GAL-01': 'Objective Start',
    'VO-GAL-02': "Gremlin's Wager — final crossing",
    'VO-WARD-01': 'Objective Start',
    'VO-WARD-02': 'Objective Complete',
    'VO-WORK-01': 'Objective Start',
    'VO-GREM-01': 'Route Swap — after Ring Two restoration',
    'VO-WORK-02': 'Route Swap — after Ring Two restoration',
    'VO-GREM-02': 'First Sabotage — final route',
    'VO-WORK-03': 'First Sabotage — final route',
    'VO-GREM-03': 'Second Sabotage — final route',
    'VO-WORK-04': 'Second Sabotage — final route',
    'VO-GREM-04': 'Objective Complete',
    'VO-END-01': 'Restoration Payoff',
    'VO-END-02': 'Way Home',
}


def category_type(category: str, title: str) -> str:
    if title in TYPE_OVERRIDES:
        return TYPE_OVERRIDES[title]
    return {
        '3D Models': 'ENTITY / MODEL',
        'UI & Information': 'UI / TEXT',
        'Audio': 'SOUND',
        'Visual Effects & Presentation': 'SEQUENCE',
    }[category]


def generic_create(category: str, title: str, requirement: str) -> str:
    if title in CREATE_OVERRIDES:
        return CREATE_OVERRIDES[title]
    if category == 'UI & Information':
        return f'Create the exact player-facing {title}.'
    if category == 'Audio':
        return f'Create one standalone {title} sound.'
    if category == 'Visual Effects & Presentation':
        return f'Create one authored {title} sequence.'
    first = re.split(r'(?<=[.!?])\s+', ' '.join(requirement.split()).strip())[0] if requirement else ''
    if first.lower().startswith('create '):
        return first
    return f'Create one reusable {title} setup.'


def remove_asset(text: str, title: str) -> str:
    pattern = re.compile(rf'(?ms)^#### {re.escape(title)}\n.*?(?=^#### |^### |^## |\Z)')
    return pattern.sub('', text)


def patch_assets() -> None:
    text = ASSET.read_text(encoding='utf-8')
    for title in REMOVE_ASSETS:
        text = remove_asset(text, title)

    lines = text.splitlines()
    out = []
    i = 0
    category = ''
    while i < len(lines):
        line = lines[i]
        if line.startswith('### ') and not line.startswith('### Gameplay Flow '):
            category = line[4:].strip()
            out.append(line)
            i += 1
            continue
        if not line.startswith('#### '):
            out.append(line)
            i += 1
            continue

        title = line[5:].strip()
        block = [line]
        i += 1
        while i < len(lines) and not lines[i].startswith(('#### ', '### ', '## ')):
            block.append(lines[i])
            i += 1

        flow = next((x.split(':',1)[1].strip() for x in block if x.startswith('Flow:')), '')
        requirement = next((x.split(':',1)[1].strip() for x in block if x.startswith('Requirement:')), '')
        used = USED.get(title) or next((x.split(':',1)[1].strip() for x in block if x.startswith('Used:')), '') or flow
        moment = MOMENT.get(title) or re.sub(r'^\s*\d+\s*[—-]\s*', '', flow).strip() or 'Gameplay Use'
        type_label = category_type(category, title)
        create = generic_create(category, title, requirement)
        includes = INCLUDES.get(title, '')

        filtered = [x for x in block[1:] if not x.startswith(('Type:', 'Create:', 'Used:', 'Includes:', 'Moment:'))]
        insert_at = next((idx + 1 for idx, x in enumerate(filtered) if x.startswith('Flow:')), 0)
        meta = [
            f'Type: {type_label}',
            f'Create: {create}',
            f'Used: {used}',
            f'Moment: {moment}',
        ]
        if includes:
            meta.append(f'Includes: {includes}')
        filtered[insert_at:insert_at] = meta
        out.extend([block[0], *filtered])

    ASSET.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')


def patch_voice() -> None:
    text = VOICE.read_text(encoding='utf-8')
    lines = text.splitlines()
    out = []
    i = 0
    entry_re = re.compile(r'^###\s+([A-Za-z0-9][A-Za-z0-9-]*)\s+[—-]\s+(.+?)\s*$')
    while i < len(lines):
        m = entry_re.match(lines[i])
        if not m:
            out.append(lines[i]); i += 1; continue
        vid = m.group(1)
        block = [lines[i]]
        i += 1
        while i < len(lines) and not lines[i].startswith(('### ', '## ')):
            block.append(lines[i]); i += 1
        speaker = next((x.split(':',1)[1].strip() for x in block if x.startswith('- Speaker:')), 'character')
        filtered = [x for x in block[1:] if not x.startswith(('- Create:', '- Used:', '- Moment:'))]
        flow_idx = next((idx + 1 for idx, x in enumerate(filtered) if x.startswith('- Flow:')), 0)
        meta = [
            f'- Create: Create one {speaker} dialogue line for this gameplay moment.',
            f'- Used: {VOICE_USED.get(vid, "This gameplay moment.")}',
            f'- Moment: {VOICE_MOMENT.get(vid, "Gameplay Use")}',
        ]
        filtered[flow_idx:flow_idx] = meta
        out.extend([block[0], *filtered])
    VOICE.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')


def patch_authority() -> None:
    source = SOURCE.read_text(encoding='utf-8')
    if 'SRC-016' not in source:
        source += '''\n\n  - id: SRC-016\n    type: instruction\n    role: authoritative\n    status: current\n    origin: user\n    inspection: full\n    summary: User approved one universal Section 04 Production Assets presentation for every objective. Every objective must use the same two-part structure: WHAT TO BUILD and WHERE IT IS USED. WHAT TO BUILD contains only concrete Minecraft production deliverables and states Type, Create, Used, and optional Includes; exact UI/Text and Voice remain directly copyable. WHERE IT IS USED maps those same deliverables to visible gameplay moments without hiding content. Pure gameplay behavior remains in 03 Development. Animation, sound, and particle work that belongs to one entity/model setup stays inside that setup instead of being split into artificial standalone assets. Renderer behavior must remain generic and must never contain objective-specific layout rules.\n'''
        SOURCE.write_text(source, encoding='utf-8')

    req = REQ.read_text(encoding='utf-8')
    if 'REQ-022' not in req:
        req += '''\n\n  - id: REQ-022\n    area: production-assets\n    statement: Section 04 uses exactly one universal production-handoff template for every gameplay objective: WHAT TO BUILD followed by WHERE IT IS USED. WHAT TO BUILD lists concrete Minecraft production deliverables only, using Type, Name, Create, Used, optional Includes, and exact copy-ready UI/Text or Voice. Do not list pure gameplay behavior as an asset. Animation, sound, particle, state, or visual behavior that is part of a single entity/model setup remains included under that parent setup unless it is genuinely a standalone production resource. WHERE IT IS USED presents a visible ordered map of gameplay moments and the concrete deliverables required at each moment. The renderer may not use objective-specific presentation logic; only source data and moment names vary between objectives.\n    provenance: [SRC-016]\n    evidence_status: approved\n    recovery_class: none\n    approval_status: not_required\n    impact: high\n'''
        REQ.write_text(req, encoding='utf-8')


patch_assets()
patch_voice()
patch_authority()
print('universal Production Assets source migration prepared')
