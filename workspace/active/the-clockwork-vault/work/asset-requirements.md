# Production Asset Requirements

## Global / Shared Assets

### Gameplay Flow 01 — Shared Characters
For: Shared character assets used whenever Vex or Gremlin appears.
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
For: Main guide NPC for briefings, warnings, guidance, and the ending.
Requirement: Create or reuse one Clockwork-compatible Custodian Vex NPC presentation for all required story, briefing, warning, reminder, and ending moments. Vex must remain visually recognizable across the complete journey and support readable idle, speaking, pointing/highlight, alert, and completion-reaction states without changing gameplay rules.
Usage: Shared across the Antechamber, Objectives 1-4, and the ending wherever canonical Voice Production is triggered.

#### Gremlin
Flow: 01 — Shared Characters
For: Mischievous sabotage character used in authored disruption moments.
Requirement: Create one small Clockwork Gremlin character used for authored sabotage moments. It needs a readable mischievous traversal/arrival state and a clear sabotage action that can be synchronized with route blocking, rotator changes, and the relevant warning presentation. It does not require navigation AI; authored movement is sufficient.
Usage: Used for the Objective 2 final time-challenge framing and the Objective 4 sabotage sequences.

## The Antechamber

### Gameplay Flow 01 — Arrival & Briefing
For: Opening character and key assets before the first objective starts.
Trigger: The assigned player enters the protected Antechamber and Custodian Vex activates for the first time.
Player Experience: The player understands why the vault is sealed, what the Great Orrery is, and sees the Custodian Key as the first actionable object.
Uses: Custodian Vex; Custodian Key
Done When:
- Vex opening briefing plays once for the current session.
- The Custodian Key is clearly visible and available after the briefing.
- The player understands the key starts the restoration route and is not the exit key.

### Gameplay Flow 02 — Take Key & Open Seal
For: Key prompt, reminder, and seal-opening presentation.
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
For: Opening progression item used to unlock the Resonance Engine seal.
Requirement: Create one clearly readable key item for the opening progression. It needs available/picked-up/accepted states and must visually belong to the Clockwork Vault rather than resemble an ordinary reward item.
Usage: Presented on the Antechamber pedestal and accepted by the Resonance Engine seal.

### UI & Information

#### First Objective Prompt
Flow: 02 — Take Key & Open Seal
For: Tell the player to take the Custodian Key and use it on the first seal.
Requirement: Create one concise player-facing prompt that appears after the opening briefing and remains available until the first seal is opened.
Content:
```text
TAKE THE CUSTODIAN KEY
Use it on the marked Resonance Engine seal.
```

### Visual Effects & Presentation

#### First Seal Activation
Flow: 02 — Take Key & Open Seal
For: Make successful key use and the Objective 1 entrance opening unmistakable.
Requirement: Create one short authored activation presentation for valid Custodian Key use: the seal acknowledges the key, the Objective 1 door visibly unlocks, and the route into the Resonance Engine becomes unmistakable. Keep the sequence short enough that it functions as a handoff rather than a cutscene.
Usage: Runs once after valid Antechamber completion.

## The Resonance Engine

### Gameplay Flow 01 — Read Partial Target
For: Start the puzzle with the partial door answer and a light hint to search the chamber.
Trigger: The Resonance Engine seal opens and the player gains control inside the reset chamber.
Player Experience: The player immediately sees the basic task and the intentionally incomplete target: Middle is Brown while Left, Right, and Pulse remain unknown.
Uses: Custodian Vex; Objective 1 Instruction Panel; Partial Door Target Display
Done When:
- The instruction text is readable and does not reveal the hidden Left/Right colors, pulse location, or lever solutions.
- The door display shows Middle = Brown and keeps the other target values unknown.
- Vex briefing matches the same information and does not contradict the display.

### Gameplay Flow 02 — Search Clues
For: Provide the scattered book clues used to infer the missing target information.
Trigger: Objective 1 is active and the twelve scattered books are available around the chamber.
Player Experience: The player searches books in any order, may find useful clues early by luck, and gradually narrows the missing target information without needing every book.
Uses: Scattered Clue Book Set
Done When:
- All twelve approved books use the exact current text.
- The set remains 2 rule books + 8 useful clues + 2 harmless decoys with no forced reading order.
- Decoys contain no false puzzle facts and completion never requires all twelve books.

