---
name: voice-production
description: Semantic/product-contract specialist for PRD-Creator Flow 5–7. Use for PRD-derived Voice scope, Flow 5→6 intent completeness, canonical Voice production content, communication conservation, consolidated 04 AUDIO presentation, or Voice validation/delivery semantics.
---

# Voice Production

This skill owns semantic judgment around Voice Production Flow 5–7. Detailed procedure stays in `kits/voice-production-kit/`.

## Authority

```text
accepted project / PRD meaning
→ work/voice-requirements.md
→ work/voice-production.md
→ output/v<document.version>/prd.html
   → 04 Production Assets
      → matching gameplay moment
         → AUDIO
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

PRD/project authority owns gameplay/story truth. Flow 5 owns Voice scope, Speaker/Channel/Trigger/Purpose, communication requirements, and source timing truth. Flow 6 owns canonical production wording/performance, Estimated Duration, and actor-voice selection when known. Flow 7 owns Voice readiness/evidence.

Generic `work/asset-requirements.md` may share the same Production Assets gameplay page but does not own or duplicate Voice data.

## Routing

- Voice scope/context defect → Flow 5 owners.
- Voice production wording/performance defect → Flow 6 / `SOUNDMAKER.md`.
- Voice validation/delivery defect → Flow 7 / `VOICE-VALIDATION.md`.
- correct canonical Voice but wrong objective/moment-first HTML composition → Project Document Generator Production Assets compositor.
- optional DOCX-only defect → Voice DOCX owner/builder.
- missing project fact → return to accepted PRD/project authority.

## Production output

Production Assets sidebar navigation is objective-first:

```text
04 Production Assets
   <gameplay section title>
      <accepted PRD label>
```

Voice does **not** create an `Audio → Voice Production` sub-dashboard. Each canonical Voice line is presented as an `AUDIO` resource inside its matching natural gameplay moment:

```text
AUDIO
<Character> — <Line Title>

Function
<communication/story purpose at this moment>

Voice Preset
<selected actor voice>

ElevenLabs Model
Eleven v3

Estimated Duration
<duration>

Prompt
<exact canonical performance payload>
```

Do not show separate visible `Speaker`, Flow 5 `Context`, Trigger, line count, Primary Speaker, or Voice Setup metadata when the current 04 contract does not need them. Character identity is already in the resource title; Flow 5 Trigger/Purpose/requirements/source refs remain in their canonical owners.

Performance-direction tags remain visually distinct from spoken dialogue while `Copy Prompt` copies the exact canonical performance payload.

## Validation boundary

A Production Assets page can contain Voice plus non-Voice resources, so Voice mechanical validation checks Voice-specific canonical parity and prompt presence rather than treating every Production Assets page as Voice-only.

The Project Document 04 regression owns visible AUDIO-field/compositor behavior. Voice validation owns Voice requirement/script/payload semantics.

Static HTML checks do not prove visual quality. Generated-audio quality requires actual audio evidence.

## Scope discipline

Voice-only changes do not reopen PRD-core acceptance when PRD canonical sources are unchanged. Voice data is not duplicated into generic asset requirements, no separate Voice HTML is required by default, and Voice presentation changes do not authorize 01–03 changes.
