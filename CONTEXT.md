# PRD-Creator Context

Status: active production repository  
Working branch: `Local`

This file is the stable orientation layer for new sessions and repository Developing. It explains **what PRD-Creator is, how its major boundaries fit together, and where detailed authority lives**. It intentionally does not duplicate exact field schemas, rendering contracts, or detailed Flow procedures owned elsewhere.

## Product

PRD-Creator turns uneven project discussion + source material into one approved project model, then produces development-ready project documentation and the production resources needed to build that same project.

The normal human-facing document may contain:

```text
01 Overview
02 Gameplay Flow
03 Development
04 Production Assets
```

01–03 use the approved PRD-core/Golden system. `04 Production Assets` is additive and comes from the **same approved project model**, not from a second AI design pass over finished 01–03.

Voice Production is downstream from accepted project/PRD meaning. It does not create a second project/source-intake authority.

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

There is no canonical Flow 8. Non-Voice Production Assets are a bounded capability inside the same PRD-Creator product package, not another numbered Flow.

High-level flow policy lives in `docs/foundation/`. Detailed production procedure lives in the matching `kits/prd-creator/` domain owner.

## Stable authority shape

```text
current user instruction
+ approved decisions
+ authoritative project source
→ approved project model
   ├─ canonical PRD core 01–03
   └─ justified non-Voice 04 Production Asset requirements when needed
→ accepted PRD / handoff
→ optional Voice requirements
→ canonical Voice Production
→ derived project HTML / evidence
```

Authority decreases downstream. Generated HTML, render projections, reviews, and other derived artifacts do not repair or outrank their canonical source.

When a downstream step exposes missing or contradictory upstream meaning, return only the affected decision to the correct upstream owner. Do not hide the gap with polished prose, renderer defaults, or invented asset/script detail.

## Product boundaries

### Unified PRD Creator package

`kits/prd-creator/` is the single implementation/procedure package for Flow 2–7 plus bounded `04 Production Assets` completion.

Its internal domains remain distinct:

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

Detailed owners:

```text
intake/SOURCE-INTAKE.md             Flow 2 procedure
document/CONTENT-CONTRACT.md        exact PRD-core 01–03 contract
production-assets/CONTRACT.md       exact non-Voice 04 resource/writing contract
renderer/CONTRACT.md                renderer/compositor contract
document/VALIDATION.md              Flow 4 procedure
voice/EXTRACTION.md                 Flow 5 procedure
voice/SOUNDMAKER.md                 Eleven v3 performance-writing craft
voice/VALIDATION.md                 Flow 7 procedure/evidence
```

Voice presentation may appear as `AUDIO` inside the shared 04 Production Assets surface, but project HTML remains a derived view and does not become Voice semantic authority.

## Golden / reference boundary

The approved Golden PRD artifact is binding for the PRD-core representation contract until the user approves a new design. Golden/reference material does **not** supply another project's gameplay facts, counts, timings, lore, scoring, speakers, or implementation decisions.

Reference projects demonstrate structure/quality only within their recorded contract.

## Operating direction

- recover repository/project context before asking the user to repeat it;
- source is triaged by authority/relevance before deep reading;
- solve supported meaning before asking for decisions;
- surface only unresolved material choices;
- preserve information completeness; speed is not permission to delete material meaning;
- bounded revisions touch only invalidated scope;
- prefer existing owners before creating files, skills, schemas, workflows, compatibility layers, or frameworks;
- use the cheapest proof that can falsify the active claim;
- historical audits/backlog/TODOs are not active work unless current continuation promotes them;
- `No change required` is valid;
- stop when the requested scope is complete and sufficiently proven.

## Repository map

Use this map to orient a new chat without scanning the whole repository:

```text
AGENTS.md
→ top-level repository routing / continuity rules

GITHUB_RULES.md
→ GitHub execution, commit/history, CI/API/safety discipline

CONTEXT.md
→ stable product/repository orientation (this file)

docs/foundation/
→ durable Flow 1–7 production policy

docs/knowledge/
→ continuation, routing, ownership, decisions, evidence, backlog

.agents/skills/
→ reusable semantic judgment

kits/prd-creator/
→ categorized Flow 2–7 + bounded 04 procedure/implementation

workspace/active/
→ current project production packages

workspace/archive/
→ inactive retained project packages

tests/ + tools/ + .github/workflows/
→ repository engineering / repeatable verification
```

Use `docs/knowledge/ownership.md` only when the exact owner is unclear. Use `docs/knowledge/source-authority.md` only when source/state precedence is unclear.

## Project package principle

Project packages grow only when the current production stage needs an artifact. Canonical work stays upstream; derived delivery can be regenerated.

Normal versioned project delivery is:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

`prd.html` is the human-facing project document. `context.md` and `index.json` are AI reading/navigation projections, not a second PRD authority.

`document.version` is project/release metadata, not an edit counter.

## Continuation

For new-chat context recovery and non-trivial Developing, read `docs/knowledge/next-action.md` after this file.

`next-action.md` owns the active continuation boundary; current source/state owns actual implementation truth. If they disagree, reconcile the stale owner before continuing instead of repeating old work or inventing a new task.
