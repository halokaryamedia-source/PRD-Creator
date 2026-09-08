# Eleven v3 Naturalness & Narration Craft

Last verified: **2026-09-08**

Purpose: reduce stiff, synthetic, over-directed Voice output by making **voice fit, spoken-language writing, prosodic thought groups, and generation context** the primary controls. Audio Tags and settings are secondary interventions.

This is a craft reference for `../PERFORMANCE-WRITING.md`, not a new workflow, schema, approval layer, or source of project meaning.

## Core order

```text
approved communication meaning
→ suitable voice / target voice profile
→ spoken-language rewrite
→ thought-group / prosody design
→ continuity context
→ punctuation / emphasis
→ Audio Tags only when useful
→ Stability / Speed only when useful
→ generation / heard evidence
```

If a line sounds like a document being read aloud, adding more tags is usually the wrong first repair.

# 1. Common causes of stiffness

Treat these as likely causes before assuming Eleven v3 itself is the problem:

- PRD/specification prose was carried into the spoken line;
- every sentence is grammatically complete, similarly sized, and similarly stressed;
- several instructions or facts are packed into one breathless sentence;
- the line explains context the listener already knows from the trigger/scene;
- the wording has no clear listener relationship or conversational point of view;
- the selected voice naturally speaks with a different cadence, projection, accent, or emotional range;
- every line is prefixed with a direction tag even when the voice/text already imply the delivery;
- synonymous tags, punctuation, CAPS, and settings all push the same emotion at once;
- short connected lines are generated as isolated clips with no previous/next context;
- Speed or Stability is used to compensate for a badly sized or badly written script;
- filler, hesitations, or verbal tics are added mechanically to imitate humanity.

Natural speech is not the same as adding noise or imperfection. A clear narrator, commander, tutorial voice, or formal character can be fully natural without filler words.

# 2. Spoken-language rewrite

Before directing performance, convert the requirement into something this speaker would plausibly say **at this exact moment**.

## Speechification pass

Preserve every required fact, then remove written-language scaffolding that does not help the listener.

Prefer:

- direct spoken verbs over nominal/specification phrasing;
- familiar word order;
- context-aware pronouns and references when the referent is already clear;
- contractions when they fit the language, register, and established speaker;
- sentence-length variation that follows thought complexity;
- one clear listener-facing purpose per thought group;
- exact project terminology only where the listener actually needs it;
- the most important action/result in a position where it can land cleanly.

Avoid:

- `in order to`, `therefore`, `the player must`, `the objective is to`, `upon completion of`, and similar document-language unless the character genuinely speaks that way;
- repeating the trigger as exposition;
- restating a visible result the listener can already perceive unless acknowledgement is the communication job;
- formal connective tissue added only to make every sentence complete;
- automatic filler such as `uh`, `well`, `you know`, `like`, repeated starts, or sighs when character/scene evidence does not justify them.

Example transformation:

```text
written/spec-like
Proceed to the central console in order to activate the sequence. Upon activation, remain within the marked area until calibration is complete.

spoken
Head to the central console and start the sequence.
Stay inside the marked area until calibration finishes.
```

The second version is not “more casual” by default; it is simply easier to speak and hear.

## Listener-first compression

When the scene already establishes a noun or location, spoken language may safely use a shorter reference:

```text
The central containment chamber is now unlocked. Enter the central containment chamber.
→
The chamber's unlocked. Go in.
```

Do this only when reference remains unambiguous and all required communication survives.

# 3. Match the spoken register to the job

Naturalness depends on **appropriate register**, not one universal conversational style.

| Voice job | Natural baseline |
|---|---|
| Direct NPC dialogue | relational, context-aware, economical, responsive to what just happened |
| Narration | coherent thought flow, sentence-length contrast, controlled emphasis, fewer local directions |
| Radio / mission comms | concise, intelligible, slightly structured, limited filler, clear action/result landing |
| Tutorial / guidance | calm and direct, one action per beat, no fake personality noise |
| Warning | short, front-loaded risk/action, minimal explanation |
| Completion / success | acknowledge the result; do not replay the entire briefing |

Do not force a tutorial line to sound like casual banter or a solemn narrator to use slang merely because “conversation” sounds more human.

# 4. Thought groups before tags

