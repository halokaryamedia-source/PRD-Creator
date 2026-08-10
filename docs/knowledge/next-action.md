# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Current Status

`PRD_USER_EFFICIENCY_REFINEMENT_IMPLEMENTED_CONTINUE_PRE_SAMPLE_AUDIT`

Working branch: **`Local` only**.

## Golden Sample decision

The approved Golden Sample remains the required template authority for this PRD family.

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

Efficiency work belongs in the production process and content density, not in removing this structure or replacing the template with a smaller generic shell.

## Implemented — user-efficiency routing

Normal project production is now explicitly separated from repository/system Developing work.

```text
normal PRD / Voice project production
→ Production Execution
→ matching production owner directly
→ no development-brief

change PRD-Creator itself
→ Developing
→ development-brief
```

This prevents meta planning from appearing before ordinary PRD production.

## Implemented — automatic PRD project bootstrap

For a new PRD project the agent now owns:

- project name/slug derivation;
- active workspace creation/reuse;
- original-source preservation;
- internal SRC/REQ ID assignment;
- minimum current-Flow state/work setup.

The user should not be asked to manage repository structure unless project identity is genuinely ambiguous.

## Implemented — grouped decision interaction

Flow 2 now finishes source inspection/recovery first, then groups only real high-impact decisions.

When a responsible recommendation exists, each decision includes:

```text
Recommended
Reason
Impact
```

The user may approve all recommendations in one response or override only named exceptions. Recommendations remain pending until explicitly approved.

## Implemented — revision fast path

Bounded approved changes to an existing PRD use a delta path:

```text
approved change
→ affected requirements/sections only
→ necessary cross-references
→ regenerate render data / HTML
→ one current mechanical check
→ targeted semantic/visual re-review only where invalidated
→ updated final PRD
```

Unchanged sources, resolved decisions, unrelated packages, and unaffected review evidence are not replayed by default.

## Implemented — minimal user-facing delivery

Normal PRD completion should surface only:

```text
Final PRD
+ material adjustments/recovered decisions worth knowing
+ any real remaining attention item
```

Internal YAML/state, IDs, render data, acceptance tables, validator JSON, CI logs, and repository mechanics stay internal unless requested or needed to explain a blocker.

## Implemented — visual sanity inside REVIEW

Flow 4 keeps one REVIEW stage. When actual rendered/browser/page inspection is available, it includes one practical visual sanity pass for overflow, broken components/navigation, unreadable density, and inspected responsive/print/page-break defects.

This is not a new Flow, score, detector, pixel-diff system, or extra user approval round.

If visual inspection is unavailable, record `NOT PROVEN` and do not claim visual quality was verified.

## Changed owners

```text
AGENTS.md
README.md
.agents/skills/development-brief/SKILL.md
docs/knowledge/flow.md
docs/knowledge/flows/development-flow.md
docs/knowledge/skills/activation-matrix.md
kits/project-document-generator/SKILL.md
kits/project-document-generator/WORKFLOW.md
kits/project-document-generator/SOURCE-INTAKE.md
kits/project-document-generator/VALIDATION.md
```

The approved Golden Sample template, renderer implementation, validator code, and production tests are intentionally unchanged by this workflow-efficiency batch.

## Testing cadence

Per current user direction, do **not** perform repeated manual/local project tests after each small refinement.

Finish the remaining PRD workflow/skill readiness audit first. Use repository/CI consistency verification for repository changes as appropriate, then perform practical/manual real-project testing only when the PRD side is ready as one coherent system.

## Remaining pre-sample audit items

Before manual/real-project testing, review only unresolved workflow issues that could still materially burden the user or produce misleading output, especially:

- language/bilingual behavior and silent fallback semantics;
- whether any remaining mandatory handoff state/artifact should be changed only together with the later Voice boundary review;
- any direct routing/documentation drift exposed by the current efficiency changes.

Do not reopen Golden Sample structure, add new skills/frameworks, or refactor `content.md → render-data.json` without real evidence.

## Next Step

Continue the PRD pre-sample audit for the remaining user-facing workflow risks above. Do not start manual real-project testing yet.
