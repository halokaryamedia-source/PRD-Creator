# Eleven v3 Performance Writing

Purpose: convert correct Voice Requirements into speech that sounds performed rather than read.

This page focuses on **how the text itself directs Eleven v3**. Audio Tags are only one layer.

## Core rule

For expressive long-form voice, build performance in this order:

```text
meaning/context
→ spoken wording
→ beat architecture
→ punctuation / line structure
→ selective emphasis
→ Audio Tags
→ voice + Stability
```

A flat script should not be repaired by tag stacking.

## 1. Spoken wording before directing

Write what a person would naturally say at that trigger, not what a PRD would document.

Prefer:

- one main idea/action per beat;
- active spoken verbs;
- progressive information order;
- short enough sentences to give important thoughts their own landing;
- context that gives an emotional change a reason to happen.

Avoid:

- long specification sentences containing multiple instructions;
- narration of hidden implementation state;
- repeating complete objective text in several Voice moments;
- adding emotional wording that changes the project fact.

### Flat

```text
The engine has restarted and the western gate is beginning to close so you need to cross the chamber and restore the second connection before the system locks down.
```

### Performance-ready

```text
The engine just restarted.

And the western gate is closing.

We don't have long.

Cross the chamber.
Restore the second connection—

before the system locks us in.
```

The second version already gives v3 more usable rhythm before any tag is added.

## 2. Performance beats

A beat is a short unit with one dominant communication/performance purpose.

Typical long-form arc:

```text
establish
→ reveal
→ react
→ escalate
→ instruct
→ payoff
```

Example emotional map:

```text
mysterious
→ curious
→ uneasy
→ urgent
→ commanding
→ relieved
```

Do not force every script to use this exact sequence. The beat map follows the scene.

### Anti-flatness gate

For an energetic or cinematic line, check:

- no single sentence carries several important instructions;
- adjacent beats do not all have the same sentence shape;
- the opening establishes a state;
- at least one meaningful change happens when the scene changes;
- the final beat has a clear landing;
- the script can still be understood if all Audio Tags are removed.

## 3. Non-tag controls

ElevenLabs explicitly documents capitalization, punctuation, and text structure as important v3 controls.

### Standard punctuation

**OFFICIAL-CURRENT:** standard punctuation provides natural speech rhythm.

Use punctuation semantically. Do not pretend punctuation maps to exact milliseconds.

Production interpretation:

- `,` — keep related material in one thought;
- `.` — finish a thought / create a new beat;
- `?` — preserve a real question or rhetorical questioning contour;
- `!` — add textual intensity/assertiveness;
- `—` — hard pivot/interruption/short dramatic break;
- `...` / `…` — hesitation, suspense, weight, or a softer pause.

ElevenLabs specifically documents ellipses as adding pauses/weight and dashes as a pause alternative. Dashes/ellipses are not exact timing controls.

### CAPS

**OFFICIAL-CURRENT:** capitalization increases emphasis in v3.

Use selective stress:

```text
We need it NOW.

DO NOT touch that switch.
```

Avoid full paragraphs in CAPS. If everything is emphasized, nothing has contrast.

### Line and paragraph structure

**OFFICIAL-CURRENT:** text structure strongly influences v3 output.

Use line breaks to make phrasing and beat boundaries legible. A newline is **not** an exact-duration pause command.

Useful pattern:

```text
Something moved.

Nobody touched it.

...we're not alone.
```

### Repetition / restarts

Repeated words can create panic, disbelief, hesitation, or self-correction:

```text
No. No, no—MOVE!

I... I don't know.
```

Treat this as expressive writing, not a universal control. Keep it natural and sparse.

### Letter stretching

Forms such as `Sooo...` can produce drawn-out speech on some voices and are demonstrated in ElevenLabs delivery material, but response is voice-dependent. Use only when the spelling itself represents intended speech and prefer project-calibrated evidence.

## 4. Audio Tag map

ElevenLabs' tag vocabulary is intentionally non-exhaustive. Prefer simple audible direction.