### Gameplay Flow 03 — Experiment with Pillars
For: Keep the three pillars easy to distinguish while the player experiments.
Trigger: The player changes a pillar lever or pressure-plate state while Objective 1 is active.
Player Experience: The player learns each pillar by experimentation: lever combinations change color and the plate changes only steady versus pulse.
Uses: Left / Middle / Right pillar labels; pillar lamps; upper/lower levers; pressure plates
Done When:
- LEFT, MIDDLE, and RIGHT identities remain clear from the player position.
- Every lever change produces immediate deterministic lamp-color feedback for that pillar.
- Pressure plates change only steady/pulse state and never change the selected color.

### Gameplay Flow 04 — Complete & Transition
For: Confirm the solved pillar state and open the route to the Broken Gallery.
Trigger: Left = Orange + pulse, Middle = Brown + steady, and Right = Purple + steady are all valid at the same time.
Player Experience: The three pillars visibly synchronize, the Resonance Engine returns to operation, and attention moves to the newly opened Broken Gallery route.
Uses: Resonance Engine restoration presentation; pillar completion feedback
Done When:
- Completion validates the full simultaneous final state rather than a partial match.
- The completion response plays once and clearly confirms success.
- The Broken Gallery route opens and Objective 1 temporary state is ready for the next reset.


### UI & Information

#### Objective 1 Instruction Panel
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

#### Partial Door Target Display
Flow: 01 — Read Partial Target
For: Show only Middle = Brown while Left, Right, and Pulse remain unknown.
Requirement: Create one player-readable target display near the exit that intentionally reveals only the middle pillar color. It must not reveal the left color, right color, pulse location, or any lever combination. The unknown values remain visible as missing information until the player solves the puzzle through the books and machine experimentation.
Content:
```text
LEFT      MIDDLE      RIGHT
 ?         BROWN        ?

PULSE: ?
```
Usage: Visible throughout active Objective 1 solving. It may switch to a solved/confirmed presentation only after the complete hidden target state is matched.

#### Scattered Clue Book Set
Flow: 02 — Search Clues
For: Provide the 12 approved books used to infer the missing target information.
Requirement: Produce twelve one-paragraph books scattered around the chamber with no required reading order. The set contains two mechanic-rule books, eight useful clue books, and two harmless decoys. Useful clues must be easy to understand without being overly obvious and must help the player infer the hidden target Left = Orange, Right = Purple, and Pulse = Left. They must not teach all twelve lever-to-color mappings. The two decoys must contain ordinary maintenance/lore information and must never provide false puzzle facts. A player who finds useful books first may solve faster by luck, and valid completion must not require reading all twelve books.
Content:
```text
BOOK 1 — LEVER NOTES
Each pillar is tuned by two levers. Start with the upper lever, then try the lower one. Watch the lamp after each change. Different positions reveal different colors.

BOOK 2 — PRESSURE PLATE NOTES
The plate does not change the lamp's color. It only changes the way the lamp shines. Step on it to make the lamp pulse. Leave it clear to keep the light steady.

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
Only one of the three lamps should pulse. The middle lamp shown on the door display must stay steady.

BOOK 10 — CALIBRATION NOTE
The right lamp must also stay steady. Only the remaining lamp should pulse.

BOOK 11 — REPAIR LOG
The lower gear housing was repaired after the last restoration cycle. No further damage was found during inspection.

BOOK 12 — WORKSHOP NOTE
Spare tools were moved to the eastern storage cabinet after the last maintenance shift.
```

### Visual Effects & Presentation

#### Pillar Readability
Flow: 03 — Experiment with Pillars
For: Distinguish the Left, Middle, and Right pillars through the environment, not debug-style UI.
Requirement: Make the three pillars readable through stable placement, visual identity, and lamp presentation. Do not add technical state labels such as STEADY/PULSE as standalone player UI.
Usage: Active throughout Objective 1.

#### Pillar Interaction Feedback
Flow: 03 — Experiment with Pillars
For: Show the immediate lamp result of lever and pressure-plate changes.
Requirement: Every valid lever change must produce immediate readable lamp feedback on its own pillar so the player can discover the lever-to-color behavior through experimentation. Every pressure-plate interaction must visibly switch only that pillar between steady and pulsing without changing its selected color. When the hidden final target is matched—Left Orange pulsing, Middle Brown steady, Right Purple steady—run one concise confirmation response before opening the next route.
Usage: Active throughout Objective 1 and reset completely for the next run.

