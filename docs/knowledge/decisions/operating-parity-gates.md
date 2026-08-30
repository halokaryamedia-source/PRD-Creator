# Operating Parity Acceptance Decisions

Updated: 2026-08-10  
Current status: **historical/refined by the current unified repository architecture**.

This file preserves the Phase 1–3 acceptance rationale. Some captured package names and paths below were later retired. Current execution uses `../ownership.md`, `../next-action.md`, root `AGENTS.md`, and current `kits/prd-creator/` owners.

The durable principle that remains current is narrow: keep one small repository verification gate for stable, repeatable repository invariants. Do not restore retired package paths merely because they appear in this captured decision.

## Captured Context

Phase 3 exercised the BuildIT-style operating architecture added in Phase 1–2. The acceptance run found one real routing defect: Project Document Generator's kit `SKILL.md` forced broad reading across Flow 2–4 even when only one Flow was active.

The repository also depended on stable structural invariants: a frozen root skill set, canonical ownership/source routes, one active next step, executable Python production tools, and permanent retirement of the old builder tree.

## Captured Decision 1 — nearest package routing

At capture time, the decision was to keep `kits/project-document-generator/AGENTS.md` and a Flow-first kit `SKILL.md` so Flow 2, 3, and 4 could route to smaller owners.

That exact package path is now retired. Its durable intent survives in the current unified `kits/prd-creator/AGENTS.md` + categorized owners: nearest routing should reduce context and should not create agent files everywhere for symmetry.

## Decision 2 — Keep one small repository verification gate

Current canonical gate:

```text
tools/verify_repository.py
.github/workflows/repository-verify.yml
```

The gate should fail closed only on stable repository contracts that are cheap, deterministic, and repeatable, such as:

- required operating owners and current package shape;
- exact canonical root skill set;
- duplicate/retired architecture returning;
- current continuation structure;
- broken relative Markdown navigation;
- Python syntax in repository-owned code.

Domain-specific executable behavior remains with PRD/Voice regression suites rather than being duplicated into Repository Verify.

## Why This Gate Is Justified

The gate exists because real routing drift occurred and repository continuity depends on linked owners and executable Python. It is not a universal quality gate and must not grow merely to imitate another repository.

It does not prove:

- project requirement quality;
- PRD semantic readiness;
- rendered HTML visual quality;
- generated-audio quality;
- runtime behavior outside the code/tests it actually executes.

Those remain with their matching production validators and actual evidence channels.

## Historical Execution Proof

The first Repository Verify GitHub Actions execution passed at capture time:

- Commit: `5970c47c15c8e9e83df185be7c5472e976739062`
- Run ID: `31367001967`
- Conclusion: `success`

This remains provenance only; current workflow health is established by current runs, not this old proof.

## Current Boundary

Return to normal project/repository operation after the relevant invariant is protected. Future operating changes are Plan / Developing / Maintenance work and are added only when current evidence proves a missing repeatable capability.
