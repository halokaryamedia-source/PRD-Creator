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
2. **The Resonance Engine** — Search scattered books to discover the hidden Left and Right target colors and which pillar must pulse, then experiment with the three pillar controls until the Engine matches the final state.
3. **The Broken Gallery** — Cross three route-selection levels by searching checkpoint barrels, repairing only marked gaps, managing limited blocks/ladders, and surviving the final Gremlin time challenge.
4. **The Warden Halls** — Cross three trap checkpoints using the Echo Pebble against wall-laser systems while avoiding floor traps and timing swinging ceiling axes.
5. **The Gremlin’s Workshop** — Route continuous power from the Generator through Ring 1, Ring 2, and Ring 3, repairing the network each time the Gremlin disrupts an earlier connection.
6. **The Vault Awakens** — Awaken the Great Orrery, reopen the century-sealed gateway, complete the story, and return safely.

#### Global Gameplay Direction

- **Learn Inside the Vault** — Each mechanic teaches its own rule. Outside redstone or crafting knowledge is not required.
- **Authored and Readable Challenges** — Pillar mappings, route viability, trap behavior, and Gremlin sabotage follow authored states rather than hidden runtime randomness.
- **Checkpoint Recovery** — Mistakes cost time, resources, route availability, or position. Objective 3 may deplete gameplay health, but recovery returns the player to the active checkpoint rather than restarting the full journey.
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
  - The journey proceeds through four gameplay objectives—Resonance Engine, Broken Gallery, Warden Halls, and Gremlin’s Workshop—before the restored Orrery opens the ending sequence.
- **Transition:** Vex directs the player to the central pedestal. Taking the Custodian Key activates the first seal and reveals the entrance to the Resonance Engine. From this point forward, every completed objective visibly awakens another section of the vault.

#### The Antechamber

The Antechamber is a protected lobby and narrative introduction where the player first meets Custodian Vex.

- **Discovering the Clockwork Vault**
  - The Antechamber establishes the vault’s history, the century-sealed entrance, the failure of the Great Orrery, and the only possible route to freedom. The player is not tested here; the purpose is to establish motivation and make the complete journey understandable before Objective 1 begins.
- **Receiving the Custodian Key**
  - A central pedestal holds the Custodian Key. Vex explains that the key is not the exit key; it grants access to the first mechanism that must be restored. The pedestal, sealed entrance, and Objective 1 gate remain readable within the same onboarding route.
- **Opening the First Objective**
  - After the briefing, the player takes the Custodian Key and uses it on the Resonance Engine seal. The keyed gate opens and hands control directly into Objective 1.
- **Transition:** When the Custodian Key is accepted by the first seal, the Resonance Engine door opens. Vex gives a concise objective briefing and the story moves from mystery into action.

#### The Resonance Engine

The player enters a puzzle chamber containing three pillars. Each pillar has an upper lever, lower lever, pressure plate, and colored indicator lamp. Twelve books are scattered around the chamber with no required reading order.

- **Read the Partial Door Display**
  - The display near the exit reveals only one part of the required combination: the Middle pillar must be Brown. The Left color, Right color, and the one pillar that must pulse remain unknown. The display never reveals any lever combination.
- **Search Scattered Books for Missing Information**
  - The twelve books are a mixed set rather than a sequence: two explain machine rules, eight provide useful clues, and two are harmless maintenance/lore decoys. The rule books explain TOP → BOTTOM lever reading and that pressure plates control steady/pulsing behavior rather than color. The useful books gradually narrow the hidden target to Left = Orange, Right = Purple, and Pulse = Left. A player who finds useful books first may solve faster; reading all twelve is not required.
- **Experiment with the Pillars**
  - The books do not teach all twelve lever-to-color mappings. The player tries the four TOP → BOTTOM lever combinations on each pillar and reads the immediate lamp feedback to discover how that pillar produces its available colors. The pressure plate independently switches that pillar between steady and pulsing without changing the selected color.
- **Match the Hidden Final State**
  - The valid door solution is Left Orange and pulsing, Middle Brown and steady, Right Purple and steady. The player combines the book deductions with lever experimentation until all three live pillar states match this complete target simultaneously.
- **Transition:** When Left = Orange + pulse, Middle = Brown + steady, and Right = Purple + steady are confirmed together, the Resonance Engine restores, the completion boundary is secured, and the Broken Gallery opens.

#### The Broken Gallery

The Broken Gallery is a three-level route-selection challenge. Each level provides three possible routes, checkpoint-local resource barrels, and marked positions where construction blocks or ladders may be placed.

- **Level 1 — Two Viable Routes**
  - The player searches the Level 1 barrels, reads the three broken route options, and repairs only marked placement positions. The middle and right routes are viable; the left route requires more material than the available allocation. A viable Level 1 crossing requires 12 blocks. Choosing poorly may consume the available resource before the route can be finished.
- **Level 2 — One Viable Route**
  - At the second checkpoint the same loop returns with a harder resource problem. The player receives an authored allocation for a crossing that requires 20 blocks and 3 ladders. Only the right route is viable. Ladders, like blocks, can be placed only at marked authored positions.
- **Local Retry and Resource Recovery**
  - If the player exhausts the current level’s resource on an incomplete route or the configured level time expires, the player returns to that level checkpoint. Temporary blocks/ladders placed during the failed attempt are removed, the checkpoint resource search becomes available again, and completed earlier levels remain complete.
- **Level 3 — Gremlin Time Challenge**
  - All three Level 3 routes are initially viable. The player chooses one, collects the checkpoint resource, and must reach at least 50% of that route before the authored time threshold. If the threshold is missed, the player returns to Checkpoint 3, the failed route becomes unavailable for that run while an alternative remains, and the player searches for resource again before choosing another active route.
- **Transition:** Objective 2 completes when the player successfully clears Level 3 and reaches the exit into the Warden Halls. The full Gallery does not restart after a checkpoint-local failure.

#### The Warden Halls

The Warden Halls are a three-level trap maze built around wall lasers, floor traps, and swinging ceiling axes. The Echo Pebble is an unlimited tool with a 3-second cooldown between throws.

- **Learn the Three Trap Families**
  - Wall lasers communicate a visible beam/sensor state and may be crossed by timing or temporarily disabled. Floor traps are ground hazards that must be avoided. Swinging axes move across the corridor from the ceiling and must be crossed by reading their timing.
- **Use the Echo Pebble on Valid Laser Targets**
  - Throwing the Echo Pebble at an authored wall-laser sensor temporarily disables that laser. At selected encounters, the Pebble can instead strike an authored hanging stone so it drops into the beam path and blocks the laser. Floor traps and swinging axes never accept the Pebble as a disable solution.
- **Respect the Cooldown and Hazard Consequences**
  - Pebble supply is unlimited, but each throw starts a 3-second cooldown before the next throw. Laser contact deals 10 gameplay damage, Weakness II for 5 seconds, and Slowness I for 3 seconds. Floor-trap contact deals 5 gameplay damage, Slowness II for 5 seconds, and Blindness for 3 seconds. Swinging-axe contact deals 10 gameplay damage, knocks the player backward, applies Weakness II for 5 seconds, and Slowness I for 3 seconds.
- **Checkpoint Recovery**
  - Each Warden level has its own checkpoint. If gameplay health reaches zero from trap damage, the player returns to the active level checkpoint in a safe recovered state. Earlier completed Warden levels remain complete.
- **Transition:** After clearing the third trap level, the player reaches the inner gate and enters the Gremlin’s Workshop for the final restoration objective.

#### The Gremlin’s Workshop

The Workshop contains the Power Generator, three Great Orrery rings, and an authored network of power paths controlled by 90-degree L-shaped rotator junctions.

- **Level 1 — Generator to Ring 1**
  - The player learns the routing rule by rotating L-junctions until one continuous powered path reaches Ring 1. Each rotator connects exactly two orthogonal directions, so an incorrect orientation visibly interrupts the route.
- **Level 2 — Ring 1 to Ring 2**
  - The player extends the same live network from Ring 1 toward Ring 2. Earlier power must remain connected; the puzzle is cumulative rather than three unrelated ring solutions.
- **First Gremlin Sabotage — Route Swap**
  - About 20 seconds after Ring 1 and Ring 2 are successfully connected, the Gremlin disrupts the route used to reach Ring 2. The previous route receives an unmistakable blocked state, while a previously blocked alternate route opens. The player must reroute through the newly available path and restore the continuous Generator → Ring 1 → Ring 2 network.
- **Level 3 — Ring 2 to Ring 3 with Rollback Events**
  - The player continues toward Ring 3. When validated Ring 2 → Ring 3 route progress reaches 50%, the Gremlin rotates two previously correct rotators on the Generator → Ring 1 connection, forcing the player to return and repair that earlier link. At 80% progress, the Gremlin rotates three previously correct rotators on the Ring 1 → Ring 2 connection, again removing power until the player repairs the earlier network.
- **Transition:** The objective completes only when the Power Generator, Ring 1, Ring 2, and Ring 3 are all continuously connected after the sabotage events. The Great Orrery awakens and the Clockwork exit begins opening.

#### The Vault Awakens

When all three rings remain powered, the Great Orrery begins turning for the first time in centuries.

- **Awakening the Great Orrery**
  - Energy travels backward through every completed chamber: the Resonance Engine synchronizes, gallery guide lights return, Warden systems settle, and the century-sealed entrance begins unlocking. The ending confirms that the player restored one connected machine rather than completing unrelated challenges.
- **Resolving the Custodian’s Story**
  - Custodian Vex thanks the player and acknowledges that the vault was waiting for someone capable of restoring it. The player receives the Clockwork Wayfinder reward after the completion record has been saved.
- **Leaving the Clockwork Vault**
  - After the result and Clockwork Wayfinder reward state are secured, the player follows the safe return route to the Holding Area while the assigned lane begins cleanup and reset.
- **Transition:** The player exits through the reopened gateway as the Great Orrery continues operating behind them. Temporary gameplay state is cleared and the assigned lane is prepared for reuse.

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
  - Requirement: Use authored pillar mappings, route viability, route-close behavior, trap cycles/effects, and Gremlin sabotage events.
  - Requirement: Do not randomize a gameplay rule or fault effect at runtime unless an authored variant has been separately approved.
  - Result: Keeps player conditions readable and verifiable.
- **Input and Accessibility**
  - Requirement: Support keyboard, controller, and touch equally.
  - Requirement: Use simple interactions, no combat, and no vanilla-knowledge dependency.
  - Requirement: Avoid precision parkour. Objective 3 may use gameplay damage and checkpoint recovery as explicitly defined by its hazard rules.
  - Result: Preserves the intended accessible puzzle/traversal experience while respecting the approved Warden exception.
###### Delivery and QA
- **Data and Scoring Boundary**
  - Requirement: Emit raw timestamped events only.
  - Requirement: Provide enough evidence for platform-side objective scoring without showing or sending final score from the map.
  - Result: Separates gameplay implementation from platform interpretation.
- **Reset and Readiness**
  - Requirement: Reset every lane in under 30 seconds.
  - Requirement: Test pause, interruption, rejoin, timeout, completion, multi-lane load, checkpoint retry, and no-leakage behavior.
  - Result: Makes the map ready for back-to-back use.

##### Important Development Notes

- **Lane Isolation** — Every active player owns one isolated lane; visual, audio, entity, particle, and gameplay state must not leak between lanes.
- **Authored Objective Rules** — Pillar mapping, Gallery route viability, Warden trap effects, and Workshop sabotage remain reproducible for equivalent sessions.
- **Score Boundary** — The map emits raw gameplay evidence; Objective Scores are calculated outside the Minecraft experience.
- **Reusable Lane** — A lane returns to service only after objective, ending, inventory, entity, timing, temporary-block, trap, route, and sabotage states are verified clean.

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
  - Requirement: Use one persistent guide per lane with concise externalized dialogue.
  - Requirement: Pair important instructions with readable UI, in-world state, or authored presentation.
  - Requirement: Do not reveal hidden route solutions or clue answers before the player solves them.
  - Result: Provides instruction, tone, and readable setback reactions without auto-solving.
- **Inventory and Permissions**
  - Requirement: Clear and grant station-specific inventory at entry.
  - Requirement: Apply scripted break/place/interact permissions only to current station targets and marked Gallery placement positions.
  - Requirement: Remove permissions/items at exit, interruption, and reset.
  - Result: Prevents map damage and cross-station state leakage.
###### Timing and Events
- **Game-Time and Pause**
  - Requirement: Own all timers, cooldowns, and scheduled events in script game-time.
  - Requirement: Pause player/camera input, timers, Echo Pebble cooldown, trap cycles, Gallery thresholds, and Workshop sabotage at exact state.
  - Requirement: Keep absolute session hard caps according to the approved session rule.
  - Result: Makes pause deterministic without real-time drift.
- **Setback Feedback**
  - Requirement: Use telegraph → impact → Vex/UI reaction for Gallery retries, Level 3 route closure, trap damage/checkpoint recovery, and Gremlin sabotage.
  - Requirement: Ensure visual treatment carries meaning when audio is muted.
  - Result: Makes external setbacks readable and memorable.
###### Station Lifecycle
- **Boundary and Transition**
  - Requirement: Save station data, clear temporary state, close the previous route, brief the next station, and activate only after entry is safe.
  - Requirement: Complete, timeout, and interruption must use distinct exit reasons.
  - Result: Creates reliable station boundaries.
- **Rejoin Behavior**
  - Requirement: Save partial data immediately on disconnect.
  - Requirement: Mark station interrupted and restart that station from a clean valid state on rejoin while preserving earlier completed objective results.
  - Result: Protects data without resuming into invalid temporary geometry or hazard state.

##### Important Development Notes

- **Script-Owned Timing** — Use Script API / scoreboard-owned timing rather than redstone clocks for objective lifecycle and scheduled events.
- **No Hidden Runtime Rule Changes** — Gremlin events change visible route availability or rotator orientation; they do not secretly change the learned connection grammar.
- **Localization Ready** — Keep in-game strings externalized so localized copy can be added without changing gameplay logic.
- **Concurrent Lane Test** — Shared systems must remain isolated and stable with all supported lanes active together.

#### Data and Reset

Each objective records the raw gameplay events needed to reconstruct its result. Data is saved at objective boundaries and interruptions; the assigned lane is released only after temporary state is cleared, authored structures are restored, and readiness checks pass.

##### Development Flow

