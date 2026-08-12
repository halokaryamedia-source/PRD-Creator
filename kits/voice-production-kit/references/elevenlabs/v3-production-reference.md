# Eleven v3 Production Reference

Last verified: 2026-08-13

This page records current operational facts that affect real **Eleven v3** output. See `source-register.md` for evidence authority.

## 1. Current model status

**OFFICIAL-CURRENT:** Eleven v3 became Generally Available on 2026-02-02. Some older ElevenLabs pages/URLs still contain `Alpha`; do not treat that legacy label as current product status.

Operational model scope for this repository:

```text
Eleven v3 only
```

Current model documentation lists v3 with 70+ languages, high emotional range/contextual understanding, and a 5,000-character model input limit. For the web Speech Synthesis page, current account limits may differ by plan.

Do not use this page to compare or automatically fall back to other model families.

## 2. Credits / usage

**OFFICIAL-CURRENT:** website Text to Speech uses credits based on written input characters. Current ElevenLabs guidance states v3 uses 1 credit per character on the standard website path; some shared voices can apply a multiplier.

Do not describe TTS usage as LLM tokens.

Audio Tags/directions are written input and therefore contribute input characters; there is no separate documented tag surcharge.

## 3. Voice selection is the first production decision

**OFFICIAL-CURRENT:** ElevenLabs identifies voice choice as the most important parameter for v3.

The base voice must already be reasonably compatible with the requested delivery. A calm, meditative, or reassuring source is not guaranteed to become a convincing frantic/shouting/comedic actor because of tags.

For v3:

- expressive source recordings/designs are more suitable when broad acting range is required;
- neutral voices can be more stable;
- a targeted niche voice can outperform a generic narrator when one performance family dominates.

### PVC / compatibility caveat

Current ElevenLabs material and the web UI can expose compatibility warnings for some Professional Voice Clones with v3.

Repository rule under the v3-only scope:

```text
voice is weak/inconsistent with v3
→ treat as voice-fit/compatibility risk
→ choose a more suitable v3-compatible voice/profile
→ do not switch SoundMaker to another model family
```

Do not silently declare a risky pairing production-safe without actual output evidence.

### Voice Design

Current ElevenLabs material describes Voice Design v3 as a way to create character/profile characteristics compatible with v3 and Audio Tags. Use it when no existing voice has the required performance range; do not redesign a voice merely because one take was weak.

## 4. Stability

**OFFICIAL-CURRENT:** Stability is a major v3 control.

- **Creative** — more emotional/expressive; more variable and more prone to odd output.
- **Natural** — balanced; closest to reference voice behavior.
- **Robust** — more stable/consistent; less responsive to directional prompts.

Repository baseline:

```text
Natural
```

Move toward Creative only when:

- the base voice fits the task;
- spoken wording/beat structure are already sound;
- more expressive range is genuinely required.

Do not move to Creative as the first fix for a structurally flat script.

## 5. Speed

Official ElevenLabs documentation has shown conflicting information on Speed availability for v3 across product/help surfaces.

Status: **UNKNOWN / UI-DEPENDENT**.

The current web UI is authority for control availability during actual production. SoundMaker must not depend on Speed as its main duration/quality mechanism.

Primary controls remain:

```text
word budget
→ spoken architecture
→ local v3 pacing direction
```

## 6. Text structure, punctuation, and tags

**OFFICIAL-CURRENT:** v3 output is materially influenced by:

- natural speech patterns;
- emotional context;
- text structure;
- punctuation;
- capitalization;
- Audio Tags;
- voice matching.

ElevenLabs specifically documents that:

- ellipses add pauses/weight;
- capitalization increases emphasis;
- standard punctuation provides natural rhythm;
- multiple Audio Tags can be combined;
- experimental tags can vary across voices.

Detailed production rules: `v3-performance-writing.md`.

## 7. Audio Tag scope

Standard Speech Synthesis v3 supports moment-to-moment / mid-delivery direction.

**UNKNOWN:** there is no documented fixed persistence window for standard v3 TTS tags.

A separate Agents/Conversational expressive product documents a short approximate tag scope. That product-specific number must not be copied into normal Speech Synthesis rules.

SoundMaker therefore places direction close to the intended beat and re-establishes direction only when performance state materially changes.

## 8. Generation variance and regeneration

**OFFICIAL-CURRENT:** ElevenLabs TTS is nondeterministic. Same voice/settings/text can produce different takes.

API can expose a `seed` control as a best-effort consistency aid; determinism is not guaranteed.

For web v3, actual UI controls such as multiple alternatives or `Regenerate` determine what is available and whether another action may consume credits.

Production rule:

```text
one weak/odd take + otherwise sound prompt
→ review another available take / eligible regeneration first

same failure repeatedly at the same semantic/performance point
→ diagnose prompt / voice fit / Stability
```

Do not micro-edit a good prompt after every random weak take.

## 9. Long-form generation and continuity

Current v3 model documentation lists a 5,000-character API input limit. Longer production may require segmentation or a longer-form ElevenLabs product surface.

If API generation must be split, ElevenLabs supports context mechanisms such as:

- `previous_text` / `next_text`;
- `previous_request_ids` / `next_request_ids`;

for improved continuity/prosody across chunks.

For web/manual production, split at semantic boundaries:

```text
scene boundary
paragraph boundary
major emotional transition
```

Do not split inside one important emotional beat merely to create equal chunks.

## 10. Pronunciation

For production-critical terms:

1. write numbers/dates/acronyms/symbols in the intended spoken form when ambiguity matters;
2. use project pronunciation notes for fantasy/proper nouns;
3. use native v3 IPA or pronunciation dictionaries when needed;
4. approve pronunciation only after actual audio evidence exists.

Project terms should be locked once approved rather than re-guessed line by line.

## 11. Language and accent

Current ElevenLabs guidance indicates:

- text strongly determines language;
- the chosen voice strongly influences accent/pronunciation;
- voices suitable for the target language/accent generally perform more naturally.

If the live UI exposes a Language Override, treat the live control as the current product surface. Do not infer a setting that the current UI does not expose.

## 12. Text normalization

Website/API product behavior can normalize numbers, dates, symbols, and similar text.

For predictable final VO, prefer explicit spoken forms for material numbers, dates, symbols, and acronyms instead of depending on normalization to guess intent.

## 13. Duration

Normal v3 TTS duration is dynamic. Exact duration is not guaranteed from text alone.

Voiceover Studio has a product-specific Fixed Duration capability, but forcing a clip far from its natural duration can sound unnaturally fast/slow.

Use `v3-duration-planning.md` whenever timing is specified.

## 14. Output format

MP3 44.1 kHz / 128 kbps is adequate for review/general delivery and does not explain flat acting.

When downstream audio editing is expected and the account/product exposes a suitable lossless option, prefer a less-compressed source for post-production. Do not confuse codec quality with performance quality.

## 15. Voice vs sound effects boundary

This reference is for **voice performance**.

Keep environment/SFX such as doors, machinery, impacts, wind, explosions, and ambience in the Sound Effects production lane rather than relying on TTS tags as the default SFX generator.

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
- normal Speech Synthesis guarantees exact duration from text alone.

## 17. Project calibration

The strongest reusable evidence for a specific production is an approved result from the same project/voice/v3 settings.

Record only useful evidence:

```text
exact approved prompt
voice
model = Eleven v3
visible settings
actual duration
approved pronunciation
successful tag/delivery patterns
failure patterns worth avoiding
```

Project calibration informs later production; it never overrides accepted PRD/Voice facts.
