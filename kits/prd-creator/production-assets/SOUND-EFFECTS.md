# ElevenLabs Sound Effects Production

Status: active Production Assets AUDIO execution procedure  
Model scope: **ElevenLabs Sound Effects / `eleven_text_to_sound_v2`**

## Purpose

Turn one approved non-dialogue `AUDIO` Production Assets requirement into a high-quality ElevenLabs Sound Effects generation without creating another source of truth.

```text
accepted AUDIO requirement
→ recover sound intent
→ design one bounded SFX prompt/settings set
→ generate variants
→ hear / select / revise only when needed
→ deliver approved audio evidence
```

`work/asset-requirements.md` remains canonical for what sound is required. SFX prompts, settings, variants, and generated files are production execution/evidence, not new project meaning.

## Boundary

Use this owner for non-dialogue audio such as impacts, doors, machinery, UI feedback, footsteps, Foley, ambience, weather, drones, environmental loops, magical/sci-fi textures, transition effects, and short sound-design elements that are genuinely SFX.

Do not use this lane for spoken NPC/dialogue/narration. Spoken content remains Voice Requirements → Voice Production → Voice Delivery ownership even if the Sound Effects model could produce voice-like material.

## Authority

Recover only what can affect the sound:

1. exact matching `AUDIO` requirement in `work/asset-requirements.md`;
2. accepted Owner/Moment context when the Audio Brief alone is insufficient;
3. approved project-specific audio direction when it exists;
4. current ElevenLabs Sound Effects product facts for technique only.

Do not reopen the full PRD merely to make the prompt more descriptive. If the sound source/event/use is materially unresolved upstream, return to the Production Assets semantic owner rather than inventing it here.

## Operating modes

### Preparation Mode

Default when asked to design/review the sound but not actually generate audio. Create one operator-ready prompt/settings recommendation. Do not claim audio quality, exact duration, seamless looping, or mix readiness without generated evidence.

### Generation Mode

```text
one approved AST-... AUDIO target
→ exact reviewed prompt/settings
→ generate available variants
→ listen comparatively
→ select best candidate or diagnose repeated defect
→ bounded revision if needed
```

A merely different first take is not evidence that the prompt is wrong. Review available variants before rewriting a prompt whose intent/settings are already correct.

## Internal Sound Fill Map

Use only as reasoning context; do not persist another schema.

```text
Sound Source
Action
Material / Texture
Environment
Perspective
Intensity
Temporal Shape
Use
Timing Truth
```

Fill only dimensions that materially improve the result. A simple click, impact, or footstep should stay simple.

## Prompt writing

Write concise natural language with useful audio terminology. Put the core sound event first, then only details that distinguish the needed result.

```text
<source + action>, <material/texture>, <environment/perspective>, <intensity/character>, <production term when useful>
```

Avoid story prose that does not change the audible result, implementation instructions, contradictory adjectives, unrelated events in one prompt, dialogue/narration text, and filler added only to approach a prompt limit.

## Complex effects and layering

When one required effect contains materially different sound sources/events, prefer decomposing **production execution** into useful layers while keeping the canonical AST requirement unchanged.

```text
complex canonical SFX
→ generate distinct audible components
→ select best component takes
→ layer/edit downstream
```

Do not create new AST IDs merely because production uses layers unless those layers become independently required project assets.

## Current ElevenLabs settings

```text
Model: eleven_text_to_sound_v2
Duration: auto or 0.5–30 seconds on API
Loop: false by default; true only for genuinely repeating/sustained assets
Prompt Influence: 0.3 default, range 0–1
```

Leave duration on auto when no project timing requirement exists. Enable Loop only for material that genuinely repeats. Begin near default Prompt Influence rather than maximizing it. Higher Prompt Influence generally means closer adherence and less variation; it is not a universal quality slider.

## Candidate selection

Compare candidates on the audible job:

```text
identity
material
shape
space
artifacts
editability
```

Do not persist a numeric scorecard. Select the strongest take or describe the first repeated defect that justifies a prompt/settings revision.

## Troubleshooting order

```text
wrong event/source → canonical Audio Brief / Production Assets meaning
right event but wrong material/space/intensity → prompt wording
right prompt but too literal / too variable → Prompt Influence
wrong length → duration target / prompt temporal shape
loop seam / unsuitable sustained texture → Loop + regenerate/listen
complex result muddy → split into production layers
one isolated odd take → compare/regenerate before rewriting
```

Do not repair an upstream requirement problem by making the prompt increasingly complicated.

## Output and evidence

Prefer WAV when downstream editing/mastering benefits from it and the active surface exposes it; MP3 is sufficient for many review uses.

Useful generation evidence may include:

```text
AST ID
exact prompt
model
surface
duration setting
loop setting
prompt influence
selected candidate/take
actual duration when measured
```

Keep this as generation evidence/operator context, not as new canonical Production Assets fields.

## Approval lock

When the user approves an actual generated SFX:

1. preserve exact prompt/settings when evidence is retained;
2. record measured duration only from the actual file;
3. treat approved behavior as project calibration, not a universal rule;
4. do not rewrite `asset-requirements.md` unless approved project meaning changed.

## Current official references

Last verified: **2026-09-08**

- `https://elevenlabs.io/docs/overview/capabilities/sound-effects`
- `https://elevenlabs.io/docs/eleven-creative/playground/sound-effects`
- `https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert`
- `https://elevenlabs.io/docs/help-center/product/core-capabilities/sound-effects/how-do-i-prompt-for-sound-effects`

When live product controls or official API contracts conflict with this procedure, re-verify the active surface before turning new behavior into durable repository policy.