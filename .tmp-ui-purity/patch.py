from pathlib import Path

ROOT = Path('.')
PROJECT = ROOT / 'workspace/active/the-clockwork-vault'
ASSET = PROJECT / 'work/asset-requirements.md'
SOURCE = PROJECT / 'state/source-inventory.yaml'
REQ = PROJECT / 'state/requirement-register.yaml'
RENDERER = ROOT / 'kits/project-document-generator/renderer/production_assets_objective.py'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly one match, got {count}')
    return text.replace(old, new, 1)


def patch_assets() -> None:
    text = ASSET.read_text(encoding='utf-8')

    text = replace_once(
        text,
        '### Gameplay Flow 01 — Read Partial Target\nFor: Show the objective instructions and incomplete target when Objective 1 starts.',
        '### Gameplay Flow 01 — Read Partial Target\nFor: Start the puzzle with the partial door answer and a light hint to search the chamber.',
        'resonance flow for',
    )
    text = replace_once(
        text,
        '### Gameplay Flow 03 — Experiment with Pillars\nFor: Make pillar identity, color feedback, and pulse state readable while testing controls.',
        '### Gameplay Flow 03 — Experiment with Pillars\nFor: Keep the three pillars easy to distinguish while the player experiments.',
        'pillar flow for',
    )

    old_panel = '''#### Objective 1 Instruction Panel
Flow: 01 — Read Partial Target
For: Give the player the exact Objective 1 instructions without revealing the hidden solution.
Requirement: Create one persistent or easily re-readable instruction panel explaining the player task without revealing the missing colors, pulse location, or lever-to-color mapping. It must make clear that the books reveal missing target information while lever experimentation is used to produce the colors.
Content:
```text
RESTORE THE THREE PILLARS

1. Read the books scattered around the chamber.
2. The door display reveals only part of the final combination.
3. Find the missing LEFT and RIGHT colors and which lamp must PULSE.
4. Try the TOP and BOTTOM levers until each lamp reaches the color you need.

Lever order: TOP → BOTTOM
Pressure Plate: STEADY / PULSE only
```
'''
    new_panel = '''#### Objective 1 Instruction Panel
Flow: 01 — Read Partial Target
For: Hint that the missing answer can be found inside the chamber.
Requirement: Keep the opening prompt short, in-world, and non-technical. It should direct the player to search the chamber without explaining the hidden solution or the machine logic.
Content:
```text
RESTORE THE THREE PILLARS

The door reveals only part of the answer.

Everything you need is somewhere in this chamber.
Search carefully, then restore all three pillars.
```
'''
    text = replace_once(text, old_panel, new_panel, 'objective 1 panel')

    old_pillar = '''#### Pillar State Labels
Flow: 03 — Experiment with Pillars
For: Keep LEFT, MIDDLE, RIGHT and STEADY/PULSE states easy to read.
Requirement: Give each of the three puzzle pillars stable LEFT, MIDDLE, and RIGHT identities so book clues, display information, and live lamp outputs cannot be confused. Each live lamp must make its current color and steady/pulsing state readable at the same time.
Usage: Remains visible throughout Objective 1.

Content:
```text
LEFT
MIDDLE
RIGHT

STEADY
PULSE
```

'''
    text = replace_once(text, old_pillar, '', 'remove technical pillar UI')

    text = replace_once(
        text,
        '''BOOK 1 — LEVER INSTRUCTIONS
Each pillar has two levers. Read the TOP lever first, then the BOTTOM lever. Try different settings and watch the lamp. Each setting produces a different color.

BOOK 2 — PRESSURE PLATE INSTRUCTIONS
The pressure plate does not change the lamp's color. It only changes how the lamp shines. A pressed plate makes the lamp pulse. Otherwise, the lamp stays steady.''',
        '''BOOK 1 — LEVER NOTES
Each pillar is tuned by two levers. Start with the upper lever, then try the lower one. Watch the lamp after each change. Different positions reveal different colors.

BOOK 2 — PRESSURE PLATE NOTES
The plate does not change the lamp's color. It only changes the way the lamp shines. Step on it to make the lamp pulse. Leave it clear to keep the light steady.''',
        'rule book copy',
    )

    resonance_vfx = '''### Visual Effects & Presentation

#### Pillar Interaction Feedback'''
    resonance_vfx_new = '''### Visual Effects & Presentation

#### Pillar Readability
Flow: 03 — Experiment with Pillars
For: Distinguish the Left, Middle, and Right pillars through the environment, not debug-style UI.
Requirement: Make the three pillars readable through stable placement, visual identity, and lamp presentation. Do not add technical state labels such as STEADY/PULSE as standalone player UI.
Usage: Active throughout Objective 1.

#### Pillar Interaction Feedback'''
    text = replace_once(text, resonance_vfx, resonance_vfx_new, 'pillar visual requirement')

    old_warden = '''#### Objective 3 Instruction Panel
Flow: 01 — Learn Trap Rules
For: Give the exact Pebble, laser, floor-trap, axe, and cooldown rules.
Requirement: Create one concise instruction panel that distinguishes Pebble-valid hazards from timing/avoidance hazards and states the 3-second cooldown.
Content:
```text
SURVIVE THE WARDEN HALLS

ECHO PEBBLE
• Wall laser sensors: Disable them for 4 seconds.
• Marked hanging stones: Knock them into a laser beam.
• Floor traps: AVOID.
• Swinging axes: TIME YOUR MOVEMENT.

Pebbles are unlimited · 3 sec cooldown per throw.
```
'''
    new_warden = '''#### Objective 3 Instruction Panel
Flow: 01 — Learn Trap Rules
For: Tell the player what the Echo Pebble can affect and what must be avoided.
Requirement: Keep the trap guidance player-facing and concise while preserving the approved timing rules.
Content:
```text
SURVIVE THE WARDEN HALLS

ECHO PEBBLE
• Hit wall sensors to drop the beam for 4 seconds.
• Knock hanging stones into a laser beam.
• Avoid floor traps.
• Time your movement past swinging axes.

Pebbles never run out · 3 seconds between throws.
```
'''
    text = replace_once(text, old_warden, new_warden, 'warden instruction')

    old_trap = '''#### Trap Warning Readability
Flow: 01 — Learn Trap Rules
For: Label hazard types only where the environment alone is not clear enough.
Requirement: Give wall lasers, floor traps, and swinging axes distinct warning language/icons or in-world markers where additional information is needed. Never mark floor traps or swinging axes as Pebble-disableable.
Usage: Used only where the physical hazard alone would not be sufficiently readable.

Content:
```text
LASER SENSOR · PEBBLE WORKS
HANGING STONE · PEBBLE WORKS
FLOOR TRAP · AVOID
SWINGING AXE · TIME YOUR MOVE
```

'''
    text = replace_once(text, old_trap, '', 'remove technical trap UI')

    warden_vfx = '''### Visual Effects & Presentation

#### Trap Hit Feedback'''
    warden_vfx_new = '''### Visual Effects & Presentation

#### Trap Readability
Flow: 01 — Learn Trap Rules
For: Make lasers, floor traps, and swinging axes readable from their appearance and motion.
Requirement: Communicate hazard type through environment design, animation, beam state, and motion rather than debug-style instructional labels. Floor traps and swinging axes must never look Pebble-disableable.
Usage: Present wherever the physical hazard needs stronger readability.

#### Trap Hit Feedback'''
    text = replace_once(text, warden_vfx, warden_vfx_new, 'trap visual requirement')

    old_workshop_panel = '''#### Objective 4 Instruction Panel
Flow: 01 — Learn Network / Ring 1
For: Give the exact continuous-network rule from Generator through Ring 3.
Requirement: Create one instruction panel explaining the continuous network rule without exposing route coordinates or the layout solution.
Content:
```text
CONNECT THE POWER

Generator → Ring 1 → Ring 2 → Ring 3

Rotate the L-junctions to turn the power route.
Keep every earlier ring connected as you continue.
```
'''
    new_workshop_panel = '''#### Objective 4 Instruction Panel
Flow: 01 — Learn Network / Ring 1
For: Tell the player how to guide one continuous power route through all three rings.
Requirement: Keep the routing instruction player-facing and concise without exposing the authored solution.
Content:
```text
CONNECT THE POWER

Generator → Ring 1 → Ring 2 → Ring 3

Turn the L-shaped junctions to guide the power.
Keep the earlier rings connected as you move forward.
```
'''
    text = replace_once(text, old_workshop_panel, new_workshop_panel, 'workshop instruction')

    text = replace_once(
        text,
        '''#### 50% Sabotage Message
Flow: 04 — 50% Rollback
For: Tell the player Generator → Ring 1 lost alignment and two rotators changed.
Requirement: Tell the player exactly which earlier network section lost alignment and how many rotators were changed, without identifying their positions.
Content:
```text
POWER LOST · GENERATOR → RING 1
Two rotators were turned.
Repair the earlier connection, then continue toward Ring 3.
```
''',
        '''#### 50% Sabotage Message
Flow: 04 — 50% Rollback
For: Tell the player the first power connection has been disrupted.
Requirement: Identify the affected gameplay connection without exposing implementation counts or rotator positions.
Content:
```text
POWER LOST · GENERATOR → RING 1
The first connection has been knocked out of line.
Restore it, then continue toward Ring 3.
```
''',
        '50 sabotage player copy',
    )
    text = replace_once(
        text,
        '''#### 80% Sabotage Message
Flow: 05 — 80% Rollback
For: Tell the player Ring 1 → Ring 2 lost alignment and three rotators changed.
Requirement: Tell the player which second earlier network section lost alignment and how many rotators were changed, without identifying their positions.
Content:
```text
POWER LOST · RING 1 → RING 2
Three rotators were turned.
Restore the connection, then finish Ring 3.
```
''',
        '''#### 80% Sabotage Message
Flow: 05 — 80% Rollback
For: Tell the player an earlier Ring 1 → Ring 2 connection has been disrupted.
Requirement: Identify the affected gameplay connection without exposing implementation counts or rotator positions.
Content:
```text
POWER LOST · RING 1 → RING 2
An earlier connection has been knocked out of line.
Restore it, then finish Ring 3.
```
''',
        '80 sabotage player copy',
    )

    ASSET.write_text(text, encoding='utf-8')


