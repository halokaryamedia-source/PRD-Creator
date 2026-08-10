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

Normal project production is **Production Execution**, not repository Developing. Creating/revising a PRD or producing Voice output uses the matching production owner directly; `development-brief` is reserved for changing PRD-Creator itself.

The core PRD authoring path is intentionally simple:

```text
project source
→ automatic internal bootstrap
→ recover production-relevant requirements
→ grouped decisions only if needed
→ canonical PRD
→ Golden Sample projection/render
→ integrated review
→ final PRD
```

## PRD output contract

The approved Golden Sample is the required document authority for this gameplay-document family. Future projects preserve its hierarchy **and reusable page composition**, not merely its CSS/JS shell.

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

The renderer must reproduce the Golden narrative, tabs, context, production-table, role-sequence, grouped requirement, scoring/completion, notes, Terms Used, footer, and navigation component families with project-specific facts. It must not substitute generic pages that only look superficially similar because they inherit the Golden stylesheet.

## PRD quality principles

The PRD side prioritizes:

- source fidelity before polish;
- production-relevant requirement granularity instead of sentence-by-sentence extraction;
- decision-focused user interaction;
- minimum sufficient detail inside the fixed Golden structure;
- Golden page-composition fidelity, not shell-only similarity;
- plain, concrete technical writing without promotional or formulaic AI filler;
- stable terminology, numbers, scoring, triggers, and other authoritative values;
- no new machinery unless a real project proves a need.

## Main owners

```text
.agents/skills/development-brief/
.agents/skills/project-document-production/
.agents/skills/voice-production/

kits/project-document-generator/
kits/voice-production-kit/
```

`project-document-production` owns Flow 2–4 semantic/product judgment and normal PRD Production Execution. Detailed PRD production procedure lives under `kits/project-document-generator/`.

`voice-production` owns Flow 5–7 semantic/product judgment and normal Voice Production Execution. Voice remains downstream of an accepted PRD.

## Current direction

Do not extend BuildIT parity or add generic framework layers automatically. BuildIT is a reference for discipline, ownership, proof, and anti-slop behavior, not a feature checklist.

Use the current system on real project work only after the current PRD pre-sample audit is complete. When a concrete friction or defect appears, fix the smallest owning contract instead of adding preventive architecture around hypothetical failures.

Current continuation state: `docs/knowledge/next-action.md`.
