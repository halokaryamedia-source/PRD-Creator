# PRD-Creator

PRD-Creator turns uneven project material into development-ready PRD documentation and, when needed, downstream Voice Production assets.

## Working branch

`Local` is the permanent working authority. `main` stays stable unless explicitly requested.

## Production flow

```text
Flow 1  Repository Boot & Project Memory
Flow 2  Source Intake & Requirement Recovery
Flow 3  Project Document / PRD Generation
Flow 4  PRD Validation & Team Handoff
Flow 5  Voice Requirement Extraction
Flow 6  ElevenLabs Performance Script Production
Flow 7  Voice Validation & Delivery
```

Normal project production is **Production Execution**. `development-brief` is reserved for changing PRD-Creator itself.

## PRD path

```text
project source / current instruction
→ automatic internal bootstrap
→ relevance/authority triage
→ requirement recovery + problem solving
→ concrete Completion / Proposal for material gaps
→ complete Simple Chat Preview
→ user correction / approval
→ canonical PRD
→ deterministic exact-Golden projection/render
→ integrated Semantic Readiness + Material Conservation
→ targeted visual sanity
→ final PRD / handoff
```

Flow 2 should solve before asking: recover from authority, apply safe Completion, or form a responsible Proposal before escalating a material decision to the user. A Proposal is not project truth until the relevant preview is approved/corrected.

## Golden PRD contract

The approved Golden Sample is the required **canonical visible page prototype** for this gameplay-document family. It locks hierarchy, page composition, component language, labels, reading pattern, and presentation behavior unless the user explicitly approves a Golden revision.

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Future projects replace project facts; they do not redesign this document language or copy Aftershock-specific mechanics/counts.

`template/golden-reference.html` stores the canonical approved reference bytes. `template/runtime-template.html` is the runtime template alias and must remain byte-identical to the Golden artifact.

## PRD quality and efficiency

- source fidelity before polish;
- source provenance is mandatory while duplicating every source file into Git is not;
- Flow 2 uses the Golden fill map to ensure required production meaning exists without copying reference-project facts;
- complete missing material meaning with a concrete Proposal when authority does not settle it, then obtain user approval through the Simple Chat Preview;
- minimum complete production detail, not minimum-looking output;
- plain human-readable language without changing technical meaning;
- one semantic model feeds both `content.md` and direct `render-data.json` projection;
- deterministic full-file rerender is preferred over partial-render/cache infrastructure;
- Flow 4 persists Mechanical + one integrated Semantic Readiness + Material Conservation + Visual sanity, not duplicated role-by-role PASS fields;
- bounded revisions touch only invalidated semantic/review scope;
- unchanged Golden/reference proof is not replayed for ordinary content-only work;
- no new machinery without a concrete current need.

## Main owners

```text
.agents/skills/development-brief/
.agents/skills/project-document-production/
.agents/skills/voice-production/

kits/project-document-generator/
kits/voice-production-kit/
```

BuildIT remains a discipline/ownership/proof reference, not a feature checklist. Current continuation state lives in `docs/knowledge/next-action.md`.