def patch_renderer() -> None:
    text = RENDERER.read_text(encoding='utf-8')
    text = replace_once(text, '.pa-assets{display:grid;gap:8px}', '.pa-assets{display:grid;gap:16px}', 'asset gap')
    old = '.pa-asset-card,.pa-voice-inline{padding:12px 13px;border:1px solid #d8e1e5;border-radius:4px;background:var(--paper);break-inside:avoid}'
    new = old.replace('padding:12px 13px', 'padding:14px 15px').replace('border:1px solid #d8e1e5', 'border:1px solid #cbd7dd').replace('border-radius:4px', 'border-radius:5px')
    text = replace_once(text, old, new, 'asset card base')
    marker = new + '\n.pa-asset-head{display:flex;align-items:center;gap:8px}'
    replacement = new + '\n.pa-asset-card{border-left:4px solid var(--blue)}\n.pa-voice-inline{border-left:4px solid var(--amber)}\n.pa-asset-head{display:flex;align-items:center;gap:8px}'
    text = replace_once(text, marker, replacement, 'asset card separation')
    RENDERER.write_text(text, encoding='utf-8')


def patch_authority() -> None:
    src = SOURCE.read_text(encoding='utf-8').rstrip() + '\n'
    if 'id: SRC-012' not in src:
        src += '''\n  - id: SRC-012
    type: instruction
    role: authoritative
    status: current
    origin: user
    inspection: full
    summary: User requires player-facing UI and text to contain only real gameplay/story copy, never internal development or debug terminology. Production Assets should remain concise: each flow and asset gets a short For statement, exact in-game text is copy-ready, technical mechanic detail stays in Development, and separate assets must have clear visual boundaries. Objective 1 opening guidance should only hint that the missing clues are already in the chamber; the lever rule book should read naturally; technical pillar-state labels and technical trap labels are not player UI.
'''
        SOURCE.write_text(src, encoding='utf-8')

    req = REQ.read_text(encoding='utf-8').rstrip() + '\n'
    if 'id: REQ-018' not in req:
        req += '''\n  - id: REQ-018
    area: production-assets
    statement: Player-facing UI, readable text, and in-game labels must be pure gameplay/story communication. Do not surface internal development terms, debug labels, implementation counts, or technical state labels as player UI unless that information is genuinely required by the gameplay. Keep Production Assets concise with short For statements and clear visual separation between assets. Objective 1 opening copy should hint that the answer is in the chamber without explaining the full mechanic; rule-book wording should feel natural; pillar identity and trap readability belong to environmental/visual presentation rather than technical text labels.
    provenance: [SRC-012]
    evidence_status: approved
    recovery_class: none
    approval_status: not_required
    impact: high
'''
        REQ.write_text(req, encoding='utf-8')


patch_assets()
patch_renderer()
patch_authority()
print('player-facing UI purity patch applied')
