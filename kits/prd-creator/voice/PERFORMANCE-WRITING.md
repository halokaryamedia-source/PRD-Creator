# SoundMaker — Eleven v3 Execution Mode

Status: active Flow 6 execution procedure  
Model scope: **Eleven v3 only**

## Purpose

SoundMaker turns approved Voice Requirements into production-ready Eleven v3 speech while preserving **communication, naturalness, actor identity, expression, pronunciation, and continuity**.

```text
Voice Requirement
→ recover communication + performance intent
→ Actor Baseline / Voice Fit
→ natural spoken-language rewrite
→ Expression Coverage
→ pronunciation/language pass
→ continuity planning
→ conservation gates
→ Voice Script Readiness
→ canonical work/voice-production.md
→ optional Generation Mode later
```

`work/voice-production.md` remains the sole canonical Voice wording/performance owner.

# Operating modes

## Preparation Mode

Use for writing/review without generating audio.

Preparation may establish:

- natural spoken wording;
- Target Voice Profile / selected-voice fit;
- Actor Baseline and no-drift boundary;
- exact Audio Tags and expression transitions;
- pronunciation/language strategy;
- generation surface/context plan;
- Estimated Duration.

It does **not** claim heard pronunciation, measured duration, or audio quality.

## Generation Mode

Use only when actual generation/review is requested.

```text
independent Voice ID
→ Eleven v3 TTS

connected same-speaker narration
→ TTS + relevant previous/next context

same Moment + multiple speakers + response dependency
→ Text to Dialogue

long-form editorial/timeline work
→ current ElevenCreative Studio when useful
```

Generation grouping/context is ephemeral. Existing `VO-...` identities remain canonical.

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

Keep Actor Baseline maps, expression maps, pronunciation reasoning, candidate history, and generation-group metadata out of the canonical format unless an existing owner genuinely needs them.

# Authority boundary

Recover current facts in this order:

1. matching `work/voice-requirements.md`;
2. accepted PRD/project meaning only for missing delivery-relevant context;
3. current `work/voice-production.md` when revising;
4. approved same-project voice/performance/pronunciation evidence;
5. current ElevenLabs references for production technique.

SoundMaker may decide reversible craft: spoken phrasing, thought groups, expression tags, Estimated Duration, actor-fit assessment, pronunciation representation, generation surface/context, and settings.

Return upstream for changes to established character identity, material accent/relationship/lore, Voice scope, Speaker, Channel, Trigger, Purpose, mechanic, result, reward, or authoritative timing truth.

# Eleven v3 baseline

```text
Model: Eleven v3
Stability: Natural
Speed: 1.0 / unchanged when exposed
Enhance: OFF on SoundMaker-reviewed prompts
Surface: TTS for independent speech
Audio Tags: deliberate acting controls
```

Use Creative only when greater expressive variance is intentionally useful after actor fit and prompt architecture are sound. Use Robust when consistency outweighs directional responsiveness.

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

Recover only missing delivery context. Do not invent hard timing constraints or reopen the full PRD for richer prose.

## 2. Actor Baseline / Voice Casting

Before per-line acting direction, establish the recurring Speaker as an actor.

Internal Actor Continuity Map:

```text
Identity / Timbre
Native Cadence
Baseline Energy
Baseline Projection
Emotional Range
Projection Range
Language / Accent
Persona / Social Stance
No-Drift Boundary
Pronunciation Risk
```

Then treat each Moment as a **delta from that baseline**.

```text
Actor Baseline
→ MOM-01 delta
→ MOM-02 delta
→ MOM-03 delta
```

A local `[urgent]`, `[relieved]`, or `[uneasy]` direction must not mutate the Speaker into a different personality.

Voice-fit result may be:

```text
GOOD FIT | LIMITED FIT | RISKY FIT | UNKNOWN
```

Do not rescue a risky actor with increasingly complex tag stacks. For a recurring Speaker, choose the voice that covers the broadest required project envelope, not merely one impressive line.

Detailed owner: `references/elevenlabs/v3-voice-casting-continuity.md`.

## 3. Natural spoken-language pass

Make the line speakable before directing it.

```text
requirement meaning
→ plausible speech at this moment
→ remove document/specification scaffolding
→ natural thought groups
→ preserve every required fact
```

Prefer direct spoken verbs, listener-first order, context-aware references, appropriate contractions, sentence-length variation, and a clean landing.

Avoid accidental PRD syntax, repeated obvious context, uniform rhythm, fake-human filler, and overloaded instruction sentences.

Naturalness is register-correct, not universally casual.

