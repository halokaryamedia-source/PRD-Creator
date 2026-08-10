# Source Intake & Requirement Recovery

Flow 2 turns uneven project material into a production-ready requirement state. It must do more than copy source text: recover project structure, required implications, exclusions, terminology, missing material behavior, and practical solutions without inventing unapproved design choices.

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
- `inspection: full` when the source was inspected deeply enough that no uninspected portion is expected to materially alter current scope.

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

A current user instruction can be authoritative even when no file exists. Preserve coherent material instruction sets as non-file source entries instead of relying on chat history or creating fake text files:

```yaml
id: SRC-007
type: instruction
role: authoritative
origin: user
summary: Objective 2 uses three checkpoints; collapse begins only in checkpoint 3.
inspection: full
```

Do not create one source entry per sentence.

### Source roles and supersession

Roles:

- `authoritative` — defines project facts/requirements;
- `supporting` — explains/supplements authoritative material;
- `reference` — style/sample/Golden; not project fact by default;
- `generated` — prior generated output for continuity/audit only.

Use source-level `status: superseded` only when the source as a whole is no longer authoritative. If one claim/section changed, keep the source and resolve the affected requirement at claim level. Never infer supersession from file date alone.

## 2. Recover explicit production meaning

Recover explicit facts, rules, constraints, decisions, and **negative constraints** before filling gaps.

Treat language such as these as first-class requirements:

```text
add / keep / change
remove / no longer use / do not use
replaced by / only / must not
```

An approved removal/exclusion must prevent lower-authority old source, references, or generated output from silently reintroducing removed behavior.

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
- Reset: if retry is already approved, the collapsed state must be restorable for that retry.
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

If a missing concern would force a downstream role to make a product/design decision, continue through lifecycle/materiality/resolution below.

## 7. Mechanic lifecycle scan

For each material mechanic/system, inspect only the lifecycle stages that actually apply:

```text
ENTRY / PRECONDITION
→ ACTIVATE / TRIGGER
→ ACTIVE BEHAVIOR
→ SUCCESS / COMPLETION
→ FAIL / TIMEOUT / INTERRUPT
→ RESULT / TRANSITION
→ RETRY / RESET
```

A missing lifecycle stage is not automatically a gap. It becomes material only when the mechanic cannot be understood/implemented safely without it.

Example:

```text
"Player repairs the generator"
```

may require checking whether source defines:

- when repair becomes available;
- what action/progress constitutes repair;
- what proves completion;
- what state/result changes after completion;
- whether interruption/retry/reset behavior exists.

Recover what evidence supports. Do not create interaction type, progress count, timer, failure condition, reset rule, or architecture merely because a lifecycle stage exists conceptually.

## 8. Quantitative coherence scan

When source contains related numeric facts, check that they can coexist before drafting.

Examples:

```text
objective duration vs phase/checkpoint durations
player/session count vs arena/capacity assumptions
required item/count totals across sections
scoring components/weights
stage/puzzle/object counts repeated in different sources
range/minimum/maximum rules that overlap
```

A mismatch is evidence to resolve, not permission to silently edit a number. Use authority/precedence first; use Clarification/Completion only when one correction is strongly supported. Otherwise use Proposal/Blocked.

Do not "balance" numbers merely because they look unusual.

## 9. Operational clarity scan

A requirement can exist in source and still be too ambiguous for production. For material rules, ask:

> Could two competent production roles implement materially different outcomes while both reasonably claiming they followed this wording?

If yes, inspect whether the surrounding evidence already narrows the meaning. Common signals include vague terms such as `fast`, `easy`, `clear`, `challenging`, `near`, `large`, `smooth`, or `enough`, and verbs that do not define an observable result.

Do not convert every qualitative direction into a number. A qualitative requirement may remain valid when it intentionally defines experience/visual direction and downstream roles can act on it safely. If the ambiguity changes product behavior/scope, use the normal Resolution Ladder; propose a measurable/observable boundary only when it is supported or genuinely needed.

## 10. Global-vs-local coherence scan

Before readiness, reconcile shared/default rules with package-specific behavior:

```text
shared/global default
→ applies to relevant packages
→ explicit local exception only where evidence requires it
```

