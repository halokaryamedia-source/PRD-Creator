# SoundMaker — Eleven v3 Execution Mode

Status: active Flow 6 execution procedure  
Model scope: **Eleven v3 only**

## Purpose

SoundMaker turns approved Voice Requirements into production-ready Eleven v3 wording without creating a second source of truth.

```text
Voice Requirement
→ complete communication/performance intent
→ natural spoken-language rewrite
→ deliberate performance shaping
→ conserve required meaning
→ review script readiness
→ canonical work/voice-production.md
→ optional Generation Mode later
```

`work/voice-production.md` remains the canonical wording owner.

# Operating modes

## Preparation Mode

Default when the task is to design, improve, or review Voice Production without generating audio.

```text
all current Voice Requirements
→ per-line SoundMaker preparation
→ project-level readiness review
→ canonical script
→ consolidated project-HTML handoff when in scope
```

Preparation Mode:

- may process the full current Voice scope in one bounded pass;
- does **not** require audio generation/testing or `APPROVED` per line;
- may use a Target Voice Profile when an actual ElevenLabs voice is not selected yet;
- does not invent measured duration, pronunciation proof, audio quality, or project calibration.

## Generation Mode

Use only when actual ElevenLabs generation, heard-take revision, or audio approval is requested.

Choose the smallest correct generation unit:

```text
independent Voice ID
→ exact reviewed prompt
→ Eleven v3 Text to Speech

same Moment + multiple speakers + conversational response dependency
→ ordered existing Voice IDs
→ Eleven v3 Text to Dialogue

long-form editorial/timeline work
→ current ElevenCreative Studio when useful
```

Text to Dialogue grouping exists only for generation. It does **not** create a Dialogue ID, duplicate canonical script, or replace the constituent `VO-...` entries.

One-at-a-time remains the default for independent TTS generation. It does not require conversationally dependent turns to be generated separately.

# Output contract

## Canonical entry

`work/voice-production.md` contains only stable operator-useful metadata plus the exact Eleven v3 text:

```text
### <VOICE-ID> — <Title>
Type: <Flow 5 type>
Speaker: <Flow 5 speaker>
Estimated Duration: <range>

```performance
<exact Eleven v3 spoken payload; Audio Tags optional>
```
```

`Type` and `Speaker` must match Flow 5. The performance block is the exact generation payload for that Voice ID, not commentary about it.

Keep Channel, Trigger, Purpose, requirement bullets, source refs, reasoning, WPM math, voice-fit ratings, generation-group metadata, continuity context, and QA notes in their owning/internal context rather than duplicating them into every entry.

## Operator handoff

State shared setup once when useful:

```text
Model: Eleven v3
Surface: Text to Speech | Text to Dialogue | ElevenCreative Studio
Stability: Natural | project-calibrated
Speed: 1.0 / unchanged when available | project-calibrated
```

For TTS, show the active Voice ID/Title, Speaker, selected voice, Estimated Duration, and one exact prompt block.

For Text to Dialogue, show the approved Moment, ordered constituent Voice IDs, exact Speaker → actual ElevenLabs voice mapping, and each exact canonical prompt as one Dialogue turn. Do not concatenate/rewrite the conversation into a second canonical script.

Add an external production note only when the operator must take an extra action such as pronunciation dictionary setup, continuity context, timestamps, or current Studio routing.

Never place internal reasoning or operator instructions inside the Eleven v3 prompt.

# Authority and decision boundary

Recover current project facts before asking the user:

1. matching `work/voice-requirements.md` entry;
2. accepted `work/content.md` / current PRD meaning only when the requirement does not already carry enough context;
3. current `work/voice-production.md` when revising;
4. approved same-project wording/settings/pronunciation evidence when it exists;
5. Eleven v3 references only for production technique.

The Flow 5 requirement is the normal interface. Do not reopen the full PRD merely because richer prose would be convenient.

Separate these two classes:

### Production interpretation — SoundMaker may decide

Examples:

- spoken phrasing, contractions, sentence split, and context-aware compression;
- beat/thought-group structure;
- punctuation / line breaks / selective CAPS;
- whether Audio Tags are needed at all, plus tag choice/placement;
- performance pacing within the approved communication intent;
- duration-conscious compression that preserves required meaning;
- Performance Shape and final Landing when upstream meaning does not prescribe them;
- TTS vs Text to Dialogue vs current Studio generation routing when approved semantics remain unchanged;
- previous/next generation context when it changes only prosodic continuity, not spoken meaning.

These do not need a new user approval step merely because the AI made a craft decision.

### Material creative/project decision — return upstream when unresolved

Examples:

- changing the speaker's established personality;
- inventing a new accent/identity that materially defines the character;
- changing Voice scope, Trigger, Channel, objective meaning, mechanic, reward, lore, or outcome;
- changing an authoritative timing/sync constraint;
- dropping a required communication fact because it does not fit the desired duration.

Do not hide an upstream decision inside performance polish.

# Eleven v3 defaults

Unless stronger approved project evidence exists:

```text
Model: Eleven v3
Stability: Natural
Speed: 1.0 / unchanged when the active surface exposes it
Surface: Text to Speech for independent speech
Enhance on SoundMaker-reviewed prompt: OFF
Audio Tags: optional
```

Route same-Moment multi-speaker exchanges with real response dependency to Text to Dialogue. Use current ElevenCreative Studio for long-form/editorial production when it materially improves continuity or timeline work.

Enhance may help untreated text as a drafting aid. An already-directed or naturalness-reviewed SoundMaker prompt keeps Enhance OFF by default; any UI rewrite becomes a new draft requiring review.

Move toward Creative only after voice fit, spoken wording, and beat structure are sound and more expressive range is genuinely needed. Use Robust when stability/consistency is the actual priority and reduced directional response is acceptable.

Do not use Speed or Stability to rescue a line that is fundamentally written like a document.

# Preparation quality model

## 1. Voice Intent Completeness

Before writing, ensure the Voice moment is complete enough that SoundMaker does not have to invent product meaning during prose generation.

Use one internal **Performance Fill Map**. Do not persist another artifact or schema.

```text
Communication Job
→ What must this line accomplish?

Listener State
→ What is the player doing/experiencing when it plays?

Information Payload
→ Which material facts must be heard now?

Listener Outcome
→ After hearing it, what should the player know, do, or understand/feel?

Speaker Identity
→ What established speaker behavior must remain recognizable?

Timing Envelope
→ none / target range / hard maximum / fixed-sync?

Performance Shape
→ stable state or justified emotional movement?

Landing
→ What final idea/action/result must land most clearly?
```

### Fill from Flow 5 before reopening the PRD

Use the requirement fields directly:

```text
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard timing truth   ← Timing Constraint, only when present
Scope guardrails    ← Must not add/repeat
```

Then use accepted project context only for genuinely missing **delivery-relevant context**, such as established speaker characterization or scene state that cannot be understood from the requirement alone.

Rules:

- `Trigger` should already describe the event/state and relevant listener condition when material;
- `Purpose` should already express the listener-facing result, not merely say `provide dialogue`;
- `Must communicate` is the authoritative payload, not a rough writing suggestion;
- an optional Flow 5 `Timing Constraint` is authoritative source truth, **not** the same thing as Flow 6 `Estimated Duration`;
- if `Timing Constraint` is absent, do not invent a hard source limit—plan a reasonable Estimated Duration instead;
- Performance Shape and Landing normally remain SoundMaker craft decisions derived from the approved moment.

Ask only if a material unresolved decision still prevents a responsible answer after this mapping.

## 2. Naturalness-first spoken-language pass

Before thinking about Audio Tags, make the line **speakable**.

```text
requirement meaning
→ what would this speaker actually say here?
→ remove written/specification scaffolding
→ organize into natural thought groups
→ preserve every required fact
```

Prefer:

