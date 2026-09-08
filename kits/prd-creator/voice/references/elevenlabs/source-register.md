# Eleven v3 Source Register

Last verified: **2026-09-09**

Purpose: bind reusable SoundMaker rules to current evidence and prevent old Alpha guidance, generic TTS advice, deprecated product surfaces, or repository heuristics from becoming product truth.

## Authority order

```text
A — current official ElevenLabs v3/current documentation
B — official ElevenLabs product/help/blog material
C — creator/community material; heuristic only
P — approved project-calibrated prompt/audio evidence
```

For product truth: **A > B > C**. Project calibration can be stronger locally for a proven voice/project behavior, but never changes project facts.

## Conflict rule

Use the most specific current source for the active surface/model.

- v3-specific pause guidance overrides generic SSML advice;
- documented v3 Audio Tags override generic square-bracket warnings;
- active surface/API owns current setting availability;
- endpoint limits override broad product-overview claims;
- repository heuristics such as mandatory opening tags or `zero-tag-first` must yield to current product evidence and performance-quality reasoning.

## A — Current official sources

| Source | Use |
|---|---|
| `https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices` | v3 voice selection, Stability, Audio Tags, punctuation/CAPS, voice-range limits |
| `https://elevenlabs.io/docs/overview/capabilities/text-to-speech` | nondeterminism, seed, regenerations, large-text/context guidance |
| `https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech` | active TTS dashboard behavior/settings and free-regeneration conditions |
| `https://elevenlabs.io/docs/api-reference/text-to-speech/convert` | seed, `language_code`, normalization, previous/next text/request context |
| `https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps` | TTS timing + request context |
| `https://elevenlabs.io/docs/overview/capabilities/voices` | voice types and Default-voice replacement/expiry warning |
| `https://elevenlabs.io/docs/help-center/product/voices/my-voices/how-do-i-access-eleven-labs-default-voices` | Default voices expire 2026-12-31 and API voice-ID retrieval |
| `https://elevenlabs.io/docs/eleven-creative/voices/voice-design/` | Voice Design language/dialect, persona/timbre/pacing, preview-text guidance |
| `https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-i-select-the-language-and-accent` | website auto-language detection, API `language_code`, accent/voice-fit guidance |
| `https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries` | pronunciation dictionaries, IPA/CMU, v3 support |
| `https://elevenlabs.io/docs/eleven-agents/customization/voice/pronunciation-dictionary` | pronunciation dictionary formats/best practices; use only compatible general facts |
| `https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue` | turn-specific voice/text/tags, dialogue candidates/regenerations |
| `https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue` | current Dialogue request pattern |
| `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert` | Dialogue settings/request contract |
| `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps` | Dialogue timing evidence |
| `https://elevenlabs.io/docs/overview/models` | model positioning/language/input facts |
| `https://elevenlabs.io/docs/eleven-creative/products/studio` | current ElevenCreative Studio workflow |

## B — Official directing/product material

| Source | Use |
|---|---|
| `https://elevenlabs.io/blog/v3-audiotags` | emotion, pacing, delivery, reactions, placement, combinations; updated 2026-09-06 |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-expressing-emotional-context-in-speech` | emotional beats and moment-to-moment direction |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-precision-delivery-control-for-ai-speech` | pacing/rhythm/emphasis direction |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-enabling-narrative-intelligence-in-speech` | narration arcs |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-bringing-multi-character-dialogue-to-life` | multi-character interaction |
| `https://elevenlabs.io/blog/eleven-v3-character-direction` | character-performance directing |

## Current evidence conclusions

### Voice choice / actor casting

Current official v3 guidance calls voice selection the most important parameter. Tag effectiveness depends on the voice's native delivery and training range. Actor selection therefore precedes increasingly complex direction.

Current Default voices are being replaced and are scheduled to expire on **2026-12-31**. Production evidence should retain actual `voice_id` when reproducibility matters; a display-name replacement is not assumed equivalent.

### Stability

- Creative: more expressive/variable;
- Natural: balanced/closest to reference;
- Robust: more stable but less responsive to directional prompts.

For expression-heavy work, current guidance favors Creative or Natural over Robust.

### Audio Tags

Audio Tags are first-class v3 performance controls for emotion, attitude/subtext, projection, pace/rhythm, human reactions, moment-to-moment changes, and multi-speaker interaction. Tags are natural-language directions rather than a closed enum.

### Naturalness vs expression

Repository policy is hybrid:

```text
natural spoken wording
→ removes linguistic stiffness

Actor Baseline
→ preserves who is speaking

Expression Coverage + Audio Tags
→ preserves explicit acting
```

Neither `tag everything` nor `zero-tag-first` is a universal quality rule.

### Language / pronunciation

- website TTS auto-detects language from prompt context;
- mixed-language prompts can create language ambiguity;
- API supports optional `language_code` for explicit language/normalization context;
- accent comes strongly from the selected voice;
- pronunciation dictionaries support v3 phoneme control, including IPA/CMU;
- repeated critical names/terms are better candidates for dictionary control than ad-hoc emotional rewrites.

### Continuity

Use previous/next text or neighboring request IDs for connected TTS prosody. New requests can act as performance resets; material opening state may need explicit re-anchoring.

### Generation variance / candidates

ElevenLabs output is nondeterministic. API `seed` is best-effort only. Dashboard TTS can provide up to two free regenerations when text and parameters remain exactly unchanged; API billing differs. Repository policy therefore compares same-content candidates before rewriting a reviewed prompt after one weak take.

### Dialogue

Text to Dialogue keeps per-turn `voice_id` + text. Put Audio Tags inside the affected turn and review both the complete exchange and each constituent VO ID.

## Legacy warnings

- Eleven v3 does not use SSML `<break>`;
- former Voiceover Studio is not the current ElevenCreative Studio contract;
- old minimum-length/filler heuristics must not override current GA guidance;
- mechanical validation of an old repository rule does not establish product truth.

## C — Community material

Community guidance may suggest experiments but cannot establish product facts. Do not promote `always tag`, `never tag`, or other folklore into policy without stronger evidence.

## P — Project calibration

When actual audio is approved, retain only useful evidence:

```text
project / VO ID or Dialogue group
exact prompt
actual voice_id / voice source when material
surface/model/settings
expression tags and transition behavior
language/pronunciation setup when material
continuity context when material
seed when materially used
selected take
actual duration/timestamps when relevant
approved pronunciation
repeated failures worth avoiding
```

Do not universalize one project's behavior.

## Freshness rule

Re-check official sources when a task depends on changing controls or current UI/API behavior. Do not refresh everything for ceremony when the active task is unaffected.
