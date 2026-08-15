---
name: project-document-production
description: Semantic/product-contract owner for PRD-Creator Flow 2–4 plus the bounded 04 Production Assets completion contract. Use for source recovery, Golden-guided completion proposals, canonical PRD meaning, Golden representation requirements, PRD readiness/handoff semantics, and ensuring the same approved project model can produce actionable 04 Production Assets without changing the approved 01–03 contract. Do not use as a generic HTML/Python wrapper when semantics are already correct.
---

# Project Document Production

Own Flow 2–4 semantic judgment plus the bounded non-Voice Production Assets completion boundary. Detailed procedure and mechanics stay with the nearest kit owner.

## Authority chain

```text
originals + current user instruction + approved decisions
→ recovered requirement state
→ pending AI proposals for missing/conflicting material meaning
→ user-approved Simple Chat Preview
→ approved project model
   ├─ content.md                 canonical PRD-core meaning
   │  → render-data.json        derived PRD-core projection
   │  → current versioned prd.html → 01–03
   └─ asset-requirements.md     canonical non-Voice 04 production requirements when needed
      → current versioned prd.html → 04 Production Assets
→ acceptance / handoff
```

The PRD core and 04 come from the **same approved project model**. 04 is not discovered by rereading generated 01–03 and brainstorming extra assets afterward.

Generated output never becomes project authority. Pending AI proposals are allowed to complete the preview model, but they do not become project authority until the user approves/corrects the preview. Golden/reference material supplies document function, slot responsibilities and presentation quality, not project-specific mechanics, counts, lore, scoring, or implementation facts.

## Single semantic owners

Do not maintain another Golden checklist here. The gameplay PRD blueprint, mandatory surfaces, Scoring / Result rules, mandatory-slot states, role completeness, terminology/glossary semantics, material-detail conservation, Humanize behavior, and Reverse-derived Golden fill map are owned by:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

The bounded non-Voice 04 requirement/writing contract is owned by:

```text
kits/project-document-generator/PRODUCTION-ASSETS.md
```

Do not duplicate either contract here.

## Active owners

- Flow 2 source recovery/completion/preview readiness → `SOURCE-INTAKE.md`
- Flow 3 PRD-core content/quality → `CONTENT-CONTRACT.md`
- non-Voice 04 Production Assets → `PRODUCTION-ASSETS.md`
- projection/template/compositor mechanics → `RENDERING.md`
- Flow 4 acceptance/handoff → `VALIDATION.md`

Use only the smallest owner needed by the current problem.

## Flow 2 judgment

Use `SOURCE-INTAKE.md` to produce a **complete reviewable project model** before Flow 3.

Use the Reverse-derived Golden fill map as a completeness guide: it tells the AI what each project/global/objective/role surface must be able to answer. Golden does not supply the project answer.

The same understanding pass must also preserve concrete production needs that are already explicit or necessarily implied by the project. This does **not** mean adding an asset dashboard to the chat preview. It means the approved model should know what real MODEL / ITEM / UI / TEXT / AUDIO / standalone PARTICLE resources the project requires, so 04 can later be projected without guessing from generated 01–03.

Material production choices that would change gameplay, story, player communication, or another project fact follow the same Proposal/approval boundary as other project meaning. Obvious production implications do not require a second approval framework.

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

The Simple Chat Preview stays objective-based and simple. It summarizes the complete underlying model; it does not need to expose every Golden slot, every Production Asset, or internal proposal record. Every material AI-chosen Proposal must appear once in `Saran AI` before approval, while source-backed recovery and non-material production implications stay unlabeled. Keep the disclosure compact instead of turning it into a question-by-question approval flow.

Approval of the complete preview approves the represented pending proposals unless the user explicitly corrects/rejects them. A material Proposal is represented only when its chosen default is visible once in `Saran AI`; hidden material AI choices cannot be promoted by blanket approval. Persist those approvals before entering Flow 3.

Do not create a second checklist/state framework around this process.

## Flow 3 judgment

Fill the fixed PRD family with **complete preview-approved production meaning without useless repetition**.

A new reader, Level Designer, and Developer should not need original source to rediscover a material rule that belongs in the PRD.

Before polishing prose, run a material-conservation pass. Every independent approved rule from Flow 2 must have an owned location in `content.md`. Preserve independent conditions, values, exceptions, recovery rules, scoring rules, reset behavior, build constraints, and observable results even when several of them belong inside one Golden table cell.

When deriving `render-data.json`, preserve meaningful structure. Multi-rule requirement content stays as separate list items/rows; distinct Gameplay Flow action/response/recovery paragraphs stay distinct where the Golden surface supports them. Do not flatten structured content into one scalar summary merely because it is shorter or easier for the renderer.

Apply the bounded Humanize behavior from `CONTENT-CONTRACT.md` only after meaning is complete. Humanize can shorten wording, but it cannot remove material facts.

Flow 3 must not invent new product decisions. If authoring exposes a missing material answer, return only that affected slice to Flow 2, create/update the proposal, preview it, obtain approval, and continue.

The approved 01–03 style, format, Golden hierarchy, and existing authoring behavior are protected. Adding 04 is not permission to redesign or rewrite them.

## Flow 4 judgment

Use `VALIDATION.md` for one integrated semantic review against the current authoritative evidence, preview-approved decisions, and PRD.

Critical/Major findings block readiness. A production role having to reopen source for an omitted material rule is Major. Treat independent approved rules that were collapsed or deleted during Flow 3 as the same severity.

For a representative regeneration of the project used to establish the Golden Sample, compare the regenerated document against both current project authority and the approved reference. Matching page shells while materially reducing rule/detail density is a Golden/source-fidelity failure, not a successful simplification.

Mechanical validation proves deterministic structure only; browser/visual claims require actual browser/visual evidence.

## 04 Production Assets judgment

Use `PRODUCTION-ASSETS.md` after the project model is approved to materialize the non-Voice Production Assets source and current 04 presentation.

The key rule is:

```text
same approved project model
→ PRD core 01–03
→ Production Assets 04
```

not:

```text
generated 01–03
→ reread finished document
→ brainstorm 04
```

04 contains only concrete resources that must actually be prepared. Keep resource wording short, literal, reader-first, and free of invented style/lore. Gameplay behavior stays in its existing owner and must not be repackaged as fake assets or sequences.

Voice remains downstream in the Voice Production owners. When canonical Voice exists, the shared compositor may present it inside the matching 04 moment; this skill does not take ownership of Speaker/actor/script decisions.

A project with no justified custom Production Assets must not receive filler entries merely to force an empty 04.

## Proof economy

- do not load the full reference/Golden HTML during normal authoring;
- use the compact Reverse-derived Golden fill map for normal completeness work;
- do load the canonical Golden artifact during a Golden-regression audit or representative parity review;
- do not reread generated 01–03 as the normal source-discovery method for 04;
- do not reread unchanged packages during bounded revisions;
- default visual proof is targeted desktop-only unless the task is specifically mobile/responsive;
- do not rerun Voice checks for PRD-only work unless shared code changed;
- do not add word-count, row-count, semantic-similarity, snapshot, or checksum machinery as a substitute for semantic review.

## Boundary

This skill owns PRD Flow 2–4 semantics plus the bounded non-Voice Production Assets completion boundary. Renderer/validator mechanics stay in the kit, Voice stays downstream, 01–03 remain governed by their existing approved contracts, and `output/v<document.version>/prd.html` is never edited as source of truth.
