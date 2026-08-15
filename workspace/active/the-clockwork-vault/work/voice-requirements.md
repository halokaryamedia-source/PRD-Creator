# The Clockwork Vault Voice Requirements

Source PRD revision: 1.0.0
Voice system: Custodian Vex · direct in-world primary guide across the vault; Gremlin · direct in-world mischievous taunts during Objective 4; no radio/communicator layer

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
  - content.md → The Antechamber

## 02. The Resonance Engine

### VO-RES-01 — Find the Missing Combination
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Resonance Engine seal opens and the player gains control inside the reset chamber with the partial door display visible.
- Purpose: Explain the partial-display and clue-search loop without revealing the hidden target colors, pulse location, or lever solutions.
- Must communicate:
  - The door display already reveals Middle = Brown.
  - Search the scattered books in any order for the missing colors and pulse information.
  - Reading every book is not required.
  - Test each pillar's upper/lower lever combinations and watch immediate lamp feedback.
  - Make all three pillar states match the inferred final combination.
- Must not add/repeat:
  - Do not say Left = Orange, Right = Purple, or Pulse = Left.
  - Do not state any lever-to-color solution.
  - Do not imply the books form a required sequence.
- Source refs:
  - content.md → The Resonance Engine
  - REQ-002
  - REQ-014
  - REQ-015

## 03. The Broken Gallery

### VO-GAL-01 — Read the Routes and Supplies
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player enters Broken Gallery Level 1 with the three routes, checkpoint barrels, and marked repair positions available.
- Purpose: Establish the repeated route-reading and limited-resource loop without revealing which route is viable.
- Must communicate:
  - Search checkpoint barrels for the current level's supplies.
  - Blocks and ladders may be placed only on marked gaps/positions.
  - Inspect the routes before spending limited resources.
  - A failed active level resets locally rather than restarting the whole Gallery.
- Must not add/repeat:
  - Do not reveal the viable route for Level 1 or Level 2.
  - Do not introduce Spring Column, Anchor Ring, or Custodian Key carrying.
  - Do not imply free-form building.
- Source refs:
  - content.md → The Broken Gallery
  - REQ-003

### VO-GAL-02 — Level 3 Gremlin Threshold
- Type: Direct NPC Dialogue
- Function: warning
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Level 3 begins with all three routes active and the player is about to commit to one route under the authored progress threshold.
- Purpose: Make the 50-percent requirement and route-loss consequence clear before the timed attempt.
- Must communicate:
  - All three Level 3 routes are initially viable.
  - Choose one route and reach at least halfway before the threshold expires.
  - Missing the threshold closes that failed route while another alternative remains.
  - Failure returns the player to Checkpoint 3 for another attempt.
- Must not add/repeat:
  - Do not name a preferred route.
  - Do not imply full-objective restart.
  - Do not imply a closed route reopens during the same run unless the gameplay state explicitly does so.
- Source refs:
  - content.md → The Broken Gallery → Level 3
  - REQ-004

## 04. The Warden Halls

### VO-WARD-01 — Echo Pebble and Trap Rules
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Warden Halls activate and the player receives the unlimited Echo Pebble before the first trap-family encounters.
- Purpose: Explain valid Pebble targets, cooldown, laser-disable duration, hanging-stone option, and which hazards must instead be avoided or timed.
- Must communicate:
  - Echo Pebble supply is unlimited with a 3-second cooldown between throws.
  - A valid wall-laser sensor hit disables that laser for 4 seconds of game-time.
  - Some authored hanging stones can be struck to block a laser beam.
  - Floor traps cannot be disabled with Pebble.
  - Swinging axes cannot be disabled with Pebble and must be timed.
- Must not add/repeat:
  - Do not imply the Pebble disables floor traps.
  - Do not imply the Pebble disables swinging axes.
  - Do not prescribe one mandatory strategy for every laser encounter.
- Source refs:
  - content.md → The Warden Halls
  - REQ-005

