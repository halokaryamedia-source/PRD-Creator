# Changelog

## 1.9.0 — 2026-08-13

- hardened the **Flow 5 → Flow 6 interface** so SoundMaker receives complete communication intent before performance writing;
- defined the direct mapping `Function + Purpose → Communication Job`, `Trigger + Channel → Listener State`, `Must communicate → Information Payload`, `Purpose → Listener Outcome`, `Speaker → Speaker Owner`, and `Must not add/repeat → Scope Guardrails`;
- clarified Flow 5 field quality: Trigger must describe the actual gameplay/story state when material, Purpose must express the listener-facing result, and independently actionable required facts should stay distinct enough to conserve downstream;
- added optional **`Timing Constraint`** to Flow 5 only for authoritative line/window/fixed-sync truth; kept it explicitly separate from Flow 6 `Estimated Duration`;
- taught SoundMaker to consume the Flow 5 requirement first and reopen accepted PRD context only when genuinely necessary delivery context is missing;
- required Communication Conservation and Voice Script Readiness to preserve any authoritative Flow 5 timing constraint without converting production estimates into source truth;
- preserved Performance Shape, Landing, final wording, tags, CAPS/punctuation, Target Voice Profile, selected voice, Stability, Surface, and Estimated Duration as Flow 6 production interpretation;
- added no new artifact family, lifecycle state, builder/validator mechanics, Flow 6 canonical entry field, dependency, or audio-test requirement.

## 1.8.0 — 2026-08-13

- adapted the strongest PRD-Creator reasoning patterns into SoundMaker without adding a new Flow, file family, schema, score system, or audio-test requirement;
- added **Voice Intent Completeness** with one internal Performance Fill Map covering communication job, listener state, information payload, listener outcome, speaker identity, timing envelope, performance shape, and landing;
- distinguished normal **production interpretation** from unresolved material creative/project decisions so punctuation/tags/phrasing do not require unnecessary approval while project facts still return upstream;
- added **Communication Conservation** so every material Flow 5 `Must communicate` fact survives wording polish and duration compression while `Must not add/repeat` remains binding;
- replaced fragmented semantic review behavior with one integrated **Voice Script Readiness** decision using Communication, Listener, Character, Performance, Timing, Continuity, and Operator lenses;
- kept Communication Conservation explicit because a polished script can still omit required meaning;
- formalized first-wrong-owner routing and bounded revision so only invalidated Voice/speaker scope is replayed;
- compacted `work/voice-acceptance.md` semantics while preserving the existing `voice-state.yaml` schema for compatibility;
- added an explicit Preparation Mode stop rule to prevent optional tag/schema/artifact/proof-layer expansion after current scope is ready;
- changed no builder/validator mechanics, dependencies, canonical Flow 6 entry schema, PRD behavior, or audio generation.

## 1.7.0 — 2026-08-13

- formalized a compact three-layer static output contract: canonical script, derived operator handoff, and derived DOCX;
- added `Speaker:` as the single new required Flow 6 entry field because the ElevenLabs operator must not infer which character owns a line;
- made builder/validator fail closed on Voice ID, Type, and Speaker parity against Flow 5;
- exposed `Type · Speaker` in the generated DOCX while keeping Trigger, Channel, Purpose, requirement bullets, source refs, WPM math, performance maps, voice-fit ratings, and QA notes out of the final operator artifact;
- kept the Eleven v3 prompt block exact and free of internal commentary;
- defined a compact operator handoff that states shared voice/settings once and shows only Voice ID, Speaker, Estimated Duration, exact prompt, plus exceptional production notes when required;
- added focused regression coverage for speaker parity and DOCX speaker visibility;
- created no extra handoff artifact, settings database, workflow layer, or audio test requirement.

## 1.6.0 — 2026-08-13

- separated **Preparation Mode** from actual ElevenLabs **Generation Mode**;
- allowed full-project/batch Voice script preparation without audio testing or per-line approval loops;
- kept actual generation/revision one active Voice ID at a time;
- added context recovery before asking the user for already-known project facts;
- added recurring-speaker continuity, information-progression, and cross-line anti-template/repetition gates;
- clarified pronunciation planning as preparation evidence rather than generated proof;
- improved duration planning hierarchy: nearest approved similar sample → project-calibrated rate → generic WPM fallback, while keeping no-audio preparation fully valid;
- synchronized root/kit routing and Flow 6 policy so `one Voice ID at a time` applies only to Generation Mode;
- changed no builder/validator mechanics, dependencies, Voice ID/Type schema, PRD behavior, or audio generation.

## 1.5.0 — 2026-08-13

- made `SOUNDMAKER.md` the single operational Eleven v3 procedure and reduced duplicated prompting workflow across reference/Flow files;
- set directed SoundMaker prompts to **Enhance OFF by default**; Enhance output is a new draft requiring review;
- added Speech Synthesis → Studio v3 routing for long-form whisper/volume/tone/accent drift or breaking without changing model family;
- added practical Voice Performance Envelope (`GOOD / LIMITED / RISKY / UNKNOWN`) before compensating with more direction;
- separated documented Audio Tags, descriptive candidates, and project-calibrated directions;
- expanded heard-result diagnosis to distinguish take variance, flat writing, over-direction/Stability, voice-fit/drift, pronunciation, duration, and long-form surface issues;
- added explicit precedence for v3-specific official guidance over conflicting generic TTS guidance;
- kept SoundMaker v3-only and changed no builder/validator mechanics, dependencies, PRD artifacts, or Voice ID/Type schema.

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
