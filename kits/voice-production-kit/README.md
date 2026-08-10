# Voice Production Kit v1.2.0

Repository-backed Voice Production workflow for turning accepted PRD communication requirements into ElevenLabs-ready performance scripts and a reference-styled `Voice Production.docx`.

## Current flow

```text
handoff_ready PRD
→ Flow 5 voice requirements
→ voice_requirements_ready
→ Flow 6 performance script
→ work/voice-production.md
→ output/Voice Production.docx
→ voice_script_ready
→ Flow 7 validation/delivery
```

## Canonical owners

- `VOICE-EXTRACTION.md` — which voice moments exist and what they must communicate;
- `SCRIPT-PRODUCTION.md` — how justified moments become spoken/performance text;
- `work/voice-requirements.md` — project-specific Flow 5 source of truth;
- `work/voice-production.md` — project-specific Flow 6 source of truth for final spoken wording;
- `output/Voice Production.docx` — derived production artifact;
- `state/voice-state.yaml` — current downstream voice lifecycle status.

## DOCX builder

Install:

```bash
python -m pip install -r kits/voice-production-kit/requirements.txt
```

Build:

```bash
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  workspace/active/<project>/output/Voice\ Production.docx \
  --requirements workspace/active/<project>/work/voice-requirements.md
```

Read `DOCX-FORMAT.md` for the reference styling contract.

## Reference

`REFERENCE/Aftershock/README.md` records the audited original Aftershock DOCX benchmark and source SHA-256. Its demonstrated formatting/performance contract is codified in `DOCX-FORMAT.md` and the builder; the source binary is not required at runtime and is not duplicated through the current GitHub write surface.

The original paired `Gameplay.html` v1.2 is intentionally not duplicated here because active projects must use their own accepted PRD revision as upstream authority.
