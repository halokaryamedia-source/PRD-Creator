# Product Boundaries

Status: active policy

## Project Document Generator Owns — Flow 2–4

- source intake/provenance;
- requirement recovery and real decision isolation;
- canonical PRD content;
- approved-shell HTML rendering;
- PRD development-readiness/team handoff.

It does not create voice performance text to compensate for unresolved PRD decisions.

## Voice Production Kit Owns — Flow 5–7

### Flow 5 — Voice Requirement Extraction

- identify justified player-facing voice moments from a `handoff_ready` PRD;
- define Voice ID, type, speaker, channel, trigger, purpose, required facts, and guardrails;
- allow valid `no_voice_required`;
- route missing upstream decisions back to PRD owners.

### Flow 6 — Performance Script Production

- convert the exact accepted Voice ID/type set into final spoken wording;
- add production-appropriate performance direction, emphasis, pauses, line breaks, and Estimated Duration;
- produce canonical `work/voice-production.md`;
- generate derived `output/Voice Production.docx` using the approved formatting reference.

Flow 6 may not add/drop voice moments or project facts without reopening the owning upstream scope.

### Flow 7 — Voice Validation & Delivery

- final terminology/pronunciation/continuity/coverage/readability/delivery acceptance;
- final current-revision delivery status.

Flow 7 is not yet implemented.

## Shared Boundary Rule

If downstream voice work exposes a missing speaker, channel, trigger, story outcome, reward, mechanic, or other product decision, return it to the correct upstream owner. Do not hide the missing decision inside polished dialogue.

## Reference Rule

Aftershock demonstrates layout/performance quality. It does not define another project's speaker, communicator, voice count, duration, script structure, or content.
