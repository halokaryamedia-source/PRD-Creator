# Workspace Agent Rules

This repository is the project memory. Chat history is supporting context, never the canonical owner of project state.

## Branch Policy

- `Local` is the permanent working/development authority.
- Perform normal implementation and documentation work directly on `Local`.
- Do not create per-flow/per-task branches or routine pull requests.
- `main` remains a stable baseline and is changed only when the user explicitly requests it.
- Any older `agent/*` branch is non-authoritative unless the user explicitly reactivates it.

## Mandatory Boot

At the start of every material session:

1. read `CONTEXT.md` for stable facts and terminology;
2. read `docs/knowledge/next-action.md` for the single active task and continuation state;
3. read only the relevant `docs/foundation/` rule;
4. inspect the affected kit, project source, canonical content, or output before changing behavior;
5. use `docs/knowledge/minimal-nav.md` when ownership is unclear.

Do not broad-read every reference, old output, saved project, or Archived file by default.

## Repository Continuity

- `CONTEXT.md` owns stable workspace facts and terminology.
- `docs/knowledge/next-action.md` owns current goal/status/completed boundary and exactly one next step.
- `docs/knowledge/decision-log.md` owns durable decisions and reasons.
- `docs/foundation/` owns durable production policy.
- active kit files own current production procedure.
- project originals + approved project decisions own project-specific facts/design intent.
- after Flow 2, `state/requirement-register.yaml` owns normalized traceable requirement state.
- during Flow 3, `work/content.md` owns canonical PRD meaning.
- `work/render-data.json` is a derived rendering projection only.
- generated HTML/output never outranks canonical content or its source/approved decisions.

Before ending material work, update only the canonical owner whose state actually changed.

## Current Instruction And Source Precedence

Use this order when resolving conflicts:

1. current user instruction for the present task;
2. explicit approved project decisions;
3. authoritative project source documents;
4. normalized requirement state derived from those sources/decisions;
5. durable workspace/foundation rules;
6. affected active kit instructions;
7. approved Golden Sample/reference for structure/presentation/demonstrated quality only;
8. prior generated output and chat/history as supporting context only.

A current instruction can change intent, but do not silently rewrite historical facts or previously approved decisions. Record material new decisions in their canonical owner.

## Prompt Assistance

The user's prompt defines intent; it does not need to be a complete production specification.

Before asking for more information:

1. inspect repository state and supplied project sources;
2. preserve authoritative facts and decisions;
3. distinguish missing explanation from a true missing design decision;
4. complete low-risk gaps from strong context when current policy allows it;
5. ask only when a high-impact unresolved decision cannot be recovered safely;
6. persist the resolved decision so later sessions do not ask again.

## Sample / Golden Reference Rule

Treat a sample as evidence of structure, presentation, density, tone, or quality only to the extent explicitly defined by its owner.

Do not promote sample-specific content into generic policy. A sample objective count, character, mechanic, story beat, scoring rule, or voice line does not become mandatory for another project.

## Edit Gate

Before creating, moving, or changing a file:

- identify its canonical owner;
- inspect whether an existing file already owns that responsibility;
- extend/correct before creating a parallel system;
- keep project source, state, canonical work, derived render data, and final output separate;
- do not revive Archived schemas/validators/process layers without a proved current need.

`No change required` is valid.

## Anti-Slop Baseline

- Understand the whole request before optimizing one section.
- Prefer the smallest complete change.
- Every changed file must trace to the active goal.
- Do not widen scope because adjacent improvements are visible.
- Do not invent project facts, mechanics, lore, scoring, triggers, rewards, quantities, or approvals.
- Do not hide uncertainty behind polished prose.
- Do not use rendering to solve a content-definition problem.
- Do not repeatedly patch symptoms when the content owner or rule is wrong.
- If the same correction direction fails twice without new evidence, re-diagnose.
- Do not claim approval, validation, successful generation, or delivery that did not occur.

## Evidence / Completion Status

Use labels only when they resolve real uncertainty:

- `CURRENT-WORKSPACE VERIFIED` — exact claim/output checked in current workspace.
- `REFERENCE VERIFIED` — approved reference demonstrates the relevant contract, but not current-project correctness.
- `EXECUTION PROOF REQUIRED` — source/rules exist, but relevant execution/output check has not been performed.
- `UNSUPPORTED` — evidence shows the method should not be relied on.
- `UNKNOWN` — evidence is insufficient or materially conflicting.

## Production Boundary

- **Project Document Generator** owns source/requirement recovery plus canonical PRD generation/rendering through Flow 3.
- **Flow 4** owns whether generated PRD is actually development-ready and suitable for team handoff.
- **Voice Production Kit** consumes sufficiently mature upstream facts and must not become a second PRD designer.

Do not solve an upstream content-definition problem inside Voice Production merely to make a script easier to write.

## User-Facing Reporting

For a material implementation slice, report:

```text
Status:
Implemented:
Preserved / not changed:
Evidence:
Next step:
```

Use exactly one next step.
