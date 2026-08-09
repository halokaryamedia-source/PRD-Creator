# Implementation Map

Updated: 2026-08-10

Use this note to answer where current behavior or policy lives. It is not the active task tracker.

## Repository Areas

| Boundary | Current owner |
|---|---|
| Permanent working branch | `Local` |
| Repository-wide work rules / authority | `AGENTS.md` |
| Stable product context / terminology | `CONTEXT.md` |
| Durable product boundaries | `docs/foundation/00-product-boundaries.md` |
| End-to-end production sequence | `docs/foundation/01-production-flow.md` |
| Source intake / recovery policy | `docs/foundation/02-source-intake-recovery.md` |
| Source intake executable procedure | `kits/project-document-generator/SOURCE-INTAKE.md` |
| Project Document Generator current kit | `kits/project-document-generator/` |
| Current evidence/implementation status | `docs/foundation/validation-report.md` |
| Active continuation state | `docs/knowledge/next-action.md` |
| Durable decisions and reasons | `docs/knowledge/decision-log.md` |
| Active project packages | `workspace/active/` |
| Saved/completed project packages | `workspace/saved/` |
| Archived historical document-builder package | `Production Document Builder/` |

## Current Baseline State

- **Project Document Generator** — migrated into `kits/project-document-generator/`; Flow 2 intake/recovery integrated. Flow 3 canonical content/rendering audit is next.
- **Voice Production Kit** — supplied and reviewed; migrate/reconcile only when Flow 5/6 is active.
- **Production Document Builder** — Archived. Preserve for bounded migration/reference until useful behavior/dependencies are evaluated and migrated or intentionally retired.

## Current Boundary

Flow 2 is complete at repository/kit contract level. It does not claim a real project has already passed intake. Flow 3 is the next active boundary and must consume the recovered requirement state rather than restarting source discovery from scratch.
