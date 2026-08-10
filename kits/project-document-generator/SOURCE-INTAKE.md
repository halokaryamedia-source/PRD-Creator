# Source Intake & Requirement Recovery

This file owns Flow 2 for repository-backed PRD projects. Its job is to recover enough trustworthy project meaning for Flow 3 without forcing the user to prepare repository structure, answer unnecessary questions, or pay model context for irrelevant material.

## Automatic project bootstrap

For a new project:

```text
user project name OR strongest authoritative title
→ derive stable kebab-case slug
→ reuse a clearly matching active project OR create workspace/active/<slug>/
→ preserve supplied originals
→ create only artifacts required by the active Flow
```

Do not ask the user to choose slugs, folders, IDs, YAML shape, or renderer files. Ask only when project identity is genuinely ambiguous.

## Relevance-first source reading

All supplied/current sources relevant to the project are inventoried, but **inventory does not mean deep-reading every byte**.

Use this sequence:

```text
inventory source
→ quick relevance/authority triage
→ deep-read material authoritative source
→ targeted-read supporting/reference/generated source only where it can affect current scope
→ recover requirements
```

Triage may use filename/title, source role, table of contents, headings, metadata, preview/snippet, or already-known project context when available.

Rules:

- deep-read authoritative material that can materially change current scope;
- read supporting material only to the depth needed to resolve/confirm current requirements;
- read reference/Golden material only for the demonstrated structure/quality actually needed; do not reload the full Golden document when its contract is already encoded in PRD-Creator;
- read prior generated output only where it contributes continuity, conflict detection, or a bounded revision;
- if relevance is uncertain and the source could materially change the PRD, inspect it rather than assuming it is irrelevant;
- do not repeatedly reread unchanged sources during bounded revisions;
- do not let source-reading economy hide a contradiction, superseding instruction, or material requirement.

The goal is **complete production meaning**, not complete byte consumption.

## Project package during Flow 2

Minimum active package:

```text
workspace/active/<project-slug>/
├── source/originals/
└── state/
    ├── source-inventory.yaml
    ├── requirement-register.yaml
    └── intake-state.yaml
```

`work/review.md` is conditional and appears only when a human-facing decision/recovery summary is useful.

Later Flow artifacts are not pre-created merely because the repository eventually supports them.

## Source inventory

Every source receives a stable `SRC-###` internally. Persist only fields that add information.

Compact normal form:

```yaml
id: SRC-001
path: source/originals/example.docx
role: authoritative
```

Defaults that may be omitted:

```text
type   → infer from file/format when obvious
origin → user
status → current
notes  → absent when there is nothing useful to record
```

Write exceptions when needed, for example:

```yaml
id: SRC-004
path: source/originals/old-notes.pdf
role: supporting
status: superseded
notes: Replaced by SRC-006 for Objective 2 timing.
```

Allowed roles:

- `authoritative` — intended to define project facts/requirements;
- `supporting` — explains or supplements authoritative material;
- `reference` — sample/Golden/reference material; not project fact by default;
- `generated` — prior generated output retained for continuity/audit only.

Allowed non-default statuses include `superseded`, `unreadable`, and `missing`.

Do not infer supersession from file date alone.

## Requirement register

Create one `REQ-###` per meaningful production rule, constraint, conflict, or open decision that must survive into PRD/acceptance. Do not mirror source sentences or catalog incidental facts.

Compact supported requirement:

```yaml
id: REQ-001
area: gameplay
statement: Player must cross the bridge before collapse.
provenance: [SRC-001]
impact: high
```

Default semantics may be omitted:

```text
evidence_status  → supported
recovery_class   → none
approval_status  → not_required
affects          → []
resolution       → absent when none is needed
```

Persist exception state explicitly:

```yaml
id: REQ-014
area: gameplay
statement: Collapse starts at checkpoint 2 or 3.
provenance: [SRC-001, SRC-003]
evidence_status: conflicting
recovery_class: proposal
approval_status: pending
impact: high
```

Sparse state is a storage rule only; it does **not** weaken traceability. Missing non-default state must never be interpreted as approval or conflict resolution.

Requirement granularity:

- combine tightly coupled facts that function as one production rule;
- split only when items can differ independently in source, approval, conflict, implementation, or acceptance;
- attach multiple provenance references to one requirement instead of duplicating the requirement;
- keep one stable meaning per REQ.

## Recovery classes

- **Clarification** — meaning already exists; wording/explanation may improve without changing intent.
- **Completion** — missing detail has one strongly supported low-risk completion.
- **Proposal** — a material design/product choice must be made; requires approval.
- **Blocked** — evidence is insufficient or materially conflicting.

Conflict is an evidence condition. If authority does not resolve it, the affected requirement becomes Blocked/Proposal as appropriate.

Golden/reference material may guide demonstrated structure/quality but never silently supplies project-specific names, mechanics, quantities, story, scoring, or runtime rules.

## Question economy

```text
triage + inspect all materially relevant source
→ reconcile authority/duplicates
→ recover supported requirements
→ apply safe Clarification/Completion
→ collect remaining material Proposal/Blocked items
→ one grouped decision review when needed
```

Zero questions is preferred when the project is sufficiently defined.

When approval is required:

```text
Decision N — <topic>
Recommended: <option>
Reason: <short source/context reason>
Impact: <what changes>
```

The user may approve all recommendations or override named exceptions. A recommendation remains pending until approved.

## Intake state

`state/intake-state.yaml` keeps one current status and one practical next step.

Normal in-progress form:

```yaml
status: audit_in_progress
next_step: Complete remaining source recovery.
```

Only persist non-zero unresolved counters when they help continuation. Omitted unresolved counts mean zero.

Positive readiness remains explicit:

```yaml
status: ready_for_prd
ready_for_prd: true
next_step: Build canonical PRD content.
```

Recommended statuses:

- `collecting_sources`;
- `audit_in_progress`;
- `needs_decision`;
- `blocked`;
- `ready_for_prd`.

Do not maintain redundant false/zero fields simply to make every state file look identical.

## Conditional human review

Create/update `work/review.md` only when it adds user or resumability value, such as:

- Proposal requires approval;
- Blocked/conflicting requirement needs attention;
- meaningful Clarification/Completion should be surfaced;
- the user asks for an intake summary;
- a concise persistent note materially helps continuation.

When used, keep only: project/source snapshot, confirmed scope, meaningful recovery, decisions/blockers, readiness, and one next step. Detailed traceability remains in the requirement register.

## Revision fast path

An explicit approved bounded revision does not restart full intake when project identity and authority are already clear.

```text
approved change
→ affected REQ(s)
→ necessary cross-reference/conflict check
→ continue downstream revision path
```

Reopen broader intake only when the change affects source authority, shared/global rules, broader scope, or unresolved material decisions.

## Flow 2 completion gate

Flow 2 is complete when:

- every source that can materially affect current scope has been inventoried and inspected to sufficient depth, or explicitly marked unavailable/unreadable;
- every production-relevant requirement is traceable to evidence or approved state;
- material conflicts/gaps are resolved or visibly Proposal/Blocked;
- low-risk recovery was not unnecessarily escalated to the user;
- `intake-state.yaml` truthfully reports readiness;
- `ready_for_prd: true` is impossible while unresolved material Proposal/Blocked items affect required output.

When ready, Flow 3 begins canonical PRD generation.