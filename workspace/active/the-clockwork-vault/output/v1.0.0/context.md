# The Clockwork Vault — Development Context

PRD Version: v1.0.0
Status: handoff_ready

## Reading Guidance

- Use this document as the current accepted product context for development.
- A newer explicitly approved change overrides only the affected context; preserve unrelated accepted meaning.
- Existing, legacy, template, or unused implementation is evidence, not automatic product authority.
- Use `index.json` first and read only the relevant `context.md` line ranges plus any directly related scope.
- Prefer the smallest complete implementation and reuse an existing owner only when it has the same responsibility.
- Do not add abstraction, fallback, migration, or compatibility behavior without a current need.
- If implementation requires a new product decision, surface it instead of inventing it.

## Accepted PRD

### Gameplay & Development Specification

- Document Type: Adventure Map
- Version: 1.0.0
- Language: English

### 01. Overview

The Clockwork Vault is a solo adventure set inside a sealed ancient machine complex. Guided by Custodian Vex, the player restores four connected systems—Resonance Engine, Broken Gallery, Warden Halls, and the Great Orrery—so the century-sealed gateway can reopen. The journey focuses on learning invented rules, recovering from readable setbacks, and seeing the vault visibly return to life.

- **Session Model:** Solo · 1 player per isolated lane
- **Target Playtime:** ≈45 minutes total
- **Game Structure:** Introduction → 4 Objectives → Ending

#### Complete Gameplay Journey

1. **The Antechamber** — Meet Custodian Vex, learn why the vault is sealed, obtain the Custodian Key, and open the first objective chamber.
2. **The Resonance Engine** — Use six levers and a pressure plate to match three crystal states, using books around the chamber as puzzle clues.
3. **The Broken Gallery** — Cross three checkpoints using upper, lower, and side route variations while managing limited construction materials and adapting to the final collapse.
4. **The Warden Halls** — Cross three increasingly complex trap checkpoints using the Echo Pebble to temporarily disable selected wall and floor traps while timing ceiling hazards.
5. **The Gremlin’s Workshop** — Connect all three Great Orrery rings, then recover when a Gremlin destroys one active power connection after Ring 2.
6. **The Vault Awakens** — Awaken the Great Orrery, reopen the century-sealed gateway, complete the story, and return safely.

#### Global Gameplay Direction

- **Learn Inside the Vault** — Each mechanic teaches its own rule. Outside redstone or crafting knowledge is not required.
- **Consistent Challenges** — Puzzle states, trap cycles, collapse events, and Gremlin sabotage behave predictably for every run.
- **Always Recoverable** — Mistakes may cost time, resources, or position, but no objective creates an unwinnable state.
- **Visible Restoration** — Each completed objective visibly restores another part of the Clockwork Vault.
- **Vex Guides the Journey** — Custodian Vex explains transitions, reacts to setbacks, and connects every chamber to the Great Orrery restoration.

### 02. Gameplay Flow

#### The Journey Begins

The player discovers the Clockwork Vault beneath forgotten ruins and crosses its entrance before understanding that the gateway opens only once every hundred years.

- **From Forgotten Ruins to the Sealed Vault**
  - The player discovers the Clockwork Vault beneath forgotten ruins and crosses its ancient entrance. The gate immediately seals behind them, trapping the player inside a place caught in a century-long restoration cycle. In the Antechamber, Custodian Vex awakens and explains that the vault was not built to hide treasure; it was built to protect the Great Orrery. The machine has been dormant for centuries, and the entrance cannot reopen until its connected mechanisms are restored in sequence.
- **The Custodian’s Warning**
  - Custodian Vex explains that previous visitors attempted the same journey but never restored the full system. Every chamber controls a necessary part of the vault: power distribution, access through the collapsed inner gallery, the ancient security halls, and the final network feeding the Great Orrery. The player must proceed because no other exit exists.
- **Beginning the Restoration**
  - The journey then proceeds through four gameplay objectives—Resonance Engine, Broken Gallery, Warden Halls, and Gremlin’s Workshop—before the restored Orrery opens the ending sequence.
- **Transition:** Vex directs the player to the central pedestal. Taking the Custodian Key activates the first seal and reveals the entrance to the Resonance Engine. From this point forward, every completed objective visibly awakens another section of the vault.

#### The Antechamber

The Antechamber is a protected lobby and narrative introduction where the player first meets Custodian Vex.

- **Discovering the Clockwork Vault**
  - The Antechamber is a protected lobby and narrative introduction where the player first meets Custodian Vex. The room establishes the vault’s history, the century-sealed entrance, the failure of the Great Orrery, and the only possible route to freedom. The player is not tested here; the purpose is to establish motivation and make the complete journey understandable before Objective 1 begins.
- **Receiving the Custodian Key**
  - A central pedestal holds the Custodian Key. Vex explains that the key is not the exit key; it grants access to the first mechanism that must be restored. The pedestal, the sealed entrance behind the player, and the Objective 1 gate must remain visible within the same composition so the player understands where they came from and where they must go.
- **Opening the First Objective**
  - After the briefing, the player takes the Custodian Key from the central pedestal and uses it on the Resonance Engine seal. The keyed gate opens and hands control directly into Objective 1.
- **Transition:** When the player takes the Custodian Key and uses it on the first vault seal, the Resonance Engine door opens. Vex gives a concise objective briefing and the story moves from mystery into action.

#### The Resonance Engine

The player enters a compact puzzle chamber with six levers, one pressure-plate submission, three crystal outputs, a physically visible but initially blank target display, and authored clue books.

- **Free Experimentation**
  - The player enters with all machine elements visible. Vex demonstrates that the levers and pressure plate are safe to use without revealing the hidden mapping. The target display is present but remains blank/inactive.
  - For approximately 90 seconds of game-time, the player can read clues and test inputs freely. Every valid interaction produces immediate crystal light/sound feedback and the complete panel state remains readable.
- **Target 1 Appears**
  - After the free-play phase, Target 1 appears with a clear chime. The player compares the required Dark, Glowing, and Pulsing states with the observed machine behavior, adjusts the six lever configuration, and submits using the pressure plate. Incorrect submissions stay visible and can be revised immediately.
- **Target 2 Requires the Learned Rule**
  - When Target 1 is confirmed, Target 2 appears. The second target must require the player to apply the distinguishing rule learned from clues/experimentation rather than repeat the first configuration. The objective remains recoverable until confirmation or the station deadline.
- **Restoring the Resonance Engine**
  - Target 2 confirmation locks the completed Engine state, records the raw input/state and target timing evidence, activates the vault response, and opens the Broken Gallery transition. The platform calculates the Objective Score; the map does not display or export it.
- **Transition:** The Broken Gallery opens after Target 2 confirmation and the Resonance Engine boundary record is secured.

#### The Broken Gallery

The player enters a vast collapsed gallery with three route families: upper, lower, and side.

- **Checkpoint 1 — Choosing a Viable Route**
  - The player enters a vast collapsed gallery with three route families: upper, lower, and side. None is fully intact. Building materials are collected near the starting checkpoint and must be used to repair gaps, missing stairs, broken ladders, or disconnected platforms. During Phase 1, two routes are valid and can reach Checkpoint 1, allowing the player to compare route readability and material cost.
- **Phase 2 — Finding the Single Correct Continuation**
  - After Checkpoint 1, the gallery narrows into another three-route decision, but only one route can be completed with the available materials. The other routes provide visible warning signs and consume resources if chosen carelessly. The player must inspect the damage, estimate the required repairs, and commit before exhausting the limited kit. Checkpoint 2 secures progress and provides the final controlled material allocation.
- **Checkpoint 3 — Crossing Before the Route Collapses**
  - Beyond Checkpoint 2, the final crossing becomes unstable. A visible warning sequence starts, and the player must move efficiently through the authored repairs. Around 50% of Checkpoint 3 progress, the current segment resolves into its collapsed/sealed state from a safe event position. The player then uses the remaining recovery connector/route to continue. Failure or a fall returns the player to the nearest valid checkpoint/ledge with the final-phase state recoverable; the full objective does not restart.
- **Placing the Custodian Key**
  - After the recovery crossing, the player reaches the far pedestal and places the Custodian Key. The Gallery records checkpoint progress, resource state, collapse response, resupply use, and completion before opening the Warden Halls.
- **Transition:** The Warden Halls open after the Custodian Key is accepted by the far pedestal and the Gallery completion record is secured.

#### The Warden Halls

The Warden Halls are a controlled security corridor containing wall sensors, floor traps, and ceiling traps.

- **Phase 1 — Learning the Three Trap Families**
  - The Warden Halls are a controlled security corridor containing wall sensors, floor traps, and ceiling traps. Each type has a distinct silhouette, warning cue, active state, and non-lethal consequence. The player receives an Echo Pebble that can disable wall and floor traps for a 4-second game-time window. Ceiling traps cannot be disabled and must be passed through observation and timing.
- **Phase 2 — Combining Trap Types**
  - After the first checkpoint, wall, floor, and ceiling hazards begin appearing in combinations. Echo Pebble use creates a 4-second safe window on valid wall/floor targets, so the player must disable the correct trap, read the remaining active hazard, and move before the disabled trap recovers. Failure costs time or returns the player to the nearest safe checkpoint.
- **Phase 3 — Crossing the Final Security Sequence**
  - The final phase uses denser combinations and shorter decision windows while preserving the same established rules. The player must choose when to use the Echo Pebble, when to wait, and when to move through an unavoidable ceiling cycle. The difficulty increases through composition, not by introducing unexplained trap behavior.
- **Reaching the Inner Vault**
  - After the final trap sequence, the player reaches the protected Records Room. The hall completion state is recorded and the route toward Gremlin’s Workshop opens.
- **Transition:** After the final trap sequence, the player reaches the inner gate and the entrance to the Gremlin’s Workshop. Vex confirms that the Wardens never stopped protecting the Orrery; the still-active defence system proves that the vault has continued performing its purpose throughout the centuries.

#### The Gremlin’s Workshop

The final chamber contains the Source Crystal, the Great Orrery, three target rings, and a 3×3 grid of rotatable conduit nodes.

- **Connecting Ring 1**
  - The final chamber contains the Source Crystal, the Great Orrery, three target rings, and a 3×3 grid of rotatable conduit nodes. Every conduit has visible connection sides and rotates in 90-degree steps. Power travels only through sides that physically connect. The player first creates one valid route from the Source Crystal to Ring 1.
- **Connecting Ring 2 and Surviving the Sabotage**
  - Ring 2 must be connected while Ring 1 remains powered, requiring the player to build a cumulative network rather than replace the first solution. After Ring 2 stabilizes, a Gremlin visibly crosses the board and destroys one active conduit connection between the Source Crystal and an already powered ring. The damaged connection is permanently marked and cannot conduct power again during the run.
- **Rebuilding and Extending the Network**
  - The sabotage interrupts the active network. The player must rotate the remaining conduits to establish a new valid route from the Source Crystal, restore the disconnected ring, preserve the other active ring, and then extend the network to Ring 3. The final challenge is therefore not a reversed pipe rule; it is a cumulative rerouting problem with one known connection permanently unavailable.
