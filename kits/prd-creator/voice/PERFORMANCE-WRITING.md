# SoundMaker — Eleven v3 Execution Mode

Status: active Flow 6 execution procedure  
Model scope: **Eleven v3 only**

## Purpose

SoundMaker turns approved Voice Requirements into production-ready Eleven v3 speech while preserving both **communication meaning** and **intended expression**.

```text
Voice Requirement
→ recover communication + performance intent
→ natural spoken-language rewrite
→ Expression Coverage
→ deliberate performance shaping
→ Communication + Expression Conservation
→ Voice Script Readiness
→ canonical work/voice-production.md
→ optional Generation Mode later
```

`work/voice-production.md` remains the sole canonical wording/performance owner.

# Operating modes

## Preparation Mode

Default when designing, improving, or reviewing Voice Production without generating audio.

Preparation Mode:

- may process the full current Voice scope in one bounded pass;
- does **not** require audio generation/testing or per-line `APPROVED`;
- may use a Target Voice Profile before an actual ElevenLabs voice is selected;
- may establish exact Audio Tags and performance architecture;
- does not claim measured duration, pronunciation proof, or heard-audio quality.

## Generation Mode

Use only when actual ElevenLabs generation, heard-take revision, or approval is requested.

```text
independent Voice ID
→ Eleven v3 Text to Speech

connected same-speaker narration split across requests
→ TTS + relevant previous/next context

same Moment + multiple speakers + response dependency
→ ordered existing Voice IDs
→ Eleven v3 Text to Dialogue

long-form editorial/timeline work
→ current ElevenCreative Studio when useful
```

Generation grouping/context is ephemeral. It does not create a Dialogue ID, duplicate canonical script, or replace existing `VO-...` identity.

# Canonical output contract

```text
# Voice Production
Source Voice Requirements: <revision> / work/voice-requirements.md | sha256:<sha>

Voice Cast:
- <Speaker>: <selected voice or target profile>

## <Gameplay Section>
Owner ID: <Flow 5 Owner ID>

### VO-... — <Title>
Type: <Flow 5 Type>
Speaker: <Flow 5 Speaker>
Estimated Duration: <range>

```performance
<exact Eleven v3 payload>
```
```

The `performance` block contains the exact generation payload. Audio Tags may be present wherever acting direction is required; a zero-tag line remains structurally valid when no material expression needs explicit direction.

Do not duplicate Trigger, Purpose, source refs, reasoning, expression maps, WPM math, generation-group metadata, or QA notes into every canonical entry.

# Authority and decision boundary

Recover current facts in this order:

1. matching `work/voice-requirements.md` entry;
2. accepted PRD/project meaning only when Flow 5 lacks delivery-relevant context;
3. current `work/voice-production.md` when revising;
4. approved same-project performance/pronunciation/settings evidence when it exists;
5. Eleven v3 references only for production technique.

Flow 5 defines what must be communicated and the approved moment. Flow 6 owns reversible performance craft inside that boundary.

### SoundMaker may decide

- spoken phrasing, contractions, sentence split, and context-aware compression;
- thought groups and beat architecture;
- performance baseline/shape/landing when upstream meaning does not prescribe them;
- Audio Tag choice, placement, transitions, and reactions;
- punctuation / line breaks / selective CAPS;
- Estimated Duration;
- Target Voice Profile / actor fit assessment;
- Stability / supported Speed use;
- TTS vs Text to Dialogue vs Studio routing;
- previous/next generation context when it affects prosody only.

### Return upstream when unresolved

- changing established character identity/personality;
- inventing a material accent/relationship/lore fact;
- changing Voice scope, Speaker, Channel, Trigger, Purpose, mechanic, reward, outcome, or authoritative timing truth;
- deleting required communication because it is hard to perform.

# Eleven v3 baseline

Unless stronger approved project evidence exists:

```text
Model: Eleven v3
Stability: Natural
Speed: 1.0 / unchanged when the active surface exposes it
Enhance on SoundMaker-reviewed prompt: OFF
Surface: Text to Speech for independent speech
Audio Tags: deliberate expression controls, not boilerplate
```

