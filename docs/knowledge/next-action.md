# Next Action

## Current Status

`VOICE_EXPRESSION_3_1_2_CANDIDATE_READY`

Package 3.1.2 corrects the Voice naturalness refinement so Eleven v3 expression remains fully directed without returning to mandatory boilerplate tags.

Completed high-value changes:

1. preserve Package 3.1.1 speechification, register-aware naturalness, thought groups, and narration continuity;
2. elevate Audio Tags back to **first-class acting controls** rather than treating them as last-resort decoration;
3. add `v3-expression-direction.md` with an internal Expression Coverage Map for Baseline State, Emotion, Attitude/Subtext, Projection, Pace/Rhythm, Intensity/Energy, Cognitive State, Reaction, Transitions, and Landing;
4. replace `minimum tags` thinking with **complete expression coverage without redundant direction**;
5. require explicit direction when material emotion/subtext/projection/pacing/reaction/transition would otherwise be ambiguous or under-directed;
6. keep zero-tag prompts valid only for true natural-baseline lines with no material acting requirement beyond voice/text context;
7. require material opening states to be anchored, material state changes to be directed near transitions, and reactions to be placed at their event point;
8. keep 1 tag preferred when sufficient, allow 2 compatible dimensions, and reserve 3+ simultaneous tags for concrete/calibrated need;
9. treat every new TTS request as a possible acting reset: previous/next context preserves prosody, while critical continuing expression is re-anchored at the new clip opening when necessary;
10. apply the same Expression Coverage principle per Text-to-Dialogue turn, including interruption/overlap/reaction dynamics;
11. align Stability policy with current ElevenLabs guidance: Natural baseline, Creative for intentional extra range, Robust only when consistency outweighs directional responsiveness;
12. retain no new expression schema/manifest/scorecard; Expression Conservation remains part of Voice Script Readiness.

The user has explicitly deferred real audio testing. No generated-audio quality claim is made.

## Active Boundary

Keep current work on `develop`.

- `work/voice-production.md` remains the sole canonical Voice wording/performance source.
- Audio Tags are not mandatory syntax, but material acting direction is mandatory by craft.
- Do not remove expression-bearing tags solely to make prompts cleaner.
- Do not add tags solely to satisfy a template.
- Naturalness and expression are separate complementary goals.
- Generation continuity context remains ephemeral; do not duplicate it into canonical schema.
- Current Golden design/machine identities remain unchanged.
- Do not promote to `Local` until explicitly requested.

## Next Step

Use Package 3.1.2 as the current preparation policy. Further Voice changes should be driven by a concrete prompt/production defect or, when the user later permits it, actual generated-audio evidence.