- **Restoring the Great Orrery**
  - When all three rings are powered at the same time, the Great Orrery enters its restored state. Puzzle input closes and the controlled Vault Restored ending begins.
- **Transition:** The objective completes only when Ring 1, Ring 2, and Ring 3 are powered simultaneously. The Great Orrery begins rotating, energy returns throughout the vault, and the ending sequence starts. If the player reaches the configured assist threshold, Vex may highlight a valid connection without rotating the board automatically; the player still completes the route.

#### The Vault Awakens

When all three rings remain powered, the Great Orrery begins turning for the first time in centuries.

- **Awakening the Great Orrery**
  - When all three rings remain powered, the Great Orrery begins turning for the first time in centuries. Energy travels backward through every completed chamber: the Resonance crystals synchronize, gallery guide lights return, the Warden systems enter standby, and the century-sealed entrance begins unlocking. The ending visually confirms that the player restored one connected machine rather than completing unrelated challenges.
- **Resolving the Custodian’s Story**
  - Custodian Vex thanks the player and acknowledges that the vault was never waiting for someone merely to escape; it was waiting for someone capable of restoring it. The player receives the Clockwork Wayfinder reward after the completion record has been saved.
- **Leaving the Clockwork Vault**
  - After the result and Clockwork Wayfinder reward state are secured, the player follows the safe return route to the Holding Area while the assigned lane begins cleanup and reset.
- **Transition:** The player exits through the reopened gateway as the Great Orrery continues operating behind them. The entrance closes gradually, not as another trap, but as the vault returns to its century-long cycle with its purpose restored. Temporary gameplay state is then cleared and the assigned lane is prepared for reuse.

### 03. Global Development

#### Development Overview

Build one isolated Clockwork journey per active player lane. Shared runtime systems own session start, transitions, pause, data, interruption, and reset, while each objective owns its local mechanic and completion state.

##### Development Flow

- **Foundation Setup** — Prepare isolated lanes, holding area, start gate, transitions, shared identifiers, and reset ownership.
- **Shared Systems** — Implement Vex, game-time, pause, inventory, permissions, feedback, data boundaries, and platform score inputs.
- **Station Integration** — Connect Introduction, four objectives, ending, and all station-boundary saves in fixed story order.
- **Verification and Reuse** — Validate parity across lanes, no cross-lane leakage, complete event delivery, and reset under 30 seconds.

##### Development Requirements

###### Production Foundation
- **Lane Architecture**
  - Requirement: Use one player per lane and five station cells plus ending space.
  - Requirement: Prevent visual, audio, entity, particle, and state leakage between lanes.
  - Requirement: Start the session only when the player exits the holding-area gate.
  - Result: Defines safe parallel ownership for school sessions.
- **Story and Navigation**
  - Requirement: Keep fixed order: Antechamber → Resonance → Gallery → Warden → Workshop → Ending.
  - Requirement: Use one-way corridors for briefing, cleanup, boundary save, and next-station activation.
  - Result: Maintains one coherent adventure and clean state boundaries.
###### Shared Contracts
- **Deterministic Treatment**
  - Requirement: Use authored template/layout selection and fixed event dose.
  - Requirement: Do not randomize collapse, traps, fault timing, or rule effects at runtime.
  - Result: Keeps player conditions comparable and verifiable.
- **Input and Accessibility**
  - Requirement: Support keyboard, controller, and touch equally.
  - Requirement: Use simple interactions, no combat, no death, no precision parkour, and no vanilla-knowledge dependency.
  - Result: Preserves the target experience for students aged 9–14.
###### Delivery and QA
- **Data and Scoring Boundary**
  - Requirement: Emit raw timestamped events only.
  - Requirement: Provide enough evidence for platform-side objective scoring without showing or sending final score from the map.
  - Result: Separates gameplay implementation from platform interpretation.
- **Reset and Readiness**
  - Requirement: Reset every lane in under 30 seconds.
  - Requirement: Test pause, interruption, rejoin, timeout, completion, multi-lane load, and no-leakage behavior.
  - Result: Makes the map ready for back-to-back use.

##### Important Development Notes

- **Lane Isolation** — Every active player owns one isolated lane; visual, audio, entity, particle, and gameplay state must not leak between lanes.
- **Deterministic Objectives** — Authored targets, trap cycles, collapse behavior, and Gremlin sabotage remain reproducible across equivalent lanes.
- **Score Boundary** — The map emits raw gameplay evidence; Objective Scores are calculated outside the Minecraft experience.
- **Reusable Lane** — A lane returns to service only after objective, ending, inventory, entity, timing, and temporary-block state are verified clean.

#### Game System

The shared runtime controls lane ownership, objective order, Custodian Vex, game-time, pause, inventory, permissions, transitions, and interruption handling. Objective mechanics plug into this lifecycle without changing its global rules.

##### Development Flow

- **Session and Lane Setup** — Assign one player, initialize lane ownership, and keep the holding area isolated until the start gate.
- **Station Lifecycle** — Run briefing → active → complete/timeout/interrupted → transition with one authoritative station state.
- **Pause and Persistence** — Freeze game-time, player input, and scheduled events; save every boundary and interruption.
- **Ending and Release** — Complete the session, deliver reward/data, return to lobby, and release the lane only after reset verification.

##### Development Requirements

###### Session Ownership
- **Holding Area and Start**
  - Requirement: Contain players until they use the start gate.
  - Requirement: Start master/session game-time only after lane entry.
  - Requirement: Prevent early visibility of active stations.
  - Result: Absorbs uneven classroom joins without shortening gameplay.
- **Lane Isolation**
  - Requirement: Own players, entities, effects, sounds, particles, scoreboards, timers, and temporary blocks by lane.
  - Requirement: Reject cross-lane interaction and clean lane-owned objects at every boundary.
  - Result: Prevents another player’s event from spoiling or changing the experience.
###### Guide and Interaction
- **Custodian Vex**
  - Requirement: Use one persistent guide per lane with short externalized dialogue.
  - Requirement: Pair every instruction with demonstration or highlight.
  - Requirement: Do not reveal hidden rules before experimentation.
  - Result: Provides instruction, tone, and blameless setback reactions.
- **Inventory and Permissions**
  - Requirement: Clear and grant station-specific inventory at entry.
  - Requirement: Apply scripted break/place/interact permissions only to current station targets.
  - Requirement: Remove permissions/items at exit, interruption, and reset.
  - Result: Prevents map damage and cross-station state leakage.
###### Timing and Events
- **Game-Time and Pause**
  - Requirement: Own all timers and scheduled events in script game-time.
  - Requirement: Pause player/camera input, timers, trap cycles, collapse, and fault at exact state.
  - Requirement: Keep absolute session hard caps according to the approved session rule.
  - Result: Makes pause deterministic without real-time drift.
- **Setback Feedback**
  - Requirement: Use telegraph → impact → Vex reaction for Gallery collapse, trap consequences, and Gremlin fault.
  - Requirement: Ensure visual treatment carries meaning when audio is muted.
  - Result: Makes external setbacks readable and memorable.
###### Station Lifecycle
- **Boundary and Transition**
  - Requirement: Save station data, clear temporary state, close the previous route, brief the next station, and activate only after entry is safe.
  - Requirement: Complete, timeout, and interruption must use distinct exit reasons.
  - Result: Creates reliable station boundaries.
- **Rejoin Behavior**
  - Requirement: Save partial data immediately on disconnect.
  - Requirement: Mark station interrupted and restart that station from initial state on rejoin while preserving completed objective results.
  - Result: Protects data without resuming into an invalid temporary state.

##### Important Development Notes

- **Script-Owned Timing** — Use Script API / scoreboard-owned timing rather than redstone clocks for objective lifecycle and scheduled events.
- **Fixed Authored Rules** — Adaptive tiering does not rewrite Clockwork puzzle or hazard rules in this version.
- **Localization Ready** — Keep in-game strings externalized so localized copy can be added without changing gameplay logic.
- **Concurrent Lane Test** — Shared systems must remain isolated and stable with all supported lanes active together.

#### Data and Reset

Each objective records the raw gameplay events needed to reconstruct its result. Data is saved at objective boundaries and interruptions; the assigned lane is released only after temporary state is cleared, authored structures are restored, and readiness checks pass.

##### Development Flow

- **Capture** — Record session, station, action, state, dose, pause, completion, timeout, and interruption events.
- **Persist and Send** — Buffer safely, save at boundaries, and retry delivery without duplicate semantic events.
- **Clear Runtime State** — Remove inventory, permissions, entities, particles, scheduled tasks, temporary blocks, and lane properties.
- **Restore and Verify** — Reload structures, restore defaults, run readiness checks, then release the lane.

##### Development Requirements

###### Event Contract
- **Common Envelope**
  - Requirement: Every event carries anonymous session ID, map ID, station ID, lane ID, build version, event name, and game-time timestamp.
  - Requirement: Do not send player name, gamertag, device identifier, platform interpretation, or final map-side score.
  - Result: Provides consistent anonymous event ownership.
- **Objective Payloads**
  - Requirement: Record the exact action and complete resulting state needed to reconstruct Resonance and Workshop behavior.
  - Requirement: Record route/resource, trap/strategy, event dose, pause, completion, timeout, and interruption fields where required.
  - Result: Provides platform scoring evidence without aggregation in-world.
###### Persistence and Delivery
- **Boundary Save**
  - Requirement: Save and send at station exit, disconnect, ending, and session end.
  - Requirement: Use idempotent event IDs or sequence numbers to prevent duplicate delivery after retry.
  - Result: Prevents loss and duplication.
- **Timing Rules**
  - Requirement: Use game-time timestamps; pause freezes gameplay timing.
  - Requirement: Record scripted event dose exactly, including route collapsed, trap instance, and connection sabotaged.
  - Result: Allows fair timing and treatment verification.
###### Reset Contract
- **Script Cleanup**
  - Requirement: Cancel scheduled callbacks; clear station state, UI, effects, entities, items, permissions, scoreboards, and lane dynamic properties.
  - Requirement: Remove any player-placed or temporary blocks before structure restore.
  - Result: Prevents stale runtime logic.
- **Structure Restore and Verification**
  - Requirement: Restore all station cells and ending states from approved structures.
  - Requirement: Verify doors, targets, items, guide, timers, event flags, chosen variants, and player state.
  - Requirement: Release lane only after all readiness checks pass within 30 seconds.
  - Result: Guarantees pristine reuse.
###### Failure Recovery
- **Interrupted Sessions**
  - Requirement: Preserve partial data and mark incomplete.
  - Requirement: On rejoin, restart the interrupted station and retain earlier completed objective results.
  - Result: Protects evidence while avoiding corrupted temporary state.
- **Delivery or Reset Failure**
  - Requirement: Queue failed data sends for retry and keep semantic IDs stable.
  - Requirement: Keep a lane unavailable when reset verification fails and surface a technical error for staff.
  - Result: Prevents silent data loss and unsafe reuse.

##### Important Development Notes

