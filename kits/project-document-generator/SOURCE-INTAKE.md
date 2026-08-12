# Source Intake & Requirement Recovery

Flow 2 turns uneven project material into a production-ready requirement state. Its job is to recover enough supported project meaning that Flow 3 can write the PRD without inventing product behavior.

## Outcome

Flow 2 maintains only the state needed to resume and prove current project truth:

```text
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
work/review.md                 only when user decisions need a readable summary
```

The mandatory Simple Chat Preview is **not** stored as another artifact. Persist only material corrections/approvals needed for continuation.

Do not create another topology map, coverage checklist, dependency graph, recovery schema, or preview document.

## 1. Bootstrap and source authority

```text
user project name OR strongest authoritative title
→ derive stable project slug
→ reuse clearly matching active workspace OR create workspace/active/<slug>/
→ preserve supplied originals
→ inventory current evidence
```

Do not ask the user for slugs, folders, internal IDs, YAML structure, or renderer files.

Every material source receives one stable `SRC-###` entry. Use these source roles:

- `authoritative` — defines project facts or requirements;
- `supporting` — explains or supplements authoritative evidence;
- `reference` — demonstrates structure/quality; does not define project facts by default;
- `generated` — prior generated output for continuity/conflict evidence only.

Use `status: superseded` only when the whole source is no longer authoritative. Resolve partial changes at requirement/claim level.

### Reading depth

Read by authority and relevance, not by file count:

```text
inventory
→ triage authority/relevance
→ inspect material authoritative evidence deeply enough for current scope
→ inspect supporting/reference/generated evidence only as needed
```

Use:

```yaml
inspection: full
```

when no uninspected portion is expected to materially alter the current scope, or:

```yaml
inspection: targeted
inspection_scope: Objective 2 timing and reset behavior
```

for bounded inspection.

The goal is **complete production meaning, not complete byte consumption**.

### Material user instructions

A current user instruction can be authoritative without a file. Persist coherent material instruction sets as source entries instead of relying on chat history or creating fake source files:

```yaml
id: SRC-007
type: instruction
role: authoritative
origin: user
summary: Objective 2 uses three checkpoints; collapse begins only in checkpoint 3.
inspection: full
```

Do not create one source entry per sentence.

## 2. Recover requirement truth

Recover explicit facts, rules, constraints, exclusions, removals, topology, and terminology before filling gaps.

Negative rules are first-class requirements:

```text
remove
no longer use
do not use
only
must not
replaced by
```

An approved exclusion must prevent lower-authority old material or references from silently reintroducing removed behavior.

Create one `REQ-###` per meaningful production rule, constraint, conflict, exclusion, topology rule, or unresolved decision that must survive into PRD/acceptance. Do not mirror every source sentence.

Normal requirement:

```yaml
id: REQ-001
area: gameplay
statement: Player must cross the bridge before collapse.
provenance: [SRC-001]
impact: high
```

Sparse defaults remain implicit unless a non-default condition matters:

```text
evidence_status → supported
recovery_class  → none
approval_status → not_required
affects         → []
resolution      → absent
```

Use `affects` only when it materially clarifies cross-role impact; do not duplicate one rule into several paraphrased requirements just to fill role buckets.

### Recover topology

Before readiness, the project must have enough supported structure for Flow 3 to know:

```text
project experience
├── shared/global rules
├── ordered gameplay packages/stages
├── dependencies/transitions
└── ending/final result or handoff
```

Store material topology as normal requirements. Do not create a separate topology artifact.

### Normalize terminology

When source variants may refer to the same concept, resolve them by authority:

```text
Power Core / Energy Core / Generator Core
→ same concept: keep one canonical approved name
→ different concepts: preserve the distinction
→ unclear and material: resolve before readiness
```

Do not synonym-cycle approved names during drafting.

## 3. One production-readiness pass

After explicit recovery, perform **one integrated pass** over the material requirements. This is reasoning, not a form to populate and not a sequence of independent approval stages.

| Concern | What must be clear when applicable |
|---|---|
| Topology | package order, shared/local ownership, dependencies, transitions, ending/final result |
| Gameplay | purpose/objective, start, player action/feedback, completion/end, failure/retry/recovery, result |
| Level Design | required areas/objects/routes, relationships, readability, known spatial constraints, gameplay function |
| Developer | activation, state/progression, timing/quantities, completion/result, data, interruption/reset, handoff |
| Lifecycle | precondition → trigger → active behavior → success/fail/interruption → result → retry/reset |
| Quantitative coherence | related timings, counts, capacities, scoring inputs/weights, repeated numeric rules agree |
| Global/local coherence | shared defaults remain shared; local exceptions are explicit and supported |
| Known constraints | authoritative platform/capacity/production limits do not silently conflict with required behavior |
| Operational clarity | two competent roles should not reasonably produce materially different behavior from the same requirement |

