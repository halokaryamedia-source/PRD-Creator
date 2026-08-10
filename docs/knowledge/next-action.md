# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Close **P0.1 — Executable Production Verify** from the current BuildIT parity reassessment without changing Flow 2–7 product semantics.

## Current Status

`BUILD_IT_PARITY_REASSESSMENT_P0_1_PRODUCTION_VERIFY_PENDING`

Execution channel: **ChatGPT → GitHub**.  
Working branch: **`Local` only**.

## Governing Evidence

Current comparison audit:

`docs/knowledge/reviews/buildit-current-parity-gap-audit.md`

Ordered remediation:

`docs/knowledge/operations/buildit-parity-remediation-plan.md`

The previous Phase 3 `OPERATING_PARITY_ACCEPTED` evidence remains historical proof for agent-governance/routing acceptance, but its overall full-parity conclusion is superseded by the deeper comparison against current BuildIT.

## P0.1 Implementation Boundary

This slice adds:

```text
requirements.lock.txt
kits/voice-production-kit/requirements.txt exact direct pin

tests/test_prd_contracts.py
tests/test_voice_contracts.py

.github/workflows/production-verify.yml
```

`Repository Verify` remains the static repository/routing gate. `Production Verify` is a separate executable engineering gate.

### PRD contracts

- real renderer CLI builds HTML from a minimal generic fixture using the approved template;
- real PRD validator must PASS the generated project;
- negative fixture must fail scoring/completion exclusivity;
- negative fixture must fail numeric scoring weights that do not total 100.

### Voice contracts

- real DOCX builder runs from canonical requirements + performance script;
- real Voice validator must PASS the generated project;
- second section must retain `Heading 1.page_break_before = True`, locking the real blank-page root fix;
- missing Voice ID parity must fail;
- Voice Type mismatch must fail.

### Dependency contract

Production Verify installs an exact Python 3.11 dependency lock and runs `pip check` before executable contracts.

## Proof Boundary

GitHub Actions can prove dependency installation, Python compilation, CLI execution, structural render/DOCX contracts, and focused regression behavior.

It does **not** prove:

- PRD semantic development-readiness for an arbitrary project;
- browser visual appearance;
- DOCX rendered-page visual quality;
- generated-audio quality.

Those remain Flow-specific evidence boundaries.

## Preserved Boundaries

- no new root skill in P0.1;
- no renderer/validator/builder redesign;
- no test coverage target;
- no browser or audio framework;
- no change to `main`.

## Next Step

Run and inspect the first **Production Verify** workflow on the P0.1 `Local` commit. If it passes without weakening checks, record P0.1 complete and advance only to **P0.2 — Technical Ownership Refinement**; if it fails, fix the reported root contract and rerun.
