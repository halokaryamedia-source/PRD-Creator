# Technical Ownership Refinement Audit — P0.2

Updated: 2026-08-10
Status: completed ownership audit

## Purpose

Determine whether PRD-Creator needs a new repository-wide technical specialist for renderer, validator, DOCX builder, dependency, test, or CI failures after P0.1 introduced executable production verification.

This audit changes ownership/routing only. It does not redesign Flow 2–7 semantics or production artifacts.

## Evidence Reviewed

Current owners:

- `.agents/skills/project-document-production/SKILL.md`;
- `.agents/skills/voice-production/SKILL.md`;
- `docs/knowledge/skills/activation-matrix.md`;
- `kits/project-document-generator/AGENTS.md`;
- `kits/voice-production-kit/AGENTS.md`;
- PRD renderer + validator source;
- Voice DOCX builder + validator source;
- P0.1 `tests/`, `requirements.lock.txt`, `tools/`, and `Production Verify`.

Relevant BuildIT operating pattern:

- choose technical specialists only when a reusable technical contract has distinct procedure/ownership;
- do not select a language/tool skill merely because the implementation uses that technology;
- Maintenance may route to the smallest diagnostic/module owner rather than forcing a semantic specialist.

## Observed Ownership Boundaries

### Project Document semantic boundary

Root semantic owner: `project-document-production`.

It owns decisions about:

- source authority and requirement recovery;
- canonical PRD meaning;
- render projection meaning and approved-template contract;
- development-readiness / handoff semantics.

A renderer change that changes which project facts/pages/role data are represented is still a Project Document semantic/product-contract change.

### Project Document technical boundary

Module-local owners:

- `kits/project-document-generator/renderer/`;
- `kits/project-document-generator/template/`;
- `kits/project-document-generator/validator/validate.py`.

If canonical content/projection semantics are already correct and the defect is purely mechanical—for example parser failure, deterministic marker replacement, file output, HTML ID/navigation implementation, or validator implementation—the smallest owner is the affected module surface under the nearest kit `AGENTS.md`.

A root semantic specialist is optional in Maintenance and should not be loaded merely because the failing file is part of Flow 3/4.

### Voice semantic boundary

Root semantic owner: `voice-production`.

It owns decisions about:

- which Voice moments exist;
- Voice ID/Type/speaker/channel/trigger scope;
- final wording/performance notation;
- delivery-readiness semantics and evidence boundary.

A builder/validator change that changes what Voice content is represented or accepted remains a Voice semantic/product-contract change.

### Voice technical boundary

Module-local owners:

- `kits/voice-production-kit/builder/build_docx.py`;
- `kits/voice-production-kit/validator/validate.py`;
- `kits/voice-production-kit/DOCX-FORMAT.md` for intentional presentation contract.

If canonical requirements/script semantics are correct and the defect is purely builder/validator mechanics—for example DOCX pagination, XML/paragraph formatting, file generation, parser mechanics, or mechanical comparison implementation—the smallest owner is the affected module surface under the nearest kit `AGENTS.md`.

The real blank-page defect is the strongest evidence: the correct repair was builder mechanics (`page_break_before`), not a change to Voice scope or performance semantics.

### Shared repository engineering boundary

Current shared technical concerns are:

- exact dependency pins: `requirements.lock.txt`;
- generic regression contracts: `tests/`;
- static repository contract: `tools/verify_repository.py`;
- executable gate: `.github/workflows/prd-verify.yml`;
- static gate: `.github/workflows/repository-verify.yml`.

These are repository-engineering owners, not another production semantic domain.

P0.1 proved this boundary can serve both kits without creating a cross-kit production specialist.

## Candidate Technical Root Skill Audit

Candidate concept: a root `production-tooling`, `artifact-engineering`, or Python/tooling specialist.

Decision vocabulary result:

`DROP AS ROOT SKILL + MOVE TO MODULE-LOCAL / REPOSITORY ENGINEERING`

Reasons:

1. PRD HTML rendering and Voice DOCX generation do not share one artifact/runtime contract beyond generic Python execution.
2. A Python specialist would be selected because of implementation language, which violates semantic/cause-based routing.
3. Shared dependency/test/CI work already has a smaller repository-level owner in `requirements.lock.txt`, `tests/`, `tools/`, and workflows.
4. Pure technical Maintenance does not require a root specialist; nearest `AGENTS.md` + exact implementation source is sufficient.
5. No repeated cross-kit technical failure currently demonstrates a missing reusable specialist procedure.

## Current Three-Skill Result

`KEEP`, with narrowed ownership wording.

- `development-brief` — unchanged;
- `project-document-production` — semantic/product-contract specialist for Flow 2–4, not automatic owner of every renderer/validator mechanical defect;
- `voice-production` — semantic/product-contract specialist for Flow 5–7, not automatic owner of every DOCX builder/validator mechanical defect.

The three-skill freeze remains valid after P0.2, but the earlier phrase “renderer/validator/builder surfaces are inside the semantic specialist” is superseded where it implied mandatory root-skill ownership for pure mechanics.

## Routing Rule

```text
semantic/product contract wrong
→ matching root semantic specialist

semantic contract already correct
+ renderer/validator/builder mechanics wrong
→ nearest kit AGENTS + exact implementation owner
→ no root specialist required by default

shared dependency/test/CI contract wrong
→ requirements.lock.txt / tests / tools / workflows
→ no production specialist required by default
```

If investigation shows both semantic and mechanical defects, resolve/reframe them as separate boundaries instead of stacking specialists.

## Contributor Contract Finding

Both executable kits need nearest `AGENTS.md` to describe not only Flow routing but also:

- implementation structure;
- exact verification commands;
- canonical-vs-derived edit rules;
- dependency/build assumptions where relevant;
- regression and visual-proof boundaries.

This is justified by P0.1 executable verification and the real DOCX defect. It does not require new nested skill roots.

## Decision

P0.2 ownership audit passes with **no new root skill**.

Strengthen routing and kit-local contributor rules, keep the three root semantic skills, and move the active parity boundary to P1 Production Engineering Quality Audit after repository/production gates pass on the P0.2 change.