### VO-WARD-02 — The Wardens Still Serve
- Type: Main Story
- Function: transition
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player clears the third Warden level, reaches the inner gate, and the route toward Gremlin's Workshop opens.
- Purpose: Connect the still-active security system to the vault's story and frame the Workshop as the next destination without replaying trap instructions.
- Must communicate:
  - The Wardens never stopped protecting the Great Orrery.
  - Parts of the vault remain functional.
  - Continue to the Workshop.
- Must not add/repeat:
  - Do not replay Echo Pebble instructions.
  - Do not claim the Great Orrery is already restored.
  - Do not reveal the Workshop sabotage sequence.
- Source refs:
  - content.md → The Warden Halls → Transition

## 05. The Gremlin’s Workshop

### VO-WORK-01 — Build One Continuous Network
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player enters the Workshop and L-rotator interaction becomes active on the unsabotaged network.
- Purpose: Explain the continuous Generator → Ring 1 → Ring 2 → Ring 3 routing rule without revealing authored route solutions.
- Must communicate:
  - Power begins at the Generator.
  - Each rotator is an L-shaped connection between two orthogonal sides.
  - Build one continuous powered route to Ring 1, then extend through Ring 2 and Ring 3.
  - Earlier connections must remain powered as the network grows.
- Must not add/repeat:
  - Do not describe a 3×3 Straight/Elbow/Split board.
  - Do not reveal an exact route.
  - Do not preview sabotage timing before it occurs.
- Source refs:
  - content.md → The Gremlin’s Workshop
  - REQ-007

### VO-GREM-01 — Route Swap Taunt
- Type: Direct NPC Dialogue
- Function: reveal
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: About 20 seconds after Ring 1 and Ring 2 are connected, the authored route swap visibly blocks the previous route and opens the alternate route.
- Purpose: Give the Gremlin a clear mischievous personality and make the sabotage feel intentional without becoming gameplay guidance.
- Must communicate:
  - The Gremlin deliberately caused the route disruption.
  - The Gremlin is pleased with the inconvenience.
- Must not add/repeat:
  - Do not tell the player which rotators to use.
  - Do not explain the alternate route; Vex owns recovery guidance.
  - Do not introduce a new routing rule.
- Source refs:
  - REQ-008
  - REQ-016
  - SRC-008

### VO-WORK-02 — Route Swap Reaction
- Type: Direct NPC Dialogue
- Function: setback_recovery
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Immediately after the route-swap sabotage is visible and Gremlin has made the disruption clear.
- Purpose: Explain the actionable recovery rule after the route swap.
- Must communicate:
  - The old route is blocked and a different route is now available.
  - The L-rotator rule itself has not changed.
  - Reroute and restore the continuous Generator → Ring 1 → Ring 2 network.
- Must not add/repeat:
  - Do not reveal the exact alternate solution path.
  - Do not imply the old route remains usable.
  - Do not introduce a new connector rule.
- Source refs:
  - content.md → The Gremlin’s Workshop → First Gremlin Sabotage
  - REQ-008

### VO-GREM-02 — First Rollback Taunt
- Type: Direct NPC Dialogue
- Function: reveal
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: During Ring 2 → Ring 3 progress, the 50-percent sabotage rotates two previously correct Generator → Ring 1 rotators and that earlier link loses power.
- Purpose: Let Gremlin gloat over the first rollback without explaining how to repair it.
- Must communicate:
  - Gremlin intentionally disturbed an earlier connection.
  - Gremlin is enjoying forcing the player backward.
- Must not add/repeat:
  - Do not state which exact two rotators changed.
  - Do not give repair instructions.
  - Do not imply Ring 3 progress itself is erased unless gameplay state says so.
- Source refs:
  - REQ-008
  - REQ-016
  - SRC-008

