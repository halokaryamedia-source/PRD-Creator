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
Visual Brief: Clockwork custodian NPC. Needs the idle, speaking, pointing, alert, and completion animations used by the story.
Function: Guide NPC used for story, warnings, and completion dialogue.
Type: MODEL
Create: Create one reusable Custodian Vex NPC/model setup.
Used: Across the story wherever Custodian Vex appears.
Moment: Used Across the Map
Includes: NPC model/texture; idle and speaking states; required authored character animations.
Group: 01 — Shared Characters
For: Vex’s reusable in-world character asset.
Requirement: Create or reuse one Clockwork-compatible Custodian Vex NPC presentation for all required story, briefing, warning, reminder, and ending moments. Vex must remain visually recognizable across the complete journey and support readable idle, speaking, pointing/highlight, alert, and completion-reaction states without changing gameplay rules.
Usage: Shared across the Antechamber, Objectives 1-4, and the ending wherever canonical Voice Production is triggered.

#### Gremlin
Flow: 01 — Shared Characters
Visual Brief: Small clockwork gremlin NPC. Needs movement, sabotage, taunt, and defeated reactions used in the map.
Function: Sabotage character used in the final Gallery crossing and the Workshop.
Type: MODEL
Create: Create one reusable Gremlin NPC/model setup.
Used: During the Broken Gallery challenge and Workshop sabotage moments.
Moment: Used Across the Map
Includes: Character model/texture; appearance/movement states; sabotage and reaction animations.
Group: 01 — Shared Characters
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
Visual Brief: Distinct key item for the opening pedestal and pickup.
Function: Opening key used to unlock the first seal.
Type: ITEM
Create: Create one reusable Custodian Key item setup.
Used: At the opening pedestal and first seal.
Moment: Entering the Antechamber
Includes: Item appearance; readable pickup/pedestal state; accepted state at the first seal.
Group: 01 — Opening Story
For: The story key used to open the first seal.
Requirement: Create one clearly readable key item for the opening progression. It needs available/picked-up/accepted states and must visually belong to the Clockwork Vault rather than resemble an ordinary reward item.
Usage: Presented on the Antechamber pedestal and accepted by the Resonance Engine seal.

### UI & Information

#### Custodian Key Prompt
Flow: 02 — Take Key & Open Seal
Function: Tells the player to take the Custodian Key and use it to begin opening the vault.
Type: UI / TEXT
Create: Create the exact player-facing Custodian Key Prompt.
Used: When the player must take the Custodian Key.
Moment: Opening the First Seal
Group: 02 — Open First Seal
For: Point the player toward the first seal.
Requirement: Keep the prompt short and fully in-world.
Content:
```text
TAKE THE CUSTODIAN KEY
The first seal is waiting.
```

### Visual Effects & Presentation

## The Resonance Engine

### Gameplay Flow 01 — The Door Remembers
For: Introduce the incomplete answer and the mystery of the chamber.
Trigger: The Resonance Engine seal opens and the player gains control inside the reset chamber.
Player Experience: The player immediately sees the basic task and the intentionally incomplete target: Middle is Brown while Left, Right, and Pulse remain unknown.
Uses: Custodian Vex; Resonance Engine Entrance Message; Partial Door Target Display
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
Uses: Custodian Vex; Resonance Engine Restored Message; Resonance Engine restoration presentation; pillar completion feedback
Done When:
- Completion validates the full simultaneous final state rather than a partial match.
- The completion response plays once and clearly confirms success.
- The Broken Gallery route opens and Objective 1 temporary state is ready for the next reset.


### UI & Information

#### Resonance Engine Entrance Message
Flow: 01 — The Door Remembers
Function: Tells the player the missing clues are somewhere in the chamber without giving the solution.
Type: UI / TEXT
Create: Create the exact player-facing Resonance Engine Entrance Message.
Used: When the Resonance Engine objective begins.
Moment: Entering the Resonance Engine
Group: 01 — Chamber Guidance
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
Function: Shows Middle = Brown. Left, Right, and Pulse remain unknown.
Type: UI / TEXT
Create: Create the exact player-facing Partial Door Target Display.
Used: Throughout Resonance Engine solving.
Moment: Throughout the Resonance Engine
Group: 01 — Chamber Guidance
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
Function: Provides 12 books: 2 rule notes, 8 useful clues, and 2 decoys.
Type: UI / TEXT
Create: Create the exact player-facing Scattered Clue Book Set.
Used: While the player searches the Resonance Engine chamber for clues.
Moment: Searching the Chamber
Group: 02 — Clue Set
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