Check for:

- a package silently contradicting a global rule;
- two packages using different meanings for what source presents as one shared rule;
- a local exception that is real but not explicitly recorded;
- global rules duplicated as slightly different local requirements.

Prefer one shared requirement plus explicit exceptions. Do not flatten legitimate package differences into one global rule merely for consistency.

## 11. Feasibility and known-constraint scan

When the project/source already defines platform, technical, capacity, production, or other hard constraints, check material requirements against them before proposing a solution.

Examples include known player/arena limits, session limits, platform capabilities, required runtime boundaries, or explicit production constraints supplied by the project.

If a requirement conflicts with an authoritative known constraint, surface the conflict and use the Resolution Ladder. A workaround or redesign is a Proposal unless existing authority already determines it.

Do not import speculative external limitations or generic "best practice" as project authority. Reference/previous-project patterns may help generate a Proposal, but they never convert that Proposal into a recovered fact.

## 12. Problem framing before proposing a solution

When a material issue remains, identify the real production problem before choosing a fix.

Frame only what evidence supports:

```text
Observed issue / symptom
→ affected player/production consequence
→ relevant constraints that must remain true
→ desired outcome implied by project intent
→ roles/requirements affected
```

Example:

```text
Symptom: failure removes too much player progress.
Constraint: objective remains time-limited and collapse mechanic remains.
Goal: reduce frustration without removing failure consequence.
```

Do not manufacture a design problem merely to justify changing an already-valid preference.

### Advisory noise control

A source can be complete yet expose a concrete gameplay/production risk. Flow 2 may surface it, but distinguish:

- **must resolve** — material ambiguity/conflict that blocks `ready_for_prd`;
- **material concern** — non-blocking issue worth showing because it could materially affect quality/feasibility;
- **optional improvement** — keep internal by default unless the user asks for ideas or it is unusually valuable and can be shown without distracting from required decisions.

These are communication priorities, not new recovery classes or mandatory state fields.

## 13. Resolution Ladder

Before asking the user, try the least-assumptive route that can solve the issue:

```text
1. Existing authority/source already resolves it?
   → recover the answer.

2. One necessary evidence-backed completion exists?
   → Completion.

3. Several designs are possible, but one option is materially better supported by project goal + constraints + existing rules?
   → Proposal with one recommended option.

4. Options are genuinely balanced and evidence does not support a clear default?
   → Proposal with 2 concise tradeoff options; state that there is no clear default.

5. No responsible resolution/options can be formed?
   → Blocked / direct user decision.
```

### Recommendation honesty

Use **Recommended** only when evidence, project goals, or constraints actually favor one option. Do not create false confidence merely to make approval easier.

If no option is clearly favored, present the smallest useful tradeoff set—normally two options—and explain the consequence of each. Reference patterns may inspire an option, but project-specific authority/constraints must remain the basis for the decision.

### Safe Completion test

A missing detail may be recovered as **Completion** only when all are true:

1. the conclusion follows from explicit source/approved state or a necessary production implication;
2. there is one reasonable completion at the abstraction level needed by the PRD;
3. it does not choose between multiple plausible gameplay/design/implementation options;
4. it does not invent unsupported quantities, timings, scoring, names, objects, architecture, or decorative detail;
5. the completion can be explained through existing provenance.

If any condition fails and the detail is material, use Proposal or Blocked.

### Material-missing test

A missing detail is material when leaving it unresolved would force Gameplay, Level Design, Developer, or acceptance to choose product behavior/scope, or would change player experience, build scope, runtime behavior, scoring/completion, timing, handoff, reset/interruption, or final result.

If the role can proceed safely while the detail remains intentionally open/neutral, it is not material. Omit it instead of creating filler, a question, or a fake requirement.

## 14. Impact propagation after a resolution

A recovered Completion or approved Proposal must update all **actually affected** meaning, not only the sentence where the issue was found.

Check as applicable:

```text
requirement itself
→ topology / global-vs-local ownership
→ Gameplay implication
→ Level Design implication
→ Developer implication
→ timing / quantities / scoring
→ transition / handoff
→ retry / reset / interruption
```