#### Resonance Engine Restoration
Flow: 04 — Complete & Transition
For: Confirm Objective 1 completion and direct attention to the next route.
Requirement: Create one short completion presentation that visually confirms all three pillars have synchronized and the Engine has returned to operation, then directs attention toward the newly opened Broken Gallery route.
Usage: Runs once after valid Objective 1 completion.

## The Broken Gallery

### Gameplay Flow 01 — Enter & Learn Route Loop
For: Teach the search, repair, and checkpoint loop used throughout the Gallery.
Trigger: The player enters Broken Gallery Level 1 with checkpoint barrels and the three route choices available.
Player Experience: The player learns the repeated loop: search barrels, repair only marked gaps, reach the checkpoint, and retry only the current level on failure.
Uses: Custodian Vex; Objective 2 Instruction Panel; Valid Placement Markers
Done When:
- The route-loop instruction text is readable without revealing a viable route.
- Legal placement markers are clearly different from ordinary environment blocks.
- Vex briefing communicates limited-resource planning and local retry without introducing old mechanics.

### Gameplay Flow 02 — Level 1
For: Present the Level 1 route choice and 12-block crossing rule.
Trigger: Checkpoint 1 is active and Level 1 resources/routes are reset.
Player Experience: The player reads three routes, uses the 12-block allocation, and must avoid wasting supplies on the non-viable route.
Uses: Level 1 Brief; checkpoint barrels; Valid Placement Markers
Done When:
- The Level 1 brief uses the exact approved text and does not reveal which two routes work.
- The authored allocation is 12 blocks and only marked placements are accepted.
- Middle and Right remain viable, Left remains non-viable, and successful crossing reaches Checkpoint 2.

### Gameplay Flow 03 — Level 2
For: Present the Level 2 route choice and 20-block + 3-ladder rule.
Trigger: Checkpoint 2 is active and Level 2 resources/routes are reset.
Player Experience: The player solves a tighter route/resource problem using 20 blocks and 3 ladders while only one route can be completed.
Uses: Level 2 Brief; checkpoint barrels; blocks; ladders; Valid Placement Markers
Done When:
- The Level 2 brief uses the exact approved text without naming the viable route.
- The authored allocation is 20 blocks + 3 ladders and placement remains marker-owned.
- Only the Right route is viable and successful crossing reaches Checkpoint 3.

### Gameplay Flow 04 — Level 3 Time Challenge
For: Present the 50% timed-route challenge and its warning cue.
Trigger: Checkpoint 3 is active, all three routes are initially viable, and the timed attempt begins when the player materially commits to a route.
Player Experience: The player chooses a route, hears/sees Gremlin-timed urgency, and must reach at least 50% route progress before the authored threshold.
Uses: Gremlin; Custodian Vex; Level 3 Time-Challenge Brief; Level 3 Time-Challenge Cue; route-progress state
Done When:
- The exact Level 3 instruction is readable before/during the attempt without revealing route geometry.
- The warning cue and Vex line clearly mark the timed requirement.
- At least 50% progress before the threshold preserves the chosen route and allows the crossing to continue.

### Gameplay Flow 05 — Retry / Route Closure
For: Explain local retry and clearly show when a failed Level 3 route closes.
Trigger: The active level exhausts its resources or configured time, or a Level 3 attempt misses the 50% progress threshold.
Player Experience: The player gets a local reset. Level 1/2 simply retry; Level 3 visibly loses the failed route while another alternative remains.
Uses: Route Failure Message; Level Retry Reset; Gremlin Route-Closed Event
Done When:
- Temporary blocks/ladders from the failed attempt are removed and the active checkpoint becomes safe/retryable.
- Current-level resources become available again while earlier completed Gallery levels remain complete.
- A failed Level 3 route is visibly unavailable while alternatives remain, and the last remaining route never makes the objective unwinnable before normal timeout.


### UI & Information

#### Objective 2 Instruction Panel
Flow: 01 — Enter & Learn Route Loop
For: Give the repeated Gallery loop: search barrels, repair marked gaps, reach checkpoint.
Requirement: Create one concise instruction panel explaining the repeatable loop shared by the three route levels: search barrels, repair only marked gaps, and reach the next checkpoint. It must explain that failed attempts reset only the current level.
Content:
```text
CROSS THE BROKEN GALLERY

SEARCH BARRELS → REPAIR MARKED GAPS → REACH THE CHECKPOINT

Blocks and ladders can only be placed on marked positions.
If a route runs out of resources or time, this level resets and you can try again.
```