- **Capture** — Record session, station, action, state, pause, completion, timeout, retry, and interruption events.
- **Persist and Send** — Buffer safely, save at boundaries, and retry delivery without duplicate semantic events.
- **Clear Runtime State** — Remove inventory, permissions, entities, particles, scheduled tasks, temporary blocks, effects, and lane properties.
- **Restore and Verify** — Reload structures, restore defaults, run readiness checks, then release the lane.

##### Development Requirements

###### Event Contract
- **Common Envelope**
  - Requirement: Every event carries anonymous session ID, map ID, station ID, lane ID, build version, event name, and game-time timestamp.
  - Requirement: Do not send player name, gamertag, device identifier, platform interpretation, or final map-side score.
  - Result: Provides consistent anonymous event ownership.
- **Objective Payloads**
  - Requirement: Record Resonance clue/pillar/target states, Gallery resource/route/checkpoint states, Warden Pebble/trap/damage/recovery states, and Workshop rotator/connectivity/sabotage states.
  - Requirement: Record pause, completion, timeout, retry, and interruption fields where required.
  - Result: Provides platform scoring evidence without aggregation in-world.
###### Persistence and Delivery
- **Boundary Save**
  - Requirement: Save and send at station exit, disconnect, ending, and session end.
  - Requirement: Use idempotent event IDs or sequence numbers to prevent duplicate delivery after retry.
  - Result: Prevents loss and duplication.
- **Timing Rules**
  - Requirement: Use game-time timestamps; pause freezes gameplay timing.
  - Requirement: Record authored event state exactly, including Gallery route closure, trap contact/effects, Pebble cooldown/disable windows, Workshop route swap, and 50%/80% rotator sabotage.
  - Result: Allows fair timing and treatment verification.
###### Reset Contract
- **Script Cleanup**
  - Requirement: Cancel scheduled callbacks; clear station state, UI, effects, entities, items, permissions, scoreboards, and lane dynamic properties.
  - Requirement: Remove player-placed Gallery blocks/ladders before structure restore.
  - Result: Prevents stale runtime logic.
- **Structure Restore and Verification**
  - Requirement: Restore all station cells and ending states from approved structures.
  - Requirement: Verify doors, targets, clue/pillar states, barrels/resources, route availability, trap cycles, health/effects, rotators, sabotage flags, items, guide, and timers.
  - Requirement: Release lane only after all readiness checks pass within 30 seconds.
  - Result: Guarantees pristine reuse.
###### Failure Recovery
- **Interrupted Sessions**
  - Requirement: Preserve partial data and mark incomplete.
  - Requirement: On rejoin, restart the interrupted station from an authored clean state and retain earlier completed objective results.
  - Result: Protects evidence while avoiding corrupted temporary state.
- **Delivery or Reset Failure**
  - Requirement: Queue failed data sends for retry and keep semantic IDs stable.
  - Requirement: Keep a lane unavailable when reset verification fails and surface a technical error for staff.
  - Result: Prevents silent data loss and unsafe reuse.

##### Important Development Notes

- **Objective-Owned Payloads** — Each objective emits only the raw fields needed to reconstruct its gameplay result and authored treatment state.
- **Raw Data Stays Raw** — Platform scoring or interpretation never changes the event payload produced by the map.
- **Reset Is Runtime-Critical** — A lane is not reusable until cleanup and structure restoration complete within the approved reset target.
- **No State Carryover** — Clue/target states, route closures, trap effects, cooldowns, sabotage states, inventory, temporary blocks, and objective flags must not survive reset.

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
  - Requirement: Keep timers, entities, effects, inventory, permissions, health/recovery logic, and temporary objects owned by the active lane/objective.
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
  - Requirement: Clear temporary inventory, permissions, callbacks, effects, entities, player-placed blocks, health/recovery state, and objective-local flags.
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
  - Build/Visual: Leave enough space for dialogue-facing readability without locking movement.
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

**Context:** The Resonance Engine chamber contains three puzzle pillars with upper/lower levers, pressure plates, and colored indicator lamps. Twelve books are scattered through the chamber with no required reading order, while the door display reveals only Middle = Brown.

**Main Objective:** Use the scattered books to discover the missing Left and Right target colors and which pillar must pulse, then experiment with each pillar’s lever combinations until the machine reaches the complete hidden door solution.

**Result:** Left is Orange and pulsing, Middle is Brown and steady, and Right is Purple and steady; the Resonance Engine restores and the Broken Gallery route opens.

##### Gameplay Information

- **Game Purpose:** Create a light deduction-and-experimentation puzzle where books reveal the missing target information and direct machine testing reveals how each lever pair produces color.
- **Gameplay Time:** Approximately 9 minutes.
- **Starting Condition:** All three pillars are reset, twelve books are scattered and readable, all pressure plates begin in their authored initial state, and the door display shows only Middle = Brown with the other target information unknown.
- **End Condition:** Left = Orange + pulse, Middle = Brown + steady, and Right = Purple + steady are simultaneously active.
- **Fail Condition:** There is no permanent fail state. Lever and pressure-plate states remain reversible; at the station deadline, partial book/pillar progress is recorded and the journey follows the session timeout rule.
- **Scoring Criteria:** Objective Score 0–100 based on Pillar Completion, Clue Coverage, and Rule Application.

##### Gameplay Flow

- **Read the Partial Display** — See LEFT = ?, MIDDLE = BROWN, RIGHT = ?, and PULSE = ? near the exit.
- **Search the Scattered Books** — Find any of twelve non-sequential books: two mechanic-rule books, eight useful clues, and two harmless decoys. Useful books gradually identify Left = Orange, Right = Purple, and Pulse = Left; reading all twelve is not required.
- **Experiment with Lever Colors** — Use each upper/lower lever pair in TOP → BOTTOM order and watch immediate lamp feedback to discover which combination produces the color needed on that pillar.
- **Set the Pulse State** — Use each pillar’s pressure plate only for steady/pulse behavior. Activate the Left plate and keep Middle/Right steady.
- **Restore and Transition** — Confirm Orange pulse / Brown steady / Purple steady together, lock the solved response, save raw evidence, and open the Broken Gallery route.

#### Level Design

Build one readable deduction room where the three pillars and partial door display remain easy to compare while the twelve books are spread broadly enough to create light exploration. The books must not form a numbered, directional, or location-based reading sequence; finding useful books earlier by chance is valid.

##### Design Flow

- **Partial Target Read** — Frame the exit-side display with only Middle = Brown and unknown Left/Right/pulse fields.
- **Scattered Book Search** — Distribute twelve books across the chamber/exploration space without implying order: two rule books, eight useful clues, and two harmless decoys.
- **Pillar Experimentation** — Keep upper lever, lower lever, pressure plate, and indicator lamp visually grouped for each pillar so color discovery through testing is immediate.
- **Engine Restoration** — Synchronize Orange pulse / Brown steady / Purple steady and frame the newly opened Broken Gallery route.

##### Build Requirements

###### Pillar Puzzle
- **Right Pillar** — Area: Fixed authored station
  - Build/Visual: Provide one upper lever, one lower lever, one pressure plate, and one indicator lamp.
  - Build/Visual: Support Red, Yellow, Green, and Purple outputs plus clearly readable steady/pulsing presentation.
  - Gameplay Function: Provides the Right target, which must finish as Purple + steady.
- **Middle Pillar** — Area: Fixed authored station
  - Build/Visual: Provide one upper lever, one lower lever, one pressure plate, and one indicator lamp.
  - Build/Visual: Support Blue, Dark Blue, Brown, and Dark Green outputs plus clearly readable steady/pulsing presentation.
  - Gameplay Function: Provides the only target color revealed by the door display and must finish as Brown + steady.
- **Left Pillar** — Area: Fixed authored station
  - Build/Visual: Provide one upper lever, one lower lever, one pressure plate, and one indicator lamp.
  - Build/Visual: Support Pink, Orange, White, and Black outputs plus clearly readable steady/pulsing presentation.
  - Gameplay Function: Provides the hidden Left target and must finish as Orange + pulse.
###### Clues and Partial Target
- **Twelve Scattered Books** — Area: Chamber-wide exploration space
  - Build/Visual: Provide two mechanic-rule books, eight useful clue books, and two harmless decoy books; every book is one short paragraph.
  - Build/Visual: Scatter them without numbering/location sequence. Keep them readable/retrievable without hidden parkour; a lucky player may encounter useful books before decoys.
  - Build/Visual: Decoys may contain ordinary maintenance/lore notes but cannot contradict or falsify puzzle information.
  - Gameplay Function: Helps the player infer the missing target facts without requiring all twelve books or teaching the full lever-to-color table.
- **Partial Door Display** — Area: Near the exit
  - Build/Visual: Show LEFT = ?, MIDDLE = BROWN, RIGHT = ?, and PULSE = ? while the puzzle is unsolved.
  - Build/Visual: Do not expose Orange, Purple, Left pulse, or any lever combination before valid completion.
  - Gameplay Function: Gives one anchor fact and defines which missing information the player must discover.
###### Feedback and Transition
- **Immediate Pillar Feedback** — Area: Each pillar
  - Build/Visual: Every lever change updates that pillar’s color immediately; every plate interaction switches only its steady/pulsing state.
  - Build/Visual: Color and pulse must remain distinguishable with audio muted.
  - Gameplay Function: Lets the player discover the fixed lever mapping through experimentation after the book clues identify the target.
- **Engine Completion / Exit** — Area: Exit frame
  - Build/Visual: Show all three pillars synchronizing only after Orange pulse / Brown steady / Purple steady is reached.
  - Build/Visual: Keep all books, lever states, plates, lamps, FX, and door state inside reset ownership.
  - Gameplay Function: Converts puzzle completion into visible vault restoration.

##### Important Build Notes

- **Books Have No Reading Order** — Do not number, group, or place the books in a way that creates a mandatory sequence.
- **Clues Reveal Target, Not Mapping** — Book content identifies the missing target colors/pulse through understandable hints; lever-to-color behavior is learned from live experimentation.
- **Two Decoys Are Harmless** — Decoy notes contain no false puzzle information and may simply cost search/read time.
- **Steady and Pulse Are Independent** — The pressure plate changes lamp behavior without changing its selected color.

#### Developer

Implement the fixed three-pillar lever mapping, fixed hidden final target, partial door display, non-sequential twelve-book set, independent steady/pulse state, immediate feedback, platform-side scoring evidence, interruption handling, and full reset.

##### Development Flow

- **Mechanic Setup** — Initialize the three pillars, fixed final target, partial display, twelve book IDs, lever states, plate states, lamps, permissions, and timer.
- **Books and Experimentation** — Record unique book reads, keep completion independent of reading all twelve, resolve lever combinations with immediate lamp feedback, and toggle pulse state from the matching pressure plate.
- **Completion and Data** — Validate Orange pulse / Brown steady / Purple steady atomically, store book/action/state evidence, and emit raw scoring inputs only.
- **Reset and Reuse** — Restore all lever/plate/lamp/book/display/door states and remove temporary session data before lane reuse.

##### Development Requirements

###### Pillar Mapping
- **Right Pillar Mapping**
  - Requirement: Read the lever pair upper then lower.
  - Requirement: Resolve ON/ON → Red, OFF/OFF → Yellow, ON/OFF → Green, OFF/ON → Purple.
  - Requirement: Update the live right-pillar lamp immediately after a valid lever change.
  - Gameplay Function: Provides a fixed machine behavior the player can discover through testing; the final Right target is Purple.
- **Middle Pillar Mapping**
  - Requirement: Read the lever pair upper then lower.
  - Requirement: Resolve ON/ON → Blue, OFF/OFF → Dark Blue, ON/OFF → Brown, OFF/ON → Dark Green.
  - Requirement: Update the live middle-pillar lamp immediately after a valid lever change.
  - Gameplay Function: Provides a fixed machine behavior the player can discover through testing; the displayed Middle target is Brown.
- **Left Pillar Mapping**
  - Requirement: Read the lever pair upper then lower.
  - Requirement: Resolve ON/ON → Pink, OFF/OFF → Orange, ON/OFF → White, OFF/ON → Black.
  - Requirement: Update the live left-pillar lamp immediately after a valid lever change.
  - Gameplay Function: Provides a fixed machine behavior the player can discover through testing; the hidden Left target is Orange.
###### Plate and Target State
- **Steady / Pulse State**
  - Requirement: Bind one pressure plate to each pillar.
  - Requirement: A valid plate interaction switches only that pillar between steady and pulsing; it must not alter the selected color.
  - Requirement: The final target requires Left pulsing and Middle/Right steady.
  - Gameplay Function: Adds the independent pulse dimension that the player must infer from the clue books.
- **Partial Door Display and Target Validation**
  - Requirement: While unsolved, expose only Middle = Brown plus unknown Left, Right, and Pulse fields.
  - Requirement: Store the fixed complete target as Left Orange + pulse, Middle Brown + steady, Right Purple + steady.
  - Requirement: Re-evaluate the full target after every valid pillar state change and complete only when all three states match simultaneously; completion is idempotent.
  - Gameplay Function: Preserves the deduction gap while keeping one deterministic completion boundary.
###### Books, Timeout, and Recovery
- **Book Set and Tracking**
  - Requirement: Provide twelve scattered, order-independent book sources: two rule books, eight useful clue books, and two harmless decoys.
  - Requirement: Rule books explain TOP → BOTTOM lever reading and pressure-plate pulse behavior. Useful clues narrow Left → Orange, Right → Purple, and Pulse → Left without explicitly stating the final answers. Decoys contain no false puzzle facts.
  - Requirement: Record first read/open evidence per book source, but never require all twelve books—or any fixed reading sequence—for valid completion.
  - Gameplay Function: Supports exploration/clue-coverage evidence while allowing luck and deduction to change solve speed.
- **Timeout / Interruption**
  - Requirement: At station timeout, preserve book coverage, final lever/plate/lamp states, target-match state, and action history for platform handling.
  - Requirement: On interrupted restart, restore the objective to its authored initial state while retaining earlier completed objective results.
  - Gameplay Function: Protects partial evidence without resuming an ambiguous machine state.

##### Scoring Setup

