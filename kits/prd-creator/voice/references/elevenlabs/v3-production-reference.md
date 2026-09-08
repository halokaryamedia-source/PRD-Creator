# Eleven v3 Production Reference

Last verified: **2026-09-08**

Purpose: store current Eleven v3 product facts that SoundMaker may need for generation-surface choice, voice choice/design, Stability, Speed, Enhance, continuity, long-form production, regeneration, pronunciation, and troubleshooting.

See `source-register.md` for evidence provenance. Multi-speaker details live in `v3-dialogue-generation.md`; naturalness craft lives in `v3-naturalness.md`.

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

Tag effectiveness and naturalness depend strongly on the chosen voice and its source/training behavior. A voice whose baseline cadence, projection, accent, or emotional range conflicts with the scene cannot be reliably repaired by direction stacking.

### Voice Performance Envelope

For production, assess only the range needed by the project/speaker:

```text
identity / timbre / persona
native baseline delivery
natural cadence / pacing
required emotion range
required projection range
language / dialect / accent compatibility
known drift or pronunciation risk
```

Use this to classify a voice internally as `GOOD FIT`, `LIMITED FIT`, `RISKY FIT`, or `UNKNOWN`.

### Native language / accent fit

Current ElevenLabs guidance states that text largely determines language while the selected voice strongly influences accent/pronunciation. Prefer a voice created/trained in the target language and desired accent when that distinction matters.

### PVC / compatibility caveat

Current ElevenLabs material contains changing caveats around Professional Voice Clone compatibility with v3. Under this repository's v3-only scope, treat any current compatibility limitation as a voice-fit risk requiring current product verification and actual output evidence rather than silently switching models.

## 4. Voice Design

Use Voice Design only when a suitable approved/library voice does not already cover the required performance envelope.

Current ElevenLabs Voice Design guidance recommends a structured audible description. A useful target shape is:

```text
Native <language / regional dialect when material>.
<gender / perceived age only when relevant and approved>. <quality level when useful>.
Persona: <2–5 useful descriptors>.
Emotion/baseline: <2–3 useful descriptors>.
<1–2 sentences about timbre, natural cadence, pacing, projection, and delivery>.
```

Important current guidance:

- specify language/dialect explicitly when drift matters;
- do not use `accent` when you really mean intonation/emphasis;
- avoid FX words such as reverb/echo/phone/tape when clean voice quality is the goal;
- use pacing language such as relaxed conversational cadence, deliberate measured pacing, or hurried cadence when that is truly part of the voice identity;
- keep baseline actor identity separate from per-line SoundMaker direction.

### Voice Design preview text

The preview text materially shapes how a designed voice demonstrates itself. Use text that matches the intended persona, emotion, pacing, and register.

For subtle tone/cadence work, current Voice Design guidance recommends enough context—a complete sentence or short paragraph—rather than an unrelated tiny phrase that can sound abrupt or inconsistent.

Do not promote preview wording into canonical project dialogue unless it is independently approved project content.

## 5. Stability

**OFFICIAL-CURRENT:** Stability is the major v3 setting.

- **Creative** — more emotional / expressive / variable, with greater risk of odd output;
- **Natural** — closest to reference voice behavior; balanced baseline;
- **Robust** — more stable but less responsive to directional prompting.

Repository baseline:

```text
Natural
```

Naturalness rule:

```text
stiff output
→ inspect voice fit + spoken wording + thought-group rhythm + context + over-direction first
→ then adjust Stability if the script/voice relationship is already sound
```

Do not treat Robust as a universal quality upgrade; its extra consistency can reduce expressive responsiveness and may reinforce a stiff result when the real problem is direction/writing.

Move toward Creative only after voice fit and prompt architecture are sound and greater expressive variance is actually useful.

## 6. Speed

Current official ElevenLabs documentation is not perfectly consistent across all pages/surfaces about historical v3 Speed availability. Current Best Practices and current Text to Speech product guidance describe Speed in Text to Speech/API with:

```text
baseline: 1.0
range described by current product guidance: 0.7–1.2
```

Repository policy is therefore **surface-aware**, not assumption-driven:

- when the active surface exposes Speed for the selected v3 workflow, keep `1.0` / unchanged as the natural baseline;
- use small adjustments only after wording/duration architecture is already correct;
- do not rely on Speed as a mandatory v3 mechanism;
- do not use extreme Speed values to rescue an oversized script; current ElevenLabs guidance warns extreme values can affect quality;
- when the active surface does not expose Speed, do not invent it.

## 7. Enhance

Current ElevenLabs Best Practices exposes Enhance behavior that can add context-appropriate Audio Tags plus CAPS, punctuation, ellipses, and other performance cues while preserving dialogue meaning.

This overlaps directly with SoundMaker's deliberate writing/directing layer.

Repository policy:

```text
plain / untreated text
→ Enhance may help create a draft

SoundMaker naturalness/performance-reviewed prompt
→ Enhance OFF by default
```

Any Enhance/UI rewrite of an already-reviewed prompt becomes a **new draft** and must be reviewed again before generation.

## 8. Text structure, context, and Audio Tags

**OFFICIAL-CURRENT:** v3 is materially influenced by natural speech patterns, emotional context, text structure, punctuation, capitalization, Audio Tags, and voice matching.

ElevenLabs documents that:

- standard punctuation provides natural speech rhythm;
- ellipses can add pauses/weight;
- capitalization increases emphasis;
- emotional context in text influences delivery;
- tag combinations are allowed;
- tag effectiveness is voice-dependent;
- tag vocabulary is non-exhaustive.

Repository interpretation:

```text
voice + natural spoken text + contextual flow
→ primary performance foundation

Audio Tags
→ optional local direction, not mandatory boilerplate
```

Detailed writing rules live in `v3-performance-writing.md` and `v3-naturalness.md`.

## 9. Audio Tag scope

Standard Speech Synthesis v3 supports moment-to-moment / mid-delivery direction. Text to Dialogue also accepts Audio Tags inside each turn's text.

**UNKNOWN:** no current standard-v3 documentation defines a fixed tag persistence window such as `exactly N words` or `until the next tag`.

Place direction close to the intended beat instead of depending on an invented persistence rule.

A zero-tag `performance` payload is valid when the selected voice, spoken wording, punctuation, and context already imply the required delivery.

## 10. Same-speaker continuity context

For API workflows that split one continuing same-speaker narration/performance into multiple TTS requests, the current Text to Speech API supports:

```text
previous_text
next_text
previous_request_ids
next_request_ids
```

Purpose: improve continuity/prosody across concatenated generations or help a regenerated middle segment connect to neighboring audio.

Current API details:

- `previous_text` / `next_text` supply surrounding text context;
- `previous_request_ids` / `next_request_ids` supply neighboring generated request IDs;
- up to three previous and three next request IDs are currently accepted;
- when both text and request IDs are supplied for the same side, request-ID context takes precedence according to current endpoint documentation;
- results are strongest when the same model is used across related generations.

Repository rule:

```text
connected narration split for implementation/editing
→ preserve canonical VO wording
→ add only relevant adjacent generation context
→ never pad the audible line with filler merely to give the model context
```

Do not use unrelated earlier/later project text as context.

## 11. Short-line naturalness

Short commands, acknowledgements, and reactions may legitimately be only a few words. Do not lengthen them automatically.

If a short line sounds detached because it belongs to a continuing same-speaker sequence, use previous/next generation context. If it is a response-dependent multi-speaker turn, use Text to Dialogue. If it is truly isolated, rely on voice fit + exact wording rather than invented filler.

## 12. Speech Synthesis vs ElevenCreative Studio

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

If a long standard TTS generation develops whispering, volume/tone drift, accent drift, distortion, or continuity loss, first inspect voice fit/settings and consider a current Studio/semantic-section workflow rather than extending one unstable generation.

## 13. Generation variance and candidate selection

**OFFICIAL-CURRENT:** ElevenLabs generation is nondeterministic.