- **Objective-Owned Payloads** — Each objective emits only the raw fields needed to reconstruct its gameplay result and treatment state.
- **Raw Data Stays Raw** — Platform scoring or interpretation never changes the event payload produced by the map.
- **Reset Is Runtime-Critical** — A lane is not reusable until cleanup and structure restoration complete within the approved reset target.
- **No State Carryover** — Selected layouts, templates, fault state, inventory, temporary blocks, and objective flags must not survive reset.

#### Gameplay Development

Every playable area follows the same lifecycle: prepare a clean area, activate its mechanic after safe entry, validate completion and save the result, then clear temporary state before handing the player to the next objective.

##### Development Flow

- **Prepare Area** — Restore the objective area, set lane ownership, grant required inventory/permissions, and present the next clear player goal.
- **Run Mechanic** — Activate only the current objective, own its game-time, feedback, setback/recovery behavior, and lane-local state.
- **Complete and Save** — Validate the objective end condition once, record the required raw result evidence, and freeze the completed state for transition.
- **Transition and Restore** — Move the player through the safe handoff, remove temporary state, and restore the previous objective for reuse.

##### Development Requirements

###### Objective Lifecycle
- **Activation and Ownership**
  - Requirement: Activate a mechanic only after the assigned player reaches its safe entry state.
  - Requirement: Keep timers, entities, effects, inventory, permissions, and temporary objects owned by the active lane/objective.
  - Requirement: Do not activate the next objective until the current handoff is complete.
  - Result: Only one objective controls the player at a time.
- **Completion and Handoff**
  - Requirement: Validate the approved end condition once.
  - Requirement: Freeze or close the completed mechanic before transition.
  - Requirement: Save the objective result at the boundary, then open the next safe route.
  - Result: Progression cannot duplicate, skip, or overlap objective states.
###### Player Readability
- **Goal and Feedback**
  - Requirement: Present one clear immediate goal when an objective becomes active.
  - Requirement: Pair important interactions or setbacks with visible feedback; audio may reinforce but not replace meaning.
  - Requirement: Use Custodian Vex for concise instruction and transition framing.
  - Result: Players can understand what changed and what to do next.
###### Data and Interruption
- **Boundary Save**
  - Requirement: Record raw gameplay evidence required by the current objective.
  - Requirement: Pause script-owned timing during pause.
  - Requirement: On interruption, keep completed objective results and restart the interrupted objective from a clean state.
  - Result: Partial sessions remain recoverable without corrupting previous progress.
###### Reset and Reuse
- **Objective Cleanup**
  - Requirement: Clear temporary inventory, permissions, callbacks, effects, entities, player-placed blocks, and objective-local flags.
  - Requirement: Restore authored structures and initial mechanic state.
  - Requirement: Release the lane only after readiness verification succeeds.
  - Result: Every objective can be replayed from the same authored starting state.

##### Important Development Notes

- **Single Active Objective** — Only the current objective may own active gameplay input, timers, and temporary state.
- **Boundary Save** — Completion and interruption both create explicit boundary records before state changes.
- **Platform Scoring** — Minecraft records raw evidence; Objective Scores remain platform-side.
- **Journey Verification** — The complete journey must pass end-to-end and concurrent-lane testing before handoff.

### 04. The Antechamber

**Introduction**

#### Gameplay Overview

**Context:** The player enters the protected Antechamber and meets Custodian Vex. A central pedestal holds the Custodian Key, and the Resonance Engine seal is the visible next destination.

**Main Objective:** Listen to Vex’s briefing, collect the Custodian Key, and use it on the Resonance Engine seal.

**Result:** The seal opens and the Resonance Engine becomes accessible. The Antechamber creates no Objective Score.

##### Gameplay Information

- **Game Purpose:** Establish story, navigation, pickup/use interaction, and the next destination without adding a separate warm-up minigame.
- **Gameplay Time:** Approximately 3 minutes.
- **Starting Condition:** The player leaves the holding area in Adventure mode with the assigned lane active and the Antechamber reset.
- **End Condition:** The Custodian Key is accepted by the Resonance Engine seal and the objective door opens.
- **Fail Condition:** There is no lethal or permanent fail state. If the key interaction is missed or interrupted, Vex repeats the cue and the key/seal state remains recoverable.
- **Scoring Criteria:** No Objective Score. Completion is recorded as story progression only.

##### Gameplay Flow

- **Arrive and Meet Vex** — Enter the protected lobby and receive the short vault-restoration briefing.
- **Read the Destination** — See the central pedestal, Custodian Key, and sealed Resonance Engine entrance as the only next objective.
- **Collect the Custodian Key** — Take the key from the pedestal and receive immediate pickup confirmation.
- **Open the Resonance Seal** — Use the key on the marked seal; invalid interaction gives a local cue without consuming the key.
- **Enter Objective 1** — The seal opens, the transition state is saved, and the player proceeds to the Resonance Engine.

#### Level Design

Build a compact protected entry lobby that frames Vex, the Great Orrery/vault context, the central Custodian Key pedestal, and the Resonance Engine seal as one readable onboarding path. Keep the onboarding focused on the approved briefing, key pickup, seal interaction, and transition.

##### Design Flow

- **Arrival** — Frame Vex and the sealed-vault context from the player spawn.
- **Briefing Focus** — Keep the next route visually quiet while Vex establishes the restoration objective.
- **Key Pedestal** — Place the Custodian Key on a clear central pedestal between the player and the first seal.
- **First Seal** — Reveal the Resonance Engine entrance as the direct visual handoff after the key is used.

##### Build Requirements

###### Story and Route
- **Protected Entry Lobby** — Area: Compact authored lobby
  - Build/Visual: Provide a safe spawn/briefing zone with no competing gameplay.
  - Build/Visual: Keep Vex, Great Orrery context, key pedestal, and first seal readable from the intended route.
  - Gameplay Function: Establishes the story and next objective without navigation ambiguity.
- **Custodian Vex Position** — Area: Visible from spawn
  - Build/Visual: Give Vex a stable presentation point outside the player collision path.
  - Build/Visual: Leave enough space for dialogue-facing camera/readability without locking movement.
  - Gameplay Function: Provides the narrative guide and objective cue.
###### Key and Seal
- **Custodian Key Pedestal** — Area: Central interaction point
  - Build/Visual: Make the key distinct from decoration and reachable without precision movement.
  - Build/Visual: Use a clear empty/collected visual state.
  - Gameplay Function: Introduces the protected objective item and pickup interaction.
- **Resonance Engine Seal** — Area: End of onboarding route
  - Build/Visual: Use one obvious keyed interaction surface and a visible locked/open state.
  - Build/Visual: Do not add unrelated levers or tile puzzles around the seal.
  - Gameplay Function: Converts the key pickup into the first objective transition.
###### Transition and Reset
- **Objective Door / Corridor** — Area: Direct connection
  - Build/Visual: Reveal the Resonance Engine route only after valid seal activation.
  - Build/Visual: Prevent visibility into another player lane.
  - Gameplay Function: Hands the player into Objective 1.
- **Reset-Owned Props** — Area: Full Antechamber
  - Build/Visual: Keep key, seal, door, Vex presentation state, lights, audio, and markers inside lane reset ownership.
  - Gameplay Function: Returns the introduction to a clean reusable state.

##### Important Build Notes

- **No Extra Tutorial Puzzle** — The Antechamber teaches controls naturally through briefing, movement, pickup, and key use.
- **Touch Readability** — The key pedestal and seal interaction must remain obvious on touch-screen play.
- **Lane Isolation** — The route must not expose another lane or its effects.
- **Clear Handoff** — Opening the first seal is the visual and mechanical handoff to the Resonance Engine.

#### Developer

Implement the Vex story briefing, Custodian Key pickup, keyed seal validation, first objective-door opening, transition save, interruption recovery, and complete lane reset. No Objective Score is created.

##### Development Flow

- **Introduction Setup** — Initialize the lane, Vex, key pedestal, seal, objective door, permissions, and presentation state.
- **Briefing and Key** — Run the briefing cue, enable the key, validate pickup, and preserve the item through local recovery.
- **Seal and Handoff** — Validate key use once, open the Resonance Engine route, record transition events, and prevent duplicate activation.
- **Reset and Reuse** — Restore Vex, key, seal, door, cues, inventory permissions, and lane ownership for the next session.

##### Development Requirements

###### Introduction Runtime
- **Briefing State**
  - Requirement: Trigger Vex once when the assigned player enters the protected Antechamber.
  - Requirement: Allow movement during the briefing unless a short authored presentation lock is required.
  - Requirement: Repeat only the needed cue after interruption; do not replay completed steps unnecessarily.
  - Gameplay Function: The player receives one clear restoration objective and next destination.
- **Key Ownership**
  - Requirement: Spawn/enable one Custodian Key after the briefing start.
  - Requirement: Bind the key to the assigned session and prevent duplication or cross-lane transfer.
  - Requirement: If the key is dropped/lost by interruption, restore it to the valid local state.
  - Gameplay Function: The objective item remains reliable and session-owned.
###### Seal and Transition
- **Keyed Seal Validation**
  - Requirement: Accept only the assigned Custodian Key on the Resonance Engine seal.
  - Requirement: Consume or retire the temporary key only after successful validation.
  - Requirement: Ignore duplicate activations after the door-open state is committed.
  - Gameplay Function: The first objective opens exactly once.
- **Transition Recording**
  - Requirement: Record arrival, briefing completion, key pickup, seal activation, and objective-door opening with game-time timestamps.
  - Requirement: Save the transition boundary before granting Resonance Engine interaction permissions.
  - Gameplay Function: The introduction is reconstructable without creating a score.

##### Completion and Data

- **Antechamber Completion** — No Objective Score
  - Completion: The assigned Custodian Key is accepted by the first seal and the Resonance Engine door reaches its open/transition state.
  - Recorded Data: Arrival, briefing completion, key pickup, seal activation, objective-door opening, interruption state, and transition timestamp.
  - Incomplete Session: Before seal completion, restore the player to the latest valid onboarding state; after the transition save, do not replay or duplicate the completed introduction.
  - Duplicate Prevention: Key pickup, seal activation, and completion events are idempotent per session.
  - Final Result: The introduction contributes no Objective Score; it only establishes the four-objective journey.
  - Player-Facing Result: Show story/objective feedback only; do not show a score.
  - Telemetry / Export: Export raw onboarding and transition events only.

##### Reset / Interruption

- Restore the Custodian Key pedestal, seal, objective door, Vex state, markers, lights/audio, inventory, and permissions.
- Clear session-owned Antechamber flags only after the player leaves or the session is terminated.
- **Reset Result:** The Antechamber returns to its original protected onboarding state and is safe for the next assigned session.

##### Important Development Notes

- **Game-Time Ownership** — All authored delays use script-owned game-time and freeze with pause.
- **No Duplicate Handoff** — Seal activation and transition save execute once per session.
- **No Warm-Up Engine Dependency** — The introduction uses only the approved story, key pickup, seal interaction, and transition sequence.
- **Reset Before Reuse** — Lane availability is not advertised until key, seal, door, Vex, and permission states are verified clean.

##### Acceptance

