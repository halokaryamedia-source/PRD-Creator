# BuildIT Parity Remediation Plan

Updated: 2026-08-10
Status: approved ordered remediation direction

Governing evidence:

`../reviews/buildit-current-parity-gap-audit.md`

This plan converts the current BuildIT comparison into bounded work. `../next-action.md` owns the single active slice.

## P0 — Production Engineering Enforcement

### P0.1 — Executable Production Verify — COMPLETE

Implemented:

- exact Python dependency lock for executable Voice tooling;
- PRD renderer → generated HTML → PRD validator focused contracts;
- PRD negative scoring/completion contracts;
- Voice requirements → script → DOCX builder → Voice validator focused contracts;
- real DOCX page-break regression;
- negative Voice ID and Type parity contracts;
- fail-closed GitHub Actions aggregation.

Proof:

```text
source head       0eb0485f117fa6ed419572a66539331f99114002
Production Verify 31372363843  PASS
Repository Verify 31372363802  PASS
```

### P0.2 — Technical Ownership Refinement — COMPLETE

Source/governance head:

`a0a51d97523ab07f87ef6deeffdafc8094febea4`

Result:

- no new root technical specialist is justified;
- three canonical root skills remain;
- semantic/product-contract failures route to matching root specialist;
- pure renderer/template/validator/builder mechanics route to nearest kit owner;
- shared dependency/test/CI mechanics route to repository engineering;
- both kit-local `AGENTS.md` files define contributor/verification contracts.

Evidence:

`../reviews/technical-ownership-refinement-audit.md`

Decision:

`../decisions/technical-ownership-boundary.md`

Proof:

```text
Repository Verify 31374226049  PASS
Production Verify 31374226078  PASS
```

## P1 — Production Engineering Quality — AUDIT COMPLETE / REMEDIATION ACTIVE

Canonical audit:

`../reviews/production-engineering-quality-audit.md`

Ordered source-remediation plan:

`production-engineering-remediation-plan.md`

The audit found material remaining gaps in:

- PRD render revision/freshness identity;
- PRD validator malformed-input fail-closed behavior;
- glossary JavaScript-context safety;
- PRD shell/metadata mechanical integrity;
- Voice requirements/script/DOCX revision identity;
- DOCX per-entry binding validation;
- Voice empty-section controlled failure;
- contract-test discovery;
- conditional derived-output atomicity.

### P1.1 — PRD Mechanical Revision Integrity — ACTIVE NEXT

Fix only the first dependency slice:

- structured fail-closed preflight for malformed render-data;
- deterministic current render-data → final HTML revision/fingerprint evidence;
- stale current HTML must fail;
- stale extra generated sections/pages must fail;
- focused regressions.

Do not automate semantic canonical-content judgement or browser visual approval.

Later P1 slices are ordered in `production-engineering-remediation-plan.md`; do not skip ahead merely because another fix is easier.

## P1.5 — Module Governance

After required P1 source findings are repaired/re-audited, strengthen module ownership only where complexity proves it useful:

- purpose/boundary/inputs/outputs/dependencies/risks;
- exact development and verification commands;
- canonical/generated artifact rules;
- module-local proof boundaries.

Do not create per-directory governance files by default.

## P2 — Knowledge / Operations Maturity

Evaluate and add only useful equivalents of:

- operations index;
- broad roadmap;
- meaningful change log;
- trigger-based documentation audit;
- repository-wide glossary;
- optional Obsidian vault ergonomics.

## P3 — Conditional Helper Routing

Make conditional diagnosis/testing/review/research/design/skill-authoring escalation explicit without copying global helpers into the repository.

## Acceptance Principle

The target is **relevant operating parity**, not tree similarity.

A BuildIT mechanism is adopted only when it protects a real PRD-Creator boundary. Domain-specific MCP/Blockbench structure is not copied.
