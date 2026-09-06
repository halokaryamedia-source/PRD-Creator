---
name: prd-creator
description: End-to-end Production Execution router for PRD-Creator Flow 2–7: recover and complete project requirements, preview for approval, produce the protected PRD core 01–03, complete 04 Production Assets, extract and produce Voice when required, then validate the current consolidated project delivery without inventing upstream project facts.
version: 1.14.0
---

# PRD Creator

Use for normal project **Production Execution** and bounded production revisions. Ordinary project production does not use `development-brief`.

This file is the cross-Flow router. It intentionally does **not** restate the detailed contracts owned by the categorized files below.

## Route first

Before opening a production owner, classify the request:

```text
changes HOW PRD-Creator works
→ leave Production Execution
→ root AGENTS.md routes Development

new / materially uncertain project meaning
→ enter Flow 2

approved bounded project / PRD / 04 / Voice change
→ enter at the first changed canonical owner
→ follow only actually invalidated downstream owners
```

Open only the smallest owner that can change the decision.

## Canonical production sequence

```text
source / current instruction / approved change
→ Flow 2 Source Intake + Requirement Recovery
→ Simple Chat Preview approval
→ Flow 3 PRD core 01–03
→ required non-Voice 04 Production Assets
→ Flow 4 Review + Acceptance / Handoff
→ Flow 5 Voice Requirements when justified
→ Flow 6 canonical Voice Production
→ Flow 7 Voice Validation + Delivery
→ one current versioned project HTML
```

`04 Production Assets` is a bounded capability, not another numbered Flow. Voice is optional and begins only from accepted `handoff_ready` project/PRD meaning.

## Owner routing

| Boundary | Owner |
|---|---|
| Flow 2 source recovery/completion + preview | `intake/SOURCE-INTAKE.md` |
| PRD core 01–03 semantic + visible contract | `document/CONTENT-CONTRACT.md` |
| non-Voice 04 resource/writing/readiness contract | `production-assets/CONTRACT.md` |
| Flow 4 validation/handoff | `document/VALIDATION.md` |
| renderer/compositor/delivery mechanics | `renderer/CONTRACT.md` |
| Flow 5 Voice extraction | `voice/EXTRACTION.md` |
| Flow 6 durable lifecycle/output policy | `docs/foundation/06-elevenlabs-script-production.md` |
| Eleven v3 performance-writing craft | `voice/PERFORMANCE-WRITING.md` |
| Flow 7 Voice validation/evidence | `voice/VALIDATION.md` |
| technical/file routing | `AGENTS.md` |

Do not load another owner merely because it is adjacent in the production sequence.

## Cross-Flow invariants

### Authority decreases downstream

```text
current explicit user instruction
→ approved project decisions
→ authoritative project source
→ normalized approved project model
   ├─ canonical PRD core
   └─ canonical non-Voice 04 requirements when present
→ accepted Voice requirements
→ canonical Voice Production
→ derived project HTML / context / index / evidence
```

Derived output never repairs or outranks its canonical owner.

### One approved project model

PRD core 01–03 and non-Voice 04 are projections of the **same approved project model**. Do not use finished 01–03 as a second design pass for inventing Production Assets.

### Voice stays downstream

Voice may interpret accepted communication/performance needs but may not create upstream gameplay, story, reward, trigger, speaker/channel, or other project facts.

### Golden stays protected

The approved PRD-core Golden hierarchy/template/visible composition remains protected. Normal 04 or Voice work must not redesign, renumber, or rewrite accepted 01–03.

### Missing meaning returns upstream

When downstream work exposes missing or contradictory material meaning, return only the affected slice to the first semantic owner that can resolve it. Do not hide the gap in polished wording, renderer defaults, generated HTML, or extra metadata.

### Proof stays truthful

Mechanical checks prove only mechanical contracts. Visual PASS requires rendered/browser evidence. Generated-audio quality requires actual heard audio evidence.

## Flow gates

### Flow 2 → Flow 3

Flow 2 owns recovery, Completion / Proposal / Blocked judgment, production completeness, and the Simple Chat Preview.

`ready_for_prd` requires:

- materially relevant authority inspected to sufficient depth;
- stable source/requirement state;
- no current material blocker;
- every material AI-chosen Proposal represented and approved/corrected;
- `preview_approved: true`.

The Simple Chat Preview is chat output, not another persistent artifact.

### Flow 3 → Flow 4

Flow 3 starts only from approved `ready_for_prd` meaning.

```text
approved project model
→ work/content.md
→ work/render-data.json
→ deterministic PRD-core render
```

