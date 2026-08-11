# Golden Mandatory PRD Contract

`work/content.md` is the human-readable source of truth for Flow 3. `render-data.json` and `final.html` are derived.

This file is the **single semantic owner** for the gameplay PRD family. Flow 2, Flow 3, rendering, and Flow 4 must refer here instead of maintaining separate Golden checklists.

## Core rule

The approved Golden Sample defines the **minimum document function** for this gameplay PRD family.

```text
Current project facts + approved decisions
→ fill the Golden mandatory surfaces
→ never remove a Golden function merely because source is short
→ never copy Golden project-specific facts merely to fill space
```

A generated PRD may contain more project-specific detail than the Golden Sample when the project needs it. It may not contain fewer required Golden functions.

**No filler does not mean minimal document.** The target is:

```text
complete material production information
+
no useless repetition
```

## Mandatory-slot state

Every mandatory concern must resolve to one of these meanings before handoff:

| State | Meaning |
|---|---|
| **Defined** | The project/source defines the actual behavior/value. |
| **Explicit No** | The concern exists, and the correct project rule is explicitly negative, e.g. `No Objective Score`, `No hard timeout`, `No permanent fail`. |
| **Not Applicable** | The concern genuinely does not apply; state that clearly with a short production reason when the visible slot would otherwise be ambiguous. |
| **Blocked** | The concern is material but cannot yet be resolved responsibly; Flow 2 must not declare `ready_for_prd`. |

A mandatory slot must **never disappear silently** because its value was absent from source or render data.

`missing` is not a fifth allowed state.

## Fixed document blueprint

For `N` gameplay packages, the gameplay PRD family uses this fixed shell:

```text
01 Overview

02 Gameplay Flow
   02A The Journey Begins
   02B+ one Gameplay Flow page for every package, in package order

03 Development
   Development Overview
   Game System
   Data and Reset
   Gameplay Development

04+ Gameplay Packages
   for every package:
   1. Gameplay Overview
   2. Level Design
   3. Developer
```

The number of package pages follows the project. The four Global Development functions do not collapse into one generic page.

For `N` packages, the expected page count is:

```text
Overview                         1
Gameplay Flow                    1 + N
Global Development               4
Gameplay role pages              3N
-----------------------------------
Total                            6 + 4N
```

This count is a consequence of the fixed shell, not a quality score or word-count target.

## Mandatory surface matrix

### 1. Overview

The Overview must provide all of these functions:

- **Project Context** — what the project/gameplay experience is and why the player is there;
- **Session Model** — player/session/arena relationship or an explicit project-equivalent rule;
- **Target Playtime** — target duration or an explicit negative/unspecified production rule;
- **Game Structure** — stage/package structure and scored/non-scored relationship at project level;
- **Complete Gameplay Journey** — the ordered journey from opening to ending;
- **Main Systems / Global Gameplay Direction** — the shared systems a new reader must understand before package detail.

Terms Used is shown when project-specific production terminology materially helps the reader.

### 2. Gameplay Flow — The Journey Begins

The opening flow page must explain:

- the player's starting situation;
- what the player sees or understands first;
- why the journey begins;
- the first instruction/cue or world response that matters;
- the first playable destination;
- the transition into the first package.

### 3. Gameplay Flow — every package

Gameplay Flow is the **chronological player journey**, not a developer checklist, abstract flowchart caption, or task summary.

Each package flow must explain the applicable story beats in production language:

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

Use enough beats to make the experience understandable without reopening the original source. Do not invent dialogue, lore, cinematics, animation, quantities, or mechanics merely to make the page feel richer.

### 4. Global Development — four fixed functions

Global Development always contains these four pages in this order:

1. **Development Overview**
2. **Game System**
3. **Data and Reset**
4. **Gameplay Development**

Each page contains:

- Overview;
- Development Flow;
- Development Requirements;
- Important Development Notes.

If one concern is intentionally simple, keep the surface and state the project truth clearly. Do not delete the page or its core blocks merely to reduce page count.

#### Development Overview owns

Project-wide implementation topology: package order, shared ownership, major dependencies, common handoff, and the overall development sequence.

#### Game System owns

