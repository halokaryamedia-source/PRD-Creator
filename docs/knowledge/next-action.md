# Next Action

Updated: 2026-08-12

## Current Status

`PRD_CONTENT_PURITY_HUMANIZE_GATE_LOCKED_CLOCKWORK_HUMANIZED_REVIEW_READY`

Working branch: **`Local` only**.

## Current system state

Project Document Generator is now **v1.13.0**.

Normal production remains:

```text
Source
→ UNDERSTAND + COMPLETE using Golden Fill Map
→ Simple Chat Preview
→ user approval
→ one Content Purity + Humanize pass
→ canonical content.md + direct render-data projection from the same approved model
→ one deterministic Golden render
→ one mechanical/content-purity + integrated review
→ representative desktop visual sanity
```

The efficiency principle is now **one semantic model, one semantic write**. Do not ask AI to independently summarize the project again when creating `render-data.json`, and do not reread/rewrite `final.html` for semantic drafting.

## Root cause fixed

The verified Clockwork render exposed a class of AI-slop that prior review did not stop strongly enough:

1. **project/document-process leakage** — visible project copy mentioned Golden HTML/page structure, page-role layout, document order/content lock, or other PRD-production mechanics;
2. **generic filler labels** — plain notes rendered as `Important Note 1/2/...`, and overview invariants could use labels such as `Global Rule 1`;
3. **mixed abstraction** — Gameplay Context/Result could carry Developer-owned telemetry, save/retry, final-score or reset detail;
4. **summary overload** — Overview facts and gameplay summary cards repeated detailed information already owned by journey/requirements;
5. **dense requirement prose** — several independently actionable rules could be written as one prose block instead of readable bullets;
6. **terminology drift** — visible project copy could alternate between reader-facing terms without a real technical distinction.

## System correction

Flow 3 now performs one bounded **Content Purity + Humanize gate before the planned render**:

```text
approved project model
→ remove document/generator-process leakage
→ enforce Gameplay / Level Design / Developer ownership
→ make summary surfaces answer one question each
→ use semantic titles instead of numbered filler labels
→ decompose independent rules into bullets/rows
→ normalize visible terminology
→ write content.md
→ directly project the same model into render-data.json
```

Humanize remains relocation/decomposition, **not material deletion**.

The existing validator now has one narrow `content_purity` check for the concrete observed failure class. It rejects explicit project/process leakage (`Golden HTML`, internal artifacts, page-role narration, three-page-contract/document-process narration), generic `Global Rule N`, and plain note strings that would render generic `Important Note N` cards. It is deliberately not a word-count/readability score or broad keyword framework.

Focused regression coverage was added in `tests/test_prd_content_purity.py`.

Proof on commit `509480d4844dafa3d933503085f6e32d843f2746`:

- **PRD Verify #133 — PASS**
- **Repository Verify #234 — PASS**

No partial renderer, HTML cache, preview renderer, similarity score, word-count gate, or second template was added.

## Clockwork humanized review revision

User feedback approved the gameplay/mechanics and requested only content-purity/readability cleanup.

A bounded humanized review artifact was prepared in the current execution runtime from the already-approved Clockwork Golden output. The revision keeps:

- the same 30 Golden page IDs/order;
- the same base Golden CSS style blocks;
- the same script set and navigation targets;
- the approved Clockwork mechanics/scoring/detail, including 90-second Resonance free play, fixed Gallery kit, Checkpoint 3 collapse, 4-second Echo Pebble, Straight/Elbow/Split conduit types, permanent Gremlin sabotage, and Clockwork Wayfinder.

It changes only review-approved presentation/copy ownership:

- Overview facts are scan-first (`Solo · 1 player per isolated lane`, `≈45 minutes total`, `Introduction → 4 Objectives → Ending`);
- Global Gameplay Direction uses semantic project rules instead of `Global Rule N` and removes localization/platform/document-process overflow;
- Development Overview / Data and Reset / Gameplay Development no longer narrate Golden/page/document workflow;
- Gameplay Context/Main Objective/Result are shorter and player-facing;
- detailed score formulas remain in Developer, while Gameplay Overview states only high-level scoring inputs;
- generic `Important Note N` titles are replaced with semantic titles such as `Lane Isolation`, `No State Carryover`, `Immediate Input Feedback`;
- long actionable requirement detail remains as lists where the existing Golden structure already supports independent bullets.

Current review-artifact SHA-256:

```text
82025447edb630d9b18918f0707e36c103937ab41ff8bee86dbbc3fde2a51016
```

Static checks on the review artifact:

- 30 document sections preserved;
- no duplicate IDs;
- all fragment navigation targets resolve;
- base Golden `<style>` blocks remain byte-equivalent after parsing/serialization comparison;
- no observed process-leak phrases remain in visible `<main>` copy;
- no generic `Important Note N` titles remain;
- approved key mechanics remain present.

## Proof boundary

The humanized HTML above is a **bounded review artifact**, not yet a new authoritative renderer-produced workspace revision, because the verified Clockwork canonical package (`content.md` / `render-data.json` / state) was not persisted under `workspace/active/` in the connected GitHub channel.

Do not claim current browser visual PASS for this humanized revision from this execution environment; browser loading was unavailable for the local artifact. The previous pre-feedback Clockwork render had representative Chromium proof, but that proof does not automatically transfer to changed copy.

Do not patch or commit the humanized HTML as project authority. The user-approved content cleanup should be reflected upstream in canonical content/render data when the Clockwork package is persisted/regenerated.

## Next Step

**Persist/recover the approved Clockwork canonical package under `workspace/active/the-clockwork-vault/`, apply the humanized/content-pure copy upstream, run the official renderer once, then perform targeted desktop visual sanity on Overview + Development Overview + one Gameplay Overview + one dense Developer page. Only change Golden CSS if the purified copy still demonstrates a concrete readability defect.**
