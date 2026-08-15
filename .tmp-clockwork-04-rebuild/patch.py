from pathlib import Path
import re

ROOT = Path('.')
PROJECT = ROOT / 'workspace/active/the-clockwork-vault'
ASSET = PROJECT / 'work/asset-requirements.md'
VOICE_REQ = PROJECT / 'work/voice-requirements.md'
VOICE_PROD = PROJECT / 'work/voice-production.md'
SOURCE = PROJECT / 'state/source-inventory.yaml'
REQ = PROJECT / 'state/requirement-register.yaml'
RENDERER = ROOT / 'kits/project-document-generator/renderer/production_assets_objective.py'

VOICE_REQUIREMENTS = r'''# The Clockwork Vault Voice Requirements

Source PRD revision: 1.0.0
Voice system: Custodian Vex · direct in-world narrative guide; Gremlin · direct in-world mischievous character in the Broken Gallery final crossing and Objective 4 sabotage; no radio/communicator layer

Voice direction: Voice exists for story, character, atmosphere, reaction, and light in-world hints. It must not read the Development specification aloud. Exact thresholds, reset logic, route viability, implementation counts, cooldown math, and other technical rules belong to Development or concise player UI when genuinely necessary.

## 01. The Antechamber

### VO-ANTE-01 — Vault Restoration Briefing
- Type: Main Story
- Function: story_opening
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The assigned player enters the protected Antechamber and Vex activates for the first time.
- Flow: 01 — Arrival & Briefing
- For: Establish the vault, Great Orrery, and the player's reason to continue.
- Purpose: Open the story and establish that restoring the vault is the only way home.
- Must communicate:
  - The entrance will not reopen on its own.
  - The vault protects the Great Orrery.
  - Four connected systems stand between the player and the Orrery.
  - The Custodian Key begins the restoration journey.
- Must not add/repeat:
  - Do not explain later objective mechanics.
  - Do not sound like a tutorial checklist.
  - Do not imply the Custodian Key directly opens the exit.
- Source refs:
  - content.md → The Journey Begins
  - content.md → The Antechamber

### VO-ANTE-02 — Custodian Key Reminder
- Type: Direct NPC Dialogue
- Function: reminder
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: After the opening briefing, the player has not yet used the Custodian Key on the first seal.
- Flow: 02 — Take Key & Open Seal
- For: Give one in-world reminder that the Custodian Key belongs to the first seal.
- Purpose: Nudge the player forward without replaying the opening story.
- Must communicate:
  - The key belongs at the first seal.
- Must not add/repeat:
  - Do not mention reset, state, or objective logic.
  - Do not replay the vault history.
- Source refs:
  - content.md → The Antechamber

## 02. The Resonance Engine

### VO-RES-01 — The Engine Remembers
- Type: Main Story
- Function: story_hint
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Resonance Engine seal opens and the player enters the chamber with the partial door display visible.
- Flow: 01 — Read Partial Target
- For: Give the Resonance Engine mystery a story voice and hint that the missing answer remains in the chamber.
- Purpose: Frame Objective 1 as restoring an old machine whose missing knowledge is still present in the room.
- Must communicate:
  - The Resonance Engine once helped keep the vault in tune.
  - The door remembers only part of the answer.
  - The rest can still be found in the chamber.
- Must not add/repeat:
  - Do not explain lever combinations, pressure-plate behavior, clue counts, or the hidden answer.
  - Do not tell the player to read every book.
  - Do not sound like a puzzle manual.
- Source refs:
  - content.md → The Resonance Engine
  - REQ-014
  - REQ-015

## 03. The Broken Gallery

### VO-GAL-01 — The Gallery Has Fallen
- Type: Main Story
- Function: story_atmosphere
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player first enters the Broken Gallery.
- Flow: 01 — Enter & Learn Route Loop
- For: Establish the Gallery's collapse and hint that Gremlin has already been through it.
- Purpose: Give the traversal challenge story context without reading its route/resource rules aloud.
- Must communicate:
  - The Gallery once carried the vault's keepers deeper inside.
  - Much of it was lost in the collapse.
  - Gremlin has interfered with this part of the vault.
- Must not add/repeat:
  - Do not explain barrels, placement markers, resource counts, retries, or viable routes.
  - Do not use checkpoint/reset language.
- Source refs:
  - content.md → The Broken Gallery

### VO-GAL-02 — Gremlin's Wager
- Type: Direct NPC Dialogue
- Function: character_challenge
- Necessity: required
- Speaker: Gremlin
- Channel: Direct
- Trigger: The final Gallery crossing begins and the player is about to choose a route.
- Flow: 04 — Level 3 Time Challenge
- For: Let Gremlin personally challenge the player before the final crossing.
- Purpose: Create urgency and character without stating the internal threshold or retry rules.
- Must communicate:
  - Gremlin is watching the crossing.
  - The player should move quickly.
  - Gremlin may take the chosen path away.
- Must not add/repeat:
  - Do not say 50 percent, checkpoint, threshold, viable route, reset, or authored timer.
  - Do not name a correct route.
- Source refs:
  - content.md → The Broken Gallery → Level 3
  - REQ-004

## 04. The Warden Halls

### VO-WARD-01 — The Wardens Are Listening
- Type: Main Story
- Function: story_hint
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Warden Halls activate and the player receives the Echo Pebble.
- Flow: 01 — Learn Trap Rules
- For: Establish the Wardens as active guardians and give one light in-world hint about the Echo Pebble.
- Purpose: Support the fiction of the Warden Halls without narrating cooldowns and exact hazard rules.
- Must communicate:
  - The Wardens are still active.
  - Wall sensors can be distracted by the Echo Pebble.
  - Floor traps and axes will not be fooled the same way.
- Must not add/repeat:
  - Do not state the 3-second cooldown or 4-second laser window.
  - Do not list hazard damage/status effects.
  - Do not sound like an instruction manual.
- Source refs:
  - content.md → The Warden Halls
  - REQ-005

### VO-WARD-02 — The Wardens Still Serve
- Type: Main Story
- Function: transition
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player clears the third Warden level and the route toward Gremlin's Workshop opens.
- Flow: 04 — Complete & Transition
- For: Close the Warden Halls story beat and point the journey toward the Workshop.
- Purpose: Connect the active security system to the Great Orrery story.
- Must communicate:
  - The Wardens never stopped protecting the Orrery.
  - Parts of the vault are still working.
  - The Workshop is next.
- Must not add/repeat:
  - Do not replay Echo Pebble rules.
  - Do not reveal Workshop sabotage.
- Source refs:
  - content.md → The Warden Halls → Transition

## 05. The Gremlin’s Workshop

### VO-WORK-01 — The Orrery's Heart
- Type: Main Story
- Function: story_reveal
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player enters the Workshop and sees the Generator and Orrery rings.
- Flow: 01 — Learn Network / Ring 1
- For: Reveal the Workshop as the heart of the Great Orrery and frame the restoration goal.
- Purpose: Give the final objective narrative weight without explaining L-junction geometry.
- Must communicate:
  - This is the heart of the Great Orrery's power system.
  - Power once crossed the rings without a break.
  - Bringing the current back can wake the vault.
- Must not add/repeat:
  - Do not explain right angles, exact rotator rules, route coordinates, or sabotage timing.
  - Do not sound like an engineering tutorial.
- Source refs:
  - content.md → The Gremlin’s Workshop
  - REQ-007

### VO-GREM-01 — Route Swap Taunt
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: The route-swap sabotage blocks the player's old path and opens the alternate path.
- Flow: 03 — Route Swap Sabotage
- For: Let Gremlin gloat when he takes the player's route away.
- Purpose: Make the sabotage feel intentional and character-driven.
- Must communicate:
  - Gremlin caused the disruption.
  - Gremlin enjoys the inconvenience.
- Must not add/repeat:
  - Do not explain the alternate route or connector logic.
- Source refs:
  - REQ-008
  - REQ-016

### VO-WORK-02 — Ring Two Goes Dark
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Immediately after the route-swap sabotage visibly cuts power to Ring 2.
- Flow: 03 — Route Swap Sabotage
- For: Have Vex react naturally when Ring Two loses power and a new path opens.
- Purpose: Keep the player oriented without restating routing rules.
- Must communicate:
  - Gremlin cut the line.
  - Ring Two is dark.
  - A new path must be found.
- Must not add/repeat:
  - Do not say rotator rule, continuous network, connector rule, or exact solution path.
- Source refs:
  - content.md → The Gremlin’s Workshop → First Gremlin Sabotage
  - REQ-008

### VO-GREM-02 — First Rollback Taunt
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: The first rollback sabotage breaks the earlier line to Ring 1.
- Flow: 04 — 50% Rollback
- For: Let Gremlin enjoy undoing an earlier part of the player's work.
- Purpose: Escalate Gremlin's nuisance personality without exposing implementation details.
- Must communicate:
  - Gremlin disturbed an earlier line.
  - Gremlin enjoys forcing the player backward.
- Must not add/repeat:
  - Do not mention percentages, rotator counts, positions, or repair logic.
- Source refs:
  - REQ-008
  - REQ-016

### VO-WORK-03 — Gremlin Strikes Back
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Immediately after the first rollback makes Ring 1 lose power.
- Flow: 04 — 50% Rollback
- For: Have Vex react to Gremlin attacking the earlier line.
- Purpose: Point attention backward without reading the repair specification aloud.
- Must communicate:
  - Gremlin has gone back after the first ring.
  - The player's earlier work is being undone.
- Must not add/repeat:
  - Do not mention 50 percent, exact rotators, orientations, or implementation rules.
- Source refs:
  - content.md → The Gremlin’s Workshop → Level 3 Rollback Events

### VO-GREM-03 — Second Rollback Taunt
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: The second rollback sabotage breaks the earlier line to Ring 2.
- Flow: 05 — 80% Rollback
- For: Let Gremlin taunt the player one last time before the final repair.
- Purpose: Escalate the final nuisance beat without becoming gameplay instruction.
- Must communicate:
  - Gremlin sabotaged the network again.
  - Gremlin is enjoying the player's frustration.
- Must not add/repeat:
  - Do not mention 80 percent, rotator counts, positions, or repair logic.
- Source refs:
  - REQ-008
  - REQ-016

### VO-WORK-04 — One More Sabotage
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Immediately after the second rollback makes Ring 2 lose power.
- Flow: 05 — 80% Rollback
- For: Have Vex react to the final setback and keep the story momentum moving.
- Purpose: Keep the affected ring readable without restating the routing specification.
- Must communicate:
  - Gremlin struck the earlier line again.
  - Ring Two is dark.
  - The player is close to finishing.
- Must not add/repeat:
  - Do not mention 80 percent, exact rotators, or implementation rules.
- Source refs:
  - content.md → The Gremlin’s Workshop → Level 3 Rollback Events

### VO-GREM-04 — Outsmarted Reaction
- Type: Direct NPC Dialogue
- Function: completion
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: The full Orrery network is restored after all sabotage events and the Great Orrery begins to wake.
- Flow: 06 — Restore Great Orrery
- For: Give Gremlin one short defeated reaction when the player finally outsmarts him.
- Purpose: Close Gremlin's character beat before Vex owns the ending.
- Must communicate:
  - Gremlin realizes the player succeeded despite the sabotage.
  - Gremlin gives up interfering with this completed attempt.
- Must not add/repeat:
  - Do not replace Vex's completion speech.
  - Do not kill or permanently remove Gremlin from the world.
- Source refs:
  - REQ-016

## 06. Vault Restored

### VO-END-01 — The Vault Is Awake
- Type: Main Story
- Function: completion
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Great Orrery restoration completes and the closing scene reaches Vex.
- Flow: 01 — Restoration Payoff & Reward
- For: Resolve Vex's story and reward the player after the Great Orrery wakes.
- Purpose: Confirm that the player restored the vault rather than merely escaping it.
- Must communicate:
  - The Great Orrery is awake.
  - The player restored what the vault was built to protect.
  - The gateway is open.
  - The Clockwork Wayfinder is the reward.
- Must not add/repeat:
  - Do not expose platform scoring or internal completion state.
  - Do not introduce another challenge.
- Source refs:
  - content.md → The Vault Awakens

### VO-END-02 — The Way Home
- Type: Main Story
- Function: farewell
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The gateway is open and the player can leave the restored vault.
- Flow: 02 — Return Home
- For: Give one final in-world farewell as the gateway home opens.
- Purpose: Close Vex's guide role without using session-management terminology.
- Must communicate:
  - The way home is clear.
  - Follow the gateway.
- Must not add/repeat:
  - Do not say holding area, lane, reset, cleanup, session result, or other internal terms.
  - Do not replay the completion speech.
- Source refs:
  - content.md → The Vault Awakens → Leaving the Clockwork Vault
'''

