---
name: project-document-production
description: Reusable semantic/product-contract specialist for PRD-Creator Flow 2–4 plus bounded non-Voice 04 Production Assets completion. Use when source recovery, project-model completion, canonical PRD meaning, 04 requirement meaning, Golden representation requirements, or PRD readiness/handoff semantics are the actual problem. Do not use as a generic HTML/Python/renderer/validator wrapper when semantics are already correct.
---

# Project Document Production

Own **semantic judgment**, not detailed production procedure or renderer mechanics.

Detailed normal Production Execution lives in `kits/project-document-generator/SKILL.md`. Exact contracts/procedures remain in their nearest owners.

## Semantic authority shape

```text
originals + current user instruction + approved decisions
→ recovered / approved project model
   ├─ canonical PRD core meaning
   └─ justified non-Voice 04 Production Asset requirements
→ acceptance / handoff
```

Generated output never becomes project authority. Golden/reference material supplies approved representation/quality requirements within its recorded contract, not another project's facts.

## Use this specialist when

The actual question requires reusable judgment about:

- whether source/requirements are complete and authoritative enough for production;
- Completion vs Proposal vs Blocked for missing/conflicting material project meaning;
- whether a material choice must return to user/project approval;
- what belongs in canonical PRD-core meaning vs non-Voice Production Asset meaning;
- whether 01–03 representation/readiness meaning is correct;
- whether 04 requirement/readiness meaning is correct;
- whether downstream work is trying to invent or repair upstream project truth;
- whether PRD handoff semantics are actually satisfied.

Do not load this skill solely because a task mentions HTML, JSON, Python, renderer, validator, template, or a file under the PRD kit.

## Canonical detailed owners

Use only the smallest owner required:

```text
Flow 2 source recovery / completion / preview
→ kits/project-document-generator/SOURCE-INTAKE.md

PRD core 01–03 exact semantic + visible-composition contract
→ kits/project-document-generator/CONTENT-CONTRACT.md

non-Voice 04 exact resource/writing/readiness contract
→ kits/project-document-generator/PRODUCTION-ASSETS.md

renderer / projection / compositor contract
→ kits/project-document-generator/RENDERING.md

Flow 4 validation / handoff procedure
→ kits/project-document-generator/VALIDATION.md

normal end-to-end Production Execution
→ kits/project-document-generator/SKILL.md
```

Do not recreate those contracts here.

## Semantic judgment rules

### Source / project-model completion

Prefer this order:

```text
current authority
→ safe Completion when one answer is implied
→ concrete Proposal when AI must choose among plausible material options
→ Blocked only when no responsible proposal can be formed
```

Material AI-chosen proposals remain pending until represented to and approved/corrected by the user through the existing Flow 2 preview boundary. Do not hide unsupported material choices inside polished PRD/04 wording.

### PRD core

Flow 3 must represent preview-approved project meaning without inventing new product decisions or deleting independently actionable rules for brevity. Exact PRD-core shape/Humanize/Golden contract belongs to `CONTENT-CONTRACT.md`.

If authoring exposes missing material meaning, return only that affected slice to Flow 2.

### Production Assets

Non-Voice 04 requirements come from the **same approved project model** as 01–03. Do not use finished generated 01–03 as a second design pass to brainstorm extra assets.

Only concrete required resources belong in 04. Exact resource types/fields/reader-first writing/readiness are owned by `PRODUCTION-ASSETS.md`; do not duplicate them here.

Voice scope/wording/actor/performance semantics remain downstream Voice ownership.

### Readiness / handoff

Mechanical PASS does not establish semantic completeness or visual quality. Flow 4 semantics follow `VALIDATION.md` and durable Flow 4 policy. A production role needing to reopen source for material meaning that belongs in the accepted document is a readiness defect.

## Semantic vs technical handoff

When semantic owners are correct but executable behavior is wrong:

```text
renderer/template/validator/compositor defect
→ kits/project-document-generator/AGENTS.md
→ exact implementation owner
```

Do not stay in the semantic specialist as a generic debugging wrapper.

When a technical change would alter what the product/artifact is required to represent or accept, reopen the semantic owner first.

## Proof economy

- inspect only the smallest current semantic owner/source needed;
- do not load full Golden/generated HTML during normal semantic work;
- do not reread unchanged project packages during bounded revisions;
- do not rerun Voice checks for PRD-only semantic work unless shared code/contract changed;
- do not add word-count, row-count, similarity, checksum, snapshot, or scoring machinery as a substitute for semantic review;
- stop when the requested semantic boundary is correct and sufficiently proven.

## Boundary

This skill owns PRD/source/04/readiness **semantic judgment** only. Detailed Flow procedure lives in the Project Document Generator kit; executable mechanics stay with nearest kit implementation owners; Voice stays downstream; derived `prd.html` is never edited as source truth.
