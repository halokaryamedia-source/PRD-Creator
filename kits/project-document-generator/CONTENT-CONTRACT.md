# Canonical PRD Content Contract

This file defines what `work/content.md` must contain after Flow 2 reaches `ready_for_prd`.

`content.md` is the canonical human-readable project document content. It owns project meaning for Flow 3. `render-data.json` is only a derived projection used by the renderer, and `final.html` is only a presentation artifact.

## Core principles

1. **Context before detail.** A reader should understand the project and player journey before implementation detail.
2. **Critical data is explicit.** Important counts, timings, conditions, scoring, handoffs, reset behavior, and state rules must be stated when they affect production.
3. **One rule, one meaning.** A mechanic or term may be repeated for local context, but its meaning cannot drift between pages.
4. **Role ownership stays separate.** Gameplay explains intended experience; Level Design explains what must be built; Developer explains runtime behavior and data.
5. **Local pages are usable alone.** A developer or level designer should not need to read the whole document to understand one assigned package.
6. **No filler.** Do not repeat narrative or requirements merely to make a page look complete.
7. **No unresolved design decisions.** Flow 3 may clarify wording, but it cannot invent a decision that Flow 2 left unresolved.
8. **Plain technical prose.** Prefer direct, concrete language. Writing quality must improve readability without changing project meaning or technical precision.
9. **Minimum sufficient detail.** Include enough information for the target role to work without guessing, but do not fill optional fields or repeat background that does not change a production decision, action, or acceptance condition.

## PRD writing quality

The PRD should read like a clear production document written by a competent team member, not promotional copy and not formulaic AI prose.

Use these rules for explanatory prose:

1. **State the concrete behavior.** Explain what happens, when it happens, and what result follows. Do not add generic comments about importance, immersion, engagement, seamlessness, or quality unless the source explicitly requires that claim.
2. **Prefer simple words when they are equally precise.** Avoid inflated vocabulary such as `pivotal`, `crucial`, `robust`, `intricate`, `transformative`, `showcase`, or `foster` when a direct technical phrase communicates the same meaning.
3. **Remove fake analysis.** Avoid trailing phrases such as `highlighting`, `underscoring`, `showcasing`, or `ensuring` when they only restate or decorate the mechanic instead of adding a real consequence.
4. **Keep terminology stable.** If the approved term is `Objective`, `Checkpoint`, `Arena`, or another project term, reuse it consistently. Do not rotate synonyms merely to make prose look varied.
5. **Do not force rhetorical patterns.** Avoid artificial rule-of-three phrasing, dramatic fragments, repeated contrast formulas such as `not only X, but Y`, and generic setup lines that delay the actual requirement.
6. **Use the minimum effective wording.** Remove filler and duplicated interpretation, but do not compress away context that a New Reader, Level Designer, or Developer needs.
7. **Protect technical facts.** A writing-quality pass must never alter IDs, approved names, numbers, coordinates, timings, formulas, scoring weights, trigger conditions, completion/fail conditions, state names, code/API names, or other authoritative values.
8. **Apply judgment by content type.** Rewrite narrative and explanatory paragraphs when needed. Leave tables, formulas, requirement lists, configuration values, code, and already-clear technical statements mostly untouched.

Example:

```text
Avoid:
This objective serves as a pivotal moment that enhances the player's experience and ensures a seamless transition into the next phase.

Prefer:
Completing this objective opens the next area and starts the following phase.
```

Another example:

```text
Avoid:
The bridge collapses after the timer ends, creating tension and encouraging players to move quickly.

Prefer:
When the timer ends, the bridge collapses. The player must cross before that happens.
```

If a smoother sentence would make a precise rule less explicit, keep the precise rule.

## Information density

Use the smallest amount of content that still makes the document production-ready.

Include a detail when it does at least one of these jobs:

- explains the project/player context needed to understand the work;
- changes what the Level Designer must build;
- changes what the Developer must implement or record;
- defines a trigger, condition, quantity, score, handoff, reset, or acceptance rule;
- prevents a target role from having to invent a product decision.

Otherwise, omit it or compress it.

Additional rules:

- Do not fill an optional section, field, note, or table merely because the template provides one.
- Do not repeat the same global rule in full across several packages. State the global rule once and repeat only the local implication needed by the package.
- Prefer one explicit requirement over several paraphrases of the same requirement.
- Background/lore may stay when it helps the reader understand the gameplay or production intent; do not expand it when it has no downstream effect.
- Brevity is not the goal by itself. If removing a detail would make a production role guess, keep the detail.

## Canonical document order

For the current approved gameplay-production template, use this order:

```text
1. Overview
2. Gameplay Flow
3. Global Development
4+. Gameplay Packages
     A. Gameplay Overview
     B. Level Design
     C. Developer
```

The exact number of Gameplay Flow pages, Global Development pages, and Gameplay Packages follows project needs. Do not force Aftershock's page count or objective count onto another project.