- The Antechamber reaches its defined end condition without creating an unrecoverable player state.
- The Antechamber preserves the approved player-facing behavior, data/result boundary, and lane isolation rules.
- The Antechamber reset restores the authored starting state before the assigned lane is reused.

##### Terms

- **Custodian Vex** — The guide who explains the restoration journey and directs the player through the vault.
- **Custodian Key** — The protected objective item collected in the Antechamber and used to open the Resonance Engine seal.
- **Resonance Engine seal** — The keyed mechanism controlling access to Objective 1.
- **Great Orrery** — The central vault machine restored across the complete journey.

### 05. The Resonance Engine

**Objective 1**

#### Gameplay Overview

**Context:** A compact chamber contains six levers, one pressure-plate submission, three crystal outputs, clue books, and a target display. The display starts blank during free experimentation.

**Main Objective:** Experiment with the Engine, infer the authored lever-to-crystal rule, then match Target 1 and Target 2.

**Result:** Both targets are confirmed, the Resonance Engine activates, and the Broken Gallery route opens.

##### Gameplay Information

- **Game Purpose:** Teach that the vault’s invented systems must be learned through observation and experimentation before directed solving.
- **Gameplay Time:** Approximately 9 minutes; the first ~90 seconds are free experimentation before Target 1 appears.
- **Starting Condition:** The player enters with the Engine reset to one authored rule template, all six levers/three panels initialized, clue books available, and the target display blank/inactive.
- **End Condition:** Target 2 is held in the correct three-crystal state for the confirmation beat.
- **Fail Condition:** Incorrect submissions show the resulting crystal state and can be retried. At the station deadline, partial progress is recorded and the journey continues.
- **Scoring Criteria:** Objective Score 0–100 based on Target Completion, Free-Play Coverage, and Rule Application.

##### Gameplay Flow

- **Enter and Read the Machine** — See all six levers, the pressure plate, three crystal panels, the blank target display, and the clue books in one compact chamber.
- **Free Experimentation** — For about 90 seconds, test inputs freely and learn the mapping from immediate panel/light/sound feedback without a target being shown.
- **Match Target 1** — Target 1 appears with a chime; adjust the lever configuration and submit until the three crystal states match.
- **Match Target 2** — After Target 1 confirmation, show a second harder target that requires applying the learned rule rather than repeating the first solution.
- **Activate and Transition** — Confirm Target 2, lock the completed Engine state, save raw evidence, play the activation payoff, and open the Broken Gallery corridor.

#### Level Design

Build one compact observation chamber where the six lever inputs, pressure-plate submission, three crystal outputs, blank/active target display, and clue books can be read together. Walking must be negligible so difficulty comes from reasoning rather than navigation.

##### Design Flow

- **Observation Point** — Enter with every machine element visible and hear Vex invite free experimentation.
- **Input Cluster** — Test six levers, the plate, and the pressure-plate submission with immediate feedback.
- **Target Wall** — Read Target 1 and Target 2 beside the live crystal states.
- **Power Reveal** — Show the Great Hall receiving power and reveal the Custodian Key route.

##### Build Requirements

###### Engine Chamber
- **Observation Layout** — Area: Full station zone
  - Build/Visual: Build one compact chamber with every interactable within a few blocks.
  - Build/Visual: Place the three crystal panels on one continuous output wall opposite the player entry.
  - Build/Visual: Keep the target display adjacent to the output wall without covering live states.
  - Gameplay Function: Lets the player compare action and result without camera searching.
- **Input Stations** — Area: Fixed authored positions
  - Build/Visual: Place three clearly differentiated lever consoles in a consistent left-to-right order.
  - Build/Visual: Place the floor plate and weight pedestal inside the same observation space.
  - Build/Visual: Provide one marked valid area for the pressure-plate submission.
  - Gameplay Function: Creates a stable physical grammar for all six rule templates.
###### Feedback and State
- **Crystal Panels** — Area: Fixed authored positions
  - Build/Visual: Create Dark, Glow, and Pulse states with distinct shape/light treatment.
  - Build/Visual: Each panel must be readable independently with sound muted.
  - Build/Visual: Show state changes immediately, not through a delayed cinematic.
  - Gameplay Function: Makes every experiment interpretable.
- **Machine Feedback** — Area: Authored area
  - Build/Visual: Provide distinct per-panel sound, light, and motion responses.
  - Build/Visual: Use authored connection details that do not imply vanilla redstone logic.
  - Build/Visual: Show powered-vault feedback only after Target 2.
  - Gameplay Function: Supports hidden-rule discovery while preserving the fiction.
###### Transition and Reset
- **Target and Exit** — Area: Authored area
  - Build/Visual: Create a clearly readable two-stage target display.
  - Build/Visual: Frame the completion reveal toward the Great Hall and Broken Gallery route.
  - Build/Visual: Keep transition movement one-way.
  - Gameplay Function: Connects machine completion to the next story need.
- **Lane Reset** — Area: As required by lane
  - Build/Visual: Keep all lever, plate, weight, crystal, target, and FX anchors inside one reset volume.
  - Build/Visual: Provide stable identifiers/marker locations for all script-owned states.
  - Gameplay Function: Allows deterministic initialization and fast reuse.

##### Important Build Notes

- **Invented Logic Only** — Do not use real redstone layouts or familiar Minecraft logic as visual explanation.
- **Single Observation Space** — All interactables must be visible from the central observation space.
- **Recoverable Weight** — The weight must be easy to retrieve and impossible to lose outside its valid area.
- **One Physical Layout** — Six templates change logic only; the physical chamber remains identical.

#### Developer

Implement six equal-difficulty authored rule templates, immediate action-to-state feedback, a ~90-second free-play phase with a blank target display, sequential Target 1/Target 2 solving, platform-side scoring evidence, interruption handling, and full reset.

##### Development Flow

- **Mechanic Setup** — Select one authored rule template and initialize six lever states, three crystal outputs, clue sources, pressure-plate submission, and a blank target display.
- **Free Play and Targets** — Record free experimentation, reveal Target 1 after ~90 seconds, then reveal Target 2 only after Target 1 confirmation.
- **Completion and Data** — Validate target holds, store the complete input/state sequence, preserve timeout partial progress, and emit raw scoring evidence only.
- **Reset and Reuse** — Restore levers, panels, display, timer, clue state, items, Vex/presentation state, and permissions before lane reuse.

##### Development Requirements

###### Mechanic Setup
- **Template Engine**
  - Requirement: Store six pre-authored templates with equivalent tested difficulty.
  - Requirement: Select one template once at station initialization and record its ID.
  - Requirement: Keep the template fixed through pause and resume; reselect only after a full interrupted restart.
  - Gameplay Function: Provides controlled variation without nondeterministic rules.
- **Input and State Resolution**
  - Requirement: Accept only the six authored levers and the central pressure plate as valid puzzle inputs.
  - Requirement: Resolve the selected rule atomically and update the complete three-panel state before accepting the next input.
  - Requirement: Trigger distinct panel feedback for every changed state.
  - Gameplay Function: Guarantees clean action-to-result reconstruction.
###### Gameplay Setup
- **Free-Play and Targets**
  - Requirement: Keep the target display physically present but blank/inactive during the opening free-play phase. Allow clue inspection and input testing immediately; reveal Target 1 at approximately 90 seconds of game-time.
  - Requirement: Record the selected target-pattern ID and the moment the player first opens or reads each clue source.
  - Requirement: Confirm a target only after the complete pattern is held for the configured validation beat.
  - Requirement: Complete the objective after the authored final target is submitted and confirmed.
  - Gameplay Function: Preserves discovery before directed solving.
- **Weight and Invalid State**
  - Requirement: Allow one weight to be picked up, placed only on the marked plate area, and retrieved.
  - Requirement: Return invalid placements to the pedestal after a short clear response.
  - Requirement: Prevent duplicate, dropped, stored, or cross-station weight states.
  - Gameplay Function: Supports plate-dependent templates without item-loss dead ends.
- **Completion and Timeout**
  - Requirement: Complete after Target 2 confirmation; lock inputs, save data, and open the Gallery transition.
  - Requirement: At timeout, preserve Target 1/2 progress and final panel/input state, then transition without failure wording.
  - Requirement: On interruption, retain partial raw events and restart the station from initial state on rejoin.
  - Gameplay Function: Creates a clear station boundary while preserving partial evidence.

##### Scoring Setup

- **Resonance Engine Score** — 0–100 — 64% Target Completion + 16% Free-Play Coverage + 20% Rule Application
  - **Target Completion (64%)** — Target 1 contributes 28 points and Target 2 contributes 36 points. Partial completion is retained at timeout.
  - **Free-Play Coverage (16%)** — Award proportionally from the five primary input types tried during the clue-reading and testing phase.
  - **Rule Application (20%)** — Award from template-specific evidence that the player used the distinguishing rule, applied it to Target 2, and avoided an extended repeated-action loop after demonstrating it.
  - **Timer Start:** Start the station game-time clock when the player gains Resonance Engine interaction control.
  - **Timer Stop:** Stop on Target 2 confirmation or the approved station deadline; pause time is excluded.
  - **No-Score Condition:** Do not create a completed Objective Score if the session ends before the station boundary record can be secured; preserve raw partial evidence for platform handling.
  - **Duplicate Prevention:** One completed Resonance Engine result per session; target confirmations and completion export are idempotent.
  - **Final Result:** One of four Objective Scores; the session result combines the four objective results after the Workshop.
  - **Player-Facing Result:** Do not display the calculated score in-game; show only puzzle feedback, target confirmations, and completion.
  - **Telemetry / Export:** Export template ID, target IDs, input/state sequence, free-play coverage evidence, target shown/matched timestamps, timeout/completion, and component inputs; no final score field from the map.

##### Reset / Interruption

- Restore all six lever states, pressure plate/weight state if used, three crystal panels, target display, free-play timer, selected template presentation, inventory/effects, and permissions.
- Verify no target, panel, timer, or interaction state from the previous run remains before the lane becomes reusable.
- **Reset Result:** The Resonance Engine returns to a neutral authored template-ready state.

##### Important Development Notes

- **Immediate Input Feedback** — Every input must produce feedback in the same tick or controlled update cycle as the state change.
- **No Vanilla Knowledge** — No template may depend on real Minecraft knowledge.
- **Target 2 Tests the Rule** — Target 2 must use the selected template’s distinguishing rule.
- **Raw Evidence Only** — The map logs raw scoring evidence but does not send or display the final score.

##### Acceptance

- The Resonance Engine reaches its defined end condition without creating an unrecoverable player state.
- The Resonance Engine preserves the approved player-facing behavior, data/result boundary, and lane isolation rules.
- The Resonance Engine reset restores the authored starting state before the assigned lane is reused.

##### Terms

- **Free-Play Phase** — The opening approximately 90-second period when the player can test inputs before Target 1 appears.
- **Rule Template** — One authored mapping between lever inputs and the three crystal panel states.
- **Target Pattern** — The three-state Dark, Glowing, and Pulsing crystal configuration the player must match.
- **Crystal Panel** — One output surface showing the current state produced by the submitted lever configuration.
- **Target Match** — A submitted crystal state that matches the currently active target and is accepted by the Engine.

