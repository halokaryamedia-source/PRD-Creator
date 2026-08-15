from pathlib import Path

ROOT = Path('.')
PROJECT = ROOT / 'workspace/active/the-clockwork-vault'
ASSET = PROJECT / 'work/asset-requirements.md'
SOURCE = PROJECT / 'state/source-inventory.yaml'
REQ = PROJECT / 'state/requirement-register.yaml'

FLOWS = {
    'Global / Shared Assets': [
        ('01 — Shared Characters',
         'Referenced whenever Custodian Vex or Gremlin appears in a gameplay flow.',
         'Vex reads as the consistent guide while Gremlin reads as the recognizable mischievous saboteur.',
         'Custodian Vex; Gremlin',
         [
             'Vex supports the current idle, speaking, alert, guidance, and completion states used by the approved Voice lines.',
             'Gremlin supports appear, sabotage, taunt, and outsmarted/defeat reaction states.',
             'Both characters stay visually and audibly distinct and can be reused by every referenced flow without duplicate implementations.',
         ]),
    ],
    'The Antechamber': [
        ('01 — Arrival & Briefing',
         'The assigned player enters the protected Antechamber and Custodian Vex activates for the first time.',
         'The player understands why the vault is sealed, what the Great Orrery is, and sees the Custodian Key as the first actionable object.',
         'Custodian Vex; Custodian Key',
         [
             'Vex opening briefing plays once for the current session.',
             'The Custodian Key is clearly visible and available after the briefing.',
             'The player understands the key starts the restoration route and is not the exit key.',
         ]),
        ('02 — Take Key & Open Seal',
         'The opening briefing is complete and the Resonance Engine seal is still closed.',
         'The player takes the key, receives only the minimum reminder if needed, uses the key on the marked seal, and sees the first objective route open.',
         'Custodian Vex; Custodian Key; Resonance Engine seal',
         [
             'The exact key prompt remains readable until valid seal activation.',
             'Valid Custodian Key use opens the Resonance Engine seal once and gives clear feedback.',
             'The handoff into Objective 1 is readable and does not become a separate puzzle.',
         ]),
    ],
    'The Resonance Engine': [
        ('01 — Read Partial Target',
         'The Resonance Engine seal opens and the player gains control inside the reset chamber.',
         'The player immediately sees the basic task and the intentionally incomplete target: Middle is Brown while Left, Right, and Pulse remain unknown.',
         'Custodian Vex; Objective 1 Instruction Panel; Partial Door Target Display',
         [
             'The instruction text is readable and does not reveal the hidden Left/Right colors, pulse location, or lever solutions.',
             'The door display shows Middle = Brown and keeps the other target values unknown.',
             'Vex briefing matches the same information and does not contradict the display.',
         ]),
        ('02 — Search Clues',
         'Objective 1 is active and the twelve scattered books are available around the chamber.',
         'The player searches books in any order, may find useful clues early by luck, and gradually narrows the missing target information without needing every book.',
         'Scattered Clue Book Set',
         [
             'All twelve approved books use the exact current text.',
             'The set remains 2 rule books + 8 useful clues + 2 harmless decoys with no forced reading order.',
             'Decoys contain no false puzzle facts and completion never requires all twelve books.',
         ]),
        ('03 — Experiment with Pillars',
         'The player changes a pillar lever or pressure-plate state while Objective 1 is active.',
         'The player learns each pillar by experimentation: lever combinations change color and the plate changes only steady versus pulse.',
         'Left / Middle / Right pillar labels; pillar lamps; upper/lower levers; pressure plates',
         [
             'LEFT, MIDDLE, and RIGHT identities remain clear from the player position.',
             'Every lever change produces immediate deterministic lamp-color feedback for that pillar.',
             'Pressure plates change only steady/pulse state and never change the selected color.',
         ]),
        ('04 — Complete & Transition',
         'Left = Orange + pulse, Middle = Brown + steady, and Right = Purple + steady are all valid at the same time.',
         'The three pillars visibly synchronize, the Resonance Engine returns to operation, and attention moves to the newly opened Broken Gallery route.',
         'Resonance Engine restoration presentation; pillar completion feedback',
         [
             'Completion validates the full simultaneous final state rather than a partial match.',
             'The completion response plays once and clearly confirms success.',
             'The Broken Gallery route opens and Objective 1 temporary state is ready for the next reset.',
         ]),
    ],
    'The Broken Gallery': [
        ('01 — Enter & Learn Route Loop',
         'The player enters Broken Gallery Level 1 with checkpoint barrels and the three route choices available.',
         'The player learns the repeated loop: search barrels, repair only marked gaps, reach the checkpoint, and retry only the current level on failure.',
         'Custodian Vex; Objective 2 Instruction Panel; Valid Placement Markers',
         [
             'The route-loop instruction text is readable without revealing a viable route.',
             'Legal placement markers are clearly different from ordinary environment blocks.',
             'Vex briefing communicates limited-resource planning and local retry without introducing old mechanics.',
         ]),
        ('02 — Level 1',
         'Checkpoint 1 is active and Level 1 resources/routes are reset.',
         'The player reads three routes, uses the 12-block allocation, and must avoid wasting supplies on the non-viable route.',
         'Level 1 Brief; checkpoint barrels; Valid Placement Markers',
         [
             'The Level 1 brief uses the exact approved text and does not reveal which two routes work.',
             'The authored allocation is 12 blocks and only marked placements are accepted.',
             'Middle and Right remain viable, Left remains non-viable, and successful crossing reaches Checkpoint 2.',
         ]),
        ('03 — Level 2',
         'Checkpoint 2 is active and Level 2 resources/routes are reset.',
         'The player solves a tighter route/resource problem using 20 blocks and 3 ladders while only one route can be completed.',
         'Level 2 Brief; checkpoint barrels; blocks; ladders; Valid Placement Markers',
         [
             'The Level 2 brief uses the exact approved text without naming the viable route.',
             'The authored allocation is 20 blocks + 3 ladders and placement remains marker-owned.',
             'Only the Right route is viable and successful crossing reaches Checkpoint 3.',
         ]),
        ('04 — Level 3 Time Challenge',
         'Checkpoint 3 is active, all three routes are initially viable, and the timed attempt begins when the player materially commits to a route.',
         'The player chooses a route, hears/sees Gremlin-timed urgency, and must reach at least 50% route progress before the authored threshold.',
         'Gremlin; Custodian Vex; Level 3 Time-Challenge Brief; Level 3 Time-Challenge Cue; route-progress state',
         [
             'The exact Level 3 instruction is readable before/during the attempt without revealing route geometry.',
             'The warning cue and Vex line clearly mark the timed requirement.',
             'At least 50% progress before the threshold preserves the chosen route and allows the crossing to continue.',
         ]),
        ('05 — Retry / Route Closure',
         'The active level exhausts its resources or configured time, or a Level 3 attempt misses the 50% progress threshold.',
         'The player gets a local reset. Level 1/2 simply retry; Level 3 visibly loses the failed route while another alternative remains.',
         'Route Failure Message; Level Retry Reset; Gremlin Route-Closed Event',
         [
             'Temporary blocks/ladders from the failed attempt are removed and the active checkpoint becomes safe/retryable.',
             'Current-level resources become available again while earlier completed Gallery levels remain complete.',
             'A failed Level 3 route is visibly unavailable while alternatives remain, and the last remaining route never makes the objective unwinnable before normal timeout.',
         ]),
    ],
    'The Warden Halls': [
        ('01 — Learn Trap Rules',
         'The Warden Halls activate and the player receives the unlimited Echo Pebble before the first trap-family encounters.',
         'The player understands which hazards accept Echo Pebble interaction and which must instead be avoided or timed.',
         'Custodian Vex; Echo Pebble; Wall Laser Sensor; Swinging Axe Trap; Objective 3 Instruction Panel',
         [
             'The instruction panel uses the exact approved trap/Pebble rules.',
             'Wall lasers, floor traps, and swinging axes remain visually distinguishable.',
             'Nothing implies that floor traps or swinging axes can be disabled with Echo Pebble.',
         ]),
        ('02 — Use Echo Pebble',
         'The player throws Echo Pebble at a valid wall-laser sensor or authored hanging-stone target.',
         'A valid sensor hit creates a short four-second laser opening; selected hanging stones can instead block the beam, while the three-second throw cooldown remains readable.',
         'Echo Pebble; Wall Laser Sensor; Laser Blocker Stone; Echo Pebble Cooldown Indicator',
         [
             'Each throw starts the approved 3-second cooldown and the UI returns to READY afterward.',
             'A valid wall-laser sensor hit disables only that laser for 4 seconds of game-time.',
             'Only authored hanging-stone targets create the alternate beam-blocking solution; invalid floor/axe targets do not disable anything.',
         ]),
        ('03 — Hazard Contact & Recovery',
         'The player contacts a laser, floor trap, or swinging axe, or gameplay health reaches zero from Warden hazards.',
         'The player receives hazard-specific feedback/effects; zero gameplay health returns them to the current safe checkpoint instead of restarting the full objective.',
         'Trap Hit Feedback; Checkpoint Recovery; active Warden checkpoint',
         [
             'Laser, floor, and axe contacts apply their approved damage/status effects and remain distinguishable.',
             'Gameplay health reaching zero returns the player to the active Warden checkpoint in a safe recovered state.',
             'Earlier completed Warden levels remain complete after checkpoint recovery.',
         ]),
        ('04 — Complete & Transition',
         'The player clears the third Warden level and reaches the inner gate.',
         'Vex acknowledges that the Wardens are still serving the vault and directs the player into Gremlin’s Workshop.',
         'Custodian Vex; inner gate transition',
         [
             'The transition Voice plays once without replaying Pebble instructions.',
             'The Workshop route becomes the clear next destination.',
             'No Workshop sabotage is revealed before its authored trigger.',
         ]),
    ],
    "The Gremlin's Workshop": [
        ('01 — Learn Network & Ring 1',
         'The player enters the Workshop and the unsabotaged L-rotator network becomes interactive.',
         'The player learns that power begins at the Generator, each rotator is an L connection, and one continuous route must reach Ring 1.',
         'Custodian Vex; Power Generator; 90-Degree Rotator Junction; Orrery Ring; Objective 4 Instruction Panel; Ring Progress Display',
         [
             'The instruction text explains Generator → Ring 1 → Ring 2 → Ring 3 without exposing the authored route solution.',
             'Each rotator has four readable orientations and powered/unpowered state is visually clear.',
             'Ring 1 becomes powered only when a continuous valid path exists from the Generator.',
         ]),
        ('02 — Extend to Ring 2',
         'Ring 1 is powered and the player continues the same network toward Ring 2.',
         'The player extends the existing live route while keeping Ring 1 connected; the status display reflects actual connectivity.',
         'Power Generator; 90-Degree Rotator Junction; Orrery Rings; Ring Progress Display',
         [
             'Ring 2 becomes powered only while Generator → Ring 1 → Ring 2 is continuously connected.',
             'The Ring Progress Display immediately reflects any real loss of power rather than milestone history.',
             'The post-Ring-2 route-swap trigger becomes eligible only after the approved stable state.',
         ]),
        ('03 — Route Swap Sabotage',
         'About 20 seconds after Ring 1 and Ring 2 are continuously connected.',
         'Gremlin deliberately blocks the route the player just used, a previously blocked alternate path opens, Ring 2 loses power, Gremlin taunts, then Vex gives recovery guidance.',
         'Gremlin; Custodian Vex; Power Generator; 90-Degree Rotator Junction; Ring Progress Display; First Sabotage Message',
         [
             'The route-swap sabotage triggers once for the session.',
             'The old route becomes clearly unavailable, the authored alternate opens, and connectivity/power is recalculated immediately.',
             'The exact sabotage text plus Gremlin and Vex lines play in the intended order without revealing the solution path.',
             'The player can recover using the same L-rotator rule.',
         ]),
        ('04 — 50% Rollback',
         'Validated Ring 2 → Ring 3 route progress reaches 50% for the first time.',
         'Gremlin rotates exactly two previously correct Generator → Ring 1 rotators, earlier power drops, Gremlin gloats, and Vex directs the player back to repair the link.',
         'Gremlin; Custodian Vex; 90-Degree Rotator Junction; Ring Progress Display; 50% Sabotage Message',
         [
             'Exactly two approved Generator → Ring 1 rotators change orientation once.',
             'Power loss propagates immediately and the exact 50% message identifies the affected section without exposing rotator positions.',
             'Gremlin taunt and Vex repair guidance play without changing the learned routing rule.',
         ]),
        ('05 — 80% Rollback',
         'Validated Ring 2 → Ring 3 route progress reaches 80% for the first time.',
         'Gremlin rotates exactly three previously correct Ring 1 → Ring 2 rotators, removes earlier power again, and the player must repair that section before finishing.',
         'Gremlin; Custodian Vex; 90-Degree Rotator Junction; Ring Progress Display; 80% Sabotage Message',
         [
             'Exactly three approved Ring 1 → Ring 2 rotators change orientation once.',
             'The exact 80% message and visible power state make the broken earlier section clear.',
             'Gremlin and Vex lines play in order and the player can repair with the same L-rotator rule.',
         ]),
        ('06 — Restore Great Orrery',
         'Generator, Ring 1, Ring 2, and Ring 3 are all continuously connected after all authored sabotage events.',
         'Gremlin realizes the player has outsmarted the sabotage, all rings synchronize, the Great Orrery returns to life, puzzle input closes, and the exit begins opening.',
         'Gremlin; Power Generator; Orrery Rings; Great Orrery Restoration',
         [
             'Completion requires one continuous final network across Generator and all three rings.',
             'Gremlin’s outsmarted reaction plays once and does not replace Vex’s later ending speech.',
             'The final restoration presentation clearly confirms success and begins the ending/exit handoff.',
         ]),
    ],
    'Vault Restored': [
        ('01 — Restoration Payoff & Reward',
         'The Great Orrery restoration callbacks complete and the closing scene reaches Vex recognition.',
         'Vex acknowledges what the player restored, the gateway is open, and the Clockwork Wayfinder reward is presented after the completion record is secured.',
         'Custodian Vex; Clockwork Wayfinder; Completion Message; Great Orrery / gateway presentation',
         [
             'The completion message and Vex line use the exact approved wording without exposing platform scoring.',
             'The Clockwork Wayfinder is presented/granted exactly once after the completion state is secured.',
             'The reopened gateway is clearly visible as the next action.',
         ]),
        ('02 — Return Home',
         'Session result and reward state are secured and the safe return route is open.',
         'Vex gives one concise farewell/navigation cue and the player follows the reopened route back to the holding area while lane cleanup begins safely.',
         'Custodian Vex; Vault Awakening and Exit Reveal; safe return route',
         [
             'The exact safe-return Voice cue plays without repeating the completion speech.',
             'The return route is obvious and no new gameplay task is introduced.',
             'Lane reset/cleanup does not invalidate the player’s safe return and prepares the lane for reuse.',
         ]),
    ],
}


