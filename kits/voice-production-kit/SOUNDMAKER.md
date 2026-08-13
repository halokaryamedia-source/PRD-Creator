# SoundMaker — Eleven v3 Execution Mode

Status: active Flow 6 execution procedure  
Model scope: **Eleven v3 only**

## Purpose

SoundMaker turns **one approved Voice Requirement at a time** into one generation-ready Eleven v3 prompt, then helps diagnose the heard result without creating a second source of truth.

```text
Voice Requirement
→ SoundMaker
→ exact Eleven v3 prompt
→ canonical work/voice-production.md
→ optional generation / feedback / approval
```

`work/voice-production.md` remains the canonical wording owner.

## Default user experience

Normal production stays simple:

```text
one Voice ID
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

## Fixed operating boundary

- model is **Eleven v3**;
- keep SFX/environment generation outside this Voice lane;
- do not switch model families to repair a weak v3 voice;
- missing project facts go upstream instead of being invented in dialogue;
- approved generated wording must synchronize back into `work/voice-production.md`.

## Generation surface

Use **Speech Synthesis / Text to Speech** as the normal surface.

Use **Studio with Eleven v3** when long-form text begins to show continuity problems such as unintended whispering, volume/tone drift, accent drift, or breaking/distortion, especially once the input is already several hundred characters. Studio is a production-surface change, not a model fallback.

Do not move to Studio merely because a line is long if normal v3 TTS is already stable and easy to review.

## Enhance policy

SoundMaker already performs deliberate Audio Tag, CAPS, punctuation, and phrasing direction.

Therefore:

```text
plain / untreated dialogue
→ Enhance may be used as a drafting aid

SoundMaker-directed prompt
→ Enhance OFF by default
```

If Enhance or another UI rewrite changes a SoundMaker prompt, treat the result as a **new draft**. Re-review it before generation. Never assume an automatic rewrite preserves the intended performance.

## Default v3 setting

Unless stronger approved project evidence exists:

```text
Model: Eleven v3
Stability: Natural
```

- move toward **Creative** only when voice fit + writing + beat structure are already sound and more range is still needed;
- use **Robust** only when stability/consistency is the actual requirement and reduced directional response is acceptable;
- do not depend on a Speed control as a required v3 mechanism; use the live UI as authority for control availability;
- do not change voice, Stability, wording, punctuation, and tags all at once after one weak take.

# Execution path

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

## 3. Check the Voice Performance Envelope

Judge only what matters for this line:

```text
Identity     → age / timbre / persona still suitable?
Baseline     → neutral / warm / theatrical / energetic / restrained?
Emotion      → can it cover the required emotional states?
Projection   → quiet / normal / shout range needed?
Pacing       → reflective / natural / urgent range needed?
Language     → language/accent compatible?
Known risk   → drift, weak shouting, monotone, pronunciation, etc.?
```

Internal result:

- **GOOD FIT** — required range is naturally plausible;
- **LIMITED FIT** — usable if the line stays inside a narrower range;
- **RISKY FIT** — the required performance repeatedly exceeds the voice;
- **UNKNOWN** — insufficient evidence.

Do not compensate for a risky voice with synonym stacks such as `[excited][energetic][enthusiastic][intense]`.

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
- line breaks — visible phrasing/beat boundaries;
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

Reactions such as sighs, gasps, laughs, gulps, and hesitation are timeline events, not decoration.

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

## 9. Pre-generation gate

A prompt is `Ready to generate` only when:

- project meaning is correct;
- Voice ID/scope are unchanged;
- target duration is plausible when timing matters;
- voice fit is acceptable or its risk is explicit;
- spoken wording is natural;
- beat changes have scene reasons;
- punctuation/CAPS are intentional;
- tags are minimal and audible;
- no SSML `<break>` is used;
- SFX/environment instructions are absent;
- material pronunciation risk is handled;
- the exact prompt revision is known.

If a material issue remains, show a review draft rather than encouraging generation.

## 10. Generate with a known setup

Immediately before generation, know:

```text
Model: Eleven v3
Surface: Speech Synthesis | Studio
Voice: selected intentionally
Stability: Natural | project-calibrated
Prompt: exact reviewed revision
Timing: none | range | hard max | fixed-sync
Pronunciation risk: resolved | pending audio review
Enhance: OFF unless its output was explicitly re-reviewed
```

# After generation

## Hear the result, then classify the failure

Evaluate the actual take for:

- meaning / intelligibility;
- voice identity;
- emotional movement;
- pacing / breath;
- emphasis / landing;
- naturalness;
- pronunciation;
- requested duration.

Use this diagnosis order:

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

When text and settings remain identical and the current ElevenLabs surface offers an eligible free regeneration/alternative, use that before making a paid micro-edit.

## Revision rule

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

Resolve known issues coherently instead of producing many tiny paid-generation revisions.

## Approval lock

When the user says **APPROVED**:

1. the exact prompt actually generated becomes approved wording for that Voice ID;
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
