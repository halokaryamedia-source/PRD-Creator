# SoundMaker — Eleven v3 Execution Mode

Status: active Flow 6 execution procedure  
Model scope: **Eleven v3 only**

## Purpose

SoundMaker turns approved Voice Requirements into production-ready Eleven v3 wording without creating a second source of truth.

```text
Voice Requirement
→ complete the communication/performance intent
→ write one exact Eleven v3 prompt
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
→ optional DOCX / script-level handoff
```

Preparation Mode:

- may process the full current Voice scope in one bounded pass;
- does **not** require audio generation/testing or `APPROVED` per line;
- may use a Target Voice Profile when an actual ElevenLabs voice is not selected yet;
- does not invent measured duration, pronunciation proof, audio quality, or project calibration.

## Generation Mode

Use only when actual ElevenLabs generation, heard-take revision, or audio approval is requested.

```text
one active Voice ID
→ one exact reviewed prompt
→ generate
→ feedback / APPROVED
→ canonical sync or bounded revision
```

One-at-a-time applies to Generation Mode only.

# Output contract

## Canonical entry

`work/voice-production.md` contains only stable operator-useful metadata plus the exact Eleven v3 text:

```text
### <VOICE-ID> — <Title>
Type: <Flow 5 type>
Speaker: <Flow 5 speaker>
Estimated Duration: <range>

```performance
<exact Eleven v3 text>
```
```

`Type` and `Speaker` must match Flow 5. The performance block is the exact generation payload, not commentary about it.

Keep Channel, Trigger, Purpose, requirement bullets, source refs, reasoning, WPM math, voice-fit ratings, and QA notes in their owning/internal context rather than duplicating them into every entry.

## Operator handoff

State shared setup once when useful:

```text
Speaker: <character>
Voice: <selected voice | target voice profile during preparation>
Model: Eleven v3
Stability: Natural | project-calibrated
Surface: Speech Synthesis | Studio when applicable
```

Then show each active line with Voice ID/Title, Speaker, Estimated Duration, and one exact prompt block. Add an external production note only when the operator must take an extra action such as pronunciation setup, Fixed Duration, or Studio routing.

Never place internal reasoning or operator instructions inside the Eleven v3 prompt.

# Authority and decision boundary

Recover current project facts before asking the user:

1. matching `work/voice-requirements.md` entry;
2. accepted `work/content.md` / current PRD meaning;
3. current `work/voice-production.md` when revising;
4. approved same-project wording/settings/pronunciation evidence when it exists;
5. Eleven v3 references only for production technique.

Separate these two classes:

### Production interpretation — SoundMaker may decide

Examples:

- spoken phrasing and sentence split;
- beat structure;
- punctuation / line breaks / selective CAPS;
- Audio Tag choice/placement;
- performance pacing within the approved communication intent;
- duration-conscious compression that preserves required meaning.

These do not need a new user approval step merely because the AI made a craft decision.

### Material creative/project decision — return upstream when unresolved

Examples:

- changing the speaker's established personality;
- inventing a new accent/identity that materially defines the character;
- changing Voice scope, Trigger, Channel, objective meaning, mechanic, reward, lore, or outcome;
- dropping a required communication fact because it does not fit the desired duration.

Do not hide an upstream decision inside performance polish.

# Eleven v3 defaults

