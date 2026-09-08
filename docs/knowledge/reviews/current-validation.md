# Current Validation Status

Updated: 2026-09-08

This file records the current validation boundary for the PRD-Creator Package 3 efficiency simplification on `develop`.

## Current system state

Working branch: `develop`.  
Verified integration baseline: `Local`.  
Stable branch: `main`.

PRD Creator package candidate is **v3.0.0** on `develop`. Repository release versioning remains separate from package versioning.

The current candidate simplifies Flow 2 production behavior without changing PRD visual grammar, render-data schema, delivery format, or Voice semantics.

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
→ Flow 4 acceptance / handoff
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

## Efficiency simplification implemented

The current candidate changes Flow 2 so that:

- authoritative-only projects do **not** require a redundant Simple Chat Preview approval round-trip;
- `preview_approved` may be omitted or `false` when no accepted material Proposal exists;
- an approved material Proposal still requires explicit preview approval evidence;
- the exact current requirement revision remains SHA-bound so stale same-version requirement edits are still rejected;
- existing projects that retain `preview_approved: true` remain valid;
- requirement records are guidance-scoped to material rules that benefit from traceability rather than every descriptive detail;
- production skills now route approval as an exception for material decisions instead of a default Flow 2 ceremony.

No compatibility alias layer, second revision registry, or new approval system was introduced.

## Unchanged boundaries

This pass does not change:

- Golden/reference visual grammar;
- `render-data.json` schema or deterministic renderer behavior;
- non-Voice Owner → Moment → Asset identity;
- Flow 4 exact acceptance bindings;
- Voice Owner → Moment → Voice identity or Flow 5–7 semantics;
- delivery bundle structure;
- branch/promotion policy.

## Verification required

The exact final `develop` candidate must pass:

```text
Repository Verify
→ Ruff format + lint/import
→ mypy shared + renderer + validator
→ full test_*.py regression + coverage
→ PRD Verify
→ Voice Verify where routed
```

The key new regression requirements are:

1. authoritative-only Flow 2 can be `ready_for_prd` without preview approval;
2. explicit `preview_approved: false` is valid when no Proposal exists;
3. approved material Proposal without preview approval is rejected;
4. stale requirement revision binding is still rejected;
5. existing preview-approved projects remain valid.

## Evidence boundary

Static/repository verification can prove contracts, parser behavior, deterministic rendering and regression behavior. It does not prove subjective visual quality, generated-audio quality, live gameplay QA, implementation completion, or client sign-off.

## Current continuation

Keep this work on `develop`. If verification fails, fix the first wrong owner and rerun the smallest relevant proof. Do not promote to `Local` as part of this simplification unless explicitly requested after acceptance.