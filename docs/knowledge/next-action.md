# Next Action

Updated: 2026-08-13

## Current Status

`SOUNDMAKER_V3_PREPARATION_WORKFLOW_READY`

Working branch: **`Local` only**.

## Current state

Project Document Generator remains **v1.13.0**. The approved Clockwork production package remains at `workspace/active/the-clockwork-vault/`; its accepted PRD meaning/rendered HTML were not changed.

Voice Production Kit is now **v1.6.0**.

Flow 5 Voice scope, canonical `work/voice-production.md`, Voice ID/Type artifact structure, DOCX builder, validator mechanics, and PRD behavior remain unchanged.

SoundMaker remains **Eleven v3 only** and now separates two working modes:

```text
Preparation Mode
→ full current Voice scope
→ no audio testing required
→ per-line SoundMaker construction
→ project-level speaker continuity / anti-repetition
→ duration + pronunciation planning
→ canonical script / optional DOCX

Generation Mode
→ only when actual ElevenLabs output is requested
→ one active Voice ID
→ one exact reviewed prompt
→ feedback / approval / canonical sync
```

Preparation Mode explicitly recovers current project context before asking the user and may finish at `voice_script_ready` with `audio_evidence: not_provided`.

Current non-audio quality workflow includes:

- requirement fidelity before performance polish;
- duration-first planning when timing matters;
- Voice Performance Envelope without requiring an actual audio test;
- spoken beats before punctuation/CAPS/Audio Tags;
- Enhance OFF by default on already-directed prompts;
- Speech Synthesis normally; Studio v3 only for long-form instability;
- project-level speaker continuity and information progression;
- anti-template review across openings, beat chains, tag placement, CAPS endings, sentence rhythm, and closing patterns;
- pronunciation risk planning without false verification;
- duration evidence hierarchy: nearest approved similar sample when available → calibrated project rate → generic WPM fallback; no-audio preparation uses the fallback honestly.

Material pronunciation risk may remain during Flow 6 Preparation Mode, but `voice_delivery_ready` remains fail-closed until the risk is confirmed or explicitly accepted-as-written.

No audio generation or listening test is part of this current workflow-hardening milestone.

## Next Step

**Continue only with another concrete non-audio workflow/content defect, or apply Preparation Mode to a project package when requested; do not require audio testing until the user explicitly starts Generation Mode.**
