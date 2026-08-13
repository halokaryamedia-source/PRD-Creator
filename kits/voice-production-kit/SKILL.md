---
name: voice-production-kit
description: Extract Flow 6-ready Voice requirements from accepted PRDs, prepare high-quality Eleven v3 performance wording through SoundMaker, preserve required communication and timing truth, and publish operator-ready Voice Production into the same project HTML without inventing upstream project facts.
version: 1.10.0
---

# Voice Production Kit

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted PRD → `work/voice-requirements.md`.
2. **Flow 6 — Eleven v3 Performance Script Production**: Voice Requirements → canonical `work/voice-production.md` → same project `output/final.html`.
3. **Flow 7 — Voice Validation & Delivery**: current revision → compact acceptance + delivery state.

Audio generation remains optional. DOCX is an optional export, not the normal human-facing Voice output.

## Routing

- Flow 5 → `VOICE-EXTRACTION.md`.
- Flow 6 lifecycle/output contract → `SCRIPT-PRODUCTION.md`.
- Eleven v3 preparation/generation quality → `SOUNDMAKER.md`.
- Flow 7 → `VOICE-VALIDATION.md`.
- optional DOCX export → `DOCX-FORMAT.md` + builder.
- deep Eleven v3 question → only the matching file under `references/elevenlabs/`.

Do not load all reference material by default.

# Authority chain

```text
accepted PRD
→ work/voice-requirements.md
→ work/voice-production.md
→ output/final.html → Production Assets → Voice
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

Ownership:

- accepted PRD owns project/gameplay truth and the need for a Voice asset;
- `voice-requirements.md` owns which Voice assets exist and what each must communicate;
- `voice-production.md` owns selected actor voice when known, Estimated Duration, and exact Eleven v3 production wording;
- `final.html` is derived presentation only;
- audio is optional downstream evidence/output.

Do not create a second Voice HTML or Asset Requirement HTML by default.

# Flow 5 → Flow 6 interface

A Flow 5 entry is ready only when SoundMaker can recover without product-level guessing:

```text
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

Rules:

- Trigger states the actual event/state and relevant listener condition when material.
- Purpose states the listener-facing outcome, not `provide dialogue`.
- independently actionable required facts remain distinct enough to conserve downstream.
- `Timing Constraint` is optional upstream truth; it is not Estimated Duration.
- Performance Shape, Landing, wording, tags, CAPS/punctuation, voice selection, Stability, Surface, and Estimated Duration stay in Flow 6 unless upstream meaning explicitly constrains them.

# Canonical Voice Production

`work/voice-production.md` may contain one optional cast block before gameplay sections:

```text
Voice Cast:
- <Speaker>: <selected ElevenLabs voice>
```

Then every entry requires:

```text
Voice ID + Title
Type
Speaker
Estimated Duration
exact performance block
```

`Type` and `Speaker` match Flow 5.

Use Voice Cast once per recurring Speaker. Do not repeat commercial voice names in every entry and do not invent one merely to fill the field. `Voice selection pending` is valid during Preparation Mode; actual Generation Mode requires an intentionally selected voice for the active Speaker.

Do not duplicate Channel, Trigger, Purpose, Timing Constraint, requirement bullets, source refs, Performance Fill Map reasoning, WPM math, voice-fit ratings, or QA notes into canonical entries.

# SoundMaker Preparation Mode

For each Voice ID:

```text
Flow 5 intent
→ Voice Intent Completeness
→ internal Performance Fill Map
→ performance writing
→ Communication Conservation
→ script-ready
```

After per-line preparation, run one integrated **Voice Script Readiness** review over Communication, Listener, Character, Performance, Timing, Continuity, and Operator lenses.

Communication Conservation remains explicit because a polished script can still omit required meaning.

Preparation Mode:

- may prepare the full current Voice scope in one bounded pass;
- does not require audio generation/testing or per-line `APPROVED`;
- may use a Target Voice Profile before actual actor voice selection;
- keeps measured duration/pronunciation/audio claims unverified until evidence exists.

# Project HTML production surface

The same `output/final.html` is the default human-facing project document.

When `work/voice-production.md` exists, the normal PRD renderer appends a professional-only section:

```text
Production Assets
└── Voice
```

The HTML intentionally exposes only:

```text
Voice Cast once
→ gameplay-ordered sections
→ per line:
   title
   Actor
   Estimated Duration
   exact Eleven v3 text
   Copy Text
```

`Copy Text` copies only the exact canonical performance block.

Internal Flow 5 requirements/reasoning/QA do not appear in the page.

## Optional DOCX

`output/Voice Production.docx` may still be generated when explicitly requested or materially useful. It is derived export only and never required merely to complete normal Voice Preparation/Delivery.

# Generation Mode

Use only when actual ElevenLabs work is requested:

```text
one active Voice ID
→ actor voice selected intentionally
→ one exact reviewed prompt
→ generate / feedback / approve
→ canonical sync
→ rerender same final.html when actor/prompt changed
```

Default v3 baseline when no stronger approved project calibration exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance on directed SoundMaker prompt: OFF
```

# First wrong owner / bounded revision

```text
project fact → PRD authority
Voice scope/Speaker/Channel/Trigger/Purpose/required communication/source timing → Flow 5
wording/performance/Estimated Duration/actor-voice selection → Flow 6
correct canonical Voice + wrong Production Assets HTML → PRD renderer compositor
optional DOCX-only defect → Voice DOCX builder
audio-only defect → Generation Mode
```

Revise only invalidated Voice IDs/Speaker scope plus continuity materially affected by the change. Voice-only production changes do not reopen PRD acceptance when PRD canonical meaning is unchanged.

# Flow 7 proof

Use:

```text
Mechanical
+ Communication Conservation
+ one integrated Voice Script Readiness review
+ Project HTML Visual when claimed
+ optional DOCX Visual when DOCX exists
+ optional Audio Evidence
```

Static HTML parity is not visual proof; visual PASS requires actual rendered/browser inspection.

# Non-negotiable rules

- SoundMaker scope is **Eleven v3 only**.
- Voice Production is downstream from accepted PRD, not a separate source-intake project.
- recover existing project context before asking the user.
- Voice scope cannot change silently after Flow 5.
- performance technique cannot create project facts/Speakers/Channels/Triggers/mechanics/rewards/outcomes/timing truth.
- source timing constraints and Estimated Duration remain distinct.
- spoken wording/beat architecture precede punctuation/CAPS/Audio Tags.
- a flat script is not repaired by tag stacking.
- exact approved/generated wording synchronizes into `work/voice-production.md`.
- generated-audio quality requires actual heard evidence.
- do not create separate Voice HTML, asset manifest, settings database, score system, or extra approval layer without a concrete defect.
- stop when current requested scope is ready.
