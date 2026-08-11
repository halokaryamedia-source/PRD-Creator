---
name: project-document-production
description: Semantic/product-contract owner for PRD-Creator Flow 2–4. Use for source recovery, canonical PRD meaning, Golden representation requirements, PRD readiness, and handoff semantics. Do not use as a generic HTML/Python wrapper when semantics are already correct.
---

# Project Document Production

Own Flow 2–4 semantic judgment. Detailed procedure and mechanics stay with the nearest kit owner.

## Authority chain

```text
originals + current user instruction + approved decisions
→ requirement state
→ content.md                 canonical meaning
→ render-data.json           derived projection
→ final.html                 derived presentation
→ acceptance / handoff
```

Generated output never becomes project authority. Golden/reference material supplies document function/quality, not project-specific mechanics, counts, lore, scoring, or implementation facts.

## Single semantic owner

Do not maintain another Golden checklist here. The gameplay PRD blueprint, mandatory surfaces, Scoring / Result rules, mandatory-slot states, role completeness, terminology/glossary semantics, and Humanize behavior are owned by:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

## Active owners

- Flow 2 source recovery/readiness → `SOURCE-INTAKE.md`
- Flow 3 content/quality → `CONTENT-CONTRACT.md`
- projection/template mechanics → `RENDERING.md`
- Flow 4 acceptance/handoff → `VALIDATION.md`

Use only the smallest owner needed by the current problem.

## Flow 2 judgment

Use `SOURCE-INTAKE.md` to recover enough supported project meaning that Flow 3 does not have to invent material behavior.

Mandatory concerns resolve only as defined by `CONTENT-CONTRACT.md`:

```text
Defined | Explicit No | Not Applicable | Blocked
```

Before asking the user, use existing authority first, then safe Completion, then a responsible Proposal when evidence supports one. Do not create a second checklist/state framework around this process.

## Flow 3 judgment

Fill the fixed PRD family with **complete material production meaning without useless repetition**.

A new reader, Level Designer, and Developer should not need original source to rediscover a material rule that belongs in the PRD.

Apply the bounded Humanize behavior from `CONTENT-CONTRACT.md` after meaning is complete. If authoring exposes an unresolved material decision, return it to Flow 2 instead of hiding it behind polished prose.

## Flow 4 judgment

Use `VALIDATION.md` for one integrated semantic review against the current authoritative evidence and PRD.

Critical/Major findings block readiness. A production role having to reopen source for an omitted material rule is Major.

Mechanical validation proves deterministic structure only; browser/visual claims require actual browser/visual evidence.

## Proof economy

- do not load the full reference/Golden HTML during normal authoring;
- do not reread unchanged packages during bounded revisions;
- default visual proof is targeted desktop-only unless the task is specifically mobile/responsive;
- do not rerun Voice checks for PRD-only work unless shared code changed;
- do not add word-count, row-count, semantic-similarity, snapshot, or checksum machinery as a substitute for semantic review.

## Boundary

This skill owns PRD Flow 2–4 semantics only. Renderer/validator mechanics stay in the kit, Voice stays downstream, and `final.html` is never edited as source of truth.
