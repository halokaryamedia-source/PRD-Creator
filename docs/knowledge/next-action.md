# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Current Status

`PRD_FLOW_SIMPLIFIED_GOLDEN_TEMPLATE_LOCKED_REAL_SAMPLE_NEXT`

Working branch: **`Local` only**.

## Golden Sample decision

The approved Golden Sample is intentionally the required template authority for this PRD family.

Do **not** replace it with a reduced/minimal shell merely to make the template smaller or more generic.

Preserve its output foundation:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Also preserve the approved visual/navigation/component foundation unless a concrete defect or explicit user decision requires a template change.

Efficiency work belongs in the **generation process and content density**, not in changing the final structure the user expects.

## Completed — PRD writing/content refinement

The PRD owner already protects:

- source fidelity and supported completion;
- production-relevant requirement granularity;
- plain, concrete anti-AI-slop technical prose;
- stable terminology and technical values;
- minimum sufficient detail;
- Gameplay / Level Design / Developer ownership separation.

## Completed — PRD flow simplification

The end-to-end PRD workflow is now expressed as three macro steps:

```text
1. UNDERSTAND  — Flow 2
2. BUILD PRD   — Flow 3
3. REVIEW      — Flow 4
```

This replaces the previous mental model of 11 separate stages. Internal files/checks still exist, but they are implementation details rather than user-facing ceremonies.

### Flow 2

- inspect all available source before asking questions;
- apply supported Clarification/Completion first;
- batch remaining high-impact Proposal/Blocked decisions into one concise review when possible;
- `work/review.md` is conditional rather than a mandatory user approval round.

### Flow 3

- preserve the Golden Sample structure/foundation;
- create canonical `content.md`;
- derive `render-data.json` internally;
- render `final.html` through the approved Golden Sample template;
- keep role pages concise when local work is small instead of inventing filler;
- do not remove role pages just to shorten the document.

### Flow 4

- run mechanical validation;
- perform one integrated review through New Reader, Level Designer, Developer, and Project Consistency lenses;
- record each finding once in a shared findings table;
- writing quality and information density stay inside the same review rather than becoming extra gates.

## Changed owners

```text
kits/project-document-generator/WORKFLOW.md
kits/project-document-generator/SOURCE-INTAKE.md
kits/project-document-generator/CONTENT-CONTRACT.md
kits/project-document-generator/RENDERING.md
kits/project-document-generator/VALIDATION.md
```

The approved Golden Sample HTML template and renderer implementation were intentionally **not changed** by this flow refinement.

## Anti-overdevelopment boundary

Do not add:

- a new PRD workflow engine;
- a new schema/profile framework;
- AI-writing detector/score;
- another approval state;
- a replacement template system;
- automatic template cleanup merely because the Golden Sample is large.

Use the smallest change that improves real project output while preserving the document foundation the user approved.

## Next Step

Use the refined three-step PRD flow on one real project/sample and compare the actual result against the Golden Sample expectations:

- same structural/foundation quality;
- clear player/project context;
- useful Gameplay / Level Design / Developer pages;
- no invented filler;
- concise source/decision interaction;
- plain, natural technical language;
- enough detail for production roles without unnecessary repetition.

If the practical result is good, stop PRD policy refinement and proceed to Voice skill review only when the user chooses to do so.