#### Level 1 Brief
Flow: 02 — Level 1
For: Tell the player the Level 1 route-count and 12-block requirement.
Requirement: Show the Level 1 rules without revealing which two routes are viable.
Content:
```text
LEVEL 1 · EASY
Three routes. Two can be completed.
A viable crossing needs 12 blocks.
Choose carefully and reach the next checkpoint.
```

#### Level 2 Brief
Flow: 03 — Level 2
For: Tell the player the Level 2 route-count and 20-block + 3-ladder supply.
Requirement: Show the Level 2 resource requirement without revealing that the right route is the viable answer.
Content:
```text
LEVEL 2 · MEDIUM
Three routes. Only one can be completed.
Crossing supply: 20 blocks + 3 ladders.
Place them only on marked positions.
```

#### Level 3 Time-Challenge Brief
Flow: 04 — Level 3 Time Challenge
For: Tell the player all routes initially work and 50% progress is required before time expires.
Requirement: Clearly explain that all three routes are initially valid in Level 3, but the chosen route must reach at least 50% progress before the authored time threshold. Explain the consequence without revealing route geometry.
Content:
```text
LEVEL 3 · GREMLIN TIME CHALLENGE
All three routes can work.
Reach 50% of your chosen route before the timer expires.
If you fail, that route closes and you return to Checkpoint 3.
```

#### Route Failure Message
Flow: 05 — Retry / Route Closure
For: Tell the player whether the active level resets or a Level 3 route is permanently lost for the run.
Requirement: Create one recovery message for Level 1/2 failed attempts and one distinct route-closed message for Level 3.
Content:
```text
ROUTE RESET
Return to the checkpoint, search the barrels again, and try another route.

ROUTE LOST
That route is now closed.
Return to Checkpoint 3, resupply, and choose another active route.
```

#### Valid Placement Markers
Flow: 01 — Enter & Learn Route Loop
For: Mark exactly where bridge blocks and ladders may be placed.
Requirement: Create one consistent player-readable marker treatment for every position where a bridge block or ladder is allowed. The marker must distinguish legal placement from ordinary environment blocks without revealing which full route is viable.
Usage: Present only on authored placement positions and restored with each current-level reset.

Content:
```text
BUILD HERE
```

### Audio

#### Level 3 Time-Challenge Cue
Flow: 04 — Level 3 Time Challenge
For: Clearly signal the start of the Level 3 progress deadline.
Requirement: Create one independent short warning cue that clearly marks the start of the Level 3 progress deadline. It should read as Gremlin-triggered urgency and remain distinct from normal checkpoint, placement, or route-reset sounds.
Usage: Plays when the Level 3 authored timer begins; Voice Production may play alongside it but is owned separately.

### Visual Effects & Presentation

#### Level Retry Reset
Flow: 05 — Retry / Route Closure
For: Show a local level retry without making it feel like a full objective failure.
Requirement: Create one brief readable reset presentation for failed Level 1/2 attempts: temporary placed blocks/ladders are removed, the player returns to the current checkpoint, and the resource-search loop visibly becomes available again. Avoid presenting this as a full objective failure.
Usage: Runs only for the current level that failed.

#### Gremlin Route-Closed Event
Flow: 05 — Retry / Route Closure
For: Make the failed route visibly unavailable while alternatives remain readable.
Requirement: Create one Level 3 failure presentation in which the selected failed route changes to a clearly unavailable state, the player returns to Checkpoint 3, and the remaining active routes stay readable. The Gremlin framing and warning cue may be synchronized inside this authored sequence.
Usage: Runs after a Level 3 route misses its required progress threshold while another active route remains.

## The Warden Halls

### Gameplay Flow 01 — Learn Trap Rules
For: Introduce the Echo Pebble and distinguish laser, floor, and axe hazards.
Trigger: The Warden Halls activate and the player receives the unlimited Echo Pebble before the first trap-family encounters.
Player Experience: The player understands which hazards accept Echo Pebble interaction and which must instead be avoided or timed.
Uses: Custodian Vex; Echo Pebble; Wall Laser Sensor; Swinging Axe Trap; Objective 3 Instruction Panel
Done When:
- The instruction panel uses the exact approved trap/Pebble rules.
- Wall lasers, floor traps, and swinging axes remain visually distinguishable.
- Nothing implies that floor traps or swinging axes can be disabled with Echo Pebble.

