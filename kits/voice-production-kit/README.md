# Voice Production Kit v1.3.0

Repository-backed voice workflow for turning an accepted PRD into traceable communication requirements, ElevenLabs-ready performance wording, a reference-styled `Voice Production.docx`, and revision-specific delivery acceptance.

## Full voice flow

```text
handoff_ready PRD
→ Flow 5 voice requirements
→ voice_requirements_ready
→ Flow 6 canonical performance script
→ Voice Production.docx
→ voice_script_ready
→ Flow 7 validation/delivery
→ voice_delivery_ready
```

## Canonical owners

- `VOICE-EXTRACTION.md` — Flow 5 procedure;
- `SCRIPT-PRODUCTION.md` — Flow 6 wording/performance procedure;
- `DOCX-FORMAT.md` — derived DOCX presentation contract;
- `VOICE-VALIDATION.md` — Flow 7 final validation/delivery procedure;
- `work/voice-requirements.md` — project Voice scope;
- `work/voice-production.md` — final spoken/performance wording;
- `work/voice-acceptance.md` — current revision validation evidence;
- `state/voice-state.yaml` — Flow 5–7 lifecycle owner.

## Build DOCX

```bash
python -m pip install -r kits/voice-production-kit/requirements.txt
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  workspace/active/<project>/output/Voice\ Production.docx \
  --requirements workspace/active/<project>/work/voice-requirements.md
```

## Validate current voice package

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

The validator checks mechanical parity/integrity. Final Flow 7 acceptance still requires semantic review and DOCX page-image inspection.

## Delivery scope

Default `voice_delivery_ready` scope is the accepted **script + DOCX** for downstream ElevenLabs use. If actual audio is not supplied, the system records `audio_evidence: not_provided` and does not claim audio quality.

## Reference

`references/aftershock/README.md` records the audited original Aftershock DOCX benchmark and source SHA-256. The active builder/validation workflow does not depend on that binary at runtime.
