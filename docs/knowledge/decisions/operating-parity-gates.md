# Operating Parity Acceptance Decisions

Updated: 2026-08-10
Status: active durable decision

## Context

Phase 3 exercised the BuildIT-style operating architecture added in Phase 1–2. The acceptance run found one real routing defect: Project Document Generator's kit `SKILL.md` forced broad reading across Flow 2–4 even when only one Flow was active.

The repository also now depends on stable structural invariants: a frozen root skill set, canonical ownership/source routes, one active next step, executable Python production tools, and permanent retirement of the old builder tree.

## Decision 1 — Project Document Generator gets nearest `AGENTS.md`

Add `kits/project-document-generator/AGENTS.md` and make the kit `SKILL.md` Flow-first.

Why:

- Flow 2, 3, and 4 have materially different read/owner boundaries;
- renderer/template/validator work benefits from scoped root-cause rules;
- nearest rules reduce context load even when a root specialist is not loaded;
- this fixes an observed routing inconsistency rather than adding symmetry for its own sake.

Voice Production's existing local `AGENTS.md` remains sufficient. Do not add nearest agent files to every directory by default.

## Decision 2 — Add one small repository verification gate

Adopt:

```text
tools/verify_repository.py
.github/workflows/repository-verify.yml
```

The gate fails closed on stable repository contracts only:

- required operating owners;
- exact canonical root skill set;
- duplicate nested skill roots;
- retired-builder return;
- `next-action.md` one-next-step structure;
- broken relative Markdown navigation;
- Python syntax in production kits.

## Why This Gate Is Justified

This is not copied because BuildIT has CI. It is justified because:

1. Phase 3 found actual routing drift after architecture changes;
2. continuity now depends on several linked owner documents;
3. root skill inventory is explicitly frozen;
4. production uses executable Python code;
5. these checks are cheap, deterministic, and meaningful on every commit.

## Tradeoffs / Boundaries

Repository Verify is deliberately **not** a universal quality gate.

It does not prove:

- project requirement quality;
- PRD semantic readiness;
- rendered HTML visual quality;
- DOCX visual quality;
- generated-audio quality.

Those remain owned by Flow-specific validators and actual visual/audio evidence.

Do not expand this workflow into a large test/packaging framework unless a future real failure demonstrates a missing repeatable invariant.

## Evidence / Validation Boundary

Phase 3 routing scenarios and the Maintenance finding are recorded in:

`docs/knowledge/operations/operating-parity-acceptance.md`

Final operating-parity acceptance additionally requires the first `Repository Verify` run on `Local` to pass.

## Follow-up

After the first successful workflow run, update the current acceptance/status owners and return the repository to normal project operation. Future operating changes are evidence-driven Maintenance, not another parity phase by default.
