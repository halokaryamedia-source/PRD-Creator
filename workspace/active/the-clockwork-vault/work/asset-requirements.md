# Production Asset Requirements

## Global / Shared Assets

### Gameplay Flow 01 — Shared Characters
For: Reusable Vex and Gremlin character assets used across the story.
Trigger: Referenced whenever Custodian Vex or Gremlin appears in a gameplay flow.
Player Experience: Vex reads as the consistent guide while Gremlin reads as the recognizable mischievous saboteur.
Uses: Custodian Vex; Gremlin
Done When:
- Vex supports the current idle, speaking, alert, guidance, and completion states used by the approved Voice lines.
- Gremlin supports appear, sabotage, taunt, and outsmarted/defeat reaction states.
- Both characters stay visually and audibly distinct and can be reused by every referenced flow without duplicate implementations.


### 3D Models

#### Custodian Vex
Flow: 01 — Shared Characters
Group: 01 — Shared Characters
Used: Throughout the full adventure.
For: Vex’s reusable in-world character asset.
Requirement: Create or reuse one Clockwork-compatible Custodian Vex NPC presentation for all required story, briefing, warning, reminder, and ending moments. Vex must remain visually recognizable across the complete journey and support readable idle, speaking, pointing/highlight, alert, and completion-reaction states without changing gameplay rules.
Usage: Shared across the Antechamber, Objectives 1-4, and the ending wherever canonical Voice Production is triggered.

#### Gremlin
Flow: 01 — Shared Characters
Group: 01 — Shared Characters
Used: Broken Gallery final crossing and Objective 4 sabotage moments.
For: Gremlin’s reusable in-world sabotage character.
Requirement: Create one small Clockwork Gremlin character used for authored sabotage moments. It needs a readable mischievous traversal/arrival state and a clear sabotage action that can be synchronized with route blocking, rotator changes, and the relevant warning presentation. It does not require navigation AI; authored movement is sufficient.
Usage: Used for the Objective 2 final time-challenge framing and the Objective 4 sabotage sequences.

## The Antechamber

### Gameplay Flow 01 — Arrival & Briefing
For: Opening story and the Custodian Key reveal.
Trigger: The assigned player enters the protected Antechamber and Custodian Vex activates for the first time.
Player Experience: The player understands why the vault is sealed, what the Great Orrery is, and sees the Custodian Key as the first actionable object.
Uses: Custodian Vex; Custodian Key
Done When:
- Vex opening briefing plays once for the current session.
- The Custodian Key is clearly visible and available after the briefing.
- The player understands the key starts the restoration route and is not the exit key.

### Gameplay Flow 02 — Take Key & Open Seal
For: Key handoff and opening of the Resonance Engine.
Trigger: The opening briefing is complete and the Resonance Engine seal is still closed.
Player Experience: The player takes the key, receives only the minimum reminder if needed, uses the key on the marked seal, and sees the first objective route open.
Uses: Custodian Vex; Custodian Key; Resonance Engine seal
Done When:
- The exact key prompt remains readable until valid seal activation.
- Valid Custodian Key use opens the Resonance Engine seal once and gives clear feedback.
- The handoff into Objective 1 is readable and does not become a separate puzzle.


### 3D Models

#### Custodian Key
Flow: 01 — Arrival & Briefing
Group: 01 — Opening Story
Used: Antechamber opening and the first seal.
For: The story key used to open the first seal.
Requirement: Create one clearly readable key item for the opening progression. It needs available/picked-up/accepted states and must visually belong to the Clockwork Vault rather than resemble an ordinary reward item.
Usage: Presented on the Antechamber pedestal and accepted by the Resonance Engine seal.

### UI & Information

#### Custodian Key Prompt
Flow: 02 — Take Key & Open Seal
Group: 02 — Open First Seal
Used: After the opening briefing, until the first seal opens.
For: Point the player toward the first seal.
Requirement: Keep the prompt short and fully in-world.
Content:
```text
TAKE THE CUSTODIAN KEY
The first seal is waiting.
```

### Visual Effects & Presentation

#### Resonance Engine Seal Opening
Flow: 02 — Take Key & Open Seal
Group: 02 — Open First Seal
Used: When the Custodian Key is accepted by the first seal.
For: Show the first seal accepting the key and opening the Resonance Engine entrance.
Requirement: Use one short presentation sequence: the seal responds, the door unlocks, and the route ahead becomes obvious. Any sound is a separate SFX asset if produced.
Usage: Plays once when the Custodian Key is accepted.

