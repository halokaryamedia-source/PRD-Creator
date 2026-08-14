---
name: project-document-production
description: Semantic/product-contract owner for PRD-Creator Flow 2–4. Use for source recovery, Golden-guided completion proposals, canonical PRD meaning, Golden representation requirements, PRD readiness, and handoff semantics. Do not use as a generic HTML/Python wrapper when semantics are already correct.
---

# Project Document Production

Own Flow 2–4 semantic judgment. Detailed procedure and mechanics stay with the nearest kit owner.

## Authority chain

```text
originals + current user instruction + approved decisions
→ recovered requirement state
→ pending AI proposals for missing/conflicting material meaning
→ user-approved Simple Chat Preview
→ approved requirement state
→ content.md                 canonical meaning
→ render-data.json           derived projection
→ current versioned prd.html                 derived presentation
→ acceptance / handoff
```

Generated output never becomes project authority. Pending AI proposals are allowed to complete the preview model, but they do not become project authority until the user approves/corrects the preview. Golden/reference material supplies document function, slot responsibilities and presentation quality, not project-specific mechanics, counts, lore, scoring, or implementation facts.

## Single semantic owner

Do not maintain another Golden checklist here. The gameplay PRD blueprint, mandatory surfaces, Scoring / Result rules, mandatory-slot states, role completeness, terminology/glossary semantics, material-detail conservation, Humanize behavior, and Reverse-derived Golden fill map are owned by:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

## Active owners

- Flow 2 source recovery/completion/preview readiness → `SOURCE-INTAKE.md`
- Flow 3 content/quality → `CONTENT-CONTRACT.md`
- projection/template mechanics → `RENDERING.md`
- Flow 4 acceptance/handoff → `VALIDATION.md`

Use only the smallest owner needed by the current problem.

## Flow 2 judgment

Use `SOURCE-INTAKE.md` to produce a **complete reviewable project model** before Flow 3.

Use the Reverse-derived Golden fill map as a completeness guide: it tells the AI what each project/global/objective/role surface must be able to answer. Golden does not supply the project answer.

Mandatory concerns ultimately resolve only as defined by `CONTENT-CONTRACT.md`:

```text
Defined | Explicit No | Not Applicable | Blocked
```

During preview preparation, missing Defined meaning may come from either recovered authority or an explicit pending AI Proposal.

Use this order:

```text
existing authority
→ safe Completion when one answer is implied
→ concrete Proposal when the AI must choose a product/design/development default
→ Blocked only when no responsible proposal can be formed
```

When same-authority source surfaces conflict, do not silently select one as source truth. Record the conflict, choose one coherent recommended preview resolution based on user direction/project intent/constraints, and keep it pending until preview approval.

When several options are genuinely balanced, still choose one reasonable preview default. The user's goal is to review a complete model, not to answer every small design question before seeing the whole project.

AI proposals may include mechanics, timings, quantities, recovery, scoring behavior, names, build expectations, runtime behavior and other material decisions at the abstraction needed by the PRD. Their protection is explicit pending approval, not vagueness.

The Simple Chat Preview stays objective-based and simple. It summarizes the complete underlying model; it does not need to expose every Golden slot or internal proposal record. Surface `Saran AI` only for material choices whose uncertainty/conflict is useful to the user.

Approval of the complete preview approves the represented pending proposals unless the user explicitly corrects/rejects them. Persist those approvals before entering Flow 3.

Do not create a second checklist/state framework around this process.

## Flow 3 judgment

Fill the fixed PRD family with **complete preview-approved production meaning without useless repetition**.

A new reader, Level Designer, and Developer should not need original source to rediscover a material rule that belongs in the PRD.

Before polishing prose, run a material-conservation pass. Every independent approved rule from Flow 2 must have an owned location in `content.md`. Preserve independent conditions, values, exceptions, recovery rules, scoring rules, reset behavior, build constraints, and observable results even when several of them belong inside one Golden table cell.

When deriving `render-data.json`, preserve meaningful structure. Multi-rule requirement content stays as separate list items/rows; distinct Gameplay Flow action/response/recovery paragraphs stay distinct where the Golden surface supports them. Do not flatten structured content into one scalar summary merely because it is shorter or easier for the renderer.

Apply the bounded Humanize behavior from `CONTENT-CONTRACT.md` only after meaning is complete. Humanize can shorten wording, but it cannot remove material facts.

Flow 3 must not invent new product decisions. If authoring exposes a missing material answer, return only that affected slice to Flow 2, create/update the proposal, preview it, obtain approval, and continue.

## Flow 4 judgment

Use `VALIDATION.md` for one integrated semantic review against the current authoritative evidence, preview-approved decisions, and PRD.

Critical/Major findings block readiness. A production role having to reopen source for an omitted material rule is Major. Treat independent approved rules that were collapsed or deleted during Flow 3 as the same severity.

For a representative regeneration of the project used to establish the Golden Sample, compare the regenerated document against both current project authority and the approved reference. Matching page shells while materially reducing rule/detail density is a Golden/source-fidelity failure, not a successful simplification.

Mechanical validation proves deterministic structure only; browser/visual claims require actual browser/visual evidence.

## Proof economy

- do not load the full reference/Golden HTML during normal authoring;
- use the compact Reverse-derived Golden fill map for normal completeness work;
- do load the canonical Golden artifact during a Golden-regression audit or representative parity review;
- do not reread unchanged packages during bounded revisions;
- default visual proof is targeted desktop-only unless the task is specifically mobile/responsive;
- do not rerun Voice checks for PRD-only work unless shared code changed;
- do not add word-count, row-count, semantic-similarity, snapshot, or checksum machinery as a substitute for semantic review.

## Boundary

This skill owns PRD Flow 2–4 semantics only. Renderer/validator mechanics stay in the kit, Voice stays downstream, and `output/v<document.version>/prd.html` is never edited as source of truth.