Shared runtime/session behavior: player/session/arena ownership, shared state/permissions, common activation/routing, concurrency/isolation, and other project-wide runtime rules.

#### Data and Reset owns

Shared persistence/result/data behavior: score/final-result storage, telemetry/export rules, interruption/disconnect/pause behavior, reset/cleanup, and reusable-arena/session recovery where applicable.

#### Gameplay Development owns

How the gameplay packages connect as one production system: package lifecycle, shared package conventions, package-to-package handoff, and cross-package implementation responsibilities.

Use explicit `Not Applicable` only when a concern genuinely does not apply to the current project. Do not hide a shared rule inside one package when multiple packages depend on it.

### 5. Gameplay Overview — every package

Every package Gameplay Overview contains:

- Gameplay Context;
- Main Objective;
- Result;
- Gameplay Information;
- chronological Player Flow.

#### Gameplay Information — fixed rows

The following concerns are always resolved and visible:

1. Game Purpose
2. Gameplay Time
3. Starting Condition
4. End Condition
5. Fail / Retry / Blocked Condition
6. Scoring / Result

Use explicit negative wording when appropriate. Examples:

```text
No hard timeout. The package continues until ...
No permanent fail. A setback returns the player to ...
No Objective Score. Completion only opens ...
```

Do not remove a row because the correct rule is negative.

### 6. Level Design — every package

Every Level Design page contains:

- Level Design Overview;
- Design Flow;
- Build Requirements;
- Important Build Notes.

Golden Build Requirements columns remain:

```text
No. | Object | Area Size | Build and Visual Requirements | Gameplay Function
```

Carry all material build-owned meaning supported by the project, including when applicable:

- required areas/sub-areas;
- objects, machines, markers, hazards, interactables;
- route/spatial relationships;
- visible destination, sightlines, readability, warnings, guidance;
- known dimensions/size constraints;
- safe landing/recovery space;
- player access and interaction placement;
- entry/exit/reset boundaries;
- build/visual requirements;
- gameplay function;
- notes that prevent a materially wrong build.

`Area Size` may use a neutral explicit value such as `Not specified — follow approved layout` when authority intentionally leaves it open. Never invent dimensions merely to fill the table.

A Level Designer must not need the original source to rediscover a material build requirement that belongs on this page.

### 7. Developer — every package

Every Developer page contains:

- Developer Overview;
- Development Flow;
- Development Requirements;
- Scoring / Result contract inside the requirement hierarchy;
- Reset / interruption behavior;
- Important Development Notes.

Golden Development Requirements columns remain:

```text
No. | Setup | Development Requirements | Gameplay Function
```

Carry all material runtime-owned meaning supported by the project, including when applicable:

- activation/precondition;
- interaction behavior;
- progression/state changes;
- quantities/timing;
- success/completion;
- Objective Score **or explicit No Objective Score**;
- score/result relationship to the final result;
- player-facing score/result display;
- telemetry/export/data behavior;
- invalid/no-score behavior;
- pause/interruption/disconnect;
- retry/reset/cleanup;
- transition/handoff;
- implementation notes that prevent materially wrong behavior.

A Developer must not need the original source to rediscover a material runtime requirement that belongs on this page.

## Scoring / Result contract — mandatory for every package

Every package must answer these questions explicitly:

```text
1. Internal result
   Does the package calculate/store an Objective Score or only completion?

2. Calculation / completion rule
   How is that score/result determined?

3. Final-result relationship
   How does this package contribute to or affect the project/session final result?

4. Player-facing display
   What score/result is shown or intentionally not shown to the player?

5. Telemetry / export
   What score/result is exported, logged, or intentionally excluded from downstream payloads when such data systems exist?
```

### Scored package

State `Objective Score` and preserve project-defined details such as:

- score name/scale;
- components/weights;
- timer start/stop/excluded time;
- bonus/reduction behavior;
- invalid/no-score condition;
- duplicate prevention when required;
- final-result relationship;
- player-facing display rule;
- telemetry/export rule;
- exact formula when product-critical.

Numeric component weights total 100% unless approved authority explicitly defines another model.

### Non-scored package

State exactly and visibly:

```text
No Objective Score
```

Then define:

