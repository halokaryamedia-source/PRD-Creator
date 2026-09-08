# ElevenLabs Sound Effects Production

Status: active non-Voice `04 AUDIO` execution procedure  
Model scope: **ElevenLabs Sound Effects / `eleven_text_to_sound_v2`**

## Purpose

Turn one approved non-dialogue `AUDIO` asset requirement into a high-quality ElevenLabs Sound Effects generation without creating another source of truth.

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

Use this owner for non-dialogue audio such as:

- impacts, doors, machinery, UI feedback, footsteps, Foley;
- ambience, weather, drones, environmental loops;
- magical/sci-fi textures and transition effects;
- short musical-like sound-design elements when they are genuinely SFX rather than a full music deliverable.

Do not use this lane for spoken NPC/dialogue/narration. Voice remains Flow 5–7 ownership even if the Sound Effects model could produce voice-like material.

## Authority

Recover only what can affect the sound:

1. exact matching `AUDIO` requirement in `work/asset-requirements.md`;
2. its accepted Owner/Moment context when the Audio Brief alone is insufficient;
3. approved project-specific audio direction when it exists;
4. current ElevenLabs Sound Effects product facts for technique only.

Do not reopen the full PRD merely to make the prompt more descriptive. If the sound source/event/use is materially unresolved upstream, return to the 04 semantic owner rather than inventing it here.

## Operating modes

### Preparation Mode

Default when asked to design/review the sound but not actually generate audio.

Create one operator-ready prompt/settings recommendation. Do not claim audio quality, exact duration, seamless looping, or mix readiness without generated evidence.

### Generation Mode

Use when actual ElevenLabs SFX generation/review is requested.

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

Use this only as reasoning context; do not persist another schema.

```text
Sound Source
→ what physically or synthetically creates the sound?

Action
→ what exactly happens?

Material / Texture
→ metal, stone, wood, glass, cloth, electrical, organic, synthetic...?

Environment
→ dry studio, room, cavern, exterior, underwater, distant open space...?

Perspective
→ close, medium, distant, first-person, off-screen...?

Intensity
→ subtle, controlled, heavy, violent, massive...?

Temporal Shape
→ attack → body → decay; single hit, sequence, sustained bed...?

Use
→ one-shot, UI feedback, transition, loop, ambience, layered component...?

Timing Truth
→ auto, target duration, hard project constraint?
```

Fill only dimensions that materially improve the result. A simple click, impact, or footstep should stay simple.

## Prompt writing

Write concise natural language with useful audio terminology. Put the core sound event first, then only the details that distinguish the needed result.

Good shape:

```text
<source + action>, <material/texture>, <environment/perspective>, <intensity/character>, <production term when useful>
```

Examples of useful production terms include `foley`, `one-shot`, `impact`, `whoosh`, `ambience`, `drone`, `glitch`, or `stem` when they accurately describe the target.

Avoid:

- story prose that does not change the audible result;
- implementation instructions such as trigger code or game-state logic;
- contradictory adjectives;
- many unrelated sound events in one prompt;
- dialogue or narration text;
- filler added only to approach the product prompt limit.

The web Sound Effects product currently accepts prompts up to 450 characters. Treat that as a ceiling, not a target.

## Complex effects and layering

When one required effect contains materially different sound sources/events, prefer decomposing the **production execution** into useful layers while keeping the canonical AST requirement unchanged.

```text
complex canonical SFX
→ generate distinct audible components
→ select best component takes
→ layer/edit downstream
```

Example:

```text
large sci-fi door event
→ heavy mechanical unlock
→ hydraulic movement
→ metal stop impact
→ optional room tail
```

Do not force several unrelated events into one oversized prompt when separate generation gives better control. Do not create new AST IDs merely because production uses layers unless those layers become independently required project assets.

## Current ElevenLabs settings

For API production, current Sound Effects v2 controls are:

```text
Model: eleven_text_to_sound_v2
Duration: auto or 0.5–30 seconds on the API
Loop: false by default; true only for a genuinely repeating/sustained asset
Prompt Influence: 0.3 default, range 0–1
```

Rules:

- leave duration on auto when no project timing requirement exists;
- set duration when a target length materially matters, but do not claim exact game-ready timing until audio is heard/measured;
- enable Loop only for ambience/continuous material that should repeat without a perceptible boundary;
- begin near the default Prompt Influence rather than maximizing it automatically;
- raise Prompt Influence when literal adherence is the actual problem;
- lower it only when additional creative variation is desirable and still inside the approved Audio Brief.

Higher Prompt Influence generally means closer prompt adherence and less variation. It is not a universal quality slider.

The current web product generates multiple variations per Generate action. API behavior may differ by surface; candidate comparison remains the production principle regardless of surface.

## Candidate selection

Compare candidates on the audible job, not on novelty.

A useful internal comparison is:

```text
identity     → unmistakably the intended sound?
material     → source/material reads correctly?
shape        → attack/body/decay or loop behavior fits the use?
space        → perspective/environment appropriate?
artifacts    → no distracting generation defects?
editability  → clean enough for downstream game/mix use?
```

Do not persist a numeric scorecard. Select the strongest take, or describe the first repeated defect that justifies a prompt/settings revision.

## Troubleshooting order

```text
wrong event/source
→ canonical Audio Brief / upstream meaning

right event but wrong material/space/intensity
→ prompt wording

right prompt but too literal / too variable
→ Prompt Influence

wrong length
→ duration target / prompt temporal shape

loop seam or unsuitable sustained texture
→ Loop setting + regenerate/listen

complex result muddy
→ split into production layers

one isolated odd take
→ compare/regenerate before rewriting
```

Do not repair an upstream requirement problem by making the prompt increasingly complicated.

## Output and evidence

Current product guidance supports MP3 output broadly and WAV 48 kHz for non-looping effects on supported product surfaces. Prefer WAV when downstream editing/mastering benefits from it and the active surface exposes it; MP3 is sufficient for many review uses.

Audio evidence should identify enough generation context to reproduce or diagnose the selected take when useful:

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

Keep this as generation evidence/operator context, not as new canonical 04 fields.

## Approval lock

When the user approves an actual generated SFX:

1. preserve the exact prompt/settings that produced the selected take when evidence is retained;
2. record measured duration only from the actual file;
3. treat the approved behavior as project calibration for similar later SFX, not a universal ElevenLabs rule;
4. do not rewrite `asset-requirements.md` unless the approved project meaning itself changed.

## Current official references

Last verified: **2026-09-08**

- `https://elevenlabs.io/docs/overview/capabilities/sound-effects`
- `https://elevenlabs.io/docs/eleven-creative/playground/sound-effects`
- `https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert`
- `https://elevenlabs.io/docs/help-center/product/core-capabilities/sound-effects/how-do-i-prompt-for-sound-effects`

When live product controls or official API contracts conflict with this procedure, re-verify the active surface before turning the new behavior into durable repository policy.
