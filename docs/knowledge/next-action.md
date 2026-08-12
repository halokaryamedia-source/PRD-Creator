# Next Action

Updated: 2026-08-12

## Current Status

`PRD_GOLDEN_GUIDED_COMPLETE_PREVIEW_AND_RENDER_ECONOMY_LOCKED_CLOCKWORK_PREVIEW_NEXT`

Working branch: **`Local` only**.

## Current system state

The exact approved AFTERSHOCK Golden remains the canonical reference/runtime template, with the bidirectional fidelity model:

```text
Reference → Fill Map
Project Authority → Filled Golden
```

The Reverse-derived Golden fill map serves two bounded jobs:

1. **Flow 2 completeness guide** — tells the AI what each global/objective/Gameplay/Level Design/Developer surface must eventually answer;
2. **Flow 3/4 rendering and fidelity contract** — tells the renderer/reviewer where approved meaning belongs and what visible composition must be preserved.

Golden supplies slot responsibility and reading structure. It does **not** supply Aftershock-specific facts to unrelated projects.

## Flow 2 → Flow 3 boundary

Initial PRD production follows:

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

## Render / review economy

Normal execution now uses three modes:

```text
MODE A — UNDERSTAND + PREVIEW
Source → complete model → Simple Chat Preview
No preview HTML, no render-data generation, no browser QA.

MODE B — PRODUCTION RENDER
Approved preview → content.md → compact render-data.json
→ one planned full final.html render
→ one mechanical validation
→ one integrated semantic/material/Golden review
→ representative desktop visual sanity.

MODE C — BOUNDED REVISION
Affected meaning only → affected preview only when interpretation changed
→ patch affected canonical content/projection
→ one planned full final.html rerender
→ one mechanical check
→ targeted review of invalidated scope.
```

The renderer may rewrite the full HTML file even for a one-objective change. That deterministic write is intentionally kept simple; the expensive work that stays bounded is AI reading, reasoning, and review.

Additional render/review cycles are justified only by a concrete validator/review finding or a later approved change. Do not generate HTML repeatedly while gameplay is still being corrected in chat.

Normal authoring uses `CONTENT-CONTRACT.md` / the Golden fill map instead of loading the large Golden HTML into model context. The exact Golden artifact is loaded only when it is itself evidence: Golden regression, template/renderer investigation, or targeted visual comparison.

`render-data.json` remains compact and projection-only; reasoning notes, source-audit notes, rejected alternatives, approval transcript, confidence scores, and duplicate prose do not belong there.

Full every-page/browser review is not the default for a content-only project generation. Escalate only when template/CSS/JS/page-composition behavior changed, a targeted finding suggests a global visual defect, or the user explicitly asks for full visual proof.

No preview renderer, partial-page renderer, incremental HTML cache, generic rendering framework, or second template is added for speed.

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

These are valid source conflicts but are no longer reasons to stop before preview. Flow 2 should choose one coherent proposal for each, propagate it through the complete objective model, then show the result for user approval.

## Proof boundary

This refinement changes only existing procedure/render/review owners and package version documentation. It does **not** add:

- a new Flow;
- preview HTML;
- partial/incremental renderer;
- cache framework;
- new schema;
- new approval framework;
- Golden/template/renderer code changes.

The next useful proof is real project execution, not additional framework work.

## Next Step

**Run The Clockwork Vault through the current Flow 2 and present one complete objective-by-objective Simple Chat Preview. After user approval, generate the Golden PRD once through the compact render path and perform one mechanical + representative targeted review.**
