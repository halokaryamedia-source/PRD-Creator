---
name: voice-production
description: Semantic/product-contract specialist for PRD-Creator Flow 5–7. Use when accepted PRD → Voice scope, communication intent, canonical Voice production meaning, communication conservation, or Voice readiness/delivery semantics are the actual problem. Do not use as a generic renderer/validator wrapper when semantics are already correct.
---

# Voice Production

Own **semantic judgment** for Voice Flow 5–7. Detailed execution, craft procedure, and executable routing stay with the nearest package owner.

## Authority

```text
accepted project / PRD meaning
→ canonical Voice requirements
→ canonical Voice Production
→ Voice acceptance / delivery evidence
```

Project/PRD authority owns gameplay/story truth. Voice may interpret approved communication/performance needs but may not invent upstream project facts. Derived HTML is presentation only, not Voice wording authority.

## Use when

Semantic judgment is required for:

- whether a Voice moment is justified by accepted project/PRD meaning;
- Flow 5 communication intent/context completeness;
- whether Flow 6 wording/performance preserves required communication;
- whether Voice scope/Speaker/Channel/Trigger/Purpose changed or must reopen;
- distinguishing a Voice semantic defect from presentation/mechanical failure;
- whether Flow 7 evidence truthfully supports readiness/delivery.

Do not load this skill merely because a task mentions ElevenLabs, AUDIO, HTML, Python, or validator.

## Detailed owners

```text
Flow 5 scope/context extraction
→ kits/prd-creator/voice/EXTRACTION.md

Flow 6 durable policy
→ docs/foundation/06-elevenlabs-script-production.md

Eleven v3 performance craft + generation-surface routing
→ kits/prd-creator/voice/PERFORMANCE-WRITING.md

Flow 7 validation/evidence
→ kits/prd-creator/voice/VALIDATION.md

normal end-to-end Voice execution
→ kits/prd-creator/SKILL.md
```

Shared 04 reader-facing resource fields/layout belong to `kits/prd-creator/production-assets/CONTRACT.md`; do not duplicate that schema here.

## Judgment rules

### Flow 5

Voice requirements define **what must be communicated, by whom, through which approved channel/trigger context, for what listener-facing purpose, with any authoritative timing truth**.

Do not create Voice because a reference project used it. Missing project-level facts return upstream instead of being invented downstream.

### Flow 6

Canonical Voice Production owns final wording/performance and production decisions allowed by the current Voice contract. It may not silently change Voice scope or upstream gameplay/story meaning.

Communication polish cannot remove required information or add unsupported lore, mechanics, rewards, or outcomes.

Generation surface is a production decision, not a new semantic identity. Independent speech normally uses Text to Speech; conversationally dependent multi-speaker Voice IDs in the same approved Moment may be generated together with Eleven v3 Text to Dialogue. The existing `VO-...` entries remain canonical and no Dialogue ID/source file is introduced merely for generation.

### Shared 04 presentation

Canonical Voice may appear as `AUDIO` inside the matching 04 gameplay moment, but presentation fields/layout belong to the shared Production Assets/rendering owners. Do not redefine Voice semantics to fit a presentation defect.

### Flow 7

Mechanical parity alone does not prove communication, visual, or generated-audio quality. Visual claims require rendered/browser evidence; audio quality requires actual audio evidence. A reviewed Text to Dialogue take may prove several constituent Voice IDs when all remain traceable to the same ordered Moment and exact canonical prompts.

## Routing boundary

```text
Voice meaning / communication contract wrong
→ this specialist + nearest Voice semantic owner

Voice meaning correct; presentation / validator / CLI mechanics wrong
→ kits/prd-creator/AGENTS.md → exact implementation owner

non-dialogue SFX
→ project-document-production / production-assets/SOUND-EFFECTS.md

shared dependency / test / CI wrong
→ repository engineering
```

If a technical change alters what Voice must represent or accept, reopen the semantic owner first.

## Proof economy

- recover accepted project/Voice context before asking the user;
- revise only invalidated Voice/Speaker scope;
- do not reopen PRD-core acceptance for Voice-only changes when upstream meaning is unchanged;
- do not duplicate Voice data into generic non-Voice asset requirements;
- do not add parallel Voice HTML, manifests, databases, scoring systems, approval layers, or speculative hardening without a concrete defect;
- stop when the requested semantic scope is correct and sufficiently proven.

## Boundary

This skill owns Voice Flow 5–7 **semantic judgment** only. Detailed procedure and executable mechanics stay with package owners; upstream project truth stays with PRD/project authority.