A useful spoken unit is a **thought group**: one breath-like phrase or sentence with one dominant idea, action, reaction, or image.

```text
setup
→ important fact
→ implication / reaction
→ action or landing
```

Not every line needs all four.

Good thought-group design:

- critical information is not buried in the middle of a long clause chain;
- a new thought earns a real boundary;
- closely related words stay together;
- the final important word/phrase is not followed by unnecessary explanation;
- adjacent beats do not all have the same cadence.

A written sentence may become two spoken beats. Two short written sentences may become one spoken thought. Grammar does not own performance segmentation.

# 5. Prosody through text

ElevenLabs documents text structure, punctuation, capitalization, and emotional context as material controls for v3. Use them before adding more directions.

## Punctuation

```text
.   complete thought / reset
,   keep related material moving
?   genuine questioning contour
!   assertive or heightened textual energy
—   pivot, cut-off, interruption, hard turn
…   hesitation, suspense, trailing weight
```

Rules:

- punctuation must reflect meaning, not function as arbitrary timing code;
- repeated ellipses can make narration mannered, slow, or melodramatic;
- repeated exclamation marks can flatten contrast by making everything intense;
- line breaks improve phrase readability but are not exact pause timers.

## CAPS

Use CAPS only when contrast really matters. If every key noun is capitalized, the voice has no unstressed baseline left.

## Natural irregularity

Human speech is rhythmically uneven because thoughts have different shapes. Create that variation through **meaningful sentence/phrase structure first**.

Contractions, fragments, restarts, repetitions, discourse markers, or stretched words are optional expressive devices—not a naturalness checklist. Use them only when they belong to the speaker/moment.

# 6. Audio Tags are optional

A canonical `performance` block may begin directly with spoken text.

```text
0 tags
→ valid natural baseline when voice + wording + context already imply the delivery

1 local tag
→ use when one audible state/reaction materially improves interpretation

2 simultaneous tags
→ use only when they control different compatible dimensions

3+ simultaneous tags
→ exceptional; require a concrete reason or project-calibrated evidence
```

## When an opening tag is useful

Use an opening direction when the required opening delivery is **not sufficiently inferable** from:

- the selected voice's baseline;
- the wording and punctuation;
- the immediate narrative/dialogue context.

Examples: whispering despite neutral wording, restrained panic, deliberate deadpan, or a performance state that intentionally differs from the voice's normal delivery.

## When an opening tag is unnecessary

Do not add `[calm]`, `[clear]`, `[natural]`, `[conversational]`, or similar boilerplate merely because every prompt “should have a tag.” If the voice is already suitable and the spoken line naturally encodes the intended tone, leave the baseline alone.

## Redundancy test

Before adding a tag, ask:

```text
If I remove this tag, does the intended audible interpretation become materially ambiguous or weaker?
```

If no, remove it.

Do not stack synonymous direction such as:

```text
[excited][energetic][enthusiastic]
```

Text + punctuation + one precise cue is usually cleaner than several overlapping controls.

# 7. Emotional context should live in the speech when possible

ElevenLabs documents that emotional context in text influences delivery. Let wording and scene logic carry as much emotion as possible.

For example, urgency can come from:

- shorter thought groups;
- direct verbs;
- interruption/cut-off structure;
- information order;
- contrast and emphasis.

A line that already says `Move. Now.` may not need `[urgent]` unless the selected voice consistently under-delivers that meaning.

Do not insert spoken narrative directions such as `she said sadly` into game dialogue merely to steer the model unless those words are genuinely meant to be heard. Use Audio Tags for non-spoken direction when needed.

# 8. Short lines: add context, not filler

Very short lines can sound abrupt because the model has little linguistic context. Do **not** pad a legitimate short command, acknowledgement, or reaction with meaningless words.

Instead, when the line belongs to a continuing same-speaker sequence:

```text
canonical VO line stays short
+ generation receives relevant previous_text / next_text
→ more contextual prosody without changing spoken meaning
```

When the short line is a response to another speaker, prefer the same-Moment Text to Dialogue route when the interaction is materially conversational.

If the short line is genuinely isolated, let it stay isolated and rely on voice fit + exact wording. Do not fabricate context inside the audible payload.

# 9. Same-speaker narration continuity

When narration is split into separate generations for identity, editing, or implementation reasons, preserve contextual flow at generation time.