VOICE_PRODUCTION = r'''# The Clockwork Vault Voice Production
Version: 1.4.0
Source Voice Requirements: 1.0.0 / work/voice-requirements.md

Voice Cast:
- Custodian Vex: William Shanks - Rich and Deep
- Gremlin: The Cheeky Trickster — selected ElevenLabs voice; young, mid-high pitch, quick, mischievous, teasing, and clearly distinct from Vex.

## 01. The Antechamber

### VO-ANTE-01 — Vault Restoration Briefing
Type: Main Story
Speaker: Custodian Vex
Estimated Duration: 16–19 seconds

```performance
[serious]
You made it inside... but the entrance won't reopen on its own.

This vault protects the Great Orrery. Four old systems between us and that machine have gone dark.

[reassuring]
Take the Custodian Key. Wake them again, and the vault may finally open a way home.
```

### VO-ANTE-02 — Custodian Key Reminder
Type: Direct NPC Dialogue
Speaker: Custodian Vex
Estimated Duration: 4–5 seconds

```performance
[gently]
That key belongs to the first seal.
Give it a try.
```

## 02. The Resonance Engine

### VO-RES-01 — The Engine Remembers
Type: Main Story
Speaker: Custodian Vex
Estimated Duration: 11–14 seconds

```performance
[thoughtful]
The Resonance Engine once kept the whole vault in tune.

Now even the door has forgotten most of its answer.

Look around. This chamber may remember more than it seems.
```

## 03. The Broken Gallery

### VO-GAL-01 — The Gallery Has Fallen
Type: Main Story
Speaker: Custodian Vex
Estimated Duration: 11–14 seconds

```performance
[cautious]
This gallery once carried every keeper deeper into the vault.

Most of it didn't survive the collapse.

What's left will have to be enough... and if you hear laughing, Gremlin's been here.
```

### VO-GAL-02 — Gremlin's Wager
Type: Direct NPC Dialogue
Speaker: Gremlin
Estimated Duration: 5–7 seconds

```performance
[mischievous]
Oh, this part is fun.
Pick a path—quickly.
I might not leave it there for long!
```

## 04. The Warden Halls

### VO-WARD-01 — The Wardens Are Listening
Type: Main Story
Speaker: Custodian Vex
Estimated Duration: 12–15 seconds

```performance
[serious]
The Wardens are still awake. They were built to listen as much as watch.

That pebble may distract their wall sensors.

The floor and the axes, though... they won't be fooled.
```

### VO-WARD-02 — The Wardens Still Serve
Type: Main Story
Speaker: Custodian Vex
Estimated Duration: 8–10 seconds

```performance
[thoughtful]
The Wardens never stopped protecting the Orrery.

Parts of this vault are still working.

Keep moving—the Workshop is next.
```

## 05. The Gremlin’s Workshop

### VO-WORK-01 — The Orrery's Heart
Type: Main Story
Speaker: Custodian Vex
Estimated Duration: 11–14 seconds

```performance
[awed]
There it is—the heart of the Great Orrery.

Power once crossed these rings without a break.

Bring that current back, and the vault may finally remember how to wake.
```

### VO-GREM-01 — Route Swap Taunt
Type: Direct NPC Dialogue
Speaker: Gremlin
Estimated Duration: 4–6 seconds

```performance
[mischievous]
Heh! Liked that route? Too bad—I blocked it.
Let's see what you do now!
```

### VO-WORK-02 — Ring Two Goes Dark
Type: Direct NPC Dialogue
Speaker: Custodian Vex
Estimated Duration: 6–8 seconds

```performance
[alert]
He cut the line! Ring Two's gone dark.

Find the new path before he gets another idea.
```

### VO-GREM-02 — First Rollback Taunt
Type: Direct NPC Dialogue
Speaker: Gremlin
Estimated Duration: 3–5 seconds

```performance
[gleeful]
Ha! I tugged at the first line.
Back you go!
```

### VO-WORK-03 — Gremlin Strikes Back
Type: Direct NPC Dialogue
Speaker: Custodian Vex
Estimated Duration: 5–7 seconds

```performance
[urgent]
He's gone back after the first ring.

Don't let him undo your work.
```

### VO-GREM-03 — Second Rollback Taunt
Type: Direct NPC Dialogue
Speaker: Gremlin
Estimated Duration: 3–5 seconds

```performance
[taunting]
Not again? Oh, yes—again!
I couldn't let you finish that easily.
```

### VO-WORK-04 — One More Sabotage
Type: Direct NPC Dialogue
Speaker: Custodian Vex
Estimated Duration: 5–7 seconds

```performance
[urgent]
Again—he struck the line behind you.

Ring Two's gone dark. You're close. Bring it back.
```

### VO-GREM-04 — Outsmarted Reaction
Type: Direct NPC Dialogue
Speaker: Gremlin
Estimated Duration: 4–6 seconds

```performance
[startled]
What?! You fixed ALL of it?
...Fine! Keep your ridiculous Orrery!
```

## 06. Vault Restored

### VO-END-01 — The Vault Is Awake
Type: Main Story
Speaker: Custodian Vex
Estimated Duration: 15–18 seconds

```performance
[slows down]
Listen... the whole vault is moving again.

You didn't just escape it—you restored what it was built to protect.

The Great Orrery is awake, and the gateway is open.

[warmly]
Take the Clockwork Wayfinder. You've earned it.
```

### VO-END-02 — The Way Home
Type: Main Story
Speaker: Custodian Vex
Estimated Duration: 3–5 seconds

```performance
[warmly]
The way home is clear.
Follow the gateway.
```
'''

