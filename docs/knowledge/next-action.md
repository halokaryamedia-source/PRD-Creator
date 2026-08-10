# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Current Status

`PRD_GOLDEN_OUTPUT_FIDELITY_REMEDIATED_PRE_SAMPLE_AUDIT_CONTINUES`

Working branch: **`Local` only**.

## Golden Sample decision

The approved Golden Sample remains the required output authority for this gameplay-document family.

Preserve both:

```text
Hierarchy
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

and its reusable page composition/component language.

Do not replace it with a smaller shell, adaptive template family, or generic report layout.

## Root cause found — Golden drift

The previous renderer used the Golden HTML mostly as a CSS/JS shell, but replaced `.document-main` with simplified generic page composition.

This allowed a document to use the Golden stylesheet while still diverging materially in:

- package title/subtitle and tabs;
- narrative Gameplay Flow composition;
- context blocks/cards;
- Gameplay Information table;
- role-sequence treatment;
- Level Design `Area Size / Build and Visual / Gameplay Function` structure;
- grouped Developer requirements;
- inline scoring/completion treatment;
- Important Notes card grids;
- Terms Used markup;
- project-branded footers.

Mechanical validation previously checked page existence/navigation but did not protect these Golden composition contracts.

## Implemented — Golden page composition

The active PRD contract now treats Golden page composition as part of Flow 3 correctness, not optional styling.

Current renderer projection is aligned to these Golden families:

```text
Gameplay Flow
→ narrative sequence / transition

Global Development
→ shared tabs
→ context block
→ Development Flow cards
→ grouped production table
→ notes card grid

Gameplay Overview
→ package title/subtitle + 1/2/3 tabs
→ Gameplay Context / Main Objective / Result
→ Gameplay Information production table
→ role-sequence

Level Design
→ package title/subtitle + tabs
→ Level Design Overview
→ Design Flow cards
→ Golden 5-column Build Requirements table
→ notes card grid

Developer
→ package title/subtitle + tabs
→ Developer Overview
→ Development Flow cards
→ grouped Golden Development Requirements table
   with scoring/completion/reset integrated
→ notes card grid
```

Footer identity now derives from the project rather than a hardcoded MIVUBI footer brand.

## Implemented — lightweight fidelity guard

The existing mechanical Flow 4 validator now checks a small set of Golden semantic DOM/class markers per generated page.

This catches regression back to generic page composition without adding:

- pixel diff;
- screenshot baseline;
- visual score;
- AI "looks like Golden" evaluator;
- schema/profile framework;
- full DOM snapshot.

Actual Golden visual quality still requires real final browser/page inspection when manual testing begins.

## Existing user-efficiency rules remain active

- normal PRD creation/revision = Production Execution, no `development-brief`;
- automatic project bootstrap;
- inspect all source before grouped decisions;
- `Recommended / Reason / Impact` decision batches;
- revision delta fast path;
- minimal user-facing delivery;
- one integrated REVIEW with visual sanity when actual visual inspection is available.

## Template boundary

The approved Golden Sample HTML template itself was intentionally **not changed** by the fidelity remediation.

The fix is in the canonical page-composition contract and renderer projection, because that was the first wrong owner.

## Testing cadence

Per current user direction:

- do not run repeated manual/local project tests during refinement;
- finish PRD pre-sample readiness first;
- repository/CI verification may run once after a coherent repository batch;
- perform one practical/manual real-project test only when the PRD side is ready as a coherent system.

## Remaining pre-sample audit

Do not reopen Golden structure unless a new concrete defect proves it necessary.

Remaining PRD-side review should now focus only on unresolved user-facing risks, especially:

1. language/bilingual behavior and silent fallback semantics;
2. direct routing/documentation drift, if any remains;
3. handoff-state/artifact simplification only together with the later Voice boundary review.

Do not refactor `content.md → render-data.json`, create another template system, or add another skill/framework without real evidence.

## Next Step

Complete the remaining PRD pre-sample audit above. Do not start manual/real-project testing yet.
