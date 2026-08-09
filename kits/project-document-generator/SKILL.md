---
name: project-document-generator
description: Review incomplete project sources, recover traceable requirements, create development-oriented canonical PRD content, and render it through the approved HTML template without inventing design decisions.
version: 1.1.0
---

# Project Document Generator

## Purpose

Use this skill to:

1. preserve and understand incomplete project sources;
2. recover supported requirements and expose true unresolved decisions;
3. create practical canonical project documentation for developers, level designers, and production teams;
4. render the approved content through the fixed HTML presentation shell.

The skill is not merely an HTML formatter. It owns requirement recovery and PRD content generation, but it does not own downstream Voice Production.

## Required inputs

- project source documents / approved project state;
- `template/approved-document.html`.

For repository-backed projects, Flow 3 starts only when `state/intake-state.yaml` is `ready_for_prd`.

## Required execution order

1. Read `GLOSSARY.md`.
2. Read `RULES.md`.
3. Read `SOURCE-INTAKE.md` when intake/recovery is active.
4. Read `CONTENT-CONTRACT.md`.
5. Read `RENDERING.md`.
6. Follow `WORKFLOW.md`.
7. Inspect `template/approved-document.html` directly when rendering/template fidelity matters.
8. Create/update `review.md` until all required high-impact decisions are resolved.
9. Create canonical `content.md` from traceable source facts, supported recovery, and approved decisions.
10. Create `render-data.json` only as a derived projection of `content.md`.
11. Render by cloning the Approved Template shell with `renderer/render.py`.
12. Stop at generated PRD output; development-readiness/team-handoff validation belongs to Flow 4.

## Repository-backed project files

Flow 2 state:

- `state/source-inventory.yaml` — provenance and authority for every source;
- `state/requirement-register.yaml` — traceable recovered requirements/gaps;
- `state/intake-state.yaml` — resumable intake status and next step.

Flow 3 work/output:

- `work/review.md` — human-readable requirement/gap review;
- `work/content.md` — canonical human-readable PRD content;
- `work/render-data.json` — derived renderer projection; never independent authority;
- `output/final.html` — rendered presentation artifact.

Do not create release reports, checksums, packaging manifests, or additional approval layers unless a concrete requirement needs them.

## Completion condition for Flow 3

Stop Flow 3 when:

- Flow 2 is `ready_for_prd`;
- canonical content follows `CONTENT-CONTRACT.md`;
- every material statement is traceable to source/recovered requirements/approved decisions;
- required Gameplay / Level Design / Developer package content is present;
- scoring or completion behavior is explicit when relevant;
- `render-data.json` contains no new meaning beyond `content.md`;
- `final.html` is generated through the approved template shell;
- generated navigation targets exist and no required placeholder remains.

Do not claim the document is development-ready or approved for team handoff yet. That status belongs to Flow 4.
