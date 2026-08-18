# Golden Prototype PRD Contract

`work/content.md` owns PRD meaning. `render-data.json` and `output/v<document.version>/prd.html` are derived.

This file is the **single semantic and visible-composition owner** for the gameplay PRD family.

## Core rule

The approved Golden Sample is not merely inspiration or a minimum quality floor.

> **The Golden Sample is the canonical page prototype. Generated PRDs must use the same visible page structure, labels, component order, reading pattern, and comparable information density.**

Project facts are dynamic. Package count is dynamic. The visible document design is not.

Do not add a new visible panel, card type, metadata strip, orientation bar, acceptance panel, alternative flow layout, renamed heading, or new page composition unless the user explicitly approves a change to the Golden prototype.

When the current project needs more detail, place that detail inside the existing Golden surface that owns it. Do not create a new surface to make the information fit.

## Authority

Project meaning follows:

1. current explicit user instruction;
2. approved project decisions;
3. current authoritative project source;
4. normalized requirement state;
5. Golden Sample for **document structure/presentation only**.

Golden example mechanics are never copied as project facts.

Every material concern resolves as:

```text
Defined | Explicit No | Not Applicable | Blocked
```

`missing` is not a valid state.

## Material-detail conservation

Flow 3 is allowed to rewrite wording. It is **not** allowed to reduce distinct production meaning merely to make the PRD shorter, cleaner, or easier to render.

Treat every independently actionable **resolved PRD-scope production rule** from Flow 2 as conserved material meaning. This includes separate conditions, values, exceptions, recovery behavior, ownership boundaries, timing rules, scoring rules, reset behavior, build constraints, interaction states, and observable results.

The conservation rule is:

```text
resolved PRD-scope material rule
→ one owned canonical representation
→ one matching Golden surface in render-data/current versioned prd.html
```

Original source may contain technical or as-built evidence that Flow 2 intentionally did not promote into canonical project meaning. Flow 3 must not reintroduce incidental implementation identifiers, final world coordinates/map-instance locators, debug/setup residue, or other excluded realization details merely to appear complete. Preserve the approved production meaning instead, including legitimate dimensions, spatial relationships, relative/functional placement, observable behavior, and explicit approved technical constraints.

Two rules may be merged only when they are genuinely the same production instruction. A shorter sentence is acceptable; deleting one of two independent requirements is not.

When source meaning naturally contains multiple requirements inside one table cell or requirement group, preserve that structure as multiple list items/rows in canonical data rather than flattening it into one summary sentence. When a Gameplay Flow beat needs multiple paragraphs to explain distinct action/response/recovery states, retain the distinct paragraphs. Do not collapse them simply because a single scalar field would be easier to render.

`Humanize`, `direct writing`, and `concise summary` apply to **wording and placement**, not to the number of material facts retained.

A generated PRD is incomplete when a Level Designer or Developer would need to reopen the source to recover a resolved PRD-scope rule that Flow 2 already established. For a representative project that is also the Golden reference project, regeneration must preserve all current approved project meaning even when the wording changes.

## Stable document version

`document.version` is release/project metadata, not an edit counter.

Clarification, Humanize, review correction, rerendering, and representative testing keep the same version. Change it only when the user/source defines a new revision or the team intentionally declares a new release/handoff milestone.

## Fixed document family

For `N` gameplay packages:

```text
01 Overview

02 Gameplay Flow
   The Journey Begins
   one Gameplay Flow page per package

03 Development
   Development Overview
   Game System
   Data and Reset
   Gameplay Development

04+ Gameplay Packages
   Gameplay Overview
   Level Design
   Developer
```

Total pages remain:

```text
6 + 4N
```

## Reverse-derived Golden fill map

The Golden contract is established **from the approved reference first**, then used to fill new projects. Do not start from an imagined generic PRD and try to make it look similar afterward.

Use this direction:

```text
exact Golden reference
→ identify each fixed visible slot and what question that slot answers
→ fill those slots only from current project authority
→ preserve project-specific material detail inside the owning slot
→ render through the exact Golden prototype
→ validate the generated page against the same slot map
```

This is a finite authoring map, **not** a new schema or abstraction layer.

