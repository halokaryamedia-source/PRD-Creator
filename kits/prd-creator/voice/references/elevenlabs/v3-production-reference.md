# Eleven v3 Production Reference

Last verified: **2026-09-08**

Purpose: current Eleven v3 product facts for voice choice/design, expression direction, Stability, Speed, Enhance, continuity, generation surfaces, regeneration, pronunciation, and troubleshooting.

See `source-register.md` for provenance, `v3-expression-direction.md` for acting coverage, `v3-naturalness.md` for stiffness/narration, and `v3-dialogue-generation.md` for multi-speaker generation.

## 1. Model scope

```text
Eleven v3 only
```

Current ElevenLabs documentation positions v3 as its expressive TTS model with 70+ languages and inline Audio Tag control.

## 2. Generation routing

```text
independent single-speaker line
→ Text to Speech

connected same-speaker narration split across requests
→ TTS + previous/next context

same Moment + multiple speakers + response dependency
→ Text to Dialogue

long-form editorial/timeline production
→ ElevenCreative Studio when useful
```

Generation routing does not create new canonical identities.

## 3. Voice selection

**OFFICIAL-CURRENT:** voice choice is the most important v3 parameter.

Tag effectiveness depends on the selected voice and its training/reference behavior. Choose a voice whose baseline is compatible with the required performance envelope:

```text
identity / timbre / persona
baseline energy
natural cadence / pacing
emotional range
projection range
language / dialect / accent compatibility
pronunciation / drift risk
```

Classify internally: `GOOD FIT | LIMITED FIT | RISKY FIT | UNKNOWN`.

Do not force a voice far outside this envelope through larger tag stacks.

### PVC caveat

Current ElevenLabs material still carries changing caveats around some Professional Voice Clone behavior with v3. Treat current compatibility limits as voice-fit risk requiring current verification and actual output evidence.

## 4. Voice Design

Use Voice Design when no suitable approved/library voice covers the required envelope.

Describe deliberately:

```text
language / regional dialect when material
perceived identity only when approved/relevant
persona
baseline emotion / energy
vocal timbre
natural cadence / pacing
projection / delivery
```

Preview with text matching the intended speaker/register and enough context to demonstrate cadence. Do not turn preview text into project dialogue unless independently approved.

## 5. Stability

**OFFICIAL-CURRENT:** Stability is the major v3 generation setting.

- **Creative** — more emotional/expressive and variable; greater odd-output risk;
- **Natural** — closest to reference voice behavior; balanced baseline;
- **Robust** — more stable but less responsive to directional prompts.

Repository baseline:

```text
Natural
```

Current ElevenLabs guidance recommends Creative or Natural for maximum expressiveness with Audio Tags; Robust reduces responsiveness to directional prompts.

For expression-critical work, do not move to Robust merely to make output more consistent if doing so weakens required acting.

## 6. Speed

Speed availability can differ by current surface. When exposed:

```text
baseline: 1.0 / unchanged
```

Use bounded adjustment only after wording/timing architecture is sound. Do not use Speed to rescue an oversized script or replace explicit pacing direction.

Eleven v3 can also receive pacing direction through Audio Tags such as `[rushed]`, `[slowly]`, or `[drawn out]` when the pacing itself is part of the performance.

## 7. Audio Tags — product role

**OFFICIAL-CURRENT:** Eleven v3 uses Audio Tags for emotional control and vocal delivery. Current official guidance demonstrates:

- emotion and attitude;
- whisper/shout/projection;
- human reactions;
- pacing/rhythm;
- accent/character candidates;
- moment-to-moment state changes;
- multi-speaker interaction cues.

Tags are bracketed natural-language instructions and are not a closed enum.

Repository interpretation:

```text
voice + spoken text + context
→ natural performance foundation

Audio Tags
→ explicit acting direction
```

Audio Tags are not mandatory syntax, but **material acting intent must not be left under-directed**.

Detailed policy: `v3-expression-direction.md`.

## 8. Expression Coverage

Use explicit direction when a material performance state is not sufficiently specified by voice + text + punctuation + immediate context.

Material dimensions include:

```text
emotion
attitude / subtext
projection
pace / rhythm
intensity / energy
cognitive state
reaction
state transition
landing
```

Opening state matters → anchor at opening.  
State changes → place new direction near the transition.  
Reaction happens → place reaction tag at the event.

Zero tags remains valid only when there is no material acting requirement beyond the natural baseline.

## 9. Tag scope / persistence

Standard v3 supports mid-delivery direction.

**UNKNOWN:** current standard-v3 documentation does not define one fixed persistence window such as `exactly N words` or `until next tag`.

Place tags near affected beats. Re-anchor when a material state changes or a new generation request needs a specific opening state.

## 10. Tag combinations

Current ElevenLabs guidance allows multiple tags.

Repository heuristic:

```text
1 tag               → preferred when sufficient
2 simultaneous tags → compatible different dimensions
3+                  → exceptional / calibrated / concrete need
```

Do not stack synonyms or rely on tag quantity as a quality metric.

## 11. Enhance

