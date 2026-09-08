# Eleven v3 Performance Writing

Last verified: **2026-09-08**

Purpose: explain how the **spoken text itself** directs Eleven v3. This is a deep reference for `../PERFORMANCE-WRITING.md`, not a second execution workflow.

Naturalness/stiffness diagnosis lives in `v3-naturalness.md`.

## Core order

```text
meaning/context
→ suitable voice baseline
→ spoken wording
→ thought-group / beat architecture
→ continuity context when needed
→ punctuation / line structure
→ selective emphasis
→ Audio Tags only when needed
```

A flat or stiff script should not be repaired by tag stacking.

# 1. Spoken wording

Write what a person would naturally say at the approved trigger, not what a PRD would document.

Prefer:

- one main idea/action per thought group;
- active spoken verbs;
- progressive, listener-first information order;
- context-aware references where the listener already knows the subject/location;
- sentence-length variation driven by thought complexity;
- enough context for emotional changes to make sense;
- short enough phrases for important thoughts to land;
- exact approved terminology only where needed.

Avoid:

- specification sentences with several critical instructions;
- repeated trigger/context exposition;
- hidden implementation detail;
- repeated full objective briefings;
- filler added only to consume duration or imitate humanity;
- mechanically formal connective language unless it belongs to the character.

The script should remain understandable and performable with all Audio Tags removed.

# 2. Thought-group / beat architecture

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

Useful checks:

- important instructions are not buried in one long sentence;
- adjacent beats do not all use the same sentence shape;
- setup, escalation, and landing have audible contrast only when the scene contains those phases;
- the final important thought has a clean landing;
- calm explanatory content is not forced into artificial excitement;
- direct dialogue responds to the current situation rather than narrating it back to the listener.

For long-form performance, let story/scene changes create performance changes. Do not assign a new emotion simply because a new sentence begins.

# 3. Natural spoken irregularity

Natural speech does not mean deliberately adding mistakes.

Optional devices include:

- contractions;
- sentence fragments;
- restart/repetition;
- hesitation;
- discourse markers;
- stretched words;
- asymmetric sentence lengths.

Use them only when they fit the speaker, language, and moment.

Bad heuristic:

```text
every line must contain filler / hesitation / ellipses to sound human
```

Better rule:

```text
use the smallest amount of spoken irregularity that naturally follows the speaker's thought
```

A polished narrator or concise radio operator may sound highly controlled and still fully human.

# 4. Non-tag controls

ElevenLabs documents text structure, punctuation, capitalization, and emotional context as material v3 controls.

## Standard punctuation

Use punctuation semantically, not as exact milliseconds:

- `,` — keep related material in one thought;
- `.` — complete thought / reset;
- `?` — real or rhetorical questioning contour;
- `!` — textual intensity/assertiveness;
- `—` — hard pivot/interruption/dramatic break;
- `...` / `…` — hesitation, suspense, weight, trailing thought.

Repeated punctuation reduces contrast and can make performance stylized rather than natural.

## CAPS

Capitalization can increase emphasis.

Good:

```text
We need it NOW.
DO NOT touch that switch.
```

Avoid whole paragraphs or many adjacent key words in CAPS. Contrast disappears when everything is stressed.

## Line / paragraph structure

Use line breaks to make thought groups legible. A newline is not an exact-duration pause command.

For narration, preserve meaningful paragraph structure when possible instead of converting every sentence into an isolated clip.

## Repetition / restart

Sparse repeated wording can communicate panic, disbelief, correction, or hesitation:

```text
No. No, no—MOVE!

I... I don't know.
```

Treat this as expressive writing, not a universal control.

## Letter stretching

Forms such as `Sooo...` can produce drawn-out speech on some voices. Treat them as voice-dependent expressive spelling and prefer project-calibrated use.

# 5. Audio Tag status

Do not treat every plausible bracketed phrase as equally established.

## A. Documented / official examples

Examples demonstrated in current ElevenLabs v3 guidance include patterns such as:

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

These are safer starting vocabulary when they match the voice and scene.

## B. Descriptive candidate

ElevenLabs says the tag vocabulary is non-exhaustive and allows natural-language direction. Cues such as:

```text
[building urgency]
[guarded]
[restrained excitement]
```

may be useful, but they are **candidates**, not guaranteed exact commands. Keep them simple and audible.

## C. Project-calibrated

A custom direction that repeatedly works for the same project/voice/settings becomes stronger local evidence for that production.

Priority:

```text
no tag when voice + text already carry the delivery
→ simple documented cue when needed
→ descriptive candidate when needed
→ project-calibrated behavior for repeated production
```

Never claim a descriptive candidate is an official exact tag unless the source actually documents it.

