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

1. read `CONTEXT.md`;
2. read `docs/knowledge/next-action.md`;
3. read only the foundation rule relevant to the active flow;
4. inspect the affected kit, project source/state/canonical work, or output before changing behavior;
5. use `docs/knowledge/minimal-nav.md` when ownership is unclear.

Do not broad-read every reference, old output, saved project, or Archived file by default.

## Repository Continuity

- `CONTEXT.md` owns stable workspace facts/terminology.
- `docs/knowledge/next-action.md` owns the current goal/status/completed boundary and exactly one next step.
- `docs/knowledge/decision-log.md` owns durable decisions/reasons.
- `docs/foundation/` owns durable production policy.
- active kit files own current flow procedure.
- project originals + approved project decisions own project-specific facts/design intent.
- `state/requirement-register.yaml` owns normalized traceable requirement state after Flow 2.
- `work/content.md` owns canonical PRD meaning through Flow 3/4.
- `work/render-data.json` is derived rendering data only.
- Flow 4 acceptance/handoff records whether an exact PRD revision is usable; they do not change project meaning.
- after Flow 5, `work/voice-requirements.md` owns canonical voice-moment scope/meaning.
- `state/voice-state.yaml` owns Flow 5 status/revision/next step, not the full voice content.
- generated HTML, voice scripts, DOCX, or other outputs never outrank their canonical upstream owners.

Before ending material work, update only the canonical owner whose state actually changed.

## Current Instruction And Source Precedence

Use this order when resolving conflicts:

1. current user instruction for the present task;
2. explicit approved project decisions;
3. authoritative project source;
4. normalized requirement state derived from those sources/decisions;
5. accepted canonical PRD content for downstream production;
6. durable workspace/foundation rules;
7. affected active kit instructions;
8. approved Golden Sample/reference for demonstrated structure/quality only;
9. prior generated output and chat/history as supporting context only.

A current instruction can change intent, but do not silently rewrite historical facts or approved decisions. Record material new decisions in their canonical owner.

## Prompt Assistance

The user's prompt defines intent; it does not need to be a complete production specification.

Before asking for more information:

1. inspect repository state and supplied sources;
2. preserve authoritative facts/decisions;
3. distinguish weak explanation from a true missing decision;
4. complete low-risk gaps from strong context when current policy allows it;
5. ask only when a high-impact unresolved decision cannot be recovered safely;
6. persist the resolved decision so later sessions do not ask again.

## Sample / Golden Reference Rule

Treat a sample as evidence of structure, presentation, density, tone, or quality only to the extent explicitly defined by its owner.

Do not promote sample-specific content into generic policy. A sample objective count, character, mechanic, scoring rule, voice type count, or voice line does not become mandatory for another project.

## Voice Production Boundary

- Flow 5 starts from a current `handoff_ready` PRD revision.
- `work/voice-requirements.md` defines **which voice moments are justified and what each must communicate**.
- Flow 5 never writes final spoken wording, ElevenLabs directions, emphasis, pauses, duration, settings, or voice selection.
- A gameplay package may have zero voice moments.
- Radio Communication requires an approved remote communication channel; do not invent one from the reference.
- If a required voice moment depends on an unresolved speaker/channel/trigger/story decision, route the issue upstream.
- Flow 6 must not add a voice moment absent from accepted Flow 5 requirements unless scope is explicitly reopened.

Canonical Flow 5 procedure: `kits/voice-production-kit/VOICE-EXTRACTION.md`.

## Edit Gate

Before creating/moving/changing a file:

- identify its canonical owner;
- inspect whether an existing file already owns that responsibility;
- extend/correct before creating a parallel system;
- keep project source, state, canonical work, derived data, and final output separate;
- do not revive Archived schemas/validators/process layers without a proved current need.

`No change required` is valid.

## Anti-Slop Baseline

- Understand the whole request before optimizing one section.
- Prefer the smallest complete change.
- Every changed file must trace to the active goal.
- Do not widen scope because adjacent improvements are visible.
- Do not invent project facts, mechanics, lore, scoring, triggers, rewards, quantities, speakers, channels, or approvals.
- Do not hide uncertainty behind polished prose.
- Do not use rendering or voice writing to solve an upstream content-definition problem.
- Do not repeatedly patch symptoms when the content owner/rule is wrong.
- If the same correction direction fails twice without new evidence, re-diagnose.
- Do not claim approval, validation, successful generation, or delivery that did not occur.

## Evidence / Completion Status

Use labels only when they resolve real uncertainty:

- `CURRENT-WORKSPACE VERIFIED` — exact claim/output checked in current workspace.
- `REFERENCE VERIFIED` — approved reference demonstrates the relevant contract, but not current-project correctness.
- `EXECUTION PROOF REQUIRED` — rules/implementation exist, but relevant real-project execution has not been performed.
- `UNSUPPORTED` — evidence shows the method should not be relied on.
- `UNKNOWN` — evidence is insufficient or materially conflicting.

## Production Boundary

- **Project Document Generator** owns Flow 2–4: source recovery, canonical PRD, rendering, and PRD handoff readiness.
- **Voice Production Kit Flow 5** owns accepted-PRD → traceable voice requirements.
- **Voice Production Kit Flow 6** will own voice requirements → ElevenLabs-ready performance scripts/DOCX.
- Flow 7 will own final voice validation/delivery.

Do not solve an upstream project-definition problem inside downstream voice production.

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
