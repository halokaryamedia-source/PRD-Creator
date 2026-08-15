# Production Asset Requirements

## Global / Shared Assets

### 3D Models

#### Custodian Vex
Requirement: Create or reuse one Clockwork-compatible Custodian Vex NPC presentation for all required story, briefing, warning, reminder, and ending moments. Vex must remain visually recognizable across the complete journey and support readable idle, speaking, pointing/highlight, alert, and completion-reaction states without changing gameplay rules.
Usage: Shared across the Antechamber, Objectives 1-4, and the ending wherever canonical Voice Production is triggered.

#### Gremlin
Requirement: Create one small Clockwork Gremlin character used for authored sabotage moments. It needs a readable mischievous traversal/arrival state and a clear sabotage action that can be synchronized with route blocking, rotator changes, and the relevant warning presentation. It does not require navigation AI; authored movement is sufficient.
Usage: Used for the Objective 2 final time-challenge framing and the Objective 4 sabotage sequences.

## The Antechamber

### 3D Models

#### Custodian Key
Requirement: Create one clearly readable key item for the opening progression. It needs available/picked-up/accepted states and must visually belong to the Clockwork Vault rather than resemble an ordinary reward item.
Usage: Presented on the Antechamber pedestal and accepted by the Resonance Engine seal.

### UI & Information

#### First Objective Prompt
Requirement: Create one concise player-facing prompt that appears after the opening briefing and remains available until the first seal is opened.
Content:
```text
TAKE THE CUSTODIAN KEY
Use it on the marked Resonance Engine seal.
```

### Visual Effects & Presentation

#### First Seal Activation
Requirement: Create one short authored activation presentation for valid Custodian Key use: the seal acknowledges the key, the Objective 1 door visibly unlocks, and the route into the Resonance Engine becomes unmistakable. Keep the sequence short enough that it functions as a handoff rather than a cutscene.
Usage: Runs once after valid Antechamber completion.

## The Resonance Engine

### UI & Information

#### Objective 1 Instruction Panel
Requirement: Create one persistent or easily re-readable instruction panel explaining the complete player action without revealing any lever-to-color solution. The top/bottom lever reading order and the pressure-plate steady/blinking function must be explicit.
Content:
```text
MATCH ALL THREE PILLARS

1. Find and read the clue books.
2. Set each pillar's TOP and BOTTOM levers.
3. Use the pressure plate to switch STEADY / BLINKING.
4. Match the target shown near the exit.

Lever order is read TOP → BOTTOM.
```

#### Three-Pillar Target Display
Requirement: Create one player-readable target display near the exit showing the required state for all three pillars. Each target must communicate the required color and whether that pillar must be STEADY or BLINKING. The display must not expose the lever combination itself.
Usage: Visible throughout active Objective 1 solving and switches to a completed/confirmed state only when all three pillar outputs match.

#### Pillar State Labels
Requirement: Give each of the three puzzle pillars a stable player-readable identity such as LEFT, MIDDLE, and RIGHT so clue books, target information, and live machine outputs cannot be confused. The live lamp must make color and steady/blinking state readable at the same time.
Usage: Remains visible throughout Objective 1.

#### Pillar Clue Book Set
Requirement: Produce twelve short clue-book paragraphs, four per pillar, that teach the lever-to-color mapping indirectly but clearly enough for a light deduction puzzle. Keep each book to one short paragraph. The current prepared wording assumes the provisional list-order combination-to-color pairing recorded in the gameplay revision review and must be updated if that pairing is corrected.
Content:
```text
RIGHT PILLAR — RED
When both brass handles stand raised, the eastern lens burns the color of hot iron.

RIGHT PILLAR — YELLOW
When both eastern handles rest low, the lens settles into a warm harvest-gold.

RIGHT PILLAR — GREEN
Raise the upper eastern handle and leave the lower asleep; the lens answers in fresh green.

RIGHT PILLAR — PURPLE
Let the upper eastern handle rest and raise only the lower; the glass deepens to royal violet.

MIDDLE PILLAR — BLUE
When both center handles stand raised, the middle lens clears to the blue of open sky.

MIDDLE PILLAR — DARK BLUE
Lower both center handles and the middle lens sinks into a midnight blue.

MIDDLE PILLAR — BROWN
Raise the upper center handle while the lower rests; the lens takes the color of old wood.

MIDDLE PILLAR — DARK GREEN
Leave the upper center handle low and raise the lower; the lens turns the deep green of moss.

LEFT PILLAR — PINK
When both western handles stand raised, the left lens glows a soft rose-pink.

LEFT PILLAR — ORANGE
When both western handles rest low, the left lens warms to ember-orange.

LEFT PILLAR — WHITE
Raise only the upper western handle; the left lens clears to bright white.

LEFT PILLAR — BLACK
Leave the upper western handle low and raise the lower; the left lens falls almost black.
```

