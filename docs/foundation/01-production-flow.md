# Canonical Production Flow

Status: active architecture

## Flow 1 — Repository Boot & Project Memory

Purpose: make the repository independently resumable.

Status: implemented.

## Flow 2 — Source Intake & Requirement Recovery

Purpose: preserve source/provenance, recover requirements, expose conflicts, and isolate real decisions.

Canonical owner: Project Document Generator intake state/contracts.

Status: implemented.

## Flow 3 — Project Document / PRD Generation

Purpose: turn `ready_for_prd` into canonical PRD content and deterministic approved-shell HTML.

Status: implemented.

## Flow 4 — PRD Validation & Team Handoff

Purpose: distinguish generated PRD from production-usable PRD and issue revision-specific handoff readiness.

Status: implemented at contract/tool level; real-project execution proof remains ongoing.

## Flow 5 — Voice Requirement Extraction

Purpose: derive justified, traceable voice moments from a `handoff_ready` PRD without writing final dialogue.

Canonical owners:

- `docs/foundation/05-voice-requirement-extraction.md`;
- `kits/voice-production-kit/VOICE-EXTRACTION.md`;
- project `work/voice-requirements.md` + `state/voice-state.yaml`.

Status: implemented.

## Flow 6 — ElevenLabs Performance Script Production

Purpose: convert `voice_requirements_ready` into final spoken/performance wording and a reference-styled Voice Production DOCX without changing upstream scope.

Canonical owners:

- `docs/foundation/06-elevenlabs-script-production.md`;
- `kits/voice-production-kit/SCRIPT-PRODUCTION.md`;
- `kits/voice-production-kit/DOCX-FORMAT.md`;
- `kits/voice-production-kit/builder/build_docx.py`;
- project `work/voice-production.md` + `state/voice-state.yaml` + `output/Voice Production.docx`.

Status: implemented at contract/tool level; first real project remains execution proof.

## Flow 7 — Voice Validation & Delivery

Purpose: validate final script/DOCX continuity, terminology, pronunciation risk, coverage, pacing/readability, and delivery state for the current revision.

This is the next active boundary.

## Architecture Rule

Implement one flow boundary at a time. Do not change downstream output to compensate for unresolved upstream meaning.
