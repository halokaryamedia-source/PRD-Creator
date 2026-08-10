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
project source
→ automatic internal bootstrap
→ relevance/authority triage
→ requirement recovery + problem solving
→ humanized grouped unresolved decisions only if needed
→ canonical PRD
→ deterministic Golden projection/render
→ integrated review
→ final PRD
```

Flow 2 should solve before asking: recover from authority, apply safe Completion, or form a responsible Proposal/tradeoff before escalating a material decision to the user.

## Golden PRD contract

The approved Golden Sample is the required hierarchy, page-composition, component-language, and presentation authority for this gameplay-document family:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Future projects replace project facts; they do not redesign this document language or copy Aftershock-specific facts/counts.

## PRD quality and efficiency

- source fidelity before polish;
- production-relevant requirement granularity instead of sentence-by-sentence extraction;
- relevance-first source reading rather than loading every byte;
- Flow 2 resolves topology, lifecycle, numeric/clarity/coherence issues, known constraint conflicts, and cross-role implications before drafting when material;
- recommendations are honest about evidence and tradeoffs rather than forcing a false default;
- minimum sufficient detail inside the Golden structure;
- plain, human-readable production language without changing technical meaning;
- canonical meaning first, compact derived projection second;
- deterministic renderer/validator consume large HTML at runtime;
- bounded revisions/reviews touch only affected scope;
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