### Visual Effects & Presentation

#### Pillar Interaction Feedback
Requirement: Every valid lever change must produce immediate readable lamp feedback on its own pillar, and every pressure-plate interaction must visibly switch that pillar between steady and blinking without changing its selected color. When all three required states match, run one concise confirmation response before opening the next route.
Usage: Active throughout Objective 1 and reset completely for the next run.

#### Resonance Engine Restoration
Requirement: Create one short completion presentation that visually confirms all three pillars have synchronized and the Engine has returned to operation, then directs attention toward the newly opened Broken Gallery route.
Usage: Runs once after valid Objective 1 completion.

## The Broken Gallery

### UI & Information

#### Objective 2 Instruction Panel
Requirement: Create one concise instruction panel explaining the repeatable loop shared by the three route levels: search barrels, repair only marked gaps, and reach the next checkpoint. It must explain that failed attempts reset only the current level.
Content:
```text
CROSS THE BROKEN GALLERY

SEARCH BARRELS → REPAIR MARKED GAPS → REACH THE CHECKPOINT

Blocks and ladders can only be placed on marked positions.
If a route runs out of resources or time, this level resets and you can try again.
```

#### Level 1 Brief
Requirement: Show the Level 1 rules without revealing which two routes are viable.
Content:
```text
LEVEL 1 · EASY
Three routes. Two can be completed.
A viable crossing needs 12 blocks.
Choose carefully and reach the next checkpoint.
```

#### Level 2 Brief
Requirement: Show the Level 2 resource requirement without revealing that the right route is the viable answer.
Content:
```text
LEVEL 2 · MEDIUM
Three routes. Only one can be completed.
Crossing supply: 20 blocks + 3 ladders.
Place them only on marked positions.
```

#### Level 3 Time-Challenge Brief
Requirement: Clearly explain that all three routes are initially valid in Level 3, but the chosen route must reach at least 50% progress before the authored time threshold. Explain the consequence without revealing route geometry.
Content:
```text
LEVEL 3 · GREMLIN TIME CHALLENGE
All three routes can work.
Reach 50% of your chosen route before the timer expires.
If you fail, that route closes and you return to Checkpoint 3.
```

#### Route Failure Message
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
Requirement: Create one consistent player-readable marker treatment for every position where a bridge block or ladder is allowed. The marker must distinguish legal placement from ordinary environment blocks without revealing which full route is viable.
Usage: Present only on authored placement positions and restored with each current-level reset.

### Audio

#### Level 3 Time-Challenge Cue
Requirement: Create one independent short warning cue that clearly marks the start of the Level 3 progress deadline. It should read as Gremlin-triggered urgency and remain distinct from normal checkpoint, placement, or route-reset sounds.
Usage: Plays when the Level 3 authored timer begins; Voice Production may play alongside it but is owned separately.

### Visual Effects & Presentation

#### Level Retry Reset
Requirement: Create one brief readable reset presentation for failed Level 1/2 attempts: temporary placed blocks/ladders are removed, the player returns to the current checkpoint, and the resource-search loop visibly becomes available again. Avoid presenting this as a full objective failure.
Usage: Runs only for the current level that failed.

#### Gremlin Route-Closed Event
Requirement: Create one Level 3 failure presentation in which the selected failed route changes to a clearly unavailable state, the player returns to Checkpoint 3, and the two remaining active routes stay readable. The Gremlin framing and warning cue may be synchronized inside this authored sequence.
Usage: Can occur once per chosen Level 3 route until the player succeeds or the available route set is exhausted by the authored recovery rules.

## The Warden Halls

### 3D Models