FLOW_FOR = {
    'Global / Shared Assets': {'01 — Shared Characters': 'Reusable Vex and Gremlin character assets used across the story.'},
    'The Antechamber': {
        '01 — Arrival & Briefing': 'Opening story and the Custodian Key reveal.',
        '02 — Take Key & Open Seal': 'Key handoff and opening of the Resonance Engine.',
    },
    'The Resonance Engine': {
        '01 — Read Partial Target': 'Introduce the incomplete answer and the mystery of the chamber.',
        '02 — Search Clues': 'Clues left behind by the vault’s former keepers.',
        '03 — Experiment with Pillars': 'Readable pillar feedback while the player experiments.',
        '04 — Complete & Transition': 'Resonance Engine restoration and the route opening.',
    },
    'The Broken Gallery': {
        '01 — Enter & Learn Route Loop': 'Introduce the collapsed Gallery and the supplies left behind.',
        '02 — Level 1': 'First crossing through the Broken Gallery.',
        '03 — Level 2': 'Second, tighter crossing through the Broken Gallery.',
        '04 — Level 3 Time Challenge': 'Gremlin’s timed final crossing.',
        '05 — Retry / Route Closure': 'Failure feedback when a route gives way.',
    },
    'The Warden Halls': {
        '01 — Learn Trap Rules': 'Introduce the Wardens and the Echo Pebble.',
        '02 — Use Echo Pebble': 'Echo Pebble interactions and sensor feedback.',
        '03 — Hazard Contact & Recovery': 'Trap-hit and recovery presentation.',
        '04 — Complete & Transition': 'Story transition into the Workshop.',
    },
    "The Gremlin's Workshop": {
        '01 — Learn Network / Ring 1': 'Introduce the Orrery power network and the first ring.',
        '02 — Extend to Ring 2': 'Show the restored current reaching Ring Two.',
        '03 — Route Swap Sabotage': 'Gremlin blocks the old route and forces a new path.',
        '04 — 50% Rollback': 'Gremlin disrupts the first powered line.',
        '05 — 80% Rollback': 'Gremlin disrupts the second powered line.',
        '06 — Restore Great Orrery': 'Final restoration of the Great Orrery.',
    },
    'Vault Restored': {
        '01 — Restoration Payoff & Reward': 'Final restoration payoff and the Clockwork Wayfinder reward.',
        '02 — Return Home': 'Farewell and the open gateway home.',
    },
}