### Gameplay Flow 02 — Use Echo Pebble
For: Support valid Pebble interactions, laser disable, blocker stones, and cooldown feedback.
Trigger: The player throws Echo Pebble at a valid wall-laser sensor or authored hanging-stone target.
Player Experience: A valid sensor hit creates a short four-second laser opening; selected hanging stones can instead block the beam, while the three-second throw cooldown remains readable.
Uses: Echo Pebble; Wall Laser Sensor; Laser Blocker Stone; Echo Pebble Cooldown Indicator
Done When:
- Each throw starts the approved 3-second cooldown and the UI returns to READY afterward.
- A valid wall-laser sensor hit disables only that laser for 4 seconds of game-time.
- Only authored hanging-stone targets create the alternate beam-blocking solution; invalid floor/axe targets do not disable anything.

### Gameplay Flow 03 — Hazard Contact & Recovery
For: Show trap-hit feedback and checkpoint recovery after gameplay health reaches zero.
Trigger: The player contacts a laser, floor trap, or swinging axe, or gameplay health reaches zero from Warden hazards.
Player Experience: The player receives hazard-specific feedback/effects; zero gameplay health returns them to the current safe checkpoint instead of restarting the full objective.
Uses: Trap Hit Feedback; Checkpoint Recovery; active Warden checkpoint
Done When:
- Laser, floor, and axe contacts apply their approved damage/status effects and remain distinguishable.
- Gameplay health reaching zero returns the player to the active Warden checkpoint in a safe recovered state.
- Earlier completed Warden levels remain complete after checkpoint recovery.

### Gameplay Flow 04 — Complete & Transition
For: Close the Warden section and direct the player toward the Workshop.
Trigger: The player clears the third Warden level and reaches the inner gate.
Player Experience: Vex acknowledges that the Wardens are still serving the vault and directs the player into Gremlin’s Workshop.
Uses: Custodian Vex; inner gate transition
Done When:
- The transition Voice plays once without replaying Pebble instructions.
- The Workshop route becomes the clear next destination.
- No Workshop sabotage is revealed before its authored trigger.


### 3D Models

#### Echo Pebble
Flow: 01 — Learn Trap Rules
For: Reusable throwable tool for valid wall-laser and hanging-stone interactions.
Requirement: Create one small throwable pebble item, visually derived from a stone/snowball-scale projectile but clearly authored for the Clockwork Vault. It needs held/throw/projectile/valid-hit feedback and must support an unlimited-use loop with a visible 3-second cooldown. Its impact feedback must distinguish a valid wall-laser sensor or hanging-stone target from an invalid floor/axe target.
Usage: Granted for Objective 3 and removed/reset at objective exit.

#### Wall Laser Sensor
Flow: 02 — Use Echo Pebble
For: Readable Pebble target with active and 4-second disabled states.
Requirement: Create one readable wall-mounted laser sensor/beam assembly with Active and Temporarily Disabled states. The sensor must be an obvious Echo Pebble target; a valid hit disables the beam for the approved 4-second game-time window before normal behavior resumes. Attached activation/deactivation VFX and SFX remain part of this asset.
Usage: Distributed across the three Warden levels.

#### Laser Blocker Stone
Flow: 02 — Use Echo Pebble
For: Alternate laser solution that drops into the beam after a valid Pebble hit.
Requirement: Create one authored hanging-stone target for selected laser encounters. A valid Echo Pebble hit must cause the stone to move/drop into the beam path and visibly block the laser, creating a readable alternate solution without changing unrelated traps.
Usage: Used only at authored laser encounters that support the blocker-stone solution.

#### Swinging Axe Trap
Flow: 01 — Learn Trap Rules
For: Ceiling timing hazard with readable swing, hit, knockback, and reset states.
Requirement: Create one large double-sided swinging axe trap mounted from the ceiling. It needs a clearly readable left-right swing cycle, safe timing windows, contact/knockback feedback, and a reset state. It must never appear to accept Echo Pebble disable input.
Usage: Distributed across the Warden levels as a timing hazard.

### UI & Information

#### Objective 3 Instruction Panel
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

#### Echo Pebble Cooldown Indicator
Flow: 02 — Use Echo Pebble
For: Show whether the unlimited Echo Pebble is READY or RECHARGING.
Requirement: Create one compact player-facing cooldown indicator that appears after a throw and clearly returns to READY after 3 seconds. It must not imply that the player has a limited pebble count.
Content:
```text
ECHO PEBBLE · READY
ECHO PEBBLE · RECHARGING
```

### Visual Effects & Presentation

