# Eleven v3 Expression Direction

Last verified: **2026-09-08**

Purpose: preserve intended acting, emotion, subtext, pacing, projection, and reactions in Eleven v3 without returning to boilerplate tag spam. This is a craft reference for `../PERFORMANCE-WRITING.md`, not a new workflow, schema, scorecard, or source of project meaning.

## Core principle

```text
natural spoken wording
+ suitable voice
+ deliberate expression direction
+ contextual continuity
= target performance
```

Audio Tags are a **first-class acting control** in Eleven v3. They are not mandatory syntax for every line, but they are required whenever a material performance state would otherwise be left ambiguous or under-directed.

The goal is not `fewest tags`. The goal is **complete expression coverage with the least redundant direction**.

# 1. Expression Coverage Map

For each Voice ID, reason internally over only the dimensions that matter:

```text
Baseline State
→ neutral / calm / tense / excited / reflective / other approved state

Emotion
→ what is felt?

Attitude / Subtext
→ how does the speaker relate to the listener or situation?

Projection
→ whisper / intimate / normal / projected / shout / other audible presence

Pace / Rhythm
→ measured / hesitant / rushed / interrupted / drawn-out / other material rhythm

Intensity / Energy
→ restrained / normal / building / high / falling / exhausted / other material level

Cognitive State
→ certain / doubtful / surprised / processing / disbelieving / other material thought-state

Reaction Event
→ sigh / laugh / gasp / gulp / inhale / exhale / other audible reaction

Transition Points
→ where does any material state change?

Landing
→ what final idea, action, emotion, or result must land?
```

Do not persist this map into a second artifact. It is a reasoning instrument over the current Voice requirement and approved speaker/scene context.

# 2. Performance classes

Classify each prepared line/beat conceptually:

## Natural Baseline

Use when there is no material acting direction beyond the selected voice's normal register and the spoken text itself carries the intended meaning.

```text
The chamber's open. Go in.
```

Zero tags may be correct here.

## Directed Static

Use when one stable performance state materially matters across the line.

```text
[whispers]
Don't turn around.
```

If the intended whisper, sarcasm, nervousness, relief, restraint, or other audible state is important, do not leave it to chance merely because the wording is natural.

## Directed Dynamic

Use when the acting state changes during the line or narration.

```text
[reflective]
I thought this place was abandoned.

[uneasy]
Then the lights came back on.

[urgent]
We need to move. Now.
```

Direction follows the emotional/narrative transition, not every sentence boundary.

## Reaction Event

Use a reaction tag at the point where the reaction happens.

```text
I really thought we lost it.
[sighs]
Okay. We're still here.
```

Reactions are timeline events, not decoration.

# 3. Expression-source priority

Material expression may come from:

1. explicit approved speaker/character direction;
2. explicit scene/Voice requirement context;
3. communication function and listener state when the acting implication is necessary to perform the approved moment correctly;
4. established approved same-project performance behavior.

SoundMaker may make reversible craft interpretations such as `restrained`, `warming`, or `building urgency` when they are supported by approved context. It may not invent a new personality, accent, emotional relationship, or character identity merely to make a line more colorful.

# 4. Direction-coverage rule

For every material expression dimension, ask:

```text
Is this performance requirement sufficiently explicit in the selected voice + spoken wording + punctuation + immediate context?
```

If **yes**, no redundant tag is required.

If **no**, add a precise Audio Tag close to the beat it must control.

If the expression is **critical** to the intended acting—emotion, subtext, projection, pacing, reaction, or a state transition—prefer explicit direction rather than hoping v3 infers the same interpretation from text alone.

Examples:

```text
ambiguous text + required relief
→ [relieved]

neutral wording + required whisper
→ [whispers]

same sentence changes from confidence to fear
→ place the transition tag at the fear beat

visible success acknowledgement with no special acting requirement
→ zero tag can remain valid
```

# 5. Tag selection hierarchy

Prefer the smallest reliable direction:

```text
simple documented/official-style cue
→ concise descriptive cue when needed
→ project-calibrated custom cue when repeatedly proven
```

Good cues describe something audible:

- emotion: `[excited]`, `[sad]`, `[curious]`;
- attitude/subtext: `[sarcastic]`, `[mischievously]`, `[matter-of-fact]`;
- projection: `[whispers]`, `[shouts]`, `[softly]`;
- pacing/rhythm: `[rushed]`, `[slowly]`, `[pause]`, `[drawn out]`;
- reactions: `[laughs]`, `[sighs]`, `[gasps]`, `[gulps]`;
- narrative state: `[reflective]`, `[awe]`, `[serious tone]` when useful and voice-compatible.

Do not use non-auditory stage directions such as `[standing]`, `[looking worried]`, or `[walking away]`.

# 6. Tag combination rule

ElevenLabs allows tag combinations. Repository policy is about redundancy, not arbitrary prohibition.

```text
1 tag
→ preferred when one direction is sufficient

2 simultaneous tags
→ valid when they control different compatible dimensions

3+ simultaneous tags
→ exceptional; use only when simpler direction cannot represent the approved performance or project calibration proves it useful
```