- **Resonance Engine Score** — 0–100 — 64% Pillar Completion + 16% Clue Coverage + 20% Rule Application
  - **Pillar Completion (64%)** — Award proportionally from correct progress toward Orange pulse / Brown steady / Purple steady; full value requires all three final pillar states together.
  - **Clue Coverage (16%)** — Award proportionally from unique authored books opened/read during the objective, capped at the twelve available books. Reading all twelve is not a completion requirement.
  - **Rule Application (20%)** — Award from evidence that the player converts discovered target information into purposeful lever/plate experimentation and avoids an extended repeated-action loop after demonstrating the needed mapping.
  - **Timer Start:** Start when Resonance Engine interaction becomes active.
  - **Timer Stop:** Stop when the complete hidden target is confirmed or at the approved station deadline; pause time is excluded.
  - **No-Score Condition:** Do not create a completed Objective Score if the station boundary record cannot be secured; preserve raw partial evidence for platform handling.
  - **Duplicate Prevention:** Pillar completion and objective export are idempotent per session.
  - **Final Result:** One of four Objective Scores; the session result combines the four objective results after the Workshop.
  - **Player-Facing Result:** Do not display the calculated score in-game; show only book, pillar, partial-target, and completion feedback.
  - **Telemetry / Export:** Export unique book reads, lever states, plate states, lamp color/pulse states, partial-display state, target-match transitions, timeout/completion, and component inputs; no final score field from the map.

##### Reset / Interruption

- Restore all six lever states, three pressure-plate states, three indicator lamps, partial target display, twelve book sources, timer, inventory/effects, and permissions.
- Verify no solved/display/lamp state from the previous run remains before the lane becomes reusable.
- **Reset Result:** The Resonance Engine returns to its authored three-pillar starting state with Middle = Brown as the only displayed target fact.

##### Important Development Notes

- **Fixed Machine Mapping** — Use the approved list-order lever-to-color mapping exactly; do not randomize it per run.
- **Books Do Not Teach the Full Mapping** — Books reveal missing target information; color mapping remains discoverable through immediate machine feedback.
- **No Mandatory Book Sequence** — Player luck may expose useful clues early, and completion is owned only by the valid final machine state.
- **Plate Does Not Change Color** — Color mapping and steady/pulse state are independent.

##### Acceptance

- The Resonance Engine reaches its defined end condition without requiring all twelve books or a fixed reading order.
- The Resonance Engine preserves the partial display, hidden Orange/Purple/Left-pulse deduction, fixed lever mapping, data/result boundary, and lane isolation rules.
- The Resonance Engine reset restores the authored starting state before the assigned lane is reused.

##### Terms

- **Pillar** — One of the three Resonance Engine puzzle stations containing an upper lever, lower lever, pressure plate, and indicator lamp.
- **Lever Combination** — The fixed TOP → BOTTOM ON/OFF pair that selects a pillar color and is discovered through experimentation.
- **Steady / Pulse State** — The independent lamp behavior controlled by that pillar’s pressure plate.
- **Clue Book** — One of twelve scattered one-paragraph books; rule and useful clue books help recover missing target information while two harmless decoys add search uncertainty.
- **Partial Door Display** — The exit display that reveals only Middle = Brown and leaves Left, Right, and Pulse unknown until the puzzle is solved.
- **Final Target State** — Left Orange + pulse, Middle Brown + steady, Right Purple + steady.

### 06. The Broken Gallery

**Objective 2**

#### Gameplay Overview

**Context:** The player enters a ruined crossing divided into three checkpoint levels. Each level presents three route choices, checkpoint-local resource barrels, and marked positions where blocks or ladders may be placed.

**Main Objective:** Clear Level 1, Level 2, and the Level 3 Gremlin time challenge by choosing a viable route, using only the available resource, and reaching each next checkpoint.

**Result:** The player clears the third route level and reaches the Warden Halls entrance.

##### Gameplay Information

- **Game Purpose:** Create a route-reading and limited-resource traversal challenge where incorrect choices produce a local reset instead of permanent failure.
- **Gameplay Time:** Approximately 9 minutes.
- **Starting Condition:** Level 1 is reset, its resource barrels are available, all temporary placement positions are empty, and the three route choices are readable.
- **End Condition:** The player successfully reaches the exit beyond Level 3.
- **Fail Condition:** Resource exhaustion or configured level-time expiry resets only the active level. In Level 3, missing the 50% progress threshold additionally closes the failed route while another alternative remains. Earlier completed levels stay complete.
- **Scoring Criteria:** Objective Score 0–100 based on Objective Progress, Resource Planning, Timed-Route Adaptation, and Recovery Independence.

##### Gameplay Flow

- **Level 1 — Choose Between Two Viable Routes** — Search the checkpoint barrels, inspect three routes, and use 12 blocks on a viable middle/right crossing without wasting the allocation on the non-viable left route.
- **Reset and Relearn When Needed** — If the attempt exhausts its resource or level time, return to the current checkpoint, remove temporary placements, resupply, and try another route.
- **Level 2 — Find the Single Viable Route** — Use the authored 20-block + 3-ladder allocation; only the right route can be completed and all placements remain restricted to marked positions.
- **Level 3 — Beat the Gremlin Threshold** — Choose any initially viable route and reach at least 50% progress before the configured threshold. A failed route closes and the player returns to Checkpoint 3 to resupply and choose another active route.
- **Reach the Warden Halls** — Clear the final route, save checkpoint/resource/retry evidence, and open the next chamber.

#### Level Design

Build the Gallery as three readable route-selection levels. Every level exposes three choices while keeping the viable answer hidden from the player. Barrels, placement markers, reset geometry, and checkpoints must be readable as one repeatable local loop.

##### Design Flow

- **Level 1 — Basic Route Reading** — Present three routes with middle/right viable and left deliberately over-budget.
- **Level 2 — Block + Ladder Planning** — Present three routes with only the right route compatible with the 20-block + 3-ladder allocation.
- **Level 3 — Timed Route Commitment** — Make all three routes initially viable, then visibly close a failed route after the 50% progress deadline is missed.
- **Exit Handoff** — Frame the Warden Halls entrance as the clear destination after Level 3 success.

##### Build Requirements

###### Level 1
- **Three Route Options** — Area: First checkpoint zone
  - Build/Visual: Provide left, middle, and right route choices with clearly different broken geometry.
  - Build/Visual: Middle and right must be completable with the authored 12-block allocation; left must visibly remain unfinished if the same allocation is committed there.
  - Gameplay Function: Teaches resource viability through route choice.
- **Level 1 Barrels and Markers** — Area: Checkpoint start
  - Build/Visual: Place the resource barrels before route commitment and mark only legal placement positions.
  - Build/Visual: Do not use free-form placement surfaces outside the authored markers.
  - Gameplay Function: Keeps the challenge controlled and resettable.
###### Level 2
- **Three Route Options** — Area: Second checkpoint zone
  - Build/Visual: Provide three routes with only the right route completable from the authored allocation.
  - Build/Visual: Author the viable crossing around 20 block placements plus 3 ladder placements.
  - Gameplay Function: Increases planning difficulty while retaining the same rule.
- **Level 2 Barrels and Markers** — Area: Checkpoint start
  - Build/Visual: Provide the 20-block + 3-ladder resource loop and separate block/ladder legal placement markers where needed.
  - Gameplay Function: Makes the resource budget and ladder requirement readable.
###### Level 3
- **Three Initially Viable Routes** — Area: Third checkpoint zone
  - Build/Visual: Author three routes that can all reach the exit when completed within their intended resource/time structure.
  - Build/Visual: Provide readable progress geometry so the 50% threshold can be validated from authored route state.
  - Gameplay Function: Shifts difficulty from route correctness to timely execution.
- **Closed-Route State** — Area: Each Level 3 route
  - Build/Visual: Give every route a clear inactive/closed state that can be activated after that route fails the time threshold.
  - Build/Visual: Keep remaining active routes visually distinct after the player returns to Checkpoint 3.
  - Gameplay Function: Makes Gremlin failure persistent and understandable for the current run.
###### Retry and Exit
- **Checkpoint Retry Space** — Area: Each level start
  - Build/Visual: Keep barrel respawn/search, teleport/return position, and temporary-block cleanup inside the same local reset space.
  - Build/Visual: Do not reset earlier completed levels when the active level retries.
  - Gameplay Function: Supports fast learning loops.
- **Warden Halls Exit** — Area: End of Level 3
  - Build/Visual: Make the next chamber readable immediately after final route success.
  - Build/Visual: Keep all placed blocks/ladders, route states, barrel resources, markers, and effects inside reset ownership.
  - Gameplay Function: Defines exact objective completion and handoff.

##### Important Build Notes

- **Marked Placement Only** — Blocks and ladders may be placed only at authored positions.
- **Viability Is Developer/Designer Truth, Not Player UI** — Level 1 middle/right and Level 2 right are fixed answers but must not be directly labeled as correct in-world.
- **Local Reset Only** — Failed attempts remove current-level temporary placements and return to that checkpoint without replaying earlier levels.
- **Level 3 Route Closure Must Be Visible** — A failed timed route cannot look available after it has been closed.

#### Developer

Implement checkpoint-local barrel resources, restricted placement, fixed route viability, Level 1/2 retry, Level 3 timed route closure, platform-side scoring evidence, interruption handling, and full restoration.

##### Development Flow

- **Level Setup** — Initialize the active checkpoint, route availability, barrels/resources, placement markers, temporary blocks/ladders, timer, and player permissions.
- **Placement and Route Validation** — Accept placement only at authored markers, track resource use and route progress, and detect resource/time failure locally.
- **Level 3 Timed Adaptation** — Track the chosen route, evaluate the 50% progress threshold, close a failed route, and return the player to Checkpoint 3 for a new attempt.
- **Completion and Reset** — Record raw checkpoint/resource/retry evidence, complete after Level 3 success, and restore all three levels for reuse.

##### Development Requirements

###### Level 1 Runtime
- **Resource and Viability**
  - Requirement: Provide the authored 12-block Level 1 allocation from checkpoint barrels.
  - Requirement: Treat middle and right as viable routes and left as over-budget for that allocation.
  - Requirement: Track resource use and route progress per attempt.
  - Gameplay Function: Creates the first controlled route-selection problem.
- **Retry**
  - Requirement: If resource is exhausted before a viable crossing completes or the configured Level 1 time expires, return the player to Checkpoint 1.
  - Requirement: Remove temporary placements from that attempt and restore the Level 1 barrel resource.
  - Gameplay Function: Lets the player learn from a wrong choice without restarting the objective.
###### Level 2 Runtime
- **Resource and Viability**
  - Requirement: Provide the authored Level 2 allocation needed for 20 blocks and 3 ladders.
  - Requirement: Treat only the right route as viable for that allocation.
  - Requirement: Validate block and ladder placement only at authored markers.
  - Gameplay Function: Creates the harder single-route resource puzzle.
- **Retry**
  - Requirement: On resource exhaustion or configured Level 2 time expiry, return to Checkpoint 2 and remove only Level 2 temporary placements.
  - Requirement: Preserve completed Level 1 state.
  - Gameplay Function: Keeps progression checkpoint-local.
###### Level 3 Runtime
- **Timed Route State**
  - Requirement: Start Level 3 with all three routes active and viable.
  - Requirement: Bind the attempt to the first route the player materially commits to and evaluate progress from authored route-progress markers/state.
  - Requirement: Require at least 50% progress before the configured threshold.
  - Gameplay Function: Defines the Gremlin time challenge without hidden camera inference.
- **Route Failure and Recovery**
  - Requirement: If the threshold is missed, return the player to Checkpoint 3, remove current-attempt temporary placements, restore the resource-search loop, and close the failed route while another alternative remains.
  - Requirement: Preserve at least one retryable active route so the objective does not become unwinnable before the station timeout boundary.
  - Requirement: Record closed-route identity and the next chosen route.
  - Gameplay Function: Turns failure into persistent route knowledge and adaptation.
###### Completion and Interruption
- **Objective Completion**
  - Requirement: Complete only when the player reaches the authored exit beyond Level 3.
  - Requirement: At station timeout preserve furthest completed level, current route, resource state, closed routes, retry count, and progress evidence.
  - Requirement: On interruption restart the active objective from its authored clean state according to shared rejoin rules.
  - Gameplay Function: Creates a clear finish while retaining partial evidence.

##### Scoring Setup

- **Broken Gallery Score** — 0–100 — 40% Objective Progress + 28% Resource Planning + 24% Timed-Route Adaptation + 8% Recovery Independence
  - **Objective Progress (40%)** — Award from Level 1 completion, Level 2 completion, Level 3 progress, and final exit reach.
  - **Resource Planning (28%)** — Award from completing routes within their authored resource budgets and limiting resource-consuming wrong-route attempts.
  - **Timed-Route Adaptation (24%)** — Award from Level 3 threshold success or, after a failed route, recognizing the closure and making progress through a remaining active route.
  - **Recovery Independence (8%)** — Award from completing with fewer local resets while never removing points already earned for objective progress.
  - **Timer Start:** Start when Level 1 becomes active and its resource barrels are available.
  - **Timer Stop:** Stop on final Level 3 exit or the approved station deadline; pause time is excluded.
  - **No-Score Condition:** Do not finalize a completed Objective Score without a secured station-boundary record; preserve partial checkpoint/resource evidence for platform handling.
  - **Duplicate Prevention:** Checkpoint completion, route closure, retry reset, and Gallery completion are idempotent per session/attempt identity.
  - **Final Result:** One of four Objective Scores combined in the completed session result.
  - **Player-Facing Result:** Do not show a calculated score; show only resource, placement, checkpoint, timer-warning, route-closure, retry, and completion feedback.
  - **Telemetry / Export:** Export barrel/resource events, placement events, route choice/progress, checkpoint state, time-threshold state, route closure, retries, timeout/completion, and component inputs; no final score field.

##### Reset / Interruption

- Clear station inventory/temporary permissions and remove all player-placed blocks/ladders.
- Restore all three route levels, barrels/resources, legal placement markers, timers, closed-route states, checkpoint positions, doors, entities, lights/audio/particles, and safe return markers.
- **Reset Result:** The Broken Gallery returns to pristine Level 1 with all routes in their authored starting availability.

##### Important Development Notes

- **Blocks and Ladders Only** — Gallery construction uses checkpoint barrel blocks/ladders and authored placement markers.
- **No Free-Form Building** — Placement validation is marker-owned and fail-closed.
- **Level 3 Uses Progress State** — Do not infer the 50% threshold from player camera direction alone.
- **Raw Evidence Only** — The map records scoring inputs but sends no calculated Broken Gallery Score.

##### Acceptance

- The Broken Gallery reaches its defined end condition without creating an unrecoverable player state before the normal station timeout boundary.
- The Broken Gallery preserves the approved player-facing behavior, data/result boundary, and lane isolation rules.
- The Broken Gallery reset restores the authored starting state before the assigned lane is reused.

