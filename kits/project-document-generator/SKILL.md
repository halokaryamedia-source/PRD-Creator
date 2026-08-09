---
name: project-document-generator
description: Recover incomplete project requirements, create canonical development-oriented PRD content, render it through the approved HTML shell, and validate whether the result is development-ready for team handoff without inventing product decisions.
version: 1.2.0
---

# Project Document Generator

## Purpose

Use this skill to:

1. preserve and understand incomplete project sources;
2. recover traceable requirements and expose true unresolved decisions;
3. create practical canonical project documentation for developers, level designers, and production teams;
4. render approved content through the fixed HTML presentation shell;
5. validate the generated PRD from New Reader, Level Designer, Developer, and Project Consistency perspectives;
6. produce a concise team handoff only when the accepted revision is actually development-ready.

The skill owns PRD production through Flow 4. It does not own downstream Voice Requirement extraction or ElevenLabs scripting.

## Required execution order

1. Read `GLOSSARY.md`.
2. Read `RULES.md`.
3. Read `SOURCE-INTAKE.md` when intake/recovery is active.
4. Read `CONTENT-CONTRACT.md`.
5. Read `RENDERING.md`.
6. Read `VALIDATION.md` when Flow 4/handoff is in scope.
7. Follow `WORKFLOW.md`.
8. Inspect `template/approved-document.html` directly when rendering/template fidelity matters.
9. Resolve required high-impact decisions before canonical drafting.
10. Maintain `work/content.md` as canonical PRD meaning.
11. Maintain `work/render-data.json` only as a derived projection.
12. Render with `renderer/render.py`.
13. Validate mechanically with `validator/validate.py` and semantically with the four-perspective audit.
14. Set `development_ready` only when Critical=0, Major=0, mechanical checks pass, and all four perspectives pass.
15. Create `output/team-handoff.md`, set `handoff_ready`, then stop Flow 4.

## Repository-backed project files

Flow 2 state:

- `state/source-inventory.yaml`
- `state/requirement-register.yaml`
- `state/intake-state.yaml`

Flow 3 work/output:

- `work/review.md`
- `work/content.md` — canonical PRD meaning
- `work/render-data.json` — derived renderer projection
- `output/final.html` — rendered PRD artifact

Flow 4 acceptance/handoff:

- `work/acceptance.md` — concise role-based audit and findings
- `state/handoff-state.yaml` — current readiness status for the exact accepted revision
- `output/team-handoff.md` — concise navigation aid for the production team

Do not create release reports, checksums, packaging manifests, Content Freeze layers, or duplicate PRD summaries unless a concrete requirement needs them.

## Completion condition for Flow 4

Stop when:

- Flow 3 artifacts exist for the same current revision;
- mechanical validation passes;
- New Reader, Level Designer, Developer, and Project Consistency perspectives pass;
- Critical findings = 0;
- Major findings = 0;
- remaining Minor findings, if any, are intentionally accepted and non-semantic;
- `work/acceptance.md` records the evidence;
- `state/handoff-state.yaml` = `handoff_ready`;
- `output/team-handoff.md` points the team to the accepted canonical/rendered PRD.

Do not claim client approval, implementation completion, QA completion, or Voice Production readiness from this status.
