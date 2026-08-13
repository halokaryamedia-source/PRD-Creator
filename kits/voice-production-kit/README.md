# Voice Production Kit v1.9.0

Repository-backed workflow for accepted PRD → Flow 6-ready Voice Requirements → high-quality Eleven v3 performance wording → derived DOCX → compact current-revision acceptance, with audio generation optional.

## Flow

```text
handoff_ready PRD
→ Flow 5 Voice Requirements
     communication job / listener state / payload / outcome / speaker / timing truth
→ Flow 6 Preparation Mode
     Voice Intent Completeness
     → Performance Fill Map
     → SoundMaker writing
     → Communication Conservation
     → integrated Voice Script Readiness
→ canonical voice-production.md
→ derived Voice Production.docx
→ Flow 7 validation/delivery
→ optional Generation Mode later
```

## Owners

- `VOICE-EXTRACTION.md` — Flow 5 scope + Flow 5→6 intent interface;
- `SCRIPT-PRODUCTION.md` — Flow 6 lifecycle/output contract;
- `SOUNDMAKER.md` — single operational Eleven v3 preparation/generation procedure;
- `DOCX-FORMAT.md` — derived DOCX presentation;
- `VOICE-VALIDATION.md` — Flow 7 integrated readiness/evidence gate;
- `references/elevenlabs/` — deep v3 reference only when needed.

Canonical project files remain:

- `work/voice-requirements.md` — Voice scope/approved communication intent;
- `work/voice-production.md` — final spoken/performance wording;
- `output/Voice Production.docx` — derived presentation;
- `work/voice-acceptance.md` — compact current revision evidence;
- `state/voice-state.yaml` — lifecycle state.

# Flow 5 → Flow 6 interface

A Flow 5 requirement should let SoundMaker recover:

```text
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

`Timing Constraint` is optional and only for an authoritative line/window/fixed-sync rule. It is not Flow 6 Estimated Duration.

Flow 5 does not define final performance shape, landing wording, Audio Tags, CAPS/punctuation, Target Voice Profile, selected ElevenLabs voice, Stability, Surface, or production-estimated duration.

# Preparation quality model

## Voice Intent Completeness

Before writing, SoundMaker fills the internal Performance Fill Map from Flow 5 first:

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

Reopen accepted PRD context only when the Flow 5 entry lacks genuinely necessary delivery-relevant context. This is an internal reasoning map, not another persisted artifact.

## Communication Conservation

After writing/shortening, every independently actionable Flow 5 `Must communicate` fact that belongs in the moment must remain clearly represented, `Must not add/repeat` remains binding, and any authoritative Flow 5 timing constraint remains respected.

Performance polish and duration compression may improve wording; they may not thin material communication.

## Voice Script Readiness

After per-line preparation, review the current scope once through seven lenses:

```text
Communication
Listener
Character
Performance
Timing
Continuity
Operator
```

Record one semantic decision rather than seven separate gates/scores.

`Communication Conservation` remains explicit because an elegant script can still omit required meaning.

# Preparation Mode

Preparation Mode may prepare the full current Voice scope in one bounded pass and requires no audio testing or per-line approval. An actual commercial voice may remain unselected when a clear Target Voice Profile exists.

# Canonical output

Each Flow 6 entry contains only:

```text
Voice ID — Title
Type
Speaker
Estimated Duration
exact Eleven v3 performance block
```

Do not duplicate Channel, Trigger, Purpose, Timing Constraint, requirement bullets, source refs, Performance Fill Map reasoning, WPM math, voice-fit ratings, or QA notes into the canonical script/DOCX.

# Operator handoff

Do not create another handoff file by default. State shared speaker/voice/settings once when useful, then show each active line with Voice ID/Title, Speaker, Estimated Duration, and exact Eleven v3 prompt.

Only add an external note when the operator must take a special action such as an authoritative timing constraint, pronunciation setup, Fixed Duration, or Studio routing.

# Generation Mode

Use only when actual ElevenLabs output is requested:

```text
one active Voice ID
→ one exact reviewed prompt
→ generate / feedback / approve
→ canonical sync
```

# v3 defaults

When no stronger approved project calibration exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance on directed SoundMaker prompt: OFF
```

Long-form instability may route to Studio while keeping Eleven v3.

# Validation model

Flow 7 keeps proof economical:

```text
Mechanical
+ Communication Conservation
+ one integrated Voice Script Readiness review
+ DOCX Visual when claimed
+ optional Audio Evidence
```

Existing `voice-state.yaml` fields remain compatible; they summarize the integrated semantic review and do not create separate review ceremonies.

# Revision discipline

Fix the first wrong owner and revise only invalidated Voice IDs/speaker scope plus continuity materially affected by the change. A change to authoritative Voice timing truth returns to Flow 5 first; an Estimated Duration adjustment stays in Flow 6.

# Build / validate

```bash
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  workspace/active/<project>/output/Voice\ Production.docx \
  --requirements workspace/active/<project>/work/voice-requirements.md

python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Builder/validator PASS does not prove semantic readiness, visual quality, pronunciation, or generated-audio quality.

# Stop rule

Stop Preparation Mode when current scope is script-ready, Communication Conservation and Voice Script Readiness pass, requested derived artifacts are current, and remaining evidence is stated honestly.

Do not add optional tags, schemas, scores, artifacts, review layers, or speculative hardening without a concrete defect.
