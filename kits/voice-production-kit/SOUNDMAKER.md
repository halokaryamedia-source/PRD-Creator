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

Preparation Mode may process the full current Voice scope in one bounded pass:

```text
all Voice Requirements
→ per-line SoundMaker construction
→ cross-line continuity / anti-repetition pass
→ duration / pronunciation planning
→ canonical work/voice-production.md
→ DOCX / Flow 7 script-level readiness as requested
```

Rules:

- do **not** ask the user to generate/test audio merely to finish script preparation;
- do not require `APPROVED` per line when no actual generation is requested;
- actual ElevenLabs voice selection is optional during preparation when a clear target voice profile can be derived;
- do not invent audio evidence, measured duration, pronunciation proof, or project calibration;
- all lines still receive the same script-level quality gate;
- batch preparation is allowed, but every Voice ID remains independently traceable to Flow 5.

## Generation Mode

Use only when the user wants to generate, revise from a heard take, or approve actual ElevenLabs output.

```text
one active Voice ID
→ one best prompt
→ generate
→ APPROVED or specific feedback
→ lock or revise
```

Default visible result:

````markdown
## <VOICE-ID / TASK NAME>

```text
<exact text to paste into ElevenLabs>
```
````

Inside the code block include only text intended for ElevenLabs. Do not expose internal scoring/checklists unless requested.

If no approved project setting exists, state once outside the prompt:

```text
Eleven v3 · Stability: Natural
```

# Fixed operating boundary

- model is **Eleven v3**;
- keep SFX/environment generation outside this Voice lane;
- do not switch model families to repair a weak v3 voice;
- missing project facts go upstream instead of being invented in dialogue;
- approved generated wording must synchronize back into `work/voice-production.md`.

# Context recovery before asking

Before asking the user for information, recover it from current project authority in this order:

1. matching `work/voice-requirements.md` entry;
2. accepted `work/content.md` / current PRD meaning;
3. existing canonical `work/voice-production.md` when revising;
4. approved same-project wording/settings/pronunciation evidence when it exists;
5. relevant Eleven v3 reference only for production technique.

Ask only when a **material creative/production decision remains unresolved** and cannot be recovered safely. Do not ask for information already present in the project package.

# Generation surface

Use **Speech Synthesis / Text to Speech** as the normal surface.

Use **Studio with Eleven v3** when long-form text begins to show continuity problems such as unintended whispering, volume/tone drift, accent drift, or breaking/distortion, especially once the input is already several hundred characters. Studio is a production-surface change, not a model fallback.

Do not move to Studio merely because a line is long if normal v3 TTS is already stable and easy to review.

# Enhance policy

SoundMaker already performs deliberate Audio Tag, CAPS, punctuation, and phrasing direction.

```text
plain / untreated dialogue
→ Enhance may be used as a drafting aid

SoundMaker-directed prompt
→ Enhance OFF by default
```

If Enhance or another UI rewrite changes a SoundMaker prompt, treat the result as a **new draft**. Re-review it before generation.

# Default v3 setting

Unless stronger approved project evidence exists:

```text
Model: Eleven v3
Stability: Natural
```

- move toward **Creative** only when voice fit + writing + beat structure are already sound and more range is still needed;
- use **Robust** only when stability/consistency is the actual requirement and reduced directional response is acceptable;
- do not depend on a Speed control as a required v3 mechanism; use the live UI as authority for control availability;
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

## 2. Plan duration first when timing matters

Classify timing before writing:

- **target range** — approximate; naturalness first;
- **hard maximum** — must remain under the cap;
- **fixed-sync** — externally fixed timeline.

Use `references/elevenlabs/v3-duration-planning.md`.

Do not write an oversized script and rescue it later with `[rushed]`, tag spam, or forced speed.

## 3. Define the voice requirement

If an actual ElevenLabs voice is already selected, evaluate its **Voice Performance Envelope**.

```text
Identity     → age / timbre / persona suitable?
Baseline     → neutral / warm / theatrical / energetic / restrained?
Emotion      → required emotional range plausible?
Projection   → quiet / normal / shout range needed?
Pacing       → reflective / natural / urgent range needed?
Language     → language/accent compatible?
Known risk   → drift, weak shouting, monotone, pronunciation, etc.?
```

Result when a voice exists:

- **GOOD FIT** — required range is naturally plausible;
- **LIMITED FIT** — usable inside a narrower range;
- **RISKY FIT** — required performance repeatedly exceeds the voice;
- **UNKNOWN** — insufficient evidence.

If no actual voice is selected in Preparation Mode, derive a **Target Voice Profile** instead:

```text
speaker identity / persona
baseline tone / energy
required emotional range
projection range
pacing range
language / accent expectation
material pronunciation needs
```

`VOICE NOT SELECTED` is not a Preparation Mode blocker when the target profile is clear. Actual voice-fit validation is deferred to Generation Mode.

Do not invent a commercial voice name merely to complete preparation. Do not compensate for a risky selected voice with synonym stacks.

## 4. Map the performance

Only create emotional movement when the scene actually changes.

Typical long-form pattern:

```text
initial state
→ new information
→ reaction
→ escalation / release
→ instruction / payoff / landing
```

A simple warning or acknowledgement may correctly use one stable state.

## 5. Write spoken text and beats

Write speech before tags.

Prefer:

- one main idea/action per beat;
- natural spoken wording;
- active verbs;
- important information in listener order;
- short enough sentences for key thoughts to land;
- exact approved terminology.

Avoid specification prose, hidden implementation details, filler, and several critical instructions inside one long sentence.

The line must remain understandable with all Audio Tags removed.