##### Terms

- **Route Level** — One of the three checkpoint-based Gallery challenges.
- **Viable Route** — A route that can be completed with that level’s authored resource allocation.
- **Placement Marker** — An authored position where the current block/ladder resource may legally be placed.
- **Route Closure** — The Level 3 state that makes a failed timed route unavailable for the remainder of that run while an alternative remains.

### 07. The Warden Halls

**Objective 3**

#### Gameplay Overview

**Context:** The Warden Halls are a three-level trap maze using wall lasers, floor traps, and swinging ceiling axes. Echo Pebble is unlimited but has a 3-second throw cooldown and only interacts with authored laser solutions.

**Main Objective:** Reach the inner gate by disabling or blocking selected wall lasers, avoiding floor traps, timing swinging axes, and recovering from trap damage at level checkpoints.

**Result:** The player clears all three Warden levels and the Gremlin’s Workshop route opens.

##### Gameplay Information

- **Game Purpose:** Create a readable hazard-navigation challenge where the player distinguishes Pebble-valid laser solutions from traps that must be avoided or timed.
- **Gameplay Time:** Approximately 9 minutes.
- **Starting Condition:** Warden Level 1 is reset, trap cycles are in their authored starting states, gameplay health is safe, and Echo Pebble is available.
- **End Condition:** The player clears the third trap level and enters the inner gate trigger.
- **Fail Condition:** Trap contacts apply the approved gameplay damage/status effects. If gameplay health reaches zero, the player returns to the active level checkpoint with earlier Warden levels preserved.
- **Scoring Criteria:** Objective Score 0–100 based on Objective Progress, Rule Recognition, Intentional Strategy, and Time-Loss Control.

##### Gameplay Flow

- **Read the Trap Families** — Learn that wall lasers use beam/sensor logic, floor traps must be avoided, and swinging axes must be crossed by timing.
- **Use Echo Pebble on Laser Solutions** — Hit a wall-laser sensor for a temporary disable or strike an authored hanging stone to block a beam; invalid floor/axe targets do not disable.
- **Respect the 3-Second Cooldown** — Move through the safe opening created by a valid throw while the next Pebble throw remains unavailable for three seconds.
- **Cross Three Checkpoint Levels** — Face increasingly dense trap combinations; damage/effects may slow the player, and health depletion returns only to the active Warden checkpoint.
- **Reach the Inner Gate** — Clear Level 3, save trap/Pebble/recovery evidence, and open the Workshop transition.

#### Level Design

Build three increasingly demanding maze/corridor levels using the same three trap families. Every trap needs a readable danger state, a safe observation/approach space, and enough separation to prevent unavoidable chain damage.

##### Design Flow

- **Level 1 — Learn** — Introduce laser, floor, and axe behavior in readable encounters with generous safe space.
- **Level 2 — Combine** — Mix hazard families so the player must decide when to throw, wait, avoid, or move.
- **Level 3 — Execute** — Increase density and timing pressure without changing the learned rules.
- **Inner Gate** — Provide a safe final checkpoint exit and clear Workshop handoff.

##### Build Requirements

###### Wall Laser Family
- **Laser Sensor and Beam** — Area: Authored wall encounters
  - Build/Visual: Use a visible wall-mounted sensor and beam with Active and Temporarily Disabled states.
  - Build/Visual: Make valid Echo Pebble sensor targets obvious enough to learn without marking floor/axe traps as valid.
  - Gameplay Function: Provides the primary Pebble-disable interaction.
- **Hanging Laser Blocker Stone** — Area: Selected authored laser encounters
  - Build/Visual: Place a readable hanging stone target above or near the beam path.
  - Build/Visual: A valid Pebble hit must visibly move/drop the stone into the beam so the blocked state is understandable.
  - Gameplay Function: Provides an alternate authored laser solution using the same Pebble tool.
###### Non-Pebble Hazards
- **Floor Trap** — Area: Authored floor encounters
  - Build/Visual: Make danger tiles/areas visually readable before contact and leave a safe path or timing/avoidance decision.
  - Build/Visual: Do not show a Pebble target state.
  - Gameplay Function: Tests movement awareness and imposes the approved damage/status consequence when stepped on.
- **Swinging Axe** — Area: Ceiling-mounted corridor encounters
  - Build/Visual: Use a double-sided axe or equivalent readable blade with a clear left-right swing arc and safe timing window.
  - Build/Visual: Provide approach space where the player can observe the cycle without taking unavoidable damage.
  - Gameplay Function: Creates timing pressure that cannot be bypassed with Pebble.
###### Checkpoints and Exit
- **Three Level Checkpoints** — Area: Start of each Warden level
  - Build/Visual: Provide a safe respawn/recovery position outside active trap volumes.
  - Build/Visual: Completed earlier levels must not need to be replayed after gameplay-health depletion.
  - Gameplay Function: Owns local failure recovery.
- **Inner Gate** — Area: End of Level 3
  - Build/Visual: Keep the final approach safe after the last trap and clearly reveal the Workshop route.
  - Build/Visual: Keep trap pieces, blocker stones, gates, FX, and checkpoint markers inside reset ownership.
  - Gameplay Function: Defines objective completion and handoff.

##### Important Build Notes

- **Pebble Targets Are Laser-Owned** — Only authored wall-laser sensors and authored hanging-stone targets accept Pebble as a gameplay solution.
- **Floor and Axe Never Disable** — Their challenge remains avoidance/timing even when the player throws Pebble at them.
- **Damage Must Be Readable** — Each hazard family needs distinct impact feedback before status effects alter movement/vision.
- **Checkpoint Spawn Is Safe** — Recovery positions cannot overlap active beams, floor traps, or axe arcs.

#### Developer

Implement deterministic trap cycles, unlimited Echo Pebble with a 3-second cooldown, 4-second temporary wall-laser disable windows, hanging-stone blocking interactions, exact hazard damage/status effects, checkpoint recovery, platform-side scoring evidence, interruption handling, and complete reset.

##### Development Flow

- **Mechanic Setup** — Initialize three Warden levels, checkpoints, trap instances/cycles, gameplay health/effects, valid Pebble targets, cooldown state, and permissions.
- **Pebble and Trap Interaction** — Validate throws against laser sensors/hanging stones, enforce the 3-second cooldown, and keep floor/axe targets invalid.
- **Damage and Recovery** — Apply exact hazard consequences, track gameplay-health depletion, and return the player safely to the active level checkpoint when needed.
- **Completion and Reset** — Complete on inner-gate entry, export raw trap/strategy evidence only, and restore every trap/tool/checkpoint state.

##### Development Requirements

###### Echo Pebble
- **Unlimited Tool / Cooldown**
  - Requirement: Keep Echo Pebble supply unlimited for the active objective.
  - Requirement: After every valid or invalid throw that consumes the throw action, block the next throw for 3 seconds of game-time and expose a readable recharge/ready state.
  - Requirement: Freeze/resume the cooldown with shared pause behavior.
  - Gameplay Function: Prevents spam while keeping the puzzle independent of ammunition count.
- **Valid Targets**
  - Requirement: Accept authored wall-laser sensors and authored hanging-stone targets only.
  - Requirement: On a sensor hit, disable that laser for 4 seconds of game-time before its authored cycle resumes.
  - Requirement: On a hanging-stone hit, move the authored stone into its beam-blocking state for that encounter until local reset/completion.
  - Requirement: Reject floor traps and swinging axes as disable targets.
  - Gameplay Function: Preserves the approved difference between laser solutions and avoidance/timing hazards.
###### Hazard Consequences
- **Wall Laser Contact**
  - Requirement: Apply 10 gameplay damage per valid contact tick/event according to the authored beam collision guard.
  - Requirement: Apply Weakness II for 5 seconds and Slowness I for 3 seconds.
  - Requirement: Prevent duplicate damage from one collision frame beyond the intended contact cadence.
  - Gameplay Function: Makes forcing through an active laser costly and slows immediate follow-up movement.
- **Floor Trap Contact**
  - Requirement: Apply 5 gameplay damage.
  - Requirement: Apply Slowness II for 5 seconds and Blindness for 3 seconds.
  - Requirement: Debounce one trap activation so standing on one trigger does not create unintended duplicate stacks.
  - Gameplay Function: Punishes careless footing without changing objective progress.
- **Swinging Axe Contact**
  - Requirement: Apply 10 gameplay damage and authored backward knockback.
  - Requirement: Apply Weakness II for 5 seconds and Slowness I for 3 seconds.
  - Requirement: Tie damage to the authored active swing/contact window.
  - Gameplay Function: Makes incorrect timing visibly costly and pushes the player away from the hazard.
###### Checkpoints and Completion
- **Gameplay-Health Recovery**
  - Requirement: If gameplay health reaches zero, clear invalid lingering hit states, restore the player to a safe gameplay-health/effect state, and return them to the active Warden level checkpoint.
  - Requirement: Preserve earlier completed Warden levels and reset only encounter-local states that must be replayable from the checkpoint.
  - Gameplay Function: Converts hazard defeat into local time loss rather than full-objective restart.
- **Objective Completion**
  - Requirement: Complete when the player enters the inner-gate trigger after Level 3.
  - Requirement: At station timeout preserve furthest level/checkpoint, trap contacts, effects, Pebble actions/cooldowns, and recovery count.
  - Gameplay Function: Creates a clear station boundary with meaningful partial evidence.

##### Scoring Setup

- **Warden Halls Score** — 0–100 — 40% Objective Progress + 24% Rule Recognition + 20% Intentional Strategy + 16% Time-Loss Control
  - **Objective Progress (40%)** — Award from Warden Level 1 completion, Level 2 completion, Level 3 progress, and inner-gate entry.
  - **Rule Recognition (24%)** — Award from correctly distinguishing laser Pebble solutions from floor/axe avoidance/timing and retaining that distinction across later encounters.
  - **Intentional Strategy (20%)** — Award from purposeful laser-sensor disables, blocker-stone use, safe waits/timed axe crossings, and avoidance choices rather than random Pebble spam.
  - **Time-Loss Control (16%)** — Calculate from non-pause hazard impairment/checkpoint-recovery time and repeated contact cost against the configured reference dose.
  - **Timer Start:** Start when Warden Level 1 activates and Echo Pebble becomes available.
  - **Timer Stop:** Stop on inner-gate entry or station deadline; pause time is excluded.
  - **No-Score Condition:** Do not finalize a completed Objective Score without a secured station-boundary record; partial raw progress remains available for platform handling.
  - **Duplicate Prevention:** Trap contacts, status applications, cooldown transitions, checkpoint recovery, and completion use stable session/instance identity.
  - **Final Result:** One of four Objective Scores combined in the completed session result.
  - **Player-Facing Result:** Show trap tells, Pebble target/disable/block feedback, cooldown, health/effect consequences, checkpoint recovery, and completion only; no calculated score.
  - **Telemetry / Export:** Export trap instance/type, contact/damage/effects, Pebble throw/target/result, disable/block windows, cooldowns, checkpoint/recovery, progress, timeout/completion, and component inputs; no final score field.

##### Reset / Interruption

- Clear Echo Pebble, gameplay-health/effects, cooldown, permissions, and projectile state.
- Restore every laser sensor/beam, blocker stone, floor trap, swinging axe cycle, checkpoint, gate, Vex trigger, visual/audio effect, and authored level state.
- **Reset Result:** The Warden Halls return to a clean Level 1 starting state with no previous damage, effect, cooldown, trap, or Pebble state.

##### Important Development Notes

- **3-Second Cooldown / 4-Second Laser Disable** — These are separate game-time rules and must not be conflated.
- **Exact Hazard Effects** — Use the approved damage/effect values; do not retain the previous no-damage Warden behavior.
- **No Floor-Trap Pebble Disable** — Floor traps remain avoidance hazards in gameplay, highlights, and telemetry.
- **Raw Evidence Only** — The map records scoring inputs but sends no calculated Warden Halls Score.

##### Acceptance

- The Warden Halls reaches its defined end condition using the approved checkpoint recovery behavior.
- The Warden Halls preserves exact trap consequences, Pebble scope, data/result boundary, and lane isolation rules.
- The Warden Halls reset restores the authored starting state before the assigned lane is reused.

##### Terms

- **Echo Pebble** — The unlimited throwable tool with a 3-second cooldown used only on authored laser solutions.
- **Wall Laser** — A sensor/beam hazard that may be timed, temporarily disabled, or blocked by an authored hanging stone.
- **Floor Trap** — A ground hazard that cannot be disabled by Echo Pebble.
- **Swinging Axe** — A ceiling timing hazard that swings across the player route and cannot be disabled by Echo Pebble.
- **Gameplay Health** — The Objective 3 hazard-health state whose depletion causes checkpoint recovery.

### 08. The Gremlin’s Workshop

**Objective 4**

#### Gameplay Overview

**Context:** The Workshop contains the Power Generator, three Great Orrery rings, and an authored power-routing field of 90-degree L rotators.

**Main Objective:** Keep one continuous network from Generator → Ring 1 → Ring 2 → Ring 3 while repairing the route swap and two later Gremlin rotator-sabotage events.

**Result:** Generator and all three rings are continuously powered, the Great Orrery restores, and the Clockwork exit opens.

##### Gameplay Information

- **Game Purpose:** Test power-routing understanding, memory of previously solved sections, and adaptation when an external Gremlin visibly changes the network.
- **Gameplay Time:** Approximately 9 minutes.
- **Starting Condition:** The authored routing field is reset, Power Generator and Ring 1–3 are readable, normal blockers are in their initial states, and no Gremlin event has fired.
- **End Condition:** Power Generator, Ring 1, Ring 2, and Ring 3 are all continuously connected after the 20-second route swap and 50%/80% rollback events.
- **Fail Condition:** There is no permanent fail state. Rotators remain reversible and the authored blocker changes always leave a valid route; progress may be interrupted until earlier damaged connections are repaired.
- **Scoring Criteria:** Objective Score 0–100 based on Ring Completion, Gremlin Adaptation, and Independent Progress.

##### Gameplay Flow

