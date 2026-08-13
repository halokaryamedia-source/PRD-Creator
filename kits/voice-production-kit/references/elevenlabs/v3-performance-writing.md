# Eleven v3 Performance Writing

Purpose: explain how text itself directs Eleven v3. This is a deep reference for `SOUNDMAKER.md`, not a second execution workflow.

## Core order

```text
meaning/context
→ spoken wording
→ beat architecture
→ punctuation / line structure
→ selective emphasis
→ Audio Tags
```

A flat script should not be repaired by tag stacking.

## 1. Spoken wording

Write what a person would naturally say at the approved trigger, not what a PRD would document.

Prefer:

- one main idea/action per beat;
- active spoken verbs;
- progressive information order;
- enough context for emotional changes to make sense;
- short enough sentences for important thoughts to land.

Avoid:

- specification sentences with several critical instructions;
- hidden implementation detail;
- repeated full objective briefings;
- filler added only to consume duration.

The script should remain understandable with all Audio Tags removed.

## 2. Beat architecture

A beat is a short unit with one dominant communication/performance purpose.

Possible functions:

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

For long-form performance, let scene changes create performance changes. Do not assign new emotion simply because a new sentence begins.

Useful anti-flatness checks:

- important instructions are not buried in one long sentence;
- adjacent beats do not all use the same sentence shape;
- setup, escalation, and landing have audible contrast when the scene contains those phases;
- the final important thought has a clean landing;
- calm explanatory content is not forced into artificial excitement.

## 3. Non-tag controls

ElevenLabs documents text structure, punctuation, and capitalization as material v3 controls.

### Standard punctuation

Use punctuation semantically, not as exact milliseconds:

- `,` — keep related material in one thought;
- `.` — complete thought / new beat;
- `?` — real or rhetorical questioning contour;
- `!` — textual intensity/assertiveness;
- `—` — hard pivot/interruption/dramatic break;
- `...` / `…` — hesitation, suspense, weight, softer pause.

### CAPS

Capitalization can increase emphasis.

Good:

```text
We need it NOW.
DO NOT touch that switch.
```

Avoid whole paragraphs in CAPS. Contrast disappears when everything is stressed.

### Line / paragraph structure

Use line breaks to make phrasing and beat boundaries legible. A newline is not an exact-duration pause command.

### Repetition / restart

Sparse repeated wording can communicate panic, disbelief, or hesitation:

```text
No. No, no—MOVE!

I... I don't know.
```

Treat this as expressive writing, not a universal control.

### Letter stretching

Forms such as `Sooo...` can produce drawn-out speech on some voices. Treat them as voice-dependent expressive spelling and prefer project-calibrated use.

## 4. Audio Tag status

Do not treat every plausible bracketed phrase as equally established.

### A. Documented / official examples

Examples directly demonstrated in current ElevenLabs v3 guidance include patterns such as:

```text
[laughs]
[whispers]
[sighs]
[exhales]
[sarcastic]
[curious]
[excited]
[crying]
[snorts]
[mischievously]
```

These are the safest starting vocabulary when they match the voice and scene.

### B. Descriptive candidate

ElevenLabs says the tag vocabulary is non-exhaustive and encourages descriptive emotional states/actions. Therefore cues such as:

```text
[building urgency]
[guarded]
[restrained excitement]
```

may be useful, but they are **candidates**, not guaranteed exact commands. Keep them simple and audible.

### C. Project-calibrated

A custom direction that repeatedly works for the same project/voice/settings becomes stronger local evidence for that production.

Priority:

```text
simple documented cue when sufficient
→ descriptive candidate when needed
→ project-calibrated behavior for repeated production
```

Never claim a descriptive candidate is an official exact tag unless the source actually documents it.

## 5. Tag dimensions

| Dimension | Examples | Purpose |
|---|---|---|
| Emotion | `[nervous]`, `[excited]` | dominant feeling |
| Tone / attitude | `[sarcastic]`, `[mischievously]` | stance/subtext |
| Projection | `[whispers]`, `[shouts]` | vocal presence |
| Pace / rhythm | descriptive or calibrated pacing cues | local tempo/landing |
| Cognitive beat | `[hesitates]`, pause-like cues | thought/rhythm event |
| Human reaction | `[sighs]`, `[laughs]`, `[gulps]` | non-verbal event |
| Character / accent | voice-dependent descriptive cue | presentation/identity |

Do not use non-auditory stage directions such as `[standing]` or `[looking worried]` as voice-performance instructions.

## 6. Tag placement and persistence

Current v3 guidance supports moment-to-moment/mid-delivery direction and strategic placement near the dialogue it affects.

Standard Speech Synthesis v3 does **not** document a fixed persistence rule such as:

```text
one tag = exactly N words
one tag = active until next tag
```

Therefore:

- place a direction directly near the beat it should shape;
- add a new direction only when performance state materially changes;
- do not repeat the same tag every sentence without reason;
- do not transfer tag-scope numbers from another ElevenLabs product surface into normal Speech Synthesis.

## 7. Tag stacking

ElevenLabs allows combinations, but does not publish an ideal simultaneous count.

Repository heuristic:

```text
0–1 tag → default
2 tags   → normal when dimensions differ and are compatible
3 tags   → exception / preferably project-calibrated
4+ tags  → reject by default
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

Do not use contradictory direction stacks unless an intentionally unusual result has already been approved for the project.

## 8. Reactions are timeline events

Prefer sequencing a reaction at the point where it happens:

```text
[nervous][quietly]
I think something is coming...

[gulps]

Don't move.
```

rather than placing every reaction inside one large tag cluster.

## 9. Long-form emotional movement

For a long narration, use several meaningful beats instead of one global mood tag.

Example shape:

```text
reflective setup
→ quiet reveal
→ curiosity
→ unease
→ urgency
→ firm instruction
```

The exact tags are secondary. What matters is that performance movement follows scene movement.

## 10. Pauses: v3-specific rule

Eleven v3 does **not** support SSML `<break>` tags.

For v3, use:

- natural punctuation;
- ellipses;
- em dashes;
- line/text structure;
- appropriate pause/reaction cues when a pause is a real performance event.

## 11. Numbers, acronyms, symbols, spelling

For predictable production speech, write ambiguous items the way they should be spoken:

```text
50% → fifty percent
$100 → one hundred dollars
15 sec → fifteen seconds
```

Proofread. Misspellings may be pronounced rather than silently corrected.

For material proper nouns, route to `v3-production-reference.md` for IPA/dictionary guidance.

## 12. Pre-generation writing check

Before returning to SoundMaker:

- spoken wording is natural;
- every important beat has a clear function;
- emotional changes have a scene reason;
- punctuation/CAPS are intentional;
- tags are audible, compatible, and minimal;
- documented vs descriptive/custom tag status is understood;
- no SSML `<break>` exists;
- the prompt does not rely on an invented tag-persistence rule.