## The Resonance Engine

### Gameplay Flow 01 — The Door Remembers
For: Introduce the incomplete answer and the mystery of the chamber.
Trigger: The Resonance Engine seal opens and the player gains control inside the reset chamber.
Player Experience: The player immediately sees the basic task and the intentionally incomplete target: Middle is Brown while Left, Right, and Pulse remain unknown.
Uses: Custodian Vex; Objective 1 Instruction Panel; Partial Door Target Display
Done When:
- The instruction text is readable and does not reveal the hidden Left/Right colors, pulse location, or lever solutions.
- The door display shows Middle = Brown and keeps the other target values unknown.
- Vex briefing matches the same information and does not contradict the display.

### Gameplay Flow 02 — Search the Chamber
For: Clues left behind by the vault’s former keepers.
Trigger: Objective 1 is active and the twelve scattered books are available around the chamber.
Player Experience: The player searches books in any order, may find useful clues early by luck, and gradually narrows the missing target information without needing every book.
Uses: Scattered Clue Book Set
Done When:
- All twelve approved books use the exact current text.
- The set remains 2 rule books + 8 useful clues + 2 harmless decoys with no forced reading order.
- Decoys contain no false puzzle facts and completion never requires all twelve books.

### Gameplay Flow 03 — Tune the Pillars
For: Readable pillar feedback while the player experiments.
Trigger: The player changes a pillar lever or pressure-plate state while Objective 1 is active.
Player Experience: The player learns each pillar by experimentation: lever combinations change color and the plate changes only steady versus pulse.
Uses: Left / Middle / Right pillar labels; pillar lamps; upper/lower levers; pressure plates
Done When:
- LEFT, MIDDLE, and RIGHT identities remain clear from the player position.
- Every lever change produces immediate deterministic lamp-color feedback for that pillar.
- Pressure plates change only steady/pulse state and never change the selected color.

### Gameplay Flow 04 — Engine Restored
For: Resonance Engine restoration and the route opening.
Trigger: Left = Orange + pulse, Middle = Brown + steady, and Right = Purple + steady are all valid at the same time.
Player Experience: The three pillars visibly synchronize, the Resonance Engine returns to operation, and attention moves to the newly opened Broken Gallery route.
Uses: Resonance Engine restoration presentation; pillar completion feedback
Done When:
- Completion validates the full simultaneous final state rather than a partial match.
- The completion response plays once and clearly confirms success.
- The Broken Gallery route opens and Objective 1 temporary state is ready for the next reset.


### UI & Information

#### Objective 1 Instruction Panel
Flow: 01 — The Door Remembers
Group: 01 — Chamber Guidance
Used: When the player enters the Resonance Engine.
For: Hint that the missing answer is still somewhere in the chamber.
Requirement: Keep the opening prompt short, mysterious, and non-technical.
Content:
```text
RESTORE THE THREE PILLARS

The door remembers only part of the answer.

Everything else you need is somewhere in this chamber.
Look carefully, then bring the Engine back to life.
```

#### Partial Door Target Display
Flow: 01 — The Door Remembers
Group: 01 — Chamber Guidance
Used: Throughout Objective 1.
For: Show the one answer the door still remembers.
Requirement: Create one player-readable target display near the exit that intentionally reveals only the middle pillar color. It must not reveal the left color, right color, pulse location, or any lever combination. The unknown values remain visible as missing information until the player solves the puzzle through the books and machine experimentation.
Content:
```text
LEFT      MIDDLE      RIGHT
 ?         BROWN        ?

PULSE: ?
```
Usage: Visible throughout active Objective 1 solving. It may switch to a solved/confirmed presentation only after the complete hidden target state is matched.

#### Scattered Clue Book Set
Flow: 02 — Search the Chamber
Group: 02 — Clue Set
Used: Throughout the chamber search.
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

### Visual Effects & Presentation

#### Pillar Lamp Feedback
Flow: 03 — Tune the Pillars
Group: 03 — Pillar Interaction
Used: Whenever the player tests a pillar control.
For: Show each control change through the pillar lamp.
Requirement: Every valid lever change must produce immediate readable lamp feedback on its own pillar so the player can discover the lever-to-color behavior through experimentation. Every pressure-plate interaction must visibly switch only that pillar between steady and pulsing without changing its selected color. When the hidden final target is matched—Left Orange pulsing, Middle Brown steady, Right Purple steady—run one concise confirmation response before opening the next route.
Usage: Active throughout Objective 1 and reset completely for the next run.