## 6. Add textual performance controls

Use this order:

```text
sentence boundaries
→ punctuation
→ line / paragraph structure
→ selective CAPS
```

Use them semantically:

- `.` — complete thought / new beat;
- `,` — related material in one thought;
- `?` — questioning contour;
- `!` — textual intensity;
- `...` — hesitation / suspense / weight;
- `—` — hard pivot / interruption / dramatic break;
- line breaks — phrasing/beat boundaries;
- CAPS — selective spoken emphasis.

Do not treat punctuation or line breaks as exact timing commands.

## 7. Add minimal Audio Tags

Detailed tag knowledge lives in `references/elevenlabs/v3-performance-writing.md`.

Production heuristic:

```text
0–1 simultaneous tag → default
2 tags                → valid when dimensions differ and are compatible
3 tags                → exception; preferably project-calibrated
4+ tags               → reject by default
```

Place direction close to the intended beat. Do not assume a standard v3 tag lasts exactly N words or until the next tag.

Reactions are timeline events, not decoration.

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
→ lock as project calibration
```

Do not claim pronunciation is verified before actual evidence exists.

## 9. Per-line preparation gate

A line is **script-ready** when:

- project meaning is correct;
- Voice ID/scope are unchanged;
- target duration is plausible when timing matters;
- selected voice fit is acceptable/risk is explicit, **or** a clear Target Voice Profile exists when no voice is selected;
- spoken wording is natural;
- beat changes have scene reasons;
- punctuation/CAPS are intentional;
- tags are minimal and audible;
- no SSML `<break>` is used;
- SFX/environment instructions are absent;
- material pronunciation risk is identified/handled at the planning level;
- exact canonical wording revision is known.

Actual Generation Mode readiness additionally requires an intentionally selected voice and current generation settings.

# Project-level preparation pass

After all requested lines are drafted, review the project **across Voice IDs** before calling Preparation Mode complete.

## Speaker continuity

For each recurring speaker, preserve a coherent internal profile derived from project evidence:

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

## Anti-repetition / anti-template gate

Compare nearby lines from the same speaker or same gameplay family.

Look for accidental repetition of:

- identical openings (`Good work...`, `Now...`, `Listen...`);
- the same beat chain on every objective;
- the same Audio Tags at the same positions;
- the same CAPS climax pattern;
- the same sentence length/rhythm;
- the same closing catchphrase or instruction shape.

Preserve **character identity**, but vary the structure when repetition is not intentionally part of the character or gameplay language.

Do not force variety by changing approved facts or inventing personality traits.

## Information progression

Across sequential Voice IDs:

- briefing introduces only what is needed at that stage;
- reminders repeat the minimum actionable fact;
- success lines acknowledge the result rather than replaying the briefing;
- later lines do not re-explain information the player already learned unless repetition is justified by the trigger.

## Batch preparation stop gate

Preparation Mode is complete when:

- every requested Voice ID has **script-ready** canonical wording;
- any not-yet-selected actual voice has a clear Target Voice Profile where voice characteristics materially affect delivery;
- cross-line speaker continuity passes;
- obvious template repetition is removed or intentional;
- duration targets are planned honestly;
- material pronunciation risks are identified;
- no audio-quality claim or measured-duration claim is made.

# Generation Mode handoff

Immediately before actual generation, know:

```text
Model: Eleven v3
Surface: Speech Synthesis | Studio
Voice: actual voice selected intentionally
Voice fit: reviewed for required performance range
Stability: Natural | project-calibrated
Prompt: exact reviewed revision
Timing: none | range | hard max | fixed-sync
Pronunciation risk: resolved | pending audio review
Enhance: OFF unless its output was explicitly re-reviewed
```

# After generation

This section is used only when actual audio work is requested.

## Hear the result, then classify the failure

Evaluate the actual take for meaning/intelligibility, voice identity, emotional movement, pacing/breath, emphasis/landing, naturalness, pronunciation, and requested duration.

| Heard problem | First action |
|---|---|
| one isolated glitch/distortion | review alternate take / eligible same-prompt regeneration |
| clean but flat | fix spoken beats/textual directing; then consider Stability toward Creative |
| chaotic / overacted / erratic | inspect Stability and over-direction before rewriting everything |
| unintended whisper / volume / tone / accent drift | inspect Stability + voice fit; for long-form instability consider Studio v3 |
| same emotional cue repeatedly ignored | voice-fit problem before adding more tags |
| wrong pronunciation | pronunciation control, not emotional rewrite |
| too long | reduce spoken load / word budget before forcing faster delivery |
| too short but already natural | do not add filler unless external timing requires it |

Eleven v3 is nondeterministic. A single odd take does not prove the prompt is wrong.

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

Resolve known issues coherently instead of producing many tiny revisions. Do not reset a successful line from scratch unless the evidence requires it.

## Approval lock

When the user says **APPROVED**:

1. exact prompt actually generated becomes approved wording for that Voice ID;
2. a user-edited generated prompt supersedes the assistant draft;
3. synchronize it into `work/voice-production.md`;
4. rebuild DOCX/reopen affected Flow 7 evidence only when canonical wording changed;
5. record actual duration/pronunciation/settings only when evidence exists;
6. reuse approved behavior as project calibration, never as new project facts.

# References

Open only when needed:

- writing/tags/non-tag controls → `references/elevenlabs/v3-performance-writing.md`;
- target duration → `references/elevenlabs/v3-duration-planning.md`;
- voice/Stability/Enhance/Studio/troubleshooting/pronunciation → `references/elevenlabs/v3-production-reference.md`;
- evidence provenance → `references/elevenlabs/source-register.md`.
