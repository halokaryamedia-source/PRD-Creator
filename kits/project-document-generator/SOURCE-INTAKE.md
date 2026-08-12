# Source Intake & Requirement Recovery

Flow 2 turns uneven project material into a **complete reviewable project model**. Its job is to recover supported meaning, identify what the production document still needs, fill missing/conflicting material detail with explicit AI proposals when necessary, and obtain user approval through the Simple Chat Preview before Flow 3 writes the canonical PRD.

Source-backed meaning and AI-proposed meaning must remain distinguishable internally until preview approval. The AI may propose product/design/development decisions; it must not falsely label those proposals as facts from the source.

## Outcome

Flow 2 maintains only the state needed to resume and prove current project truth:

```text
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
work/review.md                 only when a readable decision summary materially helps
```

The mandatory Simple Chat Preview is **not** stored as another artifact. Persist only material corrections, proposal/approval state, and decisions needed for continuation.

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

Create one `REQ-###` per meaningful production rule, constraint, conflict, exclusion, topology rule, or proposed/approved material decision that must survive into PRD/acceptance. Do not mirror every source sentence.

Normal source-backed requirement:

```yaml
id: REQ-001
area: gameplay
statement: Player must cross the bridge before collapse.
provenance: [SRC-001]
impact: high
```

A material AI proposal remains explicit until preview approval:

```yaml
id: REQ-014
area: gameplay
statement: The first target appears after 90 seconds of free experimentation.
evidence_status: conflict
recovery_class: proposal
approval_status: pending
resolution: Recommended preview default; preserves experiment-before-explanation.
provenance: [SRC-002, SRC-003]
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

Before preview, the project must have enough supported or proposed structure to explain:

```text
project experience
├── shared/global rules
├── ordered gameplay packages/stages
├── dependencies/transitions
└── ending/final result or handoff
```

Store material topology as normal requirements. Do not create a separate topology artifact.

### Normalize terminology

When source variants may refer to the same concept, resolve them by authority when possible:

```text
Power Core / Energy Core / Generator Core
→ same concept: keep one canonical approved name
→ different concepts: preserve the distinction
→ unclear and material: select one preview proposal and surface it when useful
```

Do not synonym-cycle approved names during drafting.

## 3. One production-completeness pass

After explicit recovery, perform **one integrated pass** over material meaning. This is reasoning, not a form to populate and not a sequence of independent approval stages.

| Concern | What must be clear when applicable |
|---|---|
| Topology | package order, shared/local ownership, dependencies, transitions, ending/final result |
| Gameplay | purpose/objective, start, player action/feedback, completion/end, failure/retry/recovery, result |
| Level Design | required areas/objects/routes, relationships, readability, known spatial constraints, gameplay function |
| Developer | activation, state/progression, timing/quantities, completion/result, data, interruption/reset, handoff |
| Lifecycle | precondition → trigger → active behavior → success/fail/interruption → result → retry/reset |
| Quantitative coherence | related timings, counts, capacities, scoring inputs/weights, repeated numeric rules agree |
| Global/local coherence | shared defaults remain shared; local exceptions are explicit and supported/proposed |
| Known constraints | authoritative platform/capacity/production limits do not silently conflict with required behavior |
| Operational clarity | two competent roles should not reasonably produce materially different behavior after preview approval |

Only inspect concerns that actually apply. Optional/irrelevant detail is not a reason to inflate scope.

### Golden-guided completeness

Use the **Reverse-derived Golden fill map** in `CONTENT-CONTRACT.md` as the finite checklist for what the PRD must eventually be able to answer.

Golden supplies **questions and placement**, not project facts.

For example, for each gameplay package the underlying model must be able to answer the Golden responsibilities for:

```text
Gameplay Overview
- context
- main objective
- result
- purpose
- gameplay time
- starting condition
- end condition
- fail / setback / recovery
- scoring meaning
- five high-level gameplay beats

Level Design
- spatial/build overview
- four useful design-flow beats
- build-owned objects/areas/constraints/functions
- highest-risk build notes

