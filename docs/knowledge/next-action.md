# Next Action

Updated: 2026-08-11

## Current Status

`FLOW2_EXPLICIT_STATE_CONTRADICTIONS_GUARDED_NEXT_FLOW5_REQUIREMENT_COMPLETENESS`

Working branch: **`Local` only**.

## Completed current correction sequence

The audited PRD-side false-green chain is now protected through unambiguous Flow 2 persisted-state blockers and the Flow 4 → Flow 5 handoff boundary:

```text
Flow 2 intake declaration
↓ explicit persisted-state blocker guard
work/content.md
↓ canonical_content_sha256
work/render-data.json
↓ render-data-sha256
output/final.html
↓ Flow 4 review / handoff
existing document.version
↓ accepted_prd_version
Flow 5 entry
```

Current guards include:

- `state/intake-state.yaml` must explicitly report `status: ready_for_prd` + `ready_for_prd: true`;
- when readiness is claimed, `validator/validate.py` rejects only unambiguous persisted blockers already present in current state:
  - `requirement-register.yaml`: `approval_status: pending` or `recovery_class: blocked`;
  - `source-inventory.yaml`: `inspection: blocked`;
- `evidence_status: conflict` alone is intentionally allowed because the conflict may already have a valid higher-authority/approved resolution;
- approved proposals, `inspection: targeted`, omitted defaults, optional/advisory ideas, and other nonblocking detail do not fail this guard;
- existing content→projection and projection→HTML SHA guards remain unchanged;
- Flow 4 → Flow 5 uses existing `document.version` / `accepted_prd_version`; no handoff SHA was added;
- scoring, bilingual display-text, and wrapped Golden-grid guards remain active.

The Flow 2 state check is intentionally line-level and bounded. It is not a generic YAML parser/schema, semantic completeness engine, conflict resolver, or materiality classifier.

## Current proof

Final narrowed implementation state before this documentation synchronization:

```text
70139643c799d451d5a671d5768392fb19ab1e4d  initial validator guard
25104df7e15bad3ed424fd7dc7bcf50070ce29a2  initial Flow 2 state tests
432eef641b695102d7446337a297e35136d3bc95  CI includes Flow 2 state contracts
efcd194b33bce08519d6d586d6948f4bdae67949  narrow to unambiguous blockers
114df1b4c6a7de1c3359091a98338820d5a1adc5  prove resolved conflict remains allowed
```

GitHub evidence:

```text
Repository Verify #89 — PASS
Production Verify #45 — PASS
Project Document contracts — PASS
```

This remains repository/static/regression proof only. Per current user direction, **do not run local/manual real-project or browser proof yet**.

## Explicit boundaries

The guard can catch only blockers that were actually persisted with the exact unambiguous markers above. It does not infer a hidden missing requirement, decide whether an unspecified detail is material, or replace Flow 2 semantic review.

No new SHA/checksum was added in this slice.

## Deliberately not changed

- no generic YAML/schema framework;
- no automatic semantic/materiality scoring;
- no automatic unresolved-conflict interpretation;
- no additional artifact manifest/checksum chain;
- no change to Flow 5 Voice scope/content yet;
- no mass renderer vocabulary refactor;
- no local/manual real-project or browser run.

## Next Step

Address the next concrete audited weak boundary in **Flow 5 — Voice Requirement Extraction**: the executable requirement parser currently proves only a subset of the documented Voice Requirement contract.

Close only the completeness gap for existing required fields (`Function`, `Necessity`, `Purpose`, non-empty `Must communicate`, `Must not add/repeat`, and `Source refs`) before Flow 6 can rely on a Voice requirement entry. Do not add a Voice schema framework, semantic similarity engine, automatic lore/mechanic inference, or checksum chain.
