# Eleven v3 Production Reference

Last verified: 2026-09-08

Purpose: store current Eleven v3 product facts that SoundMaker may need for generation-surface choice, voice choice, Stability, Enhance, long-form production, regeneration, pronunciation, and troubleshooting.

See `source-register.md` for evidence provenance. Multi-speaker details live in `v3-dialogue-generation.md`.

## 1. Model scope

Operational scope in this repository:

```text
Eleven v3 only
```

Current ElevenLabs documentation positions v3 as its emotionally rich / expressive TTS model with 70+ languages and a 5,000-character standard TTS input limit.

Do not use this reference to auto-fallback to another model family.

## 2. Generation surface routing

Choose the surface from the communication shape instead of using one surface for every Voice ID:

```text
independent single-speaker line
→ Text to Speech / Speech Synthesis

same approved Moment
+ multiple speakers
+ conversational response dependency
→ Text to Dialogue

long-form editorial production / timeline work
→ current ElevenCreative Studio when useful
```

Text to Dialogue is a generation surface, not a new canonical identity. Preserve existing `VO-...` entries and derive ordered Dialogue inputs only at generation time.

Use `v3-dialogue-generation.md` for current request limits, candidate selection, timestamps, and evidence details.

## 3. Voice selection

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

## 4. Stability

**OFFICIAL-CURRENT:** Stability is the major v3 setting.

- **Creative** — more expressive / more variable / greater risk of odd output;
- **Natural** — balanced and closest to reference voice behavior;
- **Robust** — more stable but less responsive to directional prompting.

Repository baseline:

```text
Natural
```

Move toward Creative only after voice fit and prompt architecture are already sound. Use Robust when consistency is actually more important than directional responsiveness.

## 5. Speed

Current v3-specific Text to Speech product guidance states the Speed setting is **not available for standard Eleven v3 Text to Speech**.

Current ElevenCreative Studio can expose its own production speed control. Treat that as a Studio editing control, not as evidence that standard v3 Speech Synthesis has a Speed slider.

Rule:

- do not make Speed a required SoundMaker v3 TTS mechanism;
- use word budget, spoken architecture, punctuation, and local pacing direction first;
- if the active Studio/live surface exposes a control, treat that live surface as current for that production without generalizing it into standard TTS policy.

## 6. Enhance

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

## 7. Speech Synthesis vs ElevenCreative Studio

Normal isolated line / manageable narration production uses **Text to Speech / Speech Synthesis**.

Current ElevenCreative Studio is the long-form/editorial production environment with paragraph/selection regeneration, generation history, locking, timeline/caption support, and separate SFX/music tracks.

The former Voiceover Studio product was sunset on **2026-05-15**. Do not route new work to the deprecated Voiceover Studio as if its legacy controls were the current canonical production surface.

Repository routing:

```text
normal independent v3 line
→ Speech Synthesis

same-Moment conversational multi-speaker exchange
→ Text to Dialogue

long-form / editorial timeline / repeated section-level refinement
→ ElevenCreative Studio when useful
```

If a long standard TTS generation develops whispering, volume/tone drift, accent drift, or distortion, first inspect voice fit/settings and consider a current Studio/sectioned workflow rather than extending one unstable generation.

## 8. Text structure and Audio Tags

**OFFICIAL-CURRENT:** v3 is materially influenced by natural speech patterns, emotional context, text structure, punctuation, capitalization, Audio Tags, and voice matching.

ElevenLabs documents that:

- ellipses add pauses/weight;
- capitalization increases emphasis;
- standard punctuation provides natural rhythm;
- tag combinations are allowed;
- tag effectiveness is voice-dependent;
- the tag vocabulary is non-exhaustive.

Detailed writing rules live in `v3-performance-writing.md`.

## 9. Audio Tag scope

Standard Speech Synthesis v3 supports moment-to-moment / mid-delivery direction. Text to Dialogue also accepts Audio Tags inside each turn's text.

**UNKNOWN:** no current standard-v3 documentation defines a fixed tag persistence window such as "exactly N words" or "until the next tag".

Place direction close to the intended beat instead of depending on an invented persistence rule.

## 10. Generation variance and candidate selection

**OFFICIAL-CURRENT:** ElevenLabs generation is nondeterministic.