- direct spoken verbs;
- listener-first information order;
- context-aware pronouns/references when the scene already resolves them;
- contractions when appropriate to the speaker/language/register;
- sentence-length variation driven by thought complexity;
- a clean final landing;
- exact project terminology only where the listener needs it.

Avoid:

- PRD phrasing such as `the player must`, `in order to`, `upon completion of`, or `the objective is to` unless that is genuinely the speaker's established voice;
- repeating context the trigger already makes obvious;
- mechanically complete sentences with identical rhythm;
- filler, hesitations, slang, fragments, or verbal tics added merely to simulate humanity;
- several critical instructions inside one long sentence.

Naturalness is **register-correct**, not universally casual. Tutorial, narrator, radio, warning, and direct NPC dialogue may all have different natural baselines.

For stiffness/narration work, use `references/elevenlabs/v3-naturalness.md`.

## 3. Duration planning when timing matters

Resolve timing before final wording.

First honor any authoritative Flow 5 `Timing Constraint`. Then plan the production estimate:

- **target range** — approximate; naturalness first;
- **hard maximum** — stay below the cap;
- **fixed-sync** — fit an external timeline.

Use `references/elevenlabs/v3-duration-planning.md` only when timing is material.

`Estimated Duration` is Flow 6 planning. It must remain compatible with an authoritative Flow 5 timing constraint but must never be presented as if the estimate came from upstream authority.

Do not write an oversized script and rescue it afterward with `[rushed]`, tag spam, or aggressive Speed changes. Duration pressure may simplify wording; it may not silently delete required communication.

## 4. Voice requirement / Target Voice Profile

If an actual voice is selected, judge only the required performance envelope:

```text
identity / timbre / persona
baseline tone / energy
natural cadence / pacing
required emotional range
projection range
language / accent compatibility
material pronunciation or drift risk
```

Internal result may be `GOOD FIT`, `LIMITED FIT`, `RISKY FIT`, or `UNKNOWN`.

If no voice is selected in Preparation Mode, derive a Target Voice Profile from the same dimensions. `VOICE NOT SELECTED` is not a preparation blocker when that profile is clear.

Use approved Speaker characterization when it exists. Do not invent a commercial voice name or new character identity to finish preparation, and do not compensate for risky fit with direction stacks.

When no suitable library/approved voice exists and Voice Design is in scope, use current Voice Design guidance from `v3-production-reference.md`: define language/dialect, audible identity, timbre, pacing, and delivery deliberately; preview with text that actually resembles the intended register.

## 5. Write the performance

Write spoken text before tags.

### Thought groups / beats

Prefer one dominant communication/performance purpose per thought group.

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

A written sentence may become two spoken beats. Two short written sentences may become one spoken thought. Grammar does not own performance segmentation.

For a longer line, shape movement only when the scene/meaning changes:

```text
initial state
→ new information
→ reaction
→ escalation / release
→ instruction / payoff / landing
```

A simple warning or acknowledgement may correctly remain in one stable state.

### Textual controls before tags

Use this order:

```text
spoken wording
→ thought-group boundaries
→ punctuation
→ line / paragraph structure
→ selective CAPS
→ Audio Tags only when needed
```

Interpretation:

- `.` — complete thought / reset;
- `,` — related material in one thought;
- `?` — real or rhetorical questioning contour;
- `!` — textual intensity/assertiveness;
- `...` / `…` — hesitation, suspense, trailing weight;
- `—` — hard pivot/interruption;
- line breaks — readable phrasing/beat boundaries;
- CAPS — selective contrast/emphasis.

These are performance cues, not exact timing commands. Do not use ellipses, CAPS, or exclamation marks as decorative seasoning on every line.

### Audio Tags — optional intervention

A `performance` block may begin directly with spoken text. **Zero Audio Tags is valid.**

Use an opening tag only when the intended opening delivery is not sufficiently implied by the selected voice, wording, punctuation, and immediate context.

Repository heuristic:

```text
0 tags               → valid natural baseline
1 local tag          → normal when one audible state/reaction needs help
2 simultaneous tags  → valid when dimensions differ and are compatible
3+ simultaneous tags → exception; require a concrete reason or project-calibrated evidence
```

