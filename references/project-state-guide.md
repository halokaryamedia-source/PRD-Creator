# Project State Guide

## Separation of Responsibilities

```text
Decision Log = what has been decided
Project State = where the project is
Assumptions = what is believed but unapproved
Structured Content = approved document content
```

## Required State Files

```text
state/decision-log.yaml
state/project-state.yaml
state/assumptions.yaml
content/project-content.yaml
```

## Decision Log

Each important decision needs a unique ID, stable scope/topic, bilingual decision,
status, reason, affected sections, and source references when available.

Statuses:

- `open`
- `recommended`
- `approved`
- `needs_revision`
- `deferred`
- `replaced`

Only `approved` becomes final content. A replaced decision remains in history and
must reference its replacement. There cannot be two active approved decisions for
the same scope/topic.

## Assumptions

Statuses: `unconfirmed`, `confirmed`, `rejected`, `replaced`. An unconfirmed
assumption must never appear as a Frozen requirement. Approval creates a Decision
Log entry.

## Project State

Track project metadata, Action Mode, Document Profile, current phase, one current
flow, content/html/final status, section statuses, open questions, blockers,
deferred items, errors, versions, artifact history, and exactly one primary
`next_step`.

Section statuses:

- `not_started`
- `discussing`
- `drafting`
- `in_review`
- `approved`
- `frozen`
- `needs_revision`

## One Main Active Flow

Only one flow is primary. Change it only after completion, explicit priority
change, or a newly discovered Critical blocker.

## Questions, Blockers, Deferred Items

Use stable IDs. When a question resolves, create/update the Decision Log, close
the question, remove its blocker, and update affected sections.

Do not label cosmetic preferences as blockers.

## Next Step

Store exactly one actionable next step with reason, target phase, and target flow.
It must be specific and based on current state.

## Resume Order

For Continue or Update read:

1. Project State
2. relevant approved decisions
3. latest Structured Content
4. latest artifact and audit report
5. relevant source documents

Do not restart Intake unless identity, scope, or source of truth changed.

## Revision Cycle

A Frozen document must be reopened as `needs_revision` before changes. Impacted
sections are updated and re-audited, then a new Content Freeze is created.

## Version Ownership

Project State stores the current content, template, schema, Golden Sample, and
HTML versions plus artifact checksums and latest status. `rendering-guide.md`
defines when each version increments.

## State Validation

Validate supported Action Mode/profile/phase, current flow, section statuses,
Decision/Blocker references, next step, and latest artifact identity. Do not
continue from corrupted state silently.

## Missing State Recovery

Reconstruct only directly supported facts, mark them `needs_confirmation`, and
request user confirmation. Never invent earlier approvals.
