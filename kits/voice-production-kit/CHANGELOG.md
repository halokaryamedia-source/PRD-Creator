# Changelog

## 1.5.0 — 2026-08-13

- made `SOUNDMAKER.md` the single operational Eleven v3 execution procedure and removed duplicated prompting workflow from Flow/skill/reference owners;
- added explicit Enhance policy: untreated text may use Enhance as drafting aid, while an already-directed SoundMaker prompt keeps Enhance off by default and any rewrite becomes a new draft;
- added Speech Synthesis → Studio v3 routing for long-form whisper/volume/tone/accent drift or breaking without changing model family;
- converted voice-fit into a practical Voice Performance Envelope (`GOOD FIT`, `LIMITED FIT`, `RISKY FIT`, `UNKNOWN`);
- separated documented Audio Tags, descriptive candidates, and project-calibrated directions;
- strengthened post-generation diagnosis for take variance, flat delivery, chaotic output, Stability/voice drift, pronunciation, duration, and long-form surface problems;
- clarified source precedence so explicit v3 guidance overrides conflicting generic TTS guidance;
- kept Flow 5 scope, canonical `work/voice-production.md`, DOCX builder/validator mechanics, and artifact schema unchanged.

## 1.4.1 — 2026-08-13

- added a single default Eleven v3 generation baseline: `Stability: Natural` unless stronger approved project calibration exists;
- added an explicit pre-generation handoff so model, voice, Stability, exact prompt, timing target, and pronunciation risk are known before generation;
- added actual-audio quality review for intelligibility, voice identity, emotional movement, pacing, emphasis/landing, naturalness, pronunciation, and duration;
- separated four post-generation outcomes: approve, review alternative/regenerate, revise prompt, or flag voice-fit risk;
- kept the v3-only scope, Flow 5 Voice authority, canonical `work/voice-production.md`, DOCX builder/validator, and artifact schema unchanged.

## 1.4.0 — 2026-08-13

- made SoundMaker operational production **Eleven v3 only**;
- added `SOUNDMAKER.md` as the one-entry-at-a-time v3 quality/execution procedure inside Flow 6;
- established duration-first planning, voice-fit checking, scene-driven performance maps, spoken beat architecture, punctuation/CAPS-first directing, minimal tag stacking, reaction sequencing, and pronunciation safety;
- added a default one-prompt user experience for actual generation/revision tasks;
- added flat-delivery, duration-miss, and bad-take-vs-bad-prompt diagnosis order;
- required exact user-generated/approved prompt wording to synchronize back into canonical `work/voice-production.md`;
- removed Multilingual v2 fallback from the operational SoundMaker path while retaining evidence caveats in the reference register;
- replaced the stale post-Flow-7 `system_integration_proof` continuation with `complete_or_soundmaker_v3_generation`;
- did not change DOCX builder, validator, PRD contracts, or Voice ID/Type artifact schema.

## 1.3.1 — 2026-08-13

- added an evidence-backed ElevenLabs production reference for current Eleven v3 work;
- codified spoken/performance writing, punctuation/CAPS/tag layering, long-form emotional arcs, duration planning, model/voice/settings, pronunciation, generation variance, and long-form continuity guidance;
- separated current official evidence, product-specific behavior, creator heuristics, project calibration, and unknown/conflicting behavior;
- routed Flow 6 to the minimum relevant ElevenLabs reference instead of expanding the root skill;
- kept Flow 5 Voice scope, Flow 7 acceptance semantics, DOCX builder/validator behavior, and existing project artifacts unchanged.

## 1.3.0 — 2026-08-10

- implemented Flow 7 Voice Validation & Delivery;
- added `VOICE-VALIDATION.md`;
- added mechanical voice package validator;
- added requirement coverage, terminology/pronunciation, speaker/channel/trigger, performance continuity, and DOCX visual gates;
- added truthful optional audio-evidence model;
- added `work/voice-acceptance.md` / `voice_delivery_ready` lifecycle contract;
- kept script/DOCX delivery separate from unverified generated-audio claims.

## 1.2.0 — 2026-08-10

- implemented Flow 6 canonical performance-script production;
- added DOCX format contract and deterministic builder;
- enforced Flow 5 Voice ID/type parity;
- audited/codified Aftershock reference layout/performance behavior.

## 1.1.0 — 2026-08-10

- implemented Flow 5 Voice Requirement Extraction;
- introduced canonical voice requirements and voice lifecycle state.

## 1.0.0

- original Voice Production Kit baseline.