#### Resonance Engine Restored Message
Flow: 04 — Engine Restored
Function: Confirms the Resonance Engine is restored and points the player to the Broken Gallery.
Type: UI / TEXT
Create: Create the exact player-facing Resonance Engine Restored Message.
Used: When Objective 1 completes.
Moment: Resonance Engine Restored
Group: 04 — Engine Restored
For: Confirm the successful restoration and make the next route obvious.
Requirement: Keep the completion message short and in-world. Do not repeat the hidden combination or puzzle rules.
Content:
```text
ENGINE RESTORED

The pillars are in tune again.
The Broken Gallery is open.
```

### Visual Effects & Presentation

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


### Gameplay Flow 06 — Gallery Cleared
For: Confirm the final crossing is complete and hand the player to the Warden Halls.
Trigger: The player clears the final Gallery crossing and reaches the exit.
Player Experience: The damaged Gallery is behind them, the next route is open, and Vex points them toward the Warden Halls.
Uses: Custodian Vex; Gallery Cleared Message
Done When:
- The success response plays once after the final crossing is secured.
- The completion message clearly names the Warden Halls as the next destination.
- The player is not given any Warden trap solution before entering the next objective.

### UI & Information

#### Broken Gallery Entrance Message
Flow: 01 — Enter the Gallery
Function: Tells the player to use the old supplies and repair only marked gaps.
Type: UI / TEXT
Create: Create the exact player-facing Broken Gallery Entrance Message.
Used: When the player enters the Broken Gallery.
Moment: Entering the Broken Gallery
Group: 01 — Shared Gallery Assets
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
Function: Tells the player more than one route can work without revealing which ones.
Type: UI / TEXT
Create: Create the exact player-facing First Crossing Message.
Used: When the first Gallery crossing becomes active.
Moment: First Crossing
Group: 02 — First Crossing
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
Function: Tells the player only one route can work without naming it.
Type: UI / TEXT
Create: Create the exact player-facing Second Crossing Message.
Used: When the second Gallery crossing becomes active.
Moment: Second Crossing
Group: 03 — Second Crossing
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
Function: Explains the final crossing: choose a path and reach halfway before time runs out.
Type: UI / TEXT
Create: Create the exact player-facing Gremlin's Wager Message.
Used: When the final Gallery crossing begins.
Moment: Gremlin's Final Crossing
Group: 04 — Gremlin’s Wager
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
Function: Shows a short message when a crossing fails or Gremlin removes a route.
Type: UI / TEXT
Create: Create the exact player-facing Crossing Failure Messages.
Used: When a Gallery crossing attempt fails or a final route is lost.
Moment: Crossing Failed / Route Lost
Group: 05 — Path Failure
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

#### Gallery Cleared Message
Flow: 06 — Gallery Cleared
Function: Confirms the Broken Gallery is cleared and points the player to the Warden Halls.
Type: UI / TEXT
Create: Create the exact player-facing Gallery Cleared Message.
Used: When Objective 2 completes.
Moment: Broken Gallery Cleared
Group: 06 — Gallery Cleared
For: Confirm the successful crossing and make the next destination clear.
Requirement: Keep the completion message short and in-world. Do not repeat route, resource, retry, or timer rules.
Content:
```text
GALLERY CLEARED

The last crossing is behind you.
The Warden Halls are ahead.
```

#### Repair Gap Markers
Flow: 01 — Enter the Gallery
Visual Brief: Simple marker or prop placed on repairable gaps. It must stand out from normal blocks without using debug text.
Function: Marks the gaps where the player is allowed to place repair blocks.
Type: MODEL
Create: Create one reusable marker treatment for repairable Gallery gaps.
Used: Throughout all Broken Gallery crossings.
Moment: Throughout the Broken Gallery
Includes: Visible environment marker treatment for valid repair positions.
Group: 01 — Shared Gallery Assets
For: Make repairable gaps visually distinct without putting debug text into the world.
Requirement: Use an environmental marker treatment for valid repair positions. Do not display debug-style placement text.
Usage: Visible only at authored repair positions.

### Audio

