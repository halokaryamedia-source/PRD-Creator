# Source Intake & Requirement Recovery

Flow 2 turns uneven project material into a production-ready requirement state. It must do more than copy source text: recover project structure, required implications, exclusions, terminology, and material gaps without inventing design choices.

## Automatic bootstrap

```text
user project name OR strongest authoritative title
→ derive stable kebab-case slug
→ reuse clearly matching active project OR create workspace/active/<slug>/
→ preserve supplied originals
→ create only current-Flow artifacts
```

Do not ask the user for slugs, folders, IDs, YAML shape, or renderer files. Ask only when project identity is genuinely ambiguous.

## 1. Inventory, authority, and reading depth

Inventory supplied/current source, then choose reading depth by authority and relevance:

```text
inventory
→ authority/relevance triage
→ deep-read material authoritative evidence
→ targeted-read supporting/reference/generated evidence as needed
```

Goal: **complete production meaning, not complete byte consumption**.

Rules:

- material authoritative source must be inspected deeply enough for current scope;
- supporting material is read only as far as needed to confirm/resolve requirements;
- Golden/reference material is read only for the demonstrated structure/quality actually needed;
- generated prior output is continuity/conflict evidence, not automatic authority;
- uncertain evidence that could materially change the PRD must be inspected;
- bounded revisions do not reread unchanged source;
- reading economy must never hide a contradiction, superseding instruction, exclusion, or material requirement.

### Persist inspection coverage

Every source gets a stable `SRC-###`. File-backed normal form:

```yaml
id: SRC-001
path: source/originals/example.docx
role: authoritative
inspection: full
```

Sparse defaults:

```text
type   → infer when obvious
origin → user
status → current
notes  → absent when none
inspection omitted → inventoried/triaged only
```

Use:

- `inspection: targeted` when only bounded material was read; add a concise `inspection_scope`;
- `inspection: full` when the source was inspected deeply enough that no uninspected portion is expected to materially alter the current project scope.

Example:

```yaml
id: SRC-003
path: source/originals/legacy-notes.pdf
role: supporting
inspection: targeted
inspection_scope: Objective 2 timing and reset behavior
```

This records coverage for resumability; it is not a checksum/revision system.

### Persist material user instructions

A current user instruction can be authoritative even when no file exists. Preserve material instruction sets as non-file source entries instead of relying on chat history or creating fake text files:

```yaml
id: SRC-007
type: instruction
role: authoritative
origin: user
summary: Objective 2 uses three checkpoints; collapse begins only in checkpoint 3.
inspection: full
```

Do not create one source entry per sentence. Group one coherent material instruction/decision set when practical.

### Source roles and supersession

Roles:

- `authoritative` — defines project facts/requirements;
- `supporting` — explains/supplements authoritative material;
- `reference` — style/sample/Golden; not project fact by default;
- `generated` — prior generated output for continuity/audit only.

Use source-level `status: superseded` only when the source as a whole is no longer authoritative. If only one claim/section changed, keep the source and resolve the affected requirement at claim level through current provenance/resolution. Never infer supersession from file date alone.

## 2. Recover explicit production meaning

Recover explicit facts, rules, constraints, decisions, and **negative constraints** before filling gaps.

Treat language such as these as first-class requirements:

```text
add / keep / change
remove / no longer use / do not use
replaced by / only / must not
```

An approved removal/exclusion must prevent lower-authority old source, references, or generated output from silently reintroducing the removed behavior.

Create one `REQ-###` per meaningful production rule, constraint, conflict, exclusion, topology rule, or open decision that must survive into PRD/acceptance. Do not mirror source sentences or catalog incidental facts.

Normal requirement:

```yaml
id: REQ-001
area: gameplay
statement: Player must cross the bridge before collapse.
provenance: [SRC-001]
impact: high
```

Sparse defaults:

```text
evidence_status → supported
recovery_class  → none
approval_status → not_required
affects         → []
resolution      → absent when none
```

Write every non-default conflict/recovery/approval condition explicitly. Use `affects` only when it materially helps show one requirement's cross-role impact; do not duplicate the same meaning merely to fill role buckets.

## 3. Recover project topology

Before `ready_for_prd`, reconstruct the project structure needed by Flow 3:

```text
project experience
├── shared/global rules
├── ordered gameplay packages/stages
├── package dependencies/transitions
└── ending/final result or handoff
```

Recover only topology supported by source/approved state. Store topology as normal requirements (for example `area: topology` or `area: global`); do not create a separate topology artifact.

A topology gap is material when Flow 3 would otherwise have to choose package order, global-vs-local ownership, transition behavior, dependency, or final result. Material ambiguity becomes Completion only when one safe interpretation exists; otherwise Proposal/Blocked.

## 4. Normalize terminology before drafting

Detect source variants that may refer to the same project concept.

```text
Power Core / Energy Core / Generator Core
→ same concept? use highest-authority canonical name
→ different concepts? preserve distinction
→ unclear? Clarification / conflict
```

Record a material terminology decision as a normal requirement when it must survive into the PRD. Do not synonym-cycle official concepts during drafting.

## 5. Cross-role implication recovery

For each material mechanic/system, check whether explicit facts imply production work beyond the sentence itself:

```text
PLAYER        What experience/condition/result is necessarily implied?
LEVEL DESIGN  What area/object/relationship/readability requirement must exist?
DEVELOPER     What activation/state/progression/completion behavior must exist?
RESULT        What transition/handoff/reset/interruption consequence is required?
```