Detailed owner: `references/elevenlabs/v3-naturalness.md`.

## 4. Expression Coverage

Preserve acting deliberately after the wording is natural.

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

Core rule:

```text
material expression sufficiently explicit in actor + text + punctuation + context
→ no redundant tag required

material expression ambiguous / under-directed
→ precise Audio Tag near affected beat
```

Material opening states should be anchored at the opening. Material state changes should be directed at the transition. Reactions belong at their event point.

Tag count is not the target. **Complete expression coverage without redundant direction** is the target.

```text
1 tag               → preferred when sufficient
2 simultaneous tags → valid for different compatible dimensions
3+                  → exceptional / concrete reason or project calibration
```

Detailed owner: `references/elevenlabs/v3-expression-direction.md`.

## 5. Thought groups / prosody

One thought group should have one dominant communication/performance job.

```text
spoken wording
→ thought groups
→ punctuation / line structure
→ selective CAPS
→ Audio Tags for explicit acting
```

Punctuation shapes linguistic rhythm; Audio Tags direct acting state. Do not use SSML `<break>` with v3.

## 6. Duration planning

Honor an authoritative Flow 5 Timing Constraint first, then plan `Estimated Duration`.

```text
target range | hard maximum | fixed-sync
```

Do not rescue oversized scripts with `[rushed]`, punctuation spam, or aggressive Speed. Compress wording without deleting required communication/expression.

Detailed owner: `references/elevenlabs/v3-duration-planning.md`.

## 7. Language & Pronunciation Pass

Before generation, detect only materially risky spoken forms:

```text
proper names
project/game terminology
acronyms
numbers / dates / coordinates / symbols
foreign/code-switched terms
repeated technical vocabulary
```

Use the smallest reliable control:

```text
ordinary word
→ normal text

ambiguous number/date/symbol/acronym
→ explicit spoken form / alias

unusual proper noun
→ IPA/phoneme control when needed

repeated critical term
→ pronunciation dictionary

heard + approved
→ project calibration
```

Prefer a voice trained in the target language/accent. Website TTS auto-detects language from prompt context; mixed-language prompts can be ambiguous. API `language_code` may be used when short/ambiguous input or normalization needs a dominant language.

Pronunciation risk may be identified in Preparation Mode; approval requires heard evidence.

Detailed owner: `references/elevenlabs/v3-pronunciation-language.md`.

## 8. Continuity planning

### Independent line

Generate standalone when genuinely standalone.

### Connected same-speaker narration

Use relevant:

```text
previous_text / next_text
or neighboring request IDs
```

for contextual prosody continuity.

Treat each new TTS request as a possible acting reset. If a material state must continue at the next clip opening, re-anchor that state explicitly.

### Cross-speaker interaction

Use Text to Dialogue when later turns materially react to earlier speakers in the same approved Moment. Each turn keeps its own exact canonical payload and actor-relative expression direction.

### Long-form

Split at semantic/emotional boundaries, not equal character counts. Use current Studio when paragraph-level editing/continuity is the real need.

# Conservation gates

## Communication Conservation

Pass only when required facts remain audible, exclusions remain respected, terminology/result/timing truth remain intact, and polish introduces no unsupported project fact.

## Expression Conservation

Pass only when material emotion/subtext/projection/pacing/reaction/transitions remain directed, tags do not contradict the actor/project, generation boundaries do not silently reset required acting, and the landing remains clear.

## Character Continuity Conservation

For recurring Speakers, pass only when:

- actor identity/timbre/persona remain recognizable;
- local emotion remains plausible relative to baseline;
- no line exceeds the actor envelope merely because a tag requests it;
- no-drift boundaries remain intact;
- language/accent behavior stays compatible;
- variation does not collapse into a repetitive template.

## Pronunciation Conservation

Pass only when critical terms have an intentional spoken strategy, language/accent choice is compatible, numbers/acronyms are not materially ambiguous, and unverified pronunciation is not claimed as approved.

These are semantic/craft gates inside Voice Script Readiness, not persisted schema fields.

# Per-line script-ready gate

A line is ready when:

- Voice Intent Completeness is sufficient;
- Owner/Type/Speaker remain exact;
- actor baseline/fit is clear enough for preparation;
- wording is natural for register;
- thought-group rhythm/landing are deliberate;
- Expression Coverage is complete;
- critical pronunciation/language risks have a strategy;
- Estimated Duration is plausible and source timing truth is respected;
- continuity/re-anchoring is planned when needed;
- Communication Conservation = PASS;
- Expression Conservation = PASS;
- Character Continuity Conservation = PASS when recurring Speaker context exists;
- Pronunciation Conservation = PASS;
- exact canonical wording revision is known.

