# Prompting archetypes

Read only the matching archetype. These are **repository craft recommendations**, not measured ElevenLabs presets. Official grounding: [prompting help](https://help.elevenlabs.io/hc/en-us/articles/25735604945041-How-do-I-prompt-for-sound-effects) and [SFX overview](https://elevenlabs.io/docs/overview/capabilities/sound-effects). Product controls belong to [contracts](elevenlabs-contracts-and-sources.md).

## Translate meaning into audible instructions

Keep the internal brief richer than the generation text. Recover: physical source, event, material/contact pair, time envelope, information conveyed to the player, source versus playback space, and exclusions that matter. Fill only unresolved audible dimensions. Do not add facts for descriptive richness.

Prompt order: event/source first; distinguishing mechanism/material; useful onset/sustain/decay; intended perspective; character. Prefer compatible descriptors over synonym stacks. A reaction sound is not a spoken line with a TTS acting tag.

English is a terminology convention for the examples, not a proven quality advantage. Explain unfamiliar local objects physically: egrang can be a bamboo stilt contact; sawit can mean an individual fruit or a heavy fruit bunch. Recover which one the accepted brief means rather than silently choosing scale or material.

Prefer positive audible specification. A short exclusion may clarify a recurring error, but negative wording is not a guaranteed negative-prompt control. Avoid long forbidden-word lists that compete with the actual sound. Prompt terms such as dry, isolated or one-shot must be checked in the output; they do not guarantee channel format, silence or event count.

## Archetype decisions

| Archetype | Direct the important dimensions | Reject/repair when |
|---|---|---|
| Creature | Species or approved fictional anatomy; vocal action; breath/throat/body resonance; state and intensity | Human speech, wrong species, cartoon character drift, or every state becoming a roar |
| Foley / footstep | Contacting object/footwear; surface; force/weight; one contact versus gait; debris | Unrequested full walking sequence, unrelated traffic, wrong contact material |
| Impact | Contact transient; material resonance; relevant debris; decay | Tail masks the next event, multiple unwanted hits, generic cinematic bass hides material |
| Machine | Power source; mechanism; load; stable or changing cycle; rattles only when justified | Combustion exhaust in an electric source, idle revving, inconsistent machinery |
| Vehicle | Engine identity separated from wheel/rail/air/chassis components; acceleration or braking load | Pass-by perspective baked into a source that must move freely in-game |
| UI / feedback | Information function; tonal direction; attack; duration/tail; relationship to other UI cues | Success and warning are indistinguishable, excessive ringing or a full melody |
| Ambience | Continuous bed; density; foreground spots; distance distribution; evolution | A distinctive spot repeats every cycle or an unwanted scene/voice is embedded |
| Weather | Wind/precipitation source; intensity; surface interaction; steady bed versus gust/event | Rain-on-metal replaces the required soil texture or all weather becomes cinematic thunder |
| Movement / whoosh | Moving object's mass/material; speed; trajectory; air displacement | Unwanted impact, tonal laser or giant-scale effect for a small motion |
| Sci-fi / magic | Physical acoustic anchor plus one synthetic transformation; energy envelope | Abstract adjective soup, inconsistent family timbre or unwanted music |
| Cinematic effect | Dominant onset/body/tail roles; intended scale; mix context | Detail layers compete with the main event or supply unintended story information |
| Short musical element | Instrument/texture, intended cue role; musical timing only if required | Full score is required: route to music production rather than expanding this SFX lane |

These rows are decision aids, not mandatory prompt fields. Footsteps need not describe every joint; machines need not specify an invented engineering design. For emotionally significant creatures, align intensity across states without assuming volume alone conveys the difference.

## Unheard preparation examples

The following are **UNTESTED examples**, not approved project assets, production orders, or measured results. Settings illustrate valid manual durations, not optimal durations. Every paid use still needs the execution budget gate. Each JSON block is an API request body; `output_format` is a separate query choice.

### Single bamboo contact

Use only when the approved sound is one stilt tip contacting compact soil, not a whole walking cycle. Check the hollow bamboo/ground balance and absence of extra steps. Runtime cadence belongs to the gameplay implementation.

```json
{"text":"One bamboo stilt tip striking compact dry soil, a firm hollow bamboo knock with a faint gritty contact, close dry perspective, short natural decay.","model_id":"eleven_text_to_sound_v2","duration_seconds":1.0,"loop":false,"prompt_influence":0.3}
```

### Electric motor idle

This is a loop + family state + single-source example. Check for stable load and identity; startup/shutdown are separate only when independently required. Preserve a selected anchor before producing additional states.

```json
{"text":"A compact electric traction motor idling steadily, a narrow high whine over a soft low rotor hum, subtle mechanical vibration, close dry recording, constant load without startup or shutdown.","model_id":"eleven_text_to_sound_v2","duration_seconds":8.0,"loop":true,"prompt_influence":0.3}
```

### Heavy oil-palm fruit bunch impact

Use only for an approved bunch, not an individual fruit. Check weight, ground contact and short fibrous detail. Do not add music, farm ambience or a worker's voice to a reusable impact.

```json
{"text":"One dense oil-palm fruit bunch dropping onto dry soil, a heavy muted impact followed by a brief fibrous rustle and a few small loose contacts, close perspective.","model_id":"eleven_text_to_sound_v2","duration_seconds":2.0,"loop":false,"prompt_influence":0.3}
```

### Creature alert

Check that tension is distinguishable from attack without changing the creature's apparent identity. This description does not establish a required angry state for any existing project.

```json
{"text":"A domestic cat giving one short tense warning growl, low feline throat vibration with a brief breathy release, close natural animal recording, restrained rather than a full attack.","model_id":"eleven_text_to_sound_v2","duration_seconds":2.0,"loop":false,"prompt_influence":0.3}
```

### Confirmation cue

Judge the cue in the existing UI family, not merely as an attractive isolated sound. The ascending gesture is an example design choice, not a universal semantic law.

```json
{"text":"A short clean electronic confirmation cue, two soft tones rising gently, rounded onset and a quick tidy decay, focused and unobtrusive.","model_id":"eleven_text_to_sound_v2","duration_seconds":1.0,"loop":false,"prompt_influence":0.3}
```

### Volcanic pressure bed

Check continuity and whether a distinctive pulse makes repetition obvious. An eruption and debris are not mandatory additional assets; derive them only from approved use.

```json
{"text":"Continuous deep volcanic pressure rumble, dense low rocky resonance with subtle irregular internal movement, steady underlying energy, no distinct blast or ending.","model_id":"eleven_text_to_sound_v2","duration_seconds":10.0,"loop":true,"prompt_influence":0.3}
```

## Revision economy

If the source is wrong, first compare the actual brief to the prompt. If the prompt already expresses it correctly, do not rewrite approved project facts to fit the generation. Inspect available takes; revise the smallest ambiguous phrase when justified. Change influence only after wording is clear. Exact timing, file channel layout and final level belong to editing/delivery when the endpoint cannot directly control them.
