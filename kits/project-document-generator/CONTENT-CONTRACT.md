# Golden Mandatory PRD Contract

`work/content.md` is the human-readable source of truth for Flow 3. `render-data.json` and `final.html` are derived.

This file is the **single semantic owner** for the gameplay PRD family. Flow 2, Flow 3, rendering, and Flow 4 refer here instead of keeping separate Golden checklists.

## Core rule

The approved Golden Sample defines the **minimum document function** for this gameplay PRD family.

```text
current project facts + approved decisions
→ resolve every mandatory concern
→ fill the fixed Golden surfaces
→ humanize the explanation
→ render without dropping supported meaning
```

A generated PRD may contain more project-specific detail than the Golden Sample when the project needs it. It may not contain fewer required Golden functions.

**No filler does not mean minimal document.** The target is complete material production information with no useless repetition.

## Mandatory-slot state

Every mandatory concern resolves to one of these meanings before handoff:

| State | Meaning |
|---|---|
| **Defined** | Project authority defines the behavior/value. |
| **Explicit No** | The concern exists and the correct rule is explicitly negative, e.g. `No Objective Score`, `No hard timeout`, `No permanent fail`. |
| **Not Applicable** | The concern genuinely does not apply; state why when silence would be ambiguous. |
| **Blocked** | The concern is material but cannot be resolved responsibly; Flow 2 must not declare `ready_for_prd`. |

A mandatory slot never disappears silently because source or render data omitted it. `missing` is not a fifth state.

## Fixed document blueprint

For `N` gameplay packages:

```text
01 Overview

02 Gameplay Flow
   02A The Journey Begins
   02B+ one full Gameplay Flow page for every package, in package order

03 Development
   Development Overview
   Session & Runtime System
   Data, Recovery & Reset
   Gameplay Package Integration

04+ Gameplay Packages
   for every package:
   1. Gameplay Overview
   2. Level Design
   3. Developer
```

The number of package pages follows the project. The four Global Development functions do not collapse into one generic page.

Expected page count for `N` packages:

```text
Overview                         1
Gameplay Flow                    1 + N
Global Development               4
Gameplay role pages              3N
-----------------------------------
Total                            6 + 4N
```

This count is a shell consequence, not a quality score or word-count target.

## 1. Overview

Overview gives a new team member enough project context before package detail.

Mandatory functions:

- **Project Context** — what the experience is and why the player is there;
- **Main Experience** — the journey at one readable level of abstraction;
- **Document Control** — version, document scope, and intended production use;
- **Session Model** — player/session/arena relationship or explicit project-equivalent rule;
- **Target Playtime** — target duration or explicit negative/unspecified production rule;
- **Game Structure** — stage/package structure and scored/non-scored relationship at project level;
- **Complete Gameplay Journey** — ordered journey from opening to ending;
- **Main Systems** — shared systems a new reader must understand before local implementation.

Do not use a mutable approval status inside rendered Document Control. Flow 4 lifecycle state remains in acceptance/handoff state so approving the same PRD does not require a cosmetic rerender.

Document Control is metadata, not a warning/note surface. Main Systems is production meaning, not metadata; presentation should keep those roles visually distinct.

Terms Used appears only when project-specific production terminology materially helps the reader.

## 2. Gameplay Flow — The Journey Begins

The opening page explains:

- the player's starting situation;
- what the player first sees/understands;
- why the journey begins;
- the first instruction, cue, or world response that matters;
- the first playable destination;
- the transition into the first package.

## 3. Gameplay Flow — every package

Full Gameplay Flow is the **chronological player story for production**, not a developer checklist or condensed implementation table.

Explain the applicable beats:

```text
entry / current situation
→ what the player sees or understands
→ NPC / instruction / system cue
→ what the player does
→ how the world/system responds
→ setback / recovery when relevant
→ what state, access, item, or knowledge changes
→ result
→ transition to the next stage
```

Before the detailed beats, the reader should be able to orient quickly around three questions using already-approved project truth:

```text
What is the player trying to achieve here?
Where did the player come from?
Where does completion take the player next?
```

This orientation is a reading aid, not a new product requirement. Do not invent a goal, previous stage, or next destination to populate it.

