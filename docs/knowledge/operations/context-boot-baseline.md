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

| Scenario | Expected initial route | Expected owner/skill | Phase 3 result |
|---|---|---|---|
| New project from incomplete source | boot → active project/source → Flow 2 policy | `development-brief` + `project-document-production` | **PASS** |
| Existing PRD content/structure change | boot → affected project canonical content/requirements | `development-brief` + `project-document-production` | **PASS** |
| PRD renderer/HTML defect | boot → reproduce/inspect projection/render owner | Maintenance + `project-document-production` if useful | **PASS** |
| Voice scope/script change | boot → accepted PRD / Voice state | `development-brief` + `voice-production` | **PASS** |
| DOCX builder/layout defect | boot → concrete DOCX defect → builder owner | Maintenance + `voice-production` if useful | **PASS — historical real defect supports same route** |
| Ambiguous cross-owner architecture request | boot → current ownership/decision evidence | Plan first; coordinated-change threshold only if justified | **PASS** |
| Documentation/routing cleanup | boot → stale owner/link → smallest correction | Maintenance, usually no specialist | **PASS — real broad-read defect found/fixed** |

## Phase 3 Measurements

### Developing — Project Document

- boot state remained current from repository continuity;
- routing reads before semantic owner confirmation: `development-brief`, activation matrix, `project-document-production`;
- correct owner found: yes;
- unnecessary broad scan: no;
- proof boundary clear: yes;
- user asked to repeat recoverable context: no;
- unnecessary new skill/state system created: no.

### Developing — Voice

- routing reads before semantic owner confirmation: activation matrix + `voice-production` after the Developing front door;
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

## Repository Gate Proof

`Repository Verify` run `31367001967` passed on commit `5970c47c15c8e9e83df185be7c5472e976739062`.

This confirms the accepted routing/ownership tree also satisfies the automated static invariants without weakening the gate.

## Pass Condition

A scenario passes when:

- the correct owner is reached without unnecessary repository-wide scanning;
- no redundant skill/state system is activated;
- the task is routed to the right mode;
- evidence expectations match the execution channel;
- repository continuity avoids asking the user to reconstruct known history.

## Current Result

Representative boot/routing scenarios and the repository static gate pass. The baseline supports final `OPERATING_PARITY_ACCEPTED` status.

## Update Rule

Future scenarios are added only when a real task exposes a new routing pattern or failure. Do not maintain ceremonial telemetry.

## Related

- [Minimal Navigation](../minimal-nav.md)
- [Agent Flow](../flow.md)
- [Skill Activation Matrix](../skills/activation-matrix.md)
- [Maintenance Flow](../maintenance/maintenance-flow.md)
- [Operating Parity Acceptance](operating-parity-acceptance.md)
