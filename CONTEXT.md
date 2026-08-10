# Workspace Context

Last verified: 2026-08-10
Stability: stable production system; parity remediation active
Owner: workspace

## Purpose

This repository supports a two-stage production system:

1. turn incomplete/uneven project direction into documentation developers, level designers, and production teams can use;
2. derive validated ElevenLabs-ready Voice Production from accepted project documentation without inventing upstream design.

The production pipeline and agent operating layer remain separate:

```text
Agent Operating Layer
Plan / Developing / Maintenance
→ owner + proof boundary

Production Layer
Flow 2 → Flow 3 → Flow 4 → Flow 5 → Flow 6 → Flow 7
```

## Stable Production State

Production Flow 1–7 is implemented. The Clockwork Vault completed real Flow 2→7 integration proof, including a real DOCX blank-page defect discovered by visual QA, fixed at the builder root, rebuilt, and revalidated.

`Production Document Builder/` v0.2.0 remains retired from the live `Local` tree. Git history is the recovery path for old implementation details.

## Agent Governance Layer

Canonical repository-wide skills remain under `.agents/skills/`:

- `development-brief` — mandatory front door for non-trivial Developing work;
- `project-document-production` — current Flow 2–4 semantic specialist;
- `voice-production` — current Flow 5–7 semantic specialist.

Current routing/continuity owners:

- `docs/knowledge/flow.md`;
- `docs/knowledge/skills/activation-matrix.md`;
- `docs/knowledge/skills/skill-map.md`;
- `docs/knowledge/modules/module-map.md`;
- `docs/knowledge/sources/source-map.md`;
- `docs/knowledge/maintenance/maintenance-flow.md`;
- `docs/knowledge/reviews/review-graph.md`;
- `docs/knowledge/next-action.md`.

The current three-skill freeze remains the implemented baseline, but P0.2 will audit whether semantic and technical failure ownership is still correctly represented. Do not add a skill before that evidence-driven audit.

## BuildIT Parity Reassessment

The previous Phase 3 operating acceptance remains valid for the **agent-governance/routing subset**: boot, mode routing, development brief, one-specialist budget, Maintenance route, ownership/review lifecycle, and static Repository Verify were actually exercised.

A deeper comparison against current BuildIT `Local` (`e4330f769486bcd0cee96d76fbce10f694cba2ba`) found additional relevant gaps. Therefore overall full parity is reopened.

Canonical audit:

`docs/knowledge/reviews/buildit-current-parity-gap-audit.md`

Ordered remediation:

`docs/knowledge/operations/buildit-parity-remediation-plan.md`

## Engineering Gates

### Repository Verify

```text
tools/verify_repository.py
→ .github/workflows/repository-verify.yml
```

Owns static repository invariants: required owners, skill-root containment, navigation, exact dependency-pin alignment, syntax, next-action structure, and retired-builder containment.

### Production Verify

P0.1 adds:

```text
requirements.lock.txt
→ exact dependency install
→ compile
→ tests/test_prd_contracts.py
→ tests/test_voice_contracts.py
→ .github/workflows/production-verify.yml
```

This gate executes the real PRD renderer/validator and Voice builder/validator paths on minimal generic fixtures. It does not replace semantic, browser, rendered-page, or audio evidence.

## Stable Authority Chain

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance
≠ Voice Requirements ≠ Voice Production Script ≠ DOCX
≠ Voice Acceptance ≠ Audio
```

A successful tool/artifact never silently becomes higher authority than the canonical work/evidence that produced it.

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

P0.1 — Executable Production Verify is the active BuildIT-parity remediation slice. Its implementation is prepared, but it is not complete until the GitHub Actions Production Verify run passes without weakening checks.
