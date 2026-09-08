# Next Action

## Current Status

`EFFICIENCY_SIMPLIFICATION_CURRENT_HEAD`

PRD-Creator Package 3 on `develop` now has two targeted simplifications:

1. Flow 2 approval is exception-driven: authoritative-only projects continue without a redundant preview round-trip, while material AI Proposals still require explicit approval.
2. Flow 4 handoff state stores only `status` + `accepted_prd_version`; deterministic work/output paths are derived and verified instead of persisted as duplicate state.

Branch roles remain:

- `develop` → active candidate and verification target;
- `Local` → protected verified integration baseline;
- `main` → stable repository history.

Do not promote to `Local` until explicitly requested after exact-current-HEAD verification.

## Active Boundary

```text
authority settles project model
→ bind exact requirement revision
→ Flow 3 automatically

material AI Proposal exists
→ compact preview
→ approval/correction
→ bind exact accepted requirement revision
→ Flow 3

Flow 4 accepted revision
→ state/handoff-state.yaml = status + accepted_prd_version
→ validator derives canonical work/output paths
→ prove artifact existence + delivery parity + exact acceptance
→ Flow 5 when required
```

Keep these boundaries intact:

- no duplicate readiness aliases;
- no second approval/revision registry;
- stale requirement bytes still invalidate the Flow 2 binding;
- approved Proposals still require explicit review evidence;
- no deterministic artifact-path fields in `handoff-state.yaml`;
- exact Flow 4 acceptance bindings remain mandatory;
- Golden/render schema/delivery bundle/Voice semantics remain unchanged.

## Next Step

Use the exact current `develop` HEAD CI as the stop condition:

1. Repository Verify;
2. Ruff format + lint/import;
3. mypy shared + renderer + validator;
4. full `test_*.py` regression + coverage;
5. PRD Verify;
6. Voice Verify where routed.

If all applicable gates are green, **STOP**: the current efficiency simplification is complete. If a gate fails, fix the first wrong owner and rerun the relevant proof.

Do not automatically continue into runtime-template, CI deduplication, promotion, or unrelated cleanup after green verification; those are separate later scopes.