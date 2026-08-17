# Product Boundaries

Status: active policy

## PRD Creator — Project / Document Domain

Inside `kits/prd-creator/`, the Project/PRD domain owns:

- project-source intake, production requirement recovery, and Flow 2 problem solving;
- safe Clarification/Completion vs Proposal/Blocked decision boundaries;
- clear user-facing explanation of material unresolved decisions without changing technical meaning;
- canonical PRD content and deterministic rendering through the approved Golden hierarchy, page composition, component language, and presentation foundation;
- same-project HTML composition that preserves accepted PRD hierarchy while appending approved downstream Production Assets;
- development-readiness validation and concise team handoff.

It does not own downstream Voice wording.

## PRD Creator — Voice Domain

### Flow 5

- extracting justified Voice moments from accepted PRD content;
- preserving Speaker/Channel/Trigger/Purpose and required facts;
- preventing redundant or unsupported Voice scope.

### Flow 6

- final spoken wording and performance notation for accepted Voice IDs;
- Estimated Duration as an estimate;
- canonical `work/voice-production.md` production content.

### Flow 7

- exact-revision Voice ID/Type/Speaker and project-HTML integrity validation;
- Communication Conservation and integrated Voice Script Readiness;
- current consolidated project-HTML visual QA when claimed;
- truthful delivery state and evidence boundaries.

## Voice Domain Does Not Own

- repairing unresolved project/PRD decisions by invention;
- adding new Voice moments during script polishing or final audit;
- rebuilding or renumbering accepted PRD navigation/page identity;
- treating derived HTML as higher authority than canonical script/requirements.

## Default Delivery Scope

The normal non-audio Voice deliverable is the accepted **canonical Voice Production script + current consolidated project HTML (`output/v<document.version>/prd.html`)**.

Audio remains a separate evidence/delivery scope when explicitly in scope.

## Shared Boundary Rule

Project/PRD and Voice are separate semantic domains inside one `kits/prd-creator/` product package.

When downstream work exposes a missing or contradictory upstream decision, reopen the correct owner. Do not hide the decision inside polished PRD/script/audit text or derived presentation output.
