# The Clockwork Vault Voice Requirements

Source PRD revision: 1.0.0
Voice system: Custodian Vex · direct in-world guide across the vault; no radio/communicator layer

## 01. The Antechamber

### VO-ANTE-01 — Vault Restoration Briefing
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The assigned player enters the protected Antechamber and Vex activates for the first time.
- Purpose: Establish why the player is trapped, what the Great Orrery means to the vault, that four connected systems must be restored, and that the Custodian Key begins the route forward.
- Must communicate:
  - The entrance will not reopen on its own.
  - The vault protects the Great Orrery.
  - Four connected systems must be restored in sequence.
  - The Custodian Key opens the first mechanism rather than the exit.
  - Restoring the vault creates the way home.
- Must not add/repeat:
  - Do not introduce an extra tutorial puzzle or warm-up objective.
  - Do not imply the Custodian Key directly opens the exit.
  - Do not explain later objective mechanics in detail during the opening briefing.
- Source refs:
  - content.md → 02 Gameplay Flow → The Journey Begins
  - content.md → 04 The Antechamber → Gameplay Overview
  - content.md → 04 The Antechamber → Developer → Briefing State

### VO-ANTE-02 — Custodian Key Reminder
- Type: Direct NPC Dialogue
- Function: reminder
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: After the opening briefing, the player misses the key/seal interaction or returns from a local interruption before the Resonance Engine seal is opened.
- Purpose: Repeat only the minimum actionable onboarding cue without replaying the story briefing.
- Must communicate:
  - Take the Custodian Key.
  - Use it on the marked Resonance Engine seal.
- Must not add/repeat:
  - Do not replay the vault history or four-objective briefing.
  - Do not imply a fail state or consume the key before valid seal activation.
- Source refs:
  - content.md → 04 The Antechamber → Gameplay Information → Fail Condition
  - content.md → 04 The Antechamber → Developer → Briefing State

## 02. The Resonance Engine

### VO-RES-01 — Find the Missing Combination
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Resonance Engine seal opens and the player gains control inside the reset chamber while the partial door display shows Middle = Brown and the other target fields remain unknown.
- Purpose: Explain how to approach the deduction puzzle without revealing the hidden Left/Right colors, pulse answer, or lever solution.
- Must communicate:
  - The door display already reveals Middle = Brown.
  - The scattered books provide clues for the missing Left and Right colors and which pillar must pulse.
  - The books have no required reading order and the player does not need every book to solve the puzzle.
  - The player should test each pillar’s upper/lower lever combinations and read the immediate lamp feedback to learn how to produce the needed colors.
  - Completion requires all three live pillar states to match the hidden combination together.
- Must not add/repeat:
  - Do not reveal Left = Orange, Right = Purple, or Pulse = Left.
  - Do not reveal the final lever ON/OFF combinations.
  - Do not explain all twelve lever-to-color mappings.
  - Do not imply all twelve books must be found or read.
- Source refs:
  - content.md → 02 Gameplay Flow → The Resonance Engine
  - content.md → 05 The Resonance Engine → Gameplay Overview
  - content.md → 05 The Resonance Engine → Developer → Books and Experimentation

## 03. The Broken Gallery

### VO-GAL-01 — Read the Routes and Supplies
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player enters Broken Gallery Level 1 with the checkpoint barrels available and the three route choices visible.
- Purpose: Establish the repeated route-reading/resource loop without revealing which authored routes are viable.
- Must communicate:
  - Search the checkpoint barrels for the current level’s construction resources.
  - Use blocks and ladders only at marked placement positions.
  - Inspect the three routes and spend the limited resources carefully.
  - If the active attempt fails from resource exhaustion or level-time expiry, only the current level resets while earlier completed levels remain complete.
- Must not add/repeat:
  - Do not reveal that Level 1 middle/right or Level 2 right are the viable answers.
  - Do not describe free-form building as valid.
  - Do not introduce the old Custodian Key, Spring Column, or Anchor Ring mechanics.
  - Do not imply a full-objective restart after a local retry.
- Source refs:
  - content.md → 02 Gameplay Flow → The Broken Gallery
  - content.md → 06 The Broken Gallery → Gameplay Overview
  - content.md → 06 The Broken Gallery → Developer → Level 1 / Level 2 Runtime

### VO-GAL-02 — Level 3 Gremlin Threshold
- Type: Direct NPC Dialogue
- Function: warning
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Broken Gallery Level 3 becomes active, all three routes are initially viable, and the authored progress threshold begins for the player’s chosen route.
- Purpose: Make the Level 3 timing rule and route-loss consequence understandable without choosing a route for the player.
- Must communicate:
  - All three Level 3 routes are initially viable.
  - Choose one route and reach at least 50% progress before the authored threshold.
  - Missing the threshold closes the failed route for that run while an alternative remains and returns the player to Checkpoint 3 for another attempt.
