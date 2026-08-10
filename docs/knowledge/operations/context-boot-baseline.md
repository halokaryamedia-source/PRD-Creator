# Context Boot Baseline

Updated: 2026-08-10

Manual baseline for checking whether repository boot/routing stays efficient. Expected routes become verified only after an actual scenario is exercised.

## Targets

- start from `AGENTS.md → CONTEXT.md → next-action.md`;
- identify the semantic owner before broad-reading files;
- Developing uses `development-brief` and at most one specialist;
- Maintenance starts from concrete defect/root-cause evidence, not `development-brief` by default;
- do not read the task board during normal boot;
- open `activation-matrix.md` only when skill choice is actually needed;
- use proof appropriate to the active channel and claimed result;
- avoid broad scans of saved projects, all references, generated artifacts, or Git history when the owner is already known.

## Scenarios

| Scenario | Expected initial route | Expected owner/skill | Phase 3 status |
|---|---|---|---|
| New project from incomplete source | boot → active project/source → Flow 2 policy | `development-brief` + `project-document-production` | **PASS — route exercised** |
| Existing PRD content/structure change | boot → affected project canonical content/requirements | `development-brief` + `project-document-production` | **PASS — route exercised** |
| PRD renderer/HTML defect | boot → reproduce/inspect projection/render owner | Maintenance + `project-document-production` if useful | **PASS — owner route confirmed; no defect mutation required** |
| Voice scope/script change | boot → accepted PRD / Voice state | `development-brief` + `voice-production` | **PASS — route exercised** |
| DOCX builder/layout defect | boot → concrete DOCX defect → builder owner | Maintenance + `voice-production` if useful | **PASS — historical real defect remains supporting evidence** |
| Ambiguous cross-owner architecture request | boot → current ownership/decision evidence | Plan first; coordinated-change threshold only if justified | **PASS — Phase 1–3 parity work used explicit phased contract** |
| Documentation/routing cleanup | boot → stale owner/link → smallest correction | Maintenance, usually no specialist | **PASS — real Project Document broad-read defect found** |

## Phase 3 Measurements

### Developing — Project Document

- boot state: already current from the active Phase 2 continuation;
- additional routing reads before semantic owner confirmation: `development-brief`, activation matrix, `project-document-production`;
- correct owner found: yes;
- unnecessary broad scan: no;
- proof boundary clear: yes;
- user asked to repeat recoverable context: no;
- unnecessary new skill/state system created: no.

### Developing — Voice

- additional routing reads before semantic owner confirmation: activation matrix + `voice-production`;
- correct owner found: yes;
- unnecessary Project Document/reference scan: no;
- proof boundary clear: yes;
- user asked to repeat recoverable context: no.

### Maintenance — Project Document Kit Routing

- concrete defect: kit `SKILL.md` forced broad fixed reading across Flow 2–4;
- owner: Project Document kit procedure / nearest local agent rules;
- root cause grounded before edit: yes;
- correction: Flow-first reading + nearest `AGENTS.md`;
- new root skill required: no;
- production semantics changed: no.

## Pass Condition

A scenario passes when:

- the correct owner is reached without unnecessary repository-wide scanning;
- no redundant skill/state system is activated;
- the task is routed to the right mode;
- evidence expectations match the execution channel;
- repository continuity avoids asking the user to reconstruct known history.

## Current Result

Representative boot/routing scenarios satisfy the Phase 3 routing acceptance. The remaining Phase 3 external proof is the first successful `Repository Verify` GitHub Actions run after the maintenance/gate implementation is committed.

## Update Rule

Update this note only after an actual scenario is exercised. Do not mark expected routes as verified merely because the documentation exists.

## Related

- [Minimal Navigation](../minimal-nav.md)
- [Agent Flow](../flow.md)
- [Skill Activation Matrix](../skills/activation-matrix.md)
- [Maintenance Flow](../maintenance/maintenance-flow.md)
- [Operating Parity Acceptance](operating-parity-acceptance.md)