For standard TTS, current product guidance allows same-content regenerations under product conditions. Text to Dialogue guidance explicitly notes that several generations may be required and recommends candidate selection.

Production implication:

```text
one isolated weak/glitched take
+ prompt/settings otherwise correct
→ compare available same-content take/regeneration first

same defect repeats at the same beat
→ prompt / context / Stability / voice-fit / surface diagnosis
```

API `seed` is a best-effort consistency aid; determinism is not guaranteed.

## 14. Troubleshooting map

| Symptom | Most relevant causes/actions |
|---|---|
| stiff / robotic but intelligible | voice mismatch; written/spec prose; uniform thought-group rhythm; contextless splitting; redundant tags; too-stable setting |
| flat but clean | strengthen spoken beat/emotional context first; one precise direction if needed; then consider Creative |
| overacted / synthetic | remove redundant tags/CAPS/ellipses; restore Natural baseline; inspect voice mismatch |
| chaotic / erratic | Stability too loose and/or over-direction |
| short connected line feels detached | add relevant previous/next context; do not add filler |
| whisper / volume drop / tone break | Stability or voice issue; long-form workflow may benefit from Studio/sectioning |
| accent drift | voice/language compatibility; long-form instability may contribute |
| repeated ignored emotional cue | voice-fit problem before adding more tags |
| isolated corruption/distortion | compare/regenerate same prompt before rewriting |
| multi-speaker interaction feels disconnected | route same-Moment dependent turns through Text to Dialogue |
| pronunciation error | spoken normalization / IPA / dictionary |
| duration miss | word budget / script architecture first; then small supported Speed adjustment if appropriate |

Do not diagnose from waveform screenshots alone; heard audio is the evidence.

## 15. Pronunciation

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

## 16. Language / accent

Text strongly determines language, while the selected voice strongly influences accent/pronunciation. Prefer a voice compatible with the target language/accent.

Current Dialogue API may accept `language_code`; use it only when it improves a real language/normalization need and the selected model supports it.

If live product controls differ from older help text, current UI/API owns control availability while current official language/accent principles remain the semantic reference.

## 17. Text normalization

For production-critical numbers, dates, symbols, and acronyms, explicit spoken wording is safer than depending on normalization to infer intent.

Current Dialogue API also exposes text-normalization control. Treat it as generation configuration, not a substitute for production-ready wording.

## 18. Timing

Normal v3 TTS/Dialogue duration is dynamic; text alone does not guarantee an exact second count.

Use `v3-duration-planning.md` whenever timing matters. Use Dialogue `with-timestamps` only when generated synchronization evidence is actually useful.

If Speed is available, leave it unchanged while sizing the script; use it only as a secondary bounded adjustment after natural wording/timing architecture is sound.

## 19. Output format

Encoding quality does not fix acting quality. MP3 is adequate for review/general delivery. Prefer a less-compressed source when downstream editing requires it and the current ElevenLabs surface exposes one.

## 20. Voice vs SFX

Keep doors, machinery, impacts, ambience, explosions, wind, and other environmental effects in the separate non-Voice Sound Effects lane: `production-assets/SOUND-EFFECTS.md`.

Even when v3 Dialogue documentation demonstrates audio-event tags, SoundMaker's default remains voice-performance control only. Do not merge canonical SFX requirements into Voice prompts.

## 21. Non-rules

Do not hard-code these without actual evidence:

- every Voice prompt must begin with an Audio Tag;
- one Audio Tag lasts exactly N words;
- triple tags are inherently better than doubles;
- contractions/filler always make speech more human;
- one universal WPM fits every voice/performance;
- one bad take proves the prompt is bad;
- Enhance always improves a directed prompt;
- Speed should be changed whenever duration misses;
- Speech Synthesis guarantees exact duration;
- a voice can be forced outside its natural performance envelope by adding enough tags;
- every adjacent pair of speakers should be generated with Text to Dialogue;
- legacy Voiceover Studio controls define current ElevenCreative Studio behavior.