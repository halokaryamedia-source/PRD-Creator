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

### P0.2 — Technical Ownership Refinement — COMPLETE

Source/governance head:

`a0a51d97523ab07f87ef6deeffdafc8094febea4`

Result:

- no new root technical specialist is justified;
- `development-brief`, `project-document-production`, and `voice-production` remain the canonical root skills;
- Project Document / Voice root specialists are narrowed to semantic/product-contract ownership;
- pure renderer/template/validator/builder mechanics route to nearest kit owners;
- shared dependency/test/CI mechanics route to repository engineering (`requirements.lock.txt`, `tests/`, `tools/`, workflows);
- pure technical Maintenance may use no root specialist;
- both kit-local `AGENTS.md` files now define contributor/verification contracts.

Canonical evidence:

`../reviews/technical-ownership-refinement-audit.md`

Durable decision:

`../decisions/technical-ownership-boundary.md`

Proof:

```text
Repository Verify 31374226049  PASS
Production Verify 31374226078  PASS
```

Production Verify sub-gates passed for locked dependencies, compile, PRD contracts, Voice contracts, and fail-closed aggregation.

## P1 — Production Engineering Quality Audit — ACTIVE NEXT

Run a deep source-backed review of:

- PRD renderer/template mutation contracts;
- PRD mechanical validator gaps;
- Voice parser/builder/validator contracts;
- dependency and environment assumptions;
- deterministic/derived artifact behavior;
- failure handling and evidence boundaries;
- focused test adequacy for real public/high-risk contracts.

P1 is an **audit first**, not permission to refactor all executable code.

Required output:

- source-backed findings with severity, owner, and evidence;
- explicit `No change required` where appropriate;
- ordered remediation slices only for justified findings;
- no broad framework/test-coverage project.

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
