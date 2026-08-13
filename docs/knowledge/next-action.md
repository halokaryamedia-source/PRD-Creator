# Next Action

Updated: 2026-08-13

## Current Status

`SOUNDMAKER_V3_KNOWLEDGE_HARDENED`

Working branch: **`Local` only**.

## Current state

Project Document Generator remains **v1.13.0**. The approved Clockwork production package remains at `workspace/active/the-clockwork-vault/`; its accepted PRD meaning/rendered HTML were not changed.

Voice Production Kit is now **v1.5.0**.

Flow 5 Voice scope, canonical `work/voice-production.md`, Voice ID/Type artifact structure, DOCX builder, and validator mechanics remain unchanged.

SoundMaker remains **Eleven v3 only** and is now the single operational execution procedure inside Flow 6:

```text
kits/voice-production-kit/SOUNDMAKER.md
```

The knowledge structure is now intentionally narrow:

```text
SOUNDMAKER.md
→ actual execution / generation / diagnosis

SCRIPT-PRODUCTION.md
→ Flow 6 lifecycle + canonical artifact

references/elevenlabs/v3-performance-writing.md
→ deep writing / tags / non-tag controls

references/elevenlabs/v3-duration-planning.md
→ timing only

references/elevenlabs/v3-production-reference.md
→ voice / Stability / Enhance / Studio / troubleshooting / pronunciation

references/elevenlabs/source-register.md
→ evidence only
```

Current operating decisions:

- default model: Eleven v3;
- default Stability: Natural unless stronger project calibration exists;
- already-directed SoundMaker prompt: Enhance OFF by default;
- Speech Synthesis is the normal surface;
- long-form whisper/volume/tone/accent drift or breaking may route to Studio while keeping v3;
- voice fit uses a practical performance envelope rather than tag stacking;
- documented tags, descriptive candidates, and project-calibrated directions are distinguished;
- heard failures are diagnosed as take variance, prompt/beat issue, Stability/over-direction, voice-fit/drift, pronunciation, duration, or long-form surface issue before revision.

Official v3-specific guidance has precedence over conflicting generic TTS guidance for v3 capabilities.

## Next Step

**Use SoundMaker v3.5 knowledge on the next real Voice ID only if the repository label is corrected to SoundMaker v3; then retain actual approved prompt/audio behavior as project calibration.**
