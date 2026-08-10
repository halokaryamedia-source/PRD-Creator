# Workspace Agent Rules

This repository is the project memory. Chat history is supporting context, never the canonical owner of project state.

## Branch Policy

- `Local` is the permanent working/development authority.
- Perform normal implementation and documentation work directly on `Local`.
- Do not create per-flow/per-task branches or routine pull requests.
- `main` remains a stable baseline and is changed only when the user explicitly requests it.
- Older non-`Local` work branches are non-authoritative unless explicitly reactivated.

## Mandatory Boot

At the start of material work:

1. read `CONTEXT.md`;
2. read `docs/knowledge/next-action.md`;
3. read only the foundation rule relevant to the active flow;
4. inspect the affected kit and project source/state/canonical work/output;
5. use `docs/knowledge/minimal-nav.md` when ownership is unclear.

Do not broad-read every reference, saved project, old output, or Archived file by default.

## Repository Continuity

- `CONTEXT.md` owns stable workspace facts/terminology.
- `docs/knowledge/next-action.md` owns current goal/status/completed boundary and exactly one next step.
- `docs/knowledge/decision-log.md` owns durable decisions/reasons.
- `docs/foundation/` owns durable production policy.
- active kit files own current flow procedure.
- project originals + approved project decisions own project-specific facts/design intent.
- `state/requirement-register.yaml` owns normalized requirement state after Flow 2.
- `work/content.md` owns canonical PRD meaning through Flow 3/4.
- Flow 4 acceptance/handoff records whether an exact PRD revision is usable; it does not change project meaning.
- `work/voice-requirements.md` owns which voice moments exist and what they must communicate after Flow 5.
- `work/voice-production.md` owns final spoken wording/performance notation after Flow 6.
- `state/voice-state.yaml` owns the downstream voice lifecycle status/revision/next step.
- `output/Voice Production.docx` is derived presentation; never edit it as the source of truth.
- generated HTML/DOCX/audio never outrank their canonical upstream owners.

Before ending material work, update only the owner whose state actually changed.

## Source / Decision Precedence

Use this order when resolving project-content conflicts:

1. current explicit user instruction;
2. approved project-specific decisions;
3. authoritative project source;
4. normalized requirement state derived from those sources/decisions;
5. accepted canonical PRD for downstream production;
6. accepted Voice Requirements for voice-moment scope;
7. durable workspace/foundation rules;
8. affected active kit instructions;
9. approved reference/Golden Sample for demonstrated structure/quality only;
10. prior generated output/chat/history as supporting context only.

Do not silently rewrite historical facts or approved decisions.

## Prompt Assistance

The user's prompt defines intent; it does not need to be a complete production specification.

Before asking for more information:

1. inspect repository state and supplied sources;
2. preserve authoritative facts/decisions;
3. distinguish weak explanation from a true missing decision;
4. complete low-risk gaps only when current policy allows it;
5. ask only when a high-impact unresolved decision cannot be recovered safely;
6. persist resolved decisions so later sessions do not ask again.

## Sample / Reference Rule

A sample demonstrates structure, presentation, density, tone, or quality only to the extent explicitly defined by its owner.

Do not promote sample-specific content into generic policy. Sample objective counts, characters, mechanics, scoring, voice counts, durations, speakers, tags, or lines do not become requirements for another project.

## Voice Production Boundary

- Flow 5 starts from a current `handoff_ready` PRD and defines `work/voice-requirements.md`.
- Flow 6 starts only from `voice_requirements_ready`.
- Flow 6 must preserve the exact Voice ID set and voice type unless Flow 5 scope is explicitly reopened.
- `work/voice-production.md` contains final spoken wording, performance directions, emphasis, pauses, line breaks, and estimated duration.
- performance directions describe delivery; they cannot create a new event, speaker, channel, mechanic, reward, or project fact.
- `Voice Production.docx` is generated from canonical Markdown and is not the editable authority.
- unresolved project facts route upstream instead of being repaired in dialogue.
- Flow 7 owns final voice validation/delivery and must not be self-approved during Flow 6.

Canonical procedures:

- `kits/voice-production-kit/VOICE-EXTRACTION.md`
- `kits/voice-production-kit/SCRIPT-PRODUCTION.md`
- `kits/voice-production-kit/DOCX-FORMAT.md`

## Edit Gate

Before creating/moving/changing a file:

- identify its canonical owner;
- inspect whether an existing file already owns that responsibility;
- extend/correct before creating a parallel system;
- keep source, state, canonical work, derived data, and final output separate;
- do not revive Archived schemas/process layers without a proved current need.

`No change required` is valid.

## Anti-Slop Baseline

- Understand the whole request before optimizing one section.
- Prefer the smallest complete change.
- Every changed file must trace to the active goal.
- Do not widen scope because adjacent improvements are visible.
- Do not invent facts, mechanics, lore, scoring, triggers, rewards, quantities, speakers, channels, or approvals.
- Do not hide uncertainty behind polished prose.
- Do not use rendering or voice writing to solve an upstream definition problem.
- Do not repeatedly patch symptoms when the content owner/rule is wrong.
- If the same correction direction fails twice without new evidence, re-diagnose.
- Do not claim approval, validation, generation quality, or delivery that did not occur.

## Evidence Labels

Use only when they resolve real uncertainty:

- `CURRENT-WORKSPACE VERIFIED` — exact claim/output checked in current workspace.
- `REFERENCE VERIFIED` — approved reference demonstrates the relevant contract, not current-project correctness.
- `EXECUTION PROOF REQUIRED` — implementation exists but relevant real-project execution is still missing.
- `UNSUPPORTED` — evidence shows the method should not be relied on.
- `UNKNOWN` — evidence is insufficient/conflicting.

## Production Boundary

- Project Document Generator owns Flow 2–4.
- Voice Production Kit Flow 5 owns accepted PRD → voice requirements.
- Voice Production Kit Flow 6 owns voice requirements → canonical performance script + derived DOCX.
- Flow 7 owns final voice validation/delivery.

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
