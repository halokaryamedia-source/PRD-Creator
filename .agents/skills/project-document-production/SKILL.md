---
name: project-document-production
description: Reusable semantic/product-contract specialist for PRD-Creator Flow 2–4 plus bounded non-Voice 04 Production Assets completion. Use when source recovery, project-model completion, canonical PRD meaning, 04 requirement meaning, or PRD readiness/handoff semantics are the actual problem. Presentation-only Golden questions route to the PRD design owner.
---

# Project Document Production

Own **semantic judgment**, not detailed production procedure, visual design mechanics, or renderer implementation.

## Semantic authority shape

```text
originals + current user instruction + approved decisions
→ recovered / approved project model
   ├─ canonical PRD semantic meaning
   └─ justified non-Voice 04 Production Asset requirements
→ acceptance / handoff
```

Generated output never becomes project authority. Golden/reference material supplies representation/quality evidence, not another project's facts.

## Use this specialist when

The actual question requires judgment about:

- source/requirement authority and completeness;
- Completion vs Proposal vs Blocked;
- whether a material choice needs user/project approval;
- what belongs in canonical PRD meaning vs non-Voice Production Assets;
- whether project meaning is actionable for Gameplay / Level Design / Developer;
- whether PRD handoff semantics are satisfied;
- whether a supposed presentation problem is actually missing meaning.

Do not load this skill solely because a task mentions HTML, JSON, renderer, validator, or template.

## Canonical detailed owners

```text
Flow 2 source recovery / completion / preview
→ kits/prd-creator/intake/SOURCE-INTAKE.md

PRD semantic completeness + material conservation
→ kits/prd-creator/document/CONTENT-CONTRACT.md

PRD Golden page/component grammar
→ kits/prd-creator/document/DESIGN-CONTRACT.md

non-Voice 04 meaning
→ kits/prd-creator/production-assets/CONTRACT.md

Flow 4 semantic reconciliation / handoff
→ kits/prd-creator/document/VALIDATION.md

renderer mechanics
→ kits/prd-creator/renderer/CONTRACT.md

normal end-to-end execution
→ kits/prd-creator/SKILL.md
```

## Semantic judgment rules

### Source / model completion

Prefer:

```text
current authority
→ safe Completion when one result is implied
→ concrete Proposal when AI must choose among plausible material options
→ Blocked only when no responsible proposal can be formed
```

Material AI-chosen Proposals remain pending until represented and approved/corrected. Routine wording, grouping, ordering and decomposition are not project decisions.

### PRD semantic core

Flow 3 must represent preview-approved meaning without inventing product decisions or deleting independently actionable rules.

Semantic cardinality follows meaning. If the approved lifecycle has six distinct steps, preserve six; do not compress to a sample count. If it has three, do not add filler merely because the reference showed four or five.

Stable semantic questions remain stable where the product needs them, such as Gameplay Context, Main Objective, Result and the six Gameplay Information concerns.

### Design handoff

When semantic meaning is complete but its visible placement/component behavior is wrong:

```text
→ kits/prd-creator/document/DESIGN-CONTRACT.md
```

Do not alter project truth to make the Golden surface easier to fill. Conversely, do not create a new component family merely because a semantic list has more children; existing flow/note/sequence families accept data-driven cardinality.

### Production Assets

Non-Voice 04 requirements come from the same approved project model as the PRD. Do not use generated PRD pages as a second brainstorming source for extra assets.

Voice semantics remain downstream Voice ownership.

### Readiness / handoff

Mechanical PASS does not establish semantic completeness or visual quality. Flow 4 reconciles material meaning across approved evidence → canonical content → projection → visible PRD. A production role needing to reopen source for already-resolved PRD-scope meaning is a readiness defect.

## Semantic vs technical handoff

```text
semantic meaning wrong
→ this specialist + semantic owner

meaning correct; approved visual grammar wrong
→ DESIGN-CONTRACT

semantic + design contracts correct; executable behavior wrong
→ kits/prd-creator/AGENTS.md → exact implementation owner
```

## Proof economy

- start with the smallest current semantic owner/source;
- expand only for a real cross-cutting dependency;
- do not load full Golden/generated HTML for ordinary semantic review;
- do not use sample card counts, word counts, similarity scores, checksums or snapshots as a substitute for semantic judgment;
- stop when the requested semantic boundary is correct and sufficiently proven.

## Boundary

This skill owns PRD/source/04/readiness **semantic judgment** only. Visual/page grammar belongs to `document/DESIGN-CONTRACT.md`; detailed Flow procedure belongs to categorized package owners; executable mechanics belong to implementation owners; Voice remains downstream; generated `prd.html` is never source truth.