#### Resonance Engine Restoration
Flow: 04 — Engine Restored
Group: 04 — Completion
Used: When the complete pillar state is solved.
For: Show the Resonance Engine returning to life.
Requirement: Create one short completion presentation that visually confirms all three pillars have synchronized and the Engine has returned to operation, then directs attention toward the newly opened Broken Gallery route.
Usage: Runs once after valid Objective 1 completion.

## The Broken Gallery

### Gameplay Flow 01 — Enter the Gallery
For: Introduce the collapsed Gallery and the supplies left behind.
Trigger: The player enters Broken Gallery Level 1 with checkpoint barrels and the three route choices available.
Player Experience: The player learns the repeated loop: search barrels, repair only marked gaps, reach the checkpoint, and retry only the current level on failure.
Uses: Custodian Vex; Broken Gallery Entrance Message; Repair Gap Markers
Done When:
- The route-loop instruction text is readable without revealing a viable route.
- Legal placement markers are clearly different from ordinary environment blocks.
- Vex briefing communicates limited-resource planning and local retry without introducing old mechanics.

### Gameplay Flow 02 — First Crossing
For: First crossing through the Broken Gallery.
Trigger: Checkpoint 1 is active and Level 1 resources/routes are reset.
Player Experience: The player reads three routes, uses the 12-block allocation, and must avoid wasting supplies on the non-viable route.
Uses: First Crossing Message; checkpoint barrels; Repair Gap Markers
Done When:
- The Level 1 brief uses the exact approved text and does not reveal which two routes work.
- The authored allocation is 12 blocks and only marked placements are accepted.
- Middle and Right remain viable, Left remains non-viable, and successful crossing reaches Checkpoint 2.

### Gameplay Flow 03 — Second Crossing
For: Second, tighter crossing through the Broken Gallery.
Trigger: Checkpoint 2 is active and Level 2 resources/routes are reset.
Player Experience: The player solves a tighter route/resource problem using 20 blocks and 3 ladders while only one route can be completed.
Uses: Second Crossing Message; checkpoint barrels; blocks; ladders; Repair Gap Markers
Done When:
- The Level 2 brief uses the exact approved text without naming the viable route.
- The authored allocation is 20 blocks + 3 ladders and placement remains marker-owned.
- Only the Right route is viable and successful crossing reaches Checkpoint 3.

### Gameplay Flow 04 — Gremlin’s Wager
For: Gremlin’s timed final crossing.
Trigger: Checkpoint 3 is active, all three routes are initially viable, and the timed attempt begins when the player materially commits to a route.
Player Experience: The player chooses a route, hears/sees Gremlin-timed urgency, and must reach at least 50% route progress before the authored threshold.
Uses: Gremlin; Custodian Vex; Gremlin's Wager Message; Level 3 Time-Challenge Cue; route-progress state
Done When:
- The exact Level 3 instruction is readable before/during the attempt without revealing route geometry.
- The warning cue and Vex line clearly mark the timed requirement.
- At least 50% progress before the threshold preserves the chosen route and allows the crossing to continue.

### Gameplay Flow 05 — When a Path Fails
For: Failure feedback when a route gives way.
Trigger: The active level exhausts its resources or configured time, or a Level 3 attempt misses the 50% progress threshold.
Player Experience: The player gets a local reset. Level 1/2 simply retry; Level 3 visibly loses the failed route while another alternative remains.
Uses: Crossing Failure Messages; Level Retry Reset; Gremlin Path Collapse
Done When:
- Temporary blocks/ladders from the failed attempt are removed and the active checkpoint becomes safe/retryable.
- Current-level resources become available again while earlier completed Gallery levels remain complete.
- A failed Level 3 route is visibly unavailable while alternatives remain, and the last remaining route never makes the objective unwinnable before normal timeout.


### UI & Information

#### Broken Gallery Entrance Message
Flow: 01 — Enter the Gallery
Group: 01 — Shared Gallery Assets
Used: When the player first enters the Broken Gallery.
For: Point the player toward the old supplies and the damaged crossings.
Requirement: Keep the Gallery instruction short and in-world.
Content:
```text
THE BROKEN GALLERY

The old stores still hold what you need.
Repair only the marked breaks and find a way across.
```

#### First Crossing Message
Flow: 02 — First Crossing
Group: 02 — First Crossing
Used: At the first Gallery crossing.
For: Frame the first crossing without giving away the route.
Requirement: Keep the message short and avoid system-style difficulty labels.
Content:
```text
FIRST CROSSING

More than one path can still hold.
Choose carefully before you spend your supplies.
```

