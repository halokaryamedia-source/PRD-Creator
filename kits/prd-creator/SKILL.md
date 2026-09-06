---
name: prd-creator
description: End-to-end Production Execution router for PRD-Creator Flow 2–7: recover project requirements, synthesize the complete project model, preview material decisions for approval, produce semantic PRD content through the approved Golden design grammar, complete 04 Production Assets, produce Voice when required, then validate the consolidated project delivery without inventing upstream facts.
version: 1.16.0
---

# PRD Creator

Use for normal project **Production Execution** and bounded production revisions. Changes to how PRD-Creator itself works route to repository Development.

## Route first

```text
new / materially uncertain project meaning
→ Flow 2

approved bounded project / PRD / 04 / Voice change
→ first changed canonical owner
→ only actually invalidated downstream owners

meaning complete but presentation contract wrong
→ document/DESIGN-CONTRACT.md

contracts correct but implementation wrong
→ package AGENTS.md → exact technical owner
```

Start with the smallest owner that can settle the decision. Expand context only when a real cross-cutting dependency or contradiction requires it.

## Canonical production sequence

```text
source / current instruction / approved change
→ Flow 2 Source Intake + Requirement Recovery
→ integrated cross-role synthesis
→ Simple Chat Preview approval for material AI-chosen decisions
→ Flow 3 canonical PRD semantic content
→ deterministic projection through DESIGN-CONTRACT
→ required non-Voice 04 Production Assets
→ Flow 4 mechanical validation + semantic reconciliation + acceptance
→ Flow 5 Voice Requirements when justified
→ Flow 6 canonical Voice Production
→ Flow 7 Voice Validation + Delivery
→ one current versioned project HTML
```

`04 Production Assets` is a bounded capability, not another numbered Flow. Voice remains optional and starts only from accepted `handoff_ready` meaning.

## Owner routing

| Boundary | Owner |
|---|---|
| Flow 2 source recovery/completion + preview | `intake/SOURCE-INTAKE.md` |
| PRD core semantic completeness | `document/CONTENT-CONTRACT.md` |
| PRD Golden page/component grammar | `document/DESIGN-CONTRACT.md` |
| Flow 4 validation/handoff | `document/VALIDATION.md` |
| non-Voice 04 resource meaning | `production-assets/CONTRACT.md` |
| renderer/compositor/delivery mechanics | `renderer/CONTRACT.md` |
| Flow 5 Voice extraction | `voice/EXTRACTION.md` |
| Flow 6 durable lifecycle/output policy | `docs/foundation/06-elevenlabs-script-production.md` |
| Eleven v3 performance craft | `voice/PERFORMANCE-WRITING.md` |
| Flow 7 Voice validation | `voice/VALIDATION.md` |
| technical/file routing | `AGENTS.md` |

## Cross-Flow invariants

### Authority decreases downstream

```text
current explicit user instruction
→ approved project decisions
→ authoritative project source
→ normalized approved project model
→ canonical PRD / asset / Voice meaning
→ derived render/context/index/evidence
```

Derived output never repairs or outranks its canonical owner.

### Semantic meaning and design grammar are separate

`CONTENT-CONTRACT.md` decides whether project meaning is complete. `DESIGN-CONTRACT.md` decides how accepted meaning is represented in the approved PRD visual grammar.

Do not:

- remove semantic rules to make a page fit;
- invent project meaning to fill a design surface;
- reinterpret an implementation bug as a semantic defect.

### Adaptive semantic cardinality

Golden retains the approved page/component grammar. Child counts inside these existing families follow actual project meaning:

```text
Global Development Flow / Notes
Gameplay Overview compact Flow
Level Design Flow / Notes
Developer Flow / Notes
Gameplay Flow narrative sections
```

A project may naturally need 2, 3, 4, 5, 6, 7, or another justified count. Do not add filler to hit the sample count and do not merge distinct rules merely to reduce to it.

Stable semantic questions—Overview facts, three gameplay context roles, six Gameplay Information rows, requirement-table column meanings, page family/navigation—remain stable.

### Routine synthesis is not a project decision

The model may autonomously choose reversible representation/craft details such as grouping, ordering, decomposition, direct wording, requirement placement and obvious derived relationships.

A choice becomes a material Proposal when different plausible answers would change player experience, project scope, build commitment, runtime behavior, scoring/result, timing, transition/handoff, interruption/reset, or another project fact.

### One approved project model

PRD core and non-Voice 04 are projections of the same approved model. Generated 01–03 is not a second brainstorming source for 04.

### Voice stays downstream

Voice may interpret accepted communication/performance needs but may not create upstream gameplay, story, reward, trigger, speaker/channel, or project facts.

### Missing meaning returns upstream

When downstream work exposes missing/contradictory material meaning, return only the affected slice to the first semantic owner that can resolve it. Do not hide the gap in renderer defaults or polished wording.

### Proof stays truthful

