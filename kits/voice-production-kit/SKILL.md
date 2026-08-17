---
name: voice-production-kit
description: Extract Voice requirements from accepted PRDs, prepare canonical Eleven v3 production content, conserve required communication, and publish developer-ready Voice Production into matching 04 AUDIO resources without inventing upstream project facts.
version: 1.11.2
---

# Voice Production Kit

Use for normal Voice **Production Execution** after accepted project/PRD meaning is available.

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted project/PRD meaning → `work/voice-requirements.md`.
2. **Flow 6 — Voice Production**: Voice Requirements → canonical `work/voice-production.md` → matching `AUDIO` resources in the same project HTML.
3. **Flow 7 — Voice Validation & Delivery**: current Voice revision → compact acceptance + delivery state.

Generated audio remains an optional downstream scope.

## Active owners

- Flow 5 durable policy → `docs/foundation/05-voice-requirement-extraction.md`.
- Flow 5 detailed extraction procedure → `VOICE-EXTRACTION.md`.
- Flow 6 durable lifecycle/output policy → `docs/foundation/06-elevenlabs-script-production.md`.
- Flow 6 Eleven v3 performance-writing craft → `SOUNDMAKER.md`.
- Flow 7 durable policy → `docs/foundation/07-voice-validation-delivery.md`.
- Flow 7 detailed validation/evidence → `VOICE-VALIDATION.md`.
- kit file/mechanical routing → `AGENTS.md`.

`README.md` is package orientation/navigation only. The former duplicate `SCRIPT-PRODUCTION.md` lifecycle owner remains retired.

Do not load all reference material by default.

## Authority chain

```text
accepted project / PRD meaning
→ work/voice-requirements.md
→ work/voice-production.md
→ derived project HTML 04 AUDIO presentation
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

- PRD/project authority owns gameplay/story truth and the need for a Voice asset.
- Flow 5 owns which Voice assets exist plus communication intent/context and authoritative timing truth.
- Flow 6 owns canonical production wording/performance, Estimated Duration, and actor selection when known.
- Flow 7 owns Voice readiness/evidence.
- project HTML is derived presentation only.

## Flow 5 → Flow 6 interface

A Flow 5 entry is ready only when downstream production can recover communication job, listener state, required information, intended outcome, Speaker, approved channel/trigger context, optional source timing truth, and scope guardrails without project-level guessing.

Do not move downstream performance-writing fields into Flow 5. Do not invent project facts to make downstream presentation look complete.

## Canonical Voice Production

Each canonical entry requires the fields/current structure owned by Flow 6 policy and `SOUNDMAKER.md`, including stable Voice ID/Type/Speaker parity, Estimated Duration, and canonical Eleven v3 performance payload.

Do not duplicate Flow 5 Trigger/Purpose/requirements/source refs/reasoning/QA into every canonical production entry unless a current owner explicitly requires them.

Recurring actor selection may be stored once per Speaker in the canonical Voice Cast area when known. Do not invent a commercial voice merely to make Preparation Mode look complete.

## Project HTML production surface

Canonical Voice is merged into the same project `04 Production Assets` surface in the matching natural gameplay moment.

The **exact reader-facing 04 resource fields, moment organization, and dialogue AUDIO presentation contract** are owned by:

```text
kits/project-document-generator/PRODUCTION-ASSETS.md
```

Shared composition mechanics are owned by the Project Document Generator renderer. Voice does not create a separate sidebar category, `Audio → Voice Production` dashboard, or second HTML schema.

This presentation boundary must not change canonical Voice wording, Speaker/Type/Trigger authority, or performance payloads.

## Preparation vs Generation Mode

### Preparation Mode

Default when actual audio generation is not requested. Full current Voice scope may be prepared and validated without claiming audio evidence. A Target Voice Profile may be sufficient before final actor selection when current Flow 6 policy allows it.

### Generation Mode

Used only for actual ElevenLabs output. Work one active Voice ID at a time with the intended actor voice selected, exact canonical prompt, real generation/feedback, and canonical synchronization after approved changes.

Generated-audio quality can be claimed only from actual heard evidence.

## First wrong owner / bounded revision

```text
project fact
→ PRD/project authority

Voice scope / Speaker / Channel / Trigger / Purpose / required communication / source timing
→ Flow 5

canonical wording / performance / Estimated Duration / actor selection
→ Flow 6

correct canonical Voice + wrong shared 04 presentation
→ Project Document Generator compositor / Production Assets owner

audio-only defect
→ Generation Mode / audio evidence scope
```

Revise only invalidated Voice/Speaker scope plus continuity materially affected by the change. Voice-only production changes do not reopen PRD-core acceptance when PRD canonical meaning is unchanged.

## Flow 7 proof

Use the proof channels owned by current Flow 7 policy/`VOICE-VALIDATION.md`:

```text
Mechanical
+ Communication Conservation
+ integrated Voice Script Readiness
+ Project HTML Visual when claimed
+ optional Audio Evidence when in scope
```

Static HTML parity is not visual proof; visual PASS requires actual rendered/browser inspection. Audio quality requires actual audio evidence.

## Non-negotiable boundaries

- SoundMaker scope is **Eleven v3 only**.
- Voice Production is downstream from accepted project/PRD meaning, not a separate source-intake project.
- recover existing project context before asking the user.
- Voice scope cannot change silently after Flow 5.
- downstream performance/presentation cannot create project facts, Speakers, Channels, Triggers, mechanics, rewards, outcomes, or source timing truth.
- exact canonical production content remains owned by `work/voice-production.md`.
- derived project HTML is not source truth.
- the retired DOCX export path must not be reintroduced without a new explicit product requirement.
- do not create separate Voice HTML, asset manifest, settings database, score system, or extra approval/workflow layer without a concrete defect.
- stop when the current requested scope is ready and sufficiently proven.