ENTRY_REPLACEMENTS = {
    'First Objective Prompt': r'''#### First Objective Prompt
Flow: 02 — Take Key & Open Seal
For: Point the player toward the first seal.
Requirement: Keep the prompt short and fully in-world.
Content:
```text
TAKE THE CUSTODIAN KEY
The first seal is waiting.
```
''',
    'First Seal Activation': r'''#### Resonance Engine Seal Opening
Flow: 02 — Take Key & Open Seal
For: Show the first seal accepting the key and opening the Resonance Engine entrance.
Requirement: Use one short presentation sequence: the seal responds, the door unlocks, and the route ahead becomes obvious. Any sound is a separate SFX asset if produced.
Usage: Plays once when the Custodian Key is accepted.
''',
    'Objective 1 Instruction Panel': r'''#### Objective 1 Instruction Panel
Flow: 01 — Read Partial Target
For: Hint that the missing answer is still somewhere in the chamber.
Requirement: Keep the opening prompt short, mysterious, and non-technical.
Content:
```text
RESTORE THE THREE PILLARS

The door remembers only part of the answer.

Everything else you need is somewhere in this chamber.
Look carefully, then bring the Engine back to life.
```
''',
    'Scattered Clue Book Set': r'''#### Scattered Clue Book Set
Flow: 02 — Search Clues
For: Provide the scattered notes that reveal the missing answer.
Requirement: Keep all twelve books short, natural, and readable as old vault notes. Two teach machine behavior, eight provide useful clues, and two are harmless maintenance notes. No reading order is required.
Content:
```text
BOOK 1 — LEVER NOTES
Each pillar is tuned by two levers. Try the upper one, then the lower, and watch how the lamp answers. Different positions reveal different colors.

BOOK 2 — PULSE NOTES
The floor plate never changes a lamp's color. It only changes its rhythm. Step on it and the light will pulse; leave it clear and the light stays steady.

BOOK 3 — LAMP NOTE
The left lamp should have a warm glow. It should not look pale or too dark.

BOOK 4 — OLD ENGINEER'S NOTE
The left light was described as closer to firelight than to the soft color of a flower.

BOOK 5 — MAINTENANCE RECORD
When the Engine was working properly, the left side gave off a gentle glow like warm embers.

BOOK 6 — LAMP RECORD
The right lamp should not use the bright shade of sunlight or the color of fresh leaves.

BOOK 7 — SAFETY NOTE
The correct right-side light is deeper and calmer than the color normally used for danger warnings.

BOOK 8 — OLD VAULT RECORD
The right lamp was once compared to a dark ceremonial cloth used for important occasions.

BOOK 9 — RHYTHM NOTE
When the Engine was balanced, only one lamp pulsed. The middle lamp remained steady.

BOOK 10 — CALIBRATION NOTE
The right lamp remained steady as well. That leaves only one place for the pulse.

BOOK 11 — REPAIR LOG
The lower gear housing was repaired after the last restoration cycle. No further damage was found during inspection.

BOOK 12 — WORKSHOP NOTE
Spare tools were moved to the eastern storage cabinet after the last maintenance shift.
```
''',
    'Objective 2 Instruction Panel': r'''#### Objective 2 Instruction Panel
Flow: 01 — Enter & Learn Route Loop
For: Point the player toward the old supplies and the damaged crossings.
Requirement: Keep the Gallery instruction short and in-world.
Content:
```text
THE BROKEN GALLERY

The old stores still hold what you need.
Repair only the marked breaks and find a way across.
```
''',
    'Level 1 Brief': r'''#### Level 1 Brief
Flow: 02 — Level 1
For: Frame the first crossing without giving away the route.
Requirement: Keep the message short and avoid system-style difficulty labels.
Content:
```text
FIRST CROSSING

More than one path can still hold.
Choose carefully before you spend your supplies.
```
''',
    'Level 2 Brief': r'''#### Level 2 Brief
Flow: 03 — Level 2
For: Frame the tighter second crossing without naming the answer.
Requirement: Keep the message short and in-world.
Content:
```text
SECOND CROSSING

Only one path still holds.
Count what you have before you commit.
```
''',
    'Level 3 Time-Challenge Brief': r'''#### Level 3 Time-Challenge Brief
Flow: 04 — Level 3 Time Challenge
For: Make Gremlin's final crossing feel dangerous without exposing internal timing language.
Requirement: Use player-facing language; “halfway” is allowed, internal percentages/threshold terminology are not.
Content:
```text
GREMLIN'S WAGER

Pick a path.
Reach halfway before the clock runs out,
or Gremlin will take that route away.
```
''',
    'Route Failure Message': r'''#### Route Failure Message
Flow: 05 — Retry / Route Closure
For: Give simple in-world feedback when a crossing fails.
Requirement: Do not mention checkpoints, local resets, resource state, or run-state terminology.
Content:
```text
TRY ANOTHER WAY
The crossing has given out.
Take another look at the routes.

PATH LOST
Gremlin took that route.
Find another way across.
```
''',
    'Valid Placement Markers': r'''#### Repair Markers
Flow: 01 — Enter & Learn Route Loop
For: Make repairable gaps visually distinct without putting debug text into the world.
Requirement: Use an environmental marker treatment for valid repair positions. Do not display labels such as BUILD HERE.
Usage: Visible only at authored repair positions.
''',
    'Objective 3 Instruction Panel': r'''#### Objective 3 Instruction Panel
Flow: 01 — Learn Trap Rules
For: Give one in-world hint about the Echo Pebble and the Warden hazards.
Requirement: Keep exact cooldown/damage math in Development; player text should read like part of the vault.
Content:
```text
THE WARDEN HALLS

The Wardens are still listening.
Echo Pebbles can disturb the wall sensors.
Loose stones may break a beam.

The floor and the axes will not be fooled.
```
''',
    'Echo Pebble Cooldown Indicator': r'''#### Echo Pebble Cooldown Indicator
Flow: 02 — Use Echo Pebble
For: Show when the Echo Pebble can be thrown again.
Requirement: Keep the HUD state compact; the exact recharge duration stays in Development.
Content:
```text
ECHO PEBBLE · READY
ECHO PEBBLE · RECHARGING
```
''',
    'Objective 4 Instruction Panel': r'''#### Objective 4 Instruction Panel
Flow: 01 — Learn Network / Ring 1
For: Frame the final objective as bringing power back through all three rings.
Requirement: Keep connector geometry and route logic in Development.
Content:
```text
AWAKEN THE ORRERY

Carry power from the Generator through all three rings.
Keep every earlier ring alive as you move forward.
```
''',
    'Ring Progress Display': r'''#### Ring Progress Display
Flow: 02 — Extend to Ring 2
For: Show which Orrery rings currently have power.
Requirement: Use simple in-world state words and update from actual connectivity.
Content:
```text
RING 1 · LIVE / DARK
RING 2 · LIVE / DARK
RING 3 · LIVE / DARK
```
''',
    'First Sabotage Message': r'''#### First Sabotage Message
Flow: 03 — Route Swap Sabotage
For: Tell the player Gremlin blocked the old path and opened another.
Requirement: Do not explain the route solution or implementation state.
Content:
```text
GREMLIN'S WORK

Your old path is blocked.
Another way has opened.

Find it and bring Ring Two back to life.
```
''',
    '50% Sabotage Message': r'''#### First Rollback Message
Flow: 04 — 50% Rollback
For: Tell the player Ring One has gone dark after Gremlin's sabotage.
Requirement: Do not expose percentages, rotator counts, positions, or internal connection names.
Content:
```text
RING ONE IS DARK

Gremlin has disturbed the first line.
Bring the power back.
```
''',
    '80% Sabotage Message': r'''#### Second Rollback Message
Flow: 05 — 80% Rollback
For: Tell the player Ring Two has gone dark after Gremlin strikes again.
Requirement: Do not expose percentages, rotator counts, positions, or internal connection names.
Content:
```text
RING TWO IS DARK

He struck again.
Restore the earlier line.
```
''',
    'Completion Message': r'''#### Completion Message
Flow: 02 — Return Home
For: Confirm the restored vault and point the player toward the open gateway.
Requirement: Keep the ending message fully in-world.
Content:
```text
THE CLOCKWORK VAULT IS RESTORED

The gateway is open.
Follow the light home.
```
''',
}

