---
name: development-brief
description: Mandatory front door for non-trivial PRD-Creator Developing tasks. Ground the real goal in repository/project evidence, separate suggested method and sample/reference from the requirement, detect execution channel, decide whether development is needed, choose Build and Acceptance POVs, define minimal scope with 2–5 provable criteria and a proof budget, then hand off to at most one semantic specialist. Re-check the same contract before completion. Do not use as the production procedure for Flow 2–7.
---

# Development Brief

Turn a create/change request into the smallest grounded development contract.

Root `AGENTS.md` owns source precedence, independent judgment, root-cause gating, proof economy, evidence status, and anti-slop behavior. Apply those rules instead of duplicating them here.

## Required Decisions

Before implementation establish only what materially affects the task:

```text
Goal:
Suggested method (if any):
Observed sample/reference (if any):
Generic requirement:
Execution channel:
Input authority:
Expected output:
Build POV:
Acceptance POV:
Interface constraints:
In scope / Out of scope:
Acceptance criteria: 2–5
Proof budget:
Open high-impact decisions:
```

Omit fields that do not apply.

## Procedure

1. **Ground the goal**
   - Read `CONTEXT.md`, `docs/knowledge/next-action.md`, and only the relevant policy/source.
   - Separate fact, approved decision, assumption, generated artifact, and unknown.
   - Treat the user-proposed solution as a method, not automatically as the requirement.
   - Treat Golden Samples/reference documents as demonstrated evidence unless object/project-specific behavior is explicitly requested.

2. **Detect execution channel**
   - `ChatGPT → GitHub`: repository preparation/static artifact proof only.
   - `Local / Codex-style`: targeted local render/build/runtime/audio/browser proof may be available; verify availability first.
   - Goal, scope, authority, Acceptance POV, and criteria remain the same across channels.

3. **Check whether development is necessary**
   - Inspect the existing owner/pattern before creating work.
   - `No change required` is valid when current behavior already satisfies the goal.

4. **Choose the two POVs**
   - **Build POV**: the semantic owner responsible for making the change correctly.
   - **Acceptance POV**: the downstream reader/operator/consumer who determines whether the result is useful.
   - Keep renderer, validator, builder, file format, and other tooling as interface constraints rather than extra personas unless they are the actual failure owner.

5. **Set minimal scope and proof**
   - Define 2–5 acceptance criteria that can actually be disproved/proved.
   - Use root minimum-useful-proof and evidence-status rules.
   - Ask the user only for unresolved high-impact decisions that repository inspection cannot recover safely.

6. **Select implementation owner**
   - Use this skill alone for trivial repository/routing work.
   - For PRD/source/handoff work, add `project-document-production` when its domain procedure materially helps.
   - For Voice requirement/script/DOCX/delivery work, add `voice-production` when its domain procedure materially helps.
   - Add at most one specialist. If investigation exposes a second independent problem, finish or explicitly reframe the first boundary before switching owner.

7. **Implement and final-gate**
   - Make the smallest complete change.
   - Before `Selesai`, re-check the original goal, out-of-scope boundary, acceptance criteria, and available proof.
   - Distinguish `implemented` from `verified` when material local/browser/audio/runtime proof remains unavailable.

## Example Owner Selection

```text
User asks to change how incomplete gameplay sources become a PRD
→ development-brief
→ project-document-production

User asks to change Voice moment extraction or ElevenLabs script wording rules
→ development-brief
→ voice-production

User reports a blank page in Voice Production.docx
→ Maintenance mode first
→ identify builder root cause
→ voice-production only if its domain procedure helps
```

## User-Facing Brief

For non-trivial Developing work:

```text
Tujuan:
Cara berpikir:
Hasil yang dituju:
Tidak diubah:
Cara memastikan benar:
```

For a trivial unambiguous change, one short line is enough.

## Escalation

Escalate only when the concrete task requires it:

- unresolved high-impact requirement → focused discovery/question;
- cross-cutting architecture/migration spanning multiple owners → durable decision/change plan;
- uncertain material evidence → root `AGENTS.md` evidence statuses;
- post-implementation independent critique → review only when it adds real value.

None are default ceremony.
