# Eleven v3 Source Register

Last verified: 2026-08-13

Purpose: keep reusable SoundMaker rules tied to evidence and prevent generic TTS guidance, old v3 Alpha material, or creator folklore from silently becoming current policy.

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

When generic ElevenLabs guidance conflicts with an explicit Eleven v3 rule, use the **v3-specific rule** for SoundMaker.

Examples:

- generic SSML pause guidance does not override the v3-specific rule that Eleven v3 does not support SSML `<break>`;
- generic warnings about square brackets do not invalidate documented v3 Audio Tags;
- generic Speed guidance does not override current v3-specific product guidance that the Speed setting is unavailable for v3.

## A — Current official sources

| Source | Use |
|---|---|
| `https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices` | v3 voice selection, Stability, punctuation/CAPS, Audio Tags, Enhance behavior, v3 pause rule, native IPA |
| `https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech` | current TTS UI/model behavior, v3 Speed availability, Stability behavior, output/settings context |
| `https://elevenlabs.io/docs/overview/capabilities/text-to-speech` | nondeterminism, up to two free same-content regenerations, seed/context mechanisms, large-text guidance |
| `https://elevenlabs.io/docs/overview/models` | current v3 positioning/language/input-limit facts |
| `https://elevenlabs.io/docs/help-center/troubleshooting/why-does-my-voice-start-whispering-change-accent-change-tone-or-break` | Stability/voice drift diagnosis and Studio recommendation for longer unstable text |
| `https://elevenlabs.io/docs/help-center/troubleshooting/why-does-my-voice-change-accent-or-language` | voice/language/accent compatibility |
| `https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries` | pronunciation dictionary behavior |
| `https://elevenlabs.io/docs/api-reference/text-to-speech/convert` | seed, text normalization, previous/next context |
| `https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps` | timing + request-context support |
| `https://elevenlabs.io/docs/voiceover-studio/overview` | Dynamic vs Fixed Duration and Studio timing behavior |
| `https://elevenlabs.io/docs/help-center/account/general/have-characters-changed` | credits/characters terminology |
| `https://elevenlabs.io/docs/help-center/product/speech-synthesis/text-to-speech/why-are-numbers-dates-symbols-and-acronyms-not-properly-pronounced-or-spoken-in-the-correct-language` | explicit spoken-form normalization guidance |

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

## Legacy warning

`https://elevenlabs.io/docs/best-practices/prompting` still contains Alpha-era text such as the old >250-character encouragement. Current v3 is GA and the current consolidated Best Practices page is the authority when it addresses the same topic.

Do not create filler merely to satisfy the old 250-character guidance.

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
project / Voice ID
exact generated prompt
voice
Eleven v3 surface
visible settings / Stability
actual duration
approved pronunciation
successful performance behavior
repeated failure worth avoiding
```

Do not promote one project's behavior into a universal v3 rule.

## Current product caveats

### Enhance

Enhance can add tags, capitalization, punctuation, and performance cues. SoundMaker-directed prompts keep Enhance **OFF by default**; any Enhance rewrite becomes a new draft requiring review.

### Speech Synthesis vs Studio

Use Speech Synthesis normally. When longer content exhibits unintended whispering, volume/tone/accent drift, or breaking/distortion, official troubleshooting supports moving that production to Studio while keeping Eleven v3.

### PVC / v3

Treat current compatibility warnings as a voice-fit risk requiring actual output evidence; do not silently approve or silently switch model families.

### Language controls

If live UI controls differ from older help text, current UI owns control availability while current official language/accent principles remain the semantic reference.

## Freshness rule

Re-check official sources when a task depends on a changing product control or when the observed current UI conflicts with this register. Do not refresh all sources for ceremony when the active task does not depend on them.
