---
name: prd-creator
description: End-to-end Production Execution router for PRD-Creator Flow 2–7: recover and complete project requirements, preview for approval, produce the protected PRD core 01–03, complete 04 Production Assets, extract and produce Voice when required, then validate the current consolidated project delivery without inventing upstream project facts.
version: 1.14.1
---

# PRD Creator

Use for normal project **Production Execution** and bounded production revisions. Ordinary project production does not use `development-brief`.

This root skill routes work across the existing domain owners. It does not replace their exact contracts.

## End-to-end sequence

```text
source / approved change
→ Flow 2 UNDERSTAND + COMPLETE
→ SIMPLE CHAT PREVIEW
→ Flow 3 BUILD PRD CORE 01–03
→ Flow 4 REVIEW + HANDOFF
→ materialize required non-Voice 04 Production Assets
→ Flow 5 Voice Requirements when justified
→ Flow 6 canonical Voice Production
→ Flow 7 Voice validation/delivery
→ one current versioned project HTML
```

Production Asset needs are recovered from the same source/discussion and approved project model during Flow 2. They are not discovered later by rereading finished 01–03 and brainstorming extra assets.

Voice is downstream from accepted project/PRD meaning. It is optional by project need and never becomes another source-intake authority.

## Owner routing

| Boundary | Owner |
|---|---|
| Flow 2 source recovery/completion + preview procedure | `intake/SOURCE-INTAKE.md` |
| PRD core 01–03 exact contract | `document/CONTENT-CONTRACT.md` |
| Flow 4 validation/handoff procedure | `document/VALIDATION.md` |
| non-Voice 04 resource contract | `production-assets/CONTRACT.md` |
| renderer/compositor/delivery mechanics | `renderer/CONTRACT.md` |
| Flow 5 Voice extraction | `voice/EXTRACTION.md` |
| Flow 6 lifecycle/output policy | `docs/foundation/06-elevenlabs-script-production.md` |
| Eleven v3 performance-writing craft | `voice/SOUNDMAKER.md` |
| Flow 7 Voice validation/evidence | `voice/VALIDATION.md` |
| technical/file routing | `AGENTS.md` |

Open only the smallest owner required for the active boundary.

## Execution gate — preserve quality without replaying unchanged work

Before opening more owners or replaying a Flow, classify the request:

```text
changes HOW PRD-Creator works
→ exit Production Execution
→ root AGENTS.md routes Developing

new / materially uncertain project meaning
→ enter the smallest affected production Flow

approved bounded project or Voice change
→ Revision Fast Path
```

For a bounded revision, determine the **first changed canonical owner** and the **downstream owners actually invalidated by that change** before reading or writing broadly.

Default behavior:

- read only the affected canonical state plus direct dependencies needed to preserve correctness;
- do not re-inventory unchanged source, replay the complete Simple Chat Preview, reread the Golden artifact, reopen all Voice work, or run broad visual QA merely because a project file changed;
- batch affected canonical edits before derived output is regenerated;
- rerender at most once per stable logical revision when derived presentation is invalidated;
- use the existing validation owner for one mechanical check plus one integrated review of the invalidated scope; broader proof is triggered only by the conditions defined there;
- run handoff validation only when the revision actually crosses a handoff boundary;
- reopen Voice only when changed accepted meaning invalidates Voice scope or content, such as Speaker, Channel, Trigger, Purpose, required communication, source timing, or another Voice-owned input;
- update continuity/status owners only when the active boundary, blocker, deferred boundary, milestone, or next meaningful step actually changes.

Scope reduction must never hide a real dependency. Expand beyond the bounded path only when current evidence proves one of these conditions:

- a shared/global rule affected by the change reaches additional objectives/packages;
- targeted inspection reveals a material contradiction or stale dependent owner;
- template/CSS/JS/runtime/page composition changed and therefore broader visual proof is required;
- accepted project meaning changed in a way that invalidates downstream Voice;
- the user explicitly requests a broader audit/review.

If none of those triggers exists, do not replay unchanged workflow stages for ceremony.