### 06. The Broken Gallery

**Objective 2**

#### Gameplay Overview

**Context:** The player enters a ruined three-checkpoint crossing with upper, lower, and side route variations. A fixed construction kit is granted at the start.

**Main Objective:** Carry the Custodian Key across all three checkpoints. In Checkpoint 3, adapt to the scripted collapse and reach the far pedestal through the valid recovery path.

**Result:** The Custodian Key reaches the far pedestal and the Warden Halls route opens.

##### Gameplay Information

- **Game Purpose:** Create a limited-resource traversal challenge where route choice, building, and recovery matter without precision movement or lethal failure.
- **Gameplay Time:** Approximately 9 minutes.
- **Starting Condition:** The Gallery is reset, the Custodian Key is granted, and the fixed crossing kit is full.
- **End Condition:** The Custodian Key is accepted by the far pedestal after the player clears Checkpoint 3.
- **Fail Condition:** No permanent fail state. A fall returns the player to a safe checkpoint; resource waste may remove one route, but one resupply and a valid recovery path remain available.
- **Scoring Criteria:** Objective Score 0–100 based on Objective Progress, Resource Planning, Post-Collapse Adaptation, and Recovery Independence.

##### Gameplay Flow

- **Survey the Crossing** — See the three checkpoint structure, route variations, far pedestal, and fixed resource kit before committing resources.
- **Checkpoint 1 — Learn the Tools** — Cross the first broken section using basic blocks/ladder placement and one clearly authored route decision.
- **Checkpoint 2 — Manage Resources** — Solve a more varied section using blocks, ladders, Spring Column, and/or Anchor Ring while preserving enough kit for the final crossing.
- **Checkpoint 3 — Collapse and Adapt** — A short warning begins; once the player reaches about 50% of the final checkpoint the authored collapse resolves safely. The current segment becomes unusable and the player must use the remaining recovery connector/route.
- **Place the Custodian Key** — Reach the far platform, place the key on the pedestal, save raw evidence, and open the Warden Halls transition.

#### Level Design

Build one ruined crossing as three readable checkpoints. Upper, lower, and side route ideas are used as spatial variations inside the crossing rather than three separate progression tracks. Checkpoint 3 owns the only collapse event, and every collapse state must preserve a visible safe recovery route.

##### Design Flow

- **Checkpoint 1 — Tool Introduction** — Establish the destination and teach basic block/ladder placement on a forgiving broken path.
- **Checkpoint 2 — Route Variation** — Combine upper/lower/side geometry with Spring Column or Anchor Ring options and tighter resource planning.
- **Checkpoint 3 — Collapse** — Telegraph the final collapse, require meaningful forward progress, then seal the current segment and expose the recovery continuation.
- **Far Pedestal** — Frame the Custodian Key placement and Warden Halls door as the completion handoff.

##### Build Requirements

###### Checkpoint Geometry
- **Start / Checkpoint 1** — Area: Forgiving authored section
  - Build/Visual: Keep the far goal visible enough to establish direction.
  - Build/Visual: Use basic broken spans, block placement, and ladder movement; avoid precision jumps.
  - Gameplay Function: Introduces traversal tools and the resource budget.
- **Checkpoint 2** — Area: Mid crossing
  - Build/Visual: Use upper/lower/side route variations, intersections, and different broken-gap shapes rather than one long bridge.
  - Build/Visual: Include one valid Spring Column surface and marked Anchor Ring opportunities with safe landing markers.
  - Gameplay Function: Creates route/resource planning before the collapse phase.
- **Checkpoint 3** — Area: Final crossing
  - Build/Visual: Create one authored collapse segment with a short readable warning and a progress threshold around 50% of the checkpoint.
  - Build/Visual: The collapse must happen from a safe event position and must never trap the player inside sealed geometry.
  - Gameplay Function: Forces adaptation using the remaining route instead of repeating earlier building.
###### Recovery and Resources
- **Recovery Connector / Route** — Area: Reachable from collapse state
  - Build/Visual: From every valid collapse position, preserve one clearly readable continuation that can be completed with the expected remaining kit.
  - Build/Visual: Do not require camera-direction inference or hidden teleports.
  - Gameplay Function: Guarantees recovery while preserving the cost of the failed route segment.
- **Single Resupply Alcove** — Area: Central recovery point
  - Build/Visual: Place one visible but non-dominant resupply point accessible after collapse or a validated low-kit state.
  - Build/Visual: Do not allow repeated farming.
  - Gameplay Function: Prevents resource waste from creating an unrecoverable run.
- **Safe Fall Recovery** — Area: Below authored traversal
  - Build/Visual: Provide safe lower surfaces/return geometry or scripted return markers at each checkpoint.
  - Gameplay Function: Turns falling into time loss rather than death or full restart.
###### Goal and Reset
- **Far Custodian Key Pedestal** — Area: End platform
  - Build/Visual: Place the destination pedestal and Warden Halls door in one completion frame.
  - Build/Visual: Use a clear empty/accepted key state.
  - Gameplay Function: Defines exact completion and next destination.
- **Reset-Owned Crossing** — Area: Full Gallery
  - Build/Visual: Keep placed blocks/ladders, route segments, collapse geometry, Spring Column, Anchor Rings, resupply, key, FX, and door states inside reset ownership.
  - Gameplay Function: Restores a deterministic crossing for the next session.

##### Important Build Notes

- **Three Checkpoints Own Progression** — Upper/lower/side are route variations; Checkpoint 1 → 2 → 3 is the actual progression model.
- **Collapse Only in Checkpoint 3** — No earlier checkpoint may trigger the route-collapse mechanic.
- **Recovery Must Remain Valid** — After collapse or resource waste, at least one safe continuation must still be possible with the recovery/resupply rules.
- **No Precision Traversal** — Movement challenge comes from building/tool choice, not pixel-perfect jumps or aim.

#### Developer

Implement the fixed station-owned crossing kit, three checkpoint progression, scripted movement tools, one Checkpoint-3 collapse, guaranteed recovery/resupply, Custodian Key completion, platform-side scoring evidence, interruption handling, and full restoration.

##### Development Flow

- **Mechanic Setup** — Grant the fixed kit, initialize three checkpoint states, Anchor charges, Spring Column, Custodian Key, resupply, and reset ownership.
- **Checkpoint Progression** — Track approved placements/tool use and advance Checkpoint 1 → 2 → 3 while preserving resource state.
- **Collapse and Completion** — In Checkpoint 3, resolve the warning/collapse at the authored threshold, switch the valid recovery state, and complete on far-pedestal key placement.
- **Data and Reset** — Record resource/checkpoint/collapse/recovery evidence, calculate nothing in-map, then restore every temporary crossing state.

##### Development Requirements

###### Crossing Runtime
- **Fixed Supply Kit**
  - Requirement: Grant 12 bridge blocks, 4 ladder segments, one single-use Spring Column, two Anchor Ring grapple charges, and one Custodian Key in station-owned inventory.
  - Requirement: Prevent drop/storage/duplication/cross-station use and placement outside approved zones.
  - Requirement: Restore a critical lost resource only when validation detects an impossible state.
  - Gameplay Function: The same bounded resource problem is available to every session.
- **Scripted Movement Tools**
  - Requirement: Implement Spring Column as one fixed vertical movement interaction.
  - Requirement: Highlight only authored Anchor Rings while the tool is active; move the player along a fixed safe arc and consume a charge only after valid arrival.
  - Gameplay Function: Special movement remains deterministic and touch-readable.
###### Checkpoint and Collapse Logic
- **Checkpoint State**
  - Requirement: Store progression as Checkpoint 1, 2, and 3 plus checkpoint-local route/resource evidence.
  - Requirement: Allow route variation inside a checkpoint without redefining the project progression order.
  - Gameplay Function: Progress and recovery use one unambiguous model.
- **Checkpoint 3 Collapse**
  - Requirement: Enable collapse logic only after Checkpoint 3 becomes active.
  - Requirement: Start a short warning and resolve the authored collapse when the player reaches approximately 50% of the final checkpoint or the configured safe fallback condition.
  - Requirement: Seal only the current authored segment, update the recovery route, and never infer the target segment from camera direction.
  - Gameplay Function: Creates one predictable adaptation event without trapping the player.
- **Recovery, Resupply, and Completion**
  - Requirement: Return falls to the nearest valid safe checkpoint/ledge with preserved progression.
  - Requirement: Grant the single resupply only once after collapse or a validated low-kit state.
  - Requirement: Complete only when the Custodian Key is accepted by the far pedestal; at station deadline preserve furthest checkpoint, resources, collapse, resupply, and key state.
  - Gameplay Function: Every run remains finishable or meaningfully recordable without lethal failure.

##### Scoring Setup

- **Broken Gallery Score** — 0–100 — 40% Objective Progress + 28% Resource Planning + 24% Post-Collapse Adaptation + 8% Recovery Independence
  - **Objective Progress (40%)** — Award from committed-route/checkpoint progress, final-collapse exposure, far platform reach, and Custodian Key placement.
  - **Resource Planning (28%)** — Compare weighted resource use with the validated expected budget for the completed crossing; cap at full value.
  - **Post-Collapse Adaptation (24%)** — Award for stopping attempts into the sealed segment, committing to the valid recovery continuation, and making forward progress after collapse.
  - **Recovery Independence (8%)** — Full value for completion without resupply; partial value for completion after the single resupply.
  - **Timer Start:** Start when the player receives the Gallery kit and Custodian Key.
  - **Timer Stop:** Stop on far-pedestal Custodian Key acceptance or station deadline; pause time is excluded.
  - **No-Score Condition:** Do not finalize a completed Objective Score without a secured station-boundary record; preserve partial checkpoint/resource evidence for platform handling.
  - **Duplicate Prevention:** Collapse fires once, resupply grants once, and Gallery completion exports once per session.
  - **Final Result:** One of four Objective Scores combined in the completed session result.
  - **Player-Facing Result:** Do not show a score or countdown; show only local resource, checkpoint, collapse, recovery, and completion feedback.
  - **Telemetry / Export:** Export resource events, checkpoint/route state, collapse warning/fire, post-collapse actions, resupply, falls/recovery, key placement, timeout/completion, and component inputs; no final score field.

##### Reset / Interruption

- Clear station inventory/temporary permissions and remove all player-placed blocks/ladders.
- Restore all three checkpoints, collapsed structures, recovery route, Anchor charges, Spring Column, resupply, Custodian Key, doors, entities, lights/audio/particles, and safe recovery markers.
- **Reset Result:** The Broken Gallery returns to the pristine three-checkpoint crossing with a full fixed kit.

##### Important Development Notes

- **Collapse Is Checkpoint-3 Only** — The collapse trigger cannot activate during Checkpoint 1 or 2.
- **No Camera Inference** — Collapse/recovery ownership comes from authored checkpoint/segment state, never viewing direction alone.
- **One Guaranteed Recovery** — Every authored collapse configuration must retain at least one valid continuation plus the one-use resupply safety net.
- **Raw Evidence Only** — The map records scoring inputs but sends no calculated Broken Gallery Score.

