---
name: project-document-generator
description: Recover project requirements, create canonical development-oriented PRD content, render it through the approved Golden hierarchy/page composition, and validate development readiness without inventing product decisions.
version: 1.7.0
---

# Project Document Generator

Use for normal PRD **Production Execution** and bounded PRD revisions. Ordinary PRD creation does not use `development-brief`.

```text
source / approved change
→ UNDERSTAND
→ BUILD PRD
→ REVIEW
→ final PRD
```

The user supplies project source/direction and only decisions they must make. The agent owns workspace/bootstrap, IDs/state, recovery analysis, projection, commands, validation evidence, and normal repository mechanics.

## 1. UNDERSTAND — Flow 2

Owner: `SOURCE-INTAKE.md`.

```text
inventory + authority/relevance inspection
→ recover explicit facts/rules/exclusions
→ recover project topology + terminology
→ cross-role implication pass
→ production coverage scan
→ safe Clarification / Completion
→ one grouped material decision batch only if needed
```

Flow 2 must improve incomplete source **without turning ambiguity into invented design**.

Rules:

- persist material user instructions even when they arrive only in chat;
- record source inspection depth enough for resumability;
- treat removals/exclusions as first-class requirements;
- resolve partial source changes at claim/requirement level instead of superseding an entire source unnecessarily;
- recover ordered packages/global ownership/transitions/final result when needed by the project;
- recover necessary Gameplay / Level Design / Developer implications of material mechanics;
- run a concern-based coverage scan before readiness;
- Completion is allowed only when one evidence-backed result exists at the needed abstraction;
- missing optional/irrelevant detail stays open/neutral rather than becoming filler or a user question.

If uncertain evidence could materially change the PRD, inspect it. Exit truthfully as `ready_for_prd`, `needs_decision`, or `blocked`.

## 2. BUILD PRD — Flow 3

Primary owner: `CONTENT-CONTRACT.md`.

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
- renderer is a black box in normal production—do not hand-author `final.html`;
- do not load the full Golden template/generated HTML into model context;
- derive the main projection after canonical content is stable enough to render;
- bounded revision patches only affected content/projection/cross-references;
- English-only projection uses scalar strings where appropriate;
- package term `roles` metadata is written only when visibility differs from the default;
- read `RENDERING.md` only when projection/HTML mechanics are actually relevant.

If Flow 3 is forced to choose missing topology, role implication, exclusion meaning, terminology, or another material product rule, return that gap to Flow 2.

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
→ affected canonical content + required cross-references
→ affected render projection
→ rerender
→ one mechanical check
→ targeted semantic/visual review
```

Do not re-inventory unchanged source, re-ask resolved decisions, or replay unrelated packages/reviews.

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

Use sparse state where defaults are defined; persist every non-default conflict, approval, blocker, supersession, inspection boundary needed for continuation, and positive readiness explicitly.

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

Stop when source/approved decisions support canonical meaning, Flow 2 coverage is truthfully ready, Golden rendering/mechanical contracts pass, the four semantic lenses have no Critical/Major finding, unresolved material decisions are absent, and the user receives the current final PRD. Do not claim visual fidelity beyond actual inspection or downstream implementation/QA/Voice completion.