#### Second Crossing Message
Flow: 03 — Second Crossing
Group: 03 — Second Crossing
Used: At the second Gallery crossing.
For: Frame the tighter second crossing without naming the answer.
Requirement: Keep the message short and in-world.
Content:
```text
SECOND CROSSING

Only one path still holds.
Count what you have before you commit.
```

#### Gremlin's Wager Message
Flow: 04 — Gremlin’s Wager
Group: 04 — Gremlin’s Wager
Used: Before the final Gallery crossing begins.
For: Make Gremlin's final crossing feel dangerous without exposing internal timing language.
Requirement: Use player-facing language; “halfway” is allowed, internal percentages/threshold terminology are not.
Content:
```text
GREMLIN'S WAGER

Pick a path.
Reach halfway before the clock runs out,
or Gremlin will take that route away.
```

#### Crossing Failure Messages
Flow: 05 — When a Path Fails
Group: 05 — Path Failure
Used: After a Gallery crossing fails.
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

#### Repair Gap Markers
Flow: 01 — Enter the Gallery
Group: 01 — Shared Gallery Assets
Used: Across all three Gallery crossings.
For: Make repairable gaps visually distinct without putting debug text into the world.
Requirement: Use an environmental marker treatment for valid repair positions. Do not display debug-style placement text.
Usage: Visible only at authored repair positions.

### Audio

#### Gremlin Wager Cue
Flow: 04 — Gremlin’s Wager
Group: 04 — Gremlin’s Wager
Used: When the final crossing becomes timed.
For: Gremlin-flavored warning sound as the final crossing turns dangerous.
Requirement: Create one independent short warning cue that clearly marks the start of the Level 3 progress deadline. It should read as Gremlin-triggered urgency and remain distinct from normal checkpoint, placement, or route-reset sounds.
Usage: Plays when the Level 3 authored timer begins; Voice Production may play alongside it but is owned separately.

### Visual Effects & Presentation

#### Gremlin Path Collapse
Flow: 05 — When a Path Fails
Group: 05 — Path Failure
Used: When Gremlin takes a failed final path away.
For: Show Gremlin taking the failed path away.
Requirement: Create one Level 3 failure presentation in which the selected failed route changes to a clearly unavailable state, the player returns to Checkpoint 3, and the remaining active routes stay readable. The Gremlin framing and warning cue may be synchronized inside this authored sequence.
Usage: Runs after a Level 3 route misses its required progress threshold while another active route remains.

## The Warden Halls

### Gameplay Flow 01 — Enter the Warden Halls
For: Introduce the Wardens and the Echo Pebble.
Trigger: The Warden Halls activate and the player receives the unlimited Echo Pebble before the first trap-family encounters.
Player Experience: The player understands which hazards accept Echo Pebble interaction and which must instead be avoided or timed.
Uses: Custodian Vex; Echo Pebble; Wall Laser Sensor; Swinging Axe Trap; Floor Trap; Warden Halls Entrance Message
Done When:
- The instruction panel uses the exact approved trap/Pebble rules.
- Wall lasers, floor traps, and swinging axes remain visually distinguishable.
- Nothing implies that floor traps or swinging axes can be disabled with Echo Pebble.

### Gameplay Flow 02 — Echo Pebble
For: Echo Pebble interactions and sensor feedback.
Trigger: The player throws Echo Pebble at a valid wall-laser sensor or authored hanging-stone target.
Player Experience: A valid sensor hit creates a short four-second laser opening; selected hanging stones can instead block the beam, while the three-second throw cooldown remains readable.
Uses: Echo Pebble; Wall Laser Sensor; Laser Blocker Stone; Echo Pebble HUD
Done When:
- Each throw starts the approved 3-second cooldown and the UI returns to READY afterward.
- A valid wall-laser sensor hit disables only that laser for 4 seconds of game-time.
- Only authored hanging-stone targets create the alternate beam-blocking solution; invalid floor/axe targets do not disable anything.

### Gameplay Flow 03 — Warden Hazards
For: Trap-hit and recovery presentation.
Trigger: The player contacts a laser, floor trap, or swinging axe, or gameplay health reaches zero from Warden hazards.
Player Experience: The player receives hazard-specific feedback/effects; zero gameplay health returns them to the current safe checkpoint instead of restarting the full objective.
Uses: Warden Hit Effects; Warden Recovery; active Warden checkpoint
Done When:
- Laser, floor, and axe contacts apply their approved damage/status effects and remain distinguishable.
- Gameplay health reaching zero returns the player to the active Warden checkpoint in a safe recovered state.
- Earlier completed Warden levels remain complete after checkpoint recovery.

