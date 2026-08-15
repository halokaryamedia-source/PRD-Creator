# Voice Production Kit v1.11.2

Voice Production Kit owns accepted project/PRD meaning → Voice requirements → canonical Eleven v3 production content → Voice validation/delivery.

## Flow

```text
accepted project / PRD meaning
→ work/voice-requirements.md
→ work/voice-production.md
→ same output/v<document.version>/prd.html
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

## Current project HTML presentation

Production Assets navigation is objective-first and page bodies are moment-first:

```text
04 Production Assets
   <gameplay section title>
      <accepted PRD label>

page body
→ <natural gameplay moment>
   → AUDIO
```

Voice does not create a separate category/dashboard inside 04. Each canonical line appears as:

```text
AUDIO
<Character> — <Line Title>

Function
<communication/story purpose>

Voice Preset
<selected actor voice>

ElevenLabs Model
Eleven v3

Estimated Duration
<duration>

Prompt
<exact canonical Eleven v3 performance payload>
```

Performance-direction tags are visually distinct from spoken dialogue. `Copy Prompt` copies the exact canonical payload.

Visible line count, Primary Speaker, Voice Setup, Flow 5 Context/Trigger, and a separate Speaker row are not part of the current 04 reader-first contract. Those facts remain in their canonical Voice owners when needed for production reasoning/validation.

Voice content remains canonical in `work/voice-production.md` and is not copied into generic `work/asset-requirements.md`.

A Production Assets page may also contain non-Voice MODEL / ITEM / UI / TEXT / AUDIO / PARTICLE resources. Voice validation therefore checks Voice-specific canonical parity rather than treating every Production Assets page as Voice-only.

## Active owners

```text
VOICE-EXTRACTION.md    Flow 5 scope/context
SOUNDMAKER.md          Eleven v3 performance production
VOICE-VALIDATION.md    Flow 7 validation/evidence
DOCX-FORMAT.md         optional portable export
```

`SCRIPT-PRODUCTION.md` remains retired as a duplicate lifecycle owner.

## Optional DOCX

`output/Voice Production.docx` is optional and does not replace canonical Voice Production or the consolidated project HTML.

The 04 presentation contract does not alter Voice wording, Speaker/Type/Trigger authority, performance payloads, or the v1.11.2 Voice semantic contract.
