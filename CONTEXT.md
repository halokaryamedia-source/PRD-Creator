# PRD-Creator Context

Status: active production system  
Development branch: `develop`  
Verified integration baseline: `Local`  
Stable release branch: `main`

This file is the stable orientation layer for new sessions and repository Development. It explains what PRD-Creator is, its major authority boundaries, and where detailed owners live. It intentionally does not duplicate field schemas, rendering contracts, or detailed Flow procedures.

## Product

PRD-Creator turns uneven project discussion and source material into one approved project model, then produces development-ready documentation and production resources needed to build that same project.

The normal human-facing document may contain:

```text
01 Overview
02 Gameplay Flow
03 Development
04 Production Assets
```

01–03 use the approved PRD-core/Golden system. `04 Production Assets` is additive and comes from the same approved project model, not from a second design pass over generated 01–03.

Voice Production is downstream from accepted project/PRD meaning. It does not create a second source-intake authority.

## Canonical production sequence

```text
Flow 1  Repository Boot & Project Memory
Flow 2  Source Intake & Requirement Recovery
Flow 3  Project Document / PRD Generation
Flow 4  PRD Validation & Team Handoff
Flow 5  Voice Requirement Extraction
Flow 6  Eleven v3 Performance Script Production
Flow 7  Voice Validation & Delivery
```

There is no canonical Flow 8. Non-Voice Production Assets are a bounded capability inside the same PRD-Creator package.

High-level policy lives in `docs/foundation/`. Detailed production procedure lives in the matching `kits/prd-creator/` domain owner.

## Branch authority

```text
develop
→ active repository Development

Local
→ verified integration / stable working baseline

main
→ stable release
```

Promotion is directional:

```text
develop → Local → main
```

Each promotion is reviewed and gated. Use merge ancestry and synchronize the promoted commit back down after integration/release. Do not let `develop`, `Local`, and `main` accumulate independent stable-only changes.

Detailed GitHub execution remains owned by `GITHUB_RULES.md`; the durable branch decision is recorded under `docs/knowledge/decisions/`.

## Stable authority shape

```text
current user instruction
+ approved decisions
+ authoritative project source
→ approved project model
   ├─ canonical PRD core 01–03
   └─ justified non-Voice 04 Production Asset requirements
→ accepted PRD / handoff
→ optional Voice requirements
→ canonical Voice Production
→ derived project HTML / evidence
```

Authority decreases downstream. Generated HTML, render projections, reviews, and other derived artifacts do not repair or outrank canonical source.

If a downstream step exposes missing or contradictory upstream meaning, return only the affected decision to the correct upstream owner.

## Product boundaries

`kits/prd-creator/` is the single implementation/procedure package for Flow 2–7 plus bounded `04 Production Assets` completion.

```text
intake/             Flow 2 source + requirement recovery
document/           PRD core 01–03 contract + Flow 4 validation
production-assets/  exact non-Voice 04 resource/writing contract
voice/              Flow 5–7 Voice procedure/craft/evidence
renderer/           deterministic PRD + shared 04 presentation
validator/          PRD, handoff, and Voice mechanical gates
template/           approved Golden/runtime bytes
```

Project/PRD semantics and Voice semantics remain separate responsibilities even though they live in one product package.

## Project-data boundary

The public PRD-Creator repository owns the **system**, not live project/client production data.

`workspace/active/` and `workspace/archive/` are local/external mount conventions. Their project subdirectories are ignored by Git; only workspace guidance is tracked.

Project packages may live:

- locally under the ignored workspace paths;
- in a separate private/authorized repository;
- in another approved storage location.

Do not commit credentials, private client/source material, live requirement registers, project outputs, or other project-specific production state into this public system repository unless an explicit visibility decision authorizes it.

This boundary prevents new exposure. It does not erase material already present in historical commits; history cleanup is a separate destructive operation and must never be implied by ordinary repository cleanup.

## Golden / reference boundary

The approved Golden PRD artifact is binding for the PRD-core representation contract until the user approves a new design. Golden/reference material does not supply another project's gameplay facts, counts, timings, lore, scoring, speakers, or implementation decisions.

## Operating direction

- recover repository/project context before asking the user to repeat it;
- triage source by authority/relevance before deep reading;
- solve supported meaning before asking for decisions;
- preserve information completeness;
- use bounded revisions;
- prefer existing owners before creating files, skills, schemas, workflows, compatibility layers, or frameworks;
- use the cheapest proof that can falsify the active claim;
- historical audits/backlog/TODOs are not active work unless promoted by current continuation;
- `No change required` is valid;
- stop when requested scope is complete and sufficiently proven.

## Repository map

```text
AGENTS.md
→ top-level repository routing / continuity rules

GITHUB_RULES.md
→ GitHub execution, commit/history, CI/API/safety discipline

CONTEXT.md
→ stable product/repository orientation

docs/foundation/
→ durable Flow 1–7 production policy

docs/knowledge/
→ continuation, routing, ownership, decisions, evidence, backlog

.agents/skills/
→ reusable semantic judgment

kits/prd-creator/
→ categorized Flow 2–7 + bounded 04 procedure/implementation

workspace/
→ ignored local/external project-package mount points

tests/ + tools/ + .github/
→ repository engineering / repeatable verification / promotion gates
```

## Project package principle

Canonical work stays upstream; derived delivery can be regenerated.

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

`prd.html` is the human-facing project document. `context.md` and `index.json` are AI reading/navigation projections, not a second PRD authority.

`document.version` is project/release metadata, not an edit counter.

## Continuation

For new-chat context recovery and non-trivial Development, read `docs/knowledge/next-action.md` after this file.

`next-action.md` owns the active continuation boundary; current source/state owns actual implementation truth. If they disagree, reconcile the stale owner before continuing.