Keep this page focused on player experience and visible consequences. Exact durability rules, internal counters, duplicate-prevention logic, storage mechanics, and similar implementation detail belong in Gameplay Information or Developer unless the player directly experiences them.

Use enough beats to make the experience understandable without reopening source. Do not invent dialogue, lore, cinematics, animation, quantities, or mechanics to make the page feel richer.

## 4. Global Development — four fixed functions

Global Development uses these fixed display names and stable functions:

1. **Development Overview**
2. **Session & Runtime System**
3. **Data, Recovery & Reset**
4. **Gameplay Package Integration**

Each page contains:

- Overview;
- Development Flow;
- Development Requirements;
- **Critical Constraints & Notes**.

The last table column is **Expected System Result**: the observable runtime/system outcome produced by the requirement.

### Development Overview owns

Project-wide implementation topology: package order, shared ownership, major dependencies, common handoff, and overall development sequence.

### Session & Runtime System owns

Shared runtime/session behavior: player/session/arena ownership, shared state/permissions, common activation/routing, concurrency/isolation, and other project-wide runtime rules.

### Data, Recovery & Reset owns

Shared persistence and recovery behavior: score/final-result storage, telemetry/export, pause/interruption/disconnect, recovery, reset/cleanup, and reusable-arena/session release where applicable.

When the project has a Final Total or another aggregate result, this page owns the **Final Result Contract**: required inputs, invalid/missing-input behavior, formula, rounding when defined, save boundary, and duplicate-prevention rule. Do not scatter the aggregate rule across packages.

### Gameplay Package Integration owns

How packages operate as one production system: package lifecycle, shared conventions, package-to-package handoff, and cross-package implementation responsibilities.

Use explicit `Not Applicable` only when a concern genuinely does not apply. Do not hide a shared rule inside one package when multiple packages depend on it.

## 5. Gameplay Overview — every package

Every Gameplay Overview contains:

- Gameplay Context;
- Main Objective;
- Result;
- Gameplay Information;
- **Objective Sequence**.

### Full Gameplay Flow vs Objective Sequence

These surfaces have different jobs:

```text
Full Gameplay Flow
→ tells the chronological player story with context, feedback, consequence, and transition

Objective Sequence
→ gives the team a short scan-friendly sequence of the package's major playable beats
```

Objective Sequence should not repeat the full narrative paragraph-by-paragraph.

### Gameplay Information — fixed rows

Every package resolves and shows:

1. Game Purpose
2. Gameplay Time
3. Starting Condition
4. End Condition
5. **Failure / Retry / Recovery**
6. **Result / Scoring Model**

Use explicit negative wording where appropriate:

```text
No hard timeout. The package continues until ...
No permanent fail. A setback returns the player to ...
No Objective Score. Completion only opens ...
```

Do not remove a row because the correct rule is negative.

## 6. Level Design — every package

Every Level Design page contains:

- Level Design Overview;
- Design Flow;
- Build Requirements;
- **Critical Constraints & Notes**.

Build Requirements columns:

```text
No. | Object | Area / Spatial Constraint | Build and Visual Requirements | Gameplay Function
```

`Area / Spatial Constraint` may contain exact dimensions when defined, or topology/clearance/relationship constraints when those are the actual production requirement. When authority intentionally leaves exact size open, use a neutral explicit value such as `Not specified — follow approved layout`; never invent dimensions.

Carry all material build-owned meaning supported by the project, including when applicable:

- required areas/sub-areas;
- objects, machines, markers, hazards, interactables;
- route/spatial relationships;
- visible destination, sightlines, readability, warnings, guidance;
- known dimensions/clearance constraints;
- safe landing/recovery space;
- player access and interaction placement;
- entry/exit/reset boundaries;
- build/visual requirements;
- gameplay function;
- constraints that prevent a materially wrong build.

A Level Designer must not need original source to rediscover a material build requirement that belongs here.

## 7. Developer — every package

Every Developer page contains:

- Developer Overview;
- Development Flow;
- Development Requirements;
- Scoring / Result contract inside the requirement hierarchy;
- Reset / interruption behavior;
- **Critical Constraints & Notes**;
- **Acceptance & Verification**.

Development Requirements columns:

```text
No. | Setup | Development Requirements | Expected System Result
```

Carry all material runtime-owned meaning supported by the project, including when applicable:

