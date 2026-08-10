# Canonical Production Flow

Status: active architecture

## Flow 1 — Repository Boot & Project Memory

Purpose: make the repository independently resumable without relying on old chat context.

Status: implemented.

## Flow 2 — Source Intake & Requirement Recovery

Purpose: preserve project source, record provenance/authority, recover requirements, expose conflicts, and ask only for real high-impact decisions.

Owners: `docs/foundation/02-source-intake-recovery.md`, active Project Document Generator intake procedure, and per-project intake state.

Status: implemented.

## Flow 3 — Project Document / PRD Generation

Purpose: turn `ready_for_prd` requirement state into canonical PRD content and approved-shell HTML without adding new project meaning.

Owners: `docs/foundation/03-prd-generation.md`, `CONTENT-CONTRACT.md`, `RENDERING.md`, and active renderer.

Status: implemented.

## Flow 4 — PRD Validation & Team Handoff

Purpose: distinguish generated PRD from development-ready PRD and issue a concise team handoff for an accepted revision.

Owners: `docs/foundation/04-prd-validation-handoff.md`, Project Document Generator `VALIDATION.md`, validator, acceptance/handoff state.

Critical/Major findings block handoff. Mechanical pass alone never establishes semantic readiness.

Status: implemented at contract/tool level; first real-project handoff remains execution proof.

## Flow 5 — Voice Requirement Extraction

Purpose: convert a current accepted `handoff_ready` PRD into a traceable set of justified voice moments without writing final scripts or inventing upstream facts.

Canonical owners:

- `docs/foundation/05-voice-requirement-extraction.md`;
- `kits/voice-production-kit/VOICE-EXTRACTION.md`;
- per-project `work/voice-requirements.md`;
- per-project `state/voice-state.yaml`.

A valid result is either `voice_requirements_ready` or `no_voice_required`. Missing material speaker/channel/trigger/story decisions return upstream.

Status: implemented at contract/kit level; first real-project extraction remains execution proof.

## Flow 6 — ElevenLabs Performance Script Production

Purpose: turn accepted voice requirements into natural, production-ready Main Story / Radio Communication / other approved voice scripts with controlled ElevenLabs notation and final DOCX structure.

The original Voice Production Kit v1.0 instructions are preserved as a reviewed baseline; Flow 6 redesign/alignment is the next active boundary.

## Flow 7 — Voice Validation & Delivery

Purpose: validate terminology, coverage, pacing, hierarchy, continuity, and delivery state before voice production is declared complete.

Not yet implemented.

## Architecture Rule

Implement one flow boundary at a time. Do not change a downstream flow to compensate for an unresolved upstream contract.
