# Canonical PRD Content Contract

`work/content.md` is the human-readable source of truth for PRD meaning. `work/render-data.json` is a derived projection and `output/final.html` is a derived presentation artifact.

## Golden Sample is the output contract

For this gameplay-document family, the approved Golden Sample defines both the document hierarchy **and the reusable page composition**. Future projects replace project facts; they do not invent a different page language.

Preserve:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Do not remove a role page merely because local work is small. Keep it concise and point to a shared/global rule when appropriate. Do not fill empty visual space with invented mechanics, dimensions, architecture, tracking, lore, or implementation detail.

## Golden page-composition contract

The renderer must project canonical content into the existing Golden Sample component families below. These are the default structures for this document family, not optional styling suggestions.

### Overview

Use the Golden overview rhythm:

```text
project identity / context
→ key production facts
→ complete gameplay journey
→ main shared systems
→ Terms Used when needed
```

Overview explains the project to a new team member before implementation detail appears.

### Gameplay Flow

Gameplay Flow is storytelling-first, not an implementation table.

```text
stage title / narrative context
→ ordered narrative beats
→ result / transition to next destination
→ Terms Used when needed
```

Use the Golden narrative component family (`narrative-page`, `narrative-sequence`, narrative beats, transition treatment). Keep implementation checklists in Development pages.

### Global Development

Global Development pages share one Golden development-navigation family. Each page uses:

```text
Development title / subtitle
→ shared section tabs
→ context block
→ Development Flow cards when a flow exists
→ grouped Development Requirements production table when requirements exist
→ Important Development Notes card grid when notes exist
→ Terms Used when needed
```

Typical global owners include Development Overview, Game/Session System, Data and Reset, and Shared Gameplay Development. Only create global pages the project actually needs; do not duplicate their full rules inside every gameplay package.

### Gameplay Package — A. Gameplay Overview

Every package keeps the Golden three-tab navigation: `1 Gameplay Overview / 2 Level Design / 3 Developer`.

Gameplay Overview uses:

```text
package title / package label
→ Golden 1/2/3 tabs
→ 3 context cards:
     Gameplay Context
     Main Objective
     Result
→ Gameplay Information production table
→ Gameplay Flow role-sequence
→ Terms Used when needed
```

Gameplay Information uses project-relevant rows from this Golden family:

- Game Purpose;
- Gameplay Time;
- Starting Condition;
- End Condition;
- Fail Condition;
- Scoring Criteria or completion behavior.

Do not add a row when the project has no meaningful value for it. Do not replace the entire Golden information block with generic prose/cards.

The Gameplay Flow is an ordered player-facing sequence, not a developer trigger/data table.

### Gameplay Package — B. Level Design

Level Design uses:

```text
package title / package label
→ Golden 1/2/3 tabs
→ Level Design Overview context block
→ Design Flow cards when meaningful
→ Build Requirements Golden production table
→ Important Build Notes card grid when meaningful
→ role-specific Terms Used only when useful
```

The Golden Build Requirements table uses:

```text
No.
Object
Area Size
Build and Visual Requirements
Gameplay Function
```

For each meaningful object/area, preserve the difference between what must be built and why gameplay needs it. `Area Size` may remain unspecified/neutral when no authoritative size exists; never invent exact dimensions just to populate the column.

The projection may use grouped rows, object subtitles, and child rows where the content naturally has them. Do not flatten meaningful hierarchy into one generic `Group / Object / Requirement / Result` table.

### Gameplay Package — C. Developer

Developer uses:

```text
package title / package label
→ Golden 1/2/3 tabs
→ Developer Overview context block
→ Development Flow cards when meaningful
→ grouped Development Requirements Golden production table
     → scoring/completion integrated inside the relevant requirement hierarchy
     → reset/interruption integrated inside the hierarchy when relevant
→ Important Development Notes card grid when meaningful
→ role-specific Terms Used only when useful
```

The Golden Developer production table uses:

```text
No.
Setup
Development Requirements
Gameplay Function
```

Preserve meaningful requirement groups such as Mechanic Setup, Gameplay Setup, Scoring/Completion, and Reset where the project actually has those concerns. A requirement cell may contain several concise rules; do not flatten grouped implementation logic into unrelated standalone tables.

Scoring or completion presentation uses the Golden inline score/completion summary + inline detail-table treatment. It must stay inside the Developer requirement structure rather than becoming an unrelated generic table after the requirements.

## Content authority and role ownership

