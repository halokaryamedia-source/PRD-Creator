# Golden Prototype PRD Contract

`work/content.md` owns PRD meaning. `render-data.json` and `final.html` are derived.

This file is the **single semantic and visible-composition owner** for the gameplay PRD family.

## Core rule

The approved Golden Sample is not merely inspiration or a minimum quality floor.

> **The Golden Sample is the canonical page prototype. Generated PRDs must use the same visible page structure, labels, component order, and reading pattern.**

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
- repeated explanation of the same consequence;
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

Humanize means clearer/directer wording, not more prose and not a new presentation pattern.

## Flow 4

Flow 4 checks:

```text
source fidelity
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
- project facts drift or are invented.

Mechanical presence alone is not acceptance.

## Final authoring test

Before render, ask:

```text
Does every page look and read like the matching Golden page prototype?
Is the information in the same visible place a Golden reader would expect?
Is every summary concise?
Are detailed rules moved into the correct table/flow instead of cramped cards?
Did we add any visible UI that Golden does not contain?
```

If the last answer is yes, remove it unless the user explicitly approved the Golden prototype change.