#### Echo Pebble
Requirement: Create one small throwable pebble item, visually derived from a stone/snowball-scale projectile but clearly authored for the Clockwork Vault. It needs held/throw/projectile/valid-hit feedback and must support an unlimited-use loop with a visible 3-second cooldown. Its impact feedback must distinguish a valid wall-laser sensor or hanging-stone target from an invalid floor/axe target.
Usage: Granted for Objective 3 and removed/reset at objective exit.

#### Wall Laser Sensor
Requirement: Create one readable wall-mounted laser sensor/beam assembly with Active and Temporarily Disabled states. The sensor must be an obvious Echo Pebble target; disabling it must visibly interrupt the beam long enough for the player to understand the safe window. Attached activation/deactivation VFX and SFX remain part of this asset.
Usage: Distributed across the three Warden levels.

#### Laser Blocker Stone
Requirement: Create one authored hanging-stone target for selected laser encounters. A valid Echo Pebble hit must cause the stone to move/drop into the beam path and visibly block the laser, creating a readable alternate solution without changing unrelated traps.
Usage: Used only at authored laser encounters that support the blocker-stone solution.

#### Swinging Axe Trap
Requirement: Create one large double-sided swinging axe trap mounted from the ceiling. It needs a clearly readable left-right swing cycle, safe timing windows, contact/knockback feedback, and a reset state. It must never appear to accept Echo Pebble disable input.
Usage: Distributed across the Warden levels as a timing hazard.

### UI & Information

#### Objective 3 Instruction Panel
Requirement: Create one concise instruction panel that distinguishes Pebble-valid hazards from timing/avoidance hazards and states the 3-second cooldown.
Content:
```text
SURVIVE THE WARDEN HALLS

ECHO PEBBLE
• Wall laser sensors: Disable them temporarily.
• Marked hanging stones: Knock them into a laser beam.
• Floor traps: AVOID.
• Swinging axes: TIME YOUR MOVEMENT.

Pebbles are unlimited · 3 sec cooldown per throw.
```

#### Echo Pebble Cooldown Indicator
Requirement: Create one compact player-facing cooldown indicator that appears after a throw and clearly returns to READY after 3 seconds. It must not imply that the player has a limited pebble count.
Content:
```text
ECHO PEBBLE · READY
ECHO PEBBLE · RECHARGING
```

#### Trap Warning Readability
Requirement: Give wall lasers, floor traps, and swinging axes distinct warning language/icons or in-world markers where additional information is needed. Never mark floor traps or swinging axes as Pebble-disableable.
Usage: Used only where the physical hazard alone would not be sufficiently readable.

### Visual Effects & Presentation

#### Trap Hit Feedback
Requirement: Create clear but compact feedback for each approved hazard consequence so the player can identify which trap hit them and understand the resulting temporary impairment. Laser, floor, and axe hits must remain distinguishable while avoiding screen obstruction during active traversal.
Usage: Triggered on valid hazard contact together with the approved damage/status effects.

#### Checkpoint Recovery
Requirement: When trap damage reduces gameplay health to zero, present one quick checkpoint recovery that returns the player to the active Warden level without replaying earlier completed levels. Restore player control only after the checkpoint position is safe.
Usage: Runs on Objective 3 hazard defeat only.

## The Gremlin's Workshop

### 3D Models

#### Power Generator
Requirement: Create one central power-source machine with clearly different Offline, Live, and Power-Interrupted feedback. The output direction into the routing network must remain visually readable from the puzzle area. Attached startup/interruption SFX and energy VFX remain part of this asset.
Usage: Source of the Objective 4 continuous power network.

#### 90-Degree Rotator Junction
Requirement: Create one reusable L-shaped power junction that rotates in 90-degree steps and connects exactly two orthogonal directions. It needs four readable orientations plus Powered and Unpowered visual states. Interaction must make the route direction legible without referring to the separate technical grid document.
Usage: Repeated at authored Objective 4 junction locations.

#### Orrery Ring
Requirement: Create one reusable ring mechanism used as Ring 1, Ring 2, and Ring 3 with clearly readable Inactive and Powered states. The three instances must remain distinguishable by position/label while sharing one visual grammar. The final state must support all three rings operating together as the Great Orrery restoration payoff.
Usage: Sequential milestones in Objective 4 and the ending transition.

