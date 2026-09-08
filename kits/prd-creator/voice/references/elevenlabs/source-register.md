# Eleven v3 Source Register

Last verified: 2026-09-08

Purpose: keep reusable SoundMaker rules tied to evidence and prevent generic TTS guidance, old v3 Alpha material, deprecated product surfaces, or creator folklore from silently becoming current policy.

## Authority order

```text
A — current official ElevenLabs v3-specific/current documentation
B — official product/help/blog material, including product-specific surfaces
C — creator/community material; heuristic only
P — project-calibrated approved prompt/audio evidence
```

For product truth: **A > B > C**.  
For an already-proved voice/project behavior: **P** can be more useful locally, but never changes upstream project facts.

### Conflict rule

When generic ElevenLabs guidance conflicts with an explicit Eleven v3 or endpoint-specific rule, use the **most specific current rule** for SoundMaker.

Examples:

- generic SSML pause guidance does not override the v3-specific rule that Eleven v3 does not support SSML `<break>`;
- generic warnings about square brackets do not invalidate documented v3 Audio Tags;
- generic Speed guidance does not override current v3-specific Text to Speech guidance that standard v3 TTS has no Speed setting;
- product overview statements do not override a stricter current API endpoint request limit for that endpoint.

## A — Current official sources

| Source | Use |
|---|---|
| `https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices` | v3 voice selection, Stability, punctuation/CAPS, Audio Tags, Enhance behavior, v3 pause rule, native IPA, multi-speaker examples |
| `https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech` | current TTS UI/model behavior, standard v3 Speed availability, Stability behavior, output/settings context |
| `https://elevenlabs.io/docs/overview/capabilities/text-to-speech` | nondeterminism, same-content regeneration behavior, seed/context mechanisms, large-text guidance |
| `https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue` | Text to Dialogue purpose, per-turn voice/text behavior, candidate generation guidance, request-size guidance |
| `https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue` | current Dialogue API generation pattern and reliable request-size guidance |
| `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert` | Dialogue endpoint settings, unique-voice/request contract, language/normalization/dictionary/seed controls |
| `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps` | Voice segments and character-level timing evidence |
| `https://elevenlabs.io/docs/overview/models` | current v3 positioning/language/input-limit facts |
| `https://elevenlabs.io/docs/help-center/troubleshooting/why-does-my-voice-start-whispering-change-accent-change-tone-or-break` | Stability/voice drift diagnosis |
| `https://elevenlabs.io/docs/help-center/troubleshooting/why-does-my-voice-change-accent-or-language` | voice/language/accent compatibility |
| `https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries` | pronunciation dictionary behavior |
| `https://elevenlabs.io/docs/api-reference/text-to-speech/convert` | seed, text normalization, previous/next context |
| `https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps` | timing + request-context support |
| `https://elevenlabs.io/docs/eleven-creative/products/studio` | current ElevenCreative Studio generation history, paragraph/selection regeneration, locking, timeline, SFX/music integration |
| `https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/why-are-numbers-dates-symbols-and-acronyms-not-properly-pronounced-or-spoken-in-the-correct-language` | explicit spoken-form normalization guidance |

## B — Official directing/product material

Use when current A-level documentation does not already settle the question.

| Source | Use / caveat |
|---|---|
| `https://elevenlabs.io/blog/eleven-v3-is-now-generally-available` | v3 GA status since 2026-02-02 |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-expressing-emotional-context-in-speech` | emotional beats / long-form performance concepts |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-precision-delivery-control-for-ai-speech` | pacing/rhythm/emphasis examples |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-enabling-narrative-intelligence-in-speech` | narrative performance examples |
| `https://elevenlabs.io/blog/eleven-v3-character-direction` | character/accent directing examples |
| `https://elevenlabs.io/blog/v3-audiotags` | Audio Tag concept/examples |
| `https://help.elevenlabs.io/hc/en-us/articles/29314862567313-What-is-Voice-Design` | Voice Design status/capability caveats |
| `https://elevenlabs.io/docs/eleven-agents/customization/voice/expressive-mode` | Agents-specific expressive behavior; do **not** copy its tag-scope number into normal Speech Synthesis |

## Legacy warnings

Old v3 Alpha-era prompting pages may contain superseded guidance such as minimum-length encouragement. Current GA documentation is authority when it addresses the same topic. Do not create filler to satisfy an old character-count heuristic.

The former Voiceover Studio product was sunset on **2026-05-15**. Its legacy Fixed Duration behavior may explain historical projects but must not be treated as the current ElevenCreative Studio contract.

## C — Creator/community material

Creator sources may suggest experiments but cannot establish product truth.

Useful current examples previously reviewed:

- Versely v3 Creator Guide 2026 — over-tagging/punctuation observations;
- Greg Preece v3 tutorial — creator workflow observations;
- OmniArt v3 tags guide — voice-director framing.

Do not store anecdotal claims such as `v3 tags are broken` as repository policy without authoritative evidence.

## P — Project calibration

When actual audio is approved, retain only evidence that improves later production:

```text
project / Voice ID or same-Moment Dialogue group
exact generated prompt(s)
actual ElevenLabs voice ID(s)
Eleven v3 surface / endpoint
visible settings / Stability
seed when materially used
actual duration / generated timestamps when relevant
approved pronunciation
successful performance behavior
repeated failure worth avoiding
```

Do not promote one project's behavior into a universal v3 rule.

## Current product caveats

### Enhance

Enhance can add tags, capitalization, punctuation, and performance cues. SoundMaker-directed prompts keep Enhance **OFF by default**; any Enhance rewrite becomes a new draft requiring review.

### Text to Speech vs Text to Dialogue

Use standard TTS for independent speech. Use Text to Dialogue for same-Moment multi-speaker turns whose delivery depends materially on the conversation. Keep canonical `VO-...` identity unchanged; generation grouping is temporary.

### ElevenCreative Studio

Use the current Studio for long-form/editorial timeline work when useful. Do not route new work to the deprecated Voiceover Studio or assume its old controls exist unchanged.

### PVC / v3

Treat current compatibility warnings as a voice-fit risk requiring actual output evidence; do not silently approve or silently switch model families.

### Language controls

If live UI/API controls differ from older help text, current surface owns control availability while current official language/accent principles remain the semantic reference.

## Freshness rule

Re-check official sources when a task depends on a changing product control or when the observed current UI/API conflicts with this register. Do not refresh all sources for ceremony when the active task does not depend on them.
