# Backlog

Updated: 2026-08-14

This file contains **future/non-active work only**. It never overrides `../next-action.md`.

## Current Backlog

The complete evidence and rationale are preserved in `../reviews/repository-quality-audit-2026-08-14.md`. Do not execute this as a bulk refactor; promote only one next concrete remediation boundary into `next-action.md`.

1. **RQ-08 — validator layering simplification (P2):** after current behavior above is stable, remove monkey-patch ownership incrementally so one current validator owns behavior. Do not rewrite the validator wholesale.
2. **RQ-09 + RQ-11 — renderer global mutation and duplicated manual parsers (P2):** address only with a concrete maintenance need or while the same owner is already changing; prefer one tiny shared reader over schemas/frameworks.
3. **RQ-10 — fixed Golden cardinality vs filler pressure (P2):** requires explicit design approval and real-project evidence before changing the Golden contract. Do not loosen counts as maintenance.
4. **RQ-14 — page lettering >26 (P3):** add only a bounded guard/helper when a real project can exceed the current range.

Closed items RQ-01, RQ-02, RQ-03, RQ-04, RQ-05, RQ-06, RQ-07, RQ-12, RQ-13, RQ-15, and RQ-16 remain documented in the audit and Git history rather than staying in this backlog.
