# Next Action

Updated: 2026-08-12

## Current Status

`PRD_GOLDEN_GUIDED_COMPLETE_PREVIEW_PROPOSAL_FLOW_LOCKED_CLOCKWORK_PREVIEW_NEXT`

Working branch: **`Local` only**.

## Current system state

The exact approved AFTERSHOCK Golden remains the canonical reference/runtime template, with the bidirectional fidelity model:

```text
Reference → Fill Map
Project Authority → Filled Golden
```

The Reverse-derived Golden fill map now serves two bounded jobs:

1. **Flow 2 completeness guide** — tells the AI what each global/objective/Gameplay/Level Design/Developer surface must eventually answer;
2. **Flow 3/4 rendering and fidelity contract** — tells the renderer/reviewer where approved meaning belongs and what visible composition must be preserved.

Golden supplies slot responsibility and reading structure. It does **not** supply Aftershock-specific facts to unrelated projects.

## Flow 2 → Flow 3 boundary

Initial PRD production now follows:

```text
Source
→ recover source-backed meaning
→ detect gaps/conflicts
→ Golden fill-map completeness pass
→ fill missing/conflicting material meaning with concrete AI proposals
→ propagate one coherent complete model
→ Simple Chat Preview
→ user correction / approval
→ promote represented proposals to approved project decisions
→ ready_for_prd
→ BUILD PRD
```

This deliberately allows the AI to make material recommendations/decisions before preview. The user reviews a **complete model**, not a list of unanswered questions.

The semantic distinction remains explicit internally:

```text
source-backed meaning = evidence from source/user authority
AI proposal          = suggested decision, pending until preview approval
```

A proposal may be specific: mechanic behavior, timing, quantity, recovery, scoring behavior, Level Design expectation, Developer behavior, naming, or another PRD-level decision. Specificity is acceptable because approval state—not vagueness—protects authority.

## Simple Chat Preview

The preview stays intentionally simple:

```text
Project Overview

Objective N
  Tujuan
  Apa yang Player Lakukan
  Hasil
  Level Design
  Developer
  Saran AI — optional, only for material choices worth calling out
```

Every objective should be filled. The detailed underlying model may contain more Golden-required meaning than is shown in the chat summary.

`Perlu Konfirmasi` is reserved for the rare case where no responsible proposal can be made because the missing answer is genuinely external/user-only or all plausible choices violate a known constraint.

User approval of the complete preview approves the represented pending proposals unless a specific proposal is corrected/rejected.

The existing `preview_approved: true` readiness gate remains unchanged.

## Clockwork real-source proof

The real non-AFTERSHOCK source remains **The Clockwork Vault - Adventure Map - Final Review.html**, whose authoritative hash matches the previous system-integration proof.

The earlier source-consistency audit found five same-authority conflicts:

1. Resonance Engine target timing/progression;
2. Broken Gallery checkpoint-vs-three-route collapse model;
3. Warden Halls Echo Pebble behavior on ceiling traps;
4. Gremlin’s Workshop permanent broken connection vs Elbow-rule inversion;
5. Ending reward name (`Clockwork Wayfinder` vs `Vault Explorer Banner`).

These are still valid source conflicts, but they are **no longer reasons to stop before preview**.

For the next live run, Flow 2 should:

```text
record each conflict
→ choose one recommended Clockwork resolution
→ propagate it through the complete objective model
→ show the resulting complete Clockwork Simple Chat Preview
→ call out the chosen resolution under Saran AI only where useful
```

The user then corrects/approves the complete model. Only after approval are those proposals promoted to project authority and used to build the Golden PRD.

## Proof boundary

This refinement changes only semantic/procedural owners and package version documentation. It does **not** add:

- a new Flow;
- a preview file/renderer;
- a new schema;
- a new approval framework;
- a new status machine;
- a Golden/template/renderer change.

The existing preview approval guard remains sufficient mechanically. The next useful proof is real use, not another framework/test layer.

## Next Step

**Run The Clockwork Vault through the revised Flow 2: use the Golden fill map to complete every material objective detail, choose concrete AI proposals for the five known conflicts and any other Golden-required gaps, then present one simple complete objective-by-objective Chat Preview for user review.**