## Protected baseline — PRD core 01–03

The approved 01 Overview, 02 Gameplay Flow, and 03 Development hierarchy, Golden contract, authoring behavior, and renderer behavior are protected.

Downstream work must not:

- redesign or renumber 01–03;
- move Development logic into Production Assets;
- change Golden template bytes merely to make 04/Voice easier;
- simplify or rewrite accepted 01–03 as part of ordinary 04 or Voice work;
- treat downstream work as permission for adjacent cleanup.

Exact PRD-core rules belong to `document/CONTENT-CONTRACT.md`.

# Flow 2 — Understand + Complete

Owner: `intake/SOURCE-INTAKE.md`.

Goal: produce a **complete reviewable project model**, not merely a list of gaps.

```text
inventory + authority/relevance inspection
→ recover facts/rules/exclusions/topology/terminology
→ recover Gameplay / Level Design / Developer implications
→ recover concrete Production Asset implications
→ lifecycle + quantitative + global/local coherence
→ Golden fill-map completeness where applicable
→ Existing authority / Completion / one concrete Proposal / Blocked
→ propagate affected meaning
→ complete Simple Chat Preview
→ user correction / approval
→ ready_for_prd
```

Core rules:

- persist material user instructions even when they arrive only in chat;
- record enough source/provenance/inspection state for continuation;
- treat exclusions/removals as first-class requirements;
- resolve partial source changes at requirement/claim level when possible;
- recover ordered objectives/packages, transitions, shared/global rules, and final result when material;
- recover necessary Gameplay, Level Design, Developer, timing, scoring, fail/recovery, interruption/reset, and handoff meaning;
- recover real Production Asset needs from the same approved model; do not wait for generated PRD pages;
- distinguish obvious production implications from material design choices;
- use Completion when evidence implies one answer;
- use one concrete Proposal when AI must choose among plausible material answers;
- keep proposals pending until represented to and approved/corrected by the user;
- use Blocked only when no responsible answer/proposal can be formed without a genuinely external fact or known constraint violation;
- do not copy project facts from Golden/reference examples;
- do not turn PRD/template/process instructions into project facts;
- stop Flow 2 once the model is production-complete and the relevant preview is approved.

## Simple Chat Preview

The preview is a chat checkpoint, not another project artifact.

Default shape:

```text
Project Overview

Objective N — <Name>
Tujuan
<direct objective>

Apa yang Player Lakukan
- chronological player actions / visible response

Hasil
<completion/result/transition>

Level Design
- material build-owned meaning

Developer
- material runtime/data/reset meaning

Saran AI
- each material AI-chosen default once; omit only when none exist
```

Use one short Global Rules block when a project-wide rule would otherwise repeat under every objective.

Do not dump internal IDs/YAML/provenance or a long asset inventory into the preview. Surface only material AI-chosen decisions that require user approval.

For a bounded revision, preview only the invalidated objective/global slice when interpretation changed. An unambiguous current user instruction may itself approve that bounded slice.

# Flow 3 — Build PRD Core 01–03

Primary owner: `document/CONTENT-CONTRACT.md`.

Entry condition: Flow 2 meaning is production-ready and the relevant Simple Chat Preview has been approved.

```text
approved project model
→ one bounded Content Purity + Humanize pass
→ work/content.md
→ direct work/render-data.json projection
→ deterministic renderer
→ output/v<document.version>/prd.html → 01–03
```

Rules:

- `work/content.md` owns canonical PRD-core meaning;
- `render-data.json` is a derived projection, not a second semantic owner;
- project meaning is projected, not independently re-summarized by another AI pass;
- generated HTML is never hand-authored as source truth;
- use the content contract/Golden fill map instead of loading the large Golden HTML during ordinary authoring;
- do not place Production Asset briefs or Voice production data inside PRD-core render data;
- if authoring exposes a missing material decision, return only that gap to Flow 2 and preview/approve it rather than inventing inside rendering.

## Content Purity + Humanize

Run once on the approved meaning before the planned PRD render. Humanize by relocating/decomposing rather than deleting material meaning.

