---
name: project-document-generator
description: Recover project requirements from discussion and source, complete missing production detail with explicit AI proposals guided by the Golden fill map, preview the complete project model for user approval, produce the existing approved PRD core 01–03 unchanged, complete 04 Production Assets from the same approved project model, and validate the consolidated project document with bounded AI/render/review cost.
version: 1.14.0
---

# Project Document Generator

Use for normal PRD **Production Execution** and bounded PRD revisions. Ordinary PRD creation does not use `development-brief`.

```text
source / approved change
→ UNDERSTAND + COMPLETE
→ SIMPLE PREVIEW
→ BUILD PRD CORE 01–03
→ REVIEW
→ COMPLETE 04 PRODUCTION ASSETS
→ final project document
```

The sequence above describes artifact timing. Production Asset needs are recovered from the same source/discussion and approved project model during understanding; 04 is not discovered later by rereading generated 01–03 and brainstorming extra assets.

The user supplies project source/direction. The agent owns workspace/bootstrap, IDs/state, recovery/problem-solving analysis, practical completion proposals, production-need coverage, projection, commands, validation evidence, and normal repository mechanics.

## Protected baseline — 01–03

The existing approved 01 Overview, 02 Gameplay Flow, and 03 Development style, structure, Golden contract, authoring behavior, and renderer behavior are protected.

Adding 04 must not:

- redesign Overview, Gameplay Flow, or Development;
- rename or move existing 01–03 surfaces;
- change Golden template bytes;
- move Development logic into Production Assets;
- simplify or rewrite 01–03 merely to make 04 easier;
- treat an 04 update as permission for adjacent PRD-core cleanup.

`CONTENT-CONTRACT.md` remains the semantic/visible-composition owner for 01–03.

## 1. UNDERSTAND + COMPLETE — Flow 2

Owner: `SOURCE-INTAKE.md`.

```text
inventory + authority/relevance inspection
→ explicit facts/rules/exclusions
→ topology + terminology
→ cross-role implications
→ production coverage
→ lifecycle + quantitative + operational clarity
→ global/local coherence + known-constraint feasibility
→ Golden fill-map completeness pass
→ fill missing/conflicting material detail with one concrete AI proposal
→ impact propagation
→ complete Simple Chat Preview
→ user correction / approval
→ ready_for_prd
```

Flow 2 must produce a **complete reviewable project model**, not merely report gaps.

The key distinction is:

```text
source-backed meaning = project evidence
AI proposal          = concrete suggested decision for preview
```

AI proposals are allowed to select material gameplay/design/development choices when the source is incomplete or contradictory. They must remain internally marked as proposed/pending until the user approves the preview; do not misrepresent a proposal as a source fact.

Rules:

- persist material user instructions even when they arrive only in chat;
- record source inspection depth enough for resumability;
- treat removals/exclusions as first-class requirements;
- resolve partial source changes at claim/requirement level instead of superseding an entire source unnecessarily;
- recover ordered packages/global ownership/transitions/final result when needed by the project;
- recover necessary Gameplay / Level Design / Developer implications of material mechanics;
- recover concrete Production Asset needs that are explicit or necessarily implied by the same project model; do not wait for finished 01–03 to discover them;
- distinguish a necessary production implication from a material design choice: material choices that change gameplay/lore/player communication require the existing Proposal/approval path; obvious resource implications do not require a new approval framework;
- scan applicable lifecycle stages so missing activation/completion/fail/result/reset behavior is noticed when material;
- check directly related numeric facts (duration/count/capacity/scoring/etc.) for contradictions before drafting;
- reconcile shared/global defaults with explicit local exceptions;
- check material requirements against authoritative known project/platform constraints without importing unrelated generic best practice as authority;
- use the **Reverse-derived Golden fill map** in `CONTENT-CONTRACT.md` as the completeness guide for 01–03: it tells the AI what each required PRD-core slot must answer;
- use `PRODUCTION-ASSETS.md` only for the bounded 04 resource contract; do not mix its presentation rules into Golden PRD-core authoring;
- never copy AFTERSHOCK-specific facts from the Golden into another project; Golden supplies the question/shape, not the answer;
- never copy Clockwork-specific asset forms, names, sizes, lore, or mechanics into another project; Clockwork is a representative quality example, not generic project truth;
- never turn Golden/template/page/validation/process instructions into project facts merely because a visible slot must be filled;
- when source does not answer a Golden-required material question, create one practical project-consistent proposal at the abstraction needed by the PRD;
- when same-authority source surfaces conflict, record the conflict internally and select one recommended preview resolution instead of leaving the objective half-empty;
- use Completion when one answer is implied by evidence; use Proposal when AI is choosing among plausible product/design options;
- if several options are balanced, still choose one reasonable preview default and surface the uncertainty briefly when it materially helps review;
- use `Blocked` only when no responsible proposal can be formed without a genuinely external/user-only fact or when every available choice would violate a known constraint;
- propagate recovered/proposed meaning to all actually affected Gameplay / Level Design / Developer / timing / scoring / handoff / reset surfaces before preview;
- keep optional advisory ideas out of the user's way by default;
- missing optional/irrelevant detail stays open/neutral; material Golden-required meaning must be source-backed, explicitly no/not-applicable, proposed, or blocked;
- present one **complete** Simple Chat Preview before initial `ready_for_prd`;
- keep the preview human-readable and objective-based; do not expose internal IDs/YAML/provenance/recovery jargon or a long asset inventory by default;
- do not enter Flow 3 until the user approves the preview or provides corrections that are incorporated and re-previewed where affected;
- user approval of the complete preview approves the pending AI proposals represented in that preview unless the user explicitly rejects/corrects them;
- stop Flow 2 once production readiness **and preview approval** are reached instead of continuing speculative optimization.