- **Level 1 — Power Ring 1** — Rotate 90-degree L junctions to create the first continuous route from the Generator to Ring 1.
- **Level 2 — Extend to Ring 2** — Continue the same live network from Ring 1 to Ring 2 while preserving the Generator → Ring 1 connection.
- **Route-Swap Sabotage** — About 20 seconds after Ring 2 stabilizes, the Gremlin blocks the route just used and opens a previously blocked alternate route. Reroute until Generator → Ring 1 → Ring 2 is live again.
- **Level 3 — Repair 50% and 80% Rollbacks** — Extend from Ring 2 toward Ring 3. At 50% progress, repair two rotated junctions on Generator → Ring 1; at 80%, repair three rotated junctions on Ring 1 → Ring 2.
- **Restore the Great Orrery** — Complete only when Generator and all three rings are simultaneously connected, save the full action/sabotage sequence, lock puzzle input, and begin the ending.

#### Level Design

Build a readable Workshop around the approved routing topology. Generator, live power, Ring 1–3, L-rotator orientation, normal blockers, Gremlin event blockers, and sabotage changes must remain understandable from the player’s puzzle position.

##### Design Flow

- **Level 1 — Learn the Rotator** — Present the first Generator → Ring 1 route with enough clarity to teach the L-junction rule.
- **Level 2 — Extend and Reroute** — Build the Ring 1 → Ring 2 continuation and the paired old-route-blocked / alternate-route-open sabotage state.
- **Level 3 — Backtrack Repairs** — Keep earlier Generator → Ring 1 and Ring 1 → Ring 2 sections reachable/readable when the 50% and 80% events rotate them out of alignment.
- **Orrery Payoff** — Frame the all-rings-powered state and opened exit as the final Workshop view.

##### Build Requirements

###### Core Network
- **Power Generator** — Area: Visible source position
  - Build/Visual: Provide clearly distinct offline/live/interrupted feedback and make the outgoing power direction readable.
  - Gameplay Function: Defines the start of the continuous network.
- **90-Degree L Rotators** — Area: Authored junction positions
  - Build/Visual: Every rotator must visibly connect exactly two orthogonal directions and support four readable orientations.
  - Build/Visual: Powered and unpowered states must remain distinct from the rotator’s physical orientation.
  - Gameplay Function: Provides the player’s routing interaction.
- **Ring 1, Ring 2, Ring 3** — Area: Authored milestone positions
  - Build/Visual: Each ring needs inactive/powered feedback and must remain distinguishable by position/label.
  - Build/Visual: Earlier rings must visibly lose power if a later Gremlin event breaks their actual upstream connection.
  - Gameplay Function: Shows cumulative progression from the real network state.
###### Blocker and Sabotage States
- **Normal Blockers** — Area: Authored inactive route segments
  - Build/Visual: Mark unavailable paths clearly without making them resemble powered paths.
  - Build/Visual: Support the Level 2 alternate route opening when its blocker is removed.
  - Gameplay Function: Controls which authored path is available at each puzzle state.
- **Gremlin Event Blocker / Route Swap** — Area: Level 2 active route
  - Build/Visual: After Ring 2 completion, show the previous active route becoming unmistakably blocked while the alternate route becomes available.
  - Build/Visual: Keep the change visible long enough to understand without route-coordinate UI.
  - Gameplay Function: Forces the first reroute.
- **50% and 80% Rotator Changes** — Area: Earlier solved network sections
  - Build/Visual: Keep the two Generator → Ring 1 rotators and three Ring 1 → Ring 2 rotators targeted by sabotage reachable and visually identifiable when they turn.
  - Gameplay Function: Forces the player to repair previously solved sections during Level 3.
###### Gremlin and Completion
- **Gremlin Presentation Path** — Area: Authored sightline
  - Build/Visual: Stage readable Gremlin movement/reaction for the route-swap and rollback events without requiring navigation AI.
  - Build/Visual: The visual event must never expose the exact solution route.
  - Gameplay Function: Makes every topology/orientation change feel externally caused rather than like a hidden rule change.
- **Great Orrery / Exit Frame** — Area: Completion view
  - Build/Visual: Show all three rings synchronized, restored power reaching the Orrery, and the Clockwork exit opening.
  - Build/Visual: Keep Generator, rings, rotators, blockers, Gremlin state, FX, audio, and exit markers inside reset ownership.
  - Gameplay Function: Connects puzzle completion to the story payoff.

##### Important Build Notes

- **Authored Route Topology** — Preserve the approved route topology and blocker states; player-facing communication uses in-world route states rather than coordinate labels.
- **One Continuous Network** — A ring is powered only while a real connected route from the Generator exists through all required earlier links.
- **Sabotage Is Visible** — Route blocking/opening and every forced rotator turn must be unmistakable before normal interaction resumes.
- **Connection Grammar Never Changes** — The Gremlin changes blockers/orientation, not the learned L-rotator rule.

#### Developer

Implement the approved authored routing graph, L-rotator state resolution, cumulative Ring 1/2/3 validation, 20-second route-swap sabotage, 50%/80% rollback events, platform-side scoring evidence, interruption handling, and full reset.

##### Development Flow

- **Mechanic Setup** — Initialize the authored topology, rotator orientations, blocker states, Generator, ring states, progress markers, Gremlin event flags, and interaction permissions.
- **Level 1 / Level 2 Connectivity** — Recalculate power after every valid rotation, complete Ring 1 from actual connectivity, then extend and validate Ring 2 without losing Ring 1.
- **Sabotage and Level 3** — Run the post-Ring-2 route swap, track Ring 2 → Ring 3 progress, fire the 50% two-rotator and 80% three-rotator events once, and require earlier links to be repaired.
- **Result and Reset** — Record the full rotation/connectivity/sabotage sequence, complete on all rings connected, then restore original rotators/blockers/event state.

##### Development Requirements

###### Connectivity Runtime
- **Rotator Solver**
  - Requirement: Store every authored 90-degree L rotator orientation and resolve only its two orthogonal connected sides.
  - Requirement: After every valid player or Gremlin rotation, recalculate Generator-to-network connectivity atomically before accepting the next state-dependent milestone.
  - Requirement: Update powered/unpowered visual state from actual connectivity rather than historical completion flags.
  - Gameplay Function: Creates one deterministic continuous network.
- **Ring Progression**
  - Requirement: Validate Ring 1 only from a live Generator → Ring 1 route.
  - Requirement: Validate Ring 2 only while Generator → Ring 1 → Ring 2 remains continuously powered.
  - Requirement: Level 3 begins from the restored Ring 2 network and tracks authored progress toward Ring 3.
  - Gameplay Function: Keeps progression cumulative and physically meaningful.
###### Level 2 Route Swap
- **Post-Ring-2 Sabotage**
  - Requirement: About 20 seconds after Ring 1 and Ring 2 are connected, run the Gremlin route-swap event once using game-time.
  - Requirement: Set the authored previous route segment to Gremlin-blocked/unavailable and remove/open the authored blocker that previously prevented the alternate route.
  - Requirement: Recalculate power immediately and record prior/new blocker state, lost ring power, event time, and first post-event interaction.
  - Gameplay Function: Forces the player to reroute through the newly available path without changing rotator grammar.
###### Level 3 Rollback Events
- **50% Progress Sabotage**
  - Requirement: Measure Ring 2 → Ring 3 progress from authored validated route-progress state defined by the technical layout.
  - Requirement: On first reach of 50%, rotate exactly two authored previously correct rotators on the Generator → Ring 1 route to their sabotage orientations.
  - Requirement: Recalculate power and require the player to restore the damaged earlier link before final completion can remain valid.
  - Gameplay Function: Tests awareness of the whole network, not only the newest route segment.
- **80% Progress Sabotage**
  - Requirement: On first reach of 80%, rotate exactly three authored previously correct rotators on the Ring 1 → Ring 2 route to their sabotage orientations.
  - Requirement: Recalculate power and require the player to repair that earlier connection before Ring 3 completion can resolve.
  - Requirement: Each rollback event fires once per session and remains idempotent across pause/resume.
  - Gameplay Function: Creates the final Gremlin interruption before full restoration.
###### Completion and Interruption
- **Full Network Completion**
  - Requirement: Complete only when Generator, Ring 1, Ring 2, and Ring 3 are continuously connected after all required sabotage events for the run.
  - Requirement: Lock puzzle interaction only after the valid completion record is committed, then begin the Great Orrery restoration presentation.
  - Requirement: At timeout preserve rotator orientations, blocker states, ring connectivity, route progress, sabotage-fired flags, and action history.
  - Gameplay Function: Defines the final objective boundary without bypassing a broken earlier link.

##### Scoring Setup

- **Gremlin’s Workshop Score** — 0–100 — 72% Ring Completion + 20% Gremlin Adaptation + 8% Independent Progress
  - **Ring Completion (72%)** — Award from validated Ring 1, Ring 2, and Ring 3 progression based on actual continuous connectivity, with the largest share reserved for final all-rings restoration.
  - **Gremlin Adaptation (20%)** — Award from responding correctly to the route swap, repairing the 50% Generator → Ring 1 rollback, repairing the 80% Ring 1 → Ring 2 rollback, and restoring lost power without repeatedly acting on visibly unavailable paths.
  - **Independent Progress (8%)** — Award from completing the authored routing work without an external auto-solve; normal Vex narrative/warning lines do not remove progress points.
  - **Timer Start:** Start when Workshop rotator interaction becomes active.
  - **Timer Stop:** Stop when the full Generator → Ring 1 → Ring 2 → Ring 3 network is restored or at the station deadline; pause time is excluded.
  - **No-Score Condition:** Do not finalize a completed Objective Score without a secured Workshop boundary record; preserve raw partial ring/sabotage evidence for platform handling.
  - **Duplicate Prevention:** Ring milestones, route-swap event, 50% event, 80% event, completion, and result export are idempotent per session.
  - **Final Result:** The fourth Objective Score; after Workshop completion the session result contains all four objective scores and proceeds to the ending.
  - **Player-Facing Result:** Show live power, ring states, blocked/open route changes, forced rotator changes, and completion only; no calculated score.
  - **Telemetry / Export:** Export authored layout/version identity, every player/Gremlin rotation, prior/new orientation, connectivity state, ring timestamps, blocker changes, 50%/80% event details, post-event repairs, pause, timeout/completion, and component inputs; no final score field.

##### Reset / Interruption

- Restore the original authored topology, rotator orientations, normal/event blocker states, Generator, ring states, progress markers, timers, Vex/Gremlin presentation state, lights/audio/particles, interaction locks, and permissions.
- Verify that route-swap, 50%, 80%, and completion flags are cleared before lane reuse.
- **Reset Result:** The Workshop returns to its authored Level 1 starting state with all three rings inactive and no Gremlin sabotage applied.

##### Important Development Notes

- **Three Distinct Gremlin Events** — Route swap, 50% rollback, and 80% rollback have separate one-shot state and telemetry.
- **Progress Comes From Authored Route State** — The technical layout defines exact Level 3 progress markers; do not estimate 50%/80% from camera direction or arbitrary rotation count.
- **No Legacy 3×3 Contract** — Do not reduce this revision back to the previous 3×3 Straight/Elbow/Split single-fault model.
- **Raw Evidence Only** — The map records scoring inputs but sends no calculated Workshop Score.

##### Acceptance

- The Gremlin’s Workshop reaches its defined end condition with all earlier network links genuinely restored.
- The Gremlin’s Workshop preserves the approved staged sabotage behavior, data/result boundary, and lane isolation rules.
- The Gremlin’s Workshop reset restores the authored starting state before the assigned lane is reused.

##### Terms

- **Power Generator** — The source node for the complete Objective 4 network.
- **Orrery Ring** — One of the three sequential power milestones connected in order.
- **L Rotator** — A 90-degree junction that connects exactly two orthogonal directions and can be rotated by the player or scripted Gremlin event.
- **Normal Blocker** — An authored unavailable route segment that may later open during the Level 2 route swap.
- **Gremlin Event Blocker** — The visible blocked state applied to the previously active Level 2 route after sabotage.
- **Rollback Event** — A Gremlin event that rotates already-correct junctions on an earlier powered section at 50% or 80% Level 3 progress.

### 09. Vault Restored

**Ending**

#### Gameplay Overview

**Context:** The Great Orrery is restored and the vault begins returning to operation. The player enters a closing scene with Custodian Vex.

**Main Objective:** Watch the restoration payoff, receive the Clockwork Wayfinder reward, and return safely to the holding area.

**Result:** The player sees the vault awaken, receives Clockwork Wayfinder once, and returns safely. The ending adds no Objective Score.

##### Gameplay Information

- **Game Purpose:** Resolve the story and close the session without exposing platform scoring/analysis or adding another gameplay challenge.
- **Gameplay Time:** Part of the approximately 5-minute transition and closing-scene allowance.
- **Starting Condition:** Valid Objective 4 completion and the all-rings-powered Great Orrery restoration event are secured.
- **End Condition:** Session data is secured, Clockwork Wayfinder is delivered once, the player returns to the holding area, and the assigned lane is reusable-ready.
- **Fail Condition:** Completed objective progress is preserved. Reward/save retries are idempotent, and a failed lane reset keeps that lane unavailable until it is clean.
- **Scoring Criteria:** No new Objective Score. The ending closes the completed four-objective session.

##### Gameplay Flow

- **Orrery Alignment** — See all three rings synchronize and release power into the restored Great Orrery.
- **Vault Awakens** — Watch coordinated callbacks from the Workshop, inner gate, Resonance Engine, and Great Hall as restored systems respond.
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
  - Requirement: Begin only after valid Objective 4 all-rings connectivity completion.
  - Requirement: Lock Workshop inputs, maintain safe player control, and prevent duplicate ending starts.
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

- **Session result** — The stored completion record containing raw completion and reward state, not a player-facing score.
- **Pending Recovery Record** — The fallback record created when primary session storage cannot complete.
- **Idempotent reward** — A reward operation that cannot grant the same cosmetic reward twice.
- **Lane verification** — The checks confirming that the completed lane is clean before reuse.

## Production Assets

### Non-Voice Requirements

#### Global / Shared Assets

##### Gameplay Flow 01 — Shared Characters
For: Reusable Vex and Gremlin character assets used across the story.
Trigger: Referenced whenever Custodian Vex or Gremlin appears in a gameplay flow.
Player Experience: Vex reads as the consistent guide while Gremlin reads as the recognizable mischievous saboteur.
Uses: Custodian Vex; Gremlin
Done When:
- Vex supports the current idle, speaking, alert, guidance, and completion states used by the approved Voice lines.
- Gremlin supports appear, sabotage, taunt, and outsmarted/defeat reaction states.
- Both characters stay visually and audibly distinct and can be reused by every referenced flow without duplicate implementations.


