# Eleven v3 Candidate Iteration Discipline

Last verified: **2026-09-09**

Purpose: distinguish nondeterministic take variance from real prompt/voice/settings defects so SoundMaker does not rewrite correct scripts after one weak generation. This is Generation Mode guidance, not a candidate database or scorecard.

## Core principle

```text
reviewed prompt + intended voice + intended settings
→ same-content candidates/regenerations
→ compare defect pattern
→ change one variable class only when repeated evidence justifies it
```

ElevenLabs generation is nondeterministic. One weak take does not prove the canonical prompt is wrong.

## 1. Candidate-first rule

When a reviewed prompt produces one weak/glitched take:

```text
isolated defect
→ same prompt + same voice + same settings candidate/regeneration first
```

Current ElevenLabs dashboard behavior may allow up to two free regenerations when text and parameters remain exactly unchanged. API billing behavior differs, but the diagnostic principle remains the same.

## 2. Freeze the comparison unit

To learn anything from candidates, keep these fixed during the first comparison:

```text
canonical text
Audio Tags
voice_id
model
Stability/settings
language/pronunciation setup
surface
continuity context
```

If several of these change simultaneously, the result cannot identify the cause.

## 3. Classify the defect before editing

### Variance / artifact

Examples:

- one take has a pop/distortion;
- one word is oddly stressed once;
- one candidate has a random pause not repeated elsewhere.

Action: prefer the best same-content take.

### Expression defect

Examples:

- intended relief repeatedly sounds neutral;
- transition repeatedly fails at the same beat;
- reaction is consistently misplaced.

Action: Expression Coverage / tag placement.

### Writing/prosody defect

Examples:

- every candidate sounds like document prose;
- the landing is consistently buried;
- the sentence remains breathless across takes.

Action: spoken wording / thought groups.

### Voice-fit defect

Examples:

- actor repeatedly cannot reach required projection;
- accent remains wrong across correct prompts;
- expressive tags repeatedly fail in the same direction.

Action: voice casting before more tag complexity.

### Pronunciation defect

Examples:

- same critical name is repeatedly wrong;
- acronym/number normalization is consistently wrong.

Action: spoken form / dictionary / IPA, not emotional rewrite.

### Surface/context defect

Examples:

- independent turns sound fine but dialogue interaction is disconnected;
- split narration loses continuity at request boundaries.

Action: Text to Dialogue or contextual TTS / Studio as appropriate.

## 4. One-variable-class rule

After a repeated defect is established, change **one class** at a time:

```text
prompt wording
OR expression/tag direction
OR voice
OR Stability/settings
OR pronunciation/language setup
OR surface/context
```

Do not simultaneously change voice + wording + tags + settings unless the old configuration is being intentionally abandoned and no diagnostic comparison is needed.

## 5. Candidate count is not a quality metric

Do not require a fixed number of candidates for every line.

```text
first take clearly meets target
→ no ceremonial extra generation

first take questionable / isolated defect
→ compare candidate(s)

same defect repeats
→ diagnose first wrong owner
```

The goal is minimum generation needed for a reliable decision, not a ritual number of takes.

## 6. Seed usage

Current API `seed` is best-effort consistency only; determinism is not guaranteed.

Use seed when repeatability materially helps comparison. Do not treat the same seed as proof that every generation should be byte-identical or performance-identical.

## 7. Dialogue candidates

For Text to Dialogue, review both:

```text
complete exchange
+ each constituent VO ID
```

A candidate may have strong overall flow while one turn drops required meaning/expression. Conversely, one slightly weaker isolated turn may not justify rewriting the whole exchange if another same-content candidate solves it.

## 8. Evidence after approval

Retain only useful selected-take evidence when actual generation is approved:

```text
VO ID / Dialogue group
voice_id(s)
model + surface
exact prompt(s)
settings
pronunciation/language setup when material
continuity context when material
seed when materially used
selected take
actual duration/timestamps when needed
```

Do not persist rejected candidate history unless a repeated failure is useful project calibration.

## 9. Stop rule

Generation iteration stops when the selected take meets:

- communication;
- actor identity;
- naturalness;
- expression;
- pronunciation;
- timing when material;
- continuity/surface requirements.

Do not keep regenerating a correct take merely to search for an undefined “perfect” variant.

## Current official sources

- `https://elevenlabs.io/docs/overview/capabilities/text-to-speech`
- `https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech`
- `https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue`
- `https://elevenlabs.io/docs/api-reference/text-to-speech/convert`