Use Creative only when greater range/variance is intentionally useful after voice fit and prompt architecture are sound. Use Robust when consistency is more important than directional responsiveness.

# Preparation quality model

## 1. Voice Intent Completeness

Map Flow 5 into one internal performance picture:

```text
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

Then recover only genuinely missing delivery context such as established speaker characterization or scene state.

Do not invent a hard timing limit when Flow 5 has none. Do not reopen the full PRD merely to make prose richer.

## 2. Natural spoken-language pass

First make the line **speakable**.

```text
requirement meaning
→ what would this speaker plausibly say here?
→ remove document/specification scaffolding
→ organize into natural thought groups
→ preserve every required fact
```

Prefer:

- direct spoken verbs;
- listener-first information order;
- context-aware references when unambiguous;
- contractions when appropriate to language/register;
- sentence-length variation driven by thought complexity;
- exact project terminology only where needed;
- clean landings.

Avoid:

- accidental PRD language such as `the player must`, `in order to`, `upon completion of` unless character-appropriate;
- repeated context already obvious from the trigger;
- uniform sentence rhythm;
- fake-human filler, slang, stutters, ellipses, fragments, or sighs without scene/character reason;
- several critical instructions inside one long sentence.

Naturalness is register-correct, not universally casual.

Detailed stiffness/narration craft: `references/elevenlabs/v3-naturalness.md`.

## 3. Expression Coverage

After the spoken text is natural, preserve acting deliberately.

Use the internal Expression Coverage Map from `references/elevenlabs/v3-expression-direction.md`:

```text
Baseline State
Emotion
Attitude / Subtext
Projection
Pace / Rhythm
Intensity / Energy
Cognitive State
Reaction Event
Transition Points
Landing
```

Do not persist another schema.

### Core rule

```text
material expression sufficiently explicit in voice + text + punctuation + immediate context
→ no redundant tag required

material expression ambiguous / under-directed
→ add a precise Audio Tag near the affected beat
```

If emotion, subtext, projection, pacing, reaction, or a state transition is **important to the intended performance**, prefer explicit direction rather than hoping v3 infers the same interpretation.

This means:

- zero tags can be correct for a truly baseline informational line;
- an expressive line normally carries at least one relevant direction;
- a dynamic line uses transition tags where acting changes;
- reactions are placed at the event point;
- tag count is never the goal—**expression coverage is**.

### Opening state

A prompt has no mechanical opening-tag requirement. But if the opening performance state materially matters, establish it explicitly.

```text
material opening state
→ opening tag by craft

no material opening state
→ zero-tag opening valid
```

### Dynamic performance

```text
[reflective]
I thought this place was abandoned.

[uneasy]
Then the lights came back on.

