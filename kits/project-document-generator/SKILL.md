---
name: project-document-generator
description: Recover project requirements, complete missing production detail with explicit AI proposals guided by the Golden fill map, preview the complete gameplay model in simple chat form for user approval, create canonical development-oriented PRD content, render it through the approved Golden hierarchy/page composition, and validate development readiness.
version: 1.11.0
---

# Project Document Generator

Use for normal PRD **Production Execution** and bounded PRD revisions. Ordinary PRD creation does not use `development-brief`.

```text
source / approved change
→ UNDERSTAND + COMPLETE
→ SIMPLE PREVIEW
→ BUILD PRD
→ REVIEW
→ final PRD
```

The user supplies project source/direction. The agent owns workspace/bootstrap, IDs/state, recovery/problem-solving analysis, practical completion proposals, projection, commands, validation evidence, and normal repository mechanics.

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
- scan applicable lifecycle stages so missing activation/completion/fail/result/reset behavior is noticed when material;
- check directly related numeric facts (duration/count/capacity/scoring/etc.) for contradictions before drafting;
- reconcile shared/global defaults with explicit local exceptions;
- check material requirements against authoritative known project/platform constraints without importing unrelated generic best practice as authority;
- use the **Reverse-derived Golden fill map** in `CONTENT-CONTRACT.md` as the completeness guide: it tells the AI what each required slot must answer;
- never copy AFTERSHOCK-specific facts from the Golden into another project; Golden supplies the question/shape, not the answer;
- when source does not answer a Golden-required material question, create one practical project-consistent proposal at the abstraction needed by the PRD;
- when same-authority source surfaces conflict, record the conflict internally and select one recommended preview resolution instead of leaving the objective half-empty;
- use Completion when one answer is implied by evidence; use Proposal when AI is choosing among plausible product/design options;
- if several options are balanced, still choose one reasonable preview default and surface the uncertainty briefly when it materially helps review;
- use `Blocked` only when no responsible proposal can be formed without a genuinely external/user-only fact or when every available choice would violate a known constraint;
- propagate recovered/proposed meaning to all actually affected Gameplay / Level Design / Developer / timing / scoring / handoff / reset surfaces before preview;
- keep optional advisory ideas out of the user's way by default;
- missing optional/irrelevant detail stays open/neutral; material Golden-required meaning must be source-backed, explicitly no/not-applicable, proposed, or blocked;
- present one **complete** Simple Chat Preview before initial `ready_for_prd`;
- keep the preview human-readable and objective-based; do not expose internal IDs/YAML/provenance/recovery jargon by default;
- do not enter Flow 3 until the user approves the preview or provides corrections that are incorporated and re-previewed where affected;
- user approval of the complete preview approves the pending AI proposals represented in that preview unless the user explicitly rejects/corrects them;
- stop Flow 2 once production readiness **and preview approval** are reached instead of continuing speculative optimization.

### Simple Chat Preview

The preview is a **chat checkpoint**, not another project artifact or documentation layer. Its job is to answer:

> Is this complete gameplay/project model what the user wants before the full Golden PRD is produced?

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

Saran AI                     # optional
- only material choices the AI filled and that are useful to call out
```

Every objective should read as complete. Do not leave blank sections merely because the source omitted the answer. The underlying detailed model may contain more information than the chat preview; the preview summarizes it for fast review.

Use `CONTENT-CONTRACT.md` when deciding what detail the underlying model needs. For example, the Golden Gameplay Overview requires purpose, timing, start, end, fail/recovery, scoring meaning and five high-level beats; Level Design requires spatial/build meaning; Developer requires mechanic lifecycle, data/result, interruption and reset. The preview may summarize those details under the simpler headings above.

Do not label every recovered sentence as source-derived versus AI-added. Surface `Saran AI` only when a material proposal is uncertain/conflict-resolving enough that the user benefits from seeing it. A normal preview can simply present the proposed complete model.

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

## 2. BUILD PRD — Flow 3

Primary owner: `CONTENT-CONTRACT.md`.

Entry condition: Flow 2 meaning is production-ready **and the complete Simple Chat Preview has been approved**.

```text
work/content.md
→ compact work/render-data.json
→ deterministic renderer
→ Golden Sample
→ output/final.html
```

Rules:

- canonical meaning is written once in `content.md`;
- Golden hierarchy/page composition is fixed; project facts are variable;
- approved preview proposals are project meaning at this boundary; unapproved proposals are not;
- renderer is a black box in normal production—do not hand-author `final.html`;
- do not load the full Golden template/generated HTML into model context;
- derive the main projection after canonical content is stable enough to render;
- bounded revision patches only affected content/projection/cross-references;
- English-only projection uses scalar strings where appropriate;
- package term `roles` metadata is written only when visibility differs from the default;
- read `RENDERING.md` only when projection/HTML mechanics are actually relevant.

If Flow 3 discovers a missing material answer, return that gap to Flow 2, create/update the proposed model, preview the affected slice, and obtain approval rather than inventing inside the renderer/content projection step.

## 3. REVIEW — Flow 4

Owner: `VALIDATION.md`.

```text
mechanical validator
+ Golden composition markers
+ one-read multi-lens semantic review
+ actual visual sanity when available
→ fix real findings
→ re-review only invalidated scope
```

Review the relevant document/package slice once and evaluate New Reader, Level Designer, Developer, and Consistency together. Do not load full `final.html` for semantic review; validator handles full-file mechanics.

## Revision fast path

```text
approved bounded change
→ persist authoritative instruction if needed
→ affected requirement + topology/terminology/exclusion/implication checks
→ Golden fill-map completeness only where invalidated
→ fill any newly missing material detail with a concrete proposal
→ Simple Chat Preview of affected objective/global slice when interpretation changed
→ user approval/correction for that slice
→ affected canonical content + required cross-references
→ affected render projection
→ rerender
→ one mechanical check
→ targeted semantic/visual review
```

Do not re-inventory unchanged source, re-ask resolved decisions, replay the full preview for a bounded change, or replay unrelated packages/reviews.

## Artifact lifecycle

Create artifacts only when their Flow needs them:

```text
CORE
Flow 2 → originals + source/requirement/intake state
Flow 3 → content.md
Flow 4 → acceptance/current handoff evidence

CONDITIONAL
review.md / project README only when useful

DERIVED
render-data.json / final.html

DOWNSTREAM
Voice artifacts only after entering Voice Flow
```

The Simple Chat Preview is not a new artifact. Persist only material corrections, proposal state, and approvals needed for continuation.

Use sparse state where defaults are defined; persist every non-default conflict, proposal, approval, blocker, supersession, inspection boundary needed for continuation, and positive readiness explicitly.

## Default delivery

```text
Final PRD: <final.html>

Main adjustments / recovered decisions:
- material items only

Needs attention:
- none OR real blocker/decision
```

Do not dump YAML, IDs, render data, validator output, CI logs, or internal evidence unless requested or required to explain a blocker.

## Stop condition

Stop when source + preview-approved decisions support canonical meaning, Flow 2 recovery/completion is truthfully ready, the Simple Chat Preview has been approved, Golden rendering/mechanical contracts pass, the four semantic lenses have no Critical/Major finding, unresolved material decisions are absent, and the user receives the current final PRD. Do not claim visual fidelity beyond actual inspection or downstream implementation/QA/Voice completion.