If a project requires a materially different document family, do not deform this template to fit it. Surface the template/profile choice as a material decision before rendering.

## 1. Overview

Must explain enough for a new team member to understand the project:

- project context;
- player/user role;
- main experience;
- game/project information that materially affects production;
- complete journey or stage overview;
- main shared systems;
- final result or end state when relevant;
- stable terms needed to understand the overview.

Avoid implementation class names, coordinates, per-package reset detail, and long formulas here unless the project specifically requires them at overview level.

## 2. Gameplay Flow

Explain the journey chronologically. Each material stage should make clear:

- where the player is / what context they enter;
- what they experience or do;
- the main obstacle, change, or interaction;
- the result of that stage;
- where progression goes next.

This section communicates the experience and handoff between stages. It is not the developer implementation checklist.

## 3. Global Development

Use only the global pages the project actually needs. Typical owners include:

- Development Overview;
- Game / Session System;
- Data and Reset;
- Shared Gameplay Development;
- another genuinely global system.

Global pages own rules shared by multiple packages. Do not duplicate the full global rule inside every package; repeat only the local implication needed by that role.

## 4+. Gameplay Package

A Gameplay Package represents a production-relevant gameplay section such as an Introduction, Objective, Transition, Ending, Stage, Station, or standalone gameplay unit.

Every package that materially requires production work uses the three-page structure below.

### A. Gameplay Overview

Required when applicable:

- local context;
- package type / label;
- main objective;
- intended result and purpose;
- estimated time when meaningful;
- start condition;
- valid end condition;
- blocked/fail/retry condition when relevant;
- ordered player flow;
- scoring summary or completion behavior;
- handoff to the next package;
- local Terms Used.

The page describes **what the player experiences and what counts as success**.

### B. Level Design

Required when the package needs build/layout work:

- concise local overview;
- Level Design flow in production order;
- grouped build requirements;
- Build & Visual requirement for each meaningful object/area;
- Gameplay Function for each meaningful object/area;
- only dimensions/quantities that materially affect gameplay or production;
- important build notes and constraints;
- local Terms Used.

Do not hide gameplay function inside visual prose. Level Design should know both what to build and why it exists.

### C. Developer

Required when the package needs runtime implementation:

- concise local overview;
- chronological trigger → behavior → data → result flow;
- grouped implementation requirements;
- scoring or completion data;
- recording/persistence requirements when applicable;
- duplicate-prevention behavior;
- interruption / disconnect behavior when applicable;
- reset behavior;
- verification/acceptance behavior;
- important implementation notes;
- local Terms Used.

Describe product/runtime behavior. Do not invent class names, file names, APIs, or architecture unless the source explicitly requires them.

## Scoring contract

If a package produces a score, define enough to implement it without guessing:

- score name and scale;
- score components;
- component weights when weighted scoring is used;
- target/standard or success basis;
- bonus/reduction behavior when applicable;
- timer start and stop;
- excluded time when applicable;
- no-score / invalid-run condition;
- recorded data;
- duplicate prevention;
- relationship to final result;
- exact formula only when exact math is actually product-critical.

If numeric component weights are used, they must total 100% unless the approved design explicitly defines another model.

## Completion-data contract

A package that does **not** produce an Objective Score must not receive an artificial score just to fill the template. Define instead:

- `produces_score: false`;
- valid completion condition;
- recorded completion/progress data;
- interruption behavior when relevant;
- duplicate prevention;
- handoff result.

## Terms Used

Use Terms Used only for project-specific or production-critical terminology.

Each term should have:

- stable key;
- label (EN and ID when available);
- concise definition;
- optional aliases when the same term appears in another approved form.

Do not over-tag ordinary language.

## Critical information

Treat these as critical when they affect the project:

- player/session/arena count;
- package/stage order;
- important quantities;
- target time and timer boundaries;
- scoring weights/inputs;
- completion and invalid/no-score conditions;
- handoff items/state;
- interruption/disconnect behavior;
- reset behavior;
- final-result rules.

Flow 3 must not hide missing critical information behind vague text such as “use the configured amount.” If required critical information is still unresolved, return the affected requirement to Flow 2 instead of rendering a polished guess.

## Canonical-content gate

`content.md` is ready for rendering when:

- Flow 2 state is `ready_for_prd`;
- every included material statement is supported by source/recovered requirements/approved decisions;
- required package pages have enough local context for their target role;
- each included detail serves a production/readability purpose and optional sections are not filled merely for completeness;
- scoring or completion behavior is explicit where relevant;
- explanatory prose is plain, concrete, and free of unnecessary filler without altering technical meaning;
- no unresolved high-impact Proposal or Blocked item affects the requested document;
- no visible placeholder such as `TBD`, `TODO`, `FIXME`, `[OPEN]`, or equivalent remains in required content.
