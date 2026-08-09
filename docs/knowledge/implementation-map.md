# Implementation Map

Updated: 2026-08-10

Use this note to answer where current behavior or policy lives. It is not the active task tracker.

## Repository Areas

| Boundary | Current owner |
|---|---|
| Repository-wide work rules / authority | `AGENTS.md` |
| Stable product context / terminology | `CONTEXT.md` |
| Durable product boundaries | `docs/foundation/00-product-boundaries.md` |
| End-to-end production sequence | `docs/foundation/01-production-flow.md` |
| Current evidence/implementation status | `docs/foundation/validation-report.md` |
| Active continuation state | `docs/knowledge/next-action.md` |
| Durable decisions and reasons | `docs/knowledge/decision-log.md` |
| Active project packages | `workspace/active/` |
| Saved/completed project packages | `workspace/saved/` |
| Pre-existing historical document-builder package | `Production Document Builder/` |

## Pending Baseline Migration

- **Project Document Generator** — supplied and reviewed; migrate/reconcile only when Flow 3 is active.
- **Voice Production Kit** — supplied and reviewed; migrate/reconcile only when Flow 5/6 is active.
- **Production Document Builder** — already present in the repository; historical/reference only until a bounded flow-specific audit adopts a proven part.

## Current Boundary

Flow 1 adds repository architecture only. It does not migrate either supplied kit and does not modify or delete the pre-existing `Production Document Builder/` package. Flow 2 is the next active boundary; any later adoption from the historical package or supplied kits must be evidence-driven and limited to the owning flow.
