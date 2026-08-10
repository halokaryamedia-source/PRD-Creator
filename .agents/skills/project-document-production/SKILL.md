---
name: project-document-production
description: Semantic/product-contract specialist for PRD-Creator Flow 2–4. Use for source recovery, canonical PRD meaning, Golden representation requirements, PRD readiness, and handoff semantics. Do not use as a generic HTML/Python wrapper when the semantic contract is already correct.
---

# Project Document Production

Own semantic judgment for Project Document Generator Flow 2–4. Detailed production procedure and executable mechanics stay in `kits/project-document-generator/`.

## Use this skill when

- incomplete/uneven source must become production requirements;
- canonical `work/content.md` meaning is being created or corrected;
- the Golden Sample representation contract is wrong or incomplete;
- PRD development-readiness or handoff meaning is being decided.

Do not keep this skill loaded merely because renderer/template/validator Python or HTML is being debugged. If semantic meaning is already correct, route directly to the nearest kit implementation owner.

## Authority chain

```text
originals + approved decisions
→ requirement state
→ canonical content.md
→ render-data.json (derived)
→ final.html (derived)
→ acceptance/handoff evidence
```

Generated HTML never becomes project authority. Renderer/prose may organize approved meaning but may not invent mechanics, quantities, lore, scoring, triggers, architecture, or unresolved decisions.

## Smallest-owner routing

- Flow 2 meaning → `SOURCE-INTAKE.md`
- Flow 3 canonical meaning → `CONTENT-CONTRACT.md`
- Flow 3 render/projection contract → `RENDERING.md` only when projection/HTML behavior is actually in scope
- Flow 4 readiness → `VALIDATION.md`
- pure renderer mechanics with correct semantics → kit `AGENTS.md` + exact `renderer/*` owner
- pure validator mechanics with correct semantics → kit `AGENTS.md` + `validator/validate.py`

Read only the smallest owner needed. `WORKFLOW.md` is a sequencing reference, not mandatory context for routine production.

## Semantic rules

- inspect available source before asking the user;
- register only production-relevant requirements/constraints/decisions;
- apply supported Clarification/Completion automatically;
- surface only unresolved material Proposal/Blocked decisions;
- use minimum sufficient detail;
- keep Gameplay / Level Design / Developer meaning separate;
- preserve Golden hierarchy/page language without copying Golden project facts;
- use the prose-quality rules owned by `CONTENT-CONTRACT.md`; do not duplicate a second writing guide here;
- return a real upstream gap to Flow 2 rather than hiding it with polished wording or HTML.

## Context economy

Normal PRD production must not spend model context on generated HTML internals unnecessarily.

- Do **not** load `template/approved-document.html` in full for normal production. The renderer may read it at runtime without putting the ~794 KB Golden file into model context.
- Do **not** load `output/final.html` in full for normal semantic review. Use canonical content for meaning, the validator for mechanical HTML checks, and actual rendered/browser inspection for visual claims.
- Inspect template or generated HTML source only when a concrete finding points to a specific marker/component; read/search only that bounded area.
- Do not reread unchanged source/packages during a bounded revision.
- Do not load root skill + kit skill + WORKFLOW + every Flow procedure merely because the task is “make a PRD.” Route by the active Flow.

## Flow 4 judgment

Acceptance asks whether the current revision is usable by:

- New Reader / Player context;
- Level Designer;
- Developer;
- Project Consistency.

Writing quality/density are checked inside those lenses, not through an AI detector or extra quality score. Critical/Major findings block readiness.

## Acceptance gate

Before reporting the PRD ready, confirm only what the current task requires:

- project meaning is supported by authority;
- no material unresolved decision was hidden;
- canonical content and derived representation do not materially disagree;
- role-specific content is usable without unnecessary duplication/filler;
- Golden structure/composition is preserved at the level actually verified;
- visual/runtime claims do not exceed actual evidence.

## Maintenance rule

```text
observe defect
→ identify first wrong owner
→ semantic wrong: fix smallest Flow owner
→ semantics correct / mechanics wrong: exact kit implementation owner
→ regenerate invalidated derived artifact
→ minimum useful proof
```

Never patch `final.html` as source of truth.

## Boundary

This skill owns Flow 2–4 semantic/product contract only. Voice remains downstream and must not be used as authority for missing PRD design.