For the API:

```text
previous_text / next_text
→ provide surrounding canonical spoken text to influence continuity

previous_request_ids / next_request_ids
→ use adjacent generated request IDs when preserving or regenerating an already-generated sequence
```

Current Text to Speech API allows up to three previous/next request IDs. When both text context and request IDs are supplied on the same side, request IDs take precedence according to the current API contract.

Use continuity context when:

- the same narrator continues one scene/thought across clips;
- a paragraph is split for implementation or editability;
- one middle clip is regenerated and should still connect naturally to its neighbors.

Do not use unrelated earlier project text merely because context fields exist.

For long-form production, split at scene/paragraph/emotional boundaries rather than equal character counts. Current ElevenCreative Studio is preferable when editorial paragraph-level continuity and regeneration are the real task.

# 10. Voice foundation

ElevenLabs identifies voice selection as the most important v3 parameter. Prompt engineering cannot reliably force a mismatched voice into an alien performance envelope.

A useful Target Voice Profile contains only audible traits needed by the project:

```text
language + regional dialect when material
timbre / vocal weight / perceived age when material
baseline energy
natural cadence / pacing
projection range
emotional range
persona / attitude
pronunciation or accent requirements
```

Prefer a native/compatible voice for the target language and accent.

## Voice Design when no suitable voice exists

Current ElevenLabs Voice Design guidance recommends explicit language/dialect, persona/emotion, timbre, pacing, and delivery. Use that structure when designing a voice instead of relying on vague adjectives.

Keep Voice Design and performance prompting separate:

```text
Voice Design
→ establishes the actor / baseline instrument

SoundMaker performance prompt
→ directs what that actor does in this moment
```

Do not use performance tags to compensate for a poorly designed baseline voice.

For Voice Design preview text, use material that matches the intended character/register. A full sentence or short paragraph gives more useful context than an unrelated tiny phrase when subtle pacing/tone is being judged.

# 11. Settings discipline

Repository baseline remains:

```text
Stability: Natural
Speed: 1.0 / unchanged when the active surface exposes Speed
```

Guidance:

- if output is stiff, inspect voice fit, written-language residue, uniform rhythm, missing context, and over-direction before changing settings;
- Robust can increase consistency while reducing directional responsiveness, so do not use it as an automatic quality upgrade;
- Creative can increase expressive variation but also variability; use it after the script/voice relationship is sound;
- if Speed is available, keep 1.0 as the natural baseline and avoid extreme changes to rescue duration; current ElevenLabs guidance warns extremes can affect quality.

Settings tune a good performance design. They do not replace it.

# 12. Text-only Naturalness Gate

Before declaring a script ready, review it without imagining any Audio Tags.

A line passes when:

- a real person with this speaker identity could plausibly say it at this trigger;
- it does not sound copied from a specification/document unless the character intentionally speaks that way;
- each thought group has a clear listener-facing job;
- sentence/phrase rhythm is not mechanically uniform;
- context is neither needlessly repeated nor required information omitted;
- contractions/fragments/fillers are used only when appropriate, not as decoration;
- the final action/result/idea lands cleanly;
- the intended delivery can mostly be inferred from voice + wording + context;
- any remaining Audio Tag solves a specific audible ambiguity or event.

This is a reasoning check, not a numeric scorecard and not a persisted artifact.

# 13. Naturalness troubleshooting order

```text
stiff / robotic
→ voice fit
→ written-language residue
→ thought-group / sentence rhythm
→ missing continuity context
→ redundant punctuation / CAPS / tags
→ Stability
→ Speed only if genuinely needed

flat but otherwise natural
→ strengthen textual emotional context / beat contrast
→ one precise direction if still needed
→ consider Creative only after that

overacted / synthetic
→ remove redundant tags / CAPS / ellipses
→ restore Natural baseline
→ inspect voice mismatch

short line sounds detached
→ previous/next context or Dialogue grouping when semantically justified
→ do not add filler
```

# Current official references

- `https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices`
- `https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech`
- `https://elevenlabs.io/docs/api-reference/text-to-speech/convert`
- `https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps`
- `https://elevenlabs.io/docs/eleven-creative/voices/voice-design/`
- `https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue`

Re-verify when official controls or model behavior materially change.