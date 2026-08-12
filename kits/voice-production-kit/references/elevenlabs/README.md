# ElevenLabs Production Reference

Status: active Voice Production reference  
Last verified: 2026-08-13  
Primary target: ElevenLabs Speech Synthesis / Text to Speech using **Eleven v3**  
Secondary comparison: **Eleven Multilingual v2** when stability or voice fidelity matters more than expressive control

## Purpose

Turn accepted Flow 5 Voice Requirements into an actual production-ready ElevenLabs performance prompt without making the operator rediscover prompting theory each time.

This reference owns **production technique**, not project facts. It can shape wording, pacing, emphasis, performance direction, model/voice choice, duration planning, pronunciation handling, and generation strategy. It may not create a new Voice moment, speaker, channel, trigger, mechanic, reward, lore fact, or outcome.

Canonical project authority remains:

```text
accepted PRD
→ work/voice-requirements.md
→ work/voice-production.md
→ generated audio evidence when actually supplied/reviewed
```

## Evidence labels

Use these labels when a rule needs qualification:

- **OFFICIAL-CURRENT** — current ElevenLabs documentation supports it.
- **OFFICIAL-PRODUCT-SPECIFIC** — official behavior, but tied to a specific product such as Voiceover Studio or API rather than the normal web TTS page.
- **CREATOR-HEURISTIC** — creator/community practice that is useful but does not override official guidance.
- **PROJECT-CALIBRATED** — proved by an approved prompt/audio result for the actual project/voice/settings.
- **UNKNOWN** — current evidence is insufficient or conflicting; do not hard-code a rule.

See `source-register.md` for evidence provenance and freshness.

## Fast production path

### 1. Start from the Voice Requirement

Know before writing:

```text
who speaks
→ to whom
→ approved channel
→ trigger
→ what must be communicated
→ what must not be added/repeated
→ desired player response
```

Project context is not automatically spoken text.

### 2. Choose the model by the actual need

Use **Eleven v3** when the line needs meaningful emotional movement, character acting, reactions, whispers/shouts, or changes of pace/tone within the same text.

Use/compare **Multilingual v2** when the priority is maximum long-form stability, consistent voice identity, or a voice/PVC pairing behaves poorly with v3. Do not switch models just because one generation was weak.

### 3. Check voice fit before adding more direction

Voice selection is the most important v3 parameter according to ElevenLabs. The base voice must already be reasonably compatible with the target delivery.

If a calm/reassuring voice cannot produce convincing panic or shouting, do not solve that by stacking more tags. Re-evaluate the voice/model pairing.

### 4. Plan duration before writing when timing matters

If the user gives a target or maximum duration, read `v3-duration-planning.md` **before** drafting the script.

Do not write an oversized script and try to rescue it afterward with `[rushed]`, excessive punctuation, or extreme speed controls.

### 5. Build a performance map

For a long line, define the emotional/story movement first:

```text
scene state
→ new information/event
→ emotional reaction
→ escalation or release
→ final landing
```

Example:

```text
mysterious
→ curious
→ uneasy
→ urgent
→ firm
→ relieved/excited
```

An emotional change needs a scene/performance reason. Do not change tone merely because another sentence started.

### 6. Write the spoken text first

Use natural spoken language. Prefer one main idea/action per beat. Remove implementation detail the player does not need to hear.

Then apply controls in this order:

```text
spoken wording
→ sentence/beat structure
→ punctuation and line breaks
→ selective CAPS/emphasis
→ minimal Audio Tags
```

Detailed rules: `v3-performance-writing.md`.

### 7. Use tags as directing, not decoration

Official ElevenLabs guidance allows multiple tags, but does not define an ideal stack count. Production heuristic:

```text
0–1 tag at one beat  → default
2 tags                → valid when they control different compatible dimensions
3 tags                → exception; use only when all three add distinct audible information
4+ tags               → reject by default
```

Good double-tag logic:

```text
[nervous][quietly]
emotion + projection

[excited][rushed]
emotion + pace
```

Bad stacking:

```text
[excited][energetic][enthusiastic][intense]
```

Do not assume a tag lasts exactly N words or one paragraph. Standard Speech Synthesis v3 does not document a fixed tag-persistence window. Put direction close to the segment it should affect and re-establish direction only at a real performance change.

### 8. Use Natural as the default v3 stability baseline

ElevenLabs documents:

- **Creative** — more expressive, more variable/risk-prone;
- **Natural** — balanced and closest to the reference voice;
- **Robust** — more stable but less responsive to directional prompting.

Start with **Natural** unless the current project has a stronger calibrated setting. Move toward Creative only after voice fit, wording, and beat structure are already sound.

### 9. Generate, then diagnose the result correctly

A weak take does not automatically prove a weak prompt. ElevenLabs TTS is nondeterministic.

Use this diagnosis order:

```text
wrong fact/meaning
→ script defect

correct meaning but flat structure
→ beat/writing defect

correct structure but target delivery is outside the base voice
→ voice/model compatibility defect

one odd take with otherwise sound prompt
→ generation variance; prefer another available take/regeneration before rewriting
```

### 10. Lock approved evidence

When an actual generated result is approved, retain the strongest useful production evidence:

```text
Voice ID / task
exact prompt actually used
voice
model
stability / visible settings
actual duration
approved pronunciation for material terms
what worked / what failed
actual audio evidence location when available
```

This becomes **PROJECT-CALIBRATED** evidence for later lines. It is stronger than generic internet advice for that exact voice/project, but it does not become a new upstream gameplay/story authority.

## Minimal operator output recipe

Internally resolve:

```text
Intent: <what this moment must achieve>
Target duration: <none / range / hard max / fixed-sync>
Model: <v3 / Multilingual v2>
Voice fit: <good / risk / unknown>
Performance arc: <state → state → state>
Pronunciation risks: <terms>
```

The user-facing generation result should stay simple:

```text
## <VOICE-ID / TASK NAME>

<prompt text ready to paste into ElevenLabs>
```

Do not expose internal QA/state unless requested.

## Supporting pages

- `v3-performance-writing.md` — wording, beat architecture, punctuation, CAPS, line breaks, tags, stacking, reactions, long-form emotional movement.
- `v3-duration-planning.md` — target duration, word budgets, project calibration, Dynamic vs Fixed Duration.
- `v3-production-reference.md` — model/voice/settings, credits, generation variance, pronunciation, normalization, long-form continuity, UI/documentation caveats.
- `source-register.md` — evidence authority and source freshness.

## Stop rule

Do not add another prompting rule because it sounds plausible. New reusable rules require one of:

1. current official ElevenLabs evidence;
2. clearly labeled creator/community evidence that does not conflict with official guidance; or
3. approved project-calibrated audio evidence.