Before adding a tag, ask whether removing it would materially weaken or confuse the intended audible interpretation. If not, omit it.

Do not add boilerplate `[calm]`, `[clear]`, `[natural]`, `[conversational]`, or equivalent merely to make the prompt look directed.

Place direction close to the beat it affects. Do not assume a fixed tag-persistence window. Reactions are timeline events, not decoration.

Detailed tag/non-tag controls stay in `references/elevenlabs/v3-performance-writing.md`.

In Text to Dialogue, the same exact performance payload is placed inside the turn for that Voice ID. Do not move tags into a separate Dialogue-level direction layer.

### Pronunciation

Use the smallest reliable control:

```text
ordinary word → normal text
ambiguous number/acronym/symbol → explicit spoken form
isolated unusual proper noun → inline v3 IPA when needed
repeated project term → project pronunciation note/dictionary when appropriate
heard + approved → project-calibrated lock
```

Preparation may identify risk without claiming verification.

## 6. Continuity planning

Do not confuse canonical line identity with generation isolation.

### Independent short line

If the Voice ID is genuinely standalone, generate it standalone. Do not add filler merely to create context.

### Connected same-speaker narration

When several Voice IDs/segments belong to one continuing narration and must still be generated separately, use generation context rather than audible padding:

```text
previous_text / next_text
→ surrounding canonical spoken text for prosodic continuity

previous_request_ids / next_request_ids
→ already-generated adjacent clips, especially when regenerating a middle segment
```

Use only relevant adjacent context. Do not persist this as duplicate canonical wording.

### Cross-speaker interaction

If later delivery materially reacts to an earlier speaker in the same approved Moment, route to Text to Dialogue instead of trying to fake conversational continuity with isolated TTS.

### Long-form

Split at semantic boundaries—scene, paragraph, emotional transition—not equal character counts. Use current ElevenCreative Studio when editorial paragraph-level continuity/regeneration is the real need.

## 7. Communication Conservation

After the prompt is written or shortened, compare it back to the Flow 5 requirement.

A line passes only when:

- every independently actionable `Must communicate` fact that belongs in this moment still has a clear spoken representation;
- every `Must not add/repeat` guardrail remains respected;
- required names, mechanics, result/state, sequence, and terminology retain their meaning;
- any authoritative `Timing Constraint` remains respected by the planned wording/timing approach;
- naturalness/performance polish did not introduce a new project fact;
- duration compression did not hide or delete required communication.

Paraphrase, context-aware compression, contractions, and sentence regrouping are allowed when the resulting speech still communicates the same material meaning clearly. Concision is not permission to thin requirements.

Do **not** create a persisted requirement-to-sentence mapping. This is a reasoning gate over the current requirement and prompt.

## 8. Per-line script-ready gate

A line is script-ready when:

- Voice Intent Completeness is sufficient for responsible writing;
- project meaning and Voice ID scope are intact;
- Type and Speaker remain exact Flow 5 values;
- authoritative Flow 5 timing constraints are honored when present;
- Estimated Duration is plausible when relevant;
- selected voice fit is acceptable/risk is explicit, or a clear Target Voice Profile exists;
- wording sounds like speech appropriate to this speaker/register rather than accidental document prose;
- thought-group rhythm and landing are deliberate;
- punctuation/CAPS/tags are purposeful and minimal;
- tags are absent when unnecessary and precise when present;
- no SSML `<break>` or canonical environmental-SFX instruction is present;
- material pronunciation risk is identified;
- continuity context is planned when generation isolation would otherwise make connected narration/dialogue sound detached;
- **Communication Conservation passes**;
- exact canonical wording revision is known.

Generation readiness additionally requires an intentionally selected actual voice and current generation settings.

# Integrated Voice Script Readiness

After all requested lines are script-ready, perform **one project-level semantic/craft review**. Do not turn the lenses below into separate workflow stages, scorecards, or artifacts.

