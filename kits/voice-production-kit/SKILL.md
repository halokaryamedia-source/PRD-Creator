---
name: voice-production-kit
description: Extract traceable voice requirements from accepted PRDs, create ElevenLabs-ready performance scripts and a reference-styled Voice Production DOCX, then validate the final script/DOCX revision without inventing upstream project facts.
version: 1.3.0
---

# Voice Production Kit

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted PRD → `work/voice-requirements.md`.
2. **Flow 6 — ElevenLabs Performance Script Production**: voice requirements → `work/voice-production.md` + `output/Voice Production.docx`.
3. **Flow 7 — Voice Validation & Delivery**: current script/DOCX → `work/voice-acceptance.md` + `voice_delivery_ready`.

## Routing

- Flow 5: read `VOICE-EXTRACTION.md`.
- Flow 6: read `SCRIPT-PRODUCTION.md` and `DOCX-FORMAT.md`.
- Flow 7: read `VOICE-VALIDATION.md`.

Do not skip the current project's state gate.

## Canonical owners

- `work/voice-requirements.md` — which voice moments exist and what they must communicate;
- `work/voice-production.md` — final spoken wording/performance notation;
- `output/Voice Production.docx` — derived production presentation;
- `work/voice-acceptance.md` — revision-specific Flow 7 evidence/findings;
- `state/voice-state.yaml` — lifecycle status/revision/next step across Flow 5–7.

## Non-negotiable rules

- Voice scope cannot change silently after Flow 5.
- Script polish cannot create a new project fact, speaker, channel, trigger, mechanic, reward, or outcome.
- DOCX is generated from canonical Markdown and is never the editable authority.
- Flow 7 must validate the current revision, not an older DOCX against newer script text.
- Critical/Major findings block `voice_delivery_ready`.
- Pronunciation is not called verified without evidence.
- Generated-audio quality is never claimed unless actual audio was supplied and reviewed.
- `voice_delivery_ready` normally refers to script + DOCX delivery scope; audio is a separate evidence dimension unless explicitly included.
- Aftershock remains a demonstrated quality/layout reference only, never project content or quota.