1. **Source fidelity first.** Only source, supported recovery, and approved decisions may define project meaning.
2. **Context before detail.** A New Reader understands the experience before role implementation pages.
3. **One rule, one meaning.** Repetition for local context is allowed; semantic drift is not.
4. **Gameplay / Level Design / Developer stay separate.** Gameplay = intended player experience; Level Design = what must be built; Developer = runtime behavior/data/result.
5. **Local pages are usable alone.** A production role can work from its assigned package plus relevant global rules.
6. **No filler.** Fixed Golden structure does not authorize invented content.
7. **No unresolved material decisions.** Return a true unresolved decision to Flow 2.

## Information density

Use minimum sufficient detail **inside the fixed Golden composition**.

Keep a detail when it:

- explains project/player context needed to understand the work;
- changes what Level Design must build;
- changes what Developer must implement or record;
- defines a trigger, condition, quantity, timing, score, handoff, reset, or acceptance rule;
- prevents a production role from guessing a product decision.

Otherwise omit it, compress it, or reference the existing global/shared rule.

Do not:

- populate every possible field because the template has visual space;
- repeat a global rule in full across several packages;
- invent metrics, persistence, APIs, architecture, dimensions, objects, or decorative requirements;
- expand background/lore that has no gameplay or production effect.

## PRD writing quality

Write like a competent production team member, not promotional copy and not formulaic AI prose.

- State concrete behavior, condition, action, and consequence.
- Prefer simple precise words over inflated terms such as `pivotal`, `crucial`, `robust`, `intricate`, `transformative`, `showcase`, or `foster` when they add no precision.
- Remove fake analysis and decorative `highlighting / showcasing / ensuring` tails that merely restate the mechanic.
- Keep approved terminology stable instead of synonym cycling.
- Do not force rule-of-three phrasing or repeated rhetorical patterns.
- Make the minimum effective wording edit; leave already-clear technical text alone.
- Never rewrite IDs, approved names, numbers, coordinates, timings, formulas, weights, triggers, conditions, state names, code/API names, or other authoritative values for style.
- Apply prose polishing mainly to explanation/narrative; do not aggressively humanize tables, formulas, configuration, code, or concise requirements.

Example:

```text
Avoid:
This objective serves as a pivotal moment that enhances the player's experience and ensures a seamless transition into the next phase.

Prefer:
Completing this objective opens the next area and starts the following phase.
```

## Scoring contract

If a package produces a score, define only the scoring facts the product actually needs:

- score name and scale when defined;
- score components and weights when weighted scoring is used;
- target/standard or success basis when relevant;
- bonus/reduction behavior when relevant;
- timer start/stop and excluded time when relevant;
- invalid/no-score condition;
- recorded data when genuinely required;
- duplicate prevention when genuinely required;
- relationship to the package/final result;
- exact formula only when the exact math is product-critical.

Numeric component weights must total 100% unless an approved design explicitly defines another model.

## Completion-data contract

A non-scoring package must not receive an artificial score just to look like a scoring objective.

Use completion data for the actual product outcome:

- `produces_score: false`;
- valid completion condition;
- recorded completion/progress data only when genuinely required;
- interruption behavior when relevant;
- duplicate prevention when relevant;
- handoff result.

Do not invent analytics, counters, persistence, or duplicate-prevention systems merely to fill the Golden surface.

## Terms Used

Use Terms Used only for project-specific or production-critical terminology.

Each term has a stable key, label, concise definition, and optional aliases. Package-wide terms may power glossary/tooltips, but a Level Design or Developer page should only render a Terms Used block when that role actually benefits from it. Do not repeat the same visible glossary block on every role page by default.

## Critical information

Treat these as critical when they affect the project:

- player/session/arena count;
- package/stage order;
- important quantities and dimensions;
- target time and timer boundaries;
- scoring weights/inputs;
- completion and invalid/no-score conditions;
- handoff items/state;
- interruption/disconnect behavior;
- reset behavior;
- final-result rules.

If required critical information remains unresolved, return that requirement to Flow 2 rather than hiding the gap behind vague text or a polished Golden-looking component.

## Canonical-content gate

`content.md` is ready for projection when:

- Flow 2 is truthfully `ready_for_prd`;
- material statements trace to source/recovery/approved decisions;
- Golden Sample hierarchy and page-composition contract are represented;
- each role surface contains enough local context to work without invented filler;
- scoring/completion behavior is explicit where relevant;
- explanatory prose is plain and concrete;
- no material Proposal/Blocked item affects requested scope;
- no unresolved placeholder remains.

A semantically correct PRD that cannot be projected into the Golden page composition is **not** finished Flow 3 content for this document family.