| Lens | Ready when... |
|---|---|
| Communication | Required meaning survives clearly and no unsupported meaning was added. |
| Listener | Each line fits the player's state and gives the right amount of information/action at that moment. |
| Naturalness | Wording is speakable, register-correct, rhythmically non-mechanical, and free of unnecessary direction/filler. |
| Character | Recurring speakers remain recognizable without forcing every line into the same template. |
| Performance | Emotional movement, thought groups, punctuation, CAPS, and optional tags serve the scene rather than decorate it. |
| Timing | Estimated duration/density is plausible, authoritative timing constraints are honored, and no required fact was sacrificed to fit them. |
| Continuity | Information and prosody progress; connected narration/dialogue is not needlessly generated as contextless fragments. |
| Operator | Speaker ownership, duration, exact prompt, voice, surface, and any special generation context are clear enough to use without guessing. |

Speaker continuity and structural variety are reviewed together: preserve character identity, but vary structure when repetition is accidental rather than intentional character/gameplay language.

Briefings introduce what is needed, reminders repeat only the minimum actionable fact, and success lines acknowledge results rather than replaying the briefing.

The review result is conceptually one decision: **Voice Script Readiness: PASS | FAIL**. Findings identify the first wrong owner rather than creating more gates.

# First wrong owner

```text
wrong gameplay/story fact
→ PRD / upstream project authority

wrong Voice moment / Speaker / Channel / Trigger / Purpose / required communication / authoritative timing truth
→ Flow 5 voice-requirements.md

correct requirement but stiff/weak wording, thought groups, Estimated Duration, or performance direction
→ Flow 6 / SoundMaker / voice-production.md

correct canonical script but wrong Production Assets HTML
→ kits/prd-creator/renderer/ shared 04 compositor owner

correct script but actual generated-audio-only issue
→ Generation Mode evidence/settings/voice/surface/context
```

Do not repair an upstream problem by making the prompt more complicated.

# Bounded revision

Revise only invalidated scope.

```text
specific line change
→ affected Voice ID
→ Naturalness + Communication Conservation
→ adjacent continuity only if materially affected
→ update canonical/derived output
→ stop
```

A speaker-wide identity change may invalidate all lines for that speaker; a project-wide communication rule may invalidate broader scope. Do not replay unaffected Voice IDs for ceremony.

# Preparation Mode stop gate

Preparation is complete when:

- every requested Voice ID is script-ready;
- Naturalness and Communication Conservation pass for changed/current prepared scope;
- integrated Voice Script Readiness passes;
- required Target Voice Profiles exist when actual voices are not yet selected;
- material pronunciation risks are identified honestly;
- canonical script and requested derived output are current;
- no audio-quality or measured-duration claim is made.

Stop. Do not continue adding optional tags, schemas, artifacts, proof layers, or speculative hardening after current preparation scope is ready.

# Generation surface selection

Before generation, inspect only the relevant approved Moment relationships.

### Text to Speech

Use for an independent Voice ID whose performance does not materially require a preceding/following speaker turn.

For connected same-speaker sequences that must remain separate VO generations, supply relevant continuity context when the active API/workflow supports it.

### Text to Dialogue

Use when all are true:

- two or more speakers are involved;
- the Voice IDs belong to the same approved Moment;
- turn order matters;
- later delivery materially responds to earlier turns.

Preserve each canonical prompt exactly as one Dialogue turn. Use `references/elevenlabs/v3-dialogue-generation.md` for request limits, candidates, timestamps, and evidence.

### ElevenCreative Studio

Use for long-form/editorial/timeline production when section-level regeneration, locking/history, captions, or timeline assembly materially helps. Do not treat legacy Voiceover Studio controls as current policy.

# Generation Mode handoff

Before generation, know:

```text
Model: Eleven v3
Surface: Text to Speech | Text to Dialogue | ElevenCreative Studio
Speaker(s): exact project speaker(s)
Voice(s): actual ElevenLabs voice selection(s)
Voice fit: reviewed
Stability: Natural | project-calibrated
Speed: 1.0 / unchanged when available | project-calibrated
Prompt(s): exact reviewed canonical revision(s)
Continuity context: isolated | previous/next text | adjacent request IDs | Dialogue context
Timing: none | target range | hard max | fixed-sync
Authoritative timing constraint: none | known
Pronunciation: normal | special setup required
Enhance: OFF unless rewritten output was explicitly re-reviewed
```

For Dialogue, also know the exact ordered constituent Voice IDs and keep the request within the current reliable endpoint limits. Use the timestamps endpoint only when generated synchronization evidence materially helps.

For sequential TTS API work, use `previous_text`/`next_text` or adjacent request IDs only when they improve real continuity. Context is not another spoken/canonical field.

Use the operator handoff contract above. Do not create a second handoff file by default.

# After generation

Use this section only when actual audio work is requested.

Evaluate the heard result for meaning/intelligibility, voice identity, naturalness, emotional movement, pacing/breath, emphasis/landing, pronunciation, and requested duration. For Dialogue, also evaluate turn-to-turn reaction/timing and the complete exchange.

| Heard problem | First action |
|---|---|
| one isolated glitch/distortion | review alternate take / eligible same-prompt regeneration |
| stiff / robotic but intelligible | inspect voice fit → written-language residue → thought-group rhythm → missing context → over-direction before settings |
| clean but flat | strengthen textual beat/emotional context; add one precise direction if needed; then consider Creative |
| chaotic / overacted / synthetic | remove redundant tags/CAPS/ellipses; restore Natural baseline; inspect voice mismatch |
| whisper / volume / tone / accent drift | inspect Stability + voice fit; long-form may route to current Studio/sectioned production |
| same emotional cue repeatedly ignored | treat as voice-fit problem before adding tags |
| connected short line sounds detached | add relevant previous/next context or use Dialogue when response-dependent; do not add filler |
| individual lines sound fine but conversation feels disconnected | use/review Text to Dialogue surface before rewriting all turns |
| wrong pronunciation | pronunciation control, not emotional rewrite |
| too long | reduce spoken load / word budget first; use Speed only if the active surface supports it and the adjustment remains natural |
| too short but natural | do not add filler unless external timing requires it |

A single odd take does not prove the prompt is wrong. For both TTS and Dialogue, compare available same-content candidates/regenerations before changing correct wording solely because of one nondeterministic result.

## Revision discipline

Preserve what already worked. Diagnose in this order:

```text
meaning
→ voice fit
→ speakability / written-language residue
→ thought-group density / sentence rhythm
→ continuity context
→ punctuation / CAPS
→ Audio Tags
→ pronunciation
→ Stability
→ Speed when actually needed/available
→ generation surface / candidate variance
```

Resolve known issues coherently instead of producing many tiny revisions.

## Approval lock

When the user says **APPROVED**:

1. exact prompt actually generated becomes approved wording for that Voice ID;
2. a user-edited generated prompt supersedes the assistant draft;
3. synchronize it into `work/voice-production.md`;
4. rebuild/reopen only affected derived scope when wording changed;
5. record actual duration/pronunciation/settings only when evidence exists;
6. for an approved Dialogue take, keep each constituent `VO-...` prompt canonical and retain generation-group/timestamp evidence only where useful;
7. retain continuity-context/request evidence only when it improves reproducibility or later regeneration;
8. reuse approved behavior as project calibration, never as new project facts.

# References

Open only when needed:

- stiffness / natural speech / narration / continuity craft → `references/elevenlabs/v3-naturalness.md`;
- tags/non-tag text controls → `references/elevenlabs/v3-performance-writing.md`;
- target duration → `references/elevenlabs/v3-duration-planning.md`;
- Text to Dialogue / candidate selection / timestamps → `references/elevenlabs/v3-dialogue-generation.md`;
- voice/Voice Design/Stability/Speed/Studio/troubleshooting/pronunciation → `references/elevenlabs/v3-production-reference.md`;
- evidence provenance → `references/elevenlabs/source-register.md`.