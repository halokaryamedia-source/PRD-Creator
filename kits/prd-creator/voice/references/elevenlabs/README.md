# Eleven v3 Reference Index

Status: active Voice Production reference  
Last verified: 2026-08-13  
Scope: **Eleven v3 only**

## Purpose

This folder stores evidence-backed Eleven v3 production knowledge. It does **not** own project facts or the execution workflow.

Use:

```text
actual Voice task
→ SOUNDMAKER.md
→ open only the reference needed by the active problem
```

Canonical project authority remains:

```text
accepted PRD
→ work/voice-requirements.md
→ work/voice-production.md
→ generated audio evidence when actually reviewed
```

## Reference map

| Need | Open |
|---|---|
| How to produce one v3 prompt | `../../SOUNDMAKER.md` |
| Spoken wording, beats, punctuation, CAPS, Audio Tags | `v3-performance-writing.md` |
| Target / max / fixed duration | `v3-duration-planning.md` |
| Voice fit, Stability, Enhance, Studio, regeneration, pronunciation, troubleshooting | `v3-production-reference.md` |
| Why a reusable rule is trusted | `source-register.md` |

Do not load every page by default.

## Evidence labels

- **OFFICIAL-CURRENT** — current ElevenLabs guidance directly supports the rule.
- **OFFICIAL-PRODUCT-SPECIFIC** — official behavior for a specific ElevenLabs surface such as Studio/API.
- **CREATOR-HEURISTIC** — useful creator/community practice, not product truth.
- **PROJECT-CALIBRATED** — approved result for the actual project/voice/settings.
- **UNKNOWN** — evidence is insufficient or conflicting; do not hard-code it.

For v3 behavior, **v3-specific official documentation overrides generic TTS guidance when the capability explicitly differs**.

Examples:

- generic SSML pause guidance does not override the v3-specific rule that Eleven v3 does not support SSML `<break>`;
- generic special-character warnings do not invalidate v3 Audio Tags in square brackets.

## Operational defaults

These are only navigation-level reminders; detailed rules live in their owners:

```text
Model: Eleven v3
Default Stability: Natural
Enhance on a SoundMaker-directed prompt: OFF by default
Normal surface: Speech Synthesis
Long-form drift/whisper/accent/tone instability: consider Studio with v3
```

## Stop rule

Do not add another reusable prompting rule because it sounds plausible. A new rule needs current official evidence, clearly labeled creator evidence that does not conflict with official guidance, or actual approved project calibration.