ASSET_FOR = {
    'Custodian Vex': 'Vex’s reusable in-world character asset.',
    'Gremlin': 'Gremlin’s reusable in-world sabotage character.',
    'Custodian Key': 'The story key used to open the first seal.',
    'Partial Door Target Display': 'Show the one answer the door still remembers.',
    'Pillar Readability': 'Make Left, Middle, and Right distinct without debug-style labels.',
    'Pillar Interaction Feedback': 'Show each control change through the pillar lamp.',
    'Resonance Engine Restoration': 'Show the Resonance Engine returning to life.',
    'Level 3 Time-Challenge Cue': 'Gremlin-flavored warning sound as the final crossing turns dangerous.',
    'Level Retry Reset': 'Show the current crossing reforming for another attempt.',
    'Gremlin Route-Closed Event': 'Show Gremlin taking the failed path away.',
    'Echo Pebble': 'The throwable tool used against Warden sensors and loose stones.',
    'Wall Laser Sensor': 'The wall-mounted Warden target the Echo Pebble can disturb.',
    'Laser Blocker Stone': 'A loose stone that can fall into a laser beam.',
    'Swinging Axe Trap': 'The ceiling hazard the player must time past.',
    'Trap Readability': 'Make each Warden hazard readable from appearance and motion.',
    'Trap Hit Feedback': 'Make laser, floor, and axe hits feel distinct.',
    'Checkpoint Recovery': 'Bring the player back safely after the Warden Halls defeat them.',
    'Power Generator': 'The visible source feeding power into the Orrery network.',
    '90-Degree Rotator Junction': 'The reusable junction the player turns to redirect power.',
    'Orrery Ring': 'The three visible milestones the player brings back to life.',
    'Ring 2 Route-Swap Sabotage': 'Show Gremlin blocking the old route and opening another.',
    '50% Rotator Sabotage': 'Show Gremlin disturbing the earlier line to Ring One.',
    '80% Rotator Sabotage': 'Show Gremlin disturbing the earlier line to Ring Two.',
    'Great Orrery Restoration': 'Show all three rings waking the Great Orrery.',
    'Clockwork Wayfinder': 'The cosmetic reward presented at the end of the story.',
    'Vault Awakening and Exit Reveal': 'Deliver the final vault-awakening and gateway-opening payoff.',
}