### Gameplay Flow 04 — Enter the Workshop
For: Story transition into the Workshop.
Trigger: The player clears the third Warden level and reaches the inner gate.
Player Experience: Vex acknowledges that the Wardens are still serving the vault and directs the player into Gremlin’s Workshop.
Uses: Custodian Vex; inner gate transition
Done When:
- The transition Voice plays once without replaying Pebble instructions.
- The Workshop route becomes the clear next destination.
- No Workshop sabotage is revealed before its authored trigger.


### 3D Models

#### Echo Pebble
Flow: 01 — Enter the Warden Halls
Group: 01 — Core Trap Kit
Used: Throughout the Warden Halls.
For: The throwable tool used against Warden sensors and loose stones.
Requirement: Create one small throwable pebble item, visually derived from a stone/snowball-scale projectile but clearly authored for the Clockwork Vault. It needs held/throw/projectile/valid-hit feedback and must support an unlimited-use loop with a visible 3-second cooldown. Its impact feedback must distinguish a valid wall-laser sensor or hanging-stone target from an invalid floor/axe target.
Usage: Granted for Objective 3 and removed/reset at objective exit.

#### Wall Laser Sensor
Flow: 02 — Echo Pebble
Group: 01 — Core Trap Kit
Used: Across all Warden levels.
For: The wall-mounted Warden target the Echo Pebble can disturb.
Requirement: Create one readable wall-mounted laser sensor/beam assembly with Active and Temporarily Disabled states. The sensor must be an obvious Echo Pebble target; a valid hit disables the beam for the approved 4-second game-time window before normal behavior resumes. Attached activation/deactivation VFX and SFX remain part of this asset.
Usage: Distributed across the three Warden levels.

#### Laser Blocker Stone
Flow: 02 — Echo Pebble
Group: 01 — Core Trap Kit
Used: Selected laser encounters.
For: A loose stone that can fall into a laser beam.
Requirement: Create one authored hanging-stone target for selected laser encounters. A valid Echo Pebble hit must cause the stone to move/drop into the beam path and visibly block the laser, creating a readable alternate solution without changing unrelated traps.
Usage: Used only at authored laser encounters that support the blocker-stone solution.

#### Swinging Axe Trap
Flow: 01 — Enter the Warden Halls
Group: 01 — Core Trap Kit
Used: Across the Warden Halls.
For: The ceiling hazard the player must time past.
Requirement: Create one large double-sided swinging axe trap mounted from the ceiling. It needs a clearly readable left-right swing cycle, safe timing windows, contact/knockback feedback, and a reset state. It must never appear to accept Echo Pebble disable input.
Usage: Distributed across the Warden levels as a timing hazard.

#### Floor Trap
Flow: 01 — Enter the Warden Halls
Group: 01 — Core Trap Kit
Used: Across the Warden Halls.
For: The ground hazard the player must avoid.
Requirement: Create one readable floor-trap treatment with Armed, Triggered, and Reset states. It must stay visually distinct from wall sensors and must never suggest that Echo Pebble can disable it. Exact damage and status effects remain in 03 Development.
Usage: Distributed across the Warden levels as an avoid-only ground hazard.

### UI & Information

#### Warden Halls Entrance Message
Flow: 01 — Enter the Warden Halls
Group: 02 — Player Communication
Used: When the player enters the Warden Halls.
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

#### Echo Pebble HUD
Flow: 02 — Echo Pebble
Group: 02 — Player Communication
Used: While the Echo Pebble is available.
For: Show when the Echo Pebble can be thrown again.
Requirement: Keep the HUD state compact; the exact recharge duration stays in Development.
Content:
```text
ECHO PEBBLE · READY
ECHO PEBBLE · RECHARGING
```

### Visual Effects & Presentation

#### Warden Hit Effects
Flow: 03 — Warden Hazards
Group: 04 — Gameplay Feedback
Used: Whenever a laser, floor trap, or axe hits the player.
For: Make laser, floor, and axe hits feel distinct.
Requirement: Create clear but compact feedback for each approved hazard consequence so the player can identify which trap hit them and understand the resulting temporary impairment. Laser, floor, and axe hits must remain distinguishable while avoiding screen obstruction during active traversal.
Usage: Triggered on valid hazard contact together with the approved damage/status effects.