Unless stronger approved project evidence exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance on directed SoundMaker prompt: OFF
```

Use Studio with Eleven v3 only when long-form Speech Synthesis develops material continuity problems such as unintended whispering, volume/tone drift, accent drift, or breaking/distortion.

Enhance may help untreated text as a drafting aid. An already-directed SoundMaker prompt keeps Enhance OFF by default; any UI rewrite becomes a new draft requiring review.

Move toward Creative only after voice fit, wording, and beat structure are sound and more expressive range is genuinely needed. Use Robust when stability/consistency is the actual priority and reduced directional response is acceptable.

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

Derive these answers from current authority. Ask only if a material unresolved decision prevents a responsible answer.

A short/simple line does not need artificial complexity. If one stable state and one clear action are sufficient, keep it that way.

## 2. Duration planning when timing matters

Resolve timing before final wording:

- **target range** — approximate; naturalness first;
- **hard maximum** — stay below the cap;
- **fixed-sync** — fit an external timeline.

Use `references/elevenlabs/v3-duration-planning.md` only when timing is material.

Do not write an oversized script and rescue it afterward with `[rushed]`, tag spam, or forced speed. Duration pressure may simplify wording; it may not silently delete required communication.

## 3. Voice requirement / Target Voice Profile

If an actual voice is selected, judge only the required performance envelope:

```text
identity / timbre / persona
baseline tone / energy
required emotional range
projection range
pacing range
language / accent compatibility
material pronunciation or drift risk
```

Internal result may be `GOOD FIT`, `LIMITED FIT`, `RISKY FIT`, or `UNKNOWN`.

If no voice is selected in Preparation Mode, derive a Target Voice Profile from the same dimensions. `VOICE NOT SELECTED` is not a preparation blocker when that profile is clear.

Do not invent a commercial voice name to finish preparation or compensate for risky fit with direction stacks.

## 4. Write the performance

Write spoken text before tags.

### Spoken beats

Prefer:

- one main idea/action per beat;
- natural spoken wording and active verbs;
- listener-first information order;
- short enough sentences for key thoughts to land;
- exact approved terminology.

Avoid specification prose, hidden implementation detail, filler, and several critical instructions inside one long sentence.

### Performance shape

Only change emotional state when the scene or communication function changes.

A long line may use a shape such as:

```text
initial state
→ new information
→ reaction
→ escalation / release
→ instruction / payoff / landing
```

A simple warning or acknowledgement may correctly remain in one stable state.

### Textual controls before extra tags

Use this order:

```text
sentence boundaries
→ punctuation
→ line / paragraph structure
→ selective CAPS
→ minimal Audio Tags
```

Interpretation:

- `.` — complete thought / new beat;
- `,` — related material in one thought;
- `?` — questioning contour;
- `!` — textual intensity;
- `...` — hesitation / suspense / weight;
- `—` — hard pivot / interruption;
- line breaks — phrasing/beat boundaries;
- CAPS — selective emphasis.

These are performance cues, not exact timing commands.

### Audio Tags

Detailed tag knowledge stays in `references/elevenlabs/v3-performance-writing.md`.

```text
0–1 simultaneous tag → default
2 tags                → valid when dimensions differ and are compatible
3 tags                → exception; preferably project-calibrated
4+ tags               → reject by default
```

Place direction close to the beat it affects. Do not assume a fixed tag-persistence window. Reactions are timeline events, not decoration.

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

## 5. Communication Conservation

After the prompt is written or shortened, compare it back to the Flow 5 requirement.

A line passes only when:

- every independently actionable `Must communicate` fact that belongs in this moment still has a clear spoken representation;
- every `Must not add/repeat` guardrail remains respected;
- required names, mechanics, result/state, sequence, and terminology retain their meaning;
- performance polish did not introduce a new project fact;
- duration compression did not hide or delete required communication.

Paraphrase and merge are allowed when the resulting speech still communicates the same material meaning clearly. Concision is not permission to thin requirements.

Do **not** create a persisted requirement-to-sentence mapping. This is a reasoning gate over the current requirement and prompt.

## 6. Per-line script-ready gate

A line is script-ready when:

- Voice Intent Completeness is sufficient for responsible writing;
- project meaning and Voice ID scope are intact;
- Type and Speaker remain exact Flow 5 values;
- target duration is plausible when relevant;
- selected voice fit is acceptable/risk is explicit, or a clear Target Voice Profile exists;
- wording and performance shape are natural and justified;
- punctuation/CAPS/tags are purposeful and minimal;
- no SSML `<break>` or SFX/environment instruction is present;
- material pronunciation risk is identified;
- **Communication Conservation passes**;
- exact canonical wording revision is known.

Generation readiness additionally requires an intentionally selected actual voice and current generation settings.

# Integrated Voice Script Readiness

After all requested lines are script-ready, perform **one project-level semantic review**. Do not turn the lenses below into separate workflow stages, scorecards, or artifacts.

| Lens | Ready when... |
|---|---|
| Communication | Required meaning survives clearly and no unsupported meaning was added. |
| Listener | Each line fits the player's state and gives the right amount of information/action at that moment. |
| Character | Recurring speakers remain recognizable without forcing every line into the same template. |
| Performance | Emotional movement, beat shape, punctuation, CAPS, and tags serve the scene rather than decorate it. |
| Timing | Estimated duration/density is plausible and no required fact was sacrificed to fit it. |
| Continuity | Information progresses; nearby lines do not mechanically repeat openings, beat chains, tag positions, CAPS climaxes, rhythms, or closings without reason. |
| Operator | Speaker ownership, duration, exact prompt, and any special action are clear enough to use without guessing. |

Speaker continuity and structural variety are reviewed together: preserve character identity, but vary structure when repetition is accidental rather than intentional character/gameplay language.

Briefings introduce what is needed, reminders repeat only the minimum actionable fact, and success lines acknowledge results rather than replaying the briefing.

The review result is conceptually one decision: **Voice Script Readiness: PASS | FAIL**. Findings identify the first wrong owner rather than creating more gates.

# First wrong owner

When a finding appears, fix the earliest owner that is actually wrong:

```text
wrong gameplay/story fact
→ PRD / upstream project authority

