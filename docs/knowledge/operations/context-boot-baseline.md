# Context Boot Baseline

Updated: 2026-08-10

Manual baseline for checking whether repository boot/routing stays efficient. This records **expected routes**; unrun scenarios are not verified.

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

| Scenario | Expected initial route | Expected owner/skill | Status |
|---|---|---|---|
| New project from incomplete source | boot → active project/source → Flow 2 policy | `development-brief` + `project-document-production` | Not run under Phase 2 baseline |
| Existing PRD content/structure change | boot → affected project canonical content/requirements | `development-brief` + `project-document-production` | Not run |
| PRD renderer/HTML defect | boot → reproduce/inspect projection/render owner | Maintenance + `project-document-production` if useful | Not run |
| Voice scope/script change | boot → accepted PRD / Voice state | `development-brief` + `voice-production` | Not run |
| DOCX builder/layout defect | boot → concrete DOCX defect → builder owner | Maintenance + `voice-production` if useful | Historical real example exists; baseline route not rerun |
| Ambiguous cross-owner architecture request | boot → current ownership/decision evidence | Plan first; coordinated-change threshold only if justified | Not run |
| Documentation/routing cleanup | boot → stale owner/link → smallest correction | Maintenance, usually no specialist | Not run |

## Measurement Fields

For an actual scenario record only what is useful:

- files read before semantic owner identified;
- skills activated;
- correct owner found: yes/no;
- unnecessary broad scan: yes/no;
- proof boundary clear: yes/no;
- user asked to repeat recoverable context: yes/no;
- unnecessary new note/skill/module created: yes/no.

Do not add telemetry/scripts solely to measure this baseline.

## Pass Condition

A scenario passes when:

- the correct owner is reached without unnecessary repository-wide scanning;
- no redundant skill/state system is activated;
- the task is routed to the right mode;
- evidence expectations match the execution channel;
- repository continuity avoids asking the user to reconstruct known history.

## Update Rule

Update this note only after a real scenario is exercised. Do not mark expected routes as verified merely because the documentation exists.

## Related

- [Minimal Navigation](../minimal-nav.md)
- [Agent Flow](../flow.md)
- [Skill Activation Matrix](../skills/activation-matrix.md)
- [Maintenance Flow](../maintenance/maintenance-flow.md)
