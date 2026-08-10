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

Production Flow 1–7 is implemented and real-project proven on The Clockwork Vault. The retired `Production Document Builder/` is not a live owner.

## Mandatory Session Boot

1. read `AGENTS.md`;
2. read `CONTEXT.md`;
3. read `docs/knowledge/next-action.md`;
4. open only the smallest relevant foundation/source/kit owner;
5. use ownership/skill maps only when needed.

## BuildIT Parity State

Overall full relevant parity remains open. Current governing evidence:

```text
docs/knowledge/reviews/buildit-current-parity-gap-audit.md
docs/knowledge/reviews/production-engineering-quality-audit.md
docs/knowledge/operations/production-engineering-remediation-plan.md
```

The earlier `OPERATING_PARITY_ACCEPTED` record remains historical partial acceptance for the governance/routing subset only.

## Verification Layers

### Repository Verify

Static repository/routing/navigation/dependency-pin/syntax invariants.

### Production Verify

Exact dependency install + Python compile + focused executable PRD and Voice production contracts + fail-closed aggregation.

Neither gate replaces semantic review, browser visual inspection, rendered DOCX page QA, pronunciation/performance judgement, or actual audio review.

## Current Root Skills

```text
development-brief
project-document-production
voice-production
```

P0.2 keeps these as semantic/product-contract owners. Pure renderer/validator/builder mechanics route to nearest kit owners; shared dependency/test/CI mechanics route to repository engineering.

## P1.1 — PRD Mechanical Revision Integrity — COMPLETE

Source head:

`04f306f8589528ccc8cb03e89333dba174a3d276`

Implemented:

```text
render-data.json
→ canonical sorted JSON
→ SHA-256 render identity
→ final.html render-data-sha256 marker
→ Flow 4 validator exact match
```

The validator also fails structurally before page calculation for malformed root collection items and requires the generated document section list to match the current expected page order/set exactly.

Proof:

```text
Production Verify 31377375929  PASS
Repository Verify 31377377036  PASS
```

This closes P1-F01 and P1-F02 at the mechanical level claimed without pretending to prove semantic or visual correctness.

## Repository Map

- `AGENTS.md` — repository-wide work modes, authority, proof, anti-slop baseline;
- `CONTEXT.md` — stable workspace/product state;
- `.agents/skills/` — repository-wide semantic routing/judgment skills;
- `.github/workflows/` — repeatable static/production gates;
- `requirements.lock.txt`, `tests/`, `tools/` — shared repository engineering contracts;
- `docs/foundation/` — durable production policy + validation matrix;
- `docs/knowledge/` — current state, routing, reviews, decisions, operations;
- `kits/project-document-generator/` — Flow 2–4 implementation + module-local mechanics;
- `kits/voice-production-kit/` — Flow 5–7 implementation + module-local mechanics;
- `workspace/` — project-specific production packages.

## Current Work

P1.1 is complete. The active next source slice is **P1.2 — PRD Renderer Script/Shell Safety**. See `docs/knowledge/next-action.md` for the exact boundary.
