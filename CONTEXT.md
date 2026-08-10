# PRD-Creator Context

Status: active production repository
Working branch: `Local`

## Product

PRD-Creator converts uneven project material into development-ready PRD documentation and, when needed, downstream Voice Production assets.

## Production sequence

```text
Flow 1  Repository Boot & Project Memory
Flow 2  Source Intake & Requirement Recovery
Flow 3  Project Document / PRD Generation
Flow 4  PRD Validation & Team Handoff
Flow 5  Voice Requirement Extraction
Flow 6  ElevenLabs Performance Script Production
Flow 7  Voice Validation & Delivery
```

## Current PRD operating direction

Normal project production is **Production Execution**, not repository Developing.

```text
new/revised PRD project
→ project-document-production / Project Document Generator directly
→ no development-brief
```

`development-brief` is reserved for changing or extending PRD-Creator itself.

The PRD user experience should minimize user effort:

- auto-bootstrap project/workspace/internal IDs;
- inspect all source before asking questions;
- apply safe Clarification/Completion automatically;
- batch remaining material decisions with a recommended option/reason/impact when responsible;
- allow one approve-all response with named exceptions;
- use delta-first revision handling for bounded approved changes;
- keep internal state/evidence internal during normal delivery;
- deliver the final PRD plus only concise material changes/attention items;
- perform one visual sanity pass inside Flow 4 when actual visual inspection is available, without creating another gate.

## Golden Sample authority

The approved Golden Sample remains the required template/output foundation for this gameplay PRD family.

Preserve:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Efficiency improvements belong in generation flow and information density, not in removing this structure or replacing the template with a generic minimal shell.

## Anti-overdevelopment

Prefer the smallest complete solution. Do not add new skills, schemas, workflow engines, approval layers, checksums, generic parsers, or template systems without a proved need.

BuildIT remains a reference for discipline/ownership/proof, not a feature checklist.

## Current continuation

Read `docs/knowledge/next-action.md` for the single active task and remaining pre-sample audit boundary.