Developer
- runtime overview
- setup/initialization
- core execution/validation
- result/data/completion
- interruption/recovery/reset/handoff
- highest-risk runtime notes
```

Global Development and Gameplay Flow are checked the same way against their Golden slot meanings.

When source evidence does not answer a material Golden question, **do not leave the future slot empty just because the source is incomplete**. Create one project-consistent AI proposal at the abstraction needed by the PRD. If a detail is genuinely not applicable, record the explicit no/not-applicable meaning instead.

Do not copy Aftershock-specific mechanics, counts, timings, names, or implementation facts from the Golden. The reference shows what kind of answer belongs there, not what the answer should be.

### Cross-surface consistency for mature PRD sources

A single authoritative or mature PRD file is **not automatically internally consistent**. Before the preview, compare repeated material claims across source surfaces that describe the same package, especially:

```text
Gameplay Flow
↔ Gameplay Overview
↔ Level Design
↔ Developer
```

Check only high-impact meaning that is actually repeated: objective/progression count, trigger or timing, mechanic/state change, fail/retry/recovery, scoring/result, reward/handoff, interruption/reset, and other rules that would make two production roles build different behavior.

Do not compare wording literally and do not create a second coverage artifact.

If same-authority surfaces materially disagree and no stronger approved authority resolves them:

1. record the conflict internally;
2. identify the project constraints/intended experience that still hold;
3. select **one recommended preview resolution**;
4. mark that choice as Proposal + pending approval;
5. propagate the proposal across the preview model so the objective remains complete.

Do not silently call the selected side source truth. Do not choose merely because one surface is newer-looking, more detailed, or easier to fit into Golden. Choose based on project coherence, user direction, gameplay intent, production feasibility, and the Golden slot responsibility.

### Cross-role implications

A material rule may imply work beyond its source sentence. Recover necessary supported implications, and propose missing implementation meaning when the Golden role surface requires it.

Example:

```text
Source: Bridge collapses when the timer expires.

Gameplay     → player must cross before the collapse condition.
Level Design → a readable collapsible route must exist.
Developer    → the route changes state when the timer condition expires.
Reset        → if retry is part of the intended flow, the collapsed state must be restorable.
```

Record an implication separately only when it is independently actionable. Otherwise keep one complete rule with `affects`.

### Materiality test

A missing detail is material when leaving it unresolved would force a production role to choose product behavior/scope or would change player experience, build scope, runtime behavior, scoring/result, timing, handoff, interruption, or reset.

Material meaning should be **filled for preview** using authority, Completion, or Proposal. Optional decorative detail may stay open when production does not need it and Golden does not require a meaningful answer.

## 4. Complete material gaps for preview

When a material issue remains, first frame the real problem:

```text
observed gap/conflict
→ production/player consequence
→ constraints that must remain true
→ desired outcome supported by project intent
→ concrete preview resolution
```

Then use this bounded ladder:

```text
1. Existing authority resolves it
   → recover the answer.

2. One necessary evidence-backed completion exists
   → Completion.

3. Several designs are possible and one is materially better supported
   → Proposal using the best-supported option.

4. Options are genuinely balanced
   → choose one reasonable preview default as Proposal;
      mention an alternative only if it materially helps review.

5. Source is silent but Golden requires a material answer
   → create a practical project-consistent Proposal at PRD abstraction level.

6. No responsible proposal can be formed
   → Blocked only when the answer depends on a genuinely external/user-only fact
      or every plausible choice violates a known constraint.
```

The objective is **not** to minimize AI decisions. The objective is to give the user a complete coherent model to approve or correct in one pass.

### Completion vs Proposal

Use Completion only when all are true:

- it follows from explicit evidence or a necessary production implication;
- one reasonable answer exists at the abstraction needed by the PRD;
- it does not select between plausible product/design options;
- its provenance remains explainable.

Use Proposal when the AI is actually choosing a product/design/development default, including proposed quantities, timings, recovery behavior, scoring behavior, names, objects, or implementation rules that the source did not settle.

A Proposal may be concrete. It is allowed to make the preview production-ready enough to review. Its protection is **pending approval**, not artificial vagueness.

Do not manufacture fake source evidence or hide uncertainty. A proposal can be useful and specific while still being truthfully labeled internally as a proposal.

### Advisory noise

Not every quality idea belongs in the preview model:

- **material completion** — fill it;
- **material conflict** — choose/propose a coherent resolution and surface it when useful;
- **optional improvement** — keep internal by default unless requested or unusually valuable.

These are communication priorities, not new state fields.

## 5. Propagate recovered and proposed meaning

A recovered Completion or proposed decision must update every actually affected preview-model surface, not only the sentence where it originated.

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

If one proposal controls several symptoms, choose it once and propagate it consistently. Keep independently traceable requirements separate internally.

Before preview approval, Proposal remains pending. After the user approves the complete preview, promote the represented pending proposals to approved decision/requirement state unless the user specifically corrected/rejected them.

## 6. Simple Chat Preview and user approval

After the project model is complete enough to review coherently, **show one Simple Chat Preview before initial `ready_for_prd`**. This is the user checkpoint between UNDERSTAND + COMPLETE and BUILD PRD.

The preview should be easy to scan and explain the project **objective by objective**, not expose internal recovery machinery.

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
- material build-owned meaning

Developer
- material runtime/data/reset meaning

Saran AI
- optional: only important material choices the AI filled and that benefit from being called out
```

