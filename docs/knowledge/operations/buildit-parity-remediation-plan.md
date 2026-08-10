# BuildIT Parity Remediation Plan

Updated: 2026-08-10
Status: approved ordered remediation direction

Governing evidence:

`../reviews/buildit-current-parity-gap-audit.md`

This plan converts the current BuildIT comparison into bounded work. `../next-action.md` owns the single active slice.

## P0 — Production Engineering Enforcement

### P0.1 — Executable Production Verify

Goal: make high-risk production contracts fail closed in GitHub instead of relying on Python syntax/static structure only.

Required:

- exact Python dependency lock for executable Voice tooling;
- PRD renderer → generated HTML → PRD validator happy-path contract;
- PRD negative contract for scoring/completion exclusivity and scoring-weight total;
- Voice requirements → script → DOCX builder → Voice validator happy-path contract;
- regression for the real DOCX section page-break fix;
- negative Voice ID and Type parity contracts;
- fail-closed GitHub Actions aggregation.

Non-goals:

- browser visual automation;
- DOCX page rendering in GitHub Actions;
- generated audio;
- broad coverage targets;
- new production semantics.

### P0.2 — Technical Ownership Refinement

Audit whether renderer/validator/builder/tooling failures need a distinct reusable technical owner or whether current product specialists remain the smallest correct owners.

Do not add skills first. Use actual failure/caller boundaries and the KEEP/RENAME/MERGE/MOVE/DROP/RECOVER discipline.

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