Ensure:

- visible content explains the project, not PRD-Creator/template mechanics;
- Gameplay stays player-facing;
- Level Design owns spatial/build meaning;
- Developer owns runtime/data/scoring/interruption/reset meaning;
- labels are semantic rather than generated filler;
- independently actionable requirements are readable as distinct items;
- terminology remains consistent.

# Flow 4 — Review + Handoff

Owner: `document/VALIDATION.md`.

```text
current canonical PRD + current 04 source when present + current derived HTML
→ one mechanical validation
→ one integrated semantic-readiness review
→ Material Conservation
→ targeted visual sanity when the claim requires it
→ fix first wrong owner
→ development_ready / handoff_ready
```

Mechanical PASS does not prove semantic completeness or visual quality.

For ordinary content-only changes, review only the invalidated scope and representative/high-risk rendered pages. Broader visual proof is required only when template/CSS/runtime/page-composition changed, a finding suggests a global defect, or the user explicitly asks.

Before Flow 5, the handoff validator must confirm that the accepted current PRD revision and versioned delivery agree.

# 04 Production Assets — bounded extension, no new Flow

Owner: `production-assets/CONTRACT.md`.

Use the same approved project model that produced 01–03:

```text
approved project model
→ real required non-Voice resources
→ work/asset-requirements.md
→ optional canonical Voice Production
→ objective/moment-first compositor
→ same output/v<document.version>/prd.html → 04 Production Assets
```

Do not use:

```text
finished 01–03
→ reread generated PRD
→ brainstorm extra assets
→ invent 04
```

Rules:

- include only concrete resources that must actually be created/prepared;
- keep gameplay/runtime behavior with Gameplay/Level Design/Developer owners instead of disguising it as assets;
- use short, literal production language;
- do not invent style/lore/animation/VFX/size/state/sound merely to make a brief look complete;
- include Size only when a real approved numeric/block size exists;
- UI / TEXT carries exact player-facing copy when known;
- non-dialogue AUDIO uses the non-Voice resource contract;
- Voice is merged only from canonical Voice owners;
- ordinary 04 work must not modify accepted 01–03;
- do not create filler resources, empty groups, or another dashboard schema.

If 04 authoring exposes an unapproved material project decision, return only that decision to the existing Flow 2 proposal/approval boundary.

# Flow 5 — Voice Requirement Extraction

Owner: `voice/EXTRACTION.md`.

Entry condition: current PRD handoff is accepted for the same revision.

```text
accepted project / PRD meaning
→ justified player-facing Voice moments
→ work/voice-requirements.md
→ voice_requirements_ready | no_voice_required | needs_upstream_decision | blocked
```

Flow 5 owns **what must be communicated**, by whom, through which approved channel/trigger context, for what listener-facing purpose, and any authoritative timing truth.

Rules:

- create Voice only when accepted project meaning justifies it;
- do not create Voice simply because a reference project used it;
- preserve Speaker, Channel, Trigger, Purpose, Must communicate, Must not add/repeat, and real timing constraints;
- a gameplay section may require zero Voice moments;
- missing project/gameplay facts return upstream rather than being invented;
- do not move performance-writing decisions into Flow 5;
- set `voice_requirements_ready` only when Flow 6 can author without project-level guessing.

# Flow 6 — Canonical Voice Production

Owners: `docs/foundation/06-elevenlabs-script-production.md` + `voice/SOUNDMAKER.md`.

```text
voice_requirements_ready
→ Voice Intent Completeness
→ Eleven v3 performance writing
→ Communication Conservation
→ integrated Voice Script Readiness
→ work/voice-production.md
→ same project HTML 04 AUDIO presentation
```

Each canonical Voice entry preserves current Voice ID/Type/Speaker parity and owns final production wording/performance, Estimated Duration, and actor selection when known.

Do not duplicate Flow 5 context/reasoning/source refs into every production entry unless a current owner explicitly requires them.

## Preparation Mode

