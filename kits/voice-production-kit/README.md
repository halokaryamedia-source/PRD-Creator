# Voice Production Kit v1.5.0

Repository-backed workflow for accepted PRD → Voice Requirements → high-quality Eleven v3 performance wording → derived DOCX → current-revision acceptance.

## Flow

```text
handoff_ready PRD
→ Flow 5 Voice Requirements
→ Flow 6 canonical script + SoundMaker v3 quality
→ Voice Production.docx
→ Flow 7 validation/delivery
```

## Owners

- `VOICE-EXTRACTION.md` — Flow 5 procedure;
- `SCRIPT-PRODUCTION.md` — Flow 6 lifecycle/canonical artifact procedure;
- `SOUNDMAKER.md` — **single operational Eleven v3 execution procedure** for an actual line;
- `DOCX-FORMAT.md` — derived DOCX presentation;
- `VOICE-VALIDATION.md` — Flow 7 evidence/delivery gate;
- `references/elevenlabs/` — deep v3 reference only when needed.

Canonical project files:

- `work/voice-requirements.md` — Voice scope/required meaning;
- `work/voice-production.md` — final spoken/performance wording;
- `output/Voice Production.docx` — derived presentation;
- `work/voice-acceptance.md` — current revision evidence;
- `state/voice-state.yaml` — lifecycle state.

## SoundMaker v3

Use `SOUNDMAKER.md` for real Eleven v3 prompt work. It owns the practical sequence:

```text
understand
→ duration when needed
→ voice fit
→ performance map
→ spoken beats
→ punctuation / line structure / CAPS
→ minimal Audio Tags
→ pronunciation
→ generation setup
→ hear / diagnose
→ approve / revise
```

Defaults when no stronger approved project calibration exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance on an already-directed SoundMaker prompt: OFF
```

Long-form v3 that develops whisper/volume/tone/accent drift or breaking may route to **Studio with Eleven v3**. This changes the production surface, not the model scope.

## Reference map

Start at `references/elevenlabs/README.md` only when a deeper technical question exists.

- writing/tags → `v3-performance-writing.md`;
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

Builder/validator PASS does not prove semantic, visual, pronunciation, or audio quality.

## Boundary

SoundMaker/ElevenLabs knowledge shapes delivery only. It may not invent project facts, Voice moments, speaker/channel/trigger, mechanics, rewards, or lore. Generated audio is approved only when actual audio evidence was reviewed.
