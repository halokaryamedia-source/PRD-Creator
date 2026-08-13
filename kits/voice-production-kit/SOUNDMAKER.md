# SoundMaker — Eleven v3 Execution Mode

Status: active Flow 6 execution procedure  
Model scope: **Eleven v3 only**

## Purpose

SoundMaker turns **one approved Voice Requirement at a time** into one Eleven v3 prompt that is ready to paste into ElevenLabs.

It exists to improve actual generated performance quality without creating a second source of truth.

```text
Flow 5 Voice Requirement
→ SoundMaker internal quality pass
→ one Eleven v3 prompt
→ canonical work/voice-production.md
→ optional real generation / feedback / approval
```

SoundMaker owns **how approved meaning is performed**. It does not create Voice scope, project facts, speakers, channels, triggers, mechanics, rewards, or lore.

`work/voice-production.md` remains the canonical wording owner. SoundMaker is an execution mode, not a parallel artifact authority.

## User experience

Normal use is intentionally simple:

```text
one Voice ID / one requested voice line
→ one best prompt
→ user generates in ElevenLabs
→ APPROVED or feedback
→ lock or revise the same task
```

Do not show internal checklists, tag taxonomy, WPM calculations, alternative prompts, or long technical explanations unless the user asks.

Default visible result:

````markdown
## <VOICE-ID / TASK NAME>

```text
<exact text to paste into ElevenLabs>
```

Ready to generate. After listening, reply **APPROVED** or give the specific part that still feels wrong.
````

Inside the code block include **only** text intended for ElevenLabs.

When a project/voice does not already have an approved generation setting, one short note outside the code block may state the baseline once:

```text
Eleven v3 · Stability: Natural
```

Do not repeat the setting on every line after it is established.

## Hard scope lock

SoundMaker in this repository is **v3-only**.

- Model: Eleven v3.
- Do not route to Multilingual v2, Flash, Turbo, Dialogue, Dubbing, Voice Changer, or Sound Effects as an automatic fallback.
- If a selected voice behaves poorly with v3, classify it as a **voice-fit risk** and prefer a better v3-compatible voice rather than changing model families.
- Keep environment/SFX generation separate from TTS voice performance.

## Default v3 generation baseline

Unless stronger approved project evidence already exists:

```text
Model: Eleven v3
Stability: Natural
```

Rules:

- use **Natural** as the default balance between voice identity and expressive response;
- move toward **Creative** only after the voice fit, wording, beat structure, and directing are already sound and the performance still needs more range;
- do not use **Robust** as the default for expressive SoundMaker work because the current reference records it as less responsive to directional prompting;
- do not depend on Speed as a required quality/duration control; current ElevenLabs documentation has conflicting Speed availability for v3, so the live UI owns whether that control exists;
- a project-calibrated approved Stability/visible setting is stronger than this generic baseline for the same voice/project.

Do not change voice, Stability, wording, tags, and punctuation simultaneously merely because one take was weak. Preserve causal visibility during revision.

## Required authority

Use this order:

1. current `work/voice-requirements.md` entry;
2. accepted `work/content.md` only when project context is needed;
3. current `work/voice-production.md` when revising an existing line;
4. approved prompt/audio evidence from the same project/voice;
5. `references/elevenlabs/README.md` and its v3 supporting pages for production technique.

A reference or previous approved line can shape performance behavior, never supply missing gameplay/story facts.

# Internal Quality Engine

Run the following sequence before presenting the prompt.

## 1. Requirement fidelity

Resolve:

```text
who is speaking?
who hears it?
what trigger caused the line?
what must be communicated?
what must not be added/repeated?
what should the listener understand/do/feel afterward?
```

Keep context that helps performance understanding, but spoken text includes only what the player actually needs to hear.

If required meaning cannot be written without inventing an upstream fact, stop and return the issue to the owning requirement instead of improvising dialogue.

## 2. Duration-first planning

If the user or requirement specifies timing, decide the timing class **before drafting**:

- `target range` — approximate timing; naturalness first;
- `hard maximum` — must remain under the cap;
- `fixed-sync` — must match an external timeline.

Use `references/elevenlabs/v3-duration-planning.md`.

Rules:

- count spoken words, not bracketed directions, when planning speech density;
- use project-calibrated duration evidence when available;
- otherwise use the documented fallback word-budget heuristics;
- reserve room for pauses, reactions, reveals, and strong landings;
- never rescue an oversized script by adding `[rushed]`, tag spam, or extreme speed changes.

If no duration target exists, do not invent a hard cap merely to make the line short.

## 3. Voice-fit check

Before adding more directing, ask whether the selected base voice can plausibly perform the required range.

Check the required family, for example:

```text
controlled narration
mystery
curiosity
warning
urgency
whisper
shout
comic reaction
relief
```

If the requested performance is far outside the voice's demonstrated character, mark the voice fit as risky internally. Do not try to compensate by stacking synonyms such as:

```text
[excited][energetic][enthusiastic][intense]
```

If no voice is specified, do not invent a specific commercial voice name. Recommend a voice profile/range only when the choice materially affects the result.

## 4. Performance map before wording

For lines with meaningful emotional movement, map the scene first.

Typical structure:

```text
initial state
→ new information/event
→ reaction
→ escalation or release
→ instruction/payoff/landing
```

Example:

```text
mysterious
→ curious
→ uneasy
→ urgent
→ firm
→ relieved/excited
```

The map follows the actual scene. Do not manufacture an emotional change simply because a paragraph is long.

For a simple warning or acknowledgement, one stable state may be correct.

## 5. Write spoken text first

Create the clean speech before tags.

Prefer:

- one main idea or action per beat;
- active spoken verbs;
- natural contractions when appropriate to the character;
- information in the order the listener needs it;
- short enough sentences for important thoughts to land;
- project terminology exactly as approved.

Avoid:

- PRD/specification prose;
- multiple critical instructions buried in one sentence;
- hidden implementation detail;
- repeating a full objective briefing in later reminders;
- filler added only to consume duration.

The script should still be understandable if every Audio Tag is removed.

## 6. Build audible beat architecture

A long line should feel like a sequence of performed thoughts, not one paragraph read at one pitch.

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

Anti-monotony gate:

- do not let several important instructions collapse into one long sentence;
- avoid repeating the same sentence shape across adjacent beats when a more natural rhythm exists;
- preserve contrast between setup, escalation, and landing when the scene actually contains those changes;
- give the final important thought a clean landing;
- do not force artificial excitement into calm explanatory content.

## 7. Add textual performance controls

Apply non-tag controls before adding extra Audio Tags.

Order:

```text
sentence boundaries
→ commas / questions / exclamations
→ ellipses / em dashes
→ line / paragraph breaks
→ selective CAPS
```

Use them semantically:

- `.` completes a thought and can create a new beat;
- `,` keeps related material in one thought;
- `?` preserves real questioning/rhetorical contour;
- `!` adds textual intensity/assertiveness;
- `...` adds hesitation, suspense, weight, or a softer pause;
- `—` creates a hard pivot/interruption/dramatic break;
- line breaks expose phrasing/beat boundaries;
- CAPS adds selective emphasis.

Do not treat punctuation or line breaks as exact millisecond timing controls.

Avoid entire paragraphs in CAPS. Prefer a small number of words that genuinely need stress.

## 8. Add minimal Audio Tags

Audio Tags are directing cues, not the source of emotion.

Use simple audible directions close to the beat they affect.

Production heuristic:

```text
0–1 simultaneous tag → default
2 tags                → valid when they control different compatible dimensions
3 tags                → exception; preferably project-calibrated
4+ tags               → reject by default
```

Good cross-dimension pairs:

```text
[nervous][quietly]   → emotion + projection
[excited][rushed]    → emotion + pace
[reflective][softly] → narrative stance + projection
```

Avoid redundant emotional synonyms or contradictory directions.

Do not assume a tag remains active for exactly N words or until the next tag. Standard Speech Synthesis v3 has no documented fixed tag-persistence window. Place direction near the intended beat and restate only when the performance state materially changes.

## 9. Sequence human reactions

Treat reactions as timeline events:

```text
[sighs]
[gasps]
[laughs]
[gulps]
[hesitates]
```

Prefer:

```text
[nervous][quietly]
I think something is moving...

[gulps]

Don't move.
```

rather than stacking the reaction into a large tag cluster.

Use reactions only when they fit the character and scene. Decorative reaction spam makes the line feel synthetic.

## 10. Pronunciation safety

Before final output, identify only material pronunciation risks:

- fantasy/proper names;
- unusual acronyms;
- multilingual phrases;
- ambiguous numbers/symbols that must be spoken a specific way.

Prefer explicit spoken forms for ambiguous numbers/symbols. Use project pronunciation evidence, native v3 IPA, or pronunciation dictionaries when needed.

Do not claim pronunciation is verified until actual audio has been heard or explicit approved evidence exists.

## 11. v3 pre-generation gate

A prompt is `Ready to generate` only when:

- project meaning is correct;
- Voice ID scope is unchanged;
- wording sounds spoken rather than documented;
- target duration budget is plausible when timing matters;
- performance changes have scene reasons;
- beat structure prevents obvious monotony/density problems;
- punctuation, line breaks, and CAPS are purposeful;
- tags are audible, compatible, and minimal;
- there is no SSML `<break>` markup;
- environment/SFX instructions are not mixed into the voice prompt;
- material pronunciation risk is addressed;
- the v3 generation baseline is known for the current project/voice;
- only one best final prompt is shown.

If a material issue remains, present the same task as a review draft and do not encourage paid generation yet.

## 12. Generation handoff

Immediately before generation, the operator should be able to answer:

```text
Model: Eleven v3
Voice: known / intentionally selected
Stability: Natural or project-calibrated value
Prompt: exact reviewed version
Duration target: none / range / hard max / fixed-sync
Pronunciation risk: resolved / intentionally pending review
```

Any UI rewrite/enhancement or manual edit that changes the prompt creates a **new prompt revision**. Review that changed wording before generation instead of assuming an automatic rewrite preserves the intended performance.

# Revision after generation

## User gives textual feedback

Preserve what already worked.

Diagnose in this order:

```text
meaning / missing information
→ clarity
→ beat density / sentence architecture
→ rhythm / punctuation / CAPS
→ performance direction / tags
→ pronunciation
→ voice fit / Stability
```

Resolve all known issues in one coherent revision rather than making a series of tiny paid-generation changes.

Do not change wording, tags, Stability, and voice all at once unless the evidence genuinely shows multiple independent problems.

## One odd or weak take

Eleven v3 is nondeterministic. If the prompt is structurally sound and the failure appears take-specific, prefer reviewing the other available v3 alternative or an eligible regeneration before rewriting the prompt.

Repeated failure at the same performance point is stronger evidence that the prompt, voice fit, or setting needs revision.

## Flat delivery

Do not immediately add more tags.

Fix in this order:

1. remove specification-like wording;
2. split dense thoughts into meaningful beats;
3. create real contrast between beat functions;
4. improve punctuation / selective CAPS / line structure;
5. add or refine only the direction needed at actual emotional changes;
6. then reassess voice fit or Stability if the text architecture is already sound.

## Duration miss

If audio is too long:

1. remove nonessential spoken information;
2. shorten sentence structure;
3. preserve required facts and emotional landing;
4. recalculate the word budget;
5. only use faster delivery when it remains natural and clear.

If audio is shorter than the target but still correct and natural, do not add filler unless the external timing requirement genuinely needs it.

# Actual audio quality review

When the user supplies or plays back an actual generated take, judge the audio itself rather than inferring quality from the prompt.

Review these dimensions:

1. **Meaning / intelligibility** — required words and instructions are clearly understandable.
2. **Voice identity** — the speaker still sounds like the intended character/voice rather than drifting into a noticeably different persona.
3. **Emotional movement** — intended changes in state are audible where the scene changes; a long line should not collapse into one unchanging tone when the script contains real emotional beats.
4. **Pacing / breath** — important ideas have enough space to land; pauses are not so long/short that meaning or urgency is damaged.
5. **Emphasis / landing** — important words receive appropriate stress and the final beat ends with the intended confidence, tension, relief, warning, or payoff.
6. **Naturalness** — tags, reactions, CAPS, and punctuation do not produce obvious overacting, robotic segmentation, or artificial emotional jumps.
7. **Pronunciation** — material names/terms/numbers are spoken correctly enough for production consistency.
8. **Duration** — the actual file meets the requested range/hard maximum/fixed-sync requirement when timing is part of the task.

Use the smallest corrective action that matches the evidence:

```text
all important dimensions pass
→ APPROVE

one take is odd but prompt/voice/settings remain sound
→ REVIEW ALTERNATIVE / REGENERATE

same wording/performance point repeatedly fails
→ REVISE PROMPT

performance range consistently exceeds the selected voice
→ VOICE-FIT RISK / CHANGE VOICE
```

Do not call a line immersive merely because it contains many tags. The acceptance question is whether the **heard performance** communicates the scene clearly and changes naturally where the scene changes.

# Approval lock and canonical sync

When the user says **APPROVED**:

1. the **exact prompt actually used** becomes the approved performance wording for that Voice ID;
2. if the user edited the prompt before generation, the user's actually-generated version supersedes the assistant draft;
3. synchronize that exact wording back into `work/voice-production.md` before claiming the project script/DOCX/audio scope is current;
4. rebuild the DOCX only when canonical wording changed and the DOCX is part of the active deliverable;
5. record actual audio evidence only when the file/result is available;
6. useful project calibration may include voice, Stability/visible settings, actual duration, pronunciation, and behavior notes.

Do not keep an older canonical script while treating a different generated prompt as approved.

If approval occurs after Flow 7 had already marked an older script/DOCX revision ready, reopen the affected Flow 6/7 scope and reissue current acceptance rather than silently preserving stale delivery state.

# Relationship to Flow 6

SoundMaker is the **quality/execution profile inside Flow 6**.

- `SCRIPT-PRODUCTION.md` owns the full-project canonical script/DOCX workflow.
- `SOUNDMAKER.md` owns the one-entry-at-a-time Eleven v3 quality procedure.
- `work/voice-production.md` owns final wording.
- generated audio is evidence/output, not an upstream fact source.

When producing script/DOCX only, SoundMaker runs the pre-generation quality engine but does not require audio approval.

When actual ElevenLabs generation is part of the task, use the generation baseline, audio review, approval loop, and canonical-sync rule above.
