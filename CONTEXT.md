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

Canonical repository-wide skills currently remain:

- `development-brief`;
- `project-document-production`;
- `voice-production`.

The governance/routing subset—boot, Plan/Developing/Maintenance, development brief, Dual POV, one-specialist budget, root-cause Maintenance, ownership/review lifecycle—has real acceptance evidence.

The current three-skill freeze is an implemented baseline, **not a final answer**. P0.2 will audit semantic vs technical ownership before any skill architecture change.

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

Proof on source head `0eb0485f117fa6ed419572a66539331f99114002`:

- Production Verify `31372363843` — PASS;
- Repository Verify `31372363802` — PASS.

Production Verify executes the real PRD renderer/validator and Voice DOCX builder/validator on minimal generic fixtures, including negative high-risk contracts and the prior DOCX page-break regression.

These gates do not replace semantic, browser, rendered-page, or audio evidence.

## Stable Authority Chain

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance
≠ Voice Requirements ≠ Voice Production Script ≠ DOCX
≠ Voice Acceptance ≠ Audio
```

## Stable Structure

- `.agents/skills/` — repository-wide agent routing/judgment skills;
- `.github/workflows/` — repeatable repository/production gates;
- `docs/foundation/` — durable production policy + proof matrix;
- `docs/knowledge/` — continuity, routing, ownership, reviews, decisions, operations;
- `kits/project-document-generator/` — active PRD Flow 2–4 owner;
- `kits/voice-production-kit/` — active Voice Flow 5–7 owner;
- `tests/` — focused high-risk production contract regressions;
- `workspace/active/` / `workspace/saved/` — project-specific packages.

## Current Development State

P0.1 is complete. The next active remediation slice is **P0.2 — Technical Ownership Refinement**: audit actual semantic vs technical failure ownership before changing the current root skill freeze or broadening module governance.