def flow_block(section):
    lines = []
    for title, trigger, experience, uses, done in FLOWS[section]:
        lines += [
            f'### Gameplay Flow {title}',
            f'Trigger: {trigger}',
            f'Player Experience: {experience}',
            f'Uses: {uses}',
            'Done When:',
        ]
        lines += [f'- {item}' for item in done]
        lines.append('')
    return '\n'.join(lines).rstrip()


def patch_asset_requirements():
    text = ASSET.read_text(encoding='utf-8')
    if '### Gameplay Flow ' in text:
        raise SystemExit('Gameplay Flow metadata already exists; refusing duplicate insertion')
    lines = text.splitlines()
    out = []
    for line in lines:
        out.append(line)
        if line.startswith('## '):
            section = line[3:].strip()
            if section in FLOWS:
                out += ['', flow_block(section), '']
    missing = [section for section in FLOWS if f'## {section}' not in text]
    if missing:
        raise SystemExit('Missing asset sections: ' + ', '.join(missing))
    ASSET.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')


def patch_authority():
    src = SOURCE.read_text(encoding='utf-8')
    if 'id: SRC-011' not in src:
        src += '''\n  - id: SRC-011\n    type: instruction\n    role: authoritative\n    status: current\n    origin: user\n    inspection: full\n    summary: User approved the final developer-facing Production Assets information architecture: each gameplay flow is an implementation pack with Trigger, Player Experience, Implementation Checklist, direct asset purpose/use, exact per-item copy/Voice, and Done When. Quick Jump remains. Asset counts, asset numbering, category-first grouping, and Copy Flow Text are not useful primary UI and must not drive the presentation.\n'''
        SOURCE.write_text(src, encoding='utf-8')

    req = REQ.read_text(encoding='utf-8')
    old_start = '  - id: REQ-017\n    area: production-assets\n    statement:'
    if old_start not in req:
        raise SystemExit('REQ-017 not found')
    import re
    pattern = re.compile(r'  - id: REQ-017\n    area: production-assets\n    statement:.*?    impact: high', re.S)
    replacement = '''  - id: REQ-017\n    area: production-assets\n    statement: Production Assets must behave as developer implementation packs organized by gameplay flow. Each flow shows its Trigger, intended Player Experience, reusable assets it depends on, an Implementation Checklist, the concrete assets/Voice needed with a direct explanation of what each is for and when it is used, exact per-item player text or Voice prompt with individual Copy actions, and a Done When checklist. Quick Jump between flows remains. Asset-category-first grouping, asset counts, asset numbering, and Copy Flow Text aggregation must not be used as the primary developer experience.\n    provenance: [SRC-009, SRC-010, SRC-011]\n    evidence_status: approved\n    recovery_class: none\n    approval_status: not_required\n    impact: high'''
    req2, count = pattern.subn(replacement, req, count=1)
    if count != 1:
        raise SystemExit('REQ-017 replacement failed')
    REQ.write_text(req2, encoding='utf-8')


patch_asset_requirements()
patch_authority()
print('implementation-pack metadata prepared')
