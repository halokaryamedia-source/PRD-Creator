# The Clockwork Vault — Bounded Gameplay Revision Review

Status: approved gameplay revision with one pending Objective 1 mapping detail

## Revision Boundary

This revision updates gameplay meaning for Objectives 1-4 and the Production Assets derived from those rules. The supplied Objective 4 HTML is a technical topology/layout reference only; coordinates, preview controls, and route-layout implementation detail do not belong in the PRD.

## Objective 1 — Resonance Engine

### Tujuan
Match the required output state across three puzzle pillars within the approximately 9-minute objective.

### Apa yang Player Lakukan
- Read short clue books distributed around the chamber.
- Operate three pillars; each pillar has an upper lever, lower lever, and pressure plate.
- Read lever state in upper-then-lower order: ON/ON, OFF/OFF, ON/OFF, or OFF/ON.
- Use lever combinations to produce the required color on each pillar.
- Use the pressure plate to switch that pillar indicator between steady and blinking.
- Compare the live pillar outputs with the required target displayed near the exit and correct the machine until all three pillars match.

### Hasil
The three required pillar states are correct, the Resonance Engine is restored, and the Broken Gallery opens.

### Level Design
- Keep all three pillars and their indicator lamps readable from the puzzle space.
- Keep clue-book searching short enough that the challenge remains deduction rather than navigation.
- Place the target display near the exit so the player repeatedly compares target and live pillar states.
- Keep the pressure-plate steady/blinking state visually distinct from the selected color.

### Developer
- Resolve each pillar from upper-lever + lower-lever combination and independent steady/blinking state.
- Provide immediate visible feedback after every valid lever or plate interaction.
- Track clue reads, pillar changes, target matches, completion, timeout, interruption, and reset.
- Retain the existing 0-100 Objective Score boundary while replacing old Target 1/Target 2 evidence with pillar completion, clue coverage, and rule-application evidence.

## Objective 2 — Broken Gallery

### Tujuan
Cross three route-selection levels by finding resources, repairing only marked positions, and reaching each checkpoint.

### Apa yang Player Lakukan
- Search barrels near each checkpoint for the authored crossing resources.
- Place blocks and ladders only on marked valid placement positions.
- Level 1: choose among three routes; two are viable and a viable route requires 12 blocks.
- Level 2: choose among three routes; only one is viable and the viable crossing requires 20 blocks plus 3 ladders.
- If a wrong route consumes the available resources or the configured level time expires, return to that level checkpoint, remove the placed temporary blocks, recollect the resources, and try another route.
- Level 3: all three routes are initially viable, but the player must reach at least 50% of the chosen route before the authored time threshold.
- If the Level 3 threshold is missed, return to Checkpoint 3, close the failed route for the rest of that run, recollect resources, and choose from the remaining active routes.

### Hasil
The player clears all three route levels and reaches the next chamber.

### Level Design
- Present three visually readable route choices at each level without revealing which route is viable.
- Keep resource barrels inside each checkpoint's reset/retry space.
- Mark every legal block/ladder placement position clearly enough to prevent free-form building.
- Level 3 must support three initially valid routes and a readable disabled state after a failed route is closed.

### Developer
- Own resource allocation and temporary placement per checkpoint.
- Reset checkpoint-local temporary blocks/resources on retry without restarting completed earlier levels.
- Level 3 owns a visible time challenge, 50% route-progress threshold, route-close event, and maximum three-route state.
- Update scoring evidence around checkpoint progress, resource planning, timed-route adaptation, and recovery independence.

## Objective 3 — Warden Halls

### Tujuan
Cross three trap checkpoints and reach the end of the maze by understanding which hazards can be disabled and which must be avoided or timed.

### Apa yang Player Lakukan
- Read and avoid three trap families: wall laser, floor trap, and swinging ceiling axe.
- Throw Echo Pebble at a wall-laser sensor to disable that laser temporarily.
- Where authored, throw Echo Pebble at a hanging stone so it drops/blocks a laser beam and creates a safe passage.
- Floor traps cannot be disabled with Echo Pebble and must be avoided.
- Swinging axes cannot be disabled with Echo Pebble and must be crossed by timing.
- Echo Pebble supply is unlimited, but each throw has a 3-second cooldown.
- If trap damage reduces gameplay health to zero, return to the active level checkpoint rather than restarting the full objective.

