# Audit Guide

## Audit Levels

1. Mini Audit after one flow
2. Main Multi-Perspective Content Audit
3. Consistency Audit
4. Freeze Readiness Audit

Final rendered HTML audit is owned by `rendering-guide.md`.

## Audit Principles

Audit usability, logic before wording, approved decisions against Structured
Content, root causes rather than repeated symptoms, and affected dependencies
after corrections. Do not silently change product decisions during audit.

## Player / New Reader

Verify context, role, objective, sequence, starting and ending conditions,
blocked/fail state, result, handoff, and understandable terminology.

A reader should answer: Where am I? What do I do? What starts and ends this?
What can block me? What continues forward?

## Level Designer

Verify required areas/objects, relationships, entry/exit/return route, landmarks,
important sizes, visual readability, mechanic space, build order, and separation
of visual requirements from gameplay function.

A builder should be able to begin blockout without guessing the main spatial
structure.

## Developer

Verify mechanic, activation, progression, completion validation, quantities,
item behavior, timer, score/completion data, duplicate prevention, interruption,
reset, verification, and session ownership.

A developer should be able to make an implementation plan without inventing
product rules.

## Reader Assumption

- Reviewer/player may read Gameplay Overview only.
- Level Designer reads Gameplay Overview → Level Design.
- Developer reads Gameplay Overview → Level Design → Developer.
- Global developer reads relevant Global Development pages.

Pages need local context but should not duplicate the full package unnecessarily.

## Consistency Audit

Compare Overview, Gameplay Flow, package pages, scoring/completion data, reset,
and handoffs. Check terminology, quantities, objective order, start/end moments,
timers, weights, item transfer, session ownership, interruptions, and final result.
Different wording is allowed; different meaning is not.

## Scoring Audit

Verify score name/scale/components/100% weights/target/bonus/reduction/timer
start-stop/excluded time/no-score/recorded data/duplicate prevention/rounding when
needed/final-result relationship and explicit input quantities.

## Completion Data Audit

Verify no Objective Score, valid completion, recorded data, interrupted behavior,
duplicate prevention, and next-package handoff.

## Glossary Audit

Verify definitions, scope, aliases, ID/EN meaning, no conflicts, no collisions,
longer-term priority, removal of unused terms, and no excessive ordinary-word
matching.

## Severity

- **Critical:** can cause incorrect gameplay, build, scoring, data, ownership, or implementation.
- **Major:** important information is missing or unsafe to implement.
- **Minor:** logic remains correct but clarity/consistency is reduced.
- **Suggestion:** optional improvement.
- **Approved:** complete and usable.

Critical and Major block Content Freeze. A Minor may be accepted only when it
does not affect meaning and user acceptance is recorded.

## Finding Workflow

```text
Finding → Determine if product decision is required → Update Decision Log when
needed → Update Structured Content → Synchronize dependencies → Re-audit → Resolve
```

A finding resolves only after source-of-truth content changes and re-audit passes.

## Freeze Readiness

Requires all required sections approved, Critical=0, Major=0, blockers=0,
approved decisions synchronized, scoring/completion/glossary validation passed,
consistency passed, deferred required issues resolved, and approved scope reviewed.