##### Acceptance

- The Broken Gallery reaches its defined end condition without creating an unrecoverable player state.
- The Broken Gallery preserves the approved player-facing behavior, data/result boundary, and lane isolation rules.
- The Broken Gallery reset restores the authored starting state before the assigned lane is reused.

##### Terms

- **Route commitment** — The route the player is actively attempting at the collapse event
- **Spring Column** — A single-use climbable resource in the fixed kit
- **Anchor Ring grapple** — A limited-charge interaction that reaches marked anchors
- **Sealed segment** — The route section made unavailable by the scripted collapse

### 07. The Warden Halls

**Objective 3**

#### Gameplay Overview

**Context:** The Warden Halls use wall, floor, and ceiling traps across three increasingly complex checkpoints. Echo Pebble disables wall/floor traps briefly; ceiling traps are solved through observation and timing.

**Main Objective:** Reach the inner gate by learning the trap families, using Echo Pebble selectively, and choosing when to wait or rush.

**Result:** The player reaches the inner gate and the Gremlin’s Workshop route opens.

##### Gameplay Information

- **Game Purpose:** Create a learnable risk-reading challenge where cautious observation and informed rushing are both valid strategies.
- **Gameplay Time:** Approximately 9 minutes.
- **Starting Condition:** One authored layout is active, trap cycles/checkpoints are reset, and Echo Pebble is available.
- **End Condition:** The player enters the inner gate trigger after clearing the final security sequence.
- **Fail Condition:** Trap consequences are non-lethal and cost time or position only. The player returns to the nearest safe checkpoint without losing completed objective progress.
- **Scoring Criteria:** Objective Score 0–100 based on Objective Progress, Rule Recognition, Intentional Strategy, and Time-Loss Control.

##### Gameplay Flow

- **Learn the Three Trap Families** — Encounter wall, floor, and ceiling traps separately and read their distinct warning tells and consequence states.
- **Use Echo Pebble Selectively** — Disable wall or floor traps for a short window; ceiling traps reject Echo Pebble use and remain timing/observation challenges.
- **Checkpoint 2 — Combine Hazards** — Cross combinations of trap types by choosing when to disable, wait through a full cycle, or rush through a valid window.
- **Checkpoint 3 — Final Security Sequence** — Handle denser combinations and shorter decision windows using the same established rules; consequences return the player to a safe checkpoint.
- **Reach the Inner Gate** — Enter the inner gate trigger, save raw strategy/progress evidence, and open the Gremlin’s Workshop transition.

#### Level Design

Build three equivalent corridor layout variants containing the same three trap families and comparable traversal length. Wall and floor traps must support clear Echo Pebble disable targets; ceiling traps must not be Pebble-disableable and instead rely on readable observation/timing. All consequences are non-lethal and time-based.

##### Design Flow

- **Approach** — Enter a readable zone before each trap and see its invented tell.
- **Choose** — Probe, observe a full cycle, or rush.
- **Consequence or Safe Crossing** — Receive a controlled time cost or advance through the valid window.
- **inner gate** — Complete the final halls and reveal the Orrery routing record.

##### Build Requirements

###### Hall and Layout Variants
- **Three Layouts** — Area: Full station zone
  - Build/Visual: Build Progressive Introduction, Alternating Risk, and Clustered Patterns variants.
  - Build/Visual: Use the same count of each trap type, comparable length, and comparable total consequence dose.
  - Build/Visual: Keep transition and inner gate positions consistent across variants.
  - Gameplay Function: Provides authored variation without changing difficulty contract.
- **Approach and Checkpoints** — Area: Authored area
  - Build/Visual: Place a 3–5 block approach zone before each trap and safe space for observation.
  - Build/Visual: Create two major checkpoints plus final-hall checkpoint.
  - Build/Visual: Prevent overlapping danger volumes from producing unavoidable chained consequences.
  - Gameplay Function: Enables reliable behavior classification and recovery.
###### Trap Types
- **Watcher Gate** — Area: Authored area
  - Build/Visual: Build a mechanical eye with clear open/closed cycle, visible beam, and matching audio cue.
  - Build/Visual: Provide a fixed knockback return marker.
  - Gameplay Function: Supports waiting, probing, or timed rushing.
- **Resonant Floor** — Area: Authored area
  - Build/Visual: Build an outward rune pulse with matching sound and a padded under-hall with short return stairs.
  - Build/Visual: Ensure visual rhythm remains readable when audio is muted.
  - Gameplay Function: Creates a harmless drop and recovery loop.
- **Warden Sweep** — Area: Authored area
  - Build/Visual: Build sequential wall lights, safe recesses, and a short gate-delay consequence.
  - Build/Visual: Keep the completed sweep visually readable for follow-behind movement.
  - Gameplay Function: Creates a different time-only risk pattern.
###### Tools and Ending
- **Echo Pebble Targets** — Area: Authored area
  - Build/Visual: Provide clear Echo Pebble target anchors and highlight states only on wall and floor trap instances.
  - Build/Visual: Ceiling traps must have no valid Pebble target and must communicate their timing window through visual/audio tells.
  - Build/Visual: Keep the tool unlimited and prevent projectiles/effects from leaving the lane.
  - Gameplay Function: Supports selective safe windows without removing the ceiling-trap timing challenge.
- **inner gate** — Area: Authored area
  - Build/Visual: Build the inner gate reveal with a visible Orrery routing diagram and one-way Workshop transition.
  - Build/Visual: Keep all trap pieces, under-halls, gates, and FX within reset ownership.
  - Gameplay Function: Pays off the traversal and directs the final objective.

##### Important Build Notes

- **Pebble Scope Is Explicit** — Only wall and floor traps accept Echo Pebble; ceiling traps never do.
- **One Tell Owns One State** — Visual and audio warning cues must reflect the same authoritative trap cycle.
- **Non-Lethal Consequences** — Knockback, padded return, or short gate delay may cost time but must not remove objective progress.
- **Layout Parity** — All three layout variants require comparable length, trap counts, and tested consequence exposure.

#### Developer

Implement deterministic trap cycles, three equivalent layout variants, an unlimited Echo Pebble that disables wall/floor traps only, observation/wait/rush classification, non-lethal consequence recovery, platform-side scoring evidence, interruption handling, and complete reset.

##### Development Flow

- **Mechanic Setup** — Select one layout, initialize trap instances/checkpoints, bind visual/audio tells to deterministic game-time cycles, and grant Echo Pebble.
- **Trap Reading and Pebble** — Track approach observation, allow 4-second wall/floor disables, reject ceiling targets, and classify wait/rush/probe behavior.
- **Consequences and Completion** — Apply non-lethal time consequences, recover to valid checkpoints, complete on inner-gate entry, and preserve timeout progress.
- **Data and Reset** — Export raw trap/strategy evidence only, then restore cycles, checkpoints, Pebble state, gates, effects, and selected layout.

##### Development Requirements

###### Mechanic Setup
- **Layout Selection**
  - Requirement: Store three authored variants with identical trap-type counts and comparable path length.
  - Requirement: Select one at station entry, record its ID, and keep it fixed through pause/resume.
  - Requirement: Activate only the chosen variant’s geometry and trigger volumes.
  - Gameplay Function: Provides controlled variation with a verifiable dose.
- **Trap State Machines**
  - Requirement: Implement fixed cycles for Watcher Gate, Resonant Floor, and Warden Sweep.
  - Requirement: Expose visual and audio warning states from the same authoritative timer.
  - Requirement: Pause and resume every cycle at its exact game-time position.
  - Gameplay Function: Keeps trap tells consistent and deterministic.
###### Gameplay Setup
- **Echo Pebble**
  - Requirement: Treat wall and floor trap instances as valid Echo Pebble targets; ceiling traps are invalid targets.
  - Requirement: On a valid hit, disable the selected wall/floor trap for 4 seconds of game-time, then restore its normal cycle.
  - Requirement: Return/refresh the unlimited Pebble after use, prevent cross-lane/invalid targets, and record target, prior trap state, disable start/end, and timestamp.
  - Gameplay Function: Creates a short deliberate safe window while preserving ceiling-trap observation/timing.
- **Behavior Classification**
  - Requirement: Record approach enter/exit and time in zone.
  - Requirement: Classify wait-out only after one complete observed cycle followed by a safe crossing without probe.
  - Requirement: Classify rush when danger is entered before a full cycle or probe; record success or consequence.
  - Gameplay Function: Creates interpretable raw evidence without prescribing one strategy.
- **Consequence and Completion**
  - Requirement: Use fixed knockback, padded drop/return, or gate-delay consequences with no damage.
  - Requirement: Record consequence start/end and restore the player to a valid route.
  - Requirement: Complete at inner gate entry; at timeout preserve furthest checkpoint and current trap state.
  - Gameplay Function: Keeps setbacks low-stakes and measurable.

##### Scoring Setup

- **Warden Halls Score** — 0–100 — 40% Objective Progress + 24% Rule Recognition + 20% Intentional Strategy + 16% Time-Loss Control
  - **Objective Progress (40%)** — Award from two major checkpoints, the final hall, and inner gate entry.
  - **Rule Recognition (24%)** — Award up to 8 points for each trap family from first informed safe crossing and later retained recognition.
  - **Intentional Strategy (20%)** — Award from meaningful Echo Pebble probe/wait evidence or intentional rush/recovery evidence; no single play style is mandatory.
  - **Time-Loss Control (16%)** — Calculate from non-pause consequence time against the configured reference dose.
  - **Timer Start:** Start when the selected Warden layout activates and Echo Pebble is granted.
  - **Timer Stop:** Stop on inner-gate entry or station deadline; pause time is excluded.
  - **No-Score Condition:** Do not finalize a completed Objective Score without a secured station-boundary record; partial raw progress remains available for platform handling.
  - **Duplicate Prevention:** Each trap event, consequence, checkpoint, and completion boundary uses stable instance/session identity and idempotent export.
  - **Final Result:** One of four Objective Scores combined in the completed session result.
  - **Player-Facing Result:** Show trap tells, Pebble target/disable feedback, checkpoint/recovery cues, and completion only; no calculated score.
  - **Telemetry / Export:** Export layout ID, trap instance/type, approach timing, Pebble probes/disable windows, observed cycles, wait/rush actions, consequences, same-type history, checkpoints, timeout/completion; no final score field.

##### Reset / Interruption

- Clear Echo Pebble/permissions and restore every wall, floor, and ceiling trap cycle to its authored initial state.
- Restore gates, padded recovery areas, checkpoints, Vex triggers, doors, entities, visual/audio effects, and layout selection ownership.
- **Reset Result:** The Warden Halls return to a clean authored layout-ready state with no previous trap-cycle or Pebble-disable state.

##### Important Development Notes

- **Ceiling Traps Never Disable** — Echo Pebble validation must reject ceiling traps consistently in gameplay, highlights, and telemetry.
- **Deterministic Game-Time** — All trap cycles and 4-second disable windows freeze and resume with the script-owned pause state.
- **Strategy Neutrality** — Cautious waits and informed rushes are both valid; scoring cannot require one style exclusively.
- **Raw Evidence Only** — The map records scoring inputs but sends no calculated Warden Halls Score.

