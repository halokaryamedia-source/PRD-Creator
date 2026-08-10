---
name: project-document-production
description: Semantic/product-contract owner for PRD-Creator Flow 2–4. Use for source recovery, canonical PRD meaning, Golden representation requirements, PRD readiness, and handoff semantics. Do not use as a generic HTML/Python wrapper when semantics are already correct.
---

# Project Document Production

Own Flow 2–4 semantic judgment. Detailed production procedure/mechanics stay in `kits/project-document-generator/`.

## Use when

- uneven source must become reliable production requirements;
- canonical `work/content.md` meaning is created/corrected;
- Golden hierarchy/page-composition requirements are defined/corrected;
- PRD development-readiness or handoff meaning is decided.

If semantics are already correct and the defect is renderer/template/validator mechanics, route directly to the nearest kit implementation owner.

## Authority chain

```text
originals + approved decisions
→ requirement state
→ content.md (canonical)
→ render-data.json (derived)
→ final.html (derived)
→ acceptance/handoff evidence
```

Generated output never becomes project authority. Rendering/prose may organize approved meaning but may not invent mechanics, quantities, lore, scoring, triggers, architecture, or unresolved decisions.

## Smallest semantic owner

- Flow 2 → `SOURCE-INTAKE.md`
- Flow 3 content meaning → `CONTENT-CONTRACT.md`
- Flow 3 projection meaning → `RENDERING.md` only when projection/HTML behavior is actually in scope
- Flow 4 readiness → `VALIDATION.md`

`WORKFLOW.md` is sequencing reference only. Read the smallest owner required by the active problem.

## Core judgment

- inspect/triage available source before questioning the user;
- preserve authority/provenance and only production-relevant requirements;
- apply supported Clarification/Completion automatically;
- surface only unresolved material Proposal/Blocked decisions;
- use minimum sufficient detail;
- keep Gameplay / Level Design / Developer meaning distinct;
- preserve Golden document language without copying Golden project facts;
- use `CONTENT-CONTRACT.md` as the single prose-quality/content-density owner;
- return real upstream gaps to Flow 2 rather than hiding them with polished wording or HTML.

## Context economy

Normal production should not load the full Golden template or generated HTML source into model context. Use canonical content for meaning, validator/runtime for full-file mechanics, and actual rendered/browser inspection for visual claims. Inspect HTML source only for a concrete bounded defect. Do not reread unchanged source/packages during bounded revisions.

## Acceptance judgment

Assess the current revision once through these lenses:

- New Reader / Player Context;
- Level Designer;
- Developer;
- Project Consistency.

A single reading slice may satisfy several lenses; do not reread the same package four times. Critical/Major findings block readiness. Writing/density issues matter only when they reduce production usability or alter meaning.

Before reporting ready, confirm:

- material project meaning is supported;
- no unresolved material decision is hidden;
- canonical meaning and derived representation materially agree;
- role-specific content is usable without filler/duplication;
- Golden structure/composition is preserved at the level actually verified;
- visual/runtime claims do not exceed evidence.

## Boundary

This skill owns PRD Flow 2–4 semantic/product contract only. Voice remains downstream. Never patch `final.html` as source of truth.
