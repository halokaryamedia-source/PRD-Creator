# Voice Production Kit v1.11.2

Voice Production Kit owns accepted PRD → Voice requirements → canonical Eleven v3 production content → Voice validation/delivery.

## Flow

```text
accepted PRD
→ work/voice-requirements.md
→ work/voice-production.md
→ same output/v<document.version>/prd.html
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

## Current project HTML presentation

Production Assets is objective-first:

```text
04 Production Assets
   <gameplay section title>
      <accepted PRD label>
```

When that gameplay section contains Voice, the page presents:

```text
Audio
→ Voice Production
```

The detailed Voice block still contains Voice line count, Primary Speaker, compact Voice Setup, and per-line:

```text
title
<accepted PRD label> · Voice Line X/Y
Context = exact Flow 5 Trigger
Speaker · Estimated Duration
canonical Eleven v3 content
Copy Prompt
```

Voice content remains canonical in `work/voice-production.md` and is not copied into generic `work/asset-requirements.md`.

A Production Assets page may also contain non-Voice categories. Voice validation therefore checks Voice-specific sections/entries rather than treating every Production Assets page as Voice-only.

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

The objective-first presentation change does not alter Voice wording, Speaker/Type/Trigger authority, performance payloads, or the v1.11.2 Voice semantic contract.