- Must not add/repeat:
  - Do not identify which route the player should choose.
  - Do not invent a numeric threshold duration that the PRD does not define.
  - Do not imply death or a restart of Levels 1–2.
- Source refs:
  - content.md → 02 Gameplay Flow → The Broken Gallery → Level 3 — Gremlin Time Challenge
  - content.md → 06 The Broken Gallery → Gameplay Flow → Level 3 — Beat the Gremlin Threshold
  - content.md → 06 The Broken Gallery → Developer → Timed Route State / Route Failure and Recovery

## 04. The Warden Halls

### VO-WARD-01 — Echo Pebble and Trap Rules
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Warden Level 1 activates and the player receives the unlimited Echo Pebble before the first trap sequence.
- Purpose: Explain the approved Pebble scope, cooldown, laser-disable window, and the distinction between laser solutions and hazards that must be avoided or timed.
- Must communicate:
  - Echo Pebble supply is unlimited, but every throw starts a 3-second cooldown before the next throw.
  - Hitting an authored wall-laser sensor disables that laser for 4 seconds of game-time.
  - At selected laser encounters, an authored hanging stone can be hit so it blocks the beam.
  - Floor traps cannot be disabled by the Pebble and must be avoided.
  - Swinging ceiling axes cannot be disabled by the Pebble and must be crossed by timing their movement.
- Must not add/repeat:
  - Do not claim floor traps can be disabled by Echo Pebble.
  - Do not claim swinging axes can be disabled by Echo Pebble.
  - Do not imply Pebble ammunition is limited.
  - Do not change the 3-second cooldown or 4-second laser-disable duration.
- Source refs:
  - content.md → 02 Gameplay Flow → The Warden Halls
  - content.md → 07 The Warden Halls → Gameplay Overview
  - content.md → 07 The Warden Halls → Developer → Echo Pebble

### VO-WARD-02 — The Wardens Still Serve
- Type: Main Story
- Function: transition
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player clears the third Warden level, reaches the inner gate, and the route toward Gremlin’s Workshop opens.
- Purpose: Connect the still-active security system to the vault’s story and frame the Workshop as the next destination without rebriefing trap mechanics.
- Must communicate:
  - The Wardens never stopped protecting the Great Orrery.
  - Their continued activity shows that parts of the vault are still functioning.
  - The player should continue to the Workshop.
- Must not add/repeat:
  - Do not replay Echo Pebble instructions.
  - Do not claim the Great Orrery is already restored.
  - Do not reveal the Workshop sabotage before it happens.
- Source refs:
  - content.md → 02 Gameplay Flow → The Warden Halls → Transition
  - content.md → 07 The Warden Halls → Gameplay Flow → Reach the Inner Gate

## 05. The Gremlin’s Workshop

### VO-WORK-01 — Build One Continuous Network
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player enters the Workshop and the authored L-rotator network becomes interactive with the Generator and Ring 1–3 visible.
- Purpose: Establish the 90-degree L-rotator grammar and cumulative Generator → Ring 1 → Ring 2 → Ring 3 objective without revealing the authored route.
- Must communicate:
  - Power starts at the Generator.
  - Every rotator is an L-shaped junction connecting exactly two orthogonal directions.
  - Rotate junctions to build one continuous powered network to Ring 1, then extend that same live network to Ring 2 and Ring 3.
  - Earlier links must remain connected; losing an upstream link removes downstream power.
- Must not add/repeat:
  - Do not describe the obsolete 3×3 Straight/Elbow/Split board.
  - Do not reveal exact route coordinates, blocker positions, or rotator orientations.
  - Do not imply each ring is a separate reset puzzle.
- Source refs:
  - content.md → 02 Gameplay Flow → The Gremlin’s Workshop
  - content.md → 08 The Gremlin’s Workshop → Gameplay Overview
  - content.md → 08 The Gremlin’s Workshop → Developer → Rotator Solver / Ring Progression

### VO-WORK-02 — Route Swap Reaction
- Type: Direct NPC Dialogue
- Function: setback_recovery
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: About 20 seconds after Ring 1 and Ring 2 are connected, the Gremlin route-swap event blocks the previous active route and opens the authored alternate route.
- Purpose: Make the visible route swap unmistakable and direct the player to reroute without changing the learned L-rotator rule or revealing the solution.
- Must communicate:
  - The route previously used to reach Ring 2 is now blocked.
  - A previously blocked alternate route has opened.
  - The L-rotator connection rule has not changed.
  - Reroute through the newly available path and restore the Generator → Ring 1 → Ring 2 network.
