# Eleven v3 Source Register

Last verified: **2026-09-08**

Purpose: bind reusable SoundMaker rules to current evidence and prevent old v3 Alpha guidance, generic TTS advice, deprecated product surfaces, or repository heuristics from becoming product truth.

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

Examples:

- v3-specific pause guidance overrides generic SSML advice;
- documented v3 Audio Tags override generic square-bracket warnings;
- active surface/API owns current setting availability;
- endpoint request limits override broad product-overview claims;
- repository heuristics such as mandatory opening tags or `zero-tag-first` must yield to current product evidence and performance-quality reasoning.

## A — Current official sources

| Source | Use |
|---|---|
| `https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices` | v3 voice selection, Stability, Audio Tags, punctuation/CAPS, Enhance, pauses, IPA, multi-speaker prompting |
| `https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech` | active TTS surface behavior/settings and v3 Audio Tag/punctuation controls |
| `https://elevenlabs.io/docs/overview/capabilities/text-to-speech` | nondeterminism, regeneration, large-text/context guidance |
| `https://elevenlabs.io/docs/api-reference/text-to-speech/convert` | seed, normalization, `previous_text`/`next_text`, neighboring request-ID context |
| `https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps` | TTS timing + request context |
| `https://elevenlabs.io/docs/eleven-creative/voices/voice-design/` | Voice Design language/dialect, persona/timbre/pacing, preview-text guidance |
| `https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue` | turn-specific voice/text and Audio Tags, dialogue purpose/candidates |
| `https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue` | current Dialogue request pattern and tag placement inside each turn |
| `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert` | Dialogue settings/request contract |
| `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps` | Dialogue segment/character timing |
| `https://elevenlabs.io/docs/overview/models` | current model positioning/language/input facts |
| `https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-alpha` | current help summary for emotion/delivery/reaction tags |
| `https://elevenlabs.io/docs/eleven-creative/products/studio` | current ElevenCreative Studio workflow |
| `https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries` | pronunciation dictionaries |

## B — Official directing/product material

| Source | Use |
|---|---|
| `https://elevenlabs.io/blog/v3-audiotags` | current Audio Tag guide: emotion, pacing, delivery, reactions, accents, placement, combinations; updated 2026-07-28 |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-expressing-emotional-context-in-speech` | emotional beats and moment-to-moment direction |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-precision-delivery-control-for-ai-speech` | pacing/rhythm/emphasis direction |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-enabling-narrative-intelligence-in-speech` | narration arcs / narrative performance |
| `https://elevenlabs.io/blog/eleven-v3-audio-tags-bringing-multi-character-dialogue-to-life` | interruption/overlap/emotional interplay |
| `https://elevenlabs.io/blog/eleven-v3-character-direction` | character-performance directing |
| `https://elevenlabs.io/blog/eleven-v3-situational-awareness` | situational emotion/projection/pacing cues |

## Current evidence conclusions

### Voice choice

Current official guidance calls voice selection the most important v3 parameter. Tag effectiveness depends on voice character/training range.

### Stability

- Creative: more expressive/variable;
- Natural: balanced/closest to reference;
- Robust: more stable but less responsive to directional prompting.

For maximum expressiveness with Audio Tags, current guidance favors Creative or Natural.

### Audio Tags

Current official material establishes Audio Tags as a first-class v3 performance mechanism for:

- emotion;
- attitude/subtext;
- vocal delivery/projection;
- pacing/rhythm;
- human reactions;
- character/accent candidates;
- moment-to-moment changes;
- multi-speaker interaction.

Tags are natural-language instructions, not a closed enum. Current official examples explicitly place multiple tags and state changes inline where delivery changes.

### Enhance

Current Best Practices exposes the Enhance prompt. It explicitly asks the model to:

- analyze each line's mood/context;
- add contextually appropriate Audio Tags for expression/subtext;
- place them strategically near affected dialogue;
- keep tags auditory;
- preserve original meaning;
- avoid contradictory/invented direction.

SoundMaker adopts these principles but performs its own speechification + Expression Coverage, so Enhance remains OFF on reviewed prompts by default.

### Naturalness vs expression

Current guidance supports both natural speech/text structure **and** Audio Tags. Therefore repository policy is hybrid:

```text
natural spoken wording
→ removes linguistic stiffness

Expression Coverage + Audio Tags
→ preserves explicit acting
```

Neither `tag everything` nor `zero-tag-first` is accepted as a universal quality rule.

### Continuity

Use previous/next text or neighboring request IDs for connected TTS prosody. Treat new requests as possible acting resets; material opening state may need explicit re-anchoring.

### Dialogue

Text to Dialogue keeps per-turn `voice_id` + text. Put Audio Tags inside the turn they affect.

## Legacy warnings

- Eleven v3 does not use SSML `<break>`; use v3 prompting techniques.
- Former Voiceover Studio was sunset; do not treat legacy controls as current ElevenCreative Studio policy.
- Old minimum-length/filler heuristics must not override current GA guidance.
- Mechanical validation of an old repository rule does not establish product truth.

## C — Community material

Community/creator guidance may suggest experiments but cannot establish product facts. Do not promote anecdotal claims such as `tags are broken`, `always start with a tag`, or `never use tags` into policy without stronger evidence.

## P — Project calibration

When actual audio is later approved, retain only useful evidence:

```text
project / VO ID or Dialogue group
exact prompt
voice ID
surface/model/settings
expression tags and transition behavior that worked
continuity context when material
seed when used
actual duration/timestamps when relevant
approved pronunciation
repeated failures worth avoiding
```

Do not universalize one project's behavior.

## Freshness rule

Re-check official sources when a task depends on changing controls or current UI/API behavior. Do not refresh everything for ceremony when the active task is unaffected.
