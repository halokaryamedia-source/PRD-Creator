# PRD-Creator

PRD-Creator turns incomplete project material into development-ready project documentation and, when needed, downstream Voice Production assets.

## Working branch

`Local` is the permanent development authority. `main` stays stable unless explicitly requested.

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

The core authoring path is intentionally simple:

```text
source
→ recover production-relevant requirements
→ canonical PRD
→ render HTML
→ validate / hand off
→ optional Voice production
```

Normal project production is **Production Execution**: use the existing Flow directly without a `development-brief`. `development-brief` is reserved for changing or extending PRD-Creator itself.

## PRD quality principles

The PRD side prioritizes:

- source fidelity before polish;
- production-relevant requirement granularity instead of sentence-by-sentence extraction;
- automatic internal project/workspace setup rather than making the user manage repository structure;
- decision-focused user review with recommendations and one grouped approval when needed;
- minimum sufficient detail for New Reader, Level Designer, and Developer use;
- plain, concrete technical writing without promotional or formulaic AI filler;
- stable terminology, numbers, scoring, triggers, and other authoritative values;
- delta-first revision handling for bounded approved changes;
- final user delivery focused on the actual PRD rather than internal state/evidence machinery;
- no new machinery unless a real project proves a need.

The approved Golden Sample remains the required template/foundation for this PRD family. Efficiency work improves the generation process; it does not remove the expected Overview → Gameplay Flow → Global Development → Gameplay Overview / Level Design / Developer structure.

## Main owners

```text
.agents/skills/development-brief/
.agents/skills/project-document-production/
.agents/skills/voice-production/

kits/project-document-generator/
kits/voice-production-kit/
```

`project-document-production` owns Flow 2–4 semantic/product judgment and normal PRD Production Execution. Detailed PRD production procedure lives under `kits/project-document-generator/`.

`voice-production` owns Flow 5–7 semantic/product judgment. Voice review remains downstream of an accepted PRD.

## Current direction

Do not extend BuildIT parity or add generic framework layers automatically. BuildIT is a reference for discipline, ownership, proof, and anti-slop behavior, not a feature checklist.

Use the current system on real project work only after the PRD-side workflow/skill readiness audit is complete. When a concrete friction or defect appears, fix the smallest owning contract instead of adding preventive architecture around hypothetical failures.

Current continuation state: `docs/knowledge/next-action.md`.