#### Warden Recovery
Flow: 03 — Warden Hazards
Group: 04 — Gameplay Feedback
Used: When Warden hazards defeat the player.
For: Bring the player back safely after the Warden Halls defeat them.
Requirement: When trap damage reduces gameplay health to zero, present one quick checkpoint recovery that returns the player to the active Warden level without replaying earlier completed levels. Restore player control only after the checkpoint position is safe.
Usage: Runs on Objective 3 hazard defeat only.

## The Gremlin's Workshop

### Gameplay Flow 01 — Wake Ring One
For: Introduce the Orrery power network and the first ring.
Trigger: The player enters the Workshop and the unsabotaged L-rotator network becomes interactive.
Player Experience: The player learns that power begins at the Generator, each rotator is an L connection, and one continuous route must reach Ring 1.
Uses: Custodian Vex; Power Generator; 90-Degree Rotator Junction; Orrery Ring; Workshop Entrance Message; Orrery Ring Status
Done When:
- The instruction text explains Generator → Ring 1 → Ring 2 → Ring 3 without exposing the authored route solution.
- Each rotator has four readable orientations and powered/unpowered state is visually clear.
- Ring 1 becomes powered only when a continuous valid path exists from the Generator.

### Gameplay Flow 02 — Wake Ring Two
For: Show the restored current reaching Ring Two.
Trigger: Ring 1 is powered and the player continues the same network toward Ring 2.
Player Experience: The player extends the existing live route while keeping Ring 1 connected; the status display reflects actual connectivity.
Uses: Power Generator; 90-Degree Rotator Junction; Orrery Rings; Orrery Ring Status
Done When:
- Ring 2 becomes powered only while Generator → Ring 1 → Ring 2 is continuously connected.
- The Orrery Ring Status immediately reflects any real loss of power rather than milestone history.
- The post-Ring-2 route-swap trigger becomes eligible only after the approved stable state.

### Gameplay Flow 03 — Gremlin Changes the Path
For: Gremlin blocks the old route and forces a new path.
Trigger: About 20 seconds after Ring 1 and Ring 2 are continuously connected.
Player Experience: Gremlin deliberately blocks the route the player just used, a previously blocked alternate path opens, Ring 2 loses power, Gremlin taunts, then Vex gives recovery guidance.
Uses: Gremlin; Custodian Vex; Power Generator; 90-Degree Rotator Junction; Orrery Ring Status; Route Swap Message
Done When:
- The route-swap sabotage triggers once for the session.
- The old route becomes clearly unavailable, the authored alternate opens, and connectivity/power is recalculated immediately.
- The exact sabotage text plus Gremlin and Vex lines play in the intended order without revealing the solution path.
- The player can recover using the same L-rotator rule.

### Gameplay Flow 04 — First Rollback
For: Gremlin disrupts the first powered line.
Trigger: Validated Ring 2 → Ring 3 route progress reaches 50% for the first time.
Player Experience: Gremlin rotates exactly two previously correct Generator → Ring 1 rotators, earlier power drops, Gremlin gloats, and Vex directs the player back to repair the link.
Uses: Gremlin; Custodian Vex; 90-Degree Rotator Junction; Orrery Ring Status; Ring One Power Loss Message
Done When:
- Exactly two approved Generator → Ring 1 rotators change orientation once.
- Power loss propagates immediately and the exact 50% message identifies the affected section without exposing rotator positions.
- Gremlin taunt and Vex repair guidance play without changing the learned routing rule.

### Gameplay Flow 05 — Second Rollback
For: Gremlin disrupts the second powered line.
Trigger: Validated Ring 2 → Ring 3 route progress reaches 80% for the first time.
Player Experience: Gremlin rotates exactly three previously correct Ring 1 → Ring 2 rotators, removes earlier power again, and the player must repair that section before finishing.
Uses: Gremlin; Custodian Vex; 90-Degree Rotator Junction; Orrery Ring Status; Ring Two Power Loss Message
Done When:
- Exactly three approved Ring 1 → Ring 2 rotators change orientation once.
- The exact 80% message and visible power state make the broken earlier section clear.
- Gremlin and Vex lines play in order and the player can repair with the same L-rotator rule.

