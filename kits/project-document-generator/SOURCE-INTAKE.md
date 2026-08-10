# Source Intake & Requirement Recovery

Flow 2 recovers enough trustworthy project meaning for Flow 3 without making the user manage repository structure, answer avoidable questions, or pay context for irrelevant material.

## Automatic bootstrap

```text
user project name OR strongest authoritative title
→ derive stable kebab-case slug
→ reuse clearly matching active project OR create workspace/active/<slug>/
→ preserve supplied originals
→ create only current-Flow artifacts
```

Do not ask the user for slugs, folders, IDs, YAML shape, or renderer files. Ask only when project identity is genuinely ambiguous.

## Relevance-first reading

Inventory supplied/current source, then choose reading depth by authority and relevance:

```text
inventory
→ quick relevance/authority triage
→ deep-read material authoritative evidence
→ targeted-read supporting/reference/generated evidence as needed
→ recover requirements
```

Triage may use filename/title, role, TOC/headings, metadata, preview/snippet, or established project context.

Rules:

- deep-read authoritative material that can materially change current scope;
- supporting material is read only as far as needed to confirm/resolve current requirements;
- Golden/reference material is read only for the demonstrated structure/quality actually needed; do not reload the full Golden when its contract is already encoded;
- generated prior output is read only for continuity/conflict/bounded revision needs;
- uncertain evidence that could materially change the PRD must be inspected rather than assumed irrelevant;
- bounded revisions do not reread unchanged source;
- reading economy must never hide a contradiction, superseding instruction, or material requirement.

Goal: **complete production meaning, not complete byte consumption**.

## Flow 2 package

Minimum active package:

```text
source/originals/
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
```

`work/review.md` is conditional. Later-Flow artifacts are not pre-created.

## Source inventory

Every source gets a stable `SRC-###`. Store only information that adds meaning.

Normal form:

```yaml
id: SRC-001
path: source/originals/example.docx
role: authoritative
```

Omittable defaults:

```text
type   → infer when obvious
origin → user
status → current
notes  → absent when none
```

Write non-default state explicitly, for example `status: superseded|unreadable|missing` and a useful note. Do not infer supersession from file date alone.

Roles:

- `authoritative` — defines project facts/requirements;
- `supporting` — explains/supplements authoritative material;
- `reference` — style/sample/Golden; not project fact by default;
- `generated` — prior generated output for continuity/audit only.

## Requirement register

Create one `REQ-###` per meaningful production rule, constraint, conflict, or open decision that must survive into PRD/acceptance. Do not mirror source sentences or catalog incidental facts.

Normal supported requirement:

```yaml
id: REQ-001
area: gameplay
statement: Player must cross the bridge before collapse.
provenance: [SRC-001]
impact: high
```

Omittable defaults:

```text
evidence_status → supported
recovery_class  → none
approval_status → not_required
affects         → []
resolution      → absent when none
```

Non-default state is always explicit:

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

Sparse storage must never hide conflict, blocker, pending approval, supersession, or another non-default condition.

Granularity:

- combine tightly coupled facts that function as one rule;
- split only when source/approval/conflict/implementation/acceptance can differ independently;
- attach multiple provenance sources to one requirement instead of duplicating it;
- keep one stable meaning per REQ.

## Recovery classes

- **Clarification** — improve explanation without changing existing meaning.
- **Completion** — one low-risk completion is strongly supported by surrounding evidence.
- **Proposal** — a material design/product choice is required; user approval is mandatory.
- **Blocked** — evidence is insufficient or materially conflicting.

Conflict is an evidence condition, not a fifth class. Golden/reference material may guide structure/quality but may not silently supply project names, mechanics, quantities, story, scoring, or runtime rules.

## Question economy

```text
triage + inspect materially relevant source
→ reconcile authority/duplicates
→ recover supported requirements
→ safe Clarification / Completion
→ collect unresolved material Proposal / Blocked items
→ one grouped decision review when needed
```

Zero questions is preferred when the project is sufficiently defined. Never ask for facts already recoverable from current source/state.

When approval is needed:

```text
Decision N — <topic>
Recommended: <option>
Reason: <short evidence-based reason>
Impact: <what changes>
```

The user may approve all recommendations or override named exceptions. Recommendations remain pending until approved.

## Intake state

Keep one status and one practical next step.

In progress:

```yaml
status: audit_in_progress
next_step: Complete remaining source recovery.
```

Omitted unresolved counters mean zero; write non-zero counters only when useful. Positive readiness is explicit:

```yaml
status: ready_for_prd
ready_for_prd: true
next_step: Build canonical PRD content.
```

Statuses: `collecting_sources`, `audit_in_progress`, `needs_decision`, `blocked`, `ready_for_prd`.

## Conditional human review

Create/update `work/review.md` only when it adds user/resumability value: approval is needed, a blocker/conflict must be surfaced, meaningful recovery should be visible, the user requests an intake summary, or a concise persistent note materially helps continuation.

When used, keep only: source/scope snapshot, meaningful recovery, decisions/blockers, readiness, and one next step. Detailed traceability stays in the register.

## Revision fast path

A bounded approved revision does not restart Flow 2 when project identity/authority remain clear:

```text
approved change
→ affected REQ(s)
→ necessary cross-reference/conflict check
→ downstream revision path
```

Reopen broader intake only when source authority, shared/global rules, broader scope, or unresolved material decisions are affected.

## Completion gate

Flow 2 is complete when:

- every source that can materially affect current scope is inventoried and inspected to sufficient depth, or explicitly unavailable/unreadable;
- every production-relevant requirement traces to evidence/approved state;
- material gaps/conflicts are resolved or visibly Proposal/Blocked;
- low-risk recovery was not unnecessarily escalated;
- intake state truthfully reports readiness;
- `ready_for_prd: true` cannot coexist with an unresolved material Proposal/Blocked item affecting required output.

Then Flow 3 may begin.
