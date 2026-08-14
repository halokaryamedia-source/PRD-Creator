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

### VO-RES-01 — Experiment Before the Target
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Resonance Engine seal opens and the player gains control inside the reset Engine chamber while the target display is still blank.
- Purpose: Invite safe experimentation and clue reading before directed solving without revealing the authored hidden mapping.
- Must communicate:
  - The player should read the clue books and test the available machine inputs.
  - Lever/plate experimentation is safe and produces readable feedback.
  - The player should learn the machine rule before chasing a target.
  - The target display will activate after the free-experimentation phase.
- Must not add/repeat:
  - Do not reveal a specific rule template or solution.
  - Do not claim the target is already active.
  - Do not introduce vanilla redstone knowledge.
- Source refs:
  - content.md → 02 Gameplay Flow → The Resonance Engine → Free Experimentation
  - content.md → 05 The Resonance Engine → Level Design → Design Flow → Observation Point
  - content.md → 05 The Resonance Engine → Developer → Free-Play and Targets

## 03. The Broken Gallery

### VO-GAL-01 — Carry the Key Across
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player enters the Broken Gallery after Resonance Engine completion and receives the fixed crossing kit plus Custodian Key.
- Purpose: Establish the immediate crossing goal and limited-resource mindset without spoiling the authored Checkpoint 3 collapse.
- Must communicate:
  - Carry the Custodian Key to the far pedestal.
  - Use the fixed construction supplies carefully.
  - Choose repairs/routes that can actually be completed with the available kit.
- Must not add/repeat:
  - Do not reveal the exact future collapse timing or segment before its warning begins.
  - Do not describe upper/lower/side as three separate progression tracks.
  - Do not introduce lethal failure wording.
- Source refs:
  - content.md → 06 The Broken Gallery → Gameplay Overview
  - content.md → 06 The Broken Gallery → Gameplay Flow → Survey the Crossing
  - content.md → 06 The Broken Gallery → Developer → Fixed Supply Kit

### VO-GAL-02 — Checkpoint 3 Collapse Warning
- Type: Direct NPC Dialogue
- Function: warning
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Checkpoint 3 is active and the authored short collapse-warning sequence begins while the player is crossing the final section.
- Purpose: Reinforce the live danger state and make immediate forward movement clear while visual warning remains the primary readable cue.
- Timing Constraint: Must complete within the short Checkpoint 3 warning sequence before the authored collapse resolves.
- Must communicate:
  - The current section is about to collapse.
  - Keep moving through the active crossing.
- Must not add/repeat:
  - Do not give a camera-direction instruction or name a hidden route.
  - Do not imply death or full-objective restart.
  - Do not announce collapse before Checkpoint 3 warning begins.
- Source refs:
  - content.md → 02 Gameplay Flow → The Broken Gallery → Checkpoint 3
  - content.md → 06 The Broken Gallery → Gameplay Flow → Checkpoint 3 — Collapse and Adapt
  - content.md → 06 The Broken Gallery → Developer → Checkpoint 3 Collapse

## 04. The Warden Halls

### VO-WARD-01 — Echo Pebble Rule Briefing
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Warden Halls layout activates and the player receives the unlimited Echo Pebble before the first trap-family sequence.
- Purpose: Explain the invented Echo Pebble rule and the critical difference between wall/floor traps and ceiling traps before combinations become complex.
- Must communicate:
  - Echo Pebble can disable wall and floor traps.
  - A valid disable lasts 4 seconds of game-time.
  - Ceiling traps cannot be disabled.
  - Ceiling hazards must be crossed by observing their cycle and timing movement.
- Must not add/repeat:
  - Do not imply the Pebble is consumed permanently.
  - Do not imply ceiling traps can be disabled or bypassed by the Pebble.
  - Do not prescribe one mandatory cautious/rush strategy.
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
- Trigger: The player clears the final security sequence, enters the inner gate, and the route toward Gremlin’s Workshop opens.
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

### VO-WORK-01 — Build One Live Network
- Type: Main Story
- Function: briefing
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player enters the Workshop and conduit interaction becomes active on the unsabotaged 3×3 grid.
- Purpose: Establish the invented conduit grammar at the level needed to begin Ring 1 and understand cumulative Ring 1→2→3 progression.
- Must communicate:
  - Rotate conduits so connected sides carry power from the Source Crystal.
  - Power Ring 1 first.
  - Extend the same live network to Ring 2 and Ring 3.
  - Previously powered rings must remain connected as the network grows.
- Must not add/repeat:
  - Do not describe vanilla redstone behavior.
  - Do not reveal the exact authored route or future sabotaged edge.
  - Do not imply each ring resets the previous solution.
- Source refs:
  - content.md → 02 Gameplay Flow → The Gremlin’s Workshop
  - content.md → 08 The Gremlin’s Workshop → Gameplay Flow → Learn the Grid and Power Ring 1
  - content.md → 08 The Gremlin’s Workshop → Developer → Conduit Solver / Ring Progression

### VO-WORK-02 — Gremlin Sabotage Reaction
- Type: Direct NPC Dialogue
- Function: setback_recovery
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: About 20 seconds after Ring 2 stabilizes, the scripted Gremlin event visibly breaks one authored active connection and input is briefly locked.
- Purpose: Make the external topology change unmistakable and immediately direct the player toward rerouting without changing the learned conduit rule.
- Timing Constraint: Must fit within the authored sabotage reaction/input-lock beat before normal conduit interaction resumes.
- Must communicate:
  - The Gremlin severed an active connection.
  - That broken connection is permanently unavailable for the rest of the run.
  - The conduit connection rule itself has not changed.
  - Reroute around the broken edge, restore lost power, and continue toward Ring 3.
- Must not add/repeat:
  - Do not imply the broken connection can be repaired.
  - Do not introduce a reversed or new conduit rule.
  - Do not identify a solution path that solves the reroute automatically.
- Source refs:
  - content.md → 08 The Gremlin’s Workshop → Gameplay Flow → Gremlin Sabotage
  - content.md → 08 The Gremlin’s Workshop → Developer → Scripted Connection Sabotage
  - content.md → 08 The Gremlin’s Workshop → Important Build Notes → Fault Must Be Unmissable

### VO-WORK-03 — Highlight-Only Assist
- Type: Direct NPC Dialogue
- Function: reminder
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The configured Workshop assist threshold is reached and Vex highlights one useful node, connection, or region without changing the board.
- Purpose: Direct attention to the authored highlight while preserving player ownership of the solution.
- Must communicate:
  - Look at the highlighted area/connection.
  - The highlight is a clue, not an automatic solution.
  - The player still needs to complete the route.
- Must not add/repeat:
  - Do not rotate a node or state an exact completed route.
  - Do not claim the highlighted area is the entire solution.
  - Do not change Ring 2/3 automatically.
- Source refs:
  - content.md → 02 Gameplay Flow → The Gremlin’s Workshop → Transition / Vex assist
  - content.md → 08 The Gremlin’s Workshop → Developer → Vex Assist

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
