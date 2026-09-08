# Next Action

## Current Status

`VOICE_PREAUDIO_3_1_3_CANDIDATE_READY`

Package 3.1.3 completes the current pre-audio Voice preparation model. The user has explicitly deferred real audio testing, so current readiness covers script/prompt/casting/pronunciation/generation-method quality and mechanical verification only.

Completed high-value changes:

1. preserve 3.1.1 speechification, register-aware naturalness, thought groups, and TTS continuity;
2. preserve 3.1.2 Expression Coverage and first-class Audio Tag acting direction;
3. add actor-level continuity so every recurring Speaker has an internal baseline/range/no-drift boundary and each Moment is treated as a performance delta rather than a new personality;
4. make voice casting choose for the broadest required project envelope instead of one impressive isolated line;
5. add production reproducibility guidance around actual ElevenLabs `voice_id` and current Default-voice expiry on 2026-12-31;
6. add a pre-generation Language & Pronunciation pass for critical names, project terms, acronyms, numbers/dates/symbols, foreign/code-switched terms, and repeated technical vocabulary;
7. route pronunciation problems through spoken form / IPA / dictionary / voice-language fit instead of emotional prompt changes;
8. add Character Continuity Conservation and Pronunciation Conservation as semantic/craft gates inside Voice Script Readiness without new persisted schema;
9. add candidate-first Generation Mode discipline for ElevenLabs nondeterminism;
10. freeze text/tags/voice/settings/language/surface/context for initial candidate comparison, then change one variable class at a time only after a repeated defect is established;
11. preserve seed as best-effort consistency only and avoid ritual candidate counts;
12. synchronize package version ownership to 3.1.3.

No audio generation, browser proof, branch promotion, or heard-audio quality claim has been made.

## Active Boundary

Keep current work on `develop`.

- `work/voice-production.md` remains the sole canonical Voice wording/performance source.
- Actor maps, no-drift boundaries, pronunciation reasoning, and candidate histories remain reasoning/evidence context, not new canonical schemas.
- Audio Tags are not mandatory syntax, but material acting direction remains mandatory by craft.
- Recurring Speaker emotion is a delta from actor baseline, not permission for character drift.
- Critical pronunciation must have an intentional production strategy before generation when risk is material.
- One weak nondeterministic take must not trigger an immediate canonical rewrite.
- Current Golden design/machine identities remain unchanged.
- Do not promote to `Local` until explicitly requested.

## Next Step

For pre-audio preparation, Package 3.1.3 is the stop point. Do not add more Voice theory without a concrete new defect. When the user later permits generation, apply the candidate-first workflow and record only defects that are actually heard.