### Gameplay Flow 06 — Wake the Great Orrery
For: Final restoration of the Great Orrery.
Trigger: Generator, Ring 1, Ring 2, and Ring 3 are all continuously connected after all authored sabotage events.
Player Experience: Gremlin realizes the player has outsmarted the sabotage, all rings synchronize, the Great Orrery returns to life, puzzle input closes, and the exit begins opening.
Uses: Gremlin; Power Generator; Orrery Rings; Great Orrery Restoration
Done When:
- Completion requires one continuous final network across Generator and all three rings.
- Gremlin’s outsmarted reaction plays once and does not replace Vex’s later ending speech.
- The final restoration presentation clearly confirms success and begins the ending/exit handoff.


### 3D Models

#### Power Generator
Flow: 01 — Wake Ring One
Group: 01 — Core Network Kit
Used: Throughout Objective 4.
For: The visible source feeding power into the Orrery network.
Requirement: Create one central power-source machine with clearly different Offline, Live, and Power-Interrupted feedback. The output direction into the routing network must remain visually readable from the puzzle area. Attached startup/interruption SFX and energy VFX remain part of this asset.
Usage: Source of the Objective 4 continuous power network.

#### 90-Degree Rotator Junction
Flow: 01 — Wake Ring One
Group: 01 — Core Network Kit
Used: Throughout Objective 4.
For: The reusable junction the player turns to redirect power.
Requirement: Create one reusable L-shaped power junction that rotates in 90-degree steps and connects exactly two orthogonal directions. It needs four readable orientations plus Powered and Unpowered visual states. Interaction must make the route direction legible without exposing the route solution.
Usage: Repeated at authored Objective 4 junction locations.

#### Orrery Ring
Flow: 02 — Wake Ring Two
Group: 01 — Core Network Kit
Used: Throughout Objective 4.
For: The three visible milestones the player brings back to life.
Requirement: Create one reusable ring mechanism used as Ring 1, Ring 2, and Ring 3 with clearly readable Inactive and Powered states. The three instances must remain distinguishable by position/label while sharing one visual grammar. The final state must support all three rings operating together as the Great Orrery restoration payoff.
Usage: Sequential milestones in Objective 4 and the ending transition.

### UI & Information

#### Workshop Entrance Message
Flow: 01 — Wake Ring One
Group: 02 — Workshop Intro
Used: When the player enters the Workshop.
For: Frame the final objective as bringing power back through all three rings.
Requirement: Keep connector geometry and route logic in Development.
Content:
```text
AWAKEN THE ORRERY

Carry power from the Generator through all three rings.
Keep every earlier ring alive as you move forward.
```

#### Orrery Ring Status
Flow: 02 — Wake Ring Two
Group: 01 — Core Network Kit
Used: Throughout Objective 4.
For: Show which Orrery rings currently have power.
Requirement: Use simple in-world state words and update from actual connectivity.
Content:
```text
RING 1 · LIVE / DARK
RING 2 · LIVE / DARK
RING 3 · LIVE / DARK
```

#### Route Swap Message
Flow: 03 — Gremlin Changes the Path
Group: 03 — Gremlin Route Swap
Used: When Gremlin blocks the old route after Ring Two.
For: Tell the player Gremlin blocked the old path and opened another.
Requirement: Do not explain the route solution or implementation state.
Content:
```text
GREMLIN'S WORK

Your old path is blocked.
Another way has opened.

Find it and bring Ring Two back to life.
```

#### First Rollback Message
Flow: 04 — First Rollback
Group: 04 — First Sabotage
Used: When Ring One loses power from Gremlin’s first rollback.
For: Tell the player Ring One has gone dark after Gremlin's sabotage.
Requirement: Do not expose percentages, rotator counts, positions, or internal connection names.
Content:
```text
RING ONE IS DARK

Gremlin has disturbed the first line.
Bring the power back.
```

#### Second Rollback Message
Flow: 05 — Second Rollback
Group: 05 — Second Sabotage
Used: When Ring Two loses power from Gremlin’s second rollback.
For: Tell the player Ring Two has gone dark after Gremlin strikes again.
Requirement: Do not expose percentages, rotator counts, positions, or internal connection names.
Content:
```text
RING TWO IS DARK

He struck again.
Restore the earlier line.
```

### Visual Effects & Presentation

#### Gremlin Route Swap
Flow: 03 — Gremlin Changes the Path
Group: 03 — Gremlin Route Swap
Used: When the route-swap sabotage occurs.
For: Show Gremlin blocking the old route and opening another.
Requirement: About 20 seconds after Ring 1 and Ring 2 are connected, run one authored Gremlin sequence that makes the previously active route become visibly blocked, makes the previously blocked alternate path visibly available, removes power where connectivity is broken, and then returns control for rerouting. The change must be understandable without exposing route coordinates or implementation labels.
Usage: Runs once per Objective 4 session after the approved Ring 2 condition.

