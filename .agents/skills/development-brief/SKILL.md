---
name: development-brief
description: Mandatory front door for non-trivial repository/system Development in PRD-Creator. Recover current repository continuity, identify the actual requirement and first wrong owner, define the smallest scope with 2–5 falsifiable acceptance criteria and a proof budget, then execute with at most one useful semantic specialist. Do not use for normal Flow 2–7 project production.
---

# Development Brief

Turn a repository/system create/change request into the **smallest grounded development contract**, then continue into implementation when the requested reversible scope is clear.

Root `AGENTS.md` owns work mode, continuity, authority, action intent, evidence, and skill budget. `GITHUB_RULES.md` owns GitHub execution. Do not duplicate those policies here.

## Entry boundary

Use `development-brief` when the user asks to change **how PRD-Creator itself works**, for example policy, skills, workflow, renderer/validator/builder behavior, repository structure, or shared tooling.

Normal project production remains Production Execution.

```text
create/revise a project PRD
→ project-document-production / active production owner

create/revise accepted Voice production
→ voice-production / active Voice owner

change how PRD-Creator recovers, represents, validates, renders, or routes work
→ Development → development-brief
```

A read-only inspect/understand/recover request is Plan behavior. Report current state and stop unless the user also asked for a change.

## Mandatory Development continuity

Before non-trivial Development, recover:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules when GitHub work is material
→ CONTEXT.md
→ docs/knowledge/next-action.md
→ smallest current owner/evidence that can change the decision
```

`CONTEXT.md` and `next-action.md` prevent a new session from inventing repository boundaries, repeating completed work, or promoting an old audit/TODO into current scope.

Do not ask the user to restate information recoverable from current repository/source state.

If continuation and implementation disagree:

```text
verify current owner
→ identify stale continuity vs stale implementation
→ reconcile the stale owner
→ continue from actual state
```

## Minimal development contract

Before writing, establish only what is needed to execute safely and verify the result:

```text
Goal / actual requirement
First wrong owner
In scope / out of scope
Acceptance criteria: 2–5
Proof budget
Unresolved material decision, only when one really remains
```

Treat a user-proposed method, reference, sample, or implementation idea as input to the requirement—not automatically as the requirement itself.

Build/Acceptance POVs are optional reasoning aids. Use them only when distinguishing the implementation owner from the actual downstream consumer changes the decision. Do not create personas or formal POV fields for routine work.

Execution-channel mechanics stay in `GITHUB_RULES.md` and do not need to be restated in the brief.

## Procedure

1. **Recover and diagnose**
   - Use the mandatory continuity above.
   - Inspect current behavior before assuming development is needed.
   - Separate current authority from historical evidence, proposals, and derived output.
   - Identify the first semantic/implementation/test/workflow owner that is actually wrong.
   - `No change required` remains a valid result.

2. **Bound the change**
   - Define 2–5 falsifiable acceptance criteria.
   - Preserve valid behavior outside the affected boundary.
   - Choose the cheapest proof that can falsify the changed claim.
   - Ask the user only for a material decision that cannot be responsibly recovered or proposed under existing authority.

3. **Select only useful specialization**
   - Use this skill alone when another specialist adds no semantic value.
   - PRD/source/04/handoff semantic-system change → optionally add `project-document-production`.
   - Voice requirement/production/delivery semantic-system change → optionally add `voice-production`.
   - Pure technical mechanics with correct semantics → nearest kit `AGENTS.md` + exact implementation owner; no semantic specialist required.
   - Use at most one semantic specialist. Do not load adjacent specialists because they exist.

4. **Execute through completion**
   - Once the goal and reversible scope are clear, do not stop at the brief or ask for permission to begin.
   - Make the smallest complete change at the first wrong owner.
   - Follow only dependencies actually invalidated by that change.
   - Apply `GITHUB_RULES.md` for transfer, commit, verification, failure handling, and STOP behavior.

5. **Final gate**
   - Re-check the goal, scope boundary, acceptance criteria, and actual proof.
   - Distinguish implemented from verified when browser/audio/runtime evidence is unavailable.
   - Update `next-action.md` only when the active continuation, blocker, milestone, or next meaningful objective actually changed.

## User-facing brief

Expose a Development brief only when it materially helps the user understand scope or tradeoffs. A compact form is enough:

```text
Tujuan:
Hasil yang dituju:
Tidak diubah:
Cara memastikan benar:
```

For a straightforward change, one short progress statement is sufficient. Do not turn internal development planning into another deliverable.

## Escalation

Escalate only when current evidence proves the need:

- unresolved high-impact requirement → one focused question;
- real cross-owner architecture/migration → durable decision note when the repository recording threshold is met;
- uncertain material evidence → root evidence statuses;
- independent critique → review only when it can materially change acceptance.

None are default ceremony.
