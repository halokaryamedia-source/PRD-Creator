# Workspace Agent Rules

This repository is project memory. Chat history is supporting context, never the canonical owner of project state.

## Branch Policy

- `Local` is the permanent working/development authority.
- Perform normal implementation/documentation work directly on `Local`.
- Do not create per-flow/per-task branches or routine pull requests.
- `main` remains stable and changes only when explicitly requested.
- Older non-`Local` work branches are non-authoritative unless explicitly reactivated.

## Mandatory Boot

At the start of material work:

1. read `CONTEXT.md`;
2. read `docs/knowledge/next-action.md`;
3. read only the foundation rule relevant to the active boundary;
4. inspect the affected kit and project source/state/canonical work/output;
5. use `docs/knowledge/minimal-nav.md` when ownership is unclear.

Do not broad-read every reference, saved project, old output, or retired Git history by default.

## Repository Continuity

- `CONTEXT.md` owns stable workspace facts/terminology.
- `docs/knowledge/next-action.md` owns current goal/status/completed boundary and exactly one next step.
- `docs/knowledge/decision-log.md` owns durable decisions/reasons.
- `docs/foundation/` owns durable production policy.
- active kit files own current flow procedure.
- project originals + approved decisions own project-specific facts/design intent.
- `state/requirement-register.yaml` owns normalized requirement state after Flow 2.
- `work/content.md` owns canonical PRD meaning through Flow 3/4.
- Flow 4 acceptance/handoff records usability of an exact PRD revision; it does not change project meaning.
- `work/voice-requirements.md` owns Voice scope/required communication after Flow 5.
- `work/voice-production.md` owns final spoken/performance wording after Flow 6.
- `work/voice-acceptance.md` owns Flow 7 evidence/findings for the current voice revision.
- `state/voice-state.yaml` owns downstream Voice lifecycle status/revision/next step.
- `output/Voice Production.docx` is derived presentation; never edit it as source of truth.
- generated HTML/DOCX/audio never outrank canonical upstream owners or actual evidence.

Before ending material work, update only the owner whose state actually changed.

## Source / Decision Precedence

Use this order when resolving project-content conflicts:

1. current explicit user instruction;
2. approved project-specific decisions;
3. authoritative project source;
4. normalized requirement state;
5. accepted canonical PRD;
6. accepted Voice Requirements;
7. canonical Voice Production Script for wording/performance only;
8. durable workspace/foundation rules;
9. affected active kit instructions;
10. approved reference/Golden Sample for demonstrated quality only;
11. prior generated output/chat/history as supporting context only.

Do not silently rewrite historical facts or approved decisions.

## Prompt Assistance

The user's prompt defines intent; it does not need to be a complete specification.

Before asking for more information:

1. inspect repository state and supplied sources;
2. preserve authoritative facts/decisions;
3. distinguish weak explanation from a true missing decision;
4. complete low-risk gaps only when current policy permits it;
5. ask only when a high-impact unresolved decision cannot be recovered safely;
6. persist resolved decisions so later sessions do not ask again.

## Sample / Reference Rule

A sample demonstrates structure, presentation, density, tone, or quality only to the extent explicitly defined by its owner.

Sample objective counts, characters, mechanics, scoring, voice counts, durations, speakers, tags, lines, or pronunciation do not become requirements for another project.

## Voice Production Boundary

- Flow 5 defines `work/voice-requirements.md` from a current `handoff_ready` PRD.
- Flow 6 preserves the exact Voice ID/type set and creates `work/voice-production.md` + derived DOCX.
- Flow 7 validates the exact current script/DOCX revision through `VOICE-VALIDATION.md`.
- Flow 7 may reopen a root owner when a defect is found; it must not hide the fix in `voice-acceptance.md` or patch the DOCX directly.
- Critical/Major findings block `voice_delivery_ready`.
- DOCX visual acceptance requires rendered-page inspection.
- generated-audio quality is never claimed unless actual audio was supplied and reviewed.
- default delivery scope is script + DOCX unless the user explicitly includes generated audio.

Canonical Voice procedures:

- `kits/voice-production-kit/VOICE-EXTRACTION.md`
- `kits/voice-production-kit/SCRIPT-PRODUCTION.md`
- `kits/voice-production-kit/DOCX-FORMAT.md`
- `kits/voice-production-kit/VOICE-VALIDATION.md`

## Edit Gate

Before creating/moving/changing a file:

- identify its canonical owner;
- inspect whether an existing file already owns that responsibility;
- extend/correct before creating a parallel system;
- keep source, state, canonical work, derived data, evidence, and final output separate;
- do not revive retired schemas/process layers without a proved current need.

`No change required` is valid.

## Anti-Slop Baseline

- Understand the whole request before optimizing one section.
- Prefer the smallest complete change.
- Every changed file must trace to the active goal.
- Do not widen scope because adjacent improvements are visible.
- Do not invent facts, mechanics, lore, scoring, triggers, rewards, quantities, speakers, channels, pronunciations, or approvals.
- Do not hide uncertainty behind polished prose.
- Do not use rendering/voice writing/audit prose to solve an upstream definition problem.
- Do not repeatedly patch symptoms when the content owner/rule is wrong.
- If the same correction direction fails twice without new evidence, re-diagnose.
- Do not claim approval, validation, generation quality, or delivery that did not occur.

## Evidence Labels

Use only when they resolve real uncertainty:

- `CURRENT-WORKSPACE VERIFIED` — exact claim/output checked in current workspace.
- `REFERENCE VERIFIED` — reference demonstrates a contract, not current-project correctness.
- `EXECUTION PROOF REQUIRED` — implementation exists but relevant real-project execution is still missing.
- `UNSUPPORTED` — evidence shows the method should not be relied on.
- `UNKNOWN` — evidence is insufficient/conflicting.

## Production Boundary

- Project Document Generator owns Flow 2–4.
- Voice Production Kit owns Flow 5–7.
- Flow 1–7 plus real-project integration proof are complete; future changes are evidence-driven maintenance, not another production flow.

## User-Facing Reporting

For material implementation work, report:

```text
Status:
Implemented:
Preserved / not changed:
Evidence:
Next step:
```

Use exactly one next step.