##### Acceptance

- The Warden Halls reaches its defined end condition without creating an unrecoverable player state.
- The Warden Halls preserves the approved player-facing behavior, data/result boundary, and lane isolation rules.
- The Warden Halls reset restores the authored starting state before the assigned lane is reused.

##### Terms

- **Echo Pebble** — The unlimited tool that temporarily disables a valid wall or floor trap for four seconds of game-time.
- **Wall Trap** — A telegraphed security hazard that can be temporarily disabled with the Echo Pebble.
- **Floor Trap** — A telegraphed ground hazard that can be temporarily disabled with the Echo Pebble.
- **Ceiling Trap** — A timing-only hazard that cannot be disabled with the Echo Pebble.
- **Warning Tell** — The consistent visual and audio cue that communicates a trap's active cycle before consequence.

### 08. The Gremlin’s Workshop

**Objective 4**

#### Gameplay Overview

**Context:** The Workshop contains the Source Crystal, a 3×3 rotatable conduit grid, and the three-ring Great Orrery. After Ring 2, a Gremlin permanently breaks one active connection and the player must reroute around it.

**Main Objective:** Power Ring 1 and Ring 2, recover from the scripted sabotage, then reroute the network to power Ring 3 while restoring the full Orrery network.

**Result:** All three rings are powered together, the Great Orrery is restored, and the ending sequence begins.

##### Gameplay Information

- **Game Purpose:** Test cumulative power-routing understanding and adaptation to a visible topology change rather than a hidden rule reversal.
- **Gameplay Time:** Approximately 9 minutes.
- **Starting Condition:** The 3×3 grid is reset, all three ring targets are visible, Ring 1 has its easy authored route, and no connection is sabotaged.
- **End Condition:** All three Orrery rings are powered simultaneously after the post-sabotage reroute.
- **Fail Condition:** No permanent fail state. Rotations remain reversible; the sabotaged connection stays broken, but a valid authored reroute always exists. Vex may highlight a useful area but never solve the board.
- **Scoring Criteria:** Objective Score 0–100 based on Ring Completion, Post-Fault Adaptation, and Independent Progress.

##### Gameplay Flow

- **Learn the Grid and Power Ring 1** — Rotate the deliberately easy first path and learn how node orientation and live flow connect the Source Crystal to the Orrery.
- **Extend the Network to Ring 2** — Preserve Ring 1 while branching/extending the same cumulative network until Ring 2 is powered.
- **Gremlin Sabotage** — About 20 seconds after Ring 2 stabilizes, briefly lock input, run the scripted Gremlin event, and permanently break one authored active connection with an unmistakable damaged visual.
- **Reroute and Power Ring 3** — Restore any interrupted powered segment by routing around the broken edge, then extend the valid cumulative network to Ring 3. Vex may highlight but never auto-solve.
- **Restore the Great Orrery** — Complete only when all three rings are powered simultaneously, save the complete action/fault sequence, lock the puzzle, and begin the ending.

#### Level Design

Build a readable Workshop centered on the 3×3 rotatable conduit grid and three-ring Great Orrery. Source, live power flow, ring targets, the Gremlin path, and the permanently broken post-fault connection must remain visually readable without UI-only explanation. Show the broken connection as a physical topology change.

##### Design Flow

- **Learn Ring 1** — Use an intentionally easy route that establishes rotation and live power-flow readability.
- **Extend to Ring 2** — Require cumulative routing that preserves Ring 1 and introduces branching/split decisions.
- **Gremlin Break** — Stage one fixed Gremlin path and damage one authored active connection with a permanent broken visual.
- **Reroute to Ring 3** — Author a valid alternate route around the broken edge that restores the cumulative network and reaches Ring 3.

##### Build Requirements

###### Workshop and Orrery
- **3×3 Conduit Grid** — Area: Central 3×3 interaction field
  - Build/Visual: Use authored Straight, Elbow, and Split conduit nodes with clearly readable connection edges in every 90° rotation.
  - Build/Visual: Show live powered, unpowered, and blocked-flow states directly on the grid; no form-only interpretation.
  - Build/Visual: Do not rely on vanilla redstone textures or logic for the invented routing grammar.
  - Gameplay Function: Provides the cumulative routing puzzle.
- **Source Crystal and Three Rings** — Area: Visible from grid
  - Build/Visual: Keep Source Crystal and Ring 1–3 targets readable together with the active network.
  - Build/Visual: Each ring needs distinct inactive/powered feedback and the final three-ring restored state.
  - Gameplay Function: Makes progression and completion visible without score UI.
###### Sabotage and Reroute
- **Broken Connection** — Area: One authored active edge after Ring 2
  - Build/Visual: Provide one fixed Gremlin-accessible connection that can switch to a permanently damaged/sealed state.
  - Build/Visual: The broken edge must read as an obvious physical sabotage event caused by the Gremlin.
  - Gameplay Function: Creates the topology change that forces adaptation.
- **Ring 3 Recovery Route** — Area: Remaining authored grid topology
  - Build/Visual: Ensure a valid alternate connection path exists around the broken edge.
  - Build/Visual: Require meaningful rerouting; the original exact route must no longer complete the full network after sabotage.
  - Gameplay Function: Tests adaptation while preserving the original conduit rules.
###### Gremlin and Ending
- **Scripted Gremlin Path** — Area: Fixed cinematic route
  - Build/Visual: Keep Gremlin movement, fault point, Vex reaction, and damaged-edge reveal visible from the player’s puzzle position.
  - Build/Visual: Do not require navigation AI.
  - Gameplay Function: Externalizes the sabotage as a deterministic authored event.
- **Orrery Payoff Frame** — Area: Workshop completion view
  - Build/Visual: Frame the all-rings-powered Great Orrery and the route into the ending sequence.
  - Build/Visual: Keep grid nodes, source/rings, broken edge, Gremlin markers, lights, audio, and FX inside reset ownership.
  - Gameplay Function: Connects puzzle completion to the story payoff.

##### Important Build Notes

- **Connection Rules Stay Constant** — The Gremlin breaks one physical connection; all other conduit connection rules remain unchanged.
- **Broken Edge Is Permanent for the Run** — The sabotaged connection cannot be repaired before objective completion and must remain visibly blocked.
- **Vex Does Not Auto-Solve** — Assist may highlight a useful connection or region only; it cannot rotate nodes or automatically reach Ring 2.
- **Fault Must Be Unmissable** — Gremlin movement, input lock, break effect, Vex reaction, and damaged connection state must clearly read as external sabotage.

#### Developer

Implement the deterministic 3×3 conduit solver, cumulative Ring 1/2 progression, fixed post-Ring-2 physical connection sabotage, Ring 3 rerouting, highlight-only Vex assist, complete action/fault telemetry, platform-side scoring inputs, interruption handling, and full reset.

##### Development Flow

- **Mechanic Setup** — Initialize node types/rotations, Source Crystal, ring states, power solver, authored sabotage edge, and player interaction permissions.
- **Ring 1 and Ring 2** — Recalculate the complete orthogonal network after every rotation and validate Ring 1/2 cumulative power states.
- **Sabotage and Ring 3** — After Ring 2, run the Gremlin event, mark one authored active edge permanently broken, recalculate flow, and require a valid reroute to Ring 3.
- **Result and Reset** — Record the entire rotation/state/fault/assist sequence, complete on all three rings powered, then restore the original unsabotaged board.

##### Development Requirements

###### Conduit Runtime
- **Conduit Solver**
  - Requirement: Store Straight, Elbow, or Split node type plus 90° rotation for all 3×3 cells and resolve only orthogonal authored connections.
  - Requirement: After every valid rotation, recalculate the full Source-to-network flow atomically and update visual state before the next input.
  - Requirement: Keep Ring 1 and Ring 2 powered only while their actual route remains connected.
  - Gameplay Function: Creates a deterministic replayable cumulative network.
- **Ring Progression**
  - Requirement: Ring 1 uses the deliberately easy authored solution.
  - Requirement: Ring 2 extends/branches the existing network rather than resetting Ring 1.
  - Requirement: Complete ring milestones from actual powered state, not button count.
  - Gameplay Function: Progression teaches then extends the same routing rule.
###### Fault and Adaptation
- **Scripted Connection Sabotage**
  - Requirement: Schedule the fault about 20 seconds after Ring 2 stabilizes using game-time.
  - Requirement: Briefly lock input, play the fixed Gremlin path/Vex reaction, then permanently disable one authored active connection edge for the remainder of the run.
  - Requirement: Record the broken edge ID, prior flow state, fault time, and first post-fault interaction. Keep all normal conduit connection rules unchanged.
  - Gameplay Function: Creates one clear external topology change identical for every session.
- **Ring 3 Reroute**
  - Requirement: Recalculate the network with the broken edge unavailable.
  - Requirement: Require the player to restore any lost powered segment by using an authored alternate route and then extend valid power to Ring 3.
  - Requirement: Complete only when all three rings are simultaneously powered.
  - Gameplay Function: Verifies real adaptation to the broken network.
- **Vex Assist**
  - Requirement: At the configured assist threshold, highlight one useful node/connection/region only.
  - Requirement: Never rotate a node, change a connection, or automatically advance Ring 2/3.
  - Requirement: Record assist shown/used state for scoring independence.
  - Gameplay Function: Prevents a stalled session without removing the player’s puzzle completion.

##### Scoring Setup

- **Gremlin’s Workshop Score** — 0–100 — 72% Ring Completion + 20% Post-Fault Adaptation + 8% Independent Progress
  - **Ring Completion (72%)** — Ring 1 contributes 16 points, Ring 2 contributes 24 points, and Ring 3 contributes 32 points.
  - **Post-Fault Adaptation (20%)** — Award from recognizing the sabotaged connection, stopping attempts through the broken edge, restoring lost power through an alternate route, and using the rerouted network to reach Ring 3.
  - **Independent Progress (8%)** — Full value when Ring 2 completes without Vex assist; highlight-only assistance does not remove ring or adaptation points.
  - **Timer Start:** Start when Workshop conduit interaction becomes active.
  - **Timer Stop:** Stop when all three rings are powered simultaneously or at the station deadline; pause time is excluded.
  - **No-Score Condition:** Do not finalize a completed Objective Score without a secured Workshop boundary record; preserve raw partial ring/fault evidence for platform handling.
  - **Duplicate Prevention:** Ring milestones, sabotage, assist, completion, and result export are idempotent per session; sabotage fires once.
  - **Final Result:** The fourth Objective Score; after Workshop completion the session result contains all four objective scores and proceeds to the ending.
  - **Player-Facing Result:** Show live power flow, ring states, sabotage damage, assist highlight, and completion only; no calculated score.
  - **Telemetry / Export:** Export initial layout, every rotation/prior-new orientation, full flow state, ring timestamps, broken-edge fault details, post-fault actions, reroute recovery, assist, pause, timeout/completion; no final score field.

##### Reset / Interruption

