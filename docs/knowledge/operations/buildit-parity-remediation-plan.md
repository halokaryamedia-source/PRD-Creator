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
- PRD renderer → generated HTML → PRD validator happy-path contract;
- PRD negative contract for scoring/completion exclusivity and scoring-weight total;
- Voice requirements → script → DOCX builder → Voice validator happy-path contract;
- regression for the real DOCX section page-break fix;
- negative Voice ID and Type parity contracts;
- fail-closed GitHub Actions aggregation.

Proof:

```text
source head       0eb0485f117fa6ed419572a66539331f99114002
Production Verify 31372363843  PASS
Repository Verify 31372363802  PASS
```

P0.1 deliberately does not claim browser visual quality, rendered DOCX page quality, generated audio, or arbitrary-project semantic readiness.

### P0.2 — Technical Ownership Refinement — IMPLEMENTED / PROOF PENDING

Audit result:

- no new root technical specialist is justified;
- `development-brief`, `project-document-production`, and `voice-production` remain the canonical root skills;
- Project Document / Voice root specialists are narrowed to semantic/product-contract ownership;
- pure renderer/template/validator/builder mechanics route to nearest kit owners;
- shared dependency/test/CI mechanics route to repository engineering (`requirements.lock.txt`, `tests/`, `tools/`, workflows);
- pure technical Maintenance may use no root specialist.

Canonical evidence:

`../reviews/technical-ownership-refinement-audit.md`

Durable decision:

`../decisions/technical-ownership-boundary.md`

Contributor/verification rules were strengthened in both kit-local `AGENTS.md` files without adding nested skills or changing Flow 2–7 semantics.

P0.2 is complete only when the source revision passes:

```text
Repository Verify
Production Verify
```

Do not start P1 source-quality remediation before this proof is recorded.

## P1 — Production Engineering Quality Audit

After P0.2 proof, run a deep source-backed review of:

- PRD renderer/template mutation contracts;
- PRD mechanical validator gaps;
- Voice parser/builder/validator contracts;
- dependency and environment assumptions;
- deterministic/derived artifact behavior;
- failure handling and evidence boundaries.

Convert findings into an ordered plan; fix one bounded slice at a time.

P1 is an **audit first**, not permission to refactor all executable code.

## P1.5 — Module Governance

Where complexity proves it useful, strengthen module ownership with:

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