### UI & Information

#### Objective 4 Instruction Panel
Requirement: Create one instruction panel explaining the continuous network rule without exposing route coordinates or the technical layout solution.
Content:
```text
CONNECT THE POWER

Generator → Ring 1 → Ring 2 → Ring 3

Rotate the L-junctions to turn the power route.
Keep every earlier ring connected as you continue.
```

#### Ring Progress Display
Requirement: Create one compact player-facing or in-world status treatment showing which rings currently have power. It must update from actual connectivity rather than milestone history so a Gremlin disruption can visibly remove power from an earlier ring.
Content:
```text
RING 1 · POWERED / OFFLINE
RING 2 · POWERED / OFFLINE
RING 3 · POWERED / OFFLINE
```

#### First Sabotage Message
Requirement: Explain the post-Ring-2 route swap without identifying the alternate-route solution.
Content:
```text
GREMLIN SABOTAGE
The previous route is blocked.
A different path has opened.
Reroute the power and restore the connection.
```

#### 50% Sabotage Message
Requirement: Tell the player exactly which earlier network section lost alignment and how many rotators were changed, without identifying their positions.
Content:
```text
POWER LOST · GENERATOR → RING 1
Two rotators were turned.
Repair the earlier connection, then continue toward Ring 3.
```

#### 80% Sabotage Message
Requirement: Tell the player which second earlier network section lost alignment and how many rotators were changed, without identifying their positions.
Content:
```text
POWER LOST · RING 1 → RING 2
Three rotators were turned.
Restore the connection, then finish Ring 3.
```

### Visual Effects & Presentation

#### Ring 2 Route-Swap Sabotage
Requirement: About 20 seconds after Ring 1 and Ring 2 are connected, run one authored Gremlin sequence that makes the previously active route become visibly blocked, makes the previously blocked alternate path visibly available, removes power where connectivity is broken, and then returns control for rerouting. The change must be understandable without exposing grid coordinates or route labels from the technical HTML.
Usage: Runs once per Objective 4 session after the approved Ring 2 condition.

#### 50% Rotator Sabotage
Requirement: At the approved 50% Ring 2-to-Ring 3 progress trigger, run one short Gremlin disruption in which exactly two already-correct rotators on the Generator-to-Ring-1 connection visibly turn out of alignment. Power loss must propagate to the affected ring states before normal input resumes.
Usage: Runs once per Objective 4 session.

#### 80% Rotator Sabotage
Requirement: At the approved 80% Ring 2-to-Ring 3 progress trigger, run one short Gremlin disruption in which exactly three already-correct rotators on the Ring-1-to-Ring-2 connection visibly turn out of alignment. The player must see that an earlier completed section has broken before normal input resumes.
Usage: Runs once per Objective 4 session.

#### Great Orrery Restoration
Requirement: When Generator, Ring 1, Ring 2, and Ring 3 are continuously connected, create one strong final restoration presentation: all three rings synchronize, power visibly reaches the Great Orrery, puzzle input closes, and the Clockwork exit begins opening. Keep the transition compatible with the existing ending sequence rather than creating a fifth objective.
Usage: Runs once on valid Objective 4 completion.

## Vault Restored

### 3D Models

#### Clockwork Wayfinder
Requirement: Create one cosmetic completion reward object with a distinct Clockwork-Vault silhouette and a clear reward-reveal presentation. It does not provide new gameplay power and must support one-time grant/readability in the ending scene.
Usage: Presented after the Great Orrery restoration and granted exactly once through the existing ending flow.

### UI & Information

#### Completion Message
Requirement: Create one concise completion message confirming that the restoration journey is finished and directing the player toward the reopened return route without exposing platform scoring.
Content:
```text
THE CLOCKWORK VAULT IS RESTORED
The gateway is open.
Follow the return route home.
```

### Visual Effects & Presentation

#### Vault Awakening and Exit Reveal
Requirement: Create one coordinated closing presentation that carries restored power from the Great Orrery into the surrounding vault, reveals the reopened exit, frames Vex's closing moment and Clockwork Wayfinder reward, then hands control to the safe return route. This sequence must remain reset-owned and must not introduce another challenge.
Usage: Runs after Objective 4 completion and before the player returns to the holding area.
