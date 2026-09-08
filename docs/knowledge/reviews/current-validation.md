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

- authoritative-only projects do not require a redundant Simple Chat Preview approval round-trip;
- `preview_approved` may be omitted or `false` when no accepted material Proposal exists;
- an approved material Proposal still requires explicit preview approval evidence;
- exact current requirement bytes remain revision-bound so stale same-version edits are rejected;
- requirement records are guidance-scoped to material rules that benefit from traceability instead of every descriptive detail;
- production skills route approval as an exception for material decisions rather than a mandatory phase.

### Flow 4 — minimal handoff state

`state/handoff-state.yaml` stores only:

```yaml
status: handoff_ready
accepted_prd_version: <X.Y.Z>
```

The validator derives canonical work/output paths from the accepted version instead of persisting redundant `content`, `render_data`, `html`, `context`, `index`, `acceptance`, and `handoff` references.

Safety remains intact: the handoff validator still proves current PRD validity, semantic version identity, required artifact existence, delivery metadata parity, and exact acceptance bindings.

### Operator — reuse downstream proof

`tools/prd.py status` now starts from the deepest present mechanical stage:

```text
Voice present   → Voice validation → reuse proven handoff/PRD result
Handoff present → Handoff validation → reuse proven PRD result
PRD only        → PRD validation
```

A failed downstream proof still falls back only far enough to identify the first wrong upstream owner. Healthy project status no longer replays PRD validation merely because handoff/Voice also needs the same proof.

### Change-impact routing

`tools/prd.py impact` accepts explicit changed paths or `--git-base <ref>` and returns the smallest relevant proof set across:

```text
repository
prd
handoff
voice
browser
full_regression
```

Direct edits under `output/` are flagged as derived-output edits and routed back to canonical ownership rather than treated as legitimate source changes.

This is routing in the existing operator facade, not a second dependency registry or validation engine.

### CI — selective iteration, full promotion proof

Routine `develop` pushes use the existing path-scoped Repository / PRD / Voice workflows. `Local Promotion Verify` no longer runs the full suite after every ordinary `develop` commit.

The full suite remains mandatory for:

- `develop → Local` pull requests;
- explicit Local promotion workflow dispatch;
- changes to the promotion/browser proof harness itself;
- stable release verification.

Chrome proof is disabled in routine CI unless the gate explicitly sets `PRD_BROWSER_TEST=1`. Local promotion and stable release gates set that flag, so visual/runtime proof remains part of the integration boundary without slowing unrelated iteration.

No compatibility alias layer, second revision registry, derived-path registry, validation cache, or new CI layer was introduced.

## Verification evidence

Before changing CI frequency, the status/impact implementation candidate at commit `a3fa4603544af7300fe2befb0fbe8e9d6be555af` passed:

```text
Repository Verify
PRD Verify
full Local promotion regression suite
```

The new browser/CI boundary was then exercised at commit `16ab76176dab224b843989b416e4870e6ea68993`:

```text
PRD Verify                    PASS
Local Promotion Verify       PASS
full test_*.py regression    PASS
Chrome browser proof         forced by PRD_BROWSER_TEST=1
```

This proves both sides of the change: routine PRD CI can skip browser work, while the full integration gate still executes and passes the complete regression/browser boundary.

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

No further development step is active from this efficiency cycle. Keep the result on `develop`. Do not promote to `Local` or start runtime-template cleanup unless explicitly requested as a separate scope.
