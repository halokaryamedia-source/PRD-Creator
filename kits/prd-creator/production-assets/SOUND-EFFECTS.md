# ElevenLabs Sound Effects Production

Status: active Production Assets AUDIO execution procedure  
Model scope: **ElevenLabs Sound Effects / `eleven_text_to_sound_v2`**

## Purpose

Turn one approved non-dialogue `AUDIO` Production Assets requirement into an operator-ready or generated ElevenLabs sound effect while preserving project meaning, sound identity, continuity, and proof economy.

```text
accepted AUDIO requirement
→ recover audible intent only
→ choose the smallest useful SFX mode
→ establish family baseline only when continuity matters
→ design one bounded prompt/settings set
→ generate / compare candidates when requested
→ revise only the first repeated defect
→ deliver approved audio evidence
```

`work/asset-requirements.md` remains canonical for **what sound is required**. Prompt wording, ElevenLabs settings, family baselines, temporary layers, candidates, and generated files are production execution/evidence; they do not become a second source of project truth.

## Boundary

Use this owner for non-dialogue audio such as impacts, doors, machinery, UI feedback, footsteps, Foley, ambience, weather, drones, environmental loops, creature non-verbal sounds, magical/sci-fi textures, transition effects, and short sound-design elements that are genuinely SFX.

Do not use this lane for spoken NPC/dialogue/narration. Spoken content remains Voice Requirements → Voice Production → Voice Delivery even if a sound-effects model can produce voice-like material.

This file is the detailed SFX craft owner inside **Production Assets**. Do not create a new root semantic skill merely because SFX uses ElevenLabs or has specialized generation technique.

## Authority

Recover only context that can materially change the audible result:

1. exact matching `AUDIO` requirement in `work/asset-requirements.md`;
2. accepted Owner/Moment context when the Audio Brief alone is insufficient;
3. approved same-project sound direction or approved generated SFX evidence when it exists;
4. current ElevenLabs Sound Effects product/API facts for technique only.

Do not reopen the full PRD merely to make a richer prompt. If sound source, event, gameplay use, required state, or authoritative timing is materially unresolved, return to the Production Assets semantic owner instead of inventing it here.

## Operating modes

### Preparation Mode

Default when asked to design, review, or prepare SFX without generating audio.

Preparation may establish:

- audible intent;
- SFX mode;
- family baseline when continuity matters;
- exact prompt;
- duration / loop / prompt-influence recommendation;
- decomposition plan for a genuinely layered effect;
- generation readiness.

Preparation does **not** prove actual timbre, artifacts, seamless looping, measured duration, mix readiness, or audio quality. Those require generated/heard evidence.

### Generation Mode

Use only when actual generation/review is requested and an ElevenLabs execution surface is available.

```text
one approved AST-... AUDIO target
→ exact reviewed prompt/settings
→ generate available variants
→ listen comparatively
→ select best candidate OR identify first repeated defect
→ bounded revision when justified
→ regenerate only affected scope
```

One unusual take is candidate variance, not evidence that the prompt is wrong.

## SFX mode router

Choose the smallest mode that matches the audible job. This is ephemeral reasoning, not persisted schema.

| Mode | Use when | Default production behavior |
|---|---|---|
| `ONE_SHOT` | one discrete event | one concise prompt; loop off |
| `LOOP` | genuinely sustained/repeating ambience or mechanism | loop on only when the asset should repeat seamlessly |
| `STATE_VARIANT` | the same source has multiple required states | one family baseline + per-state audible delta |
| `SEQUENCE` | one event has meaningful temporal progression | describe ordered audible phases without story prose |
| `LAYERED` | materially distinct sources/events become muddy as one generation | generate useful components separately, combine downstream |

Do not classify a simple sound as `LAYERED` merely to make production look sophisticated. Do not split one canonical AST requirement into new AST IDs unless the project actually requires those layers as independent assets.

## Audible intent map

Use only the dimensions that materially improve the result:

```text
Sound Source
Action / Event
Material / Mechanism
Temporal Shape
Environment / Space
Perspective / Distance
Intensity / Energy
Texture / Character
Use
Timing Truth
```

For a basic click, impact, footstep, or UI cue, most fields should remain implicit. More adjectives are not automatically more control.

## Family continuity

Use an internal **SFX Family Baseline** only when multiple required sounds must remain recognizably the same source, object, creature, machine, environment, or effect family.

```text
SFX Family Baseline

Source Identity
Core Timbre
Material / Mechanism
Recording Perspective
Space
Energy Range
Texture
No-Drift Boundary
```

Then treat each required state as a delta from the same baseline:

```text
Family Baseline
→ idle delta
→ movement delta
→ alert / action delta
→ impact / damage delta
→ shutdown / aftermath delta
```

The state names above are examples only. Required states come from approved project meaning; SFX craft does not invent gameplay states.

Continuity rule:

```text
same canonical source across multiple sounds
→ preserve stable audible identity
→ vary only the state-specific event / energy / temporal shape / space that actually changes
```

Do not solve identity drift by independently rewriting every prompt with unrelated descriptors. First repair the shared baseline concept, then revise only the affected state delta.

Keep the baseline internal by default. Persist it only when approved project calibration makes it genuinely useful for reproducibility; do not create a family database or new canonical manifest.

## Prompt architecture

Write concise natural language using the audible event first. Include only detail that changes the sound.

Preferred structure:

```text
<EVENT + SOURCE>
+ <MATERIAL / MECHANISM>
+ <TEMPORAL SHAPE>
+ <SPACE / PERSPECTIVE>
+ <CHARACTER / INTENSITY when useful>
```

Example shape:

```text
Heavy wooden crate hitting concrete,
dense dry wood impact with a short splinter rattle,
close perspective,
hard transient with short natural decay.
```

For `STATE_VARIANT`, preserve the shared family descriptors that anchor identity and change only the audible delta required by that state.

For `SEQUENCE`, describe audible progression directly:

```text
mechanical startup click → rising motor whine → stable low hum
```

Avoid:

- story/lore prose that does not alter the audio;
- implementation instructions such as event names or code triggers;
- contradictory descriptors;
- unrelated events packed into one prompt;
- dialogue or narration text;
- redundant synonyms added only to make the prompt longer;
- excessive cinematic language for ordinary gameplay Foley;
- universal prompt templates that erase source-specific identity.

## Complex effects and layering

Use `LAYERED` only when materially different sound sources/events need independent control or one combined generation repeatedly becomes muddy.

```text
complex canonical SFX
→ identify distinct audible components
→ generate only useful components
→ compare/select component takes
→ layer/edit downstream
```

Examples of legitimate decomposition may include:

```text
large eruption
→ low pressure rumble
→ primary blast
→ rock/debris impacts
→ long environmental tail
```

The canonical AST requirement remains unchanged unless upstream project meaning explicitly requires independent deliverables.

## ElevenLabs settings policy

Current API baseline:

```text
Model: eleven_text_to_sound_v2
Duration: auto or 0.5–30 seconds on the API
Loop: false by default; true only for genuinely repeating/sustained assets
Prompt Influence: 0.3 default, range 0–1
```

Decision rules:

```text
Duration
├─ authoritative timing requirement exists → set intentional duration
└─ no material timing requirement            → auto

Loop
├─ asset is genuinely repeatable/sustained → true
└─ discrete / naturally ending effect       → false

Prompt Influence
├─ start near current default
├─ repeated under-adherence → raise deliberately
├─ result is too literal / useful variation collapses → lower deliberately
└─ never treat as a universal quality slider
```

Do not grid-search settings by ritual. Change a setting only when the heard defect gives a reason.

Product UI and API limits may differ; current API contract is authoritative for API execution. Re-verify the active ElevenLabs surface if its controls conflict with this document.

## Execution boundary

PRD-Creator owns project meaning and SFX production judgment. The execution adapter owns current API/SDK/CLI mechanics.

When the official ElevenLabs agent skill `sound-effects` is available, use it as the preferred execution reference for current SDK/CLI syntax, parameters, output formats, and API error handling:

```text
PRD-Creator Production Assets
→ SOUND-EFFECTS.md: intent / continuity / prompt / candidate strategy / approval logic
→ ElevenLabs `sound-effects` executor: API mechanics
→ generated audio evidence
```

Do not copy the ElevenLabs SDK into PRD-Creator, add it to the core runtime lock, or create an API wrapper solely to reproduce an execution skill that already exists. Keep `ELEVENLABS_API_KEY` and other credentials outside the repository.

If the official execution skill is unavailable, use the current official ElevenLabs Sound Effects API/SDK documentation directly without changing PRD-Creator's semantic ownership.

## Candidate iteration

ElevenLabs output is generative. Freeze the initial comparison unit so candidate review is meaningful:

```text
prompt
model
requested duration / auto
loop
prompt influence
output format when material
family baseline / state delta when applicable
```

Then:

```text
reviewed configuration
→ generate / compare same-configuration candidates
→ repeated defect?
   no  → choose best acceptable candidate
   yes → diagnose first wrong owner
```

Do not require a ritual number of takes. Use the variants already available before spending another generation when they provide enough evidence.

After a repeated defect is established, change **one variable class at a time**:

```text
prompt wording
OR duration / temporal target
OR prompt influence
OR loop behavior
OR family baseline / state delta
OR decomposition / layering
```

Changing several classes at once destroys causal evidence and wastes generation budget.

## Candidate selection

Compare candidates on the audible job, not on novelty:

```text
source identity
material / mechanism
transient + temporal shape
space / perspective
family continuity when applicable
artifacts
editability / loopability when required
```

Do not persist a numeric scorecard. Select the strongest take or state the first repeated defect that justifies revision.

## SFX Production Readiness

Review current scope once. This is a conceptual gate, not a persisted schema or score.

| Lens | Ready when... |
|---|---|
| Intent Conservation | Required event/use/timing truth is preserved; unsupported meaning was not added. |
| Source Identity | The intended source is unambiguous enough to generate. |
| Material / Mechanism | Material or mechanism is directed only as specifically as the requirement needs. |
| Temporal Shape | Attack, sustain, sequence, decay, or stop behavior is intentional when material. |
| Space / Perspective | Distance/environment is controlled when it changes gameplay/readability. |
| Family Continuity | Recurring source identity has a stable baseline and state deltas do not drift. |
| Loop Intent | Loop is enabled only when the asset genuinely needs seamless repetition. |
| Complexity | Layering is used only when one generation cannot cleanly represent distinct components. |
| Operator | Exact prompt, model, relevant settings, and generation mode are usable without guessing. |

Conceptual result:

```text
SFX Production Readiness: PASS | FAIL
```

A preparation PASS means **ready to generate**, not that final audio quality has been approved.

## Heard-problem routing

| Heard problem | First action |
|---|---|
| wrong source / wrong event | return to Audio Brief / Production Assets meaning |
| correct event, wrong material/mechanism | revise the smallest prompt phrase |
| correct identity, wrong temporal shape | prompt temporal wording or intentional duration |
| state sounds like a different source | family baseline / state delta |
| repeatedly ignores important descriptor | prompt wording, then Prompt Influence if wording is already sound |
| too literal / useful variation collapses | lower Prompt Influence deliberately |
| one isolated strange take | compare/regenerate same configuration first |
| repeated artifacts across candidates | simplify/clarify prompt or decompose when the sound is genuinely complex |
| complex result is muddy | `LAYERED` decomposition |
| loop seam / repeated texture unsuitable | verify Loop intent + regenerate/listen |
| ambience feels static or obviously tiled | prompt temporal texture + loop candidate review |
| requested duration is wrong | timing truth / duration target before adding prompt clutter |

Do not repair an upstream requirement defect by making the SFX prompt increasingly complicated.

## Output and evidence

Keep generation evidence minimal and reproducible when useful:

```text
AST ID
exact prompt
model
surface / executor
requested duration or auto
loop
prompt influence
output format when material
selected candidate/take
actual measured duration when measured
```

For downstream editing/mastering, prefer an uncompressed/high-quality output when the active surface and project workflow support it. Container/file wrapping such as WAV packaging is downstream tooling, not SFX semantic policy.

Generation evidence is not a replacement for `work/asset-requirements.md`.

## Approval lock

When the user approves an actual generated SFX:

1. preserve exact prompt/settings when reproducibility evidence is retained;
2. preserve family baseline behavior for related approved states when it proved materially useful;
3. record measured duration only from the actual file;
4. treat approved sound behavior as same-project calibration, not a universal prompting rule;
5. revise only invalidated related states after a family-level correction;
6. do not rewrite `work/asset-requirements.md` unless approved project meaning changed.

## Proof economy / stop rule

Preparation stops when:

```text
required audible meaning is conserved
+ smallest useful SFX mode is chosen
+ family continuity is sufficient when applicable
+ exact prompt/settings are operator-ready
+ SFX Production Readiness = PASS
```

Generation stops when the requested sound has an acceptable heard candidate and sufficient evidence for the requested delivery.

Do not add schemas, SFX databases, candidate scorecards, fixed take counts, generic preset libraries, new AST IDs for temporary layers, SDK/runtime dependencies, or a new root workflow/skill after the requested scope is already correct.

## Current official references

Last verified: **2026-09-09**

- `https://elevenlabs.io/docs/overview/capabilities/sound-effects`
- `https://elevenlabs.io/docs/eleven-creative/playground/sound-effects`
- `https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert`
- `https://elevenlabs.io/docs/eleven-api/guides/cookbooks/sound-effects`
- `https://github.com/elevenlabs/skills/tree/main/sound-effects`

When live product controls or official API contracts conflict with this procedure, re-verify the active surface before turning new behavior into durable repository policy.