### Hazard Consequences
- Wall laser: 10 gameplay damage, Weakness II for 5 seconds, Slowness I for 3 seconds.
- Floor trap: 5 gameplay damage, Slowness II for 5 seconds, Blindness for 3 seconds.
- Swinging axe: 10 gameplay damage, backward knockback, Weakness II for 5 seconds, Slowness I for 3 seconds.

### Hasil
The player reaches the final checkpoint exit and gains access to Objective 4.

### Level Design
- Spread the three trap types across three increasingly demanding levels.
- Make wall-laser sensors and optional hanging-stone targets clearly readable as valid Pebble targets.
- Keep floor-trap danger areas visually readable without making Pebble appear valid on them.
- Give swinging axes readable movement arcs and safe timing spaces.

### Developer
- Enforce 3-second Echo Pebble cooldown while keeping supply unlimited.
- Validate Pebble only against authored wall-laser sensors and authored hanging-stone targets.
- Apply the exact trap damage/status effects and checkpoint recovery behavior above.
- Update scoring evidence around checkpoint progress, trap-rule recognition, deliberate Pebble/timing decisions, and time/recovery cost.

## Objective 4 — Great Orrery Power Routing

### Tujuan
Create one continuous power route from Power Generator to Ring 1, Ring 2, and Ring 3 while repairing repeated Gremlin sabotage.

### Apa yang Player Lakukan
- Rotate 90-degree L-junctions to route power through the available conduits.
- Level 1: connect Power Generator to Ring 1 and learn the rotator rule.
- Level 2: continue the live route from Ring 1 to Ring 2.
- About 20 seconds after Ring 1 and Ring 2 are connected, the Gremlin blocks the active route used to reach Ring 2 and opens a previously blocked alternate route.
- Reroute power through the newly available path and restore the continuous Generator → Ring 1 → Ring 2 network.
- Level 3: extend from Ring 2 toward Ring 3.
- At 50% progress toward Ring 3, the Gremlin rotates two already-correct rotators on the Generator → Ring 1 connection. Return and repair that earlier link.
- At 80% progress, the Gremlin rotates three already-correct rotators on the Ring 1 → Ring 2 connection. Repair the second disrupted link and finish Ring 3.

### Hasil
Power Generator, Ring 1, Ring 2, and Ring 3 are continuously connected, the Great Orrery restores, and the Clockwork exit opens.

### Level Design
- PRD describes only the player-readable power-routing rule and staged sabotage behavior.
- Do not embed grid coordinates, preview colors, route coordinates, layer geometry, or HTML control labels in PRD content.
- The exact topology/layout remains a separate supporting technical document derived from the supplied HTML reference.
- Every Gremlin event must have an unmistakable blocked/open/rotated visual state so the player understands what changed.

### Developer
- Resolve power as one continuous authored route using 90-degree L rotators.
- Trigger the first route-swap sabotage about 20 seconds after Ring 2 connection.
- Trigger the two-rotator rollback at 50% Ring 2 → Ring 3 progress and the three-rotator rollback at 80%.
- Recalculate power after each rotator change and require all earlier ring links to be restored for final completion.
- Retain the existing 0-100 Objective Score boundary while updating adaptation evidence for all three Gremlin events.

## Production Asset Scope

Prepare only gameplay-required custom assets and player-facing information. Keep normal terrain/build geometry in Level Design and keep Objective 4 grid/layout coordinates in the later technical support document.

## Saran AI

- The source lists four lever combinations and four colors for each Objective 1 pillar but does not explicitly pair them. To make the 12 clue-book texts production-ready, use list-order pairing unless the implemented puzzle uses another mapping: ON/ON → color 1, OFF/OFF → color 2, ON/OFF → color 3, OFF/ON → color 4. This is the only remaining material decision in the bounded revision.
