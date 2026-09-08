# Eleven v3 Performance Writing

Last verified: **2026-09-08**

Purpose: explain how spoken text, punctuation, and Audio Tags cooperate in Eleven v3. Expression architecture lives in `v3-expression-direction.md`; stiffness/narration craft lives in `v3-naturalness.md`.

## Core order

```text
meaning/context
→ suitable voice
→ spoken wording
→ thought-group architecture
→ Expression Coverage
→ punctuation / line structure
→ precise Audio Tags
→ continuity context / generation
```

Do not repair flatness with tag spam, and do not repair over-direction by deleting expression-critical tags.

# 1. Spoken wording

Write what the approved speaker would plausibly say at the approved trigger.

Prefer:

- one main idea/action per thought group;
- active spoken verbs;
- listener-first information order;
- context-aware references;
- sentence-length variation;
- exact approved terminology where needed;
- a clear final landing.

The text should remain understandable with tags removed. That does **not** mean the intended acting must remain fully specified without tags.

# 2. Thought-group architecture

Possible beat functions:

```text
establish
reveal
observe
react
warn
instruct
escalate
recover
acknowledge
payoff
farewell
```

Use scene/thought changes—not sentence count—to decide performance changes.

# 3. Text controls

## Punctuation

- `,` keeps related material moving;
- `.` completes a thought/reset;
- `?` creates questioning contour;
- `!` increases textual intensity;
- `—` creates pivot/interruption;
- `…` creates hesitation/suspense/trailing weight.

## CAPS

Use sparingly for contrast.

## Line/paragraph structure

Use line breaks for readable thought groups. A newline is not an exact pause timer.

## Natural irregularity

Contractions, fragments, restarts, repetition, hesitation, discourse markers, or stretched words are optional expressive writing devices, not a checklist.

# 4. Audio Tags are first-class acting direction

Current Eleven v3 guidance explicitly uses Audio Tags for emotional control, delivery, pacing, reactions, and other vocal behavior.

Core categories:

```text
Emotion
→ [sad] [angry] [excited] [curious] ...

Attitude / subtext
→ [sarcastic] [mischievously] [matter-of-fact] ...

Projection / delivery
→ [whispers] [shouts] [softly] ...

Pace / rhythm
→ [rushed] [slowly] [drawn out] [pause] ...

Human reactions
→ [laughs] [sighs] [exhales] [gulps] ...

Character/accent candidates
→ use only when approved and voice-compatible
```

Tags are natural-language instructions, not a closed enum. Prefer concise audible directions.

# 5. Tag authority levels

## Official/documented-style

Prefer known current patterns when sufficient.

## Descriptive candidate

The vocabulary is non-exhaustive. Concise cues such as `[restrained excitement]`, `[building urgency]`, or `[guarded]` may be used when they describe an audible state and are supported by scene/character context.

## Project-calibrated

A cue repeatedly proven with the same project/voice/settings becomes stronger local evidence.

Priority:

```text
simple reliable cue
→ concise descriptive cue
→ project calibration
```

# 6. Opening direction

There is no syntax rule requiring every prompt to start with a tag.

Craft rule:

```text
material opening acting state
→ anchor with explicit direction

no material opening state beyond voice/text baseline
→ zero-tag opening valid
```

Examples:

```text
[whispers]
Don't turn around.
```

versus:

```text
The chamber's open. Go in.
```

# 7. Placement and transitions

Place direction close to the beat it affects.

```text
[reflective]
I thought this place was empty.

[uneasy]
Then I heard someone breathing.
```

Do not assume a documented fixed tag persistence window. Re-anchor when a material state changes or when a new generation request must reliably start in a particular state.

# 8. Tag combinations

ElevenLabs permits combinations.

Repository heuristic:

```text
1 tag               → preferred when sufficient
2 simultaneous tags → compatible independent dimensions
3+                  → exceptional / calibrated / concrete need
```

Good:

```text
[nervous][quietly]
Don't move.
```

Weak:

```text
[excited][energetic][enthusiastic][intense]
Let's go!
```

# 9. Reactions are events

```text
I thought we'd lost it.
[sighs]
Okay. It's still responding.
```

Do not front-load all reactions as one tag cluster.

# 10. Narration direction

Design the narrative performance arc first:

```text
orientation
→ curiosity
→ reveal
→ unease
→ urgency
→ resolution
```

Then place tags at meaningful state anchors/transitions.

Too many tags:

```text
tag every sentence
```

Too few tags:

```text
important emotional arc left entirely to inference
```

Target:

```text
natural prose
+ explicit state anchors
+ explicit transitions
+ sparse justified reactions
```

# 11. Dialogue direction

Text to Dialogue accepts tags inside each turn's text. Keep the tag in the turn it affects.

```text
[annoyed] You knew about this?
[defensive] I only found out this morning.
[interrupting] Then why didn't you tell me?
```

Use dialogue tags for emotional interplay, interruption, overlap, whispering, reactions, and turn-specific acting—not as a substitute for distinct Voice IDs.

# 12. Pauses and pacing

Eleven v3 does not support SSML `<break>`.

Use:

- punctuation;
- ellipses;
- em dashes;
- line structure;
- `[pause]`, `[rushed]`, `[slowly]`, `[drawn out]`, or other appropriate Audio Tags when explicit pacing direction matters.

Do not invent exact milliseconds from tags.

# 13. Pronunciation

```text
ordinary word → normal text
ambiguous token → explicit spoken form
unusual proper noun → native v3 IPA when needed
repeated project term → pronunciation dictionary/note when useful
```

# 14. Voice matching

Tag effectiveness is voice-dependent.

Before increasing direction complexity, confirm the voice can plausibly perform the required emotional/projection/pacing range.

A serious restrained voice may not respond well to playful cues; a soft voice may not become a convincing shout actor solely through `[shouts]`.

# 15. Stability interaction

For maximum expression with Audio Tags, current ElevenLabs guidance favors Creative or Natural. Robust is less responsive to directional prompts.

Repository default remains Natural.

# 16. Enhance

ElevenLabs Enhance can automatically add Audio Tags and emphasis. SoundMaker-reviewed prompts keep Enhance OFF by default because SoundMaker already owns communication + expression direction. Any Enhance rewrite becomes a new draft requiring review.

# 17. Pre-generation check

Before returning to SoundMaker:

- spoken wording is natural;
- thought groups are clear;
- material expression is identified;
- expression-critical states have sufficient explicit direction;
- opening state is anchored when needed;
- transitions/reactions are placed at the correct beat;
- tag combinations are compatible/non-redundant;
- punctuation/CAPS cooperate with, rather than duplicate, tag intent;
- the chosen voice can perform the requested range;
- no SSML `<break>` exists;
- no invented tag persistence rule is assumed.