# 6. Tag dimensions

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

# 7. Optional opening direction

A standalone Voice Production prompt is **not required** to begin with an Audio Tag.

Use a tag at the opening only when the intended opening delivery is materially under-specified by:

```text
selected voice baseline
+ spoken wording
+ punctuation/structure
+ immediate context
```

Zero-tag examples are valid when the line naturally carries its own performance:

```text
The door's open. Go.

You made it. I wasn't sure you would.
```

A tag can still be appropriate when an otherwise neutral line must begin in a specific audible state:

```text
[whispers]
Don't turn around.
```

Do not prepend generic tags such as `[calm]`, `[clear]`, `[natural]`, or `[conversational]` merely to satisfy a template.

# 8. Tag placement and persistence

Current v3 guidance supports moment-to-moment/mid-delivery direction and strategic placement near the dialogue it affects.

Standard v3 documentation does **not** define a fixed persistence rule such as:

```text
one tag = exactly N words
one tag = active until next tag
```

Therefore:

- place a direction directly near the beat it should shape;
- add a new direction only when performance state materially changes;
- do not repeat the same tag every sentence without reason;
- do not transfer tag-scope numbers from another ElevenLabs product surface into normal Speech Synthesis.

# 9. Tag stacking

ElevenLabs allows combinations but does not publish an ideal simultaneous count.

Repository naturalness heuristic:

```text
0 tags               → valid natural baseline
1 local tag          → normal when one audible dimension/event needs direction
2 simultaneous tags  → valid when dimensions differ and are compatible
3+ simultaneous tags → exception / preferably project-calibrated
```

Good when truly needed:

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

# 10. Reactions are timeline events

Prefer sequencing a reaction where it actually occurs:

```text
I think something is coming...

[gulps]

Don't move.
```

rather than placing every reaction inside one large opening tag cluster.

# 11. Emotional context from text

ElevenLabs documents that textual emotional context affects delivery. Use this before adding directions that merely restate obvious meaning.

Natural urgency can come from:

- shorter clauses;
- direct verbs;
- cut-offs/interruption structure;
- information order;
- contrast;
- an isolated landing.

Example:

```text
Move. Now.
```

may already provide enough urgency for a suitable voice. Add a tag only if a more specific performance state is genuinely needed.

Do not insert spoken prose such as `she said sadly` into a game line merely to steer emotion unless those words are intended to be heard.

# 12. Narration

For long narration, use meaningful prose movement instead of one direction tag per sentence.

A possible shape:

```text
reflective setup
→ concrete observation
→ reveal
→ implication
→ emotional turn
→ clean landing
```

Guidance:

- keep the narrator's baseline voice stable;
- vary sentence length according to the thought;
- use fewer, more meaningful local directions;
- avoid ellipses at every reflective beat;
- do not convert every sentence into a separate emotional state;
- preserve paragraph/scene context during generation when continuity matters.

The exact tags are secondary. Performance movement should follow narrative movement.

# 13. Connected speech context

When separate same-speaker TTS generations form one continuous narration, keep canonical prompts separate but provide generation context when supported:

```text
previous_text / next_text
→ surrounding canonical spoken text

previous_request_ids / next_request_ids
→ adjacent generated clips, especially for regeneration
```

This improves continuity without adding filler or duplicate audible wording.

For multi-speaker response-dependent scenes, use Text to Dialogue instead.

# 14. Pauses: v3-specific rule

Eleven v3 does **not** support SSML `<break>` tags.

For v3, use:

- natural punctuation;
- ellipses sparingly;
- em dashes for real pivots/cut-offs;
- line/text structure;
- appropriate pause/reaction tags only when the pause/reaction is itself a real performance event.

# 15. Numbers, acronyms, symbols, spelling

For predictable production speech, write ambiguous items the way they should be spoken:

```text
50% → fifty percent
$100 → one hundred dollars
15 sec → fifteen seconds
```

Proofread. Misspellings may be pronounced rather than silently corrected.

For material proper nouns, route to `v3-production-reference.md` for IPA/dictionary guidance.

# 16. Pre-generation writing check

Before returning to SoundMaker:

- spoken wording is natural for the speaker/register;
- every important thought group has a clear function;
- adjacent beats are not mechanically identical;
- context is not needlessly repeated;
- contractions/fragments/filler are used only when justified;
- emotional changes have a scene reason;
- punctuation/CAPS are intentional and not dense;
- tags are optional, audible, compatible, and minimal;
- the prompt does not rely on an invented tag-persistence rule;
- connected narration has a continuity plan when separate generation would otherwise sound detached;
- no SSML `<break>` exists;
- the line remains clear when all optional Audio Tags are mentally removed.