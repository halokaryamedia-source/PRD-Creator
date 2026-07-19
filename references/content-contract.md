# Content Contract

## Core Principles

1. Context before detail.
2. Critical data is explicit or visibly open.
3. The same rule keeps one meaning across every page.
4. Information belongs to the correct production role.
5. Every relevant page has enough local context.
6. No filler or decorative repetition.
7. Primary-language content stabilizes before translation.

## Critical Data

Includes player/session/arena count, objective order, item/resource quantities,
checkpoint/node/machine count, important sizes, target time, scoring weights,
timer start/stop, completion and no-score conditions, handoff items,
interruption/reset behavior, and final-result rules.

Unknown critical data must be represented explicitly as open and blocking. Never
replace it with vague phrases such as “use the configured amount” without a
precise reference.

## Overview

Must explain project context, player role, main experience, game information,
journey/stage overview, main systems, final result, and relevant Terms Used.
Avoid detailed script, coordinates, per-package reset, and long formulas.

## Gameplay Flow

Chronologically explains where the player arrives, what happens, the main
obstacle, the result, and the next destination. It is a narrative production
reference, not an implementation checklist.

## Global Development

For Complete Game/Map:

- Development Overview
- Game System
- Data and Reset
- Gameplay Development

Game System owns session/arena/objective runtime. Data and Reset owns tracked,
stored, removed, restored, and verified state.

## Gameplay Package

Every complete package uses:

```text
Gameplay Overview
Level Design
Developer
```

### Gameplay Overview

Requires context, main objective, result, purpose, estimated time, starting
condition, end condition, blocked/fail condition, scoring/completion criteria,
ordered player flow, and Terms Used.

### Level Design

Requires overview, design flow, grouped build requirements, important build
notes, and Terms Used. Separate Build and Visual Requirements from Gameplay
Function. Specify only sizes that materially affect gameplay or production.

### Developer

Requires overview, development flow, grouped requirements, scoring or completion
data, recording, duplicate prevention, Exit/disconnect, reset, verification,
important notes, and Terms Used. Define product behavior, not arbitrary class or
file names unless architecture is explicitly requested.

## Scoring Contract

Every score defines name, scale, components, weights totaling 100%, standard or
target, bonus behavior, reduction behavior, timer start/stop, excluded time,
no-score condition, recorded data, duplicate prevention, rounding when
product-critical, and final-result relationship.

Do not force a mathematical formula when clear product behavior is sufficient.
When exact math is required, state and validate it explicitly.

## Completion Data

Gameplay without Objective Score must define `produces_score: false`, valid
completion, recorded data, interruption behavior, duplicate prevention, and
handoff result. Do not invent an artificial score for tutorials, transitions, or
ending presentations.

## Package Types

- Introduction: onboarding, items, transition, completion data, optional no-score.
- Objective: actions, score/completion, handoff, interruption, reset.
- Transition: full package only when it has meaningful interaction/production work.
- Ending: final presentation, result, reward, save, lobby return, final reset.
- Stage/Station: entry, timer, retry/tier, score, transition, reset, global result.

## Terms Used

Each term requires stable ID, bilingual term and definition, scope, aliases, and
status. Global definitions are shared; local definitions may refine only local
meaning without conflict. Terms Used is the source for bold tooltip matching.
Ordinary words should not be over-tagged.

## Structured Draft Review

Present readable previews to the user rather than raw YAML unless requested.
Sections become approved only after required content, explicit critical data,
Mini Audit, and user approval. Sections become frozen only during Content Freeze.
