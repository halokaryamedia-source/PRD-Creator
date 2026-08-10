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

The governance/routing work from the earlier parity phases remains valid evidence, but **overall full relevant parity remains open** after a deeper comparison against current BuildIT `Local` (`e4330f769486bcd0cee96d76fbce10f694cba2ba`).

Current broad audit:

`docs/knowledge/reviews/buildit-current-parity-gap-audit.md`

Top-level remediation:

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

Proof:

```text
P0.1 source head  0eb0485f117fa6ed419572a66539331f99114002
Production Verify 31372363843  PASS
Repository Verify 31372363802  PASS

P0.2 source head  a0a51d97523ab07f87ef6deeffdafc8094febea4
Production Verify 31374226078  PASS
Repository Verify 31374226049  PASS
```

These gates do **not** replace PRD semantic review, browser visual inspection, rendered DOCX page QA, or generated-audio review.

## Current Root Skills — P0.2 Re-Audited

```text
development-brief
project-document-production
voice-production
```

P0.2 kept the three-skill set but narrowed the two production specialists to semantic/product-contract ownership.

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

A candidate Python / production-tooling / artifact-engineering root skill was rejected from current evidence.

Canonical decision:

`docs/knowledge/decisions/technical-ownership-boundary.md`

## P1 Production Engineering Quality Audit

P1 performed a source-backed audit of the renderer/template/validators, Voice parser/builder/validator, dependency environment, and focused contract gate.

Canonical audit:

`docs/knowledge/reviews/production-engineering-quality-audit.md`

Ordered source remediation:

`docs/knowledge/operations/production-engineering-remediation-plan.md`

The audit found high-priority generic trust gaps in PRD current-render revision identity, malformed render-data fail-closed behavior, glossary script-context safety, Voice revision identity, and DOCX per-entry binding. These findings limit generalization to future project revisions; they do not rewrite the historical Clockwork Vault evidence.

## Kit-Local Contributor Contracts

Both nearest `AGENTS.md` files act as contributor/verification contracts:

- Project Document Generator — exact renderer/template/validator ownership, contributor rules, and verification commands;
- Voice Production Kit — exact builder/validator ownership, dependency contract, contributor rules, and verification commands.

## Repository Map

- `AGENTS.md` — repository-wide work modes, authority, proof, semantic-vs-technical routing, anti-slop baseline;
- `CONTEXT.md` — stable workspace/product state;
- `.agents/skills/` — repository-wide semantic routing/judgment skills;
- `.github/workflows/` — repeatable static/production gates;
- `requirements.lock.txt`, `tests/`, `tools/` — shared repository engineering contracts;
- `docs/foundation/` — durable production policy + validation matrix;
- `docs/knowledge/` — current state, routing, reviews, decisions, operations;
- `kits/project-document-generator/` — Flow 2–4 implementation + module-local mechanics;
- `kits/voice-production-kit/` — Flow 5–7 implementation + module-local mechanics;
- `workspace/` — project-specific production packages.

## Core Authority Rule

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance
≠ Voice Requirements ≠ Voice Production Script ≠ DOCX
≠ Voice Acceptance ≠ Audio
```

Generated artifacts and successful tooling never silently become higher authority than the canonical work/evidence that produced them.

## Current Work

P0.1 and P0.2 are complete. P1 audit is complete. The active next source slice is **P1.1 — PRD Mechanical Revision Integrity**. See `docs/knowledge/next-action.md` for the exact implementation/acceptance boundary.
