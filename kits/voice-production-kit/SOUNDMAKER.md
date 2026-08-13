# SoundMaker — Eleven v3 Execution Mode

Status: active Flow 6 execution procedure  
Model scope: **Eleven v3 only**

## Purpose

SoundMaker turns approved Voice Requirements into production-ready Eleven v3 wording without creating a second source of truth.

```text
Voice Requirement
→ SoundMaker
→ canonical work/voice-production.md
→ optional generation / feedback / approval
```

`work/voice-production.md` remains the canonical wording owner.

# Operating modes

## Preparation Mode

Use when the task is to design, improve, or review Voice Production **without generating audio yet**.

```text
all Voice Requirements
→ per-line SoundMaker construction
→ cross-line continuity / anti-repetition
→ duration / pronunciation planning
→ canonical script
→ optional DOCX / script-level handoff
```

Preparation Mode rules:

- do **not** request audio generation/testing merely to finish preparation;
- do not require `APPROVED` per line;
- actual ElevenLabs voice selection is optional when a clear Target Voice Profile can be derived;
- do not invent audio evidence, measured duration, pronunciation proof, or project calibration;
- batch preparation is allowed, but every Voice ID remains independently traceable to Flow 5.

## Generation Mode

Use only when the user wants actual ElevenLabs generation, revision from a heard take, or audio approval.

```text
one active Voice ID
→ one exact reviewed prompt
→ generate
→ APPROVED or specific feedback
→ canonical sync / revise
```

One-at-a-time applies to **Generation Mode only**.

# Output contract

## Canonical output

The canonical entry in `work/voice-production.md` contains only:

```text
### <VOICE-ID> — <Title>
Type: <Flow 5 type>
Speaker: <Flow 5 speaker>
Estimated Duration: <range>

```performance
<exact Eleven v3 text>
```
```

`Type` and `Speaker` must match Flow 5. The `performance` block is the exact generation text, not commentary about it.

Keep Channel, Trigger, Purpose, requirement bullets, source refs, WPM math, performance-map reasoning, voice-fit ratings, and QA checklists in their owning/internal context rather than duplicating them here.

## Operator-facing handoff

When showing a prompt to the ElevenLabs operator, show only what helps execute the generation.

Project/speaker-level setup may be stated **once** when useful:

```text
Speaker: <character>
Voice: <selected ElevenLabs voice | target voice profile during Preparation Mode>
Model: Eleven v3
Stability: Natural | project-calibrated
Surface: Speech Synthesis | Studio when applicable
```

Per active line:

````markdown
## <VOICE-ID> — <Title>
Speaker: <speaker>
Estimated Duration: <range>

```text
<exact text to paste into ElevenLabs>
```
````

Inside the prompt block include **only** content Eleven v3 should receive.

Add an external production note only when the operator must take an extra action, such as:

- pronunciation dictionary/setup;
- Fixed Duration / hard sync;
- Studio instead of Speech Synthesis;
- another explicit UI control required by the current plan.

Do not expose internal reasoning/checklists by default.

# Fixed operating boundary

- model is **Eleven v3**;
- keep SFX/environment generation outside this Voice lane;
- do not switch model families to repair a weak v3 voice;
- missing project facts go upstream instead of being invented in dialogue;
- approved generated wording must synchronize back into `work/voice-production.md`.

# Context recovery before asking

Recover project facts before asking the user:

1. matching `work/voice-requirements.md` entry;
2. accepted `work/content.md` / current PRD meaning;
3. existing canonical `work/voice-production.md` when revising;
4. approved same-project wording/settings/pronunciation evidence when it exists;
5. relevant Eleven v3 reference only for production technique.

Ask only when a **material creative/production decision remains unresolved** and cannot be recovered safely.

# Eleven v3 defaults

Unless stronger approved project evidence exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance on directed SoundMaker prompt: OFF
```

### Surface

Use Speech Synthesis / Text to Speech normally.

Use Studio with Eleven v3 when long-form input develops continuity problems such as unintended whispering, volume/tone drift, accent drift, or breaking/distortion. Studio is a surface change, not a model fallback.

### Enhance

```text
plain / untreated dialogue
→ Enhance may be used as a drafting aid