#### Gallery Challenge Warning Sound
Flow: 04 — Gremlin’s Wager
Audio Brief: Short mechanical warning sound with a mischievous feel. No spoken dialogue.
Function: Signals the start of Gremlin's final Gallery crossing.
Type: AUDIO
Create: Create one standalone Gremlin Wager Cue sound.
Used: When the final Gallery crossing begins.
Moment: Gremlin's Final Crossing
Group: 04 — Gremlin’s Wager
For: Gremlin-flavored warning sound as the final crossing turns dangerous.
Requirement: Create one independent short warning cue that clearly marks the start of the Level 3 progress deadline. It should read as Gremlin-triggered urgency and remain distinct from normal checkpoint, placement, or route-reset sounds.
Usage: Plays when the Level 3 authored timer begins; Voice Production may play alongside it but is owned separately.

### Visual Effects & Presentation

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
Uses: Custodian Vex; Warden Halls Cleared Message; inner gate transition
Done When:
- The transition Voice plays once without replaying Pebble instructions.
- The Workshop route becomes the clear next destination.
- No Workshop sabotage is revealed before its authored trigger.


### 3D Models

#### Echo Pebble
Flow: 01 — Enter the Warden Halls
Visual Brief: Small ordinary stone used as the throwable item. Use the same simple stone look in hand and as a projectile.
Function: Thrown at wall sensors and selected hanging stones.
Type: ITEM
Create: Create one reusable throwable Echo Pebble item/projectile setup.
Used: Throughout the Warden Halls.
Moment: Throughout the Warden Halls
Includes: Inventory/held appearance; projectile appearance; readable valid-hit response.
Group: 01 — Core Trap Kit
For: The throwable tool used against Warden sensors and loose stones.
Requirement: Create one small throwable pebble item, visually derived from a stone/snowball-scale projectile but clearly authored for the Clockwork Vault. It needs held/throw/projectile/valid-hit feedback and must support an unlimited-use loop with a visible 3-second cooldown. Its impact feedback must distinguish a valid wall-laser sensor or hanging-stone target from an invalid floor/axe target.
Usage: Granted for Objective 3 and removed/reset at objective exit.

#### Wall Laser Sensor
Flow: 02 — Echo Pebble
Visual Brief: Wall-mounted mechanical laser emitter with a visible beam. It needs clear active and disabled looks.
Function: Laser trap that blocks the path and can be disabled with the Echo Pebble.
Type: MODEL
Create: Create one reusable wall-mounted laser sensor setup.
Used: At laser encounters throughout the Warden Halls.
Moment: Throughout the Warden Halls
Includes: Sensor model/texture; visible laser beam; active and disabled states; attached animation/sound only when part of this same setup.
Group: 01 — Core Trap Kit
For: The wall-mounted Warden target the Echo Pebble can disturb.
Requirement: Create one readable wall-mounted laser sensor/beam assembly with Active and Temporarily Disabled states. The sensor must be an obvious Echo Pebble target; a valid hit disables the beam for the approved 4-second game-time window before normal behavior resumes. Attached activation/deactivation VFX and SFX remain part of this asset.
Usage: Distributed across the three Warden levels.

#### Laser Blocker Stone
Flow: 02 — Echo Pebble
Visual Brief: Stone hanging above selected laser paths. It drops into the beam and stays there as the blocker.
Function: Hanging stone that drops into a laser beam and blocks it.
Type: MODEL
Create: Create one reusable hanging blocker-stone setup.
Used: At selected laser encounters that use the blocker-stone solution.
Moment: Throughout the Warden Halls
Includes: Stone model/texture; hanging state; drop/block animation.
Group: 01 — Core Trap Kit
For: A loose stone that can fall into a laser beam.
Requirement: Create one authored hanging-stone target for selected laser encounters. A valid Echo Pebble hit must cause the stone to move/drop into the beam path and visibly block the laser, creating a readable alternate solution without changing unrelated traps.
Usage: Used only at authored laser encounters that support the blocker-stone solution.

#### Swinging Axe Trap
Flow: 01 — Enter the Warden Halls
Visual Brief: Large double-sided axe hanging from the ceiling with a left-right swing animation.
Function: Ceiling trap that swings across the corridor.
Type: MODEL
Create: Create one reusable ceiling-mounted swinging axe trap setup.
Used: At axe encounters throughout the Warden Halls.
Moment: Throughout the Warden Halls
Includes: Axe model/texture; ceiling mount; swing animation; reset state.
Group: 01 — Core Trap Kit
For: The ceiling hazard the player must time past.
Requirement: Create one large double-sided swinging axe trap mounted from the ceiling. It needs a clearly readable left-right swing cycle, safe timing windows, contact/knockback feedback, and a reset state. It must never appear to accept Echo Pebble disable input.
Usage: Distributed across the Warden levels as a timing hazard.

