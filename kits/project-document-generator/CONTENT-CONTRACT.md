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

## Terms Used

Use Terms Used only for project-specific or production-critical terminology that materially helps the page reader. Do not repeat every ordinary noun. Prefer local terms needed by that role; other definitions remain available through the shared glossary/tooltips.

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

After meaning is complete, apply one bounded Humanize pass:

- explain context before instruction;
- prefer cause → action → response → consequence;
- turn comma-stacked dumps into readable sentences;
- keep full Gameplay Flow as a readable player journey;
- make role overviews explain the work before dense tables;
- preserve exact technical facts;
- do not add promotional language or unsupported detail.

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
- explanatory prose has received the Humanize pass;
- material meaning remains traceable to source/recovery/approved decisions;
- no material Proposal/Blocked item affects output;
- no unresolved placeholder remains.

A structurally complete document that omits material production meaning is not finished. A detailed document that invents unsupported meaning is also not finished.
