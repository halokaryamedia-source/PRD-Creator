---
name: voice-production-kit
description: Extract traceable voice requirements from accepted project documentation, then (in downstream Flow 6) produce ElevenLabs-ready voice performance scripts without inventing upstream project decisions.
version: 1.1.0
---

# Voice Production Kit

## Current production boundary

The kit is split into two repository flows:

1. **Flow 5 — Voice Requirement Extraction**: accepted PRD → justified voice moments.
2. **Flow 6 — Performance Script Production**: voice requirements → ElevenLabs-ready script/DOCX.

Flow 5 is implemented now. Flow 6 keeps the original v1.0 production instructions as a reviewed baseline but is not yet redesigned/aligned.

## Flow 5 required order

1. Confirm `state/handoff-state.yaml` is `handoff_ready` for the current accepted PRD revision.
2. Read `VOICE-EXTRACTION.md`.
3. Read the accepted `work/content.md` and `output/team-handoff.md`.
4. Use `state/requirement-register.yaml` when traceability or an upstream decision needs verification.
5. Identify only justified player-facing voice moments.
6. Create/update `work/voice-requirements.md`.
7. Update `state/voice-state.yaml`.
8. Stop when status is `voice_requirements_ready`, `no_voice_required`, `needs_upstream_decision`, or `blocked`.

Do not write performance scripts during Flow 5.

## Flow 6 boundary

`INSTRUCTIONS.md` contains the original v1.0 script-production baseline. Do not start that production stage until Flow 6 is active and `state/voice-state.yaml` is `voice_requirements_ready`.

## Non-negotiable rules

- Preserve official names, sequence, mechanics, triggers, outcomes, and rewards from accepted upstream documentation.
- Do not invent a narrator, speaker, communication channel, lore, mechanic, trigger, reward, or objective detail.
- Do not force voice into every gameplay package.
- Main Story and Radio Communication are production roles, not mandatory counts.
- Radio requires an approved remote communication channel and must stay concise/useful during play.
- If extraction reveals a missing upstream decision, return it upstream rather than solving it in voice production.
- The Aftershock reference demonstrates quality/patterns only; it is not a project-specific requirement.