Current ElevenLabs Enhance uses an LLM to add contextually appropriate Audio Tags and emphasis while preserving dialogue meaning.

SoundMaker-reviewed prompts keep Enhance **OFF by default** because SoundMaker already performs speechification + Expression Coverage. Any Enhance rewrite becomes a new draft requiring review.

The official Enhance prompt reinforces useful principles adopted here:

- analyze mood/context for each line;
- select tags that genuinely enhance emotion/subtext;
- place tags strategically near affected dialogue;
- use auditory directions only;
- do not contradict or alter meaning.

## 12. Same-speaker continuity

Current TTS APIs support:

```text
previous_text
next_text
previous_request_ids
next_request_ids
```

Use relevant adjacent context to improve prosody across split narration.

Important distinction:

```text
context
→ helps continuity

Audio Tag state anchor
→ explicitly establishes required acting
```

Treat each new request as a possible acting reset. If a new clip must reliably continue a material state, re-anchor that state at the clip opening when necessary.

Do not add audible filler just to create context.

## 13. Short-line behavior

Keep legitimate short commands/reactions short.

- continuing same-speaker line → use adjacent context;
- response-dependent turn → use Text to Dialogue;
- expression-critical short line → use explicit acting direction if needed;
- truly baseline isolated line → voice fit + wording may be enough.

## 14. Text structure and punctuation

Current v3 guidance says punctuation, capitalization, and text structure materially influence delivery.

- ellipses can add pause/weight;
- capitalization increases emphasis;
- standard punctuation provides natural rhythm.

These controls complement Audio Tags; they do not replace expression-critical direction.

Eleven v3 does not support SSML `<break>` tags. Use punctuation, text structure, or appropriate Audio Tags for pacing/pauses.

## 15. Text to Dialogue

Each turn has its own `voice_id` and text. Put Audio Tags inside the turn they should affect.

Text to Dialogue is preferred when turn-to-turn reaction, interruption, overlap, or conversational timing materially affects delivery.

Do not create a duplicate Dialogue schema; keep existing ordered `VO-...` prompts canonical.

## 16. ElevenCreative Studio

Use current Studio for long-form/editorial workflows where paragraph/selection regeneration, generation history, locking, captions, or timeline assembly materially helps.

Do not route new work to deprecated Voiceover Studio assumptions.

## 17. Generation variance / candidate selection

Eleven v3 generation is nondeterministic.

```text
one weak/glitched take
+ prompt/settings otherwise correct
→ compare same-content candidate/regeneration first

same expression defect repeats at same beat
→ inspect Expression Coverage / tag placement / voice fit / Stability / surface
```

Seed is a best-effort consistency aid, not guaranteed determinism.

## 18. Troubleshooting

| Symptom | First diagnosis |
|---|---|
| stiff/robotic | written prose, uniform rhythm, voice mismatch, contextless splitting, over-direction |
| natural but flat | missing Expression Coverage / acting direction |
| emotion wrong or ambiguous | tag choice/placement + approved expression intent |
| transition missing | transition direction too late/absent |
| overacted/synthetic | redundant tags, excessive state changes, CAPS/punctuation overload, loose Stability |
| tag ignored repeatedly | voice fit before more tags |
| tag spoken aloud | confirm v3 + voice compatibility; simplify direction |
| short connected clip detached | adjacent context + opening state re-anchor when needed |
| conversation disconnected | Text to Dialogue |
| accent/tone drift | voice/language fit, Stability, long-form structure |
| pronunciation error | spoken normalization / IPA / dictionary |
| duration miss | word budget first, then bounded pacing/Speed controls |

Heard audio is required to prove generated quality.

## 19. Pronunciation

```text
ambiguous number/date/symbol/acronym
→ explicit spoken form

unusual proper noun
→ native v3 IPA when needed

repeated project term
→ pronunciation dictionary/note when useful
```

Current native v3 IPA is useful but not perfectly deterministic.

## 20. Language / accent

Text strongly influences language; selected voice strongly affects accent/pronunciation. Prefer a compatible voice.

Accent/character Audio Tags may be used only when the identity shift itself is approved and voice-compatible. Do not use them to invent a character property downstream.

## 21. Timing / output

Text does not guarantee exact duration. Use `v3-duration-planning.md` when timing matters and timestamps when generated synchronization evidence is useful.

Encoding quality does not fix acting quality. Use output formats appropriate to review/downstream editing.

## 22. Voice vs SFX

Keep environmental SFX in `production-assets/SOUND-EFFECTS.md`. Even though Eleven v3 can emit audio-event tags, SoundMaker Voice prompts should not absorb canonical non-dialogue asset requirements.

## 23. Non-rules

Do not hard-code:

- every prompt must begin with a tag;
- zero tags is inherently more natural;
- fewer tags is inherently better;
- more tags is inherently more expressive;
- one tag has a fixed documented persistence window;
- Robust is always higher quality;
- filler/hesitation always sounds human;
- one bad take proves the prompt is wrong;
- Enhance always improves a reviewed prompt;
- voice mismatch can be fixed by enough tags.
