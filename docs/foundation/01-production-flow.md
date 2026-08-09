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

Purpose: normalize incoming source, recover known facts, classify uncertainty, and prevent users from restating information already present in the project.

Implemented by the active Project Document Generator intake contract:

```text
Original Source
→ Source Inventory
→ Requirement Register
→ Clarification / Completion / Proposal / Blocked
→ resolve supported gaps
→ ask only unresolved high-impact decisions
→ ready_for_prd
```

## Flow 3 — Project Document / PRD Generation

Purpose: turn `ready_for_prd` requirement state into canonical human-readable PRD content and deterministic HTML through the approved presentation shell.

Implemented model:

```text
ready_for_prd
→ work/content.md
→ work/render-data.json (derived)
→ approved-document.html shell
→ renderer/render.py
→ output/final.html
```

Canonical content follows Overview → Gameplay Flow → Global Development → Gameplay Package(s), with Gameplay Overview → Level Design → Developer inside each production-relevant package.

Flow 3 structural generation does not by itself authorize team handoff.

## Flow 4 — PRD Validation & Team Handoff

Purpose: determine whether generated PRD content is actually coherent, development-ready, internally consistent, and usable by intended production roles before handoff.

This is the next active redesign boundary.

## Flow 5 — Voice Requirement Extraction

Purpose: derive justified voice moments from mature project documentation without inventing upstream design facts.

Voice implementation remains deferred until this boundary.

## Flow 6 — ElevenLabs Performance Script Production

Purpose: produce natural, production-ready Main Story and Radio Communication scripts with controlled performance notation.

Current baseline has been reviewed but is not yet migrated.

## Flow 7 — Voice Validation & Delivery

Purpose: check terminology, coverage, pacing, hierarchy, usability, and delivery state before declaring voice production complete.

## Architecture Rule

Implement/revise one flow boundary at a time. Do not modify a downstream flow to compensate for an unresolved upstream contract.