### VO-WORK-03 — First Rollback Reaction
- Type: Direct NPC Dialogue
- Function: setback_recovery
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Immediately after the 50-percent sabotage removes the Generator → Ring 1 connection.
- Purpose: Direct the player back to the damaged earlier connection using the same established rotator rule.
- Must communicate:
  - The Generator → Ring 1 connection is down.
  - Repair the rotators Gremlin changed.
  - The routing rule is unchanged.
  - Resume Ring 3 progress after restoring the earlier link.
- Must not add/repeat:
  - Do not solve the rotator orientations.
  - Do not introduce a new rule.
- Source refs:
  - content.md → The Gremlin’s Workshop → Level 3 Rollback Events
  - REQ-008

### VO-GREM-03 — Second Rollback Taunt
- Type: Direct NPC Dialogue
- Function: reveal
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: At 80-percent Ring 2 → Ring 3 progress, the second sabotage rotates three previously correct Ring 1 → Ring 2 rotators and that section loses power.
- Purpose: Escalate Gremlin's nuisance personality at the final rollback without duplicating Vex's recovery instructions.
- Must communicate:
  - Gremlin intentionally sabotaged the network again.
  - Gremlin expects the player to be frustrated by another rollback.
- Must not add/repeat:
  - Do not state the exact rotator solution.
  - Do not explain how to repair the link.
  - Do not invent another sabotage after this authored event.
- Source refs:
  - REQ-008
  - REQ-016
  - SRC-008

### VO-WORK-04 — Second Rollback Reaction
- Type: Direct NPC Dialogue
- Function: setback_recovery
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Immediately after the 80-percent sabotage removes power between Ring 1 and Ring 2.
- Purpose: Identify the affected earlier section and direct repair before final Ring 3 completion.
- Must communicate:
  - The Ring 1 → Ring 2 connection is down.
  - Repair the rotators Gremlin changed using the same rule.
  - Restore that section before completing Ring 3.
- Must not add/repeat:
  - Do not state exact correct orientations.
  - Do not introduce another routing rule.
- Source refs:
  - content.md → The Gremlin’s Workshop → Level 3 Rollback Events
  - REQ-008

### VO-GREM-04 — Outsmarted Reaction
- Type: Direct NPC Dialogue
- Function: completion
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: The final network validates Generator, Ring 1, Ring 2, and Ring 3 as continuously powered after all sabotage events and the Great Orrery restoration begins.
- Purpose: Give Gremlin one short defeated reaction that acknowledges the player outsmarted the sabotage before Vex owns the main completion scene.
- Must communicate:
  - Gremlin realizes the player successfully restored the full network despite the sabotage.
  - Gremlin is frustrated and gives up interfering with this completed attempt.
- Must not add/repeat:
  - Do not replace Vex's completion speech.
  - Do not claim Gremlin is killed or permanently removed from the world.
  - Do not introduce another objective or sabotage event.
- Source refs:
  - REQ-016
  - SRC-008

## 06. Vault Restored

### VO-END-01 — The Vault Is Awake
- Type: Main Story
- Function: completion
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: All three Orrery rings remain powered, the Great Orrery restoration callbacks complete, and the closing scene reaches Vex recognition.
- Purpose: Resolve Vex's story, name what the player accomplished, acknowledge that the vault was restored rather than merely escaped, and present the Clockwork Wayfinder reward.
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
  - content.md → The Vault Awakens

### VO-END-02 — Safe Return Cue
- Type: Main Story
- Function: farewell
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Session result and reward state are secured and the safe return route to the holding area opens.
- Purpose: Give one concise final navigation cue and close Vex's guide role without adding more story exposition.
- Must communicate:
  - The gateway/return route is open.
  - Follow it back to the holding area.
  - The restoration journey is complete.
- Must not add/repeat:
  - Do not replay the completion speech or reward explanation.
  - Do not introduce another gameplay task.
  - Do not claim lane reset is complete before the player has safely returned.
- Source refs:
  - content.md → The Vault Awakens → Leaving the Clockwork Vault
