---
name: voice-production-kit
description: Extract traceable voice requirements from accepted PRDs, then convert approved voice moments into ElevenLabs-ready performance scripts and a reference-styled Voice Production DOCX without inventing upstream project facts.
version: 1.2.0
---

# Voice Production Kit

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted PRD → `work/voice-requirements.md`.
2. **Flow 6 — ElevenLabs Performance Script Production**: voice requirements → `work/voice-production.md` + `output/Voice Production.docx`.
3. **Flow 7 — Voice Validation & Delivery**: downstream final acceptance/delivery.

## Flow 6 entry gate

Start Flow 6 only when `state/voice-state.yaml` is `voice_requirements_ready` for the current accepted PRD revision.

## Flow 6 required order

1. Read `SCRIPT-PRODUCTION.md`.
2. Read `DOCX-FORMAT.md`.
3. Read `work/voice-requirements.md`.
4. Read accepted PRD content only for required context/terminology.
5. Draft `work/voice-production.md` without changing the Flow 5 Voice ID set or type.
6. Check required facts/guardrails and remove unsupported wording.
7. Build `output/Voice Production.docx` with `builder/build_docx.py` and `--requirements`.
8. Update `state/voice-state.yaml` to `voice_script_ready`.
9. Stop. Flow 7 owns final voice validation/delivery.

## Non-negotiable rules

- No new voice moment in Flow 6 unless Flow 5 scope is explicitly reopened.
- Preserve official names, speaker, channel, trigger, sequence, mechanics, outcomes, and rewards.
- Do not repair an unresolved PRD decision inside spoken wording.
- Performance directions describe delivery, not new events or facts.
- Selective CAPS, pauses, and line breaks are production tools, not decoration.
- Estimated Duration is an estimate until audio exists.
- `work/voice-production.md` owns spoken wording; the DOCX is derived.
- Aftershock is a quality/layout reference only, never a project requirement or quota.
