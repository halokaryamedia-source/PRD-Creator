# Project Production Workspace

A repository-first production workspace for turning incomplete project direction into development-ready project documentation, then deriving validated ElevenLabs-ready Voice Production deliverables.

The repository is project memory. Chat history is supporting context, not the authority for current state.

## Branch Model

- `Local` — permanent working/development authority.
- `main` — stable baseline; change only when explicitly requested.
- routine per-task/per-flow branches and PRs are not used.

## Two Architecture Layers

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

## Current Agent Governance

Canonical root skills:

```text
development-brief
project-document-production
voice-production
```

The previous Phase 1–3 work genuinely established and exercised repository boot, Plan/Developing/Maintenance routing, mandatory development brief, Dual POV, one-specialist budget, root-cause Maintenance, ownership/review lifecycle, and static Repository Verify.

## Current BuildIT Parity Status

**Overall full parity is reopened.**

A deeper audit against current BuildIT `Local` (`e4330f769486bcd0cee96d76fbce10f694cba2ba`) found relevant mechanisms still missing or weaker in PRD-Creator, especially executable engineering enforcement, technical ownership depth, module-local governance, and operations maturity.

Current audit:

`docs/knowledge/reviews/buildit-current-parity-gap-audit.md`

Ordered remediation:

`docs/knowledge/operations/buildit-parity-remediation-plan.md`

The earlier `OPERATING_PARITY_ACCEPTED` record remains historical **partial acceptance** for the governance/routing subset; it is no longer the current overall status.

## Verification Layers

### Repository Verify

```text
tools/verify_repository.py
.github/workflows/repository-verify.yml
```

Static invariants only: required owners, root skill containment, navigation, dependency-pin alignment, syntax, one-next-step continuity, and retired-builder containment.

### Production Verify — P0.1

```text
requirements.lock.txt
.github/workflows/production-verify.yml
tests/test_prd_contracts.py
tests/test_voice_contracts.py
```

Executable contracts:

- exact dependency install + `pip check`;
- Python compile;
- real PRD renderer + validator happy path;
- PRD scoring/completion + scoring-weight negative contracts;
- real Voice builder + validator happy path;
- DOCX section page-break regression for the previously fixed blank-page defect;
- Voice ID and Type parity negative contracts;
- fail-closed aggregate result.

These gates do **not** replace PRD semantic review, browser visual inspection, rendered DOCX page QA, or generated-audio review.

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

P0.1 — Executable Production Verify is active. Check `docs/knowledge/next-action.md` for the single current slice and proof state.