def replace_entry(text: str, title: str, replacement: str) -> str:
    pattern = re.compile(r'^#### ' + re.escape(title) + r'\n.*?(?=^#### |^### |^## |\Z)', re.M | re.S)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise SystemExit(f'expected one asset entry for {title}, found {len(matches)}')
    return pattern.sub(replacement.rstrip() + '\n\n', text, count=1)


def patch_flow_for(text: str) -> str:
    current_section = None
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith('## '):
            current_section = line[3:].strip()
        elif line.startswith('### Gameplay Flow '):
            flow = line[len('### Gameplay Flow '):].strip()
            value = FLOW_FOR.get(current_section, {}).get(flow)
            if value:
                if i + 1 >= len(lines) or not lines[i + 1].startswith('For:'):
                    raise SystemExit(f'missing For directly after flow {current_section} / {flow}')
                lines[i + 1] = 'For: ' + value
    return '\n'.join(lines) + '\n'


def patch_asset_for(text: str) -> str:
    lines = text.splitlines()
    current_title = None
    for i, line in enumerate(lines):
        if line.startswith('#### '):
            current_title = line[5:].strip()
        elif current_title and line.startswith('For:') and current_title in ASSET_FOR:
            lines[i] = 'For: ' + ASSET_FOR[current_title]
            current_title = None
    return '\n'.join(lines) + '\n'