#### Trap Readability
Flow: 01 — Learn Trap Rules
For: Make lasers, floor traps, and swinging axes readable from their appearance and motion.
Requirement: Communicate hazard type through environment design, animation, beam state, and motion rather than debug-style instructional labels. Floor traps and swinging axes must never look Pebble-disableable.
Usage: Present wherever the physical hazard needs stronger readability.

#### Trap Hit Feedback
Flow: 03 — Hazard Contact & Recovery
For: Make laser, floor, and axe hits visually distinguishable.
Requirement: Create clear but compact feedback for each approved hazard consequence so the player can identify which trap hit them and understand the resulting temporary impairment. Laser, floor, and axe hits must remain distinguishable while avoiding screen obstruction during active traversal.
Usage: Triggered on valid hazard contact together with the approved damage/status effects.

#### Checkpoint Recovery
Flow: 03 — Hazard Contact & Recovery
For: Return the player safely to the active Warden checkpoint after gameplay health reaches zero.
Requirement: When trap damage reduces gameplay health to zero, present one quick checkpoint recovery that returns the player to the active Warden level without replaying earlier completed levels. Restore player control only after the checkpoint position is safe.
Usage: Runs on Objective 3 hazard defeat only.

## The Gremlin's Workshop

### Gameplay Flow 01 — Learn Network / Ring 1
For: Teach the L-rotator rule and establish the first powered connection.
Trigger: The player enters the Workshop and the unsabotaged L-rotator network becomes interactive.
Player Experience: The player learns that power begins at the Generator, each rotator is an L connection, and one continuous route must reach Ring 1.
Uses: Custodian Vex; Power Generator; 90-Degree Rotator Junction; Orrery Ring; Objective 4 Instruction Panel; Ring Progress Display
Done When:
- The instruction text explains Generator → Ring 1 → Ring 2 → Ring 3 without exposing the authored route solution.
- Each rotator has four readable orientations and powered/unpowered state is visually clear.
- Ring 1 becomes powered only when a continuous valid path exists from the Generator.

### Gameplay Flow 02 — Extend to Ring 2
For: Show live ring status while the same network extends to Ring 2.
Trigger: Ring 1 is powered and the player continues the same network toward Ring 2.
Player Experience: The player extends the existing live route while keeping Ring 1 connected; the status display reflects actual connectivity.
Uses: Power Generator; 90-Degree Rotator Junction; Orrery Rings; Ring Progress Display
Done When:
- Ring 2 becomes powered only while Generator → Ring 1 → Ring 2 is continuously connected.
- The Ring Progress Display immediately reflects any real loss of power rather than milestone history.
- The post-Ring-2 route-swap trigger becomes eligible only after the approved stable state.

### Gameplay Flow 03 — Route Swap Sabotage
For: Show and explain the Gremlin route-swap event after Ring 2.
Trigger: About 20 seconds after Ring 1 and Ring 2 are continuously connected.
Player Experience: Gremlin deliberately blocks the route the player just used, a previously blocked alternate path opens, Ring 2 loses power, Gremlin taunts, then Vex gives recovery guidance.
Uses: Gremlin; Custodian Vex; Power Generator; 90-Degree Rotator Junction; Ring Progress Display; First Sabotage Message
Done When:
- The route-swap sabotage triggers once for the session.
- The old route becomes clearly unavailable, the authored alternate opens, and connectivity/power is recalculated immediately.
- The exact sabotage text plus Gremlin and Vex lines play in the intended order without revealing the solution path.
- The player can recover using the same L-rotator rule.

### Gameplay Flow 04 — 50% Rollback
For: Show the first rollback when two Generator-to-Ring-1 rotators are changed.
Trigger: Validated Ring 2 → Ring 3 route progress reaches 50% for the first time.
Player Experience: Gremlin rotates exactly two previously correct Generator → Ring 1 rotators, earlier power drops, Gremlin gloats, and Vex directs the player back to repair the link.
Uses: Gremlin; Custodian Vex; 90-Degree Rotator Junction; Ring Progress Display; 50% Sabotage Message
Done When:
- Exactly two approved Generator → Ring 1 rotators change orientation once.
- Power loss propagates immediately and the exact 50% message identifies the affected section without exposing rotator positions.
- Gremlin taunt and Vex repair guidance play without changing the learned routing rule.

