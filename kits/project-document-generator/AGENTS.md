# Project Document Generator Agent Rules

Root `AGENTS.md` remains authoritative for work mode, proof, skill budget, and repository continuity. This file narrows behavior only inside `kits/project-document-generator/`.

## Flow Routing

Start from the current project/state and identify the active Flow before opening kit documents.

- **Flow 2 — Source Intake & Requirement Recovery**
  - read `SOURCE-INTAKE.md`;
  - read `RULES.md` only when a kit-wide recovery rule is relevant;
  - read `GLOSSARY.md` only when terminology is unclear.
- **Flow 3 — PRD Generation**
  - read `CONTENT-CONTRACT.md`;
  - read `RENDERING.md` only when projection/rendering is in scope;
  - inspect `template/approved-document.html` only when template fidelity matters.
- **Flow 4 — PRD Validation & Team Handoff**
  - read `VALIDATION.md`;
  - inspect renderer/content only when a finding points back to those owners.

Use `WORKFLOW.md` only when end-to-end sequencing or Flow ownership is unclear. Do not load every kit document by default.

## Canonical Boundary

```text
project originals + approved decisions
→ requirement state
→ work/content.md                 canonical PRD meaning
→ work/render-data.json           derived projection
→ output/final.html               derived presentation
→ work/acceptance.md              revision-specific evidence
→ state/handoff-state.yaml
→ output/team-handoff.md
```

Never patch a derived artifact to hide a defect in an upstream owner.

## Maintenance

For a concrete defect:

1. identify whether the first wrong owner is source/recovery, canonical content, render projection, renderer/template, validator, or acceptance evidence;
2. fix the smallest root owner;
3. regenerate only invalidated derived artifacts;
4. run the minimum useful proof required by root `AGENTS.md`.

Maintenance does not automatically invoke `development-brief`.

## Boundaries

- This kit owns Flow 2–4 only.
- Voice scope/writing/DOCX belongs to `kits/voice-production-kit/`.
- Golden/reference material demonstrates approved structure/quality only; it does not define project facts.
- Do not recreate retired schema/profile/freeze/package architecture without a proved current requirement.