Mechanical checks prove mechanical contracts. Semantic review proves only reviewed meaning. Visual PASS requires browser/render evidence. Generated-audio quality requires actual audio evidence.

## Flow 2 → Flow 3

Flow 2 owns recovery, Completion / Proposal / Blocked judgment, production completeness, integrated cross-role synthesis, and the Simple Chat Preview.

Before preview, reason across Gameplay, Level Design, Developer, Production Assets, lifecycle, quantities and transitions deeply enough to expose material contradictions. This is reasoning, not another persistent artifact.

`ready_for_prd` requires:

- materially relevant authority inspected sufficiently;
- stable source/requirement state;
- no current material blocker;
- every material AI-chosen Proposal represented and approved/corrected;
- `preview_approved: true`.

Routine wording/grouping/ordering does not need separate approval.

## Flow 3 → Flow 4

```text
approved project model
→ work/content.md                    canonical semantic meaning
→ work/render-data.json              derived projection
→ DESIGN-CONTRACT component grammar
→ deterministic PRD-core render
```

Flow 3 must preserve semantic cardinality. If approved meaning has six useful lifecycle stages, project six stages into the existing Flow component; do not compress to four because the reference example had four.

If authoring exposes a missing material decision, return that slice to Flow 2. If meaning is complete but cannot be represented by the approved design grammar, reopen the design owner rather than changing project facts.

When approved meaning requires non-Voice resources, materialize `work/asset-requirements.md` before Flow 4 acceptance.

## Flow 4 acceptance / handoff

```text
one mechanical validation
→ one integrated semantic-readiness review
→ semantic reconciliation of material meaning
→ Material Conservation
→ visual evidence only where the claim requires it
→ development_ready | handoff_ready
```

Semantic reconciliation compares:

```text
approved source / requirements
→ canonical content
→ render projection
→ visible PRD
```

It looks for material loss, contradiction, unsupported invention, ambiguity and cross-role drift—not literal wording equality or sample-count equality.

Use `handoff_ready` only when the accepted revision intentionally crosses the downstream handoff boundary. Flow 5 must not start from `development_ready`.

## Flow 5–7

Flow 5 creates justified player-facing Voice requirements from accepted handoff meaning. Flow 6 owns final Voice wording/performance within that contract. Flow 7 validates current requirement/script/revision parity, Communication Conservation, project-HTML parity when present, and optional audio evidence.

Voice-only changes do not reopen PRD-core acceptance when upstream meaning is unchanged.

## First changed / first wrong owner

```text
project fact / gameplay / story / project-level production choice
→ Flow 2 / Project-PRD authority

canonical PRD meaning wrong/incomplete
→ CONTENT-CONTRACT / work/content.md

meaning correct; visible page/component grammar wrong
→ DESIGN-CONTRACT

non-Voice 04 resource meaning
→ production-assets owner / work/asset-requirements.md

Voice scope / communication intent
→ Flow 5 / work/voice-requirements.md

Voice wording / performance
→ Flow 6 / work/voice-production.md

correct canonical + design contracts; wrong generated presentation
→ renderer/compositor

mechanical parity defect
→ matching validator
```

## Bounded revision fast path

```text
identify first changed canonical owner
→ identify actually invalidated downstream owners
→ edit affected canonical scope
→ preview only when a material Proposal changed
→ regenerate derived output once after canonical state stabilizes
→ smallest relevant mechanical + semantic proof
→ cross handoff/Voice boundaries only when inputs changed
→ stop
```

Expand only when evidence shows a real dependency or the user explicitly asks for broader review.

## Artifact lifecycle

Create only owner-needed artifacts:

```text
Flow 2
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
work/review.md                    # only when materially useful

Flow 3
work/content.md
work/render-data.json

04 when required
work/asset-requirements.md

Flow 4
work/acceptance.md
state/handoff-state.yaml

Voice only when used
work/voice-requirements.md
work/voice-production.md
work/voice-acceptance.md
state/voice-state.yaml

Derived delivery
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

Do not create parallel schemas, registries, dashboards, approval files, alternate PRD exports, or another design system merely to make the workflow look complete.

## Context and proof economy

- Start narrow; expand progressively for real material dependencies.
- Do not load the large Golden HTML unless the template/DOM/runtime/visual claim needs evidence.
- Batch canonical edits before regeneration.
- Use the cheapest check that can falsify the changed claim.
- Do not turn semantic review into word-count, similarity, numeric scorecard, or proof-of-proof machinery.
- Do not ask the user to repeat recoverable approved/current state.

## Default delivery

```text
Final Project Document: <output/v<document.version>/prd.html>

Main adjustments / recovered decisions:
- material items only

Needs attention:
- none OR real blocker/decision
```

Internal YAML, IDs, render data and validator transcripts stay out of normal delivery unless requested or needed to explain a blocker.

## Stop condition

Stop when the requested scope is complete and evidence supports the claim. Do not continue into speculative hardening, unrelated cleanup, extra approval layers, replacement exports, or framework creation merely because more work is possible.
