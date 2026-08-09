---
name: project-document-generator
description: Review and complete project documentation, obtain approval for design-changing proposals, then reproduce the approved HTML template with project-specific content.
version: 1.0.0
---

# Project Document Generator

## Purpose

Use this skill to:

1. review incomplete project documentation;
2. complete missing information that is supported by the source context;
3. separate design-changing suggestions for user approval;
4. produce final HTML by cloning the approved template.

## Required inputs

- project source documents;
- `template/approved-document.html`.

Optional inputs:

- images;
- additional notes;
- existing assets.

## Required execution order

1. Read `GLOSSARY.md`.
2. Read `RULES.md`.
3. Read `SOURCE-INTAKE.md`.
4. Follow `WORKFLOW.md`.
5. Inspect `template/approved-document.html` directly.
6. Capture and inventory all available project sources before requirement recovery.
7. Produce the review result before canonical PRD drafting or rendering.
8. Ask only for unresolved high-impact Proposal or Blocked decisions that cannot be recovered safely.
9. Produce approved canonical content.
10. Clone the approved template and replace project-specific content only.

## Required outputs

Create only what the task requires. For repository-backed projects, Flow 2 also maintains:

- `state/source-inventory.yaml` — provenance and authority for every source;
- `state/requirement-register.yaml` — traceable recovered requirements and gaps;
- `state/intake-state.yaml` — one resumable intake status and next step.

The normal production outputs remain:

- `review.md` — human-readable gap classification and decisions needed;
- `content.md` — approved canonical content;
- `final.html` — rendered document.

Do not create audit reports, test reports, release notes, or additional process files unless explicitly requested.

## Completion condition

Stop when:

- every available source has been inventoried or explicitly marked unavailable;
- every material requirement is traceable to source evidence or an approved decision;
- every identified gap has been classified;
- all required approvals have been received;
- approved content has been applied;
- the final HTML preserves the approved template;
- the requested files have been delivered.

Do not continue improving the document after these conditions are met unless the user explicitly requests another revision.