- Restore the original unsabotaged connection graph, node rotations, Source Crystal, ring states, timer, assist, Vex, Gremlin model/path, lights/audio/particles, interaction locks, and permissions.
- Verify that the broken-edge state and all post-fault flags are cleared before lane reuse.
- **Reset Result:** The Workshop returns to its authored initial grid with no sabotaged connection and all rings inactive.

##### Important Development Notes

- **Physical Sabotage** — The connection graph changes at one edge; conduit connection rules remain constant.
- **Fault Uses Game-Time** — The ~20-second post-Ring-2 fault schedule freezes during pause.
- **Assist Is Highlight-Only** — Vex cannot rotate nodes or auto-complete Ring 2/3 and assist state is recorded.
- **Raw Evidence Only** — The map records scoring inputs but sends no calculated Workshop Score.

##### Acceptance

- The Gremlin’s Workshop reaches its defined end condition without creating an unrecoverable player state.
- The Gremlin’s Workshop preserves the approved player-facing behavior, data/result boundary, and lane isolation rules.
- The Gremlin’s Workshop reset restores the authored starting state before the assigned lane is reused.

##### Terms

- **Orrery ring** — One of the three sequential power milestones
- **Flow state** — The complete visible connection and powered state of the grid
- **Conduit rule** — The invented behavior that determines how a node passes power
- **Connection sabotage** — The one-time destruction of an active conduit connection after Ring 2

### 09. Vault Restored

**Ending**

#### Gameplay Overview

**Context:** The Great Orrery is restored and the vault begins returning to operation. The player enters a closing scene with Custodian Vex.

**Main Objective:** Watch the restoration payoff, receive the Clockwork Wayfinder reward, and return safely to the holding area.

**Result:** The player sees the vault awaken, receives Clockwork Wayfinder once, and returns safely. The ending adds no Objective Score.

##### Gameplay Information

- **Game Purpose:** Resolve the story and close the session without exposing platform scoring/analysis or adding another gameplay challenge.
- **Gameplay Time:** Part of the approximately 5-minute transition and closing-scene allowance.
- **Starting Condition:** Ring 3 completion and the valid all-rings-powered Great Orrery restoration event are secured.
- **End Condition:** Session data is secured, Clockwork Wayfinder is delivered once, the player returns to the holding area, and the assigned lane is reusable-ready.
- **Fail Condition:** Completed objective progress is preserved. Reward/save retries are idempotent, and a failed lane reset keeps that lane unavailable until it is clean.
- **Scoring Criteria:** No new Objective Score. The ending closes the completed four-objective session.

##### Gameplay Flow

- **Orrery Alignment** — See all three rings synchronize and release power into the restored Great Orrery.
- **Vault Awakens** — Watch coordinated callbacks from the Workshop, inner gate, Resonance Engine, and Great Hall as the restored systems respond.
- **Vex Recognition** — Vex delivers the closing dialogue and acknowledges completion of the restoration journey.
- **Reward and Save** — Secure the session result and grant the Clockwork Wayfinder cosmetic reward exactly once.
- **Return and Reset** — Open the safe return route, move the player to the holding area, clear temporary state, verify reset, and release the lane for reuse.

#### Level Design

Build one coordinated closing sequence that visibly connects the Great Orrery, Workshop, inner gate, Resonance Engine, and Great Hall. Present the Clockwork Wayfinder reward clearly, then guide the player to a safe return point without introducing another gameplay objective.

##### Design Flow

- **Orrery Alignment** — Show all three rings align and release power.
- **Vault Response** — Reveal Workshop, inner gate, Engine, and Great Hall callbacks.
- **Recognition** — Frame Vex and the Clockwork Wayfinder presentation.
- **Return** — Open the lobby return and keep the ending area reset-safe.

##### Build Requirements

###### Closing Presentation
- **Orrery and Workshop** — Area: Authored area
  - Build/Visual: Build the full ring alignment, central light release, and Workshop activation states.
  - Build/Visual: Keep the player in a stable viewing position with no hazardous movement.
  - Gameplay Function: Provides immediate final payoff.
- **Vault Callbacks** — Area: Authored area
  - Build/Visual: Create readable activation states for the inner gate, Resonance Engine, and Great Hall.
  - Build/Visual: Use consistent light travel to imply restored power across the vault.
  - Gameplay Function: Shows that the entire journey mattered.
###### Reward and Return
- **Vex Recognition** — Area: Authored area
  - Build/Visual: Create one clear Vex presentation position and reward reveal area.
  - Build/Visual: Display the Clockwork Wayfinder as cosmetic recognition only.
  - Gameplay Function: Closes the guide relationship and names the player’s achievement.
- **Lobby Return** — Area: Authored area
  - Build/Visual: Build a clear return gate/portal and isolate it from active lane content.
  - Build/Visual: Keep all ending objects and visual states inside reset ownership.
  - Gameplay Function: Ends the session safely and supports immediate reuse.

##### Important Build Notes

- **No Fifth Objective** — The ending is presentation, save, reward, return, and reset only; it adds no new challenge or Objective Score.
- **Reward Readability** — Clockwork Wayfinder must be clearly presented as the one-time completion reward.
- **Safe Return** — The return route cannot reopen gameplay hazards or expose another lane.
- **Reset-Owned Presentation** — Orrery callbacks, Vex position, reward visuals, doors, lights/audio/particles, and ending markers must reset cleanly.

#### Developer

Implement one interruption-safe ending sequence, synchronized vault callbacks, Vex closing dialogue, one-time Clockwork Wayfinder reward, session completion/save, safe return, cleanup, and assigned-lane reset. No additional Objective Score is created.

##### Development Flow

- **Ending Setup** — Begin only after valid Workshop completion, lock puzzle input, position the player safely, and initialize one ending state.
- **Vault Activation** — Trigger Orrery and vault-system callbacks in authored order using lane-owned visuals/audio.
- **Reward and Save** — Run Vex recognition, secure the four-objective session result, and grant Clockwork Wayfinder exactly once with retry-safe delivery.
- **Return and Reset** — Return the player only after safe save/retry handling, clear temporary state, verify all station resets, and release lane ownership.

##### Development Requirements

###### Ending Setup
- **Sequence Control**
  - Requirement: Begin only after Ring 3 completion.
  - Requirement: Lock puzzle inputs, maintain safe player control, and prevent duplicate ending starts.
  - Requirement: Use script-owned timing so pause/interruption behavior remains deterministic.
  - Gameplay Function: Creates one authoritative closing state.
- **Cross-System Callbacks**
  - Requirement: Trigger Orrery alignment followed by Workshop, inner gate, Resonance Engine, and Great Hall activation.
  - Requirement: Use lane-owned effects and prevent cross-lane visibility/audio leakage.
  - Gameplay Function: Shows the complete restoration without replaying gameplay.
###### Completion and Return
- **Reward and Session Save**
  - Requirement: Trigger Vex closing dialogue and the Clockwork Wayfinder once.
  - Requirement: Mark session complete, save objective results, and send all remaining raw events.
  - Requirement: Do not add another objective score.
  - Gameplay Function: Finalizes the story and persistence boundary.
- **Lobby Return and Reset**
  - Requirement: Open the return route only after save acknowledgement or safe retry queue.
  - Requirement: Transfer the player to lobby, clear inventory/effects/permissions, and release lane ownership.
  - Requirement: Reset all five station cells and ending states in under 30 seconds.
  - Gameplay Function: Supports reliable back-to-back sessions.
###### Data and Recovery
- **Ending Events**
  - Requirement: Record ending enter, Orrery activation, each system callback, reward trigger, session completion, final send status, lobby return, and reset status.
  - Requirement: If disconnected during ending, keep completion state and finish reward/session delivery safely on rejoin or platform retry.
  - Gameplay Function: Prevents completion loss at the final boundary.

##### Completion and Data

- **Vault Restored Session Completion** — No Objective Score
  - Completion: The four objective station results are secured, the ending sequence reaches its completion boundary, and the player enters the safe return flow.
  - Recorded Data: Four Objective Scores/component records, session completion, reward grant state, ending callbacks, final send/retry state, lobby/holding-area return, reset verification, and lane release.
  - Incomplete Session: If disconnected after Workshop completion, preserve the completed objective state and finish reward/session delivery safely on rejoin or platform retry; do not replay or double-grant the ending.
  - Duplicate Prevention: Ending start, session completion, final send, Clockwork Wayfinder grant, and lane release are idempotent per session.
  - Final Result: Closes the session containing the four Objective Scores; no Ending Objective Score is added.
  - Player-Facing Result: Show the restoration payoff, Vex recognition, reward, and return cues; do not expose platform scoring/analysis.
  - Telemetry / Export: Export ending callbacks, session completion, reward/save/retry state, return, and reset verification; no new objective score.

##### Reset / Interruption

- Clear temporary inventory/effects/permissions and restore every objective cell plus ending-specific doors, Vex/Gremlin/Orrery presentation state, lights/audio/particles, reward markers, and return-route state.
- Keep the lane unavailable until reset verification confirms every station is back at its authored starting condition.
- **Reset Result:** The completed player is safely returned and the assigned Clockwork lane is verified reusable-ready.

##### Important Development Notes

- **Reward Exactly Once** — Clockwork Wayfinder grant is idempotent and cannot duplicate on retry/rejoin.
- **Retry-Safe Final Save** — Final session transmission may retry without duplicating completion or reward state.
- **No Additional Score** — The ending stores the four-objective session result and adds no fifth Objective Score.
- **Reset Before Availability** — Lane availability is advertised only after all objective and ending states verify clean.

##### Acceptance

- Vault Restored reaches its defined end condition without creating an unrecoverable player state.
- Vault Restored preserves the approved player-facing behavior, data/result boundary, and lane isolation rules.
- Vault Restored reset restores the authored starting state before the assigned lane is reused.

##### Terms

- **Session result** — The stored completion record containing raw completion and reward state, not a player-facing score
- **Pending Recovery Record** — The fallback record created when primary session storage cannot complete
- **Idempotent reward** — A reward operation that cannot grant the same cosmetic reward twice
- **Lane verification** — The checks confirming that the completed lane is clean before reuse

## Production Assets

### Voice Requirements

Source PRD revision: 1.0.0
Voice system: Custodian Vex · direct in-world guide across the vault; no radio/communicator layer

#### 01. The Antechamber

##### VO-ANTE-01 — Vault Restoration Briefing
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

##### VO-ANTE-02 — Custodian Key Reminder
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

#### 02. The Resonance Engine

##### VO-RES-01 — Experiment Before the Target
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

#### 03. The Broken Gallery

##### VO-GAL-01 — Carry the Key Across
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

##### VO-GAL-02 — Checkpoint 3 Collapse Warning
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

#### 04. The Warden Halls

##### VO-WARD-01 — Echo Pebble Rule Briefing
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

##### VO-WARD-02 — The Wardens Still Serve
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

#### 05. The Gremlin’s Workshop

##### VO-WORK-01 — Build One Live Network
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

##### VO-WORK-02 — Gremlin Sabotage Reaction
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

##### VO-WORK-03 — Highlight-Only Assist
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

#### 06. Vault Restored

##### VO-END-01 — The Vault Is Awake
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

##### VO-END-02 — Safe Return Cue
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