SoundMaker-directed prompt
→ Enhance OFF by default
```

Any Enhance/UI rewrite creates a **new draft** that must be re-reviewed before generation.

### Stability

- move toward **Creative** only after voice fit, writing, and beat structure are sound and more range is still needed;
- use **Robust** only when stability/consistency is the actual need and reduced directional response is acceptable;
- do not change voice, Stability, wording, punctuation, and tags all at once after one weak take.

# Per-line construction

## 1. Understand the moment

Resolve internally:

```text
speaker
listener
trigger
must communicate
must not add/repeat
listener response
```

Only player-relevant information becomes spoken text.

## 2. Plan duration when timing matters

Classify before writing:

- **target range** — approximate; naturalness first;
- **hard maximum** — must stay below the cap;
- **fixed-sync** — external timeline.

Use `references/elevenlabs/v3-duration-planning.md`.

Do not rescue an oversized script later with `[rushed]`, tag spam, or forced speed.

## 3. Define the voice requirement

If an actual ElevenLabs voice is selected, evaluate its **Voice Performance Envelope**:

```text
Identity   → age / timbre / persona
Baseline   → neutral / warm / theatrical / energetic / restrained
Emotion    → required emotional range
Projection → quiet / normal / shout range
Pacing     → reflective / natural / urgent range
Language   → language / accent compatibility
Risk       → drift / monotone / weak shouting / pronunciation / etc.
```

Result:

- **GOOD FIT**;
- **LIMITED FIT**;
- **RISKY FIT**;
- **UNKNOWN**.

If no actual voice is selected in Preparation Mode, derive a **Target Voice Profile** from the same dimensions. `VOICE NOT SELECTED` is not a preparation blocker when that profile is clear.

Do not invent a commercial voice name merely to finish preparation or compensate for poor fit with tag stacking.

## 4. Map the performance

Only change emotional state when the scene/communication function changes.

Typical long-form shape:

```text
initial state
→ new information
→ reaction
→ escalation / release
→ instruction / payoff / landing
```

A simple warning or acknowledgement may correctly use one stable state.

## 5. Write spoken beats

Write speech before tags.

Prefer:

- one main idea/action per beat;
- natural spoken wording;
- active verbs;
- listener-first information order;
- short enough sentences for key thoughts to land;
- exact approved terminology.

Avoid specification prose, hidden implementation detail, filler, and multiple critical instructions buried in one long sentence.

The line must remain understandable with all Audio Tags removed.

## 6. Add textual performance controls

Use this order:

```text
sentence boundaries
→ punctuation
→ line / paragraph structure
→ selective CAPS
```

Production interpretation:

- `.` — complete thought / new beat;
- `,` — related material in one thought;
- `?` — questioning contour;
- `!` — textual intensity;
- `...` — hesitation / suspense / weight;
- `—` — hard pivot / interruption;
- line breaks — phrasing/beat boundaries;
- CAPS — selective emphasis.

These are performance cues, not exact timing commands.

## 7. Add minimal Audio Tags

Detailed tag knowledge lives in `references/elevenlabs/v3-performance-writing.md`.

```text
0–1 simultaneous tag → default
2 tags                → valid when dimensions differ and are compatible
3 tags                → exception; preferably project-calibrated
4+ tags               → reject by default
```

Place direction close to the intended beat. Do not assume a tag lasts exactly N words or until the next tag. Reactions are timeline events, not decoration.

## 8. Protect pronunciation

Use the smallest reliable control:

```text
ordinary word
→ normal text

number / acronym / symbol
→ explicit spoken form when ambiguity matters

isolated unusual proper noun
→ inline v3 IPA when needed

repeated project term
→ project pronunciation note / dictionary when appropriate

heard + approved
→ project-calibrated lock
```

Preparation may identify risk without claiming it verified.

## 9. Per-line preparation gate

A line is **script-ready** when:

- project meaning is correct;
- Voice ID/scope are unchanged;
- target duration is plausible when relevant;
- exact `Speaker` is known from Flow 5;
- selected voice fit is acceptable/risk is explicit, or a clear Target Voice Profile exists;
- wording is natural and beat changes have scene reasons;
- punctuation/CAPS are intentional;
- tags are minimal/audible;
- no SSML `<break>` is used;
- SFX/environment instructions are absent;
- material pronunciation risk is identified;
- exact canonical wording revision is known.

Generation readiness additionally requires an intentionally selected actual voice and current generation settings.

# Project-level preparation pass

After requested lines are drafted, review across Voice IDs.

## Speaker continuity

For each recurring speaker preserve a coherent internal profile:

```text
identity / persona
baseline energy
normal sentence style
allowed emotional range
language / accent expectation
recurring pronunciation
known performance risks
```

Do not create a separate speaker-bible file unless a concrete project need requires one.

## Anti-repetition / anti-template

Check nearby same-speaker/gameplay-family lines for accidental reuse of:

- identical openings;
- identical beat chains;
- identical Audio Tag placement;
- identical CAPS climax pattern;
- identical sentence rhythm;
- identical closing/catchphrase structure.

Preserve character identity while varying structure only when repetition is not intentional.

## Information progression

- briefing introduces what is needed at that stage;
- reminder repeats the minimum actionable fact;
- success line acknowledges the result instead of replaying the briefing;
- later lines do not re-explain already-learned information without trigger justification.

## Preparation Mode stop gate

Preparation is complete when:

- every requested Voice ID has script-ready canonical wording;
- every entry has exact `Type`, `Speaker`, Estimated Duration, and performance text;
- not-yet-selected voices have a clear Target Voice Profile where relevant;
- speaker continuity/information progression pass;
- accidental template repetition is removed or intentional;
- pronunciation risks are identified;
- no audio-quality or measured-duration claim is made.

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

Use the operator-facing output contract above. Do not add a second handoff file by default.

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
