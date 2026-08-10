---
name: project-document-generator
description: Recover incomplete project requirements, create canonical development-oriented PRD content, render it through the approved HTML shell, and validate whether the result is development-ready for team handoff without inventing product decisions.
version: 1.3.0
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

## Flow-first execution

Do **not** read every kit document for every task. First identify the current Flow from project state, then open only the relevant owner.

### Flow 2 — Source Intake & Requirement Recovery

Read:

- `SOURCE-INTAKE.md`;
- current project originals/source inventory/requirement state;
- `RULES.md` only when a kit-wide rule is materially relevant;
- `GLOSSARY.md` only when terminology is unclear.

Stop when the project is truthfully `ready_for_prd`, `needs_upstream_decision`, or blocked according to the Flow 2 contract.

### Flow 3 — Project Document / PRD Generation

Read:

- `CONTENT-CONTRACT.md`;
- current `work/content.md` / requirement state;
- `RENDERING.md` only when projection/rendering is in scope;
- `template/approved-document.html` only when template fidelity matters.

Maintain `work/content.md` as canonical PRD meaning. `work/render-data.json` and `output/final.html` remain derived.

### Flow 4 — PRD Validation & Team Handoff

Read:

- `VALIDATION.md`;
- the exact current canonical/rendered PRD revision;
- upstream content/renderer owners only when a finding points back to them.

Validate mechanically with `validator/validate.py` and semantically from New Reader, Level Designer, Developer, and Project Consistency perspectives.

Set `development_ready` only when Critical=0, Major=0, mechanical checks pass, and all four perspectives pass. Create `output/team-handoff.md` and set `handoff_ready` only for that accepted revision.

## Shared routing helpers

- Read `WORKFLOW.md` only when end-to-end sequencing or Flow ownership is unclear.
- Follow nearest `AGENTS.md` for local routing/edit discipline.
- Use root `.agents/skills/project-document-production/` for repository-wide semantic judgment when selected by the activation matrix.
- Do not use kit procedure as a substitute for root `development-brief` on non-trivial Developing work.

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