Example:

```text
Source: Bridge collapses when the timer expires.

Safe implications may include:
- Gameplay: player must cross before the collapse condition.
- Level Design: a defined collapsible route must exist and remain readable as the required crossing.
- Developer: the route changes state when the approved timer condition expires.
- Reset: if retry is already part of the approved flow, the collapsed state must be restorable for that retry.
```

Do **not** infer exact block counts, coordinates, animations, cooldowns, implementation architecture, or other choices unless source/approved state supports them.

When an implication is independently actionable, record it as its own requirement with provenance and `recovery_class: completion`. When one requirement already expresses the complete shared rule, use `affects` rather than paraphrasing it several times.

## 6. Production coverage scan

After explicit recovery + implications, scan the **applicable concerns** before declaring readiness. This is a reasoning pass, not a form that must be fully populated.

| Scope | Check when relevant |
|---|---|
| Project topology | journey/package order, shared/global ownership, transitions/dependencies, final result |
| Gameplay | purpose/objective, start, completion/end, fail/retry/blocked condition, player result |
| Level Design | required areas/objects, relationships/routes, known constraints, readability/build intent, gameplay function |
| Developer | activation, progression/state, completion or scoring, required timing/quantities/data, reset/interruption, transition/result |
| Critical cross-cutting | player/session/arena counts, timing boundaries, scoring inputs/weights, handoff, disconnect/interruption, reset, final-result rules |

First decide whether a concern applies. **Irrelevant or intentionally unspecified detail is not a gap.** Do not invent or ask for information merely because the Golden structure could display it.

If a missing concern would force a downstream role to make a product/design decision, classify it through the materiality/recovery tests below.

## 7. Safe Completion test

A missing detail may be recovered as **Completion** only when all are true:

1. the conclusion follows from explicit source/approved state or a necessary production implication;
2. there is one reasonable completion at the abstraction level needed by the PRD;
3. it does not choose between multiple plausible gameplay/design/implementation options;
4. it does not invent unsupported quantities, timings, scoring, names, objects, architecture, or decorative detail;
5. the completion can be explained through existing provenance.

If any condition fails and the missing detail is material:

- use **Proposal** when a design/product choice can responsibly be presented for approval;
- use **Blocked** when evidence is insufficient/conflicting and no responsible completion/proposal can be made.

**Clarification** only improves wording/explanation of meaning that already exists.

## 8. Material-missing test

A missing detail is material when leaving it unresolved would force Gameplay, Level Design, Developer, or acceptance to choose product behavior/scope, or would change player experience, build scope, runtime behavior, scoring/completion, timing, handoff, reset/interruption, or final result.

If the role can proceed safely while the detail remains intentionally open/neutral, it is not material. Omit it instead of creating filler, a question, or a fake requirement.

## 9. Conflict and decision economy

Sequence:

```text
inspect material evidence
→ reconcile authority/duplicates
→ explicit recovery
→ topology + terminology + exclusions
→ cross-role implication pass
→ coverage scan
→ safe Clarification / Completion
→ collect unresolved material Proposal / Blocked items
→ one grouped decision review when needed
```

Zero questions is preferred when evidence is sufficient. Never ask for facts already recoverable from current source/state.

When approval is needed:

```text
Decision N — <topic>
Recommended: <option>
Reason: <short evidence-based reason>
Impact: <what changes>
```

Recommendations remain pending until approved. The user may approve all or override named exceptions.

## Intake state

Keep one status and one practical next step.

```yaml
status: audit_in_progress
next_step: Complete remaining requirement recovery and coverage scan.
```

Omitted unresolved counters mean zero. Positive readiness remains explicit:

```yaml
status: ready_for_prd
ready_for_prd: true
next_step: Build canonical PRD content.
```

Statuses: `collecting_sources`, `audit_in_progress`, `needs_decision`, `blocked`, `ready_for_prd`.

`work/review.md` remains conditional; use it only when decisions/blockers/meaningful recovery should be surfaced or a concise persistent note materially helps continuation.

## Revision fast path

A bounded approved revision does not restart Flow 2 when project identity/authority remain clear:

```text
approved change
→ persist material instruction as source when needed
→ affected REQ(s), exclusions, terminology, topology, cross-role implications
→ necessary conflict/coverage check
→ downstream revision path
```

Reopen broader intake only when source authority, shared/global rules, topology, broader scope, or unresolved material decisions are affected.

## `ready_for_prd` gate

Flow 2 is ready only when:

- every source that can materially affect current scope is inventoried and inspected to sufficient depth, or explicitly unavailable/unreadable;
- material user instructions are persisted rather than left only in chat history;
- explicit rules **and exclusions** are recovered;
- project topology is sufficient for Flow 3 to organize the document without inventing order/ownership/transitions;
- material terminology ambiguity is resolved or surfaced;
- material mechanics have been checked for necessary cross-role implications;
- the production coverage scan found no hidden material gap;
- every material requirement traces to evidence/approved state;
- every Completion passes the safe-completion test;
- unresolved material Proposal/Blocked items prevent readiness;
- intake state truthfully reports `ready_for_prd: true`.

Flow 3 may improve wording and presentation, but it must not be the first place where required project topology, role implications, or material product decisions are invented/discovered.