### Gameplay Flow 05 — 80% Rollback
For: Show the second rollback when three Ring-1-to-Ring-2 rotators are changed.
Trigger: Validated Ring 2 → Ring 3 route progress reaches 80% for the first time.
Player Experience: Gremlin rotates exactly three previously correct Ring 1 → Ring 2 rotators, removes earlier power again, and the player must repair that section before finishing.
Uses: Gremlin; Custodian Vex; 90-Degree Rotator Junction; Ring Progress Display; 80% Sabotage Message
Done When:
- Exactly three approved Ring 1 → Ring 2 rotators change orientation once.
- The exact 80% message and visible power state make the broken earlier section clear.
- Gremlin and Vex lines play in order and the player can repair with the same L-rotator rule.

### Gameplay Flow 06 — Restore Great Orrery
For: Present the final continuous-power success and Great Orrery restoration.
Trigger: Generator, Ring 1, Ring 2, and Ring 3 are all continuously connected after all authored sabotage events.
Player Experience: Gremlin realizes the player has outsmarted the sabotage, all rings synchronize, the Great Orrery returns to life, puzzle input closes, and the exit begins opening.
Uses: Gremlin; Power Generator; Orrery Rings; Great Orrery Restoration
Done When:
- Completion requires one continuous final network across Generator and all three rings.
- Gremlin’s outsmarted reaction plays once and does not replace Vex’s later ending speech.
- The final restoration presentation clearly confirms success and begins the ending/exit handoff.


### 3D Models

#### Power Generator
Flow: 01 — Learn Network / Ring 1
For: Main power source with clear offline, live, and interrupted states.
Requirement: Create one central power-source machine with clearly different Offline, Live, and Power-Interrupted feedback. The output direction into the routing network must remain visually readable from the puzzle area. Attached startup/interruption SFX and energy VFX remain part of this asset.
Usage: Source of the Objective 4 continuous power network.

#### 90-Degree Rotator Junction
Flow: 01 — Learn Network / Ring 1
For: Reusable L-junction showing route direction and powered/unpowered state.
Requirement: Create one reusable L-shaped power junction that rotates in 90-degree steps and connects exactly two orthogonal directions. It needs four readable orientations plus Powered and Unpowered visual states. Interaction must make the route direction legible without exposing the route solution.
Usage: Repeated at authored Objective 4 junction locations.

#### Orrery Ring
Flow: 02 — Extend to Ring 2
For: Reusable Ring 1–3 milestone asset with clear inactive and powered states.
Requirement: Create one reusable ring mechanism used as Ring 1, Ring 2, and Ring 3 with clearly readable Inactive and Powered states. The three instances must remain distinguishable by position/label while sharing one visual grammar. The final state must support all three rings operating together as the Great Orrery restoration payoff.
Usage: Sequential milestones in Objective 4 and the ending transition.

### UI & Information

#### Objective 4 Instruction Panel
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

#### Ring Progress Display
Flow: 02 — Extend to Ring 2
For: Show current live power state for Ring 1, Ring 2, and Ring 3.
Requirement: Create one compact player-facing or in-world status treatment showing which rings currently have power. It must update from actual connectivity rather than milestone history so a Gremlin disruption can visibly remove power from an earlier ring.
Content:
```text
RING 1 · POWERED / OFFLINE
RING 2 · POWERED / OFFLINE
RING 3 · POWERED / OFFLINE
```

#### First Sabotage Message
Flow: 03 — Route Swap Sabotage
For: Tell the player the old route is blocked and another path has opened.
Requirement: Explain the post-Ring-2 route swap without identifying the alternate-route solution.
Content:
```text
GREMLIN SABOTAGE
The previous route is blocked.
A different path has opened.
Reroute the power and restore the connection.
```

#### 50% Sabotage Message
Flow: 04 — 50% Rollback
For: Tell the player the first power connection has been disrupted.
Requirement: Identify the affected gameplay connection without exposing implementation counts or rotator positions.
Content:
```text
POWER LOST · GENERATOR → RING 1
The first connection has been knocked out of line.
Restore it, then continue toward Ring 3.
```

#### 80% Sabotage Message
Flow: 05 — 80% Rollback
For: Tell the player an earlier Ring 1 → Ring 2 connection has been disrupted.
Requirement: Identify the affected gameplay connection without exposing implementation counts or rotator positions.
Content:
```text
POWER LOST · RING 1 → RING 2
An earlier connection has been knocked out of line.
Restore it, then finish Ring 3.
```

### Visual Effects & Presentation

#### Ring 2 Route-Swap Sabotage
Flow: 03 — Route Swap Sabotage
For: Visually swap the active and alternate routes and show the resulting power loss.
Requirement: About 20 seconds after Ring 1 and Ring 2 are connected, run one authored Gremlin sequence that makes the previously active route become visibly blocked, makes the previously blocked alternate path visibly available, removes power where connectivity is broken, and then returns control for rerouting. The change must be understandable without exposing route coordinates or implementation labels.
Usage: Runs once per Objective 4 session after the approved Ring 2 condition.

