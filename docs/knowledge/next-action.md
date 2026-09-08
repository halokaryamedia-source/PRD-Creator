# Next Action

## Current Status

`VOICE_PREAUDIO_3_1_3_READY`

Package 3.1.3 is now the synchronized pre-audio Voice baseline on `develop`. Final integration review confirmed that the Voice refinements remain contained inside the established Flow 5 → Flow 6 → Flow 7 architecture and do not introduce a parallel schema, manifest, acceptance layer, or alternate workflow.

Current preparation model:

1. Flow 5 remains the sole owner of Voice scope, Speaker, Moment, Trigger/Channel, Purpose, required communication, exclusions, and source timing truth;
2. Flow 6 remains the sole owner of final spoken wording/performance craft, including Actor/Character Continuity, natural spoken language, Expression Coverage/Audio Tags, pronunciation/language strategy, timing estimates, generation continuity, and generation-surface choice;
3. Flow 7 remains the sole readiness/delivery owner and now explicitly consumes the complete 3.1.3 craft model through one compact `Voice Script Readiness` decision;
4. `work/voice-production.md` remains the sole canonical Voice wording/performance source;
5. Character maps, no-drift boundaries, pronunciation reasoning, candidate comparisons, and generation context remain reasoning/evidence context rather than new canonical schemas;
6. `work/voice-acceptance.md` remains compact: Expression/Character/Pronunciation readiness is contained inside `Voice Script Readiness` rather than expanding the machine acceptance format;
7. non-dialogue AUDIO remains 04/SFX ownership and does not leak into Voice;
8. Golden design, Owner/Moment/VO identity, exact SHA binding, handoff rules, renderer ownership, and lifecycle vocabulary remain unchanged;
9. package version ownership is synchronized at 3.1.3 across `kits/prd-creator/README.md` and `kits/prd-creator/SKILL.md`;
10. final Voice/Repository CI is required to remain green before this state is treated as closed.

No audio generation, browser proof, stable promotion, or generated-audio quality claim has been made.

## Active Boundary

Keep current work on `develop`.

```text
accepted PRD / handoff_ready
→ Flow 5 Voice requirements
→ Flow 6 actor + wording + expression + pronunciation + continuity preparation
→ Flow 7 exact validation / delivery
```

- Do not reopen accepted PRD meaning for Voice-only craft changes unless the upstream Voice contract is actually wrong.
- Do not create additional Voice theory, schemas, cast databases, pronunciation manifests, candidate scorecards, or approval layers without a concrete defect.
- Audio Tags remain first-class acting controls when expression is material, not mandatory formatting.
- Recurring Speaker expression remains a delta from a stable actor baseline.
- Critical pronunciation requires an intentional strategy before generation when risk is material.
- One weak nondeterministic take does not justify an immediate canonical rewrite.
- Actual audio/pronunciation approval requires heard evidence.
- Do not promote to `Local` or `main` until explicitly requested.

## Next Step

No further pre-audio Voice refinement is recommended. The next Voice action should occur only when the user requests real generation/testing or a concrete production defect appears. Until then, treat Package 3.1.3 as the closed development baseline on `develop`.