For standard TTS, current guidance allows up to two free same-content regenerations under product conditions. Text to Dialogue guidance explicitly notes that several generations may be required and recommends candidate selection.

Production implication:

```text
one isolated weak/glitched take
+ prompt/settings otherwise correct
→ compare available same-content take/regeneration first

same defect repeats at the same beat
→ prompt / Stability / voice-fit / surface diagnosis
```

API `seed` is a best-effort consistency aid; determinism is not guaranteed.

## 11. Troubleshooting map

| Symptom | Most relevant causes/actions |
|---|---|
| flat but clean | spoken architecture / direction first; then consider lower Stability toward Creative |
| chaotic / overacted | Stability too loose and/or over-direction |
| whisper / volume drop / tone break | Stability or voice issue; long-form workflow may benefit from Studio/sectioning |
| accent drift | voice/language compatibility; long-form instability may contribute |
| repeated ignored emotional cue | voice-fit problem before adding more tags |
| isolated corruption/distortion | compare/regenerate same prompt before rewriting |
| multi-speaker interaction feels disconnected | route same-Moment dependent turns through Text to Dialogue |
| pronunciation error | spoken normalization / IPA / dictionary |
| duration miss | word budget / script architecture, then current production surface controls if needed |

Do not diagnose from waveform screenshots alone; heard audio is the evidence.

## 12. Long-form continuity

For API workflows that must split standard TTS content, ElevenLabs supports context mechanisms such as `previous_text`, `next_text`, and related request-context fields to improve continuity/prosody across chunks.

For manual/Studio production, split only at semantic boundaries such as scene, paragraph, or major emotional transitions. Do not cut inside one important performance beat merely for equal chunk sizes.

For conversational multi-speaker content, use Text to Dialogue when the turn-to-turn interaction is itself the continuity problem.

## 13. Pronunciation

Use the smallest control that solves the risk:

```text
ambiguous number / date / symbol / acronym
→ explicit spoken form

isolated unusual proper noun
→ native v3 IPA when needed

repeated project terminology
→ project pronunciation note / dictionary when appropriate
```

Current ElevenLabs guidance supports native v3 IPA but does not make pronunciation perfectly deterministic. Different voices can still interpret controls differently.

Approve pronunciation only after actual evidence exists.

## 14. Language / accent

Text strongly determines language, while the selected voice strongly influences accent/pronunciation. Prefer a voice compatible with the target language/accent.

Current Dialogue API may accept `language_code`; use it only when it improves a real language/normalization need and the selected model supports it.

If live product controls differ from older help text, current UI/API owns control availability while current official language/accent principles remain the semantic reference.

## 15. Text normalization

For production-critical numbers, dates, symbols, and acronyms, explicit spoken wording is safer than depending on normalization to infer intent.

Current Dialogue API also exposes text-normalization control. Treat it as generation configuration, not a substitute for production-ready wording.

## 16. Timing

Normal v3 TTS/Dialogue duration is dynamic; text alone does not guarantee an exact second count.

Use `v3-duration-planning.md` whenever timing matters. Use Dialogue `with-timestamps` only when generated synchronization evidence is actually useful.

## 17. Output format

Encoding quality does not fix acting quality. MP3 44.1 kHz / 128 kbps is adequate for review/general delivery. Prefer a less-compressed source when downstream editing requires it and the current ElevenLabs surface exposes one.

## 18. Voice vs SFX

Keep doors, machinery, impacts, ambience, explosions, wind, and other environmental effects in the separate non-Voice Sound Effects lane: `production-assets/SOUND-EFFECTS.md`.

Even when v3 Dialogue documentation demonstrates audio-event tags, SoundMaker's default remains voice-performance control only. Do not merge canonical SFX requirements into Voice prompts.

## 19. Non-rules

Do not hard-code these without actual evidence:

- one Audio Tag lasts exactly N words;
- triple tags are inherently better than doubles;
- one universal WPM fits every voice/performance;
- one bad take proves the prompt is bad;
- Enhance always improves a directed prompt;
- Speech Synthesis guarantees exact duration;
- a voice can be forced outside its natural performance envelope by adding enough tags;
- every adjacent pair of speakers should be generated with Text to Dialogue;
- legacy Voiceover Studio controls define current ElevenCreative Studio behavior.