### What is fixed vs variable

The approved Golden demonstrates two different kinds of rules. Keep them separate:

| Locked by Golden | Filled from project authority |
|---|---|
| page family, page order, visible section names and component order | project title, story, mechanics, timings, scoring values and approved implementation requirements within PRD scope |
| Overview has 3 fixed fact slots: Session Model, Target Playtime, Game Structure | the value inside each fact slot |
| Global Development pages use 4 Development Flow cards and 4 Important Development Notes | the project-specific stage summaries, requirement groups/rows and note text |
| Gameplay Overview uses 3 context cards, 6 fixed Gameplay Information rows and a 5-beat compact Gameplay Flow | the actual context, objective, result, conditions, scoring meaning and five high-level beats |
| Level Design uses 4 Design Flow cards, the Golden Build Requirements columns and 4 Important Build Notes | project-specific areas/objects, spatial constraints, build requirements and functions; table row count remains data-driven |
| Developer uses 4 Development Flow cards, the Golden Development Requirements columns and 4 Important Development Notes | project-specific mechanic/setup/data/scoring/interruption/reset requirements; table row count remains data-driven |
| Terms Used placement | actual glossary entries and glossary count |
| one Complete Gameplay Journey card per package | package count and package-specific journey summary |
| Gameplay Flow story-page composition | number of narrative sections/paragraphs needed to conserve approved meaning |

Do **not** turn a number that is merely an AFTERSHOCK project fact into a global rule. For example, six packages, four scored objectives, five arenas, ore counts, storm timings, and named objects are reference-project facts, not Golden fill requirements.

### Slot meaning — Overview

| Golden slot | It must answer |
|---|---|
| Project-context lead | What is this experience, what situation drives it, what broad journey does the player complete, and what state/result closes the experience? Keep it one readable overview paragraph, not a mechanic dump. |
| Session Model | How is one play session/player run organized, including concurrency/isolation only when relevant? |
| Target Playtime | What duration target or broad timing model should production expect? Do not invent a hard timeout. |
| Game Structure | How many gameplay packages/stages exist and what broad result structure matters? |
| Complete Gameplay Journey | What happens in each package in one short action/result summary, in chronological order? Exactly one journey card per package. |
| Global Gameplay Direction | What project-wide player/gameplay invariants apply across packages? Use direct rules, not architecture notes or repeated package detail. |

### Slot meaning — Gameplay Flow

Each Gameplay Flow page is the **player-readable chronological truth** for that journey segment.

| Golden slot | It must answer |
|---|---|
| Title / eyebrow / intro | Where is the player now, what is the immediate situation, and what is this segment about? |
| Story-flow sections | In order: what the player encounters, what they do, what visible/system response follows, what setback/recovery applies when relevant, and what state changes next. Use as many distinct paragraphs as material meaning requires. |
| Transition | What completion state hands the player into the next package or final state? |
| Terms Used | Which non-obvious project terms are needed to understand this flow? Use the full relevant glossary scope; do not shrink it merely because another role page does not display Terms Used. |

Story-flow depth is **data-driven**. Golden fixes the reading pattern, not a universal number of narrative paragraphs.

### Slot meaning — the four Global Development pages

The page names are fixed, and each has a distinct job:

| Page | Owns |
|---|---|
| Development Overview | project-wide development topology: how the complete journey, shared systems, package handoffs, result handling and reuse fit together |
| Game System | shared runtime/session ownership, isolation, player state, global objective control, protected items/feedback and lifecycle rules |
| Data and Reset | timing ownership, active/completed data, valid result storage, interruption behavior, recovery/reset verification and reusable state |
| Gameplay Development | the common implementation contract for every gameplay package: mechanic, area integration, data/result handling, handoff and reset expectations |

For every Global Development page:

- **Overview context block** states the page's responsibility and boundary in one compact explanation.
- **4 Development Flow cards** summarize the four major lifecycle/stage steps. They are orientation, not a substitute for requirements.
- **Development Requirements** contains the actionable grouped rules. Group and row count are data-driven; independent rules must survive as independent readable items.
- **System Result** states the observable project/system outcome of that requirement group or item.
- **4 Important Development Notes** hold the highest-risk invariants, exceptions, or must-not-break constraints. They are not an overflow bucket for omitted requirements.

