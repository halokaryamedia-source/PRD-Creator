# Next Action

## Current Status

`AUDIO_PRODUCTION_3_1_CANDIDATE_READY`

The ElevenLabs production-quality improvement is complete as an additive Package 3.1 candidate on `develop`. Existing machine schemas, stable Asset/Voice IDs, Flow 2–7 lifecycle, and approved Golden UI remain unchanged.

Completed high-value changes:

1. keep independent Voice IDs on Eleven v3 Text to Speech by default;
2. route conversationally dependent multi-speaker Voice IDs in the same approved Moment through Eleven v3 Text to Dialogue without introducing a Dialogue schema;
3. add candidate-selection discipline so one nondeterministic weak take does not trigger unnecessary prompt churn;
4. add current Dialogue request-limit, voice mapping, seed/language/pronunciation/normalization, and `with-timestamps` guidance for actual generation evidence;
5. replace deprecated Voiceover Studio assumptions with current ElevenCreative Studio routing;
6. add a dedicated `production-assets/SOUND-EFFECTS.md` execution owner for existing non-dialogue `AUDIO` requirements using `eleven_text_to_sound_v2`;
7. add SFX prompt construction, complex-effect layering, duration/loop/prompt-influence controls, candidate review, troubleshooting, and evidence rules without creating a new Flow or manifest;
8. refresh ElevenLabs Voice source authority to current documentation verified 2026-09-08;
9. make Voice Verify react to Voice skill/foundation/reference procedure changes instead of Python-only Voice paths;
10. preserve the earlier Astra efficiency/routing improvements and the same scope-proportional working model.

No branch promotion or stable release/tag was performed.

## Active Boundary

Keep all current work on `develop`.

- Package 3.1 is backward-compatible with Package 3.0 machine-authored project state/artifacts.
- `work/asset-requirements.md` remains the sole canonical non-Voice AUDIO meaning source; SFX prompts/settings are execution context.
- `work/voice-production.md` remains the sole canonical Voice wording source; Text to Dialogue grouping is generation-only context.
- Do not add Dialogue IDs, SFX manifests, audio scorecard databases, duplicate handoff files, or model-specific state schemas without a reproduced need.
- Current Golden bytes/design grammar remain unchanged.
- Full regression/browser proof remains mandatory before any eventual `develop → Local` promotion.

## Next Step

Run one representative real production test containing **(a) a same-Moment two-speaker conversation and (b) one non-dialogue SFX asset**, then record only concrete quality/friction defects. Keep fixes bounded to the first wrong owner and do not promote to `Local` until the user explicitly requests promotion after the pilot.
