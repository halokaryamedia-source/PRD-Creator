# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Current Status

`ANTI_OVERDEVELOPMENT_CLEANUP_COMPLETE_REAL_PROJECT_WORK_NEXT`

Working branch: **`Local` only**.

## What changed

The parity hardening track was stopped after it began adding complexity that was not needed by the product flow.

Source cleanup:

`08b6f9d6a98641c5f93932df015cb0d2dffe9a42` — `refactor: remove overdeveloped revision machinery`

Removed:

- PRD render-data SHA/fingerprint metadata;
- Voice Requirements SHA metadata in canonical script;
- Voice script hash / DOCX revision identifier;
- checksum-based derived-artifact revision protocol;
- P1.3 per-entry/revision machinery that made the validator disproportionately complex.

Kept:

- PRD structural validation and exact generated page set/order;
- script-safe glossary handling and required shell-marker checks;
- Voice ID/Type parity;
- basic DOCX section/ID/duration/performance presence checks;
- real blank-page regression;
- controlled builder failure for a zero-entry Voice section;
- Repository Verify + focused Production Verify.

Durable simplification rule:

`docs/knowledge/decisions/anti-overdevelopment-simplification.md`

## Proof

```text
Repository Verify #17
run: 31381677940
head: 08b6f9d6a98641c5f93932df015cb0d2dffe9a42
result: PASS

Production Verify #7
run: 31381677946
head: 08b6f9d6a98641c5f93932df015cb0d2dffe9a42
result: PASS
```

Production Verify passed dependency install, compile, PRD contracts, Voice contracts, and the final fail-closed aggregate.

## Current direction

BuildIT remains a **reference for discipline**, not a checklist of features or machinery to reproduce.

Do not continue P1.4 / P1.5 / P1.6 as automatic phases. A new engineering change requires a concrete current defect or real project need first.

## Next Step

Use the current pipeline on the **next real project/task**. If that real work exposes a concrete defect, route it through Maintenance and apply the smallest fix that solves the observed problem.