### Slot meaning — Gameplay Overview

The three context cards are fixed summaries:

| Card | It must answer |
|---|---|
| Gameplay Context | Where/when does this package begin and what player-visible situation exists? |
| Main Objective | What must the player accomplish, in one direct objective statement? |
| Result | What player/world/session state is true immediately after valid completion, including the next handoff when relevant? |

Gameplay Information always uses these six rows with these meanings:

| Row | It must answer |
|---|---|
| Game Purpose | Why does this gameplay package exist in the player journey and what core interaction/progression does it provide? |
| Gameplay Time | What target/limit/no-limit timing rule should the reader understand at gameplay level? Detailed timer implementation belongs on Developer. |
| Starting Condition | What prerequisites and observable starting state must be true when the package becomes playable? |
| End Condition | What exact valid completion state ends the package? |
| Fail Condition | What counts as failure/setback/no-fail, and what retry/recovery behavior matters to the player? Negative rules must be explicit. |
| Scoring Criteria | Does the package produce an Objective Score or completion data only, and what high-level inputs determine it? Detailed formula/storage/display/export rules belong on Developer. |

The compact Gameplay Flow uses **5 high-level beats**. Map approved meaning to the five visible stages without inventing mechanics. Normally the beats move from entry/setup through core progression to valid completion and transition, but their titles/content remain project-specific.

### Slot meaning — Level Design

- **Level Design Overview** answers what spatial experience must be built, how its main areas relate, and what must stay readable to the player.
- **4 Design Flow cards** are the four most useful build milestones/areas in the package's actual spatial progression. Do not force generic labels when the level's structure is different.
- **Build Requirements** is the full build-owned specification. Row count is data-driven.
- **4 Important Build Notes** are the strongest spatial/readability/hazard/recovery constraints that must survive implementation.

Build Requirements columns mean:

```text
No.                          grouping/order
Object                       buildable area, route, object or grouped spatial element
Area Size                    approved dimension or direct spatial constraint
Build and Visual Requirements geometry, placement, route, readability, visual state and build-owned constraints
Gameplay Function            why that built element exists in play / what player-facing function it supports
```

### Slot meaning — Developer

- **Developer Overview** states the package's complete runtime responsibility in compact form: core mechanic, valid completion/result, and reset/handoff boundary.
- **4 Development Flow cards** summarize the implementation lifecycle. The Golden pattern normally covers setup/initialization, core execution/validation, result/data/completion handling, and reset/reuse/handoff. Preserve four cards, but use project-appropriate titles.
- **Development Requirements** owns the complete actionable technical behavior. Requirement/group count is data-driven.
- **4 Important Development Notes** are the highest-risk runtime invariants, duplication guards, interruption rules, ordering constraints or reset guarantees.

Development Requirements columns mean:

```text
No.                      grouping/order
Setup                    requirement group or concrete setup/behavior item
Development Requirements exact mechanic, trigger, validation, state, timing, data, scoring, interruption or reset rule
Gameplay Function        observable gameplay/system result and why the requirement exists
```

Scoring summaries, completion-data summaries, interruption handling and reset stay inside this existing hierarchy; do not create new visible panels for them.

### Reverse/forward proof rule

Golden fidelity is checked in two directions:

```text
Reference → Fill Map
Does the exact approved sample actually demonstrate the fixed pattern we claim?

Project Authority → Filled Golden
Does the generated PRD fill that same pattern with complete current-project meaning?
```

The first direction prevents the contract from drifting away from the real Sample. The second prevents a generator from satisfying the Sample mechanically while omitting or relocating project meaning.

Reference-specific words are not compared literally for unrelated projects. Literal content parity is relevant only when regenerating the same reference project from its current approved authority.

## 1. Overview — Golden prototype

Visible order is fixed:

```text
page header
→ map/document type eyebrow
→ project title
→ Gameplay & Development Specification subtitle
→ one project-context lead paragraph
→ three facts
     Session Model
     Target Playtime
     Game Structure
→ Complete Gameplay Journey
→ Global Gameplay Direction
→ page footer
```

