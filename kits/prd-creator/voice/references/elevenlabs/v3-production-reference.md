# Eleven v3 Production Reference

Last verified: 2026-08-13

Purpose: store current Eleven v3 product facts that SoundMaker may need for voice choice, Stability, Enhance, long-form surface selection, regeneration, pronunciation, and troubleshooting.

See `source-register.md` for evidence provenance.

## 1. Model scope

Operational scope in this repository:

```text
Eleven v3 only
```

Current ElevenLabs documentation positions v3 as its emotionally rich / expressive TTS model with 70+ languages and a 5,000-character model input limit.

Do not use this reference to auto-fallback to another model family.

## 2. Voice selection

**OFFICIAL-CURRENT:** ElevenLabs identifies voice choice as the most important v3 parameter.

Tag effectiveness depends strongly on the chosen voice and its source/training behavior. A voice that is naturally restrained, meditative, or quiet is not guaranteed to become a convincing frantic/shouting actor because of tags.

### Voice Performance Envelope

For production, assess only the range needed by the line:

```text
identity / timbre / persona
native baseline delivery
required emotion range
required projection range
required pacing range
language / accent compatibility
known drift or pronunciation risk
```

Use this to classify a voice internally as `GOOD FIT`, `LIMITED FIT`, `RISKY FIT`, or `UNKNOWN`.

### PVC / compatibility caveat

Current ElevenLabs material can warn that some Professional Voice Clone behavior is not fully optimized for v3. Under this repository's v3-only scope, treat that as a compatibility risk requiring actual output evidence rather than silently switching models.

### Voice Design

Voice Design can be considered when no existing voice has the required identity/performance range. Do not redesign a voice merely because one nondeterministic take was weak.

## 3. Stability

**OFFICIAL-CURRENT:** Stability is the major v3 setting.

- **Creative** — more expressive / more variable / greater risk of odd output;
- **Natural** — balanced and closest to reference voice behavior;
- **Robust** — more stable but less responsive to directional prompting.

Repository baseline:

```text
Natural
```

Move toward Creative only after voice fit and prompt architecture are already sound. Use Robust when consistency is actually more important than directional responsiveness.

## 4. Speed

Current v3-specific Text to Speech product guidance states the Speed setting is **not available for Eleven v3**. Some broader ElevenLabs pages describe Speed as a general TTS control, so v3-specific guidance takes precedence for this workflow.

Rule:

- do not make a Speed slider part of SoundMaker's required v3 path;
- use word budget, spoken architecture, punctuation, and local pacing direction first;
- if the live UI exposes a control that current v3-specific docs do not describe, treat the live UI as the current surface and re-verify before turning it into repository policy.

## 5. Enhance

Current ElevenLabs Best Practices exposes Enhance behavior that can add context-appropriate Audio Tags plus CAPS, question/exclamation marks, ellipses, and other vocal-performance cues while preserving dialogue meaning.

This overlaps directly with SoundMaker's deliberate directing layer.

Repository policy:

```text
plain / untreated text
→ Enhance may help create a draft

SoundMaker-directed prompt
→ Enhance OFF by default
```

Any Enhance/UI rewrite of an already-directed prompt becomes a **new draft** and must be reviewed again before generation.

## 6. Speech Synthesis vs Studio

Normal one-line / manageable narration production uses **Speech Synthesis / Text to Speech**.

ElevenLabs troubleshooting recommends **Studio** for longer text when the voice begins to whisper unexpectedly, lose volume, change accent/tone, or break/distort; Studio is less prone to these issues and allows paragraph-level regeneration.

Repository routing:

```text
normal v3 line / stable narration
→ Speech Synthesis

long-form + continuity/drift/whisper/accent/tone problem
→ Studio using Eleven v3
```

Do not treat Studio as a different model. Do not move to Studio merely because a line crosses an arbitrary character count if Speech Synthesis is already stable.

## 7. Text structure and Audio Tags

**OFFICIAL-CURRENT:** v3 is materially influenced by natural speech patterns, emotional context, text structure, punctuation, capitalization, Audio Tags, and voice matching.

ElevenLabs documents that:

- ellipses add pauses/weight;
- capitalization increases emphasis;
- standard punctuation provides natural rhythm;
- tag combinations are allowed;
- tag effectiveness is voice-dependent;
- the tag vocabulary is non-exhaustive.

Detailed writing rules live in `v3-performance-writing.md`.

## 8. Audio Tag scope

Standard Speech Synthesis v3 supports moment-to-moment / mid-delivery direction.

**UNKNOWN:** no current standard-v3 documentation defines a fixed tag persistence window such as "exactly N words" or "until the next tag".

Place direction close to the intended beat instead of depending on an invented persistence rule.

## 9. Generation variance and regeneration

**OFFICIAL-CURRENT:** ElevenLabs TTS is nondeterministic.

For identical text/settings, current ElevenLabs guidance allows up to two free regenerations per piece of content, subject to the current product conditions. Changing text or settings creates a new paid generation.

Production implication:

```text
one isolated weak/glitched take
+ prompt/settings otherwise correct
→ review another available take / eligible same-prompt regeneration first
```

Repeated failure at the same point is stronger evidence of a prompt, Stability, or voice-fit problem.

API `seed` is a best-effort consistency aid; determinism is not guaranteed.

## 10. Troubleshooting map

| Symptom | Most relevant causes/actions |
|---|---|
| flat but clean | spoken architecture / direction first; then consider lower Stability toward Creative |
| chaotic / overacted | Stability too loose and/or over-direction |
| whisper / volume drop / tone break | Stability or voice issue; long-form instability may justify Studio |
| accent drift | voice/language compatibility; long-form instability may contribute |
| repeated ignored emotional cue | voice-fit problem before adding more tags |
| isolated corruption/distortion | regenerate same prompt before rewriting |
| pronunciation error | spoken normalization / IPA / dictionary |
| duration miss | word budget / script architecture |

Do not diagnose from waveform screenshots alone; heard audio is the evidence.

## 11. Long-form continuity

For API workflows that must split content, ElevenLabs supports context mechanisms such as `previous_text`, `next_text`, and related request-context fields to improve continuity/prosody across chunks.

For manual web production, split only at semantic boundaries such as scene, paragraph, or major emotional transitions. Do not cut inside one important performance beat merely for equal chunk sizes.

## 12. Pronunciation

Use the smallest control that solves the risk:

```text
ambiguous number / date / symbol / acronym
→ explicit spoken form

isolated unusual proper noun
→ native v3 IPA when needed

repeated project terminology
→ project pronunciation note / dictionary when appropriate
```

Current ElevenLabs Best Practices reports native v3 IPA at roughly 80–90% consistency, not guaranteed 100%. Different voices can still interpret pronunciation controls differently.

Approve pronunciation only after actual evidence exists.

## 13. Language / accent

Text strongly determines language, while the selected voice strongly influences accent/pronunciation. Prefer a voice compatible with the target language/accent.

If the live product surface exposes a Language Override, treat that live control as the current UI behavior; do not invent a setting not present in the operator's current surface.

## 14. Text normalization

For production-critical numbers, dates, symbols, and acronyms, explicit spoken wording is safer than depending on normalization to infer intent.

## 15. Duration

Normal v3 TTS duration is dynamic; text alone does not guarantee an exact second count.

Use `v3-duration-planning.md` whenever timing matters.

## 16. Output format

Encoding quality does not fix acting quality. MP3 44.1 kHz / 128 kbps is adequate for review/general delivery. Prefer a less-compressed source when downstream editing requires it and the current ElevenLabs surface exposes one.

## 17. Voice vs SFX

Keep doors, machinery, impacts, ambience, explosions, wind, and other environmental effects in the separate Sound Effects lane. Even when v3 recognizes some non-speech tags, SoundMaker's default is voice-performance control only.

## 18. Non-rules

Do not hard-code these without actual evidence:

- one Audio Tag lasts exactly N words;
- triple tags are inherently better than doubles;
- one universal WPM fits every voice/performance;
- one bad take proves the prompt is bad;
- Enhance always improves a directed prompt;
- Speech Synthesis guarantees exact duration;
- a voice can be forced outside its natural performance envelope by adding enough tags.