Use existing REQs + `affects` where useful. Do not create a dependency-graph artifact.

If a new approved resolution invalidates an older claim, resolve/supersede the affected requirement at claim level instead of deleting unrelated valid source meaning.

## 15. Group related issues into one solution package

Do not ask several questions when they are consequences of one root problem.

Example:

```text
checkpoint count
collapse activation
retry location
collapse reset
```

may be one **Failure & Collapse** solution package when one coherent decision controls them.

Internally, keep requirements separate when provenance/acceptance can differ. User-facing communication may group them when one decision can resolve them together.

Default to one recommended solution only when recommendation honesty allows it. Otherwise present the smallest balanced tradeoff set. Do not bundle independent decisions merely to reduce the number of questions.

## 16. Humanized decision communication

Use a bounded **Humanize pass** for Flow 2 user-facing explanations so technical recovery is easy to understand. This is presentation behavior, not a new authority, recovery class, or root skill.

Preferred structure when one recommendation is justified:

```text
<short issue title>

Masalah
<what is unclear or risky, in plain language>

Saran
<one recommended resolution>

Kenapa
<short evidence/constraint-based reason>

Dampak
<what changes for Gameplay / Level Design / Developer / timing / reset as relevant>

Alternatif
<only when a meaningful alternative exists>
```

When there is no clear default, replace `Saran` with a concise `Pilihan` block and explain the tradeoff honestly instead of pretending one option is recommended.

Humanize may improve:

- sentence structure;
- explanation order;
- clarity;
- unnecessary internal jargon exposure.

Humanize may **not** change or soften:

- official names/terminology;
- quantities, timings, coordinates, formulas, scoring weights;
- triggers, conditions, mechanics, failure/result behavior;
- authority/provenance;
- uncertainty;
- approval status;
- technical terminology when it is itself authoritative/production-critical.

Do not expose `SRC-###`, `REQ-###`, recovery-class jargon, YAML, or internal state in normal user communication unless requested or needed to explain a blocker.

Recommendations remain pending until approved. The user may approve all recommendations or override named exceptions.

## 17. Intake state

Keep one status and one practical next step.

```yaml
status: audit_in_progress
next_step: Complete remaining recovery and resolution pass.
```

Omitted unresolved counters mean zero. Positive readiness remains explicit:

```yaml
status: ready_for_prd
ready_for_prd: true
next_step: Build canonical PRD content.
```

Statuses: `collecting_sources`, `audit_in_progress`, `needs_decision`, `blocked`, `ready_for_prd`.

`work/review.md` remains conditional. When decisions are needed, prefer the same humanized solution-package structure above rather than dumping requirement-register internals.

## Revision fast path

A bounded approved revision does not restart Flow 2 when project identity/authority remain clear:

```text
approved change
→ persist material instruction as source when needed
→ affected REQ(s), exclusions, terminology, topology, cross-role implications
→ lifecycle + quantitative + clarity + global/local + feasibility checks only where invalidated
→ impact propagation
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
- material mechanics have been checked for necessary cross-role implications and applicable lifecycle gaps;
- related quantitative facts have no unresolved material contradiction;
- material requirements are operationally clear enough that production roles do not need to choose hidden product behavior;
- shared/global rules and local exceptions are reconciled;
- authoritative known constraints do not silently conflict with required behavior;
- the production coverage scan found no hidden material gap;
- every material issue has gone through problem framing + Resolution Ladder before becoming a user question;
- recovered/approved resolutions have been propagated to affected meaning;
- every material requirement traces to evidence/approved state;
- every Completion passes the safe-completion test;
- unresolved material Proposal/Blocked items prevent readiness;
- intake state truthfully reports `ready_for_prd: true`.

## Stop rule

When the readiness gate passes, stop expanding Flow 2. Do not keep generating optional redesign ideas, extra alternatives, metrics, or hypothetical edge cases merely because more analysis is possible. Flow 2 is a production-recovery/problem-solving stage, not an endless design workshop.

Flow 3 may improve wording and presentation, but it must not be the first place where required project topology, lifecycle behavior, role implications, numeric consistency, global/local coherence, feasibility conflict, or material product decisions are invented/discovered.
