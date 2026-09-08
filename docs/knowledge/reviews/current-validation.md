# Current Validation Status

Updated: 2026-09-08

This file records the completed PRD-Creator Package 3 efficiency simplification on `develop`.

## Current system state

Working branch: `develop`.  
Verified integration baseline: `Local`.  
Stable branch: `main`.

PRD Creator package candidate is **v3.0.0** on `develop`. Repository release versioning remains separate from package versioning.

The efficiency cycle is complete on the development candidate. PRD visual grammar, render-data schema, delivery bundle, and Voice semantics were not changed.

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

## Simplification completed

### Flow 2 — approval only when material

- authoritative-only projects no longer require a redundant Simple Chat Preview approval round-trip;
- `preview_approved` may be omitted or `false` when no accepted material Proposal exists;
- an approved material Proposal still requires explicit preview approval evidence;
- exact current requirement bytes remain revision-bound so stale same-version edits are rejected;
- requirement records are guidance-scoped to material rules that benefit from traceability instead of every descriptive detail;
- production skills route approval as an exception for material decisions rather than a mandatory phase.

### Flow 4 — minimal handoff state

`state/handoff-state.yaml` now stores only:

```yaml
status: handoff_ready
accepted_prd_version: <X.Y.Z>
```

The validator derives canonical work/output paths from the accepted version instead of persisting redundant `content`, `render_data`, `html`, `context`, `index`, `acceptance`, and `handoff` references.

Safety remains intact: the handoff validator still proves current PRD validity, semantic version identity, required artifact existence, delivery metadata parity, and exact acceptance bindings.

No compatibility alias layer, second revision registry, derived-path registry, or new approval system was introduced.

## Verification evidence

The implementation candidate at commit `e6f6884fb9f0d02f371e5886c8aaa8ef2d1805fc` passed:

```text
Ruff format + lint/import
mypy shared + renderer + validator
PRD Verify
Voice Verify
full Local promotion regression suite
browser proof inside the full regression suite
```

The preceding repository-contract verification for the handoff refactor also passed, and the final full Local gate re-ran repository contracts on the exact implementation candidate.

## Unchanged boundaries

This efficiency cycle did not change:

- Golden/reference visual grammar;
- `render-data.json` vocabulary or deterministic renderer behavior;
- non-Voice Owner → Moment → Asset identity;
- Flow 4 exact acceptance SHA bindings;
- Voice Owner → Moment → Voice identity or Flow 5–7 semantics;
- delivery bundle structure;
- branch/promotion policy.

## Evidence boundary

Static/repository verification proves contracts, parser behavior, deterministic rendering and regression behavior. It does not prove subjective visual quality beyond the automated browser checks, generated-audio quality, live gameplay QA, implementation completion, or client sign-off.

## Current continuation

No further development step is active from this efficiency cycle. Keep the result on `develop`. Do not promote to `Local` or start runtime-template/CI cleanup unless explicitly requested as a separate scope.