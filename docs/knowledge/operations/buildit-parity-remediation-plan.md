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

### P0.2 — Technical Ownership Refinement — ACTIVE NEXT

Audit whether renderer/validator/builder/tooling failures need a distinct reusable technical owner or whether current product specialists remain the smallest correct owners.

Do not add skills first. Use actual failure/caller boundaries and the KEEP / RENAME / MERGE / MOVE / DROP / RECOVER discipline.

Required output:

- explicit semantic-vs-technical ownership map for current executable surfaces;
- evidence-backed decision on the current three-skill freeze;
- any justified kit-local contributor/verification-rule strengthening;
- no production redesign unless a concrete contract defect is found.

## P1 — Production Engineering Quality Audit

Run a deep source-backed review of:

- PRD renderer/template mutation contracts;
- PRD mechanical validator gaps;
- Voice parser/builder/validator contracts;
- dependency and environment assumptions;
- deterministic/derived artifact behavior;
- failure handling and evidence boundaries.

Convert findings into an ordered plan; fix one bounded slice at a time.

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