#### First Rollback Sabotage
Flow: 04 — First Rollback
Group: 04 — First Sabotage
Used: At the first authored rollback event.
For: Show Gremlin disturbing the earlier line to Ring One.
Requirement: At the approved 50% Ring 2-to-Ring 3 progress trigger, run one short Gremlin disruption in which exactly two already-correct rotators on the Generator-to-Ring-1 connection visibly turn out of alignment. Power loss must propagate to the affected ring states before normal input resumes.
Usage: Runs once per Objective 4 session.

#### Second Rollback Sabotage
Flow: 05 — Second Rollback
Group: 05 — Second Sabotage
Used: At the second authored rollback event.
For: Show Gremlin disturbing the earlier line to Ring Two.
Requirement: At the approved 80% Ring 2-to-Ring 3 progress trigger, run one short Gremlin disruption in which exactly three already-correct rotators on the Ring-1-to-Ring-2 connection visibly turn out of alignment. The player must see that an earlier completed section has broken before normal input resumes.
Usage: Runs once per Objective 4 session.

#### Great Orrery Restoration
Flow: 06 — Wake the Great Orrery
Group: 06 — Final Restoration
Used: When the full power network is restored.
For: Show all three rings waking the Great Orrery.
Requirement: When Generator, Ring 1, Ring 2, and Ring 3 are continuously connected, create one strong final restoration presentation: all three rings synchronize, power visibly reaches the Great Orrery, puzzle input closes, and the Clockwork exit begins opening. Keep the transition compatible with the existing ending sequence rather than creating a fifth objective.
Usage: Runs once on valid Objective 4 completion.

## Vault Restored

### Gameplay Flow 01 — The Vault Awakens
For: Final restoration payoff and the Clockwork Wayfinder reward.
Trigger: The Great Orrery restoration callbacks complete and the closing scene reaches Vex recognition.
Player Experience: Vex acknowledges what the player restored, the gateway is open, and the Clockwork Wayfinder reward is presented after the completion record is secured.
Uses: Custodian Vex; Clockwork Wayfinder; Vault Restored Message; Great Orrery / gateway presentation
Done When:
- The completion message and Vex line use the exact approved wording without exposing platform scoring.
- The Clockwork Wayfinder is presented/granted exactly once after the completion state is secured.
- The reopened gateway is clearly visible as the next action.

### Gameplay Flow 02 — The Way Home
For: Farewell and the open gateway home.
Trigger: Session result and reward state are secured and the safe return route is open.
Player Experience: Vex gives one concise farewell/navigation cue and the player follows the reopened route back to the holding area while lane cleanup begins safely.
Uses: Custodian Vex; Vault Awakening Sequence; safe return route
Done When:
- The exact safe-return Voice cue plays without repeating the completion speech.
- The return route is obvious and no new gameplay task is introduced.
- Lane reset/cleanup does not invalidate the player’s safe return and prepares the lane for reuse.


### 3D Models

#### Clockwork Wayfinder
Flow: 01 — The Vault Awakens
Group: 01 — Finale
Used: During the final reward reveal.
For: The cosmetic reward presented at the end of the story.
Requirement: Create one cosmetic completion reward object with a distinct Clockwork-Vault silhouette and a clear reward-reveal presentation. It does not provide new gameplay power and must support one-time grant/readability in the ending scene.
Usage: Presented after the Great Orrery restoration and granted exactly once through the existing ending flow.

### UI & Information

#### Vault Restored Message
Flow: 02 — The Way Home
Group: 01 — Finale
Used: When the restored gateway opens.
For: Confirm the restored vault and point the player toward the open gateway.
Requirement: Keep the ending message fully in-world.
Content:
```text
THE CLOCKWORK VAULT IS RESTORED

The gateway is open.
Follow the light home.
```

### Visual Effects & Presentation

#### Vault Awakening Sequence
Flow: 01 — The Vault Awakens
Group: 01 — Finale
Used: Immediately after the Great Orrery is restored.
For: Deliver the final vault-awakening and gateway-opening payoff.
Requirement: Create one coordinated closing presentation that carries restored power from the Great Orrery into the surrounding vault, reveals the reopened exit, frames Vex's closing moment and Clockwork Wayfinder reward, then hands control to the safe return route. This sequence must remain reset-owned and must not introduce another challenge.
Usage: Runs after Objective 4 completion and before the player returns to the holding area.