Only inspect concerns that actually apply. **Irrelevant or intentionally open detail is not a gap.** Do not invent dimensions, timings, metrics, architecture, animations, cooldowns, or mechanics because a category exists.

### Cross-surface consistency for mature PRD sources

A single authoritative or mature PRD file is **not automatically internally consistent**. Before `ready_for_prd`, compare repeated material claims across the source surfaces that describe the same package, especially:

```text
Gameplay Flow
↔ Gameplay Overview
↔ Level Design
↔ Developer
```

Check only high-impact meaning that is actually repeated: objective/progression count, trigger or timing, mechanic/state change, fail/retry/recovery, scoring/result, reward/handoff, interruption/reset, and other rules that would make two production roles build different behavior.

Do not compare wording literally and do not create a second coverage artifact. This is one bounded consistency sweep inside the existing readiness pass.

If two same-authority surfaces materially disagree and no stronger approved authority resolves them, record the conflict and use `needs_decision` / `blocked` as appropriate. Do **not** choose whichever surface looks newer, more detailed, or easier to fit into the Golden template, and do not use Completion to select between two plausible product behaviors.

### Cross-role implications

A material rule may imply work beyond its source sentence. Recover only necessary supported implications.

Example:

```text
Source: Bridge collapses when the timer expires.

Gameplay     → player must cross before the approved collapse condition.
Level Design → a readable collapsible route must exist.
Developer    → the route changes state when the timer condition expires.
Reset        → if retry is already approved, the collapsed state must be restorable.
```

Record an implication separately only when it is independently actionable. Otherwise keep one complete rule with `affects`.

### Materiality test

A missing detail is material only when leaving it unresolved would force a production role to choose product behavior/scope or would change player experience, build scope, runtime behavior, scoring/result, timing, handoff, interruption, or reset.

If production can proceed safely while a detail remains intentionally open, keep it open. Do not manufacture a question or fake requirement.

## 4. Resolve only real material gaps

When a material issue remains, first frame the actual problem:

```text
observed ambiguity/conflict
→ production/player consequence
→ constraints that must remain true
→ desired outcome supported by project intent
```

Then use the Resolution Ladder:

```text
1. Existing authority resolves it
   → recover the answer.

2. One necessary evidence-backed completion exists
   → Completion.

3. Several designs are possible and one is materially better supported
   → Proposal with one recommendation.

4. Options are genuinely balanced
   → Proposal with the smallest useful tradeoff set, normally two options.

5. No responsible resolution can be formed
   → Blocked / direct user decision.
```

### Safe Completion

Use Completion only when all are true:

- it follows from explicit evidence or a necessary production implication;
- one reasonable answer exists at the abstraction needed by the PRD;
- it does not select between plausible product/design options;
- it does not invent unsupported quantities, timings, scoring, names, objects, architecture, or decorative detail;
- its provenance remains explainable.

Otherwise use Proposal or Blocked when the issue is material.

Use **Recommended** only when evidence, project goals, or constraints actually favor one option. Do not manufacture confidence to reduce user questions.

### Advisory noise

Not every quality concern blocks readiness:

- **must resolve** — material ambiguity/conflict;
- **material concern** — non-blocking risk worth surfacing;
- **optional improvement** — keep internal by default unless requested or unusually valuable.

These are communication priorities, not new state fields.

## 5. Propagate resolved meaning

A recovered Completion or approved Proposal must update every actually affected meaning, not only the sentence where it originated.

Check as applicable:

```text
requirement
→ topology / shared-vs-local ownership
→ Gameplay
→ Level Design
→ Developer
→ timing / quantities / scoring
→ transition / handoff
→ retry / interruption / reset
```

Reuse existing REQs and `affects` where useful. Do not create a dependency graph.

If one decision controls several symptoms, group them for the user as one solution package while keeping independently traceable requirements separate internally.

## 6. Simple Chat Preview and user approval

After recovery/problem-solving is complete enough to explain the project coherently, **show one Simple Chat Preview before initial `ready_for_prd`**. This is the user checkpoint between UNDERSTAND and BUILD PRD.

