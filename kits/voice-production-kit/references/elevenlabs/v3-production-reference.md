# Eleven v3 Production Reference

Last verified: 2026-08-13

This page records current operational facts that affect real ElevenLabs output. See `source-register.md` for URLs and evidence authority.

## 1. Current model status

**OFFICIAL-CURRENT:** Eleven v3 became Generally Available on 2026-02-02. Some older ElevenLabs pages, URLs, and blog copy still contain the word `Alpha`; do not treat the legacy label itself as current product status.

Current positioning:

| Need | Prefer |
|---|---|
| Rich emotional movement / dramatic performance / Audio Tags | **Eleven v3** |
| Stable long-form / highly consistent natural output | **Eleven Multilingual v2** |
| Low-latency real-time generation | Flash family |

Current model docs list:

- Eleven v3: 70+ languages, 5,000-character model limit, high emotional range and contextual understanding;
- Multilingual v2: 29 languages, 10,000-character model limit, most stable on long-form generations.

For the web Speech Synthesis page, paid plans currently allow up to 5,000 characters per generation; free plans up to 2,500.

## 2. Credits / usage

**OFFICIAL-CURRENT:** website Text to Speech consumes **1 credit per written input character**. Current ElevenLabs documentation also states Eleven v3 costs 1 credit per character on the website. Some shared Voice Library voices can apply a credit multiplier.

Do not describe this as LLM tokens. For TTS, plan usage in characters/credits.

Prompt directing text also contributes characters because it is part of the TTS input; there is no documented special surcharge for Audio Tags.

## 3. Voice selection is the first production decision

**OFFICIAL-CURRENT:** ElevenLabs calls voice choice the most important parameter for v3. Model choice follows it.

The base voice must already be reasonably compatible with the requested delivery. A meditative/reassuring source is not guaranteed to become a convincing frantic shouter because of a tag.

For v3:

- expressive IVC source recordings should contain broader emotional range when broad acting range is required;
- neutral voices tend to be more stable;
- targeted niche voices can be useful when one performance family dominates.

### PVC caveat

Current ElevenLabs documentation still warns that Professional Voice Clones are not fully optimized/supported in v3 in the same way as earlier models, while the actual product UI may allow some PVC selections and show a compatibility warning.

Treat this as a **voice/model compatibility risk**, not an absolute ban:

```text
voice similarity / identity is priority
→ compare Multilingual v2

expressive v3 performance is priority
→ use a v3-compatible voice/design/IVC or accept/test the PVC risk
```

Do not silently declare a PVC-v3 pairing production-safe without actual evidence.

### Voice Design

Current ElevenLabs help material describes Voice Design v3 voices as compatible with Eleven v3 and Audio Tags, while Voice Design remains experimental. Use Voice Design when an existing library voice cannot provide the required character/performance range; do not redesign a voice merely because one take was weak.

## 4. Stability

**OFFICIAL-CURRENT:** Stability is the most important v3 setting.

- **Creative** — more emotional/expressive; more variable and more prone to odd output/hallucination.
- **Natural** — balanced; closest to the reference recording.
- **Robust** — more stable/consistent; less responsive to directional prompts.

Default production baseline for this repository:

```text
Natural
```

Move toward Creative only when:

- the base voice fits the task;
- spoken wording/beat structure are already good;
- more expressive range is genuinely required.

Do not move to Creative as the first fix for a structurally flat script.

## 5. Speed

Official ElevenLabs documentation currently conflicts on Speed availability for v3. One current product-guide section says v3 has no Speed setting, while another current FAQ says Speed 0.7–1.2 is available to all models.

Status here: **UNKNOWN / UI-DEPENDENT**.

The current web UI is the authority for control availability during actual production. Do not hard-code Speed into SoundMaker/Voice Production behavior until the product behavior is observed and stable.

## 6. Text structure, punctuation, and tags

**OFFICIAL-CURRENT:** v3 output is materially influenced by:

- natural speech patterns;
- clear emotional context;
- text structure;
- punctuation;
- capitalization;
- Audio Tags;
- voice matching.

ElevenLabs specifically states:

- ellipses add pauses and weight;
- capitalization increases emphasis;
- standard punctuation provides natural rhythm;
- multiple Audio Tags may be combined;
- some experimental tags vary across voices.

Do not assume tag stacking has a monotonic quality benefit.

Detailed production rules: `v3-performance-writing.md`.

## 7. Audio Tag scope

Standard Speech Synthesis v3 supports moment-to-moment/mid-delivery direction.

