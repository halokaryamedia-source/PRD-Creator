---
name: voice-production
description: Reusable semantic/product-contract specialist for PRD-Creator Flow 5–7. Use when accepted PRD → Voice scope, Flow 5 communication intent, canonical Voice production meaning, communication conservation, or Voice readiness/delivery semantics are the actual problem. Do not use as a generic DOCX/HTML/builder/validator wrapper when semantics are already correct.
---

# Voice Production

Own **semantic judgment** around Voice Production Flow 5–7. Detailed Production Execution stays in `kits/voice-production-kit/SKILL.md`; exact craft/validation procedure stays in the nearest Voice owner.

## Semantic authority shape

```text
accepted project / PRD meaning
→ canonical Voice requirements
→ canonical Voice Production
→ Voice acceptance / delivery evidence
```

Project/PRD authority owns gameplay/story truth. Voice work may interpret approved communication/performance needs but may not invent upstream project facts.

Derived project HTML and optional DOCX are presentation only, not Voice wording authority.

## Use this specialist when

The actual question requires reusable judgment about:

- whether a Voice moment is justified by accepted project/PRD meaning;
- whether Flow 5 communication intent/context is complete enough for production;
- whether Flow 6 wording/performance preserves required communication without changing upstream meaning;
- whether Voice scope/Speaker/Channel/Trigger/Purpose has changed or must be reopened;
- whether a downstream presentation problem is semantic or purely compositor/builder mechanics;
- whether Flow 7 evidence truthfully supports Voice readiness/delivery.

Do not load this skill solely because a task mentions ElevenLabs, AUDIO, HTML, DOCX, Python, builder, or validator.

## Canonical detailed owners

```text
Flow 5 scope/context extraction
→ kits/voice-production-kit/VOICE-EXTRACTION.md

Flow 6 durable policy
→ docs/foundation/06-elevenlabs-script-production.md

Eleven v3 performance-writing craft
→ kits/voice-production-kit/SOUNDMAKER.md

Flow 7 validation/evidence
→ kits/voice-production-kit/VOICE-VALIDATION.md

normal end-to-end Voice Production Execution
→ kits/voice-production-kit/SKILL.md
```

The shared 04 Production Assets exact reader-facing resource contract is owned by `kits/project-document-generator/PRODUCTION-ASSETS.md`; do not duplicate its field schema here.

## Semantic judgment rules

### Flow 5

Voice requirements define **what must be communicated, by whom, through which approved channel/trigger context, for what listener-facing purpose, with any authoritative timing truth**.

Do not create Voice merely because a reference project used it. Missing project-level facts return upstream instead of being invented downstream.

### Flow 6

Canonical Voice Production owns final production wording/performance and production decisions allowed by the current Voice contract. It may not silently change Voice scope or upstream gameplay/story meaning.

Communication polish cannot remove required information or add unsupported lore/mechanics/rewards/outcomes.

### Shared project HTML

Canonical Voice may be presented as `AUDIO` inside the matching 04 gameplay moment, but exact visible resource fields/layout belong to the shared Production Assets contract/compositor.

If Voice canonical meaning is correct but the 04 HTML is wrong:

```text
→ Project Document Generator 04 compositor owner
```

Do not redefine Voice semantics merely to fit a presentation defect.

### Flow 7

Mechanical parity alone does not prove communication quality, visual quality, or generated-audio quality. Visual claims require rendered/browser evidence; audio quality requires actual audio evidence.

## Semantic vs technical handoff

When semantics are correct:

```text
Voice-specific 04 parsing/presentation primitive defect
→ Project Document kit implementation owner

optional DOCX builder/pagination defect
→ Voice kit AGENTS + builder

Voice mechanical validator defect
→ Voice kit AGENTS + validator

shared dependency/test/CI defect
→ repository engineering
```

If a technical change alters what Voice is required to represent/accept, reopen the semantic owner first.

## Proof economy

- recover accepted project/Voice context before asking the user;
- revise only invalidated Voice/Speaker scope;
- do not reopen PRD-core acceptance for Voice-only changes when PRD meaning is unchanged;
- do not duplicate Voice data into generic non-Voice asset requirements;
- do not add separate Voice HTML, asset manifests, settings databases, scoring systems, extra approval layers, or speculative hardening without a concrete defect;
- stop when the requested semantic scope is correct and sufficiently proven.

## Boundary

This skill owns Voice Flow 5–7 **semantic judgment** only. Detailed production procedure stays in the Voice kit; pure builder/validator/presentation mechanics stay with exact implementation owners; upstream project truth stays with the PRD/project authority.
