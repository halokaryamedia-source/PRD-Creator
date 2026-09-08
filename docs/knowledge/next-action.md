# Next Action

## Current Status

`FLOW2_EFFICIENCY_SIMPLIFICATION_PENDING_VERIFICATION`

PRD-Creator Package 3 on `develop` now removes the default Flow 2 approval round-trip for authoritative-only projects while preserving explicit approval for material AI Proposals.

Branch roles remain:

- `develop` → active candidate and verification target;
- `Local` → protected verified integration baseline;
- `main` → stable repository history.

Do not promote to `Local` until this candidate is verified and explicitly accepted for promotion.

## Active Boundary

Current Flow 2 behavior should be:

```text
authority settles project model
→ bind exact requirement revision
→ ready_for_prd
→ continue directly to Flow 3

material AI Proposal exists
→ compact preview
→ user approval/correction
→ bind exact accepted requirement revision
→ ready_for_prd
```

Keep these boundaries intact:

- no duplicate readiness aliases;
- no second approval/revision registry;
- stale requirement bytes still invalidate the Flow 2 binding;
- approved Proposals still require explicit review evidence;
- existing `preview_approved: true` states remain valid;
- Golden/render schema/Flow 4/Voice behavior remain unchanged by this pass.

## Next Step

Run verification on the exact final `develop` HEAD:

1. Repository Verify;
2. Ruff format + lint/import;
3. mypy shared + renderer + validator;
4. full `test_*.py` regression + coverage;
5. PRD Verify;
6. Voice Verify where routed.

If a gate fails, fix the first wrong owner and rerun the relevant proof. Do not widen this task into runtime-template, handoff-state, CI, or unrelated cleanup until this production-flow simplification is green.