[urgent]
We need to move. Now.
```

Do not assign a new emotion merely because a sentence changes.

### Tag combinations

Repository heuristic:

```text
1 tag               → preferred when sufficient
2 simultaneous tags → valid for different compatible dimensions
3+                  → exceptional / concrete reason or project calibration
```

Do not stack synonyms or contradictory directions.

Detailed expression rules: `references/elevenlabs/v3-expression-direction.md`.

## 4. Thought groups / prosody

One thought group should have one dominant communication/performance job.

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

A written sentence may become multiple spoken beats; several short written sentences may become one thought. Grammar does not own performance segmentation.

Use text controls in this order:

```text
spoken wording
→ thought groups
→ punctuation / line structure
→ selective CAPS
→ Audio Tags for explicit acting direction
```

Punctuation and tags are complementary: punctuation shapes linguistic rhythm; tags direct acting state.

Do not use SSML `<break>` with v3.

## 5. Duration planning

When timing matters, resolve it before final wording.

```text
target range
hard maximum
fixed-sync
```

Honor any authoritative Flow 5 Timing Constraint first. Then plan `Estimated Duration` using `references/elevenlabs/v3-duration-planning.md`.

Do not rescue oversized text with `[rushed]`, heavy punctuation, or aggressive Speed. Compress wording without deleting required meaning or expression.

## 6. Voice fit / Target Voice Profile

Judge the performance envelope actually needed:

```text
identity / timbre / persona
baseline tone / energy
natural cadence / pacing
required emotional range
required projection range
language / accent compatibility
pronunciation / drift risk
```

Internal result: `GOOD FIT | LIMITED FIT | RISKY FIT | UNKNOWN`.

Do not compensate for a risky voice with increasingly complex tag stacks. Expression-heavy work needs a voice capable of the requested range.

If no suitable voice exists and Voice Design is in scope, follow `v3-production-reference.md`.

## 7. Continuity planning

### Independent line

Generate standalone when genuinely standalone.

### Connected same-speaker narration

When canonical VO IDs remain separate but the narration is continuous:

```text
previous_text / next_text
or neighboring request IDs
→ contextual prosody continuity
```

Treat each new TTS request as a possible acting-state reset.

If the next clip must begin in a particular material state, **re-anchor that state explicitly** in that clip's canonical prompt even when previous/next context is supplied.

Context supports continuity; it does not replace necessary acting direction.

### Cross-speaker interaction

Use Text to Dialogue when later turns materially react to earlier speakers in the same approved Moment. Each turn keeps its own exact canonical payload and may contain its own tags.

### Long-form

Split at semantic/emotional boundaries, not equal character counts. Use current ElevenCreative Studio when paragraph-level editing/continuity is the real need.

## 8. Pronunciation

Use the smallest reliable control:

```text
ordinary word → normal text
ambiguous number/acronym/symbol → explicit spoken form
unusual proper noun → native v3 IPA when needed
repeated project term → pronunciation note/dictionary when appropriate
heard + approved → project calibration
```

Preparation may identify risk; it may not claim proof.

# Conservation gates

## Communication Conservation

Pass only when:

- every material `Must communicate` fact remains audible;
- every `Must not add/repeat` rule remains respected;
- names, mechanics, result/state, sequence, terminology, and authoritative timing truth remain intact;
- naturalness/performance polish introduces no new project fact;
- timing compression deletes no required information.

## Expression Conservation

Pass only when:

- every material acting state has sufficient direction;
- natural-language rewrite has not flattened required emotion/subtext/projection/pacing;
- material transitions are represented by text/context and explicit tags when needed;
- reactions occur at the correct beat;
- tags do not contradict approved meaning or speaker identity;
- redundant tag stacks do not fight the voice/text;
- generation boundaries do not silently reset an expression that must continue;
- the final emotional/communication landing remains clear.

Expression Conservation is part of Voice Script Readiness; do not create another persisted acceptance field solely for it.

# Per-line script-ready gate

A line is script-ready when:

- Voice Intent Completeness is sufficient;
- Owner/Type/Speaker scope remains exact;
- wording is natural for speaker/register;
- thought-group rhythm/landing are deliberate;
- Expression Coverage is complete;
- material opening/transition/reaction directions are explicit where needed;
- tags are precise rather than decorative;
- Estimated Duration is plausible and source timing constraints are honored;
- voice fit is acceptable or risk/target profile is explicit;
- no SSML `<break>` or canonical environmental SFX instruction is present;
- pronunciation risk is identified;
- continuity/re-anchoring is planned when needed;
- Communication Conservation = PASS;
- Expression Conservation = PASS;
- exact canonical wording revision is known.

Generation readiness additionally requires the intended actual voice and current settings.

# Integrated Voice Script Readiness

Review once at project/scope level; do not create separate scorecards.

| Lens | Ready when... |
|---|---|
| Communication | Required meaning survives and unsupported meaning was not added. |
| Listener | Information/action fits the player's state. |
| Naturalness | Speech is speakable and register-correct, not document-like or artificially casual. |
| Expression | Material emotion, subtext, projection, pacing, reactions, and transitions have sufficient direction. |
| Character | Recurring speakers remain recognizable without template repetition. |
| Performance | Thought groups, punctuation, tags, and transitions serve the scene. |
| Timing | Density and duration are plausible without sacrificing meaning/expression. |
| Continuity | Narrative/dialogue and acting arcs survive clip/turn boundaries. |
| Operator | Exact prompt, voice, duration, surface, and special context are usable without guessing. |

Conceptual result: **Voice Script Readiness: PASS | FAIL**.

# First wrong owner

```text
wrong gameplay/story fact
→ PRD / project authority