**UNKNOWN:** there is no documented fixed persistence window for standard v3 TTS tags.

The separate v3 Conversational/Agents Expressive Mode documents approximately 4–5 words for its tags. That product-specific number must not be copied into normal Speech Synthesis rules.

## 8. Generation variance and regeneration

**OFFICIAL-CURRENT:** ElevenLabs TTS is nondeterministic. Same voice/model/settings/text can produce different takes.

API has a `seed` parameter that makes a best effort toward repeatable sampling; determinism is not guaranteed.

For web v3, current account/help documentation says each paid `Generate` click can return two v3 alternatives while charging for one generation. General free-regeneration behavior varies by product/model/UI state; the actual `Generate` vs `Regenerate` label is the production authority for whether another click costs credits.

Production rule:

```text
one weak/odd take + otherwise sound prompt
→ review the alternative / eligible regeneration first

same failure repeatedly at the same semantic/performance point
→ diagnose prompt/voice/settings
```

Do not micro-edit a good prompt after every random weak take.

## 9. Long-form generation and continuity

Current v3 model limit: 5,000 characters per API request. For content beyond a few thousand characters on the website, ElevenLabs recommends Studio.

If API generation must be split, ElevenLabs supports:

- `previous_text` / `next_text`;
- `previous_request_ids` / `next_request_ids`;

for improved continuity/prosody between chunks and during regeneration of a middle section.

For web/manual production, prefer semantic boundaries:

```text
scene boundary
paragraph boundary
major emotional transition
```

Do not split inside one important emotional beat merely to create symmetrical chunks.

## 10. Pronunciation

For production-critical terms:

1. write numbers/dates/acronyms/symbols in the way they should be spoken when ambiguity matters;
2. use project pronunciation notes for fantasy/proper nouns;
3. use native v3 IPA or pronunciation dictionaries when needed;
4. approve pronunciation only after actual audio evidence exists.

Current ElevenLabs documentation says pronunciation dictionary phoneme tags support `eleven_v3` (and `eleven_flash_v2`) and that v3 can use IPA/CMU in languages beyond English.

Project terms should be locked once approved rather than re-guessed line by line.

## 11. Language and accent

Current ElevenLabs guidance:

- the text determines the language;
- the chosen voice strongly influences accent/pronunciation;
- voices trained in the target language/accent generally perform more naturally.

Current web/help documentation and the observed product UI may not always expose the same language controls. If the live UI offers a Language Override, treat that UI as the current control surface; do not infer behavior from an older help page.

## 12. Text normalization

Website TTS currently enables normalization by default. API supports `apply_text_normalization = auto | on | off`.

For predictable final VO, prefer explicit spoken forms for material numbers, dates, symbols, and acronyms instead of depending on the normalizer to guess the intended reading.

## 13. Duration

Normal TTS duration is dynamic. Exact duration is not guaranteed from text alone.

Voiceover Studio offers Fixed Duration, but can sound unnaturally fast/slow if forced too far from the natural length.

Use `v3-duration-planning.md` when timing is specified.

## 14. Output format

MP3 44.1 kHz / 128 kbps is sufficient for review/general delivery and does not explain a flat acting performance.

When downstream audio editing is expected and the account/product exposes a suitable WAV/PCM option, prefer a lossless/less-compressed source for post-production. Do not confuse codec quality with acting quality.

## 15. Voice vs sound effects boundary

This reference is for **voice performance**. Keep environment/SFX such as doors, machinery, impacts, wind, explosions, and ambience in the Sound Effects production lane rather than relying on TTS tags as the default SFX generator.

V3 may recognize some experimental non-speech tags, but that is not the Voice Production default because it reduces control over separate game assets.

## 16. What is explicitly not a reusable rule

Do not hard-code any of these without project evidence:

- one Audio Tag lasts exactly N words in standard Speech Synthesis;
- one tag lasts until the next tag;
- triple tags are inherently better than double tags;
- there is an ideal number of tags per 10 seconds;
- one universal WPM describes every v3 voice/performance;
- Creative always makes the audio faster or slower;
- Enhance always improves an already-directed prompt;
- one bad take proves the prompt is bad;
- Speech Synthesis can guarantee exact duration from text alone.

## 17. Project calibration

The strongest reusable evidence for a specific production is an approved result from the same project/voice/model/settings.

Record only useful evidence:

```text
exact approved prompt
voice
model
visible settings
actual duration
approved pronunciation
successful tag/delivery patterns
failure patterns worth avoiding
```

Project calibration informs later production; it never overrides accepted PRD/Voice facts.
