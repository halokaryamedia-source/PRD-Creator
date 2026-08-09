# Workspace Agent Rules

This repository is the project memory. Chat history is supporting context, never the canonical owner of project state.

## Mandatory Boot

At the start of every material session:

1. read `CONTEXT.md` for stable facts and terminology;
2. read `docs/knowledge/next-action.md` for the single active task and continuation state;
3. read only the relevant `docs/foundation/` policy;
4. inspect the affected kit, project source, or generated output before changing behavior;
5. use `docs/knowledge/minimal-nav.md` when ownership is unclear.

Do not broad-read every reference, old output, saved project, or historical note by default.

## Repository Continuity

- `CONTEXT.md` owns stable workspace facts and terminology.
- `docs/knowledge/next-action.md` owns the current goal, status, frozen boundaries, completed slice, and exactly one next step.
- `docs/knowledge/decision-log.md` owns durable decisions and their reasons.
- `docs/foundation/` owns durable product and workflow policy.
- kit files own their current executable/document-production instructions.
- project source plus approved project decisions own project-specific factual/design content.
- generated output is never automatically more authoritative than its source and approved decisions.

Before ending material work, update only the canonical owner whose state actually changed.

## Current Instruction And Source Precedence

Use this order when resolving conflicts:

1. current user instruction for the present task;
2. explicit approved project decisions;
3. authoritative project source documents;
4. durable workspace/foundation rules;
5. affected kit instructions;
6. approved Golden Sample/reference for structure, presentation, and demonstrated quality only;
7. prior chat/history as supporting context only.

A current user instruction can change intent, but do not silently rewrite historical facts or previously approved decisions. Record a material new decision in its canonical owner.

## Prompt Assistance

The user's prompt defines intent; it does not need to be a complete production specification.

Before asking the user for more information:

1. inspect repository state and supplied project sources;
2. preserve already-authoritative facts and decisions;
3. distinguish missing explanation from a real missing design decision;
4. complete low-risk gaps from strong context when the active kit allows it;
5. ask only when a high-impact unresolved decision cannot be recovered safely;
6. record approved material decisions so later sessions do not ask again.

## Sample / Golden Reference Rule

Treat a sample as evidence of structure, presentation, density, tone, or quality only to the extent explicitly defined by its owner.

Do not promote sample-specific content into generic policy. For example, a sample objective count, character, mechanic, story beat, or voice line does not become mandatory for another project unless explicitly required.

## Edit Gate

Before creating, moving, or changing a file:

- identify its canonical owner;
- inspect whether an existing file already owns that responsibility;
- extend or correct the existing owner before creating a parallel system;
- keep per-project source, work-in-progress, and final deliverables separate;
- do not create validators, manifests, reports, templates, abstractions, or compatibility layers for hypothetical future needs.

`No change required` is a valid result.

## Anti-Slop Baseline

- Understand the whole request before optimizing one section.
- Prefer the smallest complete change.
- Every changed file must trace to the active goal.
- Do not widen scope because adjacent improvements are visible.
- Do not invent project facts, mechanics, lore, scoring, triggers, rewards, or approvals.
- Do not hide uncertainty behind polished prose.
- Do not repeatedly patch the symptom when the content owner or rule is wrong.
- If the same correction direction fails twice without new evidence, re-diagnose before continuing.
- Do not claim approval, validation, successful generation, or delivery that did not actually occur.

## Evidence / Completion Status

Use status labels only when they resolve a real uncertainty:

- `CURRENT-WORKSPACE VERIFIED` — the exact claim/output has been checked in the current workspace.
- `REFERENCE VERIFIED` — an approved reference demonstrates the structure/quality contract, but not necessarily the current project's correctness.
- `EXECUTION PROOF REQUIRED` — source/rules exist, but the relevant generation or output check has not yet been performed.
- `UNSUPPORTED` — available evidence shows the requested method should not be relied on.
- `UNKNOWN` — evidence is insufficient or materially conflicting.

Do not use these labels ceremonially for routine text edits.

## Production Boundary

The two current kits have different responsibilities:

- **Project Document Generator** owns requirement recovery, content completion within its approval rules, canonical project documentation, and approved-template rendering.
- **Voice Production Kit** consumes sufficiently mature gameplay/story/project facts and produces ElevenLabs-ready voice performance scripts. It must not become a second PRD designer.

Do not solve a PRD/content-definition problem inside the Voice Production Kit merely to make the voice script easier to write.

## User-Facing Reporting

For a material implementation slice, report:

```text
Status:
Implemented:
Preserved / not changed:
Evidence:
Next step:
```

Use exactly one next step so the project has one clear continuation point.