wrong Voice moment / Speaker / Channel / Trigger / Purpose / payload / source timing
→ Flow 5

correct requirement but stiff wording / weak expression / wrong tags / Estimated Duration
→ Flow 6 SoundMaker

correct script but wrong 04 presentation
→ renderer / shared production-assets owner

correct script but generated-audio-only issue
→ Generation Mode evidence/settings/voice/surface/context
```

# Bounded revision

```text
specific line defect
→ affected Voice ID
→ Communication Conservation
→ Expression Conservation
→ adjacent continuity only when materially affected
→ update canonical + derived output
→ stop
```

Do not replay unaffected Voice IDs for ceremony.

# Generation surface selection

### Text to Speech

Independent Voice ID.

### Contextual TTS

Connected same-speaker narration split across requests. Supply relevant adjacent context and re-anchor a material acting state at a new clip opening when necessary.

### Text to Dialogue

Use when:

- two or more speakers;
- same approved Moment;
- turn order matters;
- later delivery materially responds to earlier turns.

Tags remain inside the turn they affect.

### ElevenCreative Studio

Use for long-form/editorial/timeline production when section regeneration, locking/history, captions, or timeline assembly materially helps.

# Generation handoff

Before generation, know:

```text
Model: Eleven v3
Surface: TTS | Text to Dialogue | ElevenCreative Studio
Speaker(s): exact project speaker(s)
Voice(s): actual ElevenLabs voice(s)
Voice fit: reviewed
Stability/settings: Natural | project-calibrated
Prompt(s): exact canonical payload(s)
Expression Coverage: reviewed
Timing: none | target | hard max | fixed-sync
Continuity context: none | previous/next text | neighboring request IDs
Pronunciation: normal | special setup
Enhance: OFF unless rewritten output is re-reviewed
```

# After generation

When actual audio is requested, evaluate:

- meaning/intelligibility;
- voice identity;
- naturalness;
- expression accuracy;
- state transitions and reactions;
- pacing/breath;
- landing/emphasis;
- pronunciation;
- duration;
- continuity across clips/turns.

| Heard problem | First action |
|---|---|
| isolated glitch | compare eligible same-prompt regeneration/candidate |
| flat / missing emotion | check Expression Coverage and tag placement first |
| state change missing | add/reposition transition direction before rewriting whole line |
| overacted / synthetic | remove redundant/synonymous direction; inspect punctuation/CAPS and Stability |
| cue repeatedly ignored | inspect voice fit before stacking more tags |
| short connected clip detached | add relevant context and confirm opening state re-anchor |
| dialogue interaction disconnected | use/review Text to Dialogue |
| wrong pronunciation | pronunciation control, not emotional rewrite |
| too long | reduce spoken load first |

Diagnosis order:

```text
meaning
→ naturalness
→ expression intent
→ expression coverage / tag placement
→ thought-group rhythm
→ voice fit
→ Stability
→ continuity / generation surface
→ candidate variance
```

# Approval lock

When the user says **APPROVED** after actual generation:

1. exact generated prompt becomes approved wording for that Voice ID;
2. user-edited generated prompt supersedes the assistant draft;
3. synchronize it into `work/voice-production.md`;
4. rebuild only affected derived scope;
5. record actual duration/pronunciation/settings only when evidence exists;
6. retain useful expression/voice behavior as project calibration, never as new project facts.

# Stop rule

Preparation stops when:

```text
Communication Conservation = PASS
Expression Conservation = PASS
Voice Script Readiness = PASS
```

Do not keep adding tags, schemas, manifests, scorecards, or speculative hardening after the requested scope is ready.

# References

- natural wording/stiffness → `references/elevenlabs/v3-naturalness.md`
- expression/Audio Tag architecture → `references/elevenlabs/v3-expression-direction.md`
- tag vocabulary/text controls → `references/elevenlabs/v3-performance-writing.md`
- duration → `references/elevenlabs/v3-duration-planning.md`
- Text to Dialogue → `references/elevenlabs/v3-dialogue-generation.md`
- voice/settings/continuity/Studio → `references/elevenlabs/v3-production-reference.md`
- source authority → `references/elevenlabs/source-register.md`