### Simple Chat Preview

The preview is a **chat checkpoint**, not another project artifact or documentation layer. Its job is to answer:

> Is this complete gameplay/project model what the user wants before the full project document is produced?

Default format:

```text
Project Overview
<1–3 short paragraphs or bullets>

Objective N — <Name>
Tujuan
<direct objective>

Apa yang Player Lakukan
- chronological player actions / visible responses

Hasil
<valid completion/result/transition>

Level Design
- material build-owned meaning

Developer
- material runtime/data/reset meaning

Saran AI                     # required when material AI-chosen Proposals exist
- each material AI-chosen default once; omit only when none exist
```

Every objective should read as complete. Do not leave blank sections merely because the source omitted the answer. The underlying detailed model may contain more information than the chat preview; the preview summarizes it for fast review.

The underlying model may already contain concrete Production Asset implications. Do not dump them into the preview unless they contain a material AI-chosen decision that the user needs to approve.

Use `CONTENT-CONTRACT.md` when deciding what detail the PRD-core model needs. For example, the Golden Gameplay Overview requires purpose, timing, start, end, fail/recovery, scoring meaning and five high-level beats; Level Design requires spatial/build meaning; Developer requires mechanic lifecycle, data/result, interruption and reset. The preview may summarize those details under the simpler headings above.

Do not label every recovered sentence as source-derived versus AI-added. Every **material AI-chosen Proposal** must be disclosed once in `Saran AI` before approval; this includes chosen timing, quantity, progression, scoring, fail/recovery, reward, build scope, and runtime behavior. Keep it one compact disclosure list, not a multi-option questionnaire. Omit the block only when the reviewed slice contains no material AI-chosen Proposal.

If a genuinely unresolvable external fact remains, use a short `Perlu Konfirmasi` block only for that item; this is the exception, not the normal completion path.

If there are project-wide rules that materially affect every objective, show one short **Global Rules** block once instead of repeating them under every objective.

After the user approves the preview, promote represented pending proposals to approved project decisions/requirement state before Flow 3. If the user corrects something, persist the correction as authoritative, rerun only affected checks, and re-preview only the invalidated objective/global slice unless the change is broad.

For a bounded revision, do not replay the whole preview. Show only the affected objective/global slice when interpretation changed. If the user's instruction already states the complete intended bounded result unambiguously, that instruction may serve as approval for that slice.

### User-facing proposal communication

When a proposal deserves explicit attention, keep it compact:

```text
Saran AI
<chosen default>

Kenapa
<short project-based reason>

Alternatif
<only when materially useful>
```

Do not force a multi-option decision dialog when one reasonable preview default can be proposed and reviewed in context.

Humanize changes presentation only. Preserve official source names, known numbers, known timings, formulas, mechanics, triggers, uncertainty, provenance, and approval state internally. Do not expose internal IDs/YAML/recovery jargon by default.

## 2. BUILD PRD CORE 01–03 — Flow 3

Primary owner: `CONTENT-CONTRACT.md`.

Entry condition: Flow 2 meaning is production-ready **and the complete Simple Chat Preview has been approved**.

```text
approved project model
→ one Content Purity + Humanize pass
→ work/content.md
→ direct compact work/render-data.json projection from the same approved model
→ deterministic renderer
→ Golden Sample
→ output/v<document.version>/prd.html → 01–03
```

Rules:

- canonical PRD-core meaning is written once in `content.md`;
- Golden hierarchy/page composition is fixed; project facts are variable;
- approved preview proposals are project meaning at this boundary; unapproved proposals are not;
- renderer is a black box in normal production—do not hand-author `output/v<document.version>/prd.html`;
- do not load the full Golden template/generated HTML into model context;
- do not perform a second AI summarization when creating `render-data.json`; project the same purified/humanized approved model directly;
- derive the main projection after canonical meaning is stable enough to render;
- bounded revision patches only affected content/projection/cross-references;
- English-only projection uses scalar strings where appropriate;
- package term `roles` metadata is written only when visibility differs from the default;
- read `RENDERING.md` only when projection/HTML mechanics are actually relevant.

If Flow 3 discovers a missing material answer, return that gap to Flow 2, create/update the proposed model, preview the affected slice, and obtain approval rather than inventing inside the renderer/content projection step.

### Content Purity + Humanize gate

Run this **once before the planned PRD-core render**, on the approved project model/canonical copy. This is not another Flow or artifact.

Check:

```text
PROJECT CONTENT ONLY
- visible copy explains the project/game, not PRD-Creator, Golden, templates, page structure or approval workflow;

ROLE OWNERSHIP
- Gameplay summaries stay player-facing;
- Level Design owns spatial/build meaning;
- Developer owns runtime, telemetry, scoring formula, interruption and reset detail;

SUMMARY DISCIPLINE
- Overview facts and 3-card Gameplay summaries answer one question each;
- do not use a summary card as an overflow bucket for implementation detail;

SEMANTIC LABELS
- note/rule/card titles describe the actual meaning;
- avoid "Global Rule 1", "Important Note 2" and similar generated filler labels;

MATERIAL DECOMPOSITION
- when one requirement contains several independently actionable rules, store them as separate list items/rows rather than one long sentence;

TERMINOLOGY
- use one visible term for the same concept unless a technical distinction is intentional.
```

Humanize by **relocating and decomposing**, not deleting:

```text
long technical Result card
→ short player-facing Result
+ complete technical detail in Developer

long requirement paragraph with four actions
→ four readable bullets in the same requirement row
```

Do not remove a material rule merely to shorten copy.

### Execution economy

Optimize **AI reasoning and review scope**, not HTML file-writing. The deterministic renderer may rewrite the complete `output/v<document.version>/prd.html`; that is intentionally cheaper and safer than inventing partial-render/cache machinery.

Use three modes:

```text
A. UNDERSTAND + PREVIEW
   Source → complete project model → Simple Chat Preview
   No preview HTML, no render-data generation, no browser QA.

B. PRODUCTION RENDER
   Approved preview → one purity/humanize pass
   → write canonical PRD-core content + direct render projection from the same model
   → one planned full render → one mechanical validation
   → one integrated semantic review → representative desktop visual sanity
   → project approved non-Voice resource needs into 04 from the same model.

C. BOUNDED REVISION
   Affected meaning only → affected preview only when interpretation changed
   → purity/humanize only the invalidated slice
   → patch affected canonical content/projection or Production Asset source as applicable
   → one planned full rerender
   → one mechanical check → targeted review of invalidated scope.
```

For initial production, do **not** repeatedly generate HTML while the user is still correcting gameplay in chat. Stabilize and approve the model first. Plan one render for the approved revision; rerender again only after a concrete validator/review finding, downstream Production Asset/Voice materialization, or a later approved change.

During normal authoring, use `CONTENT-CONTRACT.md` / the Golden fill map instead of loading the large Golden HTML. Load the exact Golden artifact only for Golden regression, template/renderer investigation, or actual visual comparison where the artifact itself is evidence.

`render-data.json` should contain only the structured project data needed to fill Golden surfaces. Do not copy Production Asset briefs, reasoning, source-analysis notes, rejected alternatives, approval dialogue, confidence scores, document-process instructions, or duplicate prose into render data.

The same approved in-memory model should feed PRD-core canonical content/projection and downstream resource planning. Do not reread generated HTML or ask the model to independently redesign the project a second time just to discover 04.

Do **not** add a preview renderer, per-page renderer, incremental HTML cache, generic rendering framework, or second template solely for speed. Full-file deterministic rerender remains the normal path.

## 3. REVIEW — Flow 4

Owner: `VALIDATION.md`.

```text
mechanical validator
+ content-purity check
+ Golden composition markers
+ one-read multi-lens semantic review
+ actual visual sanity when available
→ fix real findings
→ re-review only invalidated scope
```

