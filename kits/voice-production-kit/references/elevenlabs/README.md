# Eleven v3 Production Reference

Status: active Voice Production reference  
Last verified: 2026-08-13  
Primary target: ElevenLabs Speech Synthesis / Text to Speech using **Eleven v3 only**

## Purpose

Turn accepted Flow 5 Voice Requirements into actual generation-ready Eleven v3 performance direction without making the operator rediscover prompting theory each time.

This reference owns **production technique**, not project facts. It can shape wording, pacing, emphasis, performance direction, duration planning, pronunciation handling, voice-fit judgment, and generation strategy. It may not create a new Voice moment, speaker, channel, trigger, mechanic, reward, lore fact, or outcome.

Canonical project authority remains:

```text
accepted PRD
→ work/voice-requirements.md
→ SoundMaker v3 quality pass
→ work/voice-production.md
→ generated audio evidence when actually supplied/reviewed
```

## Operational scope

This reference is deliberately **v3-only**.

Do not use it to select or fall back to another ElevenLabs model family. If a voice performs poorly with v3, treat that as a voice-fit/compatibility issue and prefer a more suitable v3-compatible voice rather than changing SoundMaker's model scope.

Other model families may remain documented in external/historical sources, but they are not part of this operational path.

## Evidence labels

- **OFFICIAL-CURRENT** — current ElevenLabs documentation supports it.
- **OFFICIAL-PRODUCT-SPECIFIC** — official behavior tied to a different ElevenLabs product surface such as Voiceover Studio or API.
- **CREATOR-HEURISTIC** — useful creator/community practice that does not override official guidance.
- **PROJECT-CALIBRATED** — proved by an approved prompt/audio result for the actual project/voice/settings.
- **UNKNOWN** — evidence is insufficient or conflicting; do not hard-code a rule.

See `source-register.md` for provenance and freshness.

# Fast production path

## 1. Start from one Voice Requirement

Resolve:

```text
who speaks
→ who hears it
→ approved channel
→ trigger
→ what must be communicated
→ what must not be added/repeated
→ desired listener response
```

Project context is not automatically spoken text.

For an actual one-line production/revision, use `../../SOUNDMAKER.md` as the execution procedure.

## 2. Model is fixed

```text
Eleven v3
```

Do not spend the production turn comparing models. The remaining decisions are voice fit, performance construction, timing, pronunciation, and generation behavior.

## 3. Check voice fit before adding direction

**OFFICIAL-CURRENT:** ElevenLabs identifies voice choice as the most important v3 parameter.

The base voice must be reasonably compatible with the required delivery. If a calm/reassuring voice cannot produce convincing panic, shouting, comedy, or other required extremes, do not solve that by stacking more tags.

Prefer a more suitable v3 voice/profile when the range mismatch is material.

## 4. Plan duration before writing when timing matters

If the user gives a target/max/fixed duration, read `v3-duration-planning.md` **before** drafting.

Do not write an oversized script and try to rescue it afterward with `[rushed]`, tag spam, or extreme speed changes.

## 5. Build a performance map

For a line with meaningful movement:

```text
scene state
→ new information/event
→ emotional reaction
→ escalation or release
→ final instruction/payoff/landing
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

## 6. Write the speech first

Use natural spoken language. Prefer one main idea/action per beat. Remove implementation detail the player does not need to hear.

Then apply controls in this order:

```text
spoken wording
→ sentence / beat structure
→ punctuation and line breaks
→ selective CAPS
→ minimal Audio Tags
```

Detailed rules: `v3-performance-writing.md`.

## 7. Use tags as directing, not decoration

Official ElevenLabs guidance allows multiple tags but does not define an ideal stack count.

Repository heuristic:

```text
0–1 tag at one beat → default
2 tags               → valid when they control different compatible dimensions
3 tags               → exception; preferably project-calibrated
4+ tags               → reject by default
```

Good:

```text
[nervous][quietly]
```

Bad:

```text
[excited][energetic][enthusiastic][intense]
```

Do not assume a tag lasts exactly N words or one paragraph. Standard Speech Synthesis v3 does not document a fixed persistence window.

## 8. Use Natural as baseline Stability

**OFFICIAL-CURRENT:** v3 Stability behavior is broadly:

- **Creative** — more expressive and more variable;
- **Natural** — balanced and closest to the reference voice;
- **Robust** — more stable but less responsive to directional prompting.

Repository baseline:

```text
Natural
```

Move toward Creative only after voice fit, wording, and beat structure are already sound. Do not use Creative as the first fix for flat writing.

## 9. Generate, then diagnose correctly

**OFFICIAL-CURRENT:** ElevenLabs TTS is nondeterministic.

Use this diagnosis order:

```text
wrong fact/meaning
→ script defect

correct meaning but flat/dense structure
→ beat/writing defect

correct structure but target delivery is outside the base voice
→ voice-fit defect

one odd take with otherwise sound prompt
→ generation variance; review other available take / eligible regeneration before rewriting
```

Do not micro-edit a good prompt after every random weak take.

## 10. Lock approved evidence

When an actual generated result is approved, retain useful evidence:

```text
Voice ID / task
exact prompt actually used
voice
model = Eleven v3
Stability / visible settings
actual duration
approved pronunciation for material terms
what worked / what failed
actual audio evidence location when available
```

If the user edited the prompt before generation, the actually-generated prompt supersedes the assistant draft and must be synchronized into canonical `work/voice-production.md`.

# Minimal operator output

Internally resolve:

```text
Intent: <what this moment must achieve>
Target duration: <none / range / hard max / fixed-sync>
Voice fit: <good / risk / unknown>
Performance arc: <state → state → state>
Pronunciation risks: <terms>
```

User-facing result stays simple:

```text
## <VOICE-ID / TASK NAME>

<one prompt ready to paste into ElevenLabs>
```

Do not expose internal QA/state unless requested.

# Supporting pages

- `v3-performance-writing.md` — wording, beat architecture, punctuation, CAPS, line breaks, tags, stacking, reactions, long-form emotional movement.
- `v3-duration-planning.md` — target duration, word budgets, project calibration, Dynamic vs Fixed Duration.
- `v3-production-reference.md` — v3 status, voice fit, Stability, credits, generation variance, pronunciation, normalization, long-form continuity, UI/documentation caveats.
- `source-register.md` — evidence authority and source freshness.

# Stop rule

Do not add another prompting rule because it sounds plausible. New reusable rules require one of:

1. current official ElevenLabs evidence;
2. clearly labeled creator/community evidence that does not conflict with official guidance; or
3. approved project-calibrated audio evidence.
