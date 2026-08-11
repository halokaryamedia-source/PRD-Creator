# Next Action

Updated: 2026-08-11

## Current Status

`FLOW4_TO_FLOW5_HANDOFF_VERSION_GUARDED_NEXT_FLOW2_STATE_CONSISTENCY`

Working branch: **`Local` only**.

## Completed current correction sequence

The audited PRD false-green chain is now protected through the Flow 4 → Flow 5 handoff boundary without adding another checksum layer:

```text
Flow 2 explicit ready state
↓
work/content.md
↓ canonical_content_sha256
work/render-data.json
↓ generated render-data-sha256 metadata
output/final.html
↓
Flow 4 review / handoff
↓ existing document.version
state/handoff-state.yaml accepted_prd_version
↓ validate_handoff.py
Flow 5 entry
```

Current guards include:

- Flow 4 rejects missing/ambiguous/non-ready `state/intake-state.yaml`;
- `render-data.json` must match the exact current bytes of `work/content.md` through the existing `canonical_content_sha256` guard;
- generated `final.html` must contain exactly one valid `render-data-sha256` marker matching current `render-data.json`;
- Flow 4 → Flow 5 adds **no new SHA**: the already-existing `document.version` is reused as the accepted handoff revision;
- `state/handoff-state.yaml` records `accepted_prd_version` plus the existing canonical/render/HTML/acceptance/team-handoff paths;
- `validator/validate_handoff.py` blocks Flow 5 when handoff is not `handoff_ready`, the accepted version differs from current `document.version`, or the recorded current artifacts are missing/wrong;
- a material canonical meaning change after handoff must advance `document.version` and reopen state to `pending_review` before downstream use;
- weighted scoring, bilingual display-text, and wrapped Golden-grid guards remain active.

The handoff guard is intentionally a small lifecycle check. It is not an artifact manifest, checksum chain, semantic comparison engine, or new workflow framework.

## Current proof

Implementation sequence:

```text
6e75c056bb6dea52a6bcf84481d8b30b6824c80f  handoff entry guard
f379ad4a5b27cdc208bfdfcf9406159e9c93d29a  focused regression tests
119063ca8d57cd816f01a1dfae5ae00ade517a64  Production Verify includes handoff contracts
```

GitHub evidence on the implementation HEAD:

```text
Repository Verify #80 — PASS
Production Verify #37 — PASS
Project Document contracts (including handoff tests) — PASS
```

This is repository/static/regression proof only. Per current user direction, **do not run local/manual real-project or browser proof yet**.

## Explicit tradeoff

The Flow 4 → Flow 5 guard deliberately does not hash another boundary. It assumes the existing lifecycle rule is followed: when accepted PRD meaning changes materially, `document.version` advances and handoff returns to `pending_review`.

Therefore the guard can detect:

- stale accepted version;
- non-ready state;
- missing/wrong current handoff artifact paths.

It does not automatically detect an operator changing material canonical meaning while incorrectly leaving `document.version` unchanged. That limitation is accepted to avoid turning PRD-Creator into a broad revision/checksum system.

## Deliberately not changed

- no third SHA/checksum binding for handoff;
- no artifact manifest or generic revision registry;
- no Voice requirement/script/DOCX revision framework in this slice;
- no Flow 5 scope/content redesign;
- no mass renderer vocabulary refactor;
- no local/manual real-project or browser run.

## Next Step

Address the remaining audited PRD-side false-ready boundary in **Flow 2**: `state/intake-state.yaml` must not claim `ready_for_prd` while persisted `state/requirement-register.yaml` or `state/source-inventory.yaml` explicitly contains a material pending/blocking state that contradicts readiness.

Keep this narrow: detect only explicit persisted contradictions. Do not attempt to automate Flow 2 semantic judgment, create a generic YAML/schema framework, or turn every optional/open detail into a blocker.
