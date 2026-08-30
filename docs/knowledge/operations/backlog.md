# Backlog

Updated: 2026-08-30

This file contains **future/non-active work only**. It never overrides `../next-action.md`.

## Current Backlog

1. **RQ-10 — fixed Golden cardinality vs filler pressure (P2):** requires explicit Golden-design approval plus real-project evidence before changing the representation contract. Do not loosen counts as repository maintenance.
2. **RQ-11 — duplicated manual parsers (P2):** address only when a concrete parser defect or same-owner change proves the need; prefer one tiny shared reader over schemas/frameworks.
3. **RQ-14 — page lettering >26 (P3):** add a bounded guard/helper only when a real project can exceed the current range.

## Recently closed

- **RQ-09 — renderer global mutation:** closed on the `develop` professionalization tranche. Golden rendering now adapts the canonical marker in the temporary template instead of mutating `_engine.STORAGE_PREFIX_TOKEN`.

Closed earlier items remain documented in historical audits and Git history rather than staying in this backlog.