Good:

```text
[nervous][quietly]
I don't think we're alone.
```

Weak:

```text
[excited][energetic][enthusiastic][intense]
Let's go!
```

Do not stack synonyms. Do not stack contradictory states unless the contradiction itself is an approved creative choice.

# 7. Opening direction rule

A prompt does **not** mechanically require an opening tag.

However, when the opening state materially matters, establish it explicitly at the opening.

```text
material opening state
→ opening direction required by craft

no material opening state beyond voice/text baseline
→ zero-tag opening valid
```

This is the key distinction between `mandatory tag syntax` and `mandatory expression coverage`.

# 8. Transition direction rule

When a performance state changes materially:

```text
old state
→ scene/thought/reaction changes
→ new tag immediately before the affected beat
```

Do not add a new emotion merely because a new sentence begins.

Do not assume one tag has a documented fixed persistence window. Re-anchor when the change is material or when a generation boundary makes continuity uncertain.

# 9. Generation-boundary rule

Treat each new TTS request as a possible performance reset.

For connected same-speaker narration:

```text
previous_text / next_text or neighboring request IDs
→ preserve contextual prosody

material acting state still required at the next clip opening
→ re-anchor that state explicitly in the next canonical prompt when necessary
```

Context helps continuity but is not a substitute for explicit acting direction when the next clip must reliably begin in a particular state.

Do not repeat a tag merely because two files are adjacent; repeat it only when the new generation needs that acting state established again.

# 10. Narration architecture

For narration, design the emotional arc before choosing tags.

Example:

```text
orientation
→ curiosity
→ reveal
→ unease
→ urgency
→ resolution
```

Then place direction only at meaningful state changes.

Avoid both extremes:

```text
tag every sentence
→ over-directed / synthetic risk

no tags anywhere
→ important emotional arc may be left to inference
```

Correct target:

```text
natural prose
+ explicit state anchors
+ explicit transitions
+ sparse reactions
```

# 11. Dialogue architecture

For response-dependent multi-speaker moments, use Text to Dialogue and preserve each existing VO prompt as its turn.

Each turn may carry its own acting direction:

```text
Speaker A: [annoyed] ...
Speaker B: [defensive] ...
Speaker A: [interrupting] ...
```

Use tags inside the turn they should affect. Do not create a separate dialogue-direction schema.

Interruption, overlap, whispering, laughter, and reaction cues belong near the turn/beat where they happen.

# 12. Voice-fit boundary

Audio Tags cannot reliably force a voice far outside its performance envelope.

Before escalating tag complexity, verify:

```text
voice identity/timbre
baseline energy
emotional range
projection range
cadence/pacing
language/accent compatibility
```

For expression-heavy work, prefer voices with enough emotional range. A naturally restrained voice may not become a convincing shout actor through `[shouts]` alone.

# 13. Stability coupling

Repository baseline remains:

```text
Stability: Natural
```

Use:

- **Natural** for balanced expressive control;
- **Creative** when greater emotional range/variance is intentionally needed and the voice/prompt are already sound;
- **Robust** when consistency matters more than directional responsiveness.

For expression-critical prompts, do not move to Robust casually because current ElevenLabs guidance says Robust is less responsive to directional prompts.

# 14. Punctuation and tags cooperate

Do not make tags do all the work.

```text
spoken wording
→ thought groups
→ punctuation / line structure
→ explicit Audio Tags for acting states/transitions
→ Stability only as generation behavior control
```

Punctuation provides rhythm and emphasis. Audio Tags provide explicit acting direction. They are complementary controls.

# 15. Expression Conservation gate

A prepared line passes Expression Conservation when:

- every material approved/derived acting state has enough direction;
- material emotion/subtext/projection/pacing/reaction is not accidentally lost during natural-language rewrite;
- every material state transition is represented by wording/context and, when needed, an explicit tag near the transition;
- no tag contradicts approved meaning or speaker identity;
- no expression is added merely to make the line more dramatic;
- no redundant tag stack fights the voice/text;
- connected clips preserve the intended emotional arc across generation boundaries;
- the final landing remains clear.

Expression Conservation is part of Voice Script Readiness. Do not create a new persisted acceptance field solely for it.

# 16. Diagnostic order

If prepared output risks sounding flat or losing expression:

```text
missing/ambiguous expression intent?
→ expression coverage
→ tag placement / state transitions
→ spoken wording / thought groups
→ voice fit
→ Stability
→ generation surface/context
```

If output risks sounding synthetic or overacted:

```text
synonymous/redundant tags
→ repeated re-anchoring without need
→ punctuation/CAPS overload
→ voice mismatch
→ Stability too loose
```

Do not solve `flat` with tag spam and do not solve `overacted` by deleting every tag.

# 17. Preparation stop rule

Preparation is complete when:

```text
Communication Conservation = PASS
Naturalness = PASS
Expression Conservation = PASS
Voice Script Readiness = PASS
```

No generated-audio quality claim is made until actual audio is heard.
