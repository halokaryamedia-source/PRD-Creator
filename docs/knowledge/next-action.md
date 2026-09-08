# Next Action

## Current Status

`VOICE_NATURALNESS_3_1_1_CANDIDATE_READY`

The ElevenLabs Voice naturalness refinement is complete as a backward-compatible Package 3.1.1 candidate on `develop`. The user has explicitly deferred real audio testing; current work therefore stops at script/prompt/generation-method optimization and mechanical verification.

Completed high-value changes:

1. replace mandatory opening Audio Tags with a natural-baseline-first rule; zero-tag Voice prompts are valid when voice + wording + context already carry the intended delivery;
2. add an explicit spoken-language pass so Flow 6 rewrites PRD/document syntax into plausible speech while conserving every required fact;
3. add register-aware craft for direct NPC dialogue, narration, radio/mission communication, tutorial guidance, warnings, and completion lines;
4. make thought groups, sentence-length variation, listener-first information order, and clean landings the primary prosody tools before tags/settings;
5. prohibit fake-naturalness habits such as automatic filler, slang, hesitations, fragments, ellipses, or verbal tics without speaker/scene justification;
6. add same-speaker TTS continuity guidance using relevant `previous_text` / `next_text` or neighboring request IDs instead of padding short connected lines with audible filler;
7. deepen Voice Design guidance so language/dialect, timbre/persona, cadence/pacing, projection, emotion, and preview text establish a better baseline actor before per-line direction;
8. keep Stability at Natural by default and Speed at 1.0/unchanged when the active surface exposes it; settings are secondary to correct voice fit and spoken writing;
9. add a text-only Naturalness gate and stiffness-first diagnostic order without creating a numeric scorecard or new persisted schema;
10. preserve Package 3.1 Text to Dialogue, SFX, candidate-selection, and current Studio improvements.

No branch promotion, stable release/tag, or audio-quality claim has been made.

## Active Boundary

Keep all current work on `develop`.

- Package 3.1.1 accepts existing Package 3.1/3.0 Voice Production formats and only relaxes the old mandatory-initial-tag parser rule.
- `work/voice-production.md` remains the sole canonical Voice wording source.
- Audio Tags are optional performance controls, not required syntax.
- Generation continuity context remains ephemeral operator/API context; do not duplicate it into canonical Voice schema.
- Naturalness means speaker/register-appropriate speech, not automatic casualness.
- Current Golden bytes/design grammar remain unchanged.
- Actual generated-audio quality remains unproven until the user later requests a real audio test.
- Do not promote to `Local` until the user explicitly requests promotion after the current development phase is accepted.

## Next Step

Use the Package 3.1.1 naturalness rules for future Voice Prompt / narration preparation. Continue refining only if a concrete prompt-quality requirement appears; defer generated-audio testing until the user explicitly asks for it.