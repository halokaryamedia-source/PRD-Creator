---
name: voice-production
description: Semantic/product-contract specialist for PRD-Creator Flow 5–7. Use for PRD-derived Voice scope, Flow 5→6 intent completeness, canonical Voice production content, communication conservation, consolidated Production Assets presentation, or Voice validation/delivery semantics.
---

# Voice Production

This skill owns semantic judgment around Voice Production Flow 5–7. Detailed procedure stays in `kits/voice-production-kit/`.

## Authority

```text
accepted PRD
→ work/voice-requirements.md
→ work/voice-production.md
→ output/v<document.version>/prd.html
   → Production Assets
      → matching gameplay section
         → Audio
            → Voice Production
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

PRD owns project/gameplay truth. Flow 5 owns Voice scope, Speaker/Channel/Trigger/Purpose, communication requirements, and source timing truth. Flow 6 owns canonical production wording/performance. Flow 7 owns Voice readiness/evidence.

Generic `work/asset-requirements.md` may share the same Production Assets gameplay page but does not own or duplicate Voice data.

## Routing

- Voice scope/context defect → Flow 5 owners.
- Voice production wording/performance defect → Flow 6 / `SOUNDMAKER.md`.
- Voice validation/delivery defect → Flow 7 / `VOICE-VALIDATION.md`.
- correct canonical Voice but wrong objective-first HTML composition → Project Document Generator Production Assets compositor.
- optional DOCX-only defect → Voice DOCX owner/builder.
- missing project fact → return to accepted PRD authority.

## Production output

Production Assets sidebar navigation is objective-first:

```text
04 Production Assets
   <gameplay section title>
      <accepted PRD label>
```

Voice appears inside the matching page:

```text
Audio
→ Voice Production
```

The detailed Voice block retains line count, Primary Speaker, compact Voice Setup, and per-line:

```text
title
<accepted PRD label> · Voice Line X/Y
Context = exact Flow 5 Trigger
Speaker · Estimated Duration
canonical production text
Copy Prompt
```

The visible Context is a projection of the existing Flow 5 Trigger, not a new canonical field. Copy Prompt uses the exact canonical performance payload.

## Validation boundary

A Production Assets page can contain Voice plus other asset categories, so Voice mechanical validation checks Voice-specific sections and entries rather than treating every Production Assets page as Voice-only.

Static HTML checks do not prove visual quality. Generated-audio quality requires actual audio evidence.

## Scope discipline

Voice-only changes do not reopen PRD acceptance when PRD canonical sources are unchanged. Voice data is not duplicated into generic asset requirements, and no separate Voice HTML is required by default.
