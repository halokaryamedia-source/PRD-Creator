# Voice Production Kit v1.3.1

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

## ElevenLabs production reference

For actual Eleven v3 performance/model/voice/duration/pronunciation decisions, start at:

```text
references/elevenlabs/README.md
```

It is an operational production-technique reference, not a project-fact source. Open only the supporting page required by the active question.

The reference currently covers:

- v3 vs Multilingual v2 model choice;
- voice-fit and Stability guidance;
- spoken-writing and emotional beat architecture;
- punctuation, CAPS, line structure, Audio Tags, stacking and reactions;
- target/max/fixed duration planning;
- credits/character usage;
- nondeterministic generation and regeneration diagnosis;
- pronunciation, normalization, long-form continuity, and current documentation conflicts.

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

## References

- `references/aftershock/README.md` records the audited original Aftershock DOCX benchmark and source SHA-256. The active builder/validation workflow does not depend on that binary at runtime.
- `references/elevenlabs/README.md` stores current evidence-backed ElevenLabs production guidance and a source register. It does not define project-specific voice counts, wording, speakers, or story facts.
