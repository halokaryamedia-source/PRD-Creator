# Voice Production Kit v1.7.0

Repository-backed workflow for accepted PRD → Voice Requirements → high-quality Eleven v3 performance wording → derived DOCX → current-revision acceptance, with audio generation optional.

## Flow

```text
handoff_ready PRD
→ Flow 5 Voice Requirements
→ Flow 6 Preparation Mode
→ canonical script + SoundMaker v3 quality
→ Voice Production.docx
→ Flow 7 validation/delivery
→ optional Generation Mode later
```

## Owners

- `VOICE-EXTRACTION.md` — Flow 5 procedure;
- `SCRIPT-PRODUCTION.md` — Flow 6 lifecycle + static output contract;
- `SOUNDMAKER.md` — single operational Eleven v3 preparation/generation procedure;
- `DOCX-FORMAT.md` — derived DOCX presentation;
- `VOICE-VALIDATION.md` — Flow 7 evidence/delivery gate;
- `references/elevenlabs/` — deep v3 reference only when needed.

Canonical project files:

- `work/voice-requirements.md` — Voice scope/required meaning;
- `work/voice-production.md` — final spoken/performance wording;
- `output/Voice Production.docx` — derived presentation;
- `work/voice-acceptance.md` — current revision evidence;
- `state/voice-state.yaml` — lifecycle state.

## Preparation Mode — normal script work

Use when audio generation/testing is not requested.

```text
all Voice Requirements
→ recover project context
→ SoundMaker per-line construction
→ cross-line speaker continuity / anti-repetition
→ duration + pronunciation planning
→ canonical script
→ optional DOCX / script-level validation
```

Preparation Mode may prepare all Voice IDs in one pass and does not require audio testing or per-line approval.

## Static output contract

Each canonical Flow 6 entry contains the minimum stable production data:

```text
### <VOICE-ID> — <Title>
Type: <Flow 5 type>
Speaker: <Flow 5 speaker>
Estimated Duration: <range>

```performance
<exact Eleven v3 text>
```
```

`Type` and `Speaker` are mechanically checked against Flow 5. Speaker is also shown in the generated DOCX so a production operator never has to infer which character owns a line.

Keep planning-only metadata such as Channel, Trigger, Purpose, requirement bullets, source refs, WPM calculations, performance maps, voice-fit ratings, and QA notes in their owning/internal sources instead of duplicating them into the canonical script or DOCX.

## Operator handoff

Do not create another handoff file by default. Derive a compact operator view from current authority.

State shared setup once when useful:

```text
Speaker / selected voice or target voice profile
Model: Eleven v3
Stability: Natural | project-calibrated
Surface: Speech Synthesis | Studio when applicable
```

Then each active line needs only:

```text
Voice ID — Title
Speaker
Estimated Duration
exact Eleven v3 prompt
```

Only add an external production note when the operator must perform an extra step such as pronunciation-dictionary setup, Fixed Duration, or Studio routing.

## Generation Mode — optional later

Use only when actual ElevenLabs output is requested:

```text
one active Voice ID
→ one exact reviewed prompt
→ generate / feedback / approve
→ canonical sync
```

## SoundMaker v3 defaults

When no stronger approved project calibration exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance on an already-directed SoundMaker prompt: OFF
```

Long-form v3 that develops whisper/volume/tone/accent drift or breaking may route to **Studio with Eleven v3**. This changes the production surface, not the model scope.

## Project-level quality

A full prepared script is reviewed across the project for:

- recurring speaker identity;
- information progression between briefing/reminder/success lines;
- accidental reuse of identical openings, beat chains, tag positions, CAPS climaxes, sentence rhythms, or closing patterns;
- intentional repetition vs AI-like templating.

Structural variety must never change approved facts or invent personality.

## Duration hierarchy

When timing matters:

```text
nearest approved similar sample (if one exists)
→ calibrated project performance rate
→ generic WPM fallback
```

With no approved audio, generic planning is valid and remains labeled **Estimated Duration**.

## Reference map

Open only for the active issue:

- writing/tags → `references/elevenlabs/v3-performance-writing.md`;
- timing → `v3-duration-planning.md`;
- voice/Stability/Enhance/Studio/troubleshooting/pronunciation → `v3-production-reference.md`;
- evidence provenance → `source-register.md`.

## Build / validate

```bash
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  workspace/active/<project>/output/Voice\ Production.docx \
  --requirements workspace/active/<project>/work/voice-requirements.md

python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Builder/validator PASS does not prove generated-audio quality. Audio evidence is optional unless audio delivery is explicitly requested.

## Boundary

SoundMaker/ElevenLabs knowledge shapes delivery only. It may not invent project facts, Voice moments, speaker/channel/trigger, mechanics, rewards, or lore. Generated audio becomes evidence only when actual generation/review is in scope.