#### Floor Trap
Flow: 01 — Enter the Warden Halls
Visual Brief: Floor-mounted trap that looks different from normal floor blocks. It needs a ready look and a triggered look.
Function: Floor trap that activates when the player steps on it.
Type: MODEL
Create: Create one reusable floor-trap setup.
Used: At floor-trap encounters throughout the Warden Halls.
Moment: Throughout the Warden Halls
Includes: Trap model/visual; armed, triggered, and reset states.
Group: 01 — Core Trap Kit
For: The ground hazard the player must avoid.
Requirement: Create one readable floor-trap treatment with Armed, Triggered, and Reset states. It must stay visually distinct from wall sensors and must never suggest that Echo Pebble can disable it. Exact damage and status effects remain in 03 Development.
Usage: Distributed across the Warden levels as an avoid-only ground hazard.

### UI & Information

#### Warden Halls Entrance Message
Flow: 01 — Enter the Warden Halls
Function: Introduces the Warden Halls and hints that the Echo Pebble works on wall sensors.
Type: UI / TEXT
Create: Create the exact player-facing Warden Halls Entrance Message.
Used: When the player enters the Warden Halls.
Moment: Entering the Warden Halls
Group: 02 — Player Communication
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
Function: Shows whether the Echo Pebble is ready.
Type: UI / TEXT
Create: Create the exact player-facing Echo Pebble HUD.
Used: While the Echo Pebble is available.
Moment: Throughout the Warden Halls
Group: 02 — Player Communication
For: Show when the Echo Pebble can be thrown again.
Requirement: Keep the HUD state compact; the exact recharge duration stays in Development.
Content:
```text
ECHO PEBBLE · READY
ECHO PEBBLE · RECHARGING
```

#### Warden Halls Cleared Message
Flow: 04 — Enter the Workshop
Function: Confirms the Warden Halls are cleared and points the player to the Workshop.
Type: UI / TEXT
Create: Create the exact player-facing Warden Halls Cleared Message.
Used: When Objective 3 completes.
Moment: Warden Halls Cleared
Group: 04 — Enter the Workshop
For: Confirm the inner gate has opened and make the Workshop the clear next destination.
Requirement: Keep the completion message short and in-world. Do not repeat Echo Pebble or hazard rules.
Content:
```text
WARDEN HALLS CLEARED

The inner gate is open.
The Workshop is next.
```

### Visual Effects & Presentation

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
Visual Brief: Central power machine with a clear output side. It needs powered and unpowered looks.
Function: Power source for the Orrery network.
Type: MODEL
Create: Create one reusable power-generator setup for the Orrery network.
Used: Throughout the Gremlin Workshop objective.
Moment: Throughout Gremlin's Workshop
Includes: Model/texture; offline, live, and interrupted states; attached energy/sound only when part of this same setup.
Group: 01 — Core Network Kit
For: The visible source feeding power into the Orrery network.
Requirement: Create one central power-source machine with clearly different Offline, Live, and Power-Interrupted feedback. The output direction into the routing network must remain visually readable from the puzzle area. Attached startup/interruption SFX and energy VFX remain part of this asset.
Usage: Source of the Objective 4 continuous power network.

#### 90-Degree Rotator Junction
Flow: 01 — Wake Ring One
Visual Brief: Compact L-shaped junction with two perpendicular connections. It rotates in 90-degree steps and needs powered and unpowered looks.
Function: L-shaped junction the player rotates to redirect power.
Type: MODEL
Create: Create one reusable rotator-junction setup.
Used: Throughout the Gremlin Workshop objective.
Moment: Throughout Gremlin's Workshop
Includes: Junction model/texture; four orientations; powered/unpowered states; rotation animation.
Group: 01 — Core Network Kit
For: The reusable junction the player turns to redirect power.
Requirement: Create one reusable L-shaped power junction that rotates in 90-degree steps and connects exactly two orthogonal directions. It needs four readable orientations plus Powered and Unpowered visual states. Interaction must make the route direction legible without exposing the route solution.
Usage: Repeated at authored Objective 4 junction locations.

#### Orrery Ring
Flow: 02 — Wake Ring Two
Visual Brief: Clockwork ring mechanism with powered and unpowered looks and the motion used during final restoration.
Function: Ring mechanism used for Ring 1, Ring 2, and Ring 3.
Type: MODEL
Create: Create one reusable Orrery Ring setup used for all three rings.
Used: Throughout the Gremlin Workshop objective.
Moment: Throughout Gremlin's Workshop
Includes: Ring model/texture; inactive/powered states; motion used during final restoration.
Group: 01 — Core Network Kit
For: The three visible milestones the player brings back to life.
Requirement: Create one reusable ring mechanism used as Ring 1, Ring 2, and Ring 3 with clearly readable Inactive and Powered states. The three instances must remain distinguishable by position/label while sharing one visual grammar. The final state must support all three rings operating together as the Great Orrery restoration payoff.
Usage: Sequential milestones in Objective 4 and the ending transition.