Default when actual audio generation is not requested. Full current Voice scope may be prepared and mechanically/semantically validated without claiming audio evidence. A Target Voice Profile may be sufficient before final actor selection when current Flow 6 policy allows it.

## Generation Mode

Use only when actual ElevenLabs output is requested:

```text
one active Voice ID
→ intended actor voice selected
→ exact canonical prompt
→ generate / listen / feedback / approve
→ canonical sync
→ rerender project HTML when canonical actor/prompt changed
```

Generated-audio quality may be claimed only from actual heard evidence.

# Flow 7 — Voice Validation + Delivery

Owner: `voice/VALIDATION.md`.

```text
voice_script_ready
→ mechanical revision / ID / Type / Speaker / project-HTML parity
→ Communication Conservation
→ integrated Voice Script Readiness
→ project HTML visual QA when claimed
→ optional audio evidence
→ voice_delivery_ready | needs_revision | blocked
```

Proof boundaries:

- mechanical parity does not prove communication quality;
- static HTML does not prove visual PASS;
- script appearance does not prove audio quality;
- visual PASS requires actual rendered/browser evidence;
- audio quality requires actual audio evidence.

Voice-only changes do not reopen PRD-core acceptance when upstream PRD meaning is unchanged.

# First wrong owner

```text
project fact / gameplay / story truth
→ upstream project/PRD owner

non-Voice Production Asset requirement meaning
→ production-assets/CONTRACT.md / project model

Voice scope / Speaker / Channel / Trigger / Purpose / required communication / source timing
→ Flow 5

Voice wording / performance / Estimated Duration / actor selection
→ Flow 6

correct canonical content + wrong PRD/04 HTML
→ renderer/compositor owner

Voice mechanical parity defect
→ validator/validate_voice.py

audio-only defect
→ Generation Mode / audio evidence scope
```

# Revision fast paths

Use these only after the Execution Gate identifies a bounded revision. Expand scope only when an expansion trigger above is proven.

## PRD / project revision

```text
approved bounded change
→ identify first changed canonical owner
→ determine actually invalidated downstream owners
→ inspect/update affected requirement/topology/implications only
→ affected preview only when interpretation changed
→ affected canonical PRD/04 source
→ one planned rerender when derived presentation changed
→ one mechanical check + one integrated targeted review
→ reopen Voice only when accepted Voice-owned inputs changed
→ handoff validation only when crossing the handoff boundary
→ stop
```

Do not re-inventory unchanged source, replay unrelated objectives, reread the Golden artifact, or regenerate unaffected downstream work.

## Voice-only revision

```text
changed Voice requirement or production decision
→ first wrong Voice owner
→ affected Voice/Speaker scope only
→ Communication Conservation
→ integrated readiness
→ one rerender only if canonical project presentation changed
→ recheck affected 04 AUDIO presentation
→ stop
```

Do not reopen PRD acceptance for Voice-only production changes when PRD meaning is unchanged.

# Artifact lifecycle

Create artifacts only when their owner needs them:

```text
Flow 2
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml

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

The Simple Chat Preview is not another persistent artifact.

# Default delivery

Normal user-facing production delivery is concise:

```text
Final Project Document: <output/v<document.version>/prd.html>

Main adjustments / recovered decisions:
- material items only

Needs attention:
- none OR real blocker/decision
```

Do not dump YAML, internal IDs, render data, validator transcripts, or CI logs unless requested or needed to explain a blocker.

# Stop condition

Stop when the requested production scope is complete and truthfully supported:

- source + approved decisions support the current project model;
- required preview approval exists for material AI-chosen project decisions;
- PRD core 01–03 satisfies its protected contract;
- real required 04 resources are represented without filler or unsupported invention;
- Voice scope/production is complete only when Voice is actually required;
- relevant mechanical and semantic gates pass;
- evidence claims stay within actual browser/audio proof;
- unresolved material decisions are absent for the requested scope;
- the user receives the current consolidated project document.

Do not continue with speculative hardening, extra artifacts, replacement exports, framework creation, or unrelated cleanup after the requested scope is complete.