wrong Voice moment / Speaker / Channel / Trigger / required communication
→ Flow 5 voice-requirements.md

correct requirement but weak wording/performance/duration
→ Flow 6 / SoundMaker / voice-production.md

correct canonical script but wrong DOCX presentation
→ DOCX builder / DOCX-FORMAT.md

correct script but actual generated-audio-only issue
→ Generation Mode evidence/settings/voice
```

Do not repair an upstream problem by making the prompt more complicated.

# Bounded revision

Revise only invalidated scope.

```text
specific line change
→ affected Voice ID
→ Communication Conservation
→ adjacent/project continuity only if materially affected
→ update canonical/derived output
→ stop
```

A speaker-wide identity change may invalidate all lines for that speaker; a project-wide communication rule may invalidate broader scope. Do not replay unaffected Voice IDs for ceremony.

# Preparation Mode stop gate

Preparation is complete when:

- every requested Voice ID is script-ready;
- Communication Conservation passes for changed/current prepared scope;
- integrated Voice Script Readiness passes;
- required Target Voice Profiles exist when actual voices are not yet selected;
- material pronunciation risks are identified honestly;
- canonical script and requested derived output are current;
- no audio-quality or measured-duration claim is made.

Stop. Do not continue adding optional tags, schemas, artifacts, proof layers, or speculative hardening after current preparation scope is ready.

# Generation Mode handoff

Before generation, know:

```text
Model: Eleven v3
Surface: Speech Synthesis | Studio
Speaker: exact project speaker
Voice: actual voice selected intentionally
Voice fit: reviewed
Stability: Natural | project-calibrated
Prompt: exact reviewed revision
Timing: none | range | hard max | fixed-sync
Pronunciation: normal | special setup required
Enhance: OFF unless rewritten output was explicitly re-reviewed
```

Use the operator handoff contract above. Do not create a second handoff file by default.

# After generation

Use this section only when actual audio work is requested.

Evaluate the heard result for meaning/intelligibility, voice identity, emotional movement, pacing/breath, emphasis/landing, naturalness, pronunciation, and requested duration.

| Heard problem | First action |
|---|---|
| one isolated glitch/distortion | review alternate take / eligible same-prompt regeneration |
| clean but flat | fix spoken beats/textual directing; then consider Stability toward Creative |
| chaotic / overacted / erratic | inspect Stability and over-direction first |
| whisper / volume / tone / accent drift | inspect Stability + voice fit; long-form may route to Studio v3 |
| same emotional cue repeatedly ignored | treat as voice-fit problem before adding tags |
| wrong pronunciation | pronunciation control, not emotional rewrite |
| too long | reduce spoken load / word budget first |
| too short but natural | do not add filler unless external timing requires it |

A single odd take does not prove the prompt is wrong.

## Revision discipline

Preserve what already worked. Diagnose in this order:

```text
meaning
→ clarity
→ beat density
→ sentence rhythm / punctuation / CAPS
→ Audio Tags
→ pronunciation
→ Stability
→ voice fit / production surface
```

Resolve known issues coherently instead of producing many tiny revisions.

## Approval lock

When the user says **APPROVED**:

1. exact prompt actually generated becomes approved wording for that Voice ID;
2. a user-edited generated prompt supersedes the assistant draft;
3. synchronize it into `work/voice-production.md`;
4. rebuild/reopen only affected derived scope when wording changed;
5. record actual duration/pronunciation/settings only when evidence exists;
6. reuse approved behavior as project calibration, never as new project facts.

# References

Open only when needed:

- writing/tags/non-tag controls → `references/elevenlabs/v3-performance-writing.md`;
- target duration → `references/elevenlabs/v3-duration-planning.md`;
- voice/Stability/Enhance/Studio/troubleshooting/pronunciation → `references/elevenlabs/v3-production-reference.md`;
- evidence provenance → `references/elevenlabs/source-register.md`.