- Must not add/repeat:
  - Do not claim the blocked route can still conduct power.
  - Do not introduce a new or reversed rotator rule.
  - Do not identify the exact solution sequence.
- Source refs:
  - content.md → 02 Gameplay Flow → The Gremlin’s Workshop → First Gremlin Sabotage — Route Swap
  - content.md → 08 The Gremlin’s Workshop → Developer → Post-Ring-2 Sabotage

### VO-WORK-03 — First Rollback Reaction
- Type: Direct NPC Dialogue
- Function: setback_recovery
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Validated Ring 2 → Ring 3 progress reaches 50% and the Gremlin rotates exactly two previously correct rotators on the Generator → Ring 1 connection, interrupting the earlier powered network.
- Purpose: Tell the player which earlier network section was disrupted and that it must be repaired before final completion.
- Must communicate:
  - The Generator → Ring 1 connection has been knocked out of alignment.
  - The player must return to that earlier section and repair the affected rotators.
  - The routing grammar has not changed.
- Must not add/repeat:
  - Do not reveal the exact required orientations.
  - Do not identify the affected rotators by technical coordinates.
  - Do not imply the sabotage is permanent or requires a new connection rule.
- Source refs:
  - content.md → 02 Gameplay Flow → The Gremlin’s Workshop → Level 3 — Ring 2 to Ring 3 with Rollback Events
  - content.md → 08 The Gremlin’s Workshop → Developer → 50% Progress Sabotage

### VO-WORK-04 — Second Rollback Reaction
- Type: Direct NPC Dialogue
- Function: setback_recovery
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Validated Ring 2 → Ring 3 progress reaches 80% and the Gremlin rotates exactly three previously correct rotators on the Ring 1 → Ring 2 connection, interrupting the earlier powered network.
- Purpose: Tell the player that the second earlier network section has been disrupted and must be repaired before Ring 3 can complete.
- Must communicate:
  - The Ring 1 → Ring 2 connection has been knocked out of alignment.
  - The player must repair that earlier section and restore continuous power before completing Ring 3.
  - The routing grammar has not changed.
- Must not add/repeat:
  - Do not reveal the exact required orientations.
  - Do not identify the affected rotators by technical coordinates.
  - Do not imply the sabotage is permanent or introduce a different rule.
- Source refs:
  - content.md → 02 Gameplay Flow → The Gremlin’s Workshop → Level 3 — Ring 2 to Ring 3 with Rollback Events
  - content.md → 08 The Gremlin’s Workshop → Developer → 80% Progress Sabotage

## 06. Vault Restored

### VO-END-01 — The Vault Is Awake
- Type: Main Story
- Function: completion
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: All three Orrery rings remain powered, the Great Orrery restoration callbacks complete, and the closing scene reaches Vex recognition.
- Purpose: Resolve Vex’s story, name what the player accomplished, acknowledge that the vault was restored rather than merely escaped, and present the Clockwork Wayfinder reward.
- Must communicate:
  - The Great Orrery and connected vault systems are restored.
  - The player restored what the vault was built to protect rather than merely finding an exit.
  - The gateway is open.
  - The player receives the Clockwork Wayfinder as the completion reward.
- Must not add/repeat:
  - Do not expose Objective Scores or platform analysis.
  - Do not introduce a fifth objective or new challenge.
  - Do not imply the reward can be granted repeatedly.
- Source refs:
  - content.md → 02 Gameplay Flow → The Vault Awakens
  - content.md → 09 Vault Restored → Gameplay Flow → Vex Recognition / Reward and Save
  - content.md → 09 Vault Restored → Developer → Reward and Session Save

### VO-END-02 — Safe Return Cue
- Type: Main Story
- Function: farewell
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Session result and reward state are secured and the safe return route to the holding area opens.
- Purpose: Give one concise final navigation cue and close Vex’s guide role without adding more story exposition.
- Must communicate:
  - The gateway/return route is open.
  - Follow it back to the holding area.
  - The restoration journey is complete.
- Must not add/repeat:
  - Do not replay the completion speech or reward explanation.
  - Do not introduce another gameplay task.
  - Do not claim lane reset is complete before the player has safely returned.
- Source refs:
  - content.md → 02 Gameplay Flow → The Vault Awakens → Leaving the Clockwork Vault
  - content.md → 09 Vault Restored → Gameplay Flow → Return and Reset