- valid completion condition;
- completion/progress data that must be recorded;
- interruption behavior;
- duplicate prevention when required;
- handoff result;
- final-result relationship, including non-contribution to Objective Score when applicable;
- player-facing result behavior;
- telemetry/export behavior.

### Never broaden negative rules

These are different requirements:

```text
No Objective Score
Do not display score to the player
Do not export score in telemetry
```

One does not imply either of the others.

## Terms Used

Terms Used is a supporting Golden component, not permission to repeat every noun.

Use it for project-specific or production-critical terminology that materially helps the page reader. A term has a stable key, label, concise definition, and optional aliases/role visibility.

If no project-specific term is needed on a surface, the Terms block may be omitted; this is one of the few genuinely conditional presentation components because its function itself may be Not Applicable.

## Source fidelity and authority

Project meaning follows the repository authority chain:

1. current explicit user instruction;
2. approved project decisions;
3. current authoritative project source;
4. normalized requirement state;
5. reference/Golden material for document function/quality only.

A source filename containing `FINAL` does not override higher-authority current instruction or approved decisions.

Golden supplies **document function**, not project facts. Never copy Golden mechanics, counts, story, scoring, objects, timings, or implementation decisions unless current project authority independently supports them.

## Flow 2 responsibility

Before `ready_for_prd`, Flow 2 resolves every mandatory concern that is material to the current project as:

```text
Defined
Explicit No
Not Applicable
Blocked
```

Flow 2 does **not** create a separate Golden checklist artifact. Use normal source/requirement state. A material unresolved concern becomes `Blocked`/pending decision in existing state and prevents readiness.

Flow 2 must specifically avoid these recurring interpretation errors:

- display/export prohibition incorrectly becoming `No Objective Score`;
- missing source detail being treated as permission to remove a mandatory surface;
- one package-specific rule incorrectly becoming a global rule;
- a Golden example fact being copied as project truth;
- a material build/runtime implication being lost because source prose was summarized too aggressively.

## Flow 3 authoring rule

Flow 3 fills the fixed Golden shell using **minimum complete production detail**.

Do not ask:

> How little can this page contain and still look valid?

Ask:

> What material project meaning must this page carry so its reader can work correctly without reopening the source?

Use the Golden Sample as a functional quality floor, not a word-count target.

## Humanize pass

After canonical meaning is complete and before projection, perform one bounded prose pass.

Humanize should:

- use natural production English;
- explain context before instruction;
- prefer cause → action → response → consequence;
- turn unreadable comma-stacked requirement dumps into clear sentences;
- keep Gameplay Flow as a readable account of the player journey;
- make Level Design/Developer overviews explain the work before dense tables;
- preserve stable project terminology.

Humanize must not:

- change official terminology;
- alter numbers, timings, coordinates, formulas, weights, triggers, conditions, state names, APIs, or approved mechanics;
- soften uncertainty/approval state;
- add unsupported lore/cinematic/design detail;
- inflate simple requirements with promotional writing.

Tables, formulas, IDs, configuration, and exact technical values remain concise and precise.

## Flow 4 acceptance rule

Flow 4 checks the PRD against this contract once through the relevant production lenses.

A **Major** finding exists when a production role must reopen original source to recover a material rule that belongs in the PRD, or when a mandatory Golden function has been compressed into something that no longer performs its intended role.

A mechanical presence check is not semantic acceptance.

Do not use word counts, row counts, semantic similarity scores, or a permanent source-to-output matrix as a substitute for review.

## Canonical-content gate

`content.md` is ready for projection only when:

- Flow 2 truthfully reports `ready_for_prd`;
- the fixed Golden blueprint is represented;
- every mandatory concern resolves as Defined / Explicit No / Not Applicable rather than silently missing;
- every package has a visible Scoring / Result contract;
- Gameplay Flow explains the chronological player journey;
- Global Development preserves all four fixed functions;
- Level Design and Developer carry complete material role-owned meaning;
- explanatory prose has received the Humanize pass;
- material meaning remains traceable to source/recovery/approved decisions;
- no material Proposal/Blocked item affects the output;
- no unresolved placeholder remains.

A structurally complete document that omits material production meaning is not finished. A detailed document that invents unsupported meaning is also not finished.
