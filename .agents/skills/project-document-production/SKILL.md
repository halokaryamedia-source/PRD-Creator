---
name: project-document-production
description: Semantic/product-contract owner for PRD-Creator Flow 2–4. Use for source recovery, canonical PRD meaning, Golden representation requirements, PRD readiness, and handoff semantics. Do not use as a generic HTML/Python wrapper when semantics are already correct.
---

# Project Document Production

Own Flow 2–4 semantic judgment. Detailed mechanics remain in `kits/project-document-generator/`.

## Single Golden owner

For the gameplay PRD family, **do not maintain a second Golden checklist here**.

The mandatory document blueprint, required surfaces, Scoring / Result rules, mandatory-slot states, role completeness, and Humanize behavior are owned only by:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

Flow 2, Flow 3, Flow 4, renderer policy, and acceptance must point to that contract instead of paraphrasing it into competing versions.

## Authority chain

```text
originals + current user instruction + approved decisions
→ requirement state
→ content.md                 canonical meaning
→ render-data.json           derived projection
→ final.html                 derived presentation
→ acceptance / handoff
```

Generated output never becomes project authority. Golden supplies document function/quality, not project-specific mechanics, counts, lore, scoring, or implementation facts.

## Active owners

- Flow 2 recovery/readiness → `SOURCE-INTAKE.md`
- Golden mandatory content/quality → `CONTENT-CONTRACT.md`
- projection/render mechanics → `RENDERING.md`
- Flow 4 acceptance/handoff → `VALIDATION.md`

Use only the smallest owner needed by the active problem.

## Flow 2 judgment

Flow 2 must recover enough production meaning that Flow 3 can fill every applicable mandatory Golden concern without guessing.

Use this order:

```text
source authority + sufficient inspection
→ explicit facts / exclusions / topology / terminology
→ cross-role implications
→ lifecycle / scoring-result / quantitative / operational clarity
→ global-vs-local coherence
→ Resolution Ladder
→ impact propagation
→ ready_for_prd | decision needed | blocked
```

For mandatory concerns, resolve meaning as defined by `CONTENT-CONTRACT.md`:

```text
Defined | Explicit No | Not Applicable | Blocked
```

Do not create another checklist artifact or schema merely to store these labels. Use normal requirement state and explicit project wording.

Before escalating to the user, use existing authority first, then safe Completion, then a responsible Proposal. Do not manufacture a recommendation when options are genuinely balanced.

## Flow 3 judgment

Flow 3 fills the fixed Golden shell with **minimum complete production detail**.

Do not optimize for the smallest document. Optimize for a document that lets a new reader, Level Designer, and Developer work without reopening original source for material rules.

Apply the bounded Humanize behavior from `CONTENT-CONTRACT.md` after meaning is complete and before projection.

If drafting exposes a material unresolved product/design decision, return it to Flow 2 instead of hiding it with polished prose or renderer-friendly values.

## Flow 4 judgment

Perform one integrated semantic review using the relevant authoritative requirement/source evidence plus the current PRD.

Use these lenses together:

- New Reader / Player Context;
- Level Designer;
- Developer;
- Project Consistency.

The key question is not whether every page contains text. It is whether the mandatory Golden functions are fulfilled with current-project truth and every production role has the material information it needs.

Critical/Major findings block readiness. A production role having to reopen original source for an omitted material rule is Major.

## Context and proof economy

- Do not load full Golden HTML during normal authoring.
- Do not reread unchanged packages during bounded revision.
- Mechanical validator proves deterministic structure only.
- Default browser proof is targeted desktop-only unless the task explicitly requires mobile/responsive behavior.
- Do not rerun Voice checks for PRD-only semantic work unless shared code actually changed.
- Do not add word-count, row-count, semantic-similarity, or checksum machinery as a substitute for semantic review.

## Boundary

This skill owns PRD Flow 2–4 semantics only. Voice remains downstream. Never patch `final.html` as source of truth.