##### 3D Models

###### Custodian Vex
Flow: 01 — Shared Characters
Type: ENTITY / MODEL
Create: Create one reusable Custodian Vex NPC/model setup.
Used: Across the story wherever Custodian Vex appears.
Moment: Throughout Project
Includes: NPC model/texture; idle and speaking states; required authored character animations.
Group: 01 — Shared Characters
For: Vex’s reusable in-world character asset.
Requirement: Create or reuse one Clockwork-compatible Custodian Vex NPC presentation for all required story, briefing, warning, reminder, and ending moments. Vex must remain visually recognizable across the complete journey and support readable idle, speaking, pointing/highlight, alert, and completion-reaction states without changing gameplay rules.
Usage: Shared across the Antechamber, Objectives 1-4, and the ending wherever canonical Voice Production is triggered.

###### Gremlin
Flow: 01 — Shared Characters
Type: ENTITY / MODEL
Create: Create one reusable Gremlin NPC/model setup.
Used: During the Broken Gallery challenge and Workshop sabotage moments.
Moment: Throughout Project
Includes: Character model/texture; appearance/movement states; sabotage and reaction animations.
Group: 01 — Shared Characters
For: Gremlin’s reusable in-world sabotage character.
Requirement: Create one small Clockwork Gremlin character used for authored sabotage moments. It needs a readable mischievous traversal/arrival state and a clear sabotage action that can be synchronized with route blocking, rotator changes, and the relevant warning presentation. It does not require navigation AI; authored movement is sufficient.
Usage: Used for the Objective 2 final time-challenge framing and the Objective 4 sabotage sequences.

#### The Antechamber

##### Gameplay Flow 01 — Arrival & Briefing
For: Opening story and the Custodian Key reveal.
Trigger: The assigned player enters the protected Antechamber and Custodian Vex activates for the first time.
Player Experience: The player understands why the vault is sealed, what the Great Orrery is, and sees the Custodian Key as the first actionable object.
Uses: Custodian Vex; Custodian Key
Done When:
- Vex opening briefing plays once for the current session.
- The Custodian Key is clearly visible and available after the briefing.
- The player understands the key starts the restoration route and is not the exit key.

##### Gameplay Flow 02 — Take Key & Open Seal
For: Key handoff and opening of the Resonance Engine.
Trigger: The opening briefing is complete and the Resonance Engine seal is still closed.
Player Experience: The player takes the key, receives only the minimum reminder if needed, uses the key on the marked seal, and sees the first objective route open.
Uses: Custodian Vex; Custodian Key; Resonance Engine seal
Done When:
- The exact key prompt remains readable until valid seal activation.
- Valid Custodian Key use opens the Resonance Engine seal once and gives clear feedback.
- The handoff into Objective 1 is readable and does not become a separate puzzle.


##### 3D Models

###### Custodian Key
Flow: 01 — Arrival & Briefing
Type: ITEM
Create: Create one reusable Custodian Key item setup.
Used: At the opening pedestal and first seal.
Moment: Objective Start
Includes: Item appearance; readable pickup/pedestal state; accepted state at the first seal.
Group: 01 — Opening Story
For: The story key used to open the first seal.
Requirement: Create one clearly readable key item for the opening progression. It needs available/picked-up/accepted states and must visually belong to the Clockwork Vault rather than resemble an ordinary reward item.
Usage: Presented on the Antechamber pedestal and accepted by the Resonance Engine seal.

##### UI & Information

###### Custodian Key Prompt
Flow: 02 — Take Key & Open Seal
Type: UI / TEXT
Create: Create the exact player-facing Custodian Key Prompt.
Used: When the player must take the Custodian Key.
Moment: Take Key & Open Seal
Group: 02 — Open First Seal
For: Point the player toward the first seal.
Requirement: Keep the prompt short and fully in-world.
Content:
```text
TAKE THE CUSTODIAN KEY
The first seal is waiting.
```

##### Visual Effects & Presentation

###### Resonance Engine Seal Opening
Flow: 02 — Take Key & Open Seal
Type: SEQUENCE
Create: Create one authored Resonance Engine Seal Opening sequence.
Used: When the Custodian Key is accepted by the first seal.
Moment: Take Key & Open Seal
Group: 02 — Open First Seal
For: Show the first seal accepting the key and opening the Resonance Engine entrance.
Requirement: Use one short presentation sequence: the seal responds, the door unlocks, and the route ahead becomes obvious. Any sound is a separate SFX asset if produced.
Usage: Plays once when the Custodian Key is accepted.

#### The Resonance Engine

##### Gameplay Flow 01 — The Door Remembers
For: Introduce the incomplete answer and the mystery of the chamber.
Trigger: The Resonance Engine seal opens and the player gains control inside the reset chamber.
Player Experience: The player immediately sees the basic task and the intentionally incomplete target: Middle is Brown while Left, Right, and Pulse remain unknown.
Uses: Custodian Vex; Objective 1 Instruction Panel; Partial Door Target Display
Done When:
- The instruction text is readable and does not reveal the hidden Left/Right colors, pulse location, or lever solutions.
- The door display shows Middle = Brown and keeps the other target values unknown.
- Vex briefing matches the same information and does not contradict the display.

##### Gameplay Flow 02 — Search the Chamber
For: Clues left behind by the vault’s former keepers.
Trigger: Objective 1 is active and the twelve scattered books are available around the chamber.
Player Experience: The player searches books in any order, may find useful clues early by luck, and gradually narrows the missing target information without needing every book.
Uses: Scattered Clue Book Set
Done When:
- All twelve approved books use the exact current text.
- The set remains 2 rule books + 8 useful clues + 2 harmless decoys with no forced reading order.
- Decoys contain no false puzzle facts and completion never requires all twelve books.

##### Gameplay Flow 03 — Tune the Pillars
For: Readable pillar feedback while the player experiments.
Trigger: The player changes a pillar lever or pressure-plate state while Objective 1 is active.
Player Experience: The player learns each pillar by experimentation: lever combinations change color and the plate changes only steady versus pulse.
Uses: Left / Middle / Right pillar labels; pillar lamps; upper/lower levers; pressure plates
Done When:
- LEFT, MIDDLE, and RIGHT identities remain clear from the player position.
- Every lever change produces immediate deterministic lamp-color feedback for that pillar.
- Pressure plates change only steady/pulse state and never change the selected color.

##### Gameplay Flow 04 — Engine Restored
For: Resonance Engine restoration and the route opening.
Trigger: Left = Orange + pulse, Middle = Brown + steady, and Right = Purple + steady are all valid at the same time.
Player Experience: The three pillars visibly synchronize, the Resonance Engine returns to operation, and attention moves to the newly opened Broken Gallery route.
Uses: Resonance Engine restoration presentation; pillar completion feedback
Done When:
- Completion validates the full simultaneous final state rather than a partial match.
- The completion response plays once and clearly confirms success.
- The Broken Gallery route opens and Objective 1 temporary state is ready for the next reset.


##### UI & Information

###### Objective 1 Instruction Panel
Flow: 01 — The Door Remembers
Type: UI / TEXT
Create: Create the exact player-facing Objective 1 Instruction Panel.
Used: When the Resonance Engine objective begins.
Moment: Objective Start
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

###### Partial Door Target Display
Flow: 01 — The Door Remembers
Type: UI / TEXT
Create: Create the exact player-facing Partial Door Target Display.
Used: Throughout Resonance Engine solving.
Moment: Throughout Objective
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

###### Scattered Clue Book Set
Flow: 02 — Search the Chamber
Type: UI / TEXT
Create: Create the exact player-facing Scattered Clue Book Set.
Used: While the player searches the Resonance Engine chamber for clues.
Moment: Search the Chamber
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

##### Visual Effects & Presentation

###### Resonance Engine Restoration
Flow: 04 — Engine Restored
Type: SEQUENCE
Create: Create one authored Resonance Engine Restoration sequence.
Used: When all three pillar states are correct.
Moment: Objective Complete
Group: 04 — Completion
For: Show the Resonance Engine returning to life.
Requirement: Create one short completion presentation that visually confirms all three pillars have synchronized and the Engine has returned to operation, then directs attention toward the newly opened Broken Gallery route.
Usage: Runs once after valid Objective 1 completion.

#### The Broken Gallery

##### Gameplay Flow 01 — Enter the Gallery
For: Introduce the collapsed Gallery and the supplies left behind.
Trigger: The player enters Broken Gallery Level 1 with checkpoint barrels and the three route choices available.
Player Experience: The player learns the repeated loop: search barrels, repair only marked gaps, reach the checkpoint, and retry only the current level on failure.
Uses: Custodian Vex; Broken Gallery Entrance Message; Repair Gap Markers
Done When:
- The route-loop instruction text is readable without revealing a viable route.
- Legal placement markers are clearly different from ordinary environment blocks.
- Vex briefing communicates limited-resource planning and local retry without introducing old mechanics.

##### Gameplay Flow 02 — First Crossing
For: First crossing through the Broken Gallery.
Trigger: Checkpoint 1 is active and Level 1 resources/routes are reset.
Player Experience: The player reads three routes, uses the 12-block allocation, and must avoid wasting supplies on the non-viable route.
Uses: First Crossing Message; checkpoint barrels; Repair Gap Markers
Done When:
- The Level 1 brief uses the exact approved text and does not reveal which two routes work.
- The authored allocation is 12 blocks and only marked placements are accepted.
- Middle and Right remain viable, Left remains non-viable, and successful crossing reaches Checkpoint 2.

##### Gameplay Flow 03 — Second Crossing
For: Second, tighter crossing through the Broken Gallery.
Trigger: Checkpoint 2 is active and Level 2 resources/routes are reset.
Player Experience: The player solves a tighter route/resource problem using 20 blocks and 3 ladders while only one route can be completed.
Uses: Second Crossing Message; checkpoint barrels; blocks; ladders; Repair Gap Markers
Done When:
- The Level 2 brief uses the exact approved text without naming the viable route.
- The authored allocation is 20 blocks + 3 ladders and placement remains marker-owned.
- Only the Right route is viable and successful crossing reaches Checkpoint 3.

##### Gameplay Flow 04 — Gremlin’s Wager
For: Gremlin’s timed final crossing.
Trigger: Checkpoint 3 is active, all three routes are initially viable, and the timed attempt begins when the player materially commits to a route.
Player Experience: The player chooses a route, hears/sees Gremlin-timed urgency, and must reach at least 50% route progress before the authored threshold.
Uses: Gremlin; Custodian Vex; Gremlin's Wager Message; Level 3 Time-Challenge Cue; route-progress state
Done When:
- The exact Level 3 instruction is readable before/during the attempt without revealing route geometry.
- The warning cue and Vex line clearly mark the timed requirement.
- At least 50% progress before the threshold preserves the chosen route and allows the crossing to continue.

##### Gameplay Flow 05 — When a Path Fails
For: Failure feedback when a route gives way.
Trigger: The active level exhausts its resources or configured time, or a Level 3 attempt misses the 50% progress threshold.
Player Experience: The player gets a local reset. Level 1/2 simply retry; Level 3 visibly loses the failed route while another alternative remains.
Uses: Crossing Failure Messages; Level Retry Reset; Gremlin Path Collapse
Done When:
- Temporary blocks/ladders from the failed attempt are removed and the active checkpoint becomes safe/retryable.
- Current-level resources become available again while earlier completed Gallery levels remain complete.
- A failed Level 3 route is visibly unavailable while alternatives remain, and the last remaining route never makes the objective unwinnable before normal timeout.


##### UI & Information

###### Broken Gallery Entrance Message
Flow: 01 — Enter the Gallery
Type: UI / TEXT
Create: Create the exact player-facing Broken Gallery Entrance Message.
Used: When the player enters the Broken Gallery.
Moment: Objective Start
Group: 01 — Shared Gallery Assets
For: Point the player toward the old supplies and the damaged crossings.
Requirement: Keep the Gallery instruction short and in-world.
Content:
```text
THE BROKEN GALLERY

The old stores still hold what you need.
Repair only the marked breaks and find a way across.
```

###### First Crossing Message
Flow: 02 — First Crossing
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

###### Second Crossing Message
Flow: 03 — Second Crossing
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

###### Gremlin's Wager Message
Flow: 04 — Gremlin’s Wager
Type: UI / TEXT
Create: Create the exact player-facing Gremlin's Wager Message.
Used: When the final Gallery crossing begins.
Moment: Gremlin's Wager — final crossing
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

###### Crossing Failure Messages
Flow: 05 — When a Path Fails
Type: UI / TEXT
Create: Create the exact player-facing Crossing Failure Messages.
Used: When a Gallery crossing attempt fails or a final route is lost.
Moment: Crossing Failure / Route Lost
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

###### Repair Gap Markers
Flow: 01 — Enter the Gallery
Type: BLOCK / PROP
Create: Create one reusable marker treatment for repairable Gallery gaps.
Used: Throughout all Broken Gallery crossings.
Moment: Throughout Objective
Includes: Visible environment marker treatment for valid repair positions.
Group: 01 — Shared Gallery Assets
For: Make repairable gaps visually distinct without putting debug text into the world.
Requirement: Use an environmental marker treatment for valid repair positions. Do not display debug-style placement text.
Usage: Visible only at authored repair positions.

##### Audio

###### Gremlin Wager Cue
Flow: 04 — Gremlin’s Wager
Type: SOUND
Create: Create one standalone Gremlin Wager Cue sound.
Used: When the final Gallery crossing begins.
Moment: Gremlin's Wager — final crossing
Group: 04 — Gremlin’s Wager
For: Gremlin-flavored warning sound as the final crossing turns dangerous.
Requirement: Create one independent short warning cue that clearly marks the start of the Level 3 progress deadline. It should read as Gremlin-triggered urgency and remain distinct from normal checkpoint, placement, or route-reset sounds.
Usage: Plays when the Level 3 authored timer begins; Voice Production may play alongside it but is owned separately.

##### Visual Effects & Presentation

###### Gremlin Path Collapse
Flow: 05 — When a Path Fails
Type: SEQUENCE
Create: Create one authored Gremlin Path Collapse sequence.
Used: When Gremlin removes a failed route in the final Gallery crossing.
Moment: Crossing Failure / Route Lost
Group: 05 — Path Failure
For: Show Gremlin taking the failed path away.
Requirement: Create one Level 3 failure presentation in which the selected failed route changes to a clearly unavailable state, the player returns to Checkpoint 3, and the remaining active routes stay readable. The Gremlin framing and warning cue may be synchronized inside this authored sequence.
Usage: Runs after a Level 3 route misses its required progress threshold while another active route remains.

