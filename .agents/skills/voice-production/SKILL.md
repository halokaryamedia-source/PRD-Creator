---
name: voice-production
description: Semantic/product-contract specialist for PRD-Creator Flow 5–7. Use when the active boundary is Voice Requirement scope, Flow 5→6 intent completeness, Eleven v3 wording/SoundMaker quality, communication conservation, static Voice output meaning, or final Voice validation/delivery semantics. Preserve exact upstream PRD/Voice scope and never invent gameplay, lore, speaker/channel, trigger, timing truth, or audio evidence.
---

# Voice Production

Own semantic/product-contract judgment around Voice Production Kit Flow 5–7. Detailed procedures remain in `kits/voice-production-kit/`.

## Trigger

Use when the wrong contract concerns:

- accepted PRD → Voice Requirements;
- Voice ID / Type / Speaker / Channel / Trigger / Purpose / communication scope;
- Flow 5 requirement completeness for SoundMaker;
- Voice Requirements → final Eleven v3 wording;
- Voice Intent Completeness, Performance Fill Map, Communication Conservation, duration, Target Voice Profile/fit, or operator readiness;
- what canonical script / operator handoff / DOCX / audio acceptance is allowed to represent.

Do not select merely because a task mentions ElevenLabs, DOCX, audio, Python, or CI. Pure builder/validator mechanics route to the nearest technical owner.

## Routing

1. Verify the accepted PRD revision and current Voice state.
2. Recover existing project facts before asking the user.
3. Identify the active owner:
   - Flow 5 → `VOICE-EXTRACTION.md` + `work/voice-requirements.md`;
   - Flow 6 lifecycle/static output/full-project preparation → `SCRIPT-PRODUCTION.md` + `SOUNDMAKER.md`;
   - Flow 6 actual Eleven v3 generation/revision → `SOUNDMAKER.md` Generation Mode;
   - Flow 7 → `VOICE-VALIDATION.md`.
4. Open only the deep Eleven v3 reference required by the active problem.
5. Route missing project facts upstream instead of repairing them in performance wording.

## Authority

```text
accepted PRD
→ voice-requirements.md
→ SoundMaker v3 preparation/generation quality
→ voice-production.md
→ Voice Production.docx (derived)
→ voice-acceptance.md
→ voice-state.yaml
```

- Flow 5 owns which Voice moments exist, their approved Speaker/Channel/Trigger/Purpose, required communication, exclusions, and authoritative timing truth when one exists.
- Flow 6 owns final Eleven v3 wording/performance notation and Estimated Duration, not Voice scope or source timing truth.
- canonical Flow 6 entries carry exact Voice ID/Type/Speaker parity plus Estimated Duration and exact performance text.
- `SOUNDMAKER.md` is the operational procedure, not a second wording owner.
- operator handoff is a concise derived view, not another persistent authority.
- Flow 7 owns revision-specific evidence, not rewritten dialogue.
- generated audio is evidence/output, never upstream project authority.

# Flow 5 judgment

Extract only justified player-facing communication moments and preserve supported Speaker/Channel/Trigger/Function.

A Flow 5 entry is ready for Flow 6 only when SoundMaker can recover, without product-level guessing:

```text
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

Quality rules:

- Trigger describes the actual event/state and relevant listener condition when material.
- Purpose describes what the listener should know/do/understand/acknowledge, not merely `provide dialogue`.
- Independently actionable required facts remain distinct enough to conserve downstream.
- `Timing Constraint` is optional and only for authoritative line/window/sync truth; it is not Estimated Duration.
- deduplicate repeated briefing unless Trigger/Function genuinely differs.
- implementation-only detail does not automatically become narration.
- `no_voice_required` is valid.

Do not add Flow 5 fields for performance shape, landing wording, tags, CAPS/punctuation, voice selection, Stability, or production-estimated duration.

# Flow 6 / SoundMaker judgment

SoundMaker scope is **Eleven v3 only**.

Preparation quality follows:

```text
Voice Intent Completeness
→ internal Performance Fill Map
→ performance writing
→ Communication Conservation
→ script-ready
→ integrated Voice Script Readiness
```

## Voice Intent Completeness / Performance Fill Map

Use the Flow 5 interface first. Reopen accepted PRD context only when genuinely missing delivery-relevant context prevents responsible authoring.

Performance Shape and Landing normally remain SoundMaker craft decisions; do not push them upstream merely to make the requirement more detailed.

## Communication Conservation

Every independently actionable Flow 5 `Must communicate` fact that belongs in the moment must survive wording polish and duration compression clearly. `Must not add/repeat` remains binding. Any authoritative Flow 5 timing constraint must remain respected.

Concision may improve wording; it may not thin material communication.

## Integrated Voice Script Readiness

Review Communication, Listener, Character, Performance, Timing, Continuity, and Operator clarity as one semantic decision. Do not create separate scorecards/gates for the lenses.

Communication Conservation remains explicit because a script can sound good while still omit required meaning.

## Production interpretation vs material decision

SoundMaker may decide craft details such as sentence split, beat structure, punctuation, CAPS, tags, pacing, Performance Shape, Landing, and Estimated Duration within approved intent.

Return upstream when unresolved work would materially change Speaker personality/identity, Voice scope, Trigger, Channel, mechanic, reward, lore, required communication, or an authoritative timing/sync rule.

# Static output judgment

Keep output lean:

- canonical entry → Voice ID/Title + Type + Speaker + Estimated Duration + exact performance block;
- DOCX → Type · Speaker + Voice ID/Title + Estimated Duration + Performance Script;
- operator handoff → shared setup once + active line metadata + exact prompt;
- planning/QA/source reasoning stays internal.

Do not create another handoff artifact merely to duplicate canonical output.

# First wrong owner / bounded revision

Fix the earliest wrong owner:

```text
project fact → PRD authority
Voice scope/Speaker/Channel/Trigger/Purpose/required communication/timing truth → Flow 5
wording/performance/Estimated Duration → Flow 6
DOCX-only defect → builder/DOCX contract
audio-only defect → Generation Mode
```

Revise only invalidated Voice IDs/speaker scope plus continuity materially affected by the change.

# Flow 7 judgment

Use:

```text
Mechanical
+ Communication Conservation
+ one integrated Voice Script Readiness review
+ DOCX Visual when claimed
+ optional Audio Evidence
```

Existing `voice-state.yaml` semantic fields remain compatibility summaries and do not require independent review ceremonies.

Critical/Major findings block `voice_delivery_ready`.

# Audio evidence

Use truthful states:

- `not_provided`;
- `partial_review`;
- `reviewed_passed`;
- `reviewed_with_findings`.

Preparation Mode may legitimately finish with `not_provided`. Never infer audio quality from script quality or DOCX appearance.

# Stop rule

Stop once current preparation scope is script-ready, Communication Conservation and integrated Voice Script Readiness pass, requested derived artifacts are current, and remaining evidence is stated honestly.

Do not add optional schemas, scores, artifacts, approval layers, or speculative hardening without a concrete defect.
