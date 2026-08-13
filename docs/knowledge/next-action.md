# Next Action

Updated: 2026-08-13

## Current Status

`SOUNDMAKER_V3_GENERATION_QA_READY`

Working branch: **`Local` only**.

## Current state

Project Document Generator remains **v1.13.0**. The approved Clockwork production package remains at `workspace/active/the-clockwork-vault/`; its accepted PRD meaning/rendered HTML were not changed.

Voice Production Kit is now **v1.4.1**.

Flow 5 Voice scope, DOCX builder/validator mechanics, and Voice ID/Type artifact structure remain unchanged. Flow 6 has a bounded SoundMaker execution profile at:

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
→ generation baseline
→ one paste-ready Eleven v3 prompt
→ actual audio quality review when audio exists
```

Default generation baseline is:

```text
Eleven v3
Stability: Natural
```

unless stronger approved project-calibrated evidence exists for the same production.

Actual generated audio is judged from the heard take for meaning/intelligibility, voice identity, emotional movement, pacing, emphasis/landing, naturalness, pronunciation, and duration when timing matters. A weak result is classified as one of: review alternative/regenerate, revise prompt, or voice-fit risk; a flat take is not repaired automatically by adding more tags.

Actual generation/revision uses one active Voice ID at a time. If the user edits the prompt before generation and approves that result, the exact prompt actually used must be synchronized back into canonical `work/voice-production.md`. Generated audio is not called approved without actual review.

The ElevenLabs reference front door remains:

```text
kits/voice-production-kit/references/elevenlabs/README.md
```

Its operational scope is v3-only. Evidence levels still separate current official guidance, product-specific evidence, creator heuristics, project calibration, and unknown/conflicting behavior.

## Next Step

**Use SoundMaker v3 quality behavior on the next real Voice ID/project line, then retain only actual approved prompt/audio behavior as project-calibrated evidence.**
