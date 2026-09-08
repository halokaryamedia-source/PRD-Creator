# Current Validation Status

Updated: 2026-09-08

This file records the current validation boundary for the PRD-Creator Package 3 efficiency simplification on `develop`.

## Current system state

Working branch: `develop`.  
Verified integration baseline: `Local`.  
Stable branch: `main`.

PRD Creator package candidate is **v3.0.0** on `develop`. Repository release versioning remains separate from package versioning.

Package 3 keeps the same PRD visual grammar, render-data schema, delivery bundle, and Voice semantics while reducing production ceremony in Flow 2 and Flow 4.

## Current production chain

```text
project discussion + authoritative source
→ material source inventory + requirement register
→ material Proposal/conflict?
   yes → compact Simple Chat Preview → approval/correction
   no  → continue automatically
→ exact Flow 2 requirement-revision binding
→ work/content.md
→ strict render-data projection
→ deterministic PRD core
→ optional non-Voice 04
→ Flow 4 acceptance
→ minimal handoff revision state
→ optional Voice Flow 5–7
```

Generated output never outranks canonical `state/` or `work/` sources.

Derived delivery remains:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

## Efficiency simplification

### Flow 2 — approval only when material

- authoritative-only projects do **not** require a redundant Simple Chat Preview approval round-trip;
- `preview_approved` may be omitted or `false` when no accepted material Proposal exists;
- an approved material Proposal still requires explicit preview approval evidence;
- the exact current requirement revision remains SHA-bound so stale same-version edits are rejected;
- requirement records are guidance-scoped to material rules that benefit from traceability rather than every descriptive detail;
- production skills route approval as an exception for material decisions instead of a default phase.

This boundary passed Repository Verify, PRD Verify, Voice Verify, static quality, and the full Local regression gate on commit `441db051e116354c6d9c901e8538424a55918689`.

### Flow 4 — minimal handoff state

`state/handoff-state.yaml` now stores only:

```yaml
status: handoff_ready
accepted_prd_version: <X.Y.Z>
```

The validator derives canonical work/output paths from the accepted version instead of persisting redundant `content`, `render_data`, `html`, `context`, `index`, `acceptance`, and `handoff` references.

Safety remains unchanged in intent: the handoff validator still proves current PRD validity, semantic version identity, required artifact existence, delivery metadata parity, and exact acceptance bindings.

No compatibility alias layer, second revision registry, derived-path registry, or new approval system was introduced.

## Unchanged boundaries

This efficiency cycle does not change:

- Golden/reference visual grammar;
- `render-data.json` vocabulary or deterministic renderer behavior;
- non-Voice Owner → Moment → Asset identity;
- Flow 4 exact acceptance SHA bindings;
- Voice Owner → Moment → Voice identity or Flow 5–7 semantics;
- delivery bundle structure;
- branch/promotion policy.

## Verification rule

The only readiness rule for the current candidate is the exact current `develop` HEAD evidence:

```text
Repository Verify
→ Ruff format + lint/import
→ mypy shared + renderer + validator
→ full test_*.py regression + coverage
→ PRD Verify
→ Voice Verify where routed
```

If all applicable gates are green on the exact current HEAD, this efficiency cycle is complete. If any gate fails, fix the first wrong owner and rerun the relevant proof. Do not add more machinery merely to make a theoretical audit item disappear.

## Evidence boundary

Static/repository verification can prove contracts, parser behavior, deterministic rendering and regression behavior. It does not prove subjective visual quality, generated-audio quality, live gameplay QA, implementation completion, or client sign-off.

## Current continuation

Keep this work on `develop`. Do not promote to `Local` unless explicitly requested after current-HEAD verification. Once the current HEAD is green, stop this simplification cycle rather than automatically expanding into runtime-template, CI, or unrelated cleanup.