# Canonical Production Flow

Status: active architecture

## Flow 1 — Repository Boot & Project Memory
Purpose: make the repository independently resumable.
Status: implemented.

## Flow 2 — Source Intake & Requirement Recovery
Purpose: preserve source/provenance, recover requirements, expose conflicts, and ask only real high-impact decisions.
Status: implemented.

## Flow 3 — Project Document / PRD Generation
Purpose: turn `ready_for_prd` state into canonical PRD content and approved-shell HTML without adding project meaning.
Status: implemented.

## Flow 4 — PRD Validation & Team Handoff
Purpose: distinguish generated PRD from development-ready PRD and issue revision-specific team handoff.
Status: implemented.

## Flow 5 — Voice Requirement Extraction
Purpose: derive justified, traceable voice moments from the accepted PRD without inventing upstream facts.
Status: implemented.

## Flow 6 — ElevenLabs Performance Script Production
Purpose: convert accepted Voice Requirements into canonical spoken/performance wording and a derived reference-styled DOCX while preserving exact Voice scope.
Status: implemented.

## Flow 7 — Voice Validation & Delivery
Purpose: validate the exact current Voice Requirements → Script → DOCX chain and declare script/DOCX delivery-ready only after mechanical, semantic, terminology/pronunciation, continuity, and visual gates pass.

Canonical owners:

- `docs/foundation/07-voice-validation-delivery.md`;
- `kits/voice-production-kit/VOICE-VALIDATION.md`;
- `kits/voice-production-kit/validator/validate.py`;
- per-project `work/voice-acceptance.md` + `state/voice-state.yaml`.

Actual audio is reviewed only when supplied/in scope. No audio-quality claim is inferred from script quality.

Status: implemented and exercised on the real The Clockwork Vault integration project.

## After Flow 7

There is no Flow 8 in the canonical production sequence.

System Integration Proof is complete on **The Clockwork Vault** and the final retirement audit concluded the old `Production Document Builder/` has no remaining active dependency. The live Archived tree is retired; there is no migration Flow 8.

## Architecture Rule

Implement/fix the owning boundary rather than using downstream polish to compensate for unresolved upstream meaning.