#### 50% Rotator Sabotage
Flow: 04 — 50% Rollback
For: Visually turn exactly two earlier Generator → Ring 1 rotators out of alignment.
Requirement: At the approved 50% Ring 2-to-Ring 3 progress trigger, run one short Gremlin disruption in which exactly two already-correct rotators on the Generator-to-Ring-1 connection visibly turn out of alignment. Power loss must propagate to the affected ring states before normal input resumes.
Usage: Runs once per Objective 4 session.

#### 80% Rotator Sabotage
Flow: 05 — 80% Rollback
For: Visually turn exactly three earlier Ring 1 → Ring 2 rotators out of alignment.
Requirement: At the approved 80% Ring 2-to-Ring 3 progress trigger, run one short Gremlin disruption in which exactly three already-correct rotators on the Ring-1-to-Ring-2 connection visibly turn out of alignment. The player must see that an earlier completed section has broken before normal input resumes.
Usage: Runs once per Objective 4 session.

#### Great Orrery Restoration
Flow: 06 — Restore Great Orrery
For: Show all rings synchronizing, power reaching the Orrery, and the exit beginning to open.
Requirement: When Generator, Ring 1, Ring 2, and Ring 3 are continuously connected, create one strong final restoration presentation: all three rings synchronize, power visibly reaches the Great Orrery, puzzle input closes, and the Clockwork exit begins opening. Keep the transition compatible with the existing ending sequence rather than creating a fifth objective.
Usage: Runs once on valid Objective 4 completion.

## Vault Restored

### Gameplay Flow 01 — Restoration Payoff & Reward
For: Present the restored vault, Vex closing moment, and Clockwork Wayfinder reward.
Trigger: The Great Orrery restoration callbacks complete and the closing scene reaches Vex recognition.
Player Experience: Vex acknowledges what the player restored, the gateway is open, and the Clockwork Wayfinder reward is presented after the completion record is secured.
Uses: Custodian Vex; Clockwork Wayfinder; Completion Message; Great Orrery / gateway presentation
Done When:
- The completion message and Vex line use the exact approved wording without exposing platform scoring.
- The Clockwork Wayfinder is presented/granted exactly once after the completion state is secured.
- The reopened gateway is clearly visible as the next action.

### Gameplay Flow 02 — Return Home
For: Tell the player the gateway is open and direct the final return route.
Trigger: Session result and reward state are secured and the safe return route is open.
Player Experience: Vex gives one concise farewell/navigation cue and the player follows the reopened route back to the holding area while lane cleanup begins safely.
Uses: Custodian Vex; Vault Awakening and Exit Reveal; safe return route
Done When:
- The exact safe-return Voice cue plays without repeating the completion speech.
- The return route is obvious and no new gameplay task is introduced.
- Lane reset/cleanup does not invalidate the player’s safe return and prepares the lane for reuse.


### 3D Models

#### Clockwork Wayfinder
Flow: 01 — Restoration Payoff & Reward
For: One-time cosmetic completion reward shown in the ending.
Requirement: Create one cosmetic completion reward object with a distinct Clockwork-Vault silhouette and a clear reward-reveal presentation. It does not provide new gameplay power and must support one-time grant/readability in the ending scene.
Usage: Presented after the Great Orrery restoration and granted exactly once through the existing ending flow.

### UI & Information

#### Completion Message
Flow: 02 — Return Home
For: Confirm the vault is restored and direct the player to the open return route.
Requirement: Create one concise completion message confirming that the restoration journey is finished and directing the player toward the reopened return route without exposing platform scoring.
Content:
```text
THE CLOCKWORK VAULT IS RESTORED
The gateway is open.
Follow the return route home.
```

### Visual Effects & Presentation

#### Vault Awakening and Exit Reveal
Flow: 01 — Restoration Payoff & Reward
For: Deliver the final restoration payoff, exit reveal, Vex moment, and reward handoff.
Requirement: Create one coordinated closing presentation that carries restored power from the Great Orrery into the surrounding vault, reveals the reopened exit, frames Vex's closing moment and Clockwork Wayfinder reward, then hands control to the safe return route. This sequence must remain reset-owned and must not introduce another challenge.
Usage: Runs after Objective 4 completion and before the player returns to the holding area.
