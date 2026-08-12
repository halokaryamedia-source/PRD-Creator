# Next Action

Updated: 2026-08-13

## Current Status

`SOUNDMAKER_V3_QUALITY_ENGINE_READY`

Working branch: **`Local` only**.

## Current state

Project Document Generator remains **v1.13.0**. The approved Clockwork production package remains at `workspace/active/the-clockwork-vault/`; its accepted PRD meaning/rendered HTML were not changed.

Voice Production Kit is now **v1.4.0**.

Flow 5 Voice scope, DOCX builder/validator mechanics, and Voice ID/Type artifact structure remain unchanged. Flow 6 now has a bounded SoundMaker execution profile at:

```text
kits/voice-production-kit/SOUNDMAKER.md
```

SoundMaker is **Eleven v3 only** and remains inside Flow 6 rather than becoming another root skill or production Flow.

Current quality path:

```text
Voice Requirement
→ target duration first when specified
→ voice-fit check
→ performance map
→ natural spoken wording
→ beat architecture
→ punctuation / line structure
→ selective CAPS
→ minimal Audio Tags
→ pronunciation safety
→ one paste-ready Eleven v3 prompt
```

Actual generation/revision uses one active Voice ID at a time. If the user edits the prompt before generation and approves that result, the exact prompt actually used must be synchronized back into canonical `work/voice-production.md`. Generated audio is not called approved without actual review.

The ElevenLabs reference front door remains:

```text
kits/voice-production-kit/references/elevenlabs/README.md
```

Its operational scope is now v3-only. Evidence levels still separate current official guidance, product-specific evidence, creator heuristics, project calibration, and unknown/conflicting behavior.

The old post-Flow-7 `system_integration_proof` continuation is retired from active Voice procedure. Script/DOCX delivery may end at `complete` or continue to actual SoundMaker v3 generation when requested.

## Next Step

**Use SoundMaker v3 on the next real Voice ID/project line, then keep only actual approved prompt/audio behavior as project-calibrated evidence.**
