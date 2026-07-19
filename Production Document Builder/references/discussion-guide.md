# Discussion Guide

## Goal

Convert incomplete source material into approved, production-usable decisions
without overwhelming the user or returning the whole design problem to them.

## Before Asking

Review source documents, approved decisions, Project State, Structured Content,
blockers, deferred topics, and downstream dependencies. Do not repeat answered
questions.

## Active Flow

Maintain one main active flow. Choose the topic that unlocks the most downstream
work, using this priority:

1. Project structure
2. Gameplay sequence
3. Active package completion/handoff
4. Critical global system dependency
5. Scoring and data
6. Interruption and reset
7. Production detail
8. Polish

## Round Size

Normal: three to five related decisions. Maximum: five. One complex decision may
be discussed alone.

## Decision Card

For important decisions present:

- Topic
- Information from Source
- Missing or Ambiguous Information
- Primary Recommendation
- Reason
- One Alternative, only when meaningful
- Impact
- Decision Required

Approval is never inferred from silence.

## User Has No Clear Direction

Summarize known context, identify the missing decision, recommend a complete but
simple solution, explain the practical and production impact, offer at most one
alternative, and request confirmation.

Use outcome-based language. Ask what happens to the player or system, not which
technical architecture the user prefers.

## Package Order

### Gameplay

Lock context, objective, start, end, blocked/fail condition, actions, output,
time, and scoring criteria.

### Level Design

Lock areas, relationships, entry/exit/return route, landmarks, important sizes,
mechanic space, visual direction, and gameplay function.

### Developer

Lock mechanic, activation, progression, completion validation, item behavior,
timer, scoring/completion data, duplicate prevention, interruption, reset,
verification, and ownership.

## Direct Corrections

Apply the exact correction, show old/new rule and downstream impact, and avoid
rewriting unrelated sections.

## Open, Deferred, and Blocking

A blocking decision prevents flow completion. A deferred decision may wait only
when it does not block required content. Deferred required issues must return
before Content Freeze.

## Prevent Circular Discussion

- Do not reopen approved decisions without evidence.
- Consolidate repeated symptoms into one root decision.
- After two rounds without resolution, give a final recommendation.
- If still unresolved, mark the topic deferred or blocking.
- Use Project State rather than conversation memory alone.

## Mini Audit

Run a Mini Audit after drafting one flow. The checklist and severity source is
`audit-guide.md`; this guide only determines timing and perspective.

## Flow Completion

A flow completes when required content exists, critical data is explicit, no
blocking contradiction remains, terminology is defined, Mini Audit passes, user
approves, and Decision Log/Project State are updated.

After completion, provide Status Selesai, approved decisions/results, open items,
progress, and one next step.