Do **not** render extra Document Control, Main Experience, Main Systems, status, acceptance, or metadata panels on this page.

Global Gameplay Direction is a short direct list of project-wide rules. It is not a place for architecture explanation or authoring commentary.

## 2. Gameplay Flow — Golden prototype

Visible order is fixed:

```text
page header
→ title
→ short eyebrow
→ short section-intro paragraph
→ story-flow
     section heading
     direct explanatory paragraph(s)
     section heading
     direct explanatory paragraph(s)
     ...
     transition
→ Terms Used
→ page footer
```

Gameplay Flow is a readable chronological player story. It is **not** a numbered developer checklist and it does not use orientation cards.

Write directly:

```text
situation
→ player action
→ visible/system response
→ setback/recovery when relevant
→ changed state/result
→ transition
```

Use normal paragraphs as in Golden. Do not compress the whole experience into terse database-like bullets, but do not turn one simple behavior into a long explanation either.

## 3. Global Development — Golden prototype

The four visible names are fixed:

1. **Development Overview**
2. **Game System**
3. **Data and Reset**
4. **Gameplay Development**

Every page uses this visible order:

```text
title + subtitle
→ four-tab Development navigation
→ Overview context block
→ Development Flow — 4 horizontal Golden flow cards
→ Development Requirements table
→ Important Development Notes — 4 note cards
→ Terms Used
```

Development Requirements columns are fixed:

```text
No. | Setup | Development Requirements | System Result
```

Do not rename these pages to alternative professional-sounding variants. Do not replace Development Flow with Trigger/Data/Result matrices.

## 4. Gameplay Overview — Golden prototype

Every package uses this visible order:

```text
package title + subtitle
→ Gameplay Overview / Level Design / Developer tabs
→ 3 context cards
     Gameplay Context
     Main Objective
     Result
→ Gameplay Information
→ Gameplay Flow
→ Terms Used
```

### Three context cards

These cards are summaries, not mini-specifications.

Each card should be one short, direct paragraph. Put detailed timing, state, scoring, recovery, implementation, or edge-case rules in the surfaces below.

Bad:

```text
A long paragraph that explains the mechanic, emotional purpose, two exceptions,
recovery behavior, scoring behavior, and transition inside Gameplay Context.
```

Good:

```text
Gameplay Context
The player reaches the damaged summit Beacon and begins the repair objective.
```

### Gameplay Information — exact Golden rows

Always show these six rows:

```text
Game Purpose
Gameplay Time
Starting Condition
End Condition
Fail Condition
Scoring Criteria
```

A negative rule is still shown explicitly, for example `No Objective Score` or `There is no fail state`.

### Gameplay Flow

This is the compact package sequence shown in Golden. Keep it scan-friendly and direct. Do not repeat the full Gameplay Flow narrative paragraph-by-paragraph.

For this gameplay PRD family, use the Golden five-beat sequence pattern. Combine or split already-approved meaning only at a high level; never invent a mechanic just to fill a step.

## 5. Level Design — Golden prototype

Visible order is fixed:

```text
package title + subtitle
→ package tabs
→ Level Design Overview
→ Design Flow — 4 horizontal Golden flow cards
→ Build Requirements table
→ Important Build Notes — 4 note cards
```

No separate Terms Used block is rendered on Level Design pages.

Build Requirements columns are fixed:

```text
No. | Object | Area Size | Build and Visual Requirements | Gameplay Function
```

`Area Size` may contain an exact size or a direct spatial statement when no exact dimensions are approved. Never invent dimensions.

Level Design must carry all material build-owned meaning: required areas, routes, objects, hazards, sightlines, interaction locations, recovery geometry, boundaries, visual states, and gameplay function.

## 6. Developer — Golden prototype

Visible order is fixed:

```text
package title + subtitle
→ package tabs
→ Developer Overview
→ Development Flow — 4 horizontal Golden flow cards
→ Development Requirements table
→ Important Development Notes — 4 note cards
```

No separate Terms Used block and **no separate Acceptance & Verification panel** are rendered on Developer pages.