Generation readiness additionally requires the intended actual voice and current settings.

# Integrated Voice Script Readiness

Review the current scope once; do not create scorecards.

| Lens | Ready when... |
|---|---|
| Communication | Required meaning survives; unsupported meaning was not added. |
| Naturalness | Speech is speakable and register-correct. |
| Actor | Voice fit covers required range and recurring identity remains stable. |
| Expression | Material acting states/transitions have sufficient direction. |
| Pronunciation | Critical spoken forms have an intentional production strategy. |
| Timing | Density/duration are plausible without sacrificing meaning/expression. |
| Continuity | Narrative, dialogue, and acting arcs survive boundaries. |
| Operator | Exact prompt, voice, surface, settings, and special context are usable without guessing. |

Conceptual result: **Voice Script Readiness: PASS | FAIL**.

# Generation handoff

Before actual generation, know:

```text
Model: Eleven v3
Surface: TTS | Text to Dialogue | Studio
Speaker(s): exact project Speaker(s)
Voice(s): actual ElevenLabs voice_id(s)
Voice source/type: when useful for reproducibility
Actor fit: reviewed
Stability/settings
Prompt(s): exact canonical payload(s)
Expression Coverage
Timing mode
Continuity context
Language / pronunciation setup
Enhance: OFF unless rewritten output is re-reviewed
```

Do not rely on a voice display name alone as durable production identity. Current ElevenLabs Default voices are scheduled to expire on **2026-12-31**; projects using one should be re-cast intentionally before expiry rather than treating a suggested replacement as identical.

# Candidate iteration after generation

ElevenLabs output is nondeterministic. One weak take does not prove a prompt defect.

```text
reviewed prompt + same voice/settings/context
→ same-content candidate/regeneration first
→ repeated defect?
   no  → choose best acceptable take
   yes → diagnose first wrong owner
```

Freeze the comparison unit during initial candidate review:

```text
text + tags
voice_id
model
settings
language/pronunciation setup
surface
continuity context
```

After a repeated defect is established, change **one variable class at a time**:

```text
wording
OR expression direction
OR voice
OR settings
OR pronunciation/language
OR surface/context
```

Do not require a ritual number of takes. Current dashboard rules may allow up to two free same-parameter regenerations; API billing differs. `seed` is best-effort consistency, not guaranteed determinism.

Detailed owner: `references/elevenlabs/v3-candidate-iteration.md`.

# Heard-problem routing

| Heard problem | First action |
|---|---|
| isolated glitch | same-content candidate/regeneration |
| flat / missing emotion | Expression Coverage / tag placement |
| state change missing | transition direction |
| overacted / synthetic | redundant tags/punctuation + actor fit + Stability |
| cue repeatedly ignored | actor fit before more tags |
| character sounds like a different person | Actor Baseline / no-drift boundary |
| accent consistently wrong | voice-language fit |
| critical name/acronym wrong | pronunciation control |
| short connected clip detached | continuity context + opening re-anchor |
| dialogue interaction disconnected | Text to Dialogue / dialogue candidate review |
| too long | spoken load first |

# Approval lock

After actual audio approval:

1. approved exact prompt remains canonical for that Voice ID;
2. synchronize user-edited prompt if applicable;
3. rebuild only affected derived scope;
4. retain actual `voice_id`, settings, pronunciation, timing, seed/context, and selected-take evidence only when useful;
5. retain proven actor/expression/pronunciation behavior as project calibration, never as new project facts.

# Stop rule

Preparation stops when:

```text
Communication Conservation = PASS
Expression Conservation = PASS
Character Continuity Conservation = PASS when applicable
Pronunciation Conservation = PASS
Voice Script Readiness = PASS
```

Do not add schemas, manifests, scorecards, approval layers, or more theory after the requested scope is ready.

# References

- naturalness → `references/elevenlabs/v3-naturalness.md`
- expression → `references/elevenlabs/v3-expression-direction.md`
- actor casting/continuity → `references/elevenlabs/v3-voice-casting-continuity.md`
- pronunciation/language → `references/elevenlabs/v3-pronunciation-language.md`
- candidate iteration → `references/elevenlabs/v3-candidate-iteration.md`
- tag/text controls → `references/elevenlabs/v3-performance-writing.md`
- duration → `references/elevenlabs/v3-duration-planning.md`
- Dialogue → `references/elevenlabs/v3-dialogue-generation.md`
- settings/Studio/API → `references/elevenlabs/v3-production-reference.md`
- source authority → `references/elevenlabs/source-register.md`
