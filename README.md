# Project Production Workspace

A repository-first production workspace for turning incomplete project direction into development-ready project documentation, then deriving validated ElevenLabs-ready Voice Production deliverables.

The repository is project memory. Chat history is supporting context, not the authority for current state.

## Branch Model

- `Local` — permanent working/development authority.
- `main` — stable baseline; change only when explicitly requested.
- routine per-task/per-flow branches and PRs are not used.

## Architecture

```text
Agent Operating Layer
Plan / Developing / Maintenance
→ development-brief for Developing
→ at most one specialist
→ owner/root-cause/proof routing

Product Production Layer
Flow 2 → Flow 3 → Flow 4 → Flow 5 → Flow 6 → Flow 7
```

Production Flow 1–7 is implemented and real-project proven on The Clockwork Vault. The old `Production Document Builder/` is retired from the live tree.

## Mandatory Session Boot

1. read `AGENTS.md`;
2. read `CONTEXT.md`;
3. read `docs/knowledge/next-action.md`;
4. open only the smallest relevant foundation/source/kit owner;
5. use ownership/skill maps only when needed.

## BuildIT Parity State

The governance/routing work from the earlier parity phases remains valid evidence, but **overall full relevant parity is reopened** after a deeper comparison against current BuildIT `Local` (`e4330f769486bcd0cee96d76fbce10f694cba2ba`).

Current audit:

`docs/knowledge/reviews/buildit-current-parity-gap-audit.md`

Ordered remediation:

`docs/knowledge/operations/buildit-parity-remediation-plan.md`

The earlier `OPERATING_PARITY_ACCEPTED` record is historical partial acceptance for the governance/routing subset, not current proof of full parity.

## Verification Layers

### Repository Verify

```text
tools/verify_repository.py
.github/workflows/repository-verify.yml
```

Static invariants: required owners, root skill containment, navigation, dependency-pin alignment, syntax, one-next-step continuity, and retired-builder containment.

### Production Verify — P0.1 COMPLETE

```text
requirements.lock.txt
.github/workflows/production-verify.yml
tests/test_prd_contracts.py
tests/test_voice_contracts.py
```

The gate executes:

- exact dependency install + `pip check`;
- Python compile;
- real PRD renderer + validator contracts;
- real Voice builder + validator contracts;
- regression for the previously fixed DOCX page-break defect;
- Voice ID/Type negative parity contracts;
- fail-closed aggregate result.

Proof on source head `0eb0485f117fa6ed419572a66539331f99114002`:

```text
Production Verify  run 31372363843  PASS
Repository Verify  run 31372363802  PASS
```

These gates do **not** replace PRD semantic review, browser visual inspection, rendered DOCX page QA, or generated-audio review.

## Current Root Skills

```text
development-brief
project-document-production
voice-production
```

The current three-skill freeze is still the implemented baseline, but P0.2 must audit whether semantic and technical failures are represented by the smallest correct owners before that architecture is treated as final.

## Repository Map

- `AGENTS.md` — repository-wide work modes, authority, proof, anti-slop baseline;
- `CONTEXT.md` — stable workspace/product state;
- `.agents/skills/` — repository-wide routing/judgment skills;
- `.github/workflows/` — repeatable static/production gates;
- `docs/foundation/` — durable production policy + validation matrix;
- `docs/knowledge/` — current state, routing, reviews, decisions, operations;
- `kits/project-document-generator/` — Flow 2–4 implementation;
- `kits/voice-production-kit/` — Flow 5–7 implementation;
- `tests/` — focused high-risk production regression contracts;
- `workspace/` — project-specific production packages.

## Core Authority Rule

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance
≠ Voice Requirements ≠ Voice Production Script ≠ DOCX
≠ Voice Acceptance ≠ Audio
```

Generated artifacts and successful tooling never silently become higher authority than the canonical work/evidence that produced them.

## Current Work

P0.1 is complete. The active next slice is **P0.2 — Technical Ownership Refinement**. See `docs/knowledge/next-action.md` for the exact boundary.