def patch_assets() -> None:
    text = ASSET.read_text(encoding='utf-8')
    for title, replacement in ENTRY_REPLACEMENTS.items():
        text = replace_entry(text, title, replacement)
    text = patch_flow_for(text)
    text = patch_asset_for(text)
    # Remove player-facing technical terms from exact Content blocks.
    forbidden = ['BUILD HERE', 'LEVEL 1 · EASY', 'LEVEL 2 · MEDIUM', '50% of your chosen route', 'Return to Checkpoint 3', 'Two rotators were turned.', 'Three rotators were turned.']
    for token in forbidden:
        if token in text:
            raise SystemExit(f'player-facing technical copy remains: {token}')
    ASSET.write_text(text, encoding='utf-8')


def patch_renderer() -> None:
    text = RENDERER.read_text(encoding='utf-8')
    old = '''def _category_label(category: str) -> str:\n    return {\n        "3D Models": "Model",\n        "UI & Information": "UI",\n        "Audio": "Audio",\n        "Visual Effects & Presentation": "VFX",\n    }.get(category, category)\n'''
    new = '''def _category_label(category: str, title: str = "") -> str:\n    overrides = {\n        "Custodian Vex": "MODEL / ANIMATION",\n        "Gremlin": "MODEL / ANIMATION",\n        "Wall Laser Sensor": "MODEL / VFX",\n        "Laser Blocker Stone": "MODEL / ANIMATION",\n        "Swinging Axe Trap": "MODEL / ANIMATION",\n        "Power Generator": "MODEL / VFX",\n        "90-Degree Rotator Junction": "MODEL / ANIMATION",\n        "Orrery Ring": "MODEL / ANIMATION",\n        "Repair Markers": "PRESENTATION",\n    }\n    if title in overrides:\n        return overrides[title]\n    return {\n        "3D Models": "MODEL",\n        "UI & Information": "UI / TEXT",\n        "Audio": "SFX",\n        "Visual Effects & Presentation": "PRESENTATION",\n    }.get(category, category.upper())\n'''
    if old not in text:
        raise SystemExit('category label block not found')
    text = text.replace(old, new, 1)
    text = text.replace('esc(_category_label(entry.category))', 'esc(_category_label(entry.category, entry.title))')
    text = text.replace(
        'Assets and copy-ready content for this gameplay section. See 03 Development for mechanic and implementation details.',
        'Only production-ready assets and in-game copy are shown here. See 03 Development for mechanics.'
    )
    text = text.replace('.pa-assets{display:grid;gap:8px}', '.pa-assets{display:grid;gap:14px}')
    text = text.replace(
        '.pa-asset-card,.pa-voice-inline{padding:12px 13px;border:1px solid #d8e1e5;border-radius:4px;background:var(--paper);break-inside:avoid}',
        '.pa-asset-card,.pa-voice-inline{overflow:hidden;padding:0;border:1px solid #cbd8de;border-left:4px solid var(--blue);border-radius:5px;background:var(--paper);break-inside:avoid}.pa-voice-inline{border-left-color:var(--amber)}'
    )
    text = text.replace(
        '.pa-asset-head{display:flex;align-items:center;gap:8px}',
        '.pa-asset-head{display:flex;align-items:center;gap:8px;padding:10px 12px;border-bottom:1px solid var(--line);background:var(--soft)}'
    )
    text = text.replace(
        '.pa-for{margin:6px 0 0;color:#52616a;font-size:.75rem;line-height:1.45}',
        '.pa-for{margin:0;padding:8px 12px;color:#52616a;font-size:.75rem;line-height:1.45}'
    )
    text = text.replace('.pa-copy-block{margin-top:9px}', '.pa-copy-block{padding:0 12px 12px}')
    text = text.replace('.pa-voice-inline>.pa-type-badge{margin-bottom:0}', '.pa-voice-inline>.pa-type-badge{margin:10px 12px 0}')
    text = text.replace('.pa-voice-inline .voice-script-card{margin-top:7px;border:0;border-top:1px solid var(--line);border-radius:0}', '.pa-voice-inline .voice-script-card{margin:0 12px 12px;border:0;border-top:1px solid var(--line);border-radius:0}')
    RENDERER.write_text(text, encoding='utf-8')


