# Voice Production Kit v1.4.1

Repository-backed voice workflow for turning an accepted PRD into traceable communication requirements, high-quality Eleven v3 performance wording, a reference-styled `Voice Production.docx`, and revision-specific delivery acceptance.

## Full voice flow

```text
handoff_ready PRD
→ Flow 5 voice requirements
→ voice_requirements_ready
→ Flow 6 SoundMaker v3 quality pass
→ canonical performance script
→ Voice Production.docx
→ voice_script_ready
→ Flow 7 validation/delivery
→ voice_delivery_ready
```

## Canonical owners

- `VOICE-EXTRACTION.md` — Flow 5 procedure;
- `SCRIPT-PRODUCTION.md` — Flow 6 project-level wording/performance procedure;
- `SOUNDMAKER.md` — one-entry-at-a-time Eleven v3 execution/quality procedure inside Flow 6;
- `DOCX-FORMAT.md` — derived DOCX presentation contract;
- `VOICE-VALIDATION.md` — Flow 7 final validation/delivery procedure;
- `work/voice-requirements.md` — project Voice scope;
- `work/voice-production.md` — final spoken/performance wording;
- `work/voice-acceptance.md` — current revision validation evidence;
- `state/voice-state.yaml` — Flow 5–7 lifecycle owner.

## SoundMaker v3

SoundMaker is **not** a separate source of truth and does not add a new Flow.

Use it when producing or revising an actual Eleven v3 line:

```text
Voice Requirement
→ duration-first planning when needed
→ voice-fit check
→ performance map
→ spoken wording
→ beat architecture
→ punctuation / line breaks / CAPS
→ minimal Audio Tags
→ generation baseline
→ one prompt ready to paste
→ actual audio review when audio exists
```

Default generation baseline when no stronger approved project calibration exists:

```text
Eleven v3
Stability: Natural
```

Actual audio is reviewed for the heard result, not the apparent quality of the prompt: meaning/intelligibility, voice identity, emotional movement, pacing, emphasis/landing, naturalness, pronunciation, and duration when applicable.

If the user actually generates a different edited prompt and approves it, that exact prompt must be synchronized back to `work/voice-production.md` so project state does not drift from the audio that was really produced.

## Eleven v3 production reference

Start at:

```text
references/elevenlabs/README.md
```

The reference is **v3-only** for operational production. It covers:

- voice-fit and Stability guidance;
- spoken-writing and emotional beat architecture;
- punctuation, CAPS, line structure, Audio Tags, stacking and reactions;
- target/max/fixed duration planning;
- credits/character usage;
- nondeterministic generation and regeneration diagnosis;
- pronunciation, normalization, long-form continuity, and current documentation conflicts.

It is a production-technique reference, not a project-fact source.

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

The validator checks mechanical parity/integrity. Final Flow 7 acceptance still requires semantic review and DOCX page-image inspection. Actual audio quality requires actual audio evidence and the SoundMaker audio-quality gate.

## Delivery scope

Default `voice_delivery_ready` scope is the accepted **script + DOCX** for downstream ElevenLabs use. If actual audio is not supplied, the system records `audio_evidence: not_provided` and does not claim audio quality.

## References

- `references/aftershock/README.md` records the audited original Aftershock DOCX benchmark and source SHA-256. The active builder/validation workflow does not depend on that binary at runtime.
- `references/elevenlabs/README.md` stores current evidence-backed Eleven v3 production guidance and a source register. It does not define project-specific voice counts, wording, speakers, or story facts.
