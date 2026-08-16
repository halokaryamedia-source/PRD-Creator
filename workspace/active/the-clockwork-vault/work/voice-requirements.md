# The Clockwork Vault Voice Requirements

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

### VO-RES-02 — The Engine Answers
- Type: Main Story
- Function: transition
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Resonance Engine restores and the Broken Gallery route opens.
- Purpose: Give Objective 1 a short story payoff and a clear handoff into the next room.
- Must communicate:
  - The Resonance Engine is working again.
  - The Broken Gallery is now open/next.
- Must not add/repeat:
  - Do not repeat the pillar combination, clue logic, or lever rules.
  - Do not mention validation, reset, state, or implementation language.
- Source refs:
  - content.md → The Resonance Engine → Transition

## 03. The Broken Gallery

### VO-GAL-01 — The Gallery Has Fallen
- Type: Main Story
- Function: story_atmosphere
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player first enters the Broken Gallery.
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

### VO-GAL-03 — Across the Gallery
- Type: Main Story
- Function: transition
- Necessity: supporting
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The player clears the final Broken Gallery crossing and reaches the exit into the Warden Halls.
- Purpose: Give Objective 2 a short success beat before the next room begins.
- Must communicate:
  - The Broken Gallery crossing is complete/behind the player.
  - The Warden Halls are next.
- Must not add/repeat:
  - Do not repeat resource, route, retry, or timer rules.
  - Do not explain Warden trap solutions before the player enters the next objective.
- Source refs:
  - content.md → The Broken Gallery → Transition

## 04. The Warden Halls

### VO-WARD-01 — The Wardens Are Listening
- Type: Main Story
- Function: story_hint
- Necessity: required
- Speaker: Custodian Vex
- Channel: Direct
- Trigger: The Warden Halls activate and the player receives the Echo Pebble.
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
- Purpose: Close Vex's guide role without using session-management terminology.
- Must communicate:
  - The way home is clear.
  - Follow the gateway.
- Must not add/repeat:
  - Do not say holding area, lane, reset, cleanup, session result, or other internal terms.
  - Do not replay the completion speech.
- Source refs:
  - content.md → The Vault Awakens → Leaving the Clockwork Vault