### UI & Information

#### Workshop Entrance Message
Flow: 01 — Wake Ring One
Function: Tells the player to carry power from the Generator through all three rings.
Type: UI / TEXT
Create: Create the exact player-facing Workshop Entrance Message.
Used: When the player enters the Gremlin Workshop.
Moment: Entering Gremlin's Workshop
Group: 02 — Workshop Intro
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
Function: Shows one current power state for each Orrery ring: POWERED or NO POWER.
Type: UI / TEXT
Create: Create the exact player-facing Orrery Ring Status.
Used: Throughout the Gremlin Workshop objective.
Moment: Throughout Gremlin's Workshop
Group: 01 — Core Network Kit
For: Show which Orrery rings currently have power.
Requirement: Use simple in-world state words and update from actual connectivity.
Content:
```text
RING 1 · POWERED
RING 1 · NO POWER

RING 2 · POWERED
RING 2 · NO POWER

RING 3 · POWERED
RING 3 · NO POWER
```

#### Route Swap Message
Flow: 03 — Gremlin Changes the Path
Function: Tells the player the old route is blocked and another route is open.
Type: UI / TEXT
Create: Create the exact player-facing Route Swap Message.
Used: Immediately after Gremlin changes the route.
Moment: Gremlin Changes the Route
Group: 03 — Gremlin Route Swap
For: Tell the player Gremlin blocked the old path and opened another.
Requirement: Do not explain the route solution or implementation state.
Content:
```text
GREMLIN'S WORK

Your old path is blocked.
Another way has opened.

Find it and bring Ring Two back to life.
```

#### Ring One Power-Loss Message
Flow: 04 — First Rollback
Function: Tells the player Ring One lost power after Gremlin's sabotage.
Type: UI / TEXT
Create: Create the exact player-facing Ring One Power-Loss Message.
Used: When the first sabotage makes Ring One lose power.
Moment: Ring One Loses Power
Group: 04 — First Sabotage
For: Tell the player Ring One has gone dark after Gremlin's sabotage.
Requirement: Do not expose percentages, rotator counts, positions, or internal connection names.
Content:
```text
RING ONE LOST POWER

Gremlin knocked the power line out.
Restore Ring One.
```

#### Ring Two Power-Loss Message
Flow: 05 — Second Rollback
Function: Tells the player Ring Two lost power after Gremlin's sabotage.
Type: UI / TEXT
Create: Create the exact player-facing Ring Two Power-Loss Message.
Used: When the second sabotage makes Ring Two lose power.
Moment: Ring Two Loses Power
Group: 05 — Second Sabotage
For: Tell the player Ring Two has gone dark after Gremlin strikes again.
Requirement: Do not expose percentages, rotator counts, positions, or internal connection names.
Content:
```text
RING TWO LOST POWER

Gremlin struck the power line again.
Restore Ring Two.
```

### Visual Effects & Presentation

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
Visual Brief: Distinct reward item shown at the end of the map.
Function: Reward item shown after the vault is restored.
Type: ITEM
Create: Create one Clockwork Wayfinder reward item/model.
Used: During the final reward reveal.
Moment: Vault Restored
Includes: Reward item/model appearance; readable reward reveal state.
Group: 01 — Finale
For: The cosmetic reward presented at the end of the story.
Requirement: Create one cosmetic completion reward object with a distinct Clockwork-Vault silhouette and a clear reward-reveal presentation. It does not provide new gameplay power and must support one-time grant/readability in the ending scene.
Usage: Presented after the Great Orrery restoration and granted exactly once through the existing ending flow.

### UI & Information

#### Vault Restored Message
Flow: 02 — The Way Home
Function: Confirms the vault is restored and points the player to the open gateway.
Type: UI / TEXT
Create: Create the exact player-facing Vault Restored Message.
Used: When the return gateway is open.
Moment: Way Home
Group: 01 — Finale
For: Confirm the restored vault and point the player toward the open gateway.
Requirement: Keep the ending message fully in-world.
Content:
```text
THE CLOCKWORK VAULT IS RESTORED

The gateway is open.
Follow the light home.
```

### Visual Effects & Presentation