#### The Warden Halls

##### Gameplay Flow 01 — Enter the Warden Halls
For: Introduce the Wardens and the Echo Pebble.
Trigger: The Warden Halls activate and the player receives the unlimited Echo Pebble before the first trap-family encounters.
Player Experience: The player understands which hazards accept Echo Pebble interaction and which must instead be avoided or timed.
Uses: Custodian Vex; Echo Pebble; Wall Laser Sensor; Swinging Axe Trap; Floor Trap; Warden Halls Entrance Message
Done When:
- The instruction panel uses the exact approved trap/Pebble rules.
- Wall lasers, floor traps, and swinging axes remain visually distinguishable.
- Nothing implies that floor traps or swinging axes can be disabled with Echo Pebble.

##### Gameplay Flow 02 — Echo Pebble
For: Echo Pebble interactions and sensor feedback.
Trigger: The player throws Echo Pebble at a valid wall-laser sensor or authored hanging-stone target.
Player Experience: A valid sensor hit creates a short four-second laser opening; selected hanging stones can instead block the beam, while the three-second throw cooldown remains readable.
Uses: Echo Pebble; Wall Laser Sensor; Laser Blocker Stone; Echo Pebble HUD
Done When:
- Each throw starts the approved 3-second cooldown and the UI returns to READY afterward.
- A valid wall-laser sensor hit disables only that laser for 4 seconds of game-time.
- Only authored hanging-stone targets create the alternate beam-blocking solution; invalid floor/axe targets do not disable anything.

##### Gameplay Flow 03 — Warden Hazards
For: Trap-hit and recovery presentation.
Trigger: The player contacts a laser, floor trap, or swinging axe, or gameplay health reaches zero from Warden hazards.
Player Experience: The player receives hazard-specific feedback/effects; zero gameplay health returns them to the current safe checkpoint instead of restarting the full objective.
Uses: Warden Hit Effects; Warden Recovery; active Warden checkpoint
Done When:
- Laser, floor, and axe contacts apply their approved damage/status effects and remain distinguishable.
- Gameplay health reaching zero returns the player to the active Warden checkpoint in a safe recovered state.
- Earlier completed Warden levels remain complete after checkpoint recovery.

##### Gameplay Flow 04 — Enter the Workshop
For: Story transition into the Workshop.
Trigger: The player clears the third Warden level and reaches the inner gate.
Player Experience: Vex acknowledges that the Wardens are still serving the vault and directs the player into Gremlin’s Workshop.
Uses: Custodian Vex; inner gate transition
Done When:
- The transition Voice plays once without replaying Pebble instructions.
- The Workshop route becomes the clear next destination.
- No Workshop sabotage is revealed before its authored trigger.


##### 3D Models

###### Echo Pebble
Flow: 01 — Enter the Warden Halls
Type: ITEM / PROJECTILE
Create: Create one reusable throwable Echo Pebble item/projectile setup.
Used: Throughout the Warden Halls.
Moment: Throughout Objective
Includes: Inventory/held appearance; projectile appearance; readable valid-hit response.
Group: 01 — Core Trap Kit
For: The throwable tool used against Warden sensors and loose stones.
Requirement: Create one small throwable pebble item, visually derived from a stone/snowball-scale projectile but clearly authored for the Clockwork Vault. It needs held/throw/projectile/valid-hit feedback and must support an unlimited-use loop with a visible 3-second cooldown. Its impact feedback must distinguish a valid wall-laser sensor or hanging-stone target from an invalid floor/axe target.
Usage: Granted for Objective 3 and removed/reset at objective exit.

###### Wall Laser Sensor
Flow: 02 — Echo Pebble
Type: ENTITY / MODEL
Create: Create one reusable wall-mounted laser sensor setup.
Used: At laser encounters throughout the Warden Halls.
Moment: Throughout Objective
Includes: Sensor model/texture; visible laser beam; active and disabled states; attached animation/sound only when part of this same setup.
Group: 01 — Core Trap Kit
For: The wall-mounted Warden target the Echo Pebble can disturb.
Requirement: Create one readable wall-mounted laser sensor/beam assembly with Active and Temporarily Disabled states. The sensor must be an obvious Echo Pebble target; a valid hit disables the beam for the approved 4-second game-time window before normal behavior resumes. Attached activation/deactivation VFX and SFX remain part of this asset.
Usage: Distributed across the three Warden levels.

###### Laser Blocker Stone
Flow: 02 — Echo Pebble
Type: ENTITY / MODEL
Create: Create one reusable hanging blocker-stone setup.
Used: At selected laser encounters that use the blocker-stone solution.
Moment: Throughout Objective
Includes: Stone model/texture; hanging state; drop/block animation.
Group: 01 — Core Trap Kit
For: A loose stone that can fall into a laser beam.
Requirement: Create one authored hanging-stone target for selected laser encounters. A valid Echo Pebble hit must cause the stone to move/drop into the beam path and visibly block the laser, creating a readable alternate solution without changing unrelated traps.
Usage: Used only at authored laser encounters that support the blocker-stone solution.

###### Swinging Axe Trap
Flow: 01 — Enter the Warden Halls
Type: ENTITY / MODEL
Create: Create one reusable ceiling-mounted swinging axe trap setup.
Used: At axe encounters throughout the Warden Halls.
Moment: Throughout Objective
Includes: Axe model/texture; ceiling mount; swing animation; reset state.
Group: 01 — Core Trap Kit
For: The ceiling hazard the player must time past.
Requirement: Create one large double-sided swinging axe trap mounted from the ceiling. It needs a clearly readable left-right swing cycle, safe timing windows, contact/knockback feedback, and a reset state. It must never appear to accept Echo Pebble disable input.
Usage: Distributed across the Warden levels as a timing hazard.

###### Floor Trap
Flow: 01 — Enter the Warden Halls
Type: ENTITY / MODEL
Create: Create one reusable floor-trap setup.
Used: At floor-trap encounters throughout the Warden Halls.
Moment: Throughout Objective
Includes: Trap model/visual; armed, triggered, and reset states.
Group: 01 — Core Trap Kit
For: The ground hazard the player must avoid.
Requirement: Create one readable floor-trap treatment with Armed, Triggered, and Reset states. It must stay visually distinct from wall sensors and must never suggest that Echo Pebble can disable it. Exact damage and status effects remain in 03 Development.
Usage: Distributed across the Warden levels as an avoid-only ground hazard.

##### UI & Information

###### Warden Halls Entrance Message
Flow: 01 — Enter the Warden Halls
Type: UI / TEXT
Create: Create the exact player-facing Warden Halls Entrance Message.
Used: When the player enters the Warden Halls.
Moment: Objective Start
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

###### Echo Pebble HUD
Flow: 02 — Echo Pebble
Type: UI / TEXT
Create: Create the exact player-facing Echo Pebble HUD.
Used: While the Echo Pebble is available.
Moment: Throughout Objective
Group: 02 — Player Communication
For: Show when the Echo Pebble can be thrown again.
Requirement: Keep the HUD state compact; the exact recharge duration stays in Development.
Content:
```text
ECHO PEBBLE · READY
ECHO PEBBLE · RECHARGING
```

##### Visual Effects & Presentation

#### The Gremlin's Workshop

##### Gameplay Flow 01 — Wake Ring One
For: Introduce the Orrery power network and the first ring.
Trigger: The player enters the Workshop and the unsabotaged L-rotator network becomes interactive.
Player Experience: The player learns that power begins at the Generator, each rotator is an L connection, and one continuous route must reach Ring 1.
Uses: Custodian Vex; Power Generator; 90-Degree Rotator Junction; Orrery Ring; Workshop Entrance Message; Orrery Ring Status
Done When:
- The instruction text explains Generator → Ring 1 → Ring 2 → Ring 3 without exposing the authored route solution.
- Each rotator has four readable orientations and powered/unpowered state is visually clear.
- Ring 1 becomes powered only when a continuous valid path exists from the Generator.

##### Gameplay Flow 02 — Wake Ring Two
For: Show the restored current reaching Ring Two.
Trigger: Ring 1 is powered and the player continues the same network toward Ring 2.
Player Experience: The player extends the existing live route while keeping Ring 1 connected; the status display reflects actual connectivity.
Uses: Power Generator; 90-Degree Rotator Junction; Orrery Rings; Orrery Ring Status
Done When:
- Ring 2 becomes powered only while Generator → Ring 1 → Ring 2 is continuously connected.
- The Orrery Ring Status immediately reflects any real loss of power rather than milestone history.
- The post-Ring-2 route-swap trigger becomes eligible only after the approved stable state.

##### Gameplay Flow 03 — Gremlin Changes the Path
For: Gremlin blocks the old route and forces a new path.
Trigger: About 20 seconds after Ring 1 and Ring 2 are continuously connected.
Player Experience: Gremlin deliberately blocks the route the player just used, a previously blocked alternate path opens, Ring 2 loses power, Gremlin taunts, then Vex gives recovery guidance.
Uses: Gremlin; Custodian Vex; Power Generator; 90-Degree Rotator Junction; Orrery Ring Status; Route Swap Message
Done When:
- The route-swap sabotage triggers once for the session.
- The old route becomes clearly unavailable, the authored alternate opens, and connectivity/power is recalculated immediately.
- The exact sabotage text plus Gremlin and Vex lines play in the intended order without revealing the solution path.
- The player can recover using the same L-rotator rule.

##### Gameplay Flow 04 — First Rollback
For: Gremlin disrupts the first powered line.
Trigger: Validated Ring 2 → Ring 3 route progress reaches 50% for the first time.
Player Experience: Gremlin rotates exactly two previously correct Generator → Ring 1 rotators, earlier power drops, Gremlin gloats, and Vex directs the player back to repair the link.
Uses: Gremlin; Custodian Vex; 90-Degree Rotator Junction; Orrery Ring Status; Ring One Power Loss Message
Done When:
- Exactly two approved Generator → Ring 1 rotators change orientation once.
- Power loss propagates immediately and the exact 50% message identifies the affected section without exposing rotator positions.
- Gremlin taunt and Vex repair guidance play without changing the learned routing rule.

##### Gameplay Flow 05 — Second Rollback
For: Gremlin disrupts the second powered line.
Trigger: Validated Ring 2 → Ring 3 route progress reaches 80% for the first time.
Player Experience: Gremlin rotates exactly three previously correct Ring 1 → Ring 2 rotators, removes earlier power again, and the player must repair that section before finishing.
Uses: Gremlin; Custodian Vex; 90-Degree Rotator Junction; Orrery Ring Status; Ring Two Power Loss Message
Done When:
- Exactly three approved Ring 1 → Ring 2 rotators change orientation once.
- The exact 80% message and visible power state make the broken earlier section clear.
- Gremlin and Vex lines play in order and the player can repair with the same L-rotator rule.

##### Gameplay Flow 06 — Wake the Great Orrery
For: Final restoration of the Great Orrery.
Trigger: Generator, Ring 1, Ring 2, and Ring 3 are all continuously connected after all authored sabotage events.
Player Experience: Gremlin realizes the player has outsmarted the sabotage, all rings synchronize, the Great Orrery returns to life, puzzle input closes, and the exit begins opening.
Uses: Gremlin; Power Generator; Orrery Rings; Great Orrery Restoration
Done When:
- Completion requires one continuous final network across Generator and all three rings.
- Gremlin’s outsmarted reaction plays once and does not replace Vex’s later ending speech.
- The final restoration presentation clearly confirms success and begins the ending/exit handoff.


##### 3D Models

###### Power Generator
Flow: 01 — Wake Ring One
Type: ENTITY / MODEL
Create: Create one reusable power-generator setup for the Orrery network.
Used: Throughout the Gremlin Workshop objective.
Moment: Throughout Objective
Includes: Model/texture; offline, live, and interrupted states; attached energy/sound only when part of this same setup.
Group: 01 — Core Network Kit
For: The visible source feeding power into the Orrery network.
Requirement: Create one central power-source machine with clearly different Offline, Live, and Power-Interrupted feedback. The output direction into the routing network must remain visually readable from the puzzle area. Attached startup/interruption SFX and energy VFX remain part of this asset.
Usage: Source of the Objective 4 continuous power network.

###### 90-Degree Rotator Junction
Flow: 01 — Wake Ring One
Type: ENTITY / MODEL
Create: Create one reusable rotator-junction setup.
Used: Throughout the Gremlin Workshop objective.
Moment: Throughout Objective
Includes: Junction model/texture; four orientations; powered/unpowered states; rotation animation.
Group: 01 — Core Network Kit
For: The reusable junction the player turns to redirect power.
Requirement: Create one reusable L-shaped power junction that rotates in 90-degree steps and connects exactly two orthogonal directions. It needs four readable orientations plus Powered and Unpowered visual states. Interaction must make the route direction legible without exposing the route solution.
Usage: Repeated at authored Objective 4 junction locations.

###### Orrery Ring
Flow: 02 — Wake Ring Two
Type: ENTITY / MODEL
Create: Create one reusable Orrery Ring setup used for all three rings.
Used: Throughout the Gremlin Workshop objective.
Moment: Throughout Objective
Includes: Ring model/texture; inactive/powered states; motion used during final restoration.
Group: 01 — Core Network Kit
For: The three visible milestones the player brings back to life.
Requirement: Create one reusable ring mechanism used as Ring 1, Ring 2, and Ring 3 with clearly readable Inactive and Powered states. The three instances must remain distinguishable by position/label while sharing one visual grammar. The final state must support all three rings operating together as the Great Orrery restoration payoff.
Usage: Sequential milestones in Objective 4 and the ending transition.

##### UI & Information

###### Workshop Entrance Message
Flow: 01 — Wake Ring One
Type: UI / TEXT
Create: Create the exact player-facing Workshop Entrance Message.
Used: When the player enters the Gremlin Workshop.
Moment: Objective Start
Group: 02 — Workshop Intro
For: Frame the final objective as bringing power back through all three rings.
Requirement: Keep connector geometry and route logic in Development.
Content:
```text
AWAKEN THE ORRERY

Carry power from the Generator through all three rings.
Keep every earlier ring alive as you move forward.
```