def patch_authority() -> None:
    source = SOURCE.read_text(encoding='utf-8')
    if 'SRC-013' not in source:
        source += '''\n  - id: SRC-013\n    type: instruction\n    role: authoritative\n    status: current\n    origin: user\n    inspection: full\n    summary: User requires section 04 Production Assets to reach the same clarity and quality as PRD sections 01-03. Voice must primarily serve story, character, atmosphere, reaction, or light in-world hints rather than reading gameplay specifications aloud. Player-facing UI/Text must be pure in-game communication with no internal development terminology, implementation counts, reset/checkpoint language, or debug labels unless genuinely needed by the player. Asset type labels must be literal and unambiguous (MODEL, ANIMATION, VFX, SFX, UI / TEXT, VOICE, PRESENTATION), and technical gameplay rules remain in Development.\n'''
        SOURCE.write_text(source, encoding='utf-8')

    req = REQ.read_text(encoding='utf-8')
    req = re.sub(
        r'  - id: REQ-016\n    area: voice-production\n    statement: .*?\n    provenance:',
        '  - id: REQ-016\n    area: voice-production\n    statement: Gremlin is an additional speaking character for authored sabotage and challenge moments, including the Broken Gallery final crossing and Objective 4. Custodian Vex remains the primary narrative guide. Voice exists for story, character, atmosphere, reaction, and light in-world hints; it must not become a spoken copy of Development mechanics. Gremlin dialogue adds personality and sabotage acknowledgement without revealing solutions or internal implementation state.\n    provenance:',
        req,
        count=1,
        flags=re.S,
    )
    if 'REQ-019' not in req:
        req += '''\n\n  - id: REQ-019\n    area: production-assets\n    statement: Section 04 Production Assets must match the clarity of PRD sections 01-03 while remaining a concise production companion rather than a second Development specification. Player-facing UI/Text contains only real in-game communication; Voice serves story/character/atmosphere/reaction or light in-world hints; internal development terminology, thresholds, reset/checkpoint language, implementation counts, debug labels, and engineering explanations stay in Development unless genuinely required by the player. Asset badges use literal production types so MODEL, ANIMATION, VFX, SFX, UI / TEXT, VOICE, and PRESENTATION cannot be confused.\n    provenance: [SRC-013]\n    evidence_status: approved\n    recovery_class: none\n    approval_status: not_required\n    impact: high\n'''
    REQ.write_text(req, encoding='utf-8')


def main() -> None:
    VOICE_REQ.write_text(VOICE_REQUIREMENTS, encoding='utf-8')
    VOICE_PROD.write_text(VOICE_PRODUCTION, encoding='utf-8')
    patch_assets()
    patch_renderer()
    patch_authority()
    print('04 Production Assets content rebuild prepared')

if __name__ == '__main__':
    main()