`work/content.md` owns PRD-core meaning. `render-data.json` and generated HTML are derived. If authoring exposes missing material meaning, return that slice to Flow 2 rather than deciding it inside Flow 3.

When the approved model requires non-Voice production resources, materialize `work/asset-requirements.md` before Flow 4 acceptance.

### Flow 4 acceptance / handoff

Flow 4 owns the minimum acceptance proof:

```text
one mechanical validation
→ one integrated semantic-readiness review
→ Material Conservation
→ visual evidence only where the claim requires it
→ development_ready | handoff_ready
```

Use `handoff_ready` only when the current accepted revision intentionally crosses the downstream handoff boundary. Flow 5 must not start from `development_ready`.

### Flow 5 → Flow 6

Flow 5 creates only justified player-facing Voice requirements from the accepted handoff. It owns Voice scope and communication intent/context, not final performance wording.

Entry requires the current PRD handoff validator to pass for the same revision.

### Flow 6

Flow 6 owns final Voice wording/performance, Estimated Duration, and actor selection when known, within the accepted Flow 5 contract.

Preparation Mode does not claim audio evidence. Generation Mode is used only when actual audio generation/revision is requested.

### Flow 7

Flow 7 validates current Voice requirement/script/revision parity, Communication Conservation, integrated Voice Script Readiness, current project-HTML parity when present, and optional audio evidence.

Voice-only changes do not reopen PRD-core acceptance when upstream PRD meaning is unchanged.

## First changed / first wrong owner

Use the earliest owner that is actually wrong:

```text
project fact / gameplay / story / project-level production choice
→ Flow 2 / Project-PRD authority

canonical PRD-core meaning or Golden placement
→ document/CONTENT-CONTRACT.md / work/content.md

non-Voice 04 resource meaning
→ production-assets/CONTRACT.md / work/asset-requirements.md

Voice scope / Speaker / Channel / Trigger / Purpose / required communication / source timing
→ Flow 5 / work/voice-requirements.md

Voice wording / performance / Estimated Duration / actor selection
→ Flow 6 / work/voice-production.md

correct canonical content + wrong generated presentation
→ renderer/compositor owner

mechanical parity / validation defect
→ matching validator owner

audio-only defect
→ Generation Mode / audio evidence
```

File type or implementation language does not decide ownership.

## Bounded revision fast path

For an approved revision:

```text
identify first changed canonical owner
→ identify downstream owners actually invalidated
→ edit affected canonical scope
→ preview only when interpretation introduced/changed a material Proposal
→ regenerate derived output once after canonical state is stable
→ run the smallest relevant mechanical + semantic proof
→ cross handoff/Voice boundaries only when their inputs changed
→ stop
```

Expand beyond the bounded path only when evidence shows a real dependency, for example:

- a changed shared/global rule affects additional packages;
- targeted inspection finds a material contradiction or stale dependent owner;
- template/CSS/JS/runtime/page composition changed and broader visual proof is needed;
- accepted meaning changed a Voice-owned input;
- the user explicitly requests a broader audit/review.

Do not replay unchanged source intake, full Golden review, unrelated packages, Voice work, or broad QA for ceremony.

## Artifact lifecycle

Create an artifact only when its owner needs it:

```text
Flow 2
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
work/review.md                    # only when materially useful

Flow 3
work/content.md
work/render-data.json

04 when real non-Voice resources exist
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

Do not create parallel schemas, registries, dashboards, approval files, or alternate HTML exports merely to make the workflow look more complete.

## Context and proof economy

- Read the active owner and only dependencies that can change the decision.
- Do not load the large Golden HTML unless the Golden/template/DOM/runtime claim itself needs evidence.
- Batch canonical edits before regeneration.
- Rerender at most once per stable logical revision unless new evidence invalidates it.
- Use the cheapest check that can falsify the changed claim.
- Do not turn semantic review into word-count, similarity, scorecard, or proof-of-proof machinery.
- Do not ask the user to repeat recoverable approved/current project state.

## Default user-facing delivery

Normal production delivery is concise:

```text
Final Project Document: <output/v<document.version>/prd.html>

Main adjustments / recovered decisions:
- material items only

Needs attention:
- none OR real blocker/decision
```

Internal YAML, IDs, render data, validator transcripts, CI logs, and repository mechanics stay out of the normal user-facing result unless requested or needed to explain a real blocker.

## Stop condition

Stop when the requested scope is complete and the evidence supports the claim.

Do not continue into speculative hardening, unrelated cleanup, extra artifacts, extra approval layers, replacement exports, new skills, or framework creation merely because more work is possible.
