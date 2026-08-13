# Voice Production Kit v1.8.0

Repository-backed workflow for accepted PRD → Voice Requirements → high-quality Eleven v3 performance wording → derived DOCX → compact current-revision acceptance, with audio generation optional.

## Flow

```text
handoff_ready PRD
→ Flow 5 Voice Requirements
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

- `VOICE-EXTRACTION.md` — Flow 5 scope/requirement procedure;
- `SCRIPT-PRODUCTION.md` — Flow 6 lifecycle/output contract;
- `SOUNDMAKER.md` — single operational Eleven v3 preparation/generation procedure;
- `DOCX-FORMAT.md` — derived DOCX presentation;
- `VOICE-VALIDATION.md` — Flow 7 integrated readiness/evidence gate;
- `references/elevenlabs/` — deep v3 reference only when needed.

Canonical project files remain:

- `work/voice-requirements.md` — Voice scope/required meaning;
- `work/voice-production.md` — final spoken/performance wording;
- `output/Voice Production.docx` — derived presentation;
- `work/voice-acceptance.md` — compact current revision evidence;
- `state/voice-state.yaml` — lifecycle state.

## Preparation quality model

### Voice Intent Completeness

Before writing, SoundMaker resolves the internal Performance Fill Map:

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

This is an internal reasoning map, not another persisted artifact.

### Communication Conservation

After writing/shortening, every independently actionable Flow 5 `Must communicate` fact that belongs in the moment must remain clearly represented, while `Must not add/repeat` guardrails remain binding.

Performance polish and duration compression may improve wording; they may not thin material communication.

### Voice Script Readiness

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

## Preparation Mode

Preparation Mode may prepare the full current Voice scope in one bounded pass and requires no audio testing or per-line approval. An actual commercial voice may remain unselected when a clear Target Voice Profile exists.

## Canonical output

Each Flow 6 entry contains only:

```text
Voice ID — Title
Type
Speaker
Estimated Duration
exact Eleven v3 performance block
```

Do not duplicate Channel, Trigger, Purpose, requirement bullets, source refs, Performance Fill Map reasoning, WPM math, voice-fit ratings, or QA notes into the canonical script/DOCX.

## Operator handoff

Do not create another handoff file by default. State shared speaker/voice/settings once when useful, then show each active line with Voice ID/Title, Speaker, Estimated Duration, and exact Eleven v3 prompt.

Only add an external note when the operator must take a special action such as pronunciation setup, Fixed Duration, or Studio routing.

## Generation Mode

Use only when actual ElevenLabs output is requested:

```text
one active Voice ID
→ one exact reviewed prompt
→ generate / feedback / approve
→ canonical sync
```

## v3 defaults

When no stronger approved project calibration exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance on directed SoundMaker prompt: OFF
```

Long-form instability may route to Studio while keeping Eleven v3.

## Validation model

Flow 7 keeps proof economical:

```text
Mechanical
+ Communication Conservation
+ one integrated Voice Script Readiness review
+ DOCX Visual when claimed
+ optional Audio Evidence
```

Existing `voice-state.yaml` fields remain compatible; they summarize the integrated semantic review and do not create separate review ceremonies.

## Revision discipline

Fix the first wrong owner and revise only invalidated Voice IDs/speaker scope plus continuity materially affected by the change. Do not replay unaffected work for ceremony.

## Build / validate

```bash
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  workspace/active/<project>/output/Voice\ Production.docx \
  --requirements workspace/active/<project>/work/voice-requirements.md

python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Builder/validator PASS does not prove semantic readiness, visual quality, pronunciation, or generated-audio quality.

## Stop rule

Stop Preparation Mode when current scope is script-ready, Communication Conservation and Voice Script Readiness pass, requested derived artifacts are current, and remaining evidence is stated honestly.

Do not add optional tags, schemas, scores, artifacts, review layers, or speculative hardening without a concrete defect.