| Dimension | Examples | What it controls |
|---|---|---|
| Emotion | `[calm]`, `[nervous]`, `[excited]`, `[frustrated]` | dominant feeling |
| Tone / attitude | `[deadpan]`, `[playfully]`, `[reflective]`, `[matter-of-fact]` | stance/subtext |
| Projection | `[quietly]`, `[whispers]`, `[shouts]` | vocal presence/volume style |
| Pace / rhythm | `[rushed]`, `[slows down]`, `[drawn out]` | local tempo/landing |
| Cognitive beat | `[hesitates]`, `[stammers]`, `[pause]` | thought/rhythm event |
| Human reaction | `[sigh]`, `[laughs]`, `[gasps]`, `[gulps]` | non-verbal vocal event |
| Narrative | `[awe]`, `[dramatic tone]`, `[continues softly]`, `[resigned]` | long-form storytelling shape |
| Character / accent | `[British accent]`, `[robotic tone]`, `[pirate voice]` | character presentation |

Do not use non-auditory stage directions such as `[standing]` or `[looking worried]` as voice-performance instructions.

## 5. Tag placement and persistence

**OFFICIAL-CURRENT:** tags can guide moment-to-moment/mid-delivery shifts and should be placed close to the segment they affect.

**UNKNOWN:** standard Speech Synthesis v3 does not document a fixed rule such as "one tag affects exactly 5 words" or "one tag remains active until the next tag".

Therefore:

- place a direction directly before the beat it should shape;
- add a new direction when the performance state materially changes;
- do not repeat the same tag every sentence without a reason;
- do not rely on an undocumented persistence window.

The separate Eleven v3 Conversational/Agents Expressive Mode documents an approximate 4–5-word tag scope, but that is a different product behavior and must not be transferred to normal Speech Synthesis as a rule.

## 6. Tag stacking

**OFFICIAL-CURRENT:** ElevenLabs allows tag combinations for complex emotional delivery.

ElevenLabs does **not** publish an ideal number of simultaneous tags.

Production heuristic:

```text
0–1 tag → default
2 tags   → normal when they control distinct compatible dimensions
3 tags   → exception / preferably project-calibrated
4+ tags  → reject by default
```

Good:

```text
[nervous][quietly]
Don't move.
```

Different dimensions: emotion + projection.

Good:

```text
[excited][rushed]
Get the core to the gate—NOW!
```

Different dimensions: emotion + pace.

Weak/redundant:

```text
[excited][energetic][enthusiastic][intense]
Let's go!
```

Do not combine contradictory directions such as `[calm][frantic]` or `[whispers][shouts]` unless an intentionally unusual result has already been project-calibrated.

## 7. Reactions are timeline events

Prefer sequencing reactions rather than stacking them into one direction cluster.

Better:

```text
[nervous][quietly]
I think something is coming...

[gulps]

Don't move.
```

Not preferred:

```text
[nervous][quietly][gulps]
I think something is coming.
```

A reaction such as a sigh, gasp, laugh, or gulp has a temporal position in the performance.

## 8. Long-form emotional movement

For a long narration, use several meaningful beats rather than one global mood tag.

```text
[reflective]
For centuries, the Vault kept this city alive.

Every clock.
Every gate.
Every machine.

[continues softly]
Then, one day...

it stopped.

[curious][quietly]
But listen.

Do you hear that?

[uneasy]
Something is moving down there.

[building urgency]
We need the Resonance Engine online—
FAST.

[firm]
Find the target.
Restore the connection.
```

The important part is not the tag count. It is that each change corresponds to a change in the scene or communicative function.

## 9. Pauses: v3-specific rule

**OFFICIAL-CURRENT:** Eleven v3 does **not** support SSML `<break>` tags.

For v3 use:

- natural punctuation;
- ellipses;
- dashes;
- line/text structure;
- appropriate Audio Tags such as `[pause]` when a pause is a real performance event.

Do not paste `<break time="..." />` into v3 prompts.

## 10. Numbers, acronyms, symbols, and spelling

For predictable production speech, write ambiguous items how they should be spoken:

```text
50% → fifty percent
$100 → one hundred dollars
15 sec → fifteen seconds
```

For acronyms, write the intended spoken form when ambiguity matters.

Proofread. ElevenLabs may attempt to pronounce misspellings rather than silently fix them.

Use pronunciation dictionaries/native v3 IPA for material project terms rather than repeatedly inventing phonetic hacks.

## 11. Final pre-generation gate

Before calling a v3 prompt ready:

- meaning and project facts are correct;
- spoken wording is natural;
- target duration budget is still plausible;
- every beat has a clear purpose;
- emotional changes have a scene reason;
- punctuation/CAPS are intentional;
- tags are audible, compatible, and minimal;
- no SSML break tag exists;
- material pronunciation risk is addressed;
- the prompt does not depend on unsupported tag-persistence assumptions.
