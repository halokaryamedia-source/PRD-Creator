# Canonical Production Flow

Status: active architecture

## Flow 1 — Repository Boot & Project Memory

Purpose: make the repository independently resumable without relying on old chat context.

Required owners:

- `AGENTS.md` — work rules and authority;
- `CONTEXT.md` — stable facts/terminology;
- `docs/knowledge/next-action.md` — one active task and next step;
- `docs/knowledge/decision-log.md` — durable decisions/reasons;
- `docs/knowledge/implementation-map.md` — where current behavior lives;
- `docs/foundation/validation-report.md` — current evidence state.

## Flow 2 — Source Intake & Requirement Recovery

Purpose: normalize incoming source, recover known facts, classify uncertainty, and prevent the user from having to restate information already present in the project.

This flow is not implemented yet in the repository architecture revision.

## Flow 3 — Project Document / PRD Generation

Purpose: turn recovered requirements into canonical project documentation using Project Document Generator rules and the approved template.

Current baseline was supplied and reviewed, but repository migration is deferred until this flow is implemented.

## Flow 4 — PRD Validation & Team Handoff

Purpose: determine whether the document is actually development-ready, distinguish generated from approved/verified content, and provide a clear handoff boundary.

This flow is not yet redesigned.

## Flow 5 — Voice Requirement Extraction

Purpose: derive justified voice moments from mature project documentation without inventing upstream design facts.

Current downstream kit exists, but this explicit handoff flow is not yet redesigned.

## Flow 6 — ElevenLabs Performance Script Production

Purpose: produce natural, production-ready Main Story and Radio Communication scripts with controlled performance notation.

Current baseline was supplied and reviewed, but repository migration is deferred until this flow is implemented.

## Flow 7 — Voice Validation & Delivery

Purpose: check terminology, coverage, pacing, hierarchy, usability, and delivery state before declaring voice production complete.

This flow is not yet redesigned.

## Architecture Rule

Implement or revise one flow boundary at a time. Do not modify a downstream flow to compensate for an unresolved upstream contract.