Every displayed objective must be filled. The preview is a readable summary of a more detailed underlying model, not a substitute for the Golden PRD.

Rules:

- keep wording direct and simple;
- preserve official source names and known source numbers/timings/mechanics;
- AI-proposed values may be concrete, but remain pending internally until approval;
- do not dump `SRC-###`, `REQ-###`, YAML, confidence scores, provenance, Golden DOM terms, or validator jargon;
- do not label every sentence as “AI added”; present one coherent proposed project model;
- do not hide a material source conflict by pretending the chosen proposal came from the source;
- use `Saran AI` only for material proposal choices where visibility helps the user review; most proposal detail can simply appear naturally in the complete model;
- use one short **Global Rules** block only when shared rules materially affect all objectives;
- do not turn the preview into a second PRD or a 30-page-equivalent chat response.

### If an exceptional blocker remains

A `Perlu Konfirmasi` block is reserved for the rare case where **no responsible default can be proposed** because the missing answer is genuinely external/user-only or every plausible choice violates a known constraint.

This is not the normal response to incomplete design. Normal incomplete design gets a concrete AI proposal first.

### Approval behavior

Before approval, keep Flow 2 non-ready, for example:

```yaml
status: audit_in_progress
ready_for_prd: false
preview_approved: false
next_step: Await Simple Chat Preview approval or corrections.
```

User approval of the complete preview means:

- source-backed meaning remains source-backed;
- represented pending AI proposals become approved project decisions;
- rejected/corrected proposals are replaced by the user's authoritative correction;
- only affected requirement surfaces are rechecked after a correction.

After approval and proposal promotion:

```yaml
status: ready_for_prd
ready_for_prd: true
preview_approved: true
next_step: Build canonical PRD content.
```

Natural-language approval is sufficient. Do not ask the user to type a special command.

If the user corrects the preview, persist the material correction, update/replace affected pending proposals, rerun only invalidated reasoning, then show the corrected affected preview before setting `preview_approved: true`.

### Bounded revision

A bounded approved revision does not require a full-project preview replay.

```text
approved change
→ update affected meaning
→ Golden-guided completeness check on affected slice
→ fill newly missing detail with proposal if needed
→ preview affected objective/global slice when interpretation changed
→ approval/correction of that slice
→ continue downstream revision
```

If the user's current instruction already states the complete intended bounded result unambiguously, that instruction may serve as approval for that slice. Do not manufacture an extra confirmation step.

## 7. Intake state and readiness

Keep one status and one practical next step.

Before preview approval:

```yaml
status: audit_in_progress
ready_for_prd: false
preview_approved: false
next_step: Present/resolve the complete Simple Chat Preview.
```

Positive readiness remains explicit:

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

`needs_decision` should be rare in initial production because the AI is expected to propose a complete default. Use it when user input is actually required rather than when the AI is merely uncertain between reasonable design choices.

Flow 2 is ready only when:

- material evidence is inventoried and inspected deeply enough for current scope;
- material user instructions are persisted;
- explicit rules and exclusions are recovered;
- topology and terminology are sufficient;
- every Golden-required material question has source-backed, explicit no/not-applicable, approved Completion/Proposal, or justified Blocked meaning;
- cross-surface conflicts have a coherent proposed/approved resolution;
- proposed meaning is propagated across affected Gameplay / Level Design / Developer / lifecycle surfaces;
- the complete Simple Chat Preview has been shown for the initial project scope;
- user corrections, if any, have been propagated;
- all material proposals represented by the approved preview are promoted from pending to approved;
- no genuine Blocked item remains;
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
→ Golden-guided completeness check on invalidated scope
→ fill missing material detail with Proposal where needed
→ propagate affected meaning
→ preview only affected objective/global slice when interpretation changed
→ continue downstream revision after that slice is approved
```
