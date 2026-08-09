# Source Intake & Requirement Recovery

This file owns Flow 2 for repository-backed projects. Its purpose is to turn uneven source material into a traceable, resumable requirement state without prematurely writing the final PRD.

## Project Package

Active work lives under:

```text
workspace/active/<project-slug>/
├── README.md
├── source/
│   └── originals/
├── state/
│   ├── source-inventory.yaml
│   ├── requirement-register.yaml
│   └── intake-state.yaml
└── work/
    └── review.md
```

Later flows may add canonical content and final outputs. Do not put final deliverables inside `source/` or overwrite original inputs.

## Source Inventory Contract

Every source receives a stable `SRC-###` ID and records at minimum:

```yaml
id: SRC-001
path: source/originals/example.ext
type: document
role: authoritative
origin: user
status: current
notes: ""
```

Allowed `role` values:

- `authoritative` — project/client material intended to define facts or requirements;
- `supporting` — useful context that may explain an authoritative source;
- `reference` — Golden Sample, style/example/reference material; not project fact by default;
- `generated` — prior generated output retained for continuity/audit only.

Allowed `status` values:

- `current`;
- `superseded`;
- `unreadable`;
- `missing`.

Do not mark a source `superseded` merely because another file is newer. Supersession must be explicit or reliably established by project state.

## Requirement Register Contract

Every material requirement/fact/open decision receives a stable `REQ-###` ID. Record enough information to answer: **what is claimed, where did it come from, what is missing, and does it need approval?**

Recommended fields:

```yaml
id: REQ-001
area: gameplay
statement: "..."
provenance:
  - SRC-001
evidence_status: supported
recovery_class: none
approval_status: not_required
impact: high
affects: []
resolution: ""
```

`evidence_status`:

- `supported` — available evidence supports the statement;
- `conflicting` — material sources disagree and authority/supersession has not resolved it;
- `missing` — required information is absent.

`recovery_class`:

- `none`;
- `clarification`;
- `completion`;
- `proposal`;
- `blocked`.

`approval_status`:

- `not_required`;
- `pending`;
- `approved`;
- `deferred`.

## Recovery Rules

1. Extract before inventing. Read available source first.
2. Preserve provenance. Material statements must remain traceable.
3. Clarification may improve explanation but not meaning.
4. Completion requires strong contextual support and must not define a new material design choice.
5. Proposal is used when the agent must actually choose or define something material. It never self-approves.
6. Blocked is used when evidence is insufficient or materially conflicting.
7. Conflict is evidence state. If authority resolves it, record the resolution. If not, the affected requirement is Blocked.
8. Ask only high-impact unresolved questions. Do not turn intake into a questionnaire for information already recoverable from source.
9. Reference/Golden Sample content may guide structure or demonstrated quality, but never silently supplies project-specific mechanics, names, quantities, story, or scoring.
10. Prior generated output is continuity evidence, not automatic source authority.

## Intake State

`state/intake-state.yaml` keeps one resumable state:

```yaml
status: audit_in_progress
source_count: 0
unresolved_proposals: 0
unresolved_blocked: 0
unresolved_conflicts: 0
ready_for_prd: false
next_step: ""
```

Recommended statuses:

- `collecting_sources`;
- `audit_in_progress`;
- `needs_decision`;
- `blocked`;
- `ready_for_prd`.

There must be exactly one practical `next_step`.

## Human Review

`work/review.md` is the user-facing view of the register. Keep it concise. Show:

1. project/source snapshot;
2. supported facts that materially define the project;
3. Clarification;
4. Completion;
5. Proposal requiring approval;
6. Blocked/conflicting requirements;
7. readiness and one next step.

Do not force empty sections.

## Flow 2 Completion Gate

Flow 2 is complete when:

- every available source is inventoried and read or explicitly marked unavailable/unreadable;
- every material extracted requirement is traceable to evidence or approved state;
- every gap has exactly one recovery class;
- source conflicts are resolved or visibly Blocked;
- low-risk Clarification/Completion has not been unnecessarily escalated to the user;
- `intake-state.yaml` accurately reports `ready_for_prd`, `needs_decision`, or `blocked`;
- unresolved Proposal/Blocked items that materially affect the requested PRD prevent a false `ready_for_prd`.

When `ready_for_prd: true`, Flow 3 may begin canonical PRD generation.
