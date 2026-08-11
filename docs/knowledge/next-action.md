# Next Action

Updated: 2026-08-11

## Current Status

`PRD_REPRESENTATIVE_FLOW2_NEEDS_AFTERSHOCK_SCORING_DECISION`

Working branch: **`Local` only**.

## Current system state

The three pre-test deterministic blockers are closed:

- glossary role visibility is consistent between inline highlighting and Terms Used;
- Reset / Interruption requires an explicit post-reset Expected System Result;
- Flow 4/handoff requires an explicit Acceptance lens PASS.

Current focused proof:

```text
PRD Verify #108 — PASS
```

## Representative test status

Representative Flow 2 testing has started with AFTERSHOCK `FINAL v2.4`.

The test correctly stopped before Flow 3 because current scoring meaning is unresolved:

```text
current v2.4
→ no player-facing score/results
→ no score/aggregate/interpretation in raw telemetry
→ objective progress/outcome data exists
→ no current internal Objective Score formula is defined

older Golden Sample
→ internal Objective Scores + Final Total exist
→ several formulas depend on older mechanics that no longer match v2.4
```

Therefore neither of these is valid without a new approved decision:

```text
infer No Objective Score from display/export rules
OR
copy the old Golden scoring formulas into v2.4
```

Flow 2 must remain `needs_decision` for this representative project until the current internal scoring model is resolved.

No representative HTML/browser/mobile/Voice proof should be run while this material scoring decision remains unresolved.

## Next Step

**Resolve and approve the current AFTERSHOCK internal scoring model for the v2.4 mechanics; then resume the same representative proof at Flow 3 without restarting completed intake work.**
