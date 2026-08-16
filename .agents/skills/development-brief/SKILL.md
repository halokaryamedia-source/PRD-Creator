---
name: development-brief
description: Mandatory front door for non-trivial repository/system Developing in PRD-Creator. Recover stable repository context and active continuation, ground the real goal in current evidence, separate suggested method/reference from the requirement, decide whether development is needed, choose Build/Acceptance POVs, define minimal scope with 2–5 provable criteria and a proof budget, then use at most one semantic specialist. Do not use for normal Flow 2–7 project production.
---

# Development Brief

Turn a repository/system create/change request into the smallest grounded development contract **without losing cross-session context**.

Root `AGENTS.md` owns boot, work-mode, continuity, authority, evidence, and skill-budget behavior. `GITHUB_RULES.md` owns GitHub execution. Apply those owners instead of duplicating them here.

## Entry boundary

Use `development-brief` only when the user asks to change or extend **how PRD-Creator itself works**, for example policy, skills, workflow, renderer/validator/builder contract, repository structure, or shared tooling.

Normal project production is **Production Execution**, not Developing.

Examples:

```text
"Here are the project sources; create the PRD."
→ project-document-production / active Project Document owner

"Update Objective 3 using this approved project change."
→ bounded Production Execution revision

"Create Voice Production from the accepted PRD."
→ voice-production / active Voice owner

"Change how incomplete project sources are recovered before PRD creation."
→ Developing → development-brief
```

A read-only `amati / inspect / understand / recover repo context` request does not enter implementation. Recover context, report, and stop unless the user also asks to continue/change something.

## Mandatory Developing continuity

Before non-trivial Developing, recover:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules for material GitHub work
→ CONTEXT.md
→ docs/knowledge/next-action.md
→ smallest evidence/owner needed to ground this change
```

`CONTEXT.md` and `next-action.md` are mandatory here. Their purpose is to prevent a new chat from inventing repository boundaries, repeating finished work, or selecting arbitrary TODOs.

Do not ask the user to restate information recoverable from these owners/current source.

If `next-action.md` and current source materially disagree:

```text
verify exact current owner
→ identify stale continuity vs stale implementation
→ reconcile the correct owner
→ continue from actual state
```

Do not blindly repeat the stale step and do not replace it with a nearby backlog/review/TODO item.

## Required decisions

Before implementation establish only what materially affects the task:

```text
Goal
Suggested method (if any)
Observed sample/reference (if any)
Actual requirement
Input authority
Expected output
Build POV
Acceptance POV
In scope / Out of scope
Acceptance criteria: 2–5
Proof budget
Open high-impact decisions
```

Omit fields that do not apply. Execution-channel/tool mechanics follow `GITHUB_RULES.md`; record the channel only when it materially constrains proof or implementation.

## Procedure

1. **Recover context and ground the goal**
   - Use the mandatory Developing continuity above.
   - Read only the smallest additional owner/source that can change the decision.
   - Separate current fact, approved decision, assumption/proposal, derived artifact, historical evidence, and unknown.
   - Treat the user-proposed solution as a method, not automatically as the requirement.
   - Treat references/Golden material only within their recorded authority.

2. **Check whether development is necessary**
   - Inspect current behavior/owner before creating work.
   - `No change required` is valid when current behavior already satisfies the goal.
   - Old audits, backlog items, historical failures, and adjacent cleanup are not scope by default.

3. **Choose Build and Acceptance POVs**
   - **Build POV**: semantic/implementation owner responsible for making the change correctly.
   - **Acceptance POV**: downstream reader/operator/consumer that determines whether the result solves the actual need.
   - File format/tooling is an interface constraint, not automatically another owner/persona.

4. **Set minimal scope and proof**
   - Define 2–5 falsifiable acceptance criteria.
   - Choose the cheapest proof that can falsify the changed claim.
   - Ask the user only for unresolved material decisions that repository inspection cannot recover responsibly.

5. **Select implementation owner**
   - Use this skill alone when another specialist adds no semantic value.
   - PRD/source/04/handoff semantic-system changes → optionally add `project-document-production`.
   - Voice requirement/production/delivery semantic-system changes → optionally add `voice-production`.
   - Pure technical mechanics with correct semantics → nearest kit `AGENTS.md` + exact implementation owner; no semantic specialist required.
   - Add at most one semantic specialist. If a second independent problem appears, finish/reframe the first boundary before switching.

6. **Implement and final-gate**
   - Make the smallest complete change.
   - Preserve valid behavior outside scope.
   - Follow `GITHUB_RULES.md` for commit/history/tool/CI discipline.
   - Re-check goal, out-of-scope, acceptance criteria, and actual proof before `Selesai`.
   - Distinguish implemented from verified when material runtime/browser/audio proof remains unavailable.
   - Update `next-action.md` only if active continuation meaningfully changed.

## User-facing brief

For non-trivial repository Developing, a compact visible brief is enough when useful:

```text
Tujuan:
Cara berpikir:
Hasil yang dituju:
Tidak diubah:
Cara memastikan benar:
```

For a trivial unambiguous correction, one short line is enough. Normal Production Execution does not show this meta-brief.

## Escalation

Escalate only when the current task proves the need:

- unresolved high-impact requirement → focused discovery/question;
- real cross-owner architecture/migration → durable decision/change note under the existing recording threshold;
- uncertain material evidence → root evidence statuses;
- independent critique → review only when it adds real value.

None are default ceremony.
