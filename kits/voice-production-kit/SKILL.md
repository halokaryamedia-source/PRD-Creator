---
name: voice-production-kit
description: Extract traceable voice requirements from accepted PRDs, prepare high-quality Eleven v3 performance wording through SoundMaker, preserve required communication through production polish, derive compact operator-ready Voice Production output, and optionally support one-line-at-a-time generation/revision without inventing upstream project facts.
version: 1.8.0
---

# Voice Production Kit

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted PRD → `work/voice-requirements.md`.
2. **Flow 6 — Eleven v3 Performance Script Production**: Voice Requirements → canonical `work/voice-production.md` + derived DOCX.
3. **Flow 7 — Voice Validation & Delivery**: current revision → compact acceptance + delivery state.

## Routing

- Flow 5 → `VOICE-EXTRACTION.md`.
- Flow 6 lifecycle/static output contract → `SCRIPT-PRODUCTION.md`.
- Eleven v3 preparation/generation quality → `SOUNDMAKER.md`.
- DOCX presentation → `DOCX-FORMAT.md`.
- Flow 7 → `VOICE-VALIDATION.md`.
- Deep Eleven v3 question → only the matching file under `references/elevenlabs/`.

Do not load all reference material by default.

## Canonical owners

- `work/voice-requirements.md` — which Voice moments exist and what they must communicate;
- `work/voice-production.md` — final spoken/performance wording;
- `output/Voice Production.docx` — derived operator presentation;
- `work/voice-acceptance.md` — compact current-revision evidence;
- `state/voice-state.yaml` — lifecycle state.

## Canonical entry contract

Every Flow 6 entry requires exactly:

```text
Voice ID + Title
Type
Speaker
Estimated Duration
exact performance block
```

`Type` and `Speaker` match Flow 5. The performance block contains only exact text intended for Eleven v3.

Do not duplicate Channel, Trigger, Purpose, requirement bullets, source refs, Performance Fill Map reasoning, WPM math, voice-fit ratings, or QA notes into the canonical entry.

## SoundMaker Preparation Mode

Preparation Mode is the normal script workflow when audio generation is not requested.

For each Voice ID:

```text
Voice Intent Completeness
→ internal Performance Fill Map
→ performance writing
→ Communication Conservation
→ script-ready
```

After per-line preparation, run one integrated **Voice Script Readiness** review over the requested scope.

### Voice Intent Completeness / Performance Fill Map

Resolve internally, as applicable:

```text
communication job
listener state
information payload
listener outcome
speaker identity
timing envelope
performance shape
landing
```

These are reasoning questions only; do not create another schema/artifact.

### Communication Conservation

Every independently actionable Flow 5 `Must communicate` fact that belongs in the moment must survive wording polish and duration compression clearly. `Must not add/repeat` guardrails remain binding.

Concision may improve wording; it may not thin material communication.

### Voice Script Readiness

Review once using Communication, Listener, Character, Performance, Timing, Continuity, and Operator lenses. Record one semantic result rather than separate scores/gates.

`Communication Conservation` stays explicit because a script can sound good while still omitting a required fact.

## Preparation vs Generation

### Preparation Mode

- full current Voice scope may be prepared in one bounded pass;
- actual commercial voice selection may wait if a clear Target Voice Profile exists;
- no audio testing or `APPROVED` per line is required;
- duration/pronunciation remain planned evidence until real proof exists.

### Generation Mode

- use only when actual ElevenLabs work is requested;
- one active Voice ID;
- one exact reviewed prompt;
- actual selected voice/settings;
- feedback/approval loop;
- exact approved generated wording syncs back into `work/voice-production.md`.

## Operator handoff

Do not create another handoff artifact by default. State shared speaker/voice/settings once when useful, then show per line only Voice ID/Title, Speaker, Estimated Duration, and exact Eleven v3 prompt.

Show an external production note only when the operator must take an extra action such as pronunciation setup, Fixed Duration, or Studio routing.

## Default v3 baseline

When no stronger approved project calibration exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance on directed SoundMaker prompt: OFF
```

Long-form instability may route to Studio while keeping Eleven v3.

## First wrong owner / bounded revision

Fix the earliest wrong owner rather than hiding upstream defects in prompt polish.

Revise only invalidated Voice IDs/speaker scope plus continuity materially affected by the change. Do not replay unaffected Voice work for ceremony.

## Non-negotiable rules

- SoundMaker scope is **Eleven v3 only**.
- Recover existing project context before asking the user.
- Voice scope cannot change silently after Flow 5.
- Performance technique cannot create project facts/Speakers/Channels/Triggers/mechanics/rewards/outcomes.
- Duration is planned before final wording when timing matters.
- Spoken wording/beat architecture precede punctuation/CAPS/Audio Tags.
- A flat script is not repaired by tag stacking.
- Communication Conservation must survive performance polish and duration compression.
- Batch preparation includes integrated project readiness / anti-template review.
- Any Enhance/UI rewrite of a directed prompt is a new draft requiring review.
- Exact approved generated wording synchronizes into `work/voice-production.md`.
- Generated-audio quality requires actual heard evidence only when audio is in scope.
- DOCX is always derived from canonical Markdown.
- Critical/Major findings block `voice_delivery_ready`.
- Stop after current preparation scope is ready; do not add optional schemas, gates, artifacts, or speculative hardening without a concrete defect.
- Aftershock remains a presentation benchmark only, never project content authority.