The preview should be easy to scan and should explain the project **objective by objective**, not expose the internal recovery machinery.

Default format:

```text
Project Overview
<short project/session/journey summary>

Objective N — <Name>

Tujuan
<what the player must accomplish>

Apa yang Player Lakukan
- main chronological actions
- visible/system response only when needed to understand the gameplay

Hasil
<valid completion/result/transition>

Level Design
- material build-owned meaning only

Developer
- material runtime/data/reset meaning only

Perlu Konfirmasi
- only unresolved material decisions; omit when none
```

Rules:

- keep wording direct and simple;
- preserve official names, numbers, timings, formulas, mechanics, triggers, and uncertainty;
- do not dump `SRC-###`, `REQ-###`, YAML, confidence scores, provenance, Golden DOM terms, or validator jargon;
- do not label every recovered sentence as “AI added”; present one coherent recovered gameplay model;
- do not hide a real source conflict behind a polished summary;
- use one short **Global Rules** block only when shared rules materially affect all objectives;
- do not turn the preview into a second PRD or a 30-page-equivalent chat response.

### When decisions remain

If unresolved material decisions exist, keep the relevant objective readable and place only the unresolved items under `Perlu Konfirmasi`.

Use the bounded decision pattern:

```text
Masalah
Saran — only when one option is genuinely recommended
Kenapa
Dampak
Alternatif — only when meaningful
```

When no option is clearly favored, use `Pilihan` + concise tradeoff instead.

Status remains `needs_decision` / `blocked` as appropriate. After the user resolves the issue:

1. persist the user decision as authoritative instruction/requirement state;
2. rerun only affected readiness checks;
3. re-preview only the affected objective(s)/global slice unless the correction is broad.

### When no decisions remain

Even when AI recovery resolved everything responsibly, **do not skip the initial preview**.

Before approval, keep Flow 2 non-ready, for example:

```yaml
status: audit_in_progress
ready_for_prd: false
preview_approved: false
next_step: Await Simple Chat Preview approval or corrections.
```

After explicit user approval:

```yaml
status: ready_for_prd
ready_for_prd: true
preview_approved: true
next_step: Build canonical PRD content.
```

Natural-language approval is sufficient. Do not ask the user to type a special command.

If the user corrects the preview, persist the material correction, re-run only invalidated reasoning, then show the corrected affected preview before setting `preview_approved: true`.

### Bounded revision

A bounded approved revision does not require a full-project preview replay.

```text
approved change
→ update affected meaning
→ preview affected objective/global slice when interpretation changed
→ approval/correction of that slice
→ continue downstream revision
```

If the user's current instruction already states the complete intended bounded result unambiguously, that instruction may serve as approval for that slice. Do not manufacture an extra confirmation step.

## 7. Intake state and readiness

Keep one status and one practical next step.

```yaml
status: audit_in_progress
ready_for_prd: false
preview_approved: false
next_step: Complete remaining requirement recovery.
```

Positive readiness remains explicit and now includes preview approval:

```yaml
status: ready_for_prd
ready_for_prd: true
preview_approved: true
next_step: Build canonical PRD content.
```

Statuses remain:

```text
collecting_sources
audit_in_progress
needs_decision
blocked
ready_for_prd
```

Do not add a `preview_ready` status; preview approval is a small readiness field, not a new workflow state machine.

Flow 2 is ready only when:

- material evidence is inventoried and inspected deeply enough for current scope;
- material user instructions are persisted;
- explicit rules and exclusions are recovered;
- topology and terminology are sufficient for Flow 3;
- the integrated readiness pass has no unresolved material contradiction/gap, including contradictions between repeated claims inside one authoritative source;
- every Completion passes the safe-completion rule;
- every material requirement traces to evidence/approved state;
- unresolved material Proposal/Blocked items do not remain;
- the Simple Chat Preview has been shown for the initial project scope;
- user corrections, if any, have been propagated to affected meaning;
- `preview_approved: true` truthfully records user approval;
- `intake-state.yaml` truthfully reports `ready_for_prd: true`.

When this gate passes, **stop Flow 2**. Do not keep generating redesign ideas, optional metrics, extra alternatives, or hypothetical edge cases.

## Revision fast path

A bounded approved revision does not restart intake when project identity and authority remain clear:

```text
approved change
→ persist material instruction when needed
→ update affected requirements/exclusions/topology/terminology
→ rerun only invalidated readiness concerns
→ propagate affected meaning
→ preview only affected objective/global slice when interpretation changed
→ continue downstream revision after that slice is approved
```