Review the relevant document/package slice once and evaluate New Reader, Level Designer, Developer, Content Purity, and Consistency together. Do not load full `output/v<document.version>/prd.html` for semantic review; validator handles full-file mechanics.

For normal content-only production, use representative desktop visual sanity rather than every-page browser inspection. Escalate to a full visual sweep only when template/CSS/runtime/page-composition behavior changed, a finding suggests a global layout defect, or the user explicitly asks for full visual proof.

## 4. COMPLETE 04 PRODUCTION ASSETS — bounded extension, no new Flow

Owner: `PRODUCTION-ASSETS.md`.

04 is a normal capability of the same Project Document Generator, but it does **not** create a new numbered Flow.

Use the same approved project model that produced 01–03:

```text
approved project model
→ real non-Voice production resource needs
→ work/asset-requirements.md
→ optional canonical Voice data from existing Voice owners
→ deterministic compositor
→ same output/v<document.version>/prd.html → 04 Production Assets
```

Do **not** use this anti-pattern:

```text
finished 01–03
→ reread generated PRD
→ brainstorm assets that might be useful
→ invent 04
```

Rules:

- include only concrete resources that must actually be created/prepared;
- keep Gameplay/Level Design/Developer behavior in its existing owner instead of disguising logic as assets;
- use the moment-first, reader-first resource contract in `PRODUCTION-ASSETS.md`;
- use plain human production language; short and literal beats polished but empty prose;
- do not invent style, lore, animation, VFX, sizes, states, or sound simply to make a brief look complete;
- optional Size appears only when a real approved numeric/block size exists;
- UI / TEXT carries exact player-facing copy when known;
- Voice remains owned by Flow 5–7 and is merged only from canonical Voice sources;
- do not modify 01–03 as part of ordinary 04 work;
- do not create filler resources or an empty category/dashboard merely to force Section 04 to look populated.

If authoring 04 exposes a **material project decision** that was never approved, return only that decision to the existing Flow 2 proposal/approval boundary. Do not solve it inside the asset brief.

### 04 Humanize gate

Use three questions:

1. Does this sentence help someone make the resource?
2. Is the detail supported by project authority?
3. Can a new reader understand what to make without decoding internal terminology?

If the answer fails, make the wording clearer or delete it. Do not make it longer for appearance.

## Revision fast path

```text
approved bounded change
→ persist authoritative instruction if needed
→ affected requirement + topology/terminology/exclusion/implication checks
→ Golden fill-map completeness only where 01–03 are invalidated
→ Production Asset completeness only where 04 is invalidated
→ fill any newly missing material detail with a concrete proposal
→ Simple Chat Preview of affected objective/global slice when interpretation changed
→ user approval/correction for that slice
→ purity/humanize affected slice
→ affected canonical source/projection
→ one planned full rerender
→ one mechanical check
→ targeted semantic/visual review
```

Do not re-inventory unchanged source, re-ask resolved decisions, replay the full preview for a bounded change, or replay unrelated packages/reviews.

## Artifact lifecycle

Create artifacts only when their owner needs them:

```text
CORE
Flow 2 → originals + source/requirement/intake state + complete approved project model
Flow 3 → content.md
Flow 4 → acceptance/current handoff evidence

PRODUCTION ASSETS
approved project model → work/asset-requirements.md only when real non-Voice resources exist

CONDITIONAL
review.md / project README only when useful

DERIVED
render-data.json / current versioned prd.html / context.md / index.json

DOWNSTREAM
Voice artifacts only through the existing Voice Flow
```

The Simple Chat Preview is not a new artifact. Persist only material corrections, proposal state, and approvals needed for continuation.

Use sparse state where defaults are defined; persist every non-default conflict, proposal, approval, blocker, supersession, inspection boundary needed for continuation, and positive readiness explicitly.

## Default delivery

```text
Final PRD: <output/v<document.version>/prd.html>

Main adjustments / recovered decisions:
- material items only

Needs attention:
- none OR real blocker/decision
```

Do not dump YAML, IDs, render data, validator output, CI logs, or internal evidence unless requested or required to explain a blocker.

## Stop condition

Stop when source + preview-approved decisions support the complete project model, Flow 2 recovery/completion is truthfully ready, the Simple Chat Preview has been approved, 01–03 remain valid under their existing Golden/content contracts, real required 04 resources are represented without filler or unsupported invention, visible project content is free of generator/document-process leakage, required mechanical/semantic checks pass, unresolved material decisions are absent, and the user receives the current consolidated project document. Do not claim visual fidelity beyond actual inspection or downstream implementation/QA/audio completion.