Package acceptance remains required for Flow 4, but it belongs to acceptance/review state rather than creating a new visual section not present in Golden.

Development Requirements columns are fixed:

```text
No. | Setup | Development Requirements | Gameplay Function
```

Scoring/result and reset/interruption remain inside this requirement hierarchy, as in Golden.

The Development Flow cards are short stage summaries. Do not render a 2×2 matrix of:

```text
Trigger
System Behavior
Data
Expected Result
```

Those details belong in Development Requirements.

## Scoring / Result meaning

Every package still resolves:

```text
Objective Score or No Objective Score
calculation/completion rule
final-result relationship
player-facing display rule
telemetry/export rule
```

These concerns remain distinct. `Do not display score` does not mean `No Objective Score`, and `Do not export score` does not mean either of them.

Do not create an extra scoring page or custom scoring layout. Use the Golden Development Requirements / scoring summary pattern.

## Reset / interruption

Reset remains a Developer requirement. State both the reset/recovery action and the observable post-reset gameplay function/result. Do not leave the result cell blank.

## Acceptance

Package acceptance criteria are still mandatory project meaning, but they are reviewed in Flow 4 and recorded in `work/acceptance.md`.

Do not render a new Acceptance block inside the PRD unless the Golden Sample itself is intentionally revised by the user.

## Glossary / Terms Used

`packages[].terms` remains the canonical package glossary index.

Inline glossary highlighting may operate on package-owned prose, but the visible **Terms Used** block follows Golden exactly:

```text
Gameplay Flow        visible
Global Development   visible
Gameplay Overview    visible
Level Design         not rendered
Developer            not rendered
```

Role restrictions still apply to inline highlighting. The Terms Used block must never highlight its own definitions.

Do not turn common nouns into glossary entries.

## Direct writing rule

The default writing style is **direct production prose**.

Prefer:

```text
The player places Beacon Bricks on the marked scaffold positions.
Storm 1 removes 25% of the blocks present at trigger time.
After the tower is complete, the route to the Relay opens.
```

Avoid:

- long setup phrases before the actual rule;
- repeated explanation of the same rule;
- meta-language about the document/generator;
- marketing tone;
- comma-stacked requirement dumps;
- restating a table row as another paragraph;
- explaining implementation internals on Gameplay Overview cards.

A paragraph should answer one main production question. If it needs several unrelated answers, move the details to the correct existing Golden surface.

## Flow 2

Flow 2 resolves project truth. It does not redesign the document.

If a material decision is unresolved, return `Blocked` / `needs_decision`. Never fill a Golden slot by inventing product meaning.

## Flow 3

Flow 3 writes complete project meaning **inside the locked Golden prototypes**.

The author may adapt wording and project-specific row count where Golden tables are data-driven, but may not choose a different visible component or section order.

Before Humanize, perform a conservation pass: verify that each material rule recovered in Flow 2 has an owned location in `content.md`. When deriving `render-data.json`, preserve list/row/paragraph structure needed to keep independent rules independently readable. Do not use scalar summaries to hide detail that exists canonically.

Humanize means clearer/directer wording, not more prose and not a new presentation pattern. It also never means fewer material facts.

## Flow 4

Flow 4 checks:

```text
source fidelity
material-detail conservation
Golden prototype fidelity
New Reader usability
Level Designer usability
Developer usability
Acceptance sufficiency
Project consistency
```

A **Major** finding exists when:

- a required Golden surface is replaced or omitted;
- a new unapproved visible component is introduced;
- prose becomes harder to scan than the Golden reference;
- a role must reopen source for material meaning;
- independent resolved PRD-scope rules were collapsed or omitted during Flow 3;
- project facts drift or are invented.

Mechanical presence alone is not acceptance.

## Final authoring test

Before render, ask:

```text
Does every page look and read like the matching Golden page prototype?
Is the information in the same visible place a Golden reader would expect?
Did every distinct resolved PRD-scope material rule survive into canonical content?
Did structured multi-rule content stay structured instead of becoming one summary sentence?
Is every summary concise without deleting facts owned elsewhere?
Did we add any visible UI that Golden does not contain?
```

If the last answer is yes, remove it unless the user explicitly approved the Golden prototype change.