- activation/precondition;
- interaction behavior;
- progression/state changes;
- quantities/timing;
- success/completion;
- Objective Score or explicit No Objective Score;
- score/result relationship to final result;
- player-facing score/result display;
- telemetry/export/data behavior;
- invalid/no-score behavior;
- pause/interruption/disconnect;
- retry/reset/cleanup;
- transition/handoff;
- implementation constraints that prevent materially wrong behavior.

### Developer Flow reading contract

Development Flow must preserve the lifecycle sequence **and** keep different kinds of information visibly distinguishable when they exist:

```text
Trigger / entry condition
→ System Behavior
→ Data / state affected
→ Expected Result
```

Do not flatten these fields into one punctuation-heavy sentence merely to save space. A short step may omit a genuinely non-applicable field, but it must not hide material trigger, data, or result meaning that already exists.

A Developer must not need original source to rediscover a material runtime requirement that belongs here.

## 8. Acceptance & Verification — mandatory per package

Acceptance & Verification is the package-level **definition of done**. It is rendered on the Developer page so the package closes with observable production outcomes, but it covers the whole package—not only code.

Use concise, project-specific, observable statements that prove the important behavior is correct. Cover the material acceptance concerns that actually apply, such as:

- valid entry/activation;
- chronological progression/completion;
- critical Level Design readability or spatial behavior;
- score/result creation and no-score behavior;
- interruption/recovery/reset;
- package handoff;
- session isolation or other critical shared rules.

Do not turn this into a QA test-case appendix. Do not add generic statements such as `works correctly` or `matches the design`. Each criterion must state an observable condition or result.

## Scoring / Result contract — mandatory for every package

Every package answers explicitly:

```text
1. Internal result
   Does the package calculate/store an Objective Score or only completion?

2. Calculation / completion rule
   How is that result determined?

3. Final-result relationship
   How does this package affect the project/session final result?

4. Player-facing display
   What score/result is shown or intentionally not shown?

5. Telemetry / export
   What result is exported/logged or intentionally excluded when such systems exist?
```

### Scored package

State `Objective Score` and preserve applicable project-defined details such as score name/scale, components/weights, timer boundaries, bonus/reduction behavior, invalid/no-score condition, duplicate prevention, final-result relationship, display rule, export rule, and exact formula when product-critical.

Numeric component weights total 100% unless approved authority explicitly defines another model.

### Non-scored package

State visibly:

```text
No Objective Score
```

Then define valid completion, recorded completion/progress data, interruption behavior, duplicate prevention when required, handoff result, final-result relationship, player-facing result behavior, and telemetry/export behavior.

### Never broaden negative rules

These remain distinct:

```text
No Objective Score
Do not display score to the player
Do not export score in telemetry
```

One does not imply either of the others.

## Critical Constraints & Notes

This block is not a dumping ground.

A rule that changes the primary build/runtime behavior belongs in Build Requirements or Development Requirements. Use Critical Constraints & Notes only for warnings, cross-references, edge constraints, or production reminders that prevent mistakes but do not deserve a duplicate requirement row.

## Terms Used and inline Glossary Index

`packages[].terms` is the **canonical package term index** for this gameplay PRD family.

A package term may define:

- stable key;
- canonical label;
- concise production definition;
- aliases when the same approved term appears in another written form;
- role visibility when the term is relevant only to Gameplay, Level Design, or Developer readers.

The same package term index serves both reading surfaces:

```text
inline occurrence in package-owned prose
→ subtle glossary highlight / tooltip

Terms Used block
→ local index of terms relevant to that page/role
```

Do not maintain a second copy of package terminology inside `gameplay_flow[].terms`. Full package Gameplay Flow uses the owning package's term index. `The Journey Begins` may carry opening-specific terms only when they do not belong to a gameplay package.

The Terms Used block itself is an index and must not recursively highlight its own definitions.

Use glossary highlighting as a comprehension aid, not decoration. Highlight only approved project/production terms; do not turn ordinary nouns into glossary entries merely because they repeat often.

## Terminology style

- Title Case is reserved for canonical project/system/object names such as `Beacon Core`, `Assigned Arena`, or `Objective Score` when those are approved names.
- Generic concepts stay sentence case.
- Do not synonym-cycle approved names to make prose feel varied.
- Technical IDs, state names, formulas, coordinates, timers, and API/code names remain exact.

## Language quality

English-only remains the default production output.

Enable bilingual `en + id` only when the complete user-visible Indonesian copy is intentionally translated and reviewable. Structural presence of an `id` value is not evidence that the translation is professionally written. Do not expose machine-like mixed English/Indonesian copy merely because the renderer supports the language switch.

## Source fidelity and authority

Project meaning follows repository authority:

1. current explicit user instruction;
2. approved project decisions;
3. current authoritative project source;
4. normalized requirement state;
5. reference/Golden material for document function/quality only.

A filename containing `FINAL` does not override higher-authority current instruction or approved decisions. Golden supplies document function, not project facts.

## Flow 2 responsibility

Before `ready_for_prd`, Flow 2 resolves every material mandatory concern as `Defined`, `Explicit No`, `Not Applicable`, or `Blocked` using normal requirement state—no second Golden checklist artifact.

Recurring interpretation failures to prevent:

- display/export prohibition becoming `No Objective Score`;
- missing source detail being treated as permission to remove a mandatory surface;
- one package rule becoming global without authority;
- Golden example facts being copied as project truth;
- material build/runtime implications disappearing during summarization;
- acceptance criteria being invented when the underlying material behavior is still unresolved.

## Flow 3 authoring rule

Flow 3 fills the fixed shell using **minimum complete production detail**.

Do not ask how little a page can contain and still look valid. Ask what supported material meaning that page must carry so its reader can work correctly without reopening source.

### Humanize: close the reader's next question

After meaning is complete, apply one bounded Humanize pass. The governing test is:

> **Before moving to the next idea, has this section answered the next reasonable production question created by the previous sentence?**

Prefer an explicit causal sequence when the subject is behavioral:

```text
context / trigger
→ action or system behavior
→ response / state change
→ consequence / result
→ next state or handoff when relevant
```

Examples of questions that should not be left implicit when the approved meaning already answers them:

```text
When does this start?
What does the player do?
What does the system do in response?
What changes after that?
What happens if the player fails, retries, exits, or disconnects?
When is the objective actually complete?
What result is stored or displayed?
Where does the player/system go next?
```

Humanize should:

- explain context before instruction;
- prefer cause → action → response → consequence;
- turn comma-stacked dumps into readable sentences;
- keep full Gameplay Flow as a readable player journey;
- make role overviews explain the work before dense tables;
- keep distinct technical fields visually/verbally distinct rather than compressing them into one sentence;
- preserve exact technical facts;
- do not add promotional language or unsupported detail.

Humanize is not permission to answer a question that authority does not resolve. A material unanswered question returns to Flow 2 rather than being hidden behind fluent prose.

## Flow 4 acceptance rule

Flow 4 checks the PRD against this contract once through the relevant production lenses.

A **Major** finding exists when a production role must reopen original source to recover a material rule that belongs in the PRD, when a mandatory Golden function no longer performs its intended role, or when Acceptance & Verification does not actually prove a material behavior that the package depends on.

Mechanical presence is not semantic acceptance. Do not use word counts, row counts, semantic similarity scores, or a permanent traceability matrix as substitutes for review.

## Canonical-content gate

`content.md` is ready for projection only when:

- Flow 2 truthfully reports `ready_for_prd`;
- the fixed Golden blueprint is represented;
- mandatory concerns resolve as Defined / Explicit No / Not Applicable rather than silently missing;
- Overview includes document scope and intended use;
- every package has a visible Scoring / Result contract;
- full Gameplay Flow explains the chronological player journey;
- Gameplay Overview uses a concise Objective Sequence rather than duplicating the full narrative;
- Global Development preserves all four fixed functions with the canonical professional names;
- Level Design and Developer carry complete material role-owned meaning;
- every package has observable Acceptance & Verification criteria;
- package terminology uses the canonical package term index rather than duplicated per-surface copies;
- explanatory prose has received the Humanize pass and does not leave already-resolved causal questions implicit;
- material meaning remains traceable to source/recovery/approved decisions;
- no material Proposal/Blocked item affects output;
- no unresolved placeholder remains.

A structurally complete document that omits material production meaning is not finished. A detailed document that invents unsupported meaning is also not finished.
