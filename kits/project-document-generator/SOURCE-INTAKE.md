# Source Intake & Requirement Recovery

This file owns Flow 2 for repository-backed projects. Its purpose is to turn uneven source material into a traceable, resumable requirement state without prematurely writing the final PRD or forcing unnecessary review rounds.

## Automatic project bootstrap

The user should not need to prepare repository structure before PRD production.

For a new project:

```text
user-provided project name OR strongest authoritative source title
→ derive stable project name
→ derive lowercase kebab-case project slug
→ reuse a clearly matching active project OR create workspace/active/<project-slug>/
→ preserve supplied originals
→ create only the state/work structure needed by the current Flow
```

Rules:

- do not ask the user to choose a slug, folder name, source ID, requirement ID, or internal YAML structure;
- reuse an existing active project when current evidence clearly shows the source belongs to it;
- ask only when multiple plausible projects would make automatic placement unsafe;
- project bootstrap is internal setup, not a user approval stage.

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
    └── review.md        # only when a human-facing review is useful
```

Later flows may add canonical content and final outputs. Do not put final deliverables inside `source/` or overwrite original inputs.

## Source Inventory Contract

Every source receives a stable `SRC-###` ID internally and records at minimum:

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

Every production-relevant requirement, constraint, conflict, or open decision that must survive into the PRD or acceptance flow receives a stable `REQ-###` ID internally. Do **not** create requirement IDs for incidental descriptive facts that do not affect scope, behavior, build, implementation, scoring, handoff, acceptance, or an unresolved decision.

Record enough information to answer: **what is claimed, where did it come from, what is missing, and does it need approval?**

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

## Requirement granularity

Keep the register useful rather than exhaustive.

- One `REQ-###` should represent one meaningful production rule, constraint, or decision.
- Combine tightly coupled facts when they only make sense as one rule.
- Split items only when they can differ independently in source, approval, conflict, implementation impact, or acceptance.
- Do not mirror the source sentence-by-sentence.
- Do not create duplicate requirements merely because the same rule appears in several files; preserve multiple provenance references on the same requirement when appropriate.

The goal is traceability for decisions and production behavior, not a catalog of every sentence in the source.

## Recovery Rules

1. Extract before inventing. Read available source first.
2. Preserve provenance. Material statements must remain traceable.
3. Clarification may improve explanation but not meaning.
4. Completion requires strong contextual support and must not define a new material design choice.
5. Proposal is used when the agent must actually choose or define something material. It never self-approves.
6. Blocked is used when evidence is insufficient or materially conflicting.
7. Conflict is evidence state. If authority resolves it, record the resolution. If not, the affected requirement is Blocked.
8. Reference/Golden Sample content may guide structure and demonstrated quality, but never silently supplies project-specific mechanics, names, quantities, story, or scoring.
9. Prior generated output is continuity evidence, not automatic source authority.

## Question Economy

Do not interrupt source inspection with questions that may be answered by later material.

Use this order:

```text
inspect all available source
→ reconcile authority / duplicates
→ recover supported requirements
→ apply safe Clarification / Completion
→ identify only remaining material Proposal / Blocked items
→ ask one grouped decision review when possible
```

Rules:

- do not ask the user for information already recoverable from source or approved state;
- do not ask one question per file or one question per requirement;
- group related high-impact decisions into one concise review;
- low-risk Clarification/Completion should not create an approval round;
- zero questions is the preferred result when the project is already sufficiently defined.

## Recommended decision batch

When a Proposal genuinely needs approval, reduce user effort by doing the analysis first.

Default format:

```text
Decision 1 — <topic>
Recommended: <option>
Reason: <short source/context reason>
Impact: <what changes>

Decision 2 — <topic>
Recommended: <option>
Reason: <short source/context reason>
Impact: <what changes>
```

The user may approve efficiently:

```text
Approve all recommendations.
```

or override only specific items:

```text
Approve all except Decision 2: use <other option>.
```

Rules:

- recommendations must be grounded in current source/context;
- the recommendation is still `proposal` / `pending` until user approval;
- do not make the user invent an option from scratch when a safe evidence-based recommendation can be presented;
- if there is no responsible recommendation, present the real choice/unknown plainly instead of manufacturing one.

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

`work/review.md` is a **conditional** human-facing decision/recovery summary, not a mandatory second requirement register.

Create or materially update it when at least one of these is true:

- Proposal requires approval;
- Blocked/conflicting requirement needs attention;
- meaningful Completion/Clarification changes how the project is understood and should be surfaced;
- the user explicitly asks for an intake summary;
- a persistent review note materially helps resumability.

When used, keep it concise:

1. short project/source snapshot;
2. compact confirmed production scope;
3. meaningful Clarification/Completion only;
4. Proposal requiring approval, with recommendation/reason/impact when a responsible recommendation exists;
5. Blocked/conflicting requirements requiring attention;
6. readiness and one next step.

Do not dump every supported fact into the review. Detailed traceability belongs in `requirement-register.yaml`.

If no human decision/recovery summary is needed, Flow 2 may advance directly through `intake-state.yaml` without forcing a separate user review round.

## Revision input

An explicit approved user revision to an existing project does not require full source intake again by default.

Route it to the revision fast path when:

- the project identity is already clear;
- the user instruction itself is authoritative for the requested change;
- the change is local/bounded;
- it does not invalidate source authority or introduce a broader conflict.

Update the affected requirement(s) and preserve the prior traceability. Reopen full intake only when the change materially affects broader scope, shared/global rules, source authority, or unresolved decisions.

## Flow 2 Completion Gate

Flow 2 is complete when:

- every available source relevant to current scope is inventoried and read or explicitly marked unavailable/unreadable;
- every production-relevant requirement is traceable to evidence or approved state;
- every material gap has exactly one recovery class;
- source conflicts are resolved or visibly Blocked;
- low-risk Clarification/Completion has not been unnecessarily escalated to the user;
- remaining material decisions were grouped and surfaced efficiently when needed;
- `intake-state.yaml` accurately reports `ready_for_prd`, `needs_decision`, or `blocked`;
- unresolved Proposal/Blocked items that materially affect the requested PRD prevent a false `ready_for_prd`.

When `ready_for_prd: true`, Flow 3 may begin canonical PRD generation.