###### Orrery Ring Status
Flow: 02 — Wake Ring Two
Type: UI / TEXT
Create: Create the exact player-facing Orrery Ring Status.
Used: Throughout the Gremlin Workshop objective.
Moment: Throughout Objective
Group: 01 — Core Network Kit
For: Show which Orrery rings currently have power.
Requirement: Use simple in-world state words and update from actual connectivity.
Content:
```text
RING 1 · LIVE / DARK
RING 2 · LIVE / DARK
RING 3 · LIVE / DARK
```

###### Route Swap Message
Flow: 03 — Gremlin Changes the Path
Type: UI / TEXT
Create: Create the exact player-facing Route Swap Message.
Used: Immediately after Gremlin changes the route.
Moment: Route Swap — after Ring Two restoration
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

###### First Rollback Message
Flow: 04 — First Rollback
Type: UI / TEXT
Create: Create the exact player-facing First Rollback Message.
Used: When the first sabotage makes Ring One lose power.
Moment: First Sabotage — final route
Group: 04 — First Sabotage
For: Tell the player Ring One has gone dark after Gremlin's sabotage.
Requirement: Do not expose percentages, rotator counts, positions, or internal connection names.
Content:
```text
RING ONE IS DARK

Gremlin has disturbed the first line.
Bring the power back.
```

###### Second Rollback Message
Flow: 05 — Second Rollback
Type: UI / TEXT
Create: Create the exact player-facing Second Rollback Message.
Used: When the second sabotage makes Ring Two lose power.
Moment: Second Sabotage — final route
Group: 05 — Second Sabotage
For: Tell the player Ring Two has gone dark after Gremlin strikes again.
Requirement: Do not expose percentages, rotator counts, positions, or internal connection names.
Content:
```text
RING TWO IS DARK

He struck again.
Restore the earlier line.
```

##### Visual Effects & Presentation

###### Gremlin Route Swap
Flow: 03 — Gremlin Changes the Path
Type: SEQUENCE
Create: Create one authored Gremlin Route Swap sequence.
Used: When Gremlin blocks the old route after Ring Two restoration.
Moment: Route Swap — after Ring Two restoration
Group: 03 — Gremlin Route Swap
For: Show Gremlin blocking the old route and opening another.
Requirement: About 20 seconds after Ring 1 and Ring 2 are connected, run one authored Gremlin sequence that makes the previously active route become visibly blocked, makes the previously blocked alternate path visibly available, removes power where connectivity is broken, and then returns control for rerouting. The change must be understandable without exposing route coordinates or implementation labels.
Usage: Runs once per Objective 4 session after the approved Ring 2 condition.

###### First Rollback Sabotage
Flow: 04 — First Rollback
Type: SEQUENCE
Create: Create one authored First Rollback Sabotage sequence.
Used: During the first sabotage on the final route.
Moment: First Sabotage — final route
Group: 04 — First Sabotage
For: Show Gremlin disturbing the earlier line to Ring One.
Requirement: At the approved 50% Ring 2-to-Ring 3 progress trigger, run one short Gremlin disruption in which exactly two already-correct rotators on the Generator-to-Ring-1 connection visibly turn out of alignment. Power loss must propagate to the affected ring states before normal input resumes.
Usage: Runs once per Objective 4 session.

###### Second Rollback Sabotage
Flow: 05 — Second Rollback
Type: SEQUENCE
Create: Create one authored Second Rollback Sabotage sequence.
Used: During the second sabotage on the final route.
Moment: Second Sabotage — final route
Group: 05 — Second Sabotage
For: Show Gremlin disturbing the earlier line to Ring Two.
Requirement: At the approved 80% Ring 2-to-Ring 3 progress trigger, run one short Gremlin disruption in which exactly three already-correct rotators on the Ring-1-to-Ring-2 connection visibly turn out of alignment. The player must see that an earlier completed section has broken before normal input resumes.
Usage: Runs once per Objective 4 session.

###### Great Orrery Restoration
Flow: 06 — Wake the Great Orrery
Type: SEQUENCE
Create: Create one authored Great Orrery Restoration sequence.
Used: When the full Orrery network is restored.
Moment: Objective Complete
Group: 06 — Final Restoration
For: Show all three rings waking the Great Orrery.
Requirement: When Generator, Ring 1, Ring 2, and Ring 3 are continuously connected, create one strong final restoration presentation: all three rings synchronize, power visibly reaches the Great Orrery, puzzle input closes, and the Clockwork exit begins opening. Keep the transition compatible with the existing ending sequence rather than creating a fifth objective.
Usage: Runs once on valid Objective 4 completion.

#### Vault Restored

##### Gameplay Flow 01 — The Vault Awakens
For: Final restoration payoff and the Clockwork Wayfinder reward.
Trigger: The Great Orrery restoration callbacks complete and the closing scene reaches Vex recognition.
Player Experience: Vex acknowledges what the player restored, the gateway is open, and the Clockwork Wayfinder reward is presented after the completion record is secured.
Uses: Custodian Vex; Clockwork Wayfinder; Vault Restored Message; Great Orrery / gateway presentation
Done When:
- The completion message and Vex line use the exact approved wording without exposing platform scoring.
- The Clockwork Wayfinder is presented/granted exactly once after the completion state is secured.
- The reopened gateway is clearly visible as the next action.

##### Gameplay Flow 02 — The Way Home
For: Farewell and the open gateway home.
Trigger: Session result and reward state are secured and the safe return route is open.
Player Experience: Vex gives one concise farewell/navigation cue and the player follows the reopened route back to the holding area while lane cleanup begins safely.
Uses: Custodian Vex; Vault Awakening Sequence; safe return route
Done When:
- The exact safe-return Voice cue plays without repeating the completion speech.
- The return route is obvious and no new gameplay task is introduced.
- Lane reset/cleanup does not invalidate the player’s safe return and prepares the lane for reuse.


##### 3D Models

###### Clockwork Wayfinder
Flow: 01 — The Vault Awakens
Type: ITEM
Create: Create one Clockwork Wayfinder reward item/model.
Used: During the final reward reveal.
Moment: Restoration Payoff
Includes: Reward item/model appearance; readable reward reveal state.
Group: 01 — Finale
For: The cosmetic reward presented at the end of the story.
Requirement: Create one cosmetic completion reward object with a distinct Clockwork-Vault silhouette and a clear reward-reveal presentation. It does not provide new gameplay power and must support one-time grant/readability in the ending scene.
Usage: Presented after the Great Orrery restoration and granted exactly once through the existing ending flow.

##### UI & Information

###### Vault Restored Message
Flow: 02 — The Way Home
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

##### Visual Effects & Presentation

###### Vault Awakening Sequence
Flow: 01 — The Vault Awakens
Type: SEQUENCE
Create: Create one authored Vault Awakening Sequence sequence.
Used: After the Great Orrery is restored.
Moment: Restoration Payoff
Group: 01 — Finale
For: Deliver the final vault-awakening and gateway-opening payoff.
Requirement: Create one coordinated closing presentation that carries restored power from the Great Orrery into the surrounding vault, reveals the reopened exit, frames Vex's closing moment and Clockwork Wayfinder reward, then hands control to the safe return route. This sequence must remain reset-owned and must not introduce another challenge.
Usage: Runs after Objective 4 completion and before the player returns to the holding area.

### Voice Requirements

Source PRD revision: 1.0.0
Voice system: Custodian Vex · direct in-world narrative guide; Gremlin · direct in-world mischievous character in the Broken Gallery final crossing and Objective 4 sabotage; no radio/communicator layer

Voice direction: Voice exists for story, character, atmosphere, reaction, and light in-world hints. It must not read the Development specification aloud. Exact thresholds, reset logic, route viability, implementation counts, cooldown math, and other technical rules belong to Development or concise player UI when genuinely necessary.

#### 01. The Antechamber

##### VO-ANTE-01 — Vault Restoration Briefing
- Type: Main Story
- Function: story_opening
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The assigned player enters the protected Antechamber and Vex activates for the first time.
- Flow: 01 — Arrival & Briefing
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: When the story begins in the Antechamber.
- Moment: Objective Start
- Group: 01 — Opening Story
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

##### VO-ANTE-02 — Custodian Key Reminder
- Type: Direct NPC Dialogue
- Function: reminder
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: After the opening briefing, the player has not yet used the Custodian Key on the first seal.
- Flow: 02 — Take Key & Open Seal
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: While the player still needs to use the Custodian Key.
- Moment: Take Key & Open Seal
- Group: 02 — Open First Seal
- For: Give one in-world reminder that the Custodian Key belongs to the first seal.
- Purpose: Nudge the player forward without replaying the opening story.
- Must communicate:
  - The key belongs at the first seal.
- Must not add/repeat:
  - Do not mention reset, state, or objective logic.
  - Do not replay the vault history.
- Source refs:
  - content.md → The Antechamber

#### 02. The Resonance Engine

##### VO-RES-01 — The Engine Remembers
- Type: Main Story
- Function: story_hint
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Resonance Engine seal opens and the player enters the chamber with the partial door display visible.
- Flow: 01 — The Door Remembers
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: When the Resonance Engine objective begins.
- Moment: Objective Start
- Group: 01 — Chamber Guidance
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

#### 03. The Broken Gallery

##### VO-GAL-01 — The Gallery Has Fallen
- Type: Main Story
- Function: story_atmosphere
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player first enters the Broken Gallery.
- Flow: 01 — Enter the Gallery
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: When the player enters the Broken Gallery.
- Moment: Objective Start
- Group: 01 — Shared Gallery Assets
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

##### VO-GAL-02 — Gremlin's Wager
- Type: Direct NPC Dialogue
- Function: character_challenge
- Necessity: required
- Speaker: Gremlin
- Channel: Direct
- Trigger: The final Gallery crossing begins and the player is about to choose a route.
- Flow: 04 — Gremlin’s Wager
- Create: Create one Gremlin dialogue line for this gameplay moment.
- Used: When the final Gallery crossing begins.
- Moment: Gremlin's Wager — final crossing
- Group: 04 — Gremlin’s Wager
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

#### 04. The Warden Halls

##### VO-WARD-01 — The Wardens Are Listening
- Type: Main Story
- Function: story_hint
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Warden Halls activate and the player receives the Echo Pebble.
- Flow: 01 — Enter the Warden Halls
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: When the player enters the Warden Halls.
- Moment: Objective Start
- Group: 03 — Voice
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

##### VO-WARD-02 — The Wardens Still Serve
- Type: Main Story
- Function: transition
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player clears the third Warden level and the route toward Gremlin's Workshop opens.
- Flow: 04 — Enter the Workshop
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: After the final Warden section is cleared.
- Moment: Objective Complete
- Group: 05 — Transition
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

#### 05. The Gremlin’s Workshop

##### VO-WORK-01 — The Orrery's Heart
- Type: Main Story
- Function: story_reveal
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player enters the Workshop and sees the Generator and Orrery rings.
- Flow: 01 — Wake Ring One
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: When the player enters the Gremlin Workshop.
- Moment: Objective Start
- Group: 02 — Workshop Intro
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

##### VO-GREM-01 — Route Swap Taunt
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: The route-swap sabotage blocks the player's old path and opens the alternate path.
- Flow: 03 — Gremlin Changes the Path
- Create: Create one Gremlin dialogue line for this gameplay moment.
- Used: During the route-swap sabotage.
- Moment: Route Swap — after Ring Two restoration
- Group: 03 — Gremlin Route Swap
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

##### VO-WORK-02 — Ring Two Goes Dark
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Immediately after the route-swap sabotage visibly cuts power to Ring 2.
- Flow: 03 — Gremlin Changes the Path
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: Immediately after the route-swap sabotage.
- Moment: Route Swap — after Ring Two restoration
- Group: 03 — Gremlin Route Swap
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

##### VO-GREM-02 — First Rollback Taunt
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: The first rollback sabotage breaks the earlier line to Ring 1.
- Flow: 04 — First Rollback
- Create: Create one Gremlin dialogue line for this gameplay moment.
- Used: During the first sabotage on the final route.
- Moment: First Sabotage — final route
- Group: 04 — First Sabotage
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

##### VO-WORK-03 — Gremlin Strikes Back
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Immediately after the first rollback makes Ring 1 lose power.
- Flow: 04 — First Rollback
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: Immediately after the first sabotage.
- Moment: First Sabotage — final route
- Group: 04 — First Sabotage
- For: Have Vex react to Gremlin attacking the earlier line.
- Purpose: Point attention backward without reading the repair specification aloud.
- Must communicate:
  - Gremlin has gone back after the first ring.
  - The player's earlier work is being undone.
- Must not add/repeat:
  - Do not mention 50 percent, exact rotators, orientations, or implementation rules.
- Source refs:
  - content.md → The Gremlin’s Workshop → Level 3 Rollback Events

##### VO-GREM-03 — Second Rollback Taunt
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: The second rollback sabotage breaks the earlier line to Ring 2.
- Flow: 05 — Second Rollback
- Create: Create one Gremlin dialogue line for this gameplay moment.
- Used: During the second sabotage on the final route.
- Moment: Second Sabotage — final route
- Group: 05 — Second Sabotage
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

##### VO-WORK-04 — One More Sabotage
- Type: Direct NPC Dialogue
- Function: character_reaction
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: Immediately after the second rollback makes Ring 2 lose power.
- Flow: 05 — Second Rollback
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: Immediately after the second sabotage.
- Moment: Second Sabotage — final route
- Group: 05 — Second Sabotage
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

##### VO-GREM-04 — Outsmarted Reaction
- Type: Direct NPC Dialogue
- Function: completion
- Necessity: supporting
- Speaker: Gremlin
- Channel: Direct
- Trigger: The full Orrery network is restored after all sabotage events and the Great Orrery begins to wake.
- Flow: 06 — Wake the Great Orrery
- Create: Create one Gremlin dialogue line for this gameplay moment.
- Used: When the full Orrery network is restored.
- Moment: Objective Complete
- Group: 06 — Final Restoration
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

#### 06. Vault Restored

##### VO-END-01 — The Vault Is Awake
- Type: Main Story
- Function: completion
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Great Orrery restoration completes and the closing scene reaches Vex.
- Flow: 01 — The Vault Awakens
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: During the final restoration payoff.
- Moment: Restoration Payoff
- Group: 01 — Finale
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

##### VO-END-02 — The Way Home
- Type: Main Story
- Function: farewell
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The gateway is open and the player can leave the restored vault.
- Flow: 02 — The Way Home
- Create: Create one Custodian Vex dialogue line for this gameplay moment.
- Used: When the gateway home is open.
- Moment: Way Home
- Group: 01 — Finale
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
