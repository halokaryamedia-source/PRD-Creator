# Workspace Context

Last verified: 2026-08-10
Stability: stable production system; BuildIT parity remediation active
Owner: workspace

## Purpose

This repository supports a two-stage production system:

1. turn incomplete/uneven project direction into documentation developers, level designers, and production teams can use;
2. derive validated ElevenLabs-ready Voice Production from accepted project documentation without inventing upstream design.

Production and agent-operation layers remain separate:

```text
Agent Operating Layer
Plan / Developing / Maintenance
→ owner + proof boundary

Production Layer
Flow 2 → Flow 3 → Flow 4 → Flow 5 → Flow 6 → Flow 7
```

## Stable Production State

Production Flow 1–7 is implemented. The Clockwork Vault completed real Flow 2→7 integration proof, including a real DOCX blank-page defect discovered by visual QA, fixed at the builder root, rebuilt, and revalidated.

`Production Document Builder/` v0.2.0 remains retired from the live `Local` tree.

## Agent Governance Layer

Canonical repository-wide skills remain:

- `development-brief`;
- `project-document-production`;
- `voice-production`.

P0.2 re-audited the three-skill baseline after executable production verification and kept it, while narrowing the production specialists to **semantic/product-contract ownership**.

Current routing:

```text
semantic/product contract wrong
→ matching root semantic specialist

semantic contract correct
+ renderer/validator/builder mechanics wrong
→ nearest kit AGENTS + exact implementation owner
→ no root specialist required by default

shared dependency/test/CI contract wrong
→ requirements.lock.txt / tests / tools / workflows
```

This avoids creating a Python/tooling/artifact specialist merely because executable files share an implementation language.

Canonical P0.2 decision:

`docs/knowledge/decisions/technical-ownership-boundary.md`

## BuildIT Parity Reassessment

A deeper comparison against current BuildIT `Local` (`e4330f769486bcd0cee96d76fbce10f694cba2ba`) reopened overall full parity.

Canonical audit:

`docs/knowledge/reviews/buildit-current-parity-gap-audit.md`

Ordered remediation:

`docs/knowledge/operations/buildit-parity-remediation-plan.md`

The previous Phase 3 acceptance remains historical partial evidence for the governance/routing subset.

## Engineering Gates

### Repository Verify

```text
tools/verify_repository.py
→ .github/workflows/repository-verify.yml
```

Owns static repository invariants: required owners, skill-root containment, navigation, exact dependency-pin alignment, syntax, next-action structure, and retired-builder containment.

### Production Verify — P0.1 COMPLETE

```text
requirements.lock.txt
→ exact dependency install
→ compile
→ tests/test_prd_contracts.py
→ tests/test_voice_contracts.py
→ .github/workflows/production-verify.yml
```

P0.1 proof:

```text
source head       0eb0485f117fa6ed419572a66539331f99114002
Production Verify 31372363843  PASS
Repository Verify 31372363802  PASS
```

P0.2 routing/governance proof:

```text
source head       a0a51d97523ab07f87ef6deeffdafc8094febea4
Production Verify 31374226078  PASS
Repository Verify 31374226049  PASS
```

Production Verify executes the real PRD renderer/validator and Voice DOCX builder/validator on minimal generic fixtures. These gates do not replace semantic, browser, rendered-page, or audio evidence.

## P1 Production Engineering Audit

The P1 audit is complete and recorded in:

`docs/knowledge/reviews/production-engineering-quality-audit.md`

It found material generic trust gaps that do not invalidate the specific Clockwork Vault proof, but must be fixed before the executable engine can generalize the same confidence to future revisions. Highest-priority findings include PRD stale-artifact revision identity, validator malformed-input failure handling, glossary script-context safety, Voice revision identity, and DOCX per-entry binding validation.

Ordered source remediation:

`docs/knowledge/operations/production-engineering-remediation-plan.md`

## Kit-Local Technical Governance

Both executable kits use nearest `AGENTS.md` as contributor/verification contracts:

- Project Document kit: module structure, renderer/template/validator technical ownership, exact commands, canonical-vs-derived rules;
- Voice kit: module structure, builder/validator technical ownership, exact dependency/verification commands, canonical-script-vs-derived-DOCX rules.

## Stable Authority Chain

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance
≠ Voice Requirements ≠ Voice Production Script ≠ DOCX
≠ Voice Acceptance ≠ Audio
```

## Stable Structure

- `.agents/skills/` — repository-wide semantic routing/judgment skills;
- `.github/workflows/` — repeatable repository/production gates;
- `requirements.lock.txt` + `tests/` + `tools/` — repository engineering contracts;
- `docs/foundation/` — durable production policy + proof matrix;
- `docs/knowledge/` — continuity, routing, ownership, reviews, decisions, operations;
- `kits/project-document-generator/` — active PRD Flow 2–4 owner + module-local mechanics;
- `kits/voice-production-kit/` — active Voice Flow 5–7 owner + module-local mechanics;
- `workspace/active/` / `workspace/saved/` — project-specific packages.

## Current Development State

P0.1 and P0.2 are complete. The P1 Production Engineering Quality Audit is complete. The active source-remediation slice is **P1.1 — PRD Mechanical Revision Integrity**: make malformed render-data fail in a structured way and prove that `output/final.html` belongs to the current `work/render-data.json` revision before mechanical PASS.
