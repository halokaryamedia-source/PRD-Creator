---
name: development-brief
description: Front door for non-trivial PRD-Creator repository/system Development. Recover current continuity, identify the first wrong owner, bound the smallest complete change, define 2–5 falsifiable acceptance criteria and the cheapest sufficient proof, then execute. Do not use for normal project Flow 2–7 production.
---

# Development Brief

Use when changing how PRD-Creator itself works: policy, skills, workflows, renderer/validator behavior, repository structure, shared tooling, or machine contracts. Normal PRD/Voice production uses the matching production skill instead.

Root `AGENTS.md` owns work mode, authority, continuity, action intent, and branch behavior. `GITHUB_RULES.md` owns GitHub mutation/verification mechanics. Do not restate those policies here.

## Development contract

Before writing, establish only:

```text
Goal / actual requirement
First wrong owner
In scope / out of scope
Acceptance criteria: 2–5
Cheapest sufficient proof
Unresolved material decision, only if one remains
```

A user-proposed implementation is evidence about the requirement, not automatically the required architecture.

## Procedure

1. **Recover actual state**
   - Follow the Development boot in root `AGENTS.md`.
   - Inspect current behavior before assuming a change is necessary.
   - If continuation conflicts with implementation, verify the exact owner and correct the stale side.
   - Do not ask the user to repeat recoverable repository/project state.

2. **Diagnose**
   - Separate semantic requirement, implementation, test, workflow, and derived-output failures.
   - Fix the first wrong owner.
   - `No change required` is valid when current behavior already satisfies the requirement.

3. **Bound**
   - Preserve valid behavior outside the affected scope.
   - Define 2–5 falsifiable acceptance criteria.
   - Use the cheapest proof that can disprove the changed claim.
   - Ask only for a material decision that cannot be responsibly recovered.

4. **Specialize only when useful**
   - PRD/source/04/handoff semantic-system change → optionally add `project-document-production`.
   - Voice semantic-system change → optionally add `voice-production`.
   - Pure technical mechanics with correct semantics → package `AGENTS.md` + exact implementation owner.
   - At most one semantic specialist. Do not load adjacent skills because they exist.

5. **Execute through completion**
   - Once reversible scope is clear, implement instead of stopping at the brief.
   - Follow only dependencies actually invalidated by the change.
   - Use `GITHUB_RULES.md` for mutation, commit, verification, failure handling, and STOP behavior.
   - Update `next-action.md` only when continuation, milestone, blocker, or next meaningful objective changes.

## User-facing form

Expose the brief only when it helps explain scope/tradeoffs:

```text
Tujuan:
Hasil yang dituju:
Tidak diubah:
Cara memastikan benar:
```

A straightforward change needs only a short progress statement. Internal planning is not another deliverable.

## Escalation

Escalate only when evidence proves the need: unresolved high-impact requirement, real cross-owner architecture decision, material evidence gap, or independent review that can change acceptance. None are default ceremony.

Stop when the requested scope is complete and evidence supports the claim.