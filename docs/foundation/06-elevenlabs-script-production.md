# Eleven v3 Performance Script Production

Status: active Flow 6 policy

## Purpose

Flow 6 turns mechanically ready Flow 5 requirements into canonical Eleven v3 speech while preserving upstream meaning and intended acting.

Detailed craft lives in `kits/prd-creator/voice/PERFORMANCE-WRITING.md`; this page owns lifecycle and authority boundaries.

## Ownership

```text
accepted project meaning
→ work/voice-requirements.md
→ Flow 6 spoken/performance writing
→ work/voice-production.md
   → natural spoken wording + expression direction + Estimated Duration + shared Voice Cast
→ consolidated project HTML
```

Flow 6 preserves Flow 5 Owner ID, Moment ID, Type, Speaker, and scope.

## Entry gate

Enter after `voice-state.yaml.status: voice_requirements_ready` and the Flow 5 validator passes.

## Flow 5 → Flow 6 interface

```text
Placement           ← Owner ID + Moment ID + Moment
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

Flow 6 may decide natural spoken wording, thought groups, expression direction/Audio Tags, Estimated Duration, voice/profile selection, settings, continuity context, and generation surface inside that boundary.

## Preparation Mode

```text
voice_requirements_ready
→ Voice Intent Completeness
→ natural spoken-language pass
→ Expression Coverage
→ Communication + Expression Conservation
→ integrated Voice Script Readiness
→ canonical voice-production.md
→ voice_script_ready
```

No audio generation is required.

## Voice Cast

Store shared speaker selection/profile once:

```text
Voice Cast:
- <Speaker>: <selected ElevenLabs voice or explicit target profile>
```

Voice fit is part of quality. A mismatched baseline voice must not be repaired through heavier tag stacks.

## Exact Flow 5 binding

```text
Source Voice Requirements: <accepted PRD revision> / work/voice-requirements.md | sha256:<current SHA-256>
```

Same-version requirement edits invalidate older production wording.

## Canonical production format

```text
### VO-... — <Line Title>
Type: <Flow 5 Type>
Speaker: <Flow 5 Speaker>
Estimated Duration: <production estimate>

```performance
<exact Eleven v3 payload>
```
```

A performance block is non-empty exact generation text. Audio Tags are not mandatory syntax, but material expression must have sufficient direction.

## Naturalness boundary

Flow 6 may reshape approved meaning into natural speech appropriate to the speaker/register. It may use contractions, context-aware compression, thought-group regrouping, cadence variation, and relevant continuity context.

It may not remove required facts, invent lore/personality, or change established speaker identity.

## Expression boundary

Flow 6 must preserve material acting intent.

Internally review:

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

Policy:

```text
baseline informational delivery sufficiently carried by voice + text
→ zero tag may be correct

material performance state not sufficiently explicit
→ precise Audio Tag direction required by craft

material state transition
→ direction close to transition

material reaction
→ reaction tag at event point
```

The goal is **Expression Coverage**, not tag count.

Do not add generic `[calm]`, `[clear]`, `[natural]`, or `[conversational]` merely for formatting. Do not remove tags that carry meaningful acting direction merely to make the prompt look cleaner.

## Generation-boundary expression rule

Connected narration may use `previous_text` / `next_text` or neighboring request IDs for prosody.

Each new TTS request can behave like a performance reset. If a material acting state must continue into the next clip, re-anchor that state explicitly at the new clip opening when necessary. Context helps continuity; it does not replace required acting direction.

## Scope guard

Flow 6 may not silently change Owner/Moment identity, Voice scope, Speaker/Channel/Trigger/Purpose, required communication/exclusions, project facts, or authoritative timing truth.

## Flow 6 gate

Set `voice_script_ready` only when:

- current Flow 5 requirements validate;
- every required Voice ID has one canonical production entry;
- Owner ID, Type, and Speaker parity are exact;
- every performance block is non-empty;
- wording is natural for the speaker/register;
- thought-group rhythm/landing are deliberate;
- **Expression Coverage is complete**;
- material opening states, transitions, pacing/projection changes, and reactions are explicitly directed where needed;
- tags are precise, audible, voice-compatible, and non-redundant;
- Estimated Duration exists and source timing truth remains respected;
- connected narration has appropriate continuity/re-anchoring planning;
- Communication Conservation = PASS;
- Expression Conservation = PASS;
- integrated Voice Script Readiness = PASS;
- exact Source Voice Requirements SHA is current;
- no unresolved upstream contradiction remains.

Mechanical validation does not prove naturalness/expression; those remain semantic/craft judgments.

## Generation Mode

```text
independent Voice ID
→ Eleven v3 TTS

connected same-speaker narration split across requests
→ TTS + relevant context + expression re-anchor when needed

multiple speakers in same Moment + response dependency
→ Text to Dialogue using existing ordered VO IDs

long-form editorial production
→ current ElevenCreative Studio when useful
```

Text to Dialogue grouping and continuity context are ephemeral production routing. They do not create parallel canonical schemas.

For expression-heavy work, keep Stability on Natural or Creative when appropriate; Robust is less responsive to directional prompts and should be chosen only when consistency is the actual priority.

A weak isolated take should be compared with same-prompt candidates/regeneration before rewriting otherwise-correct canonical wording. Repeated expression failure at the same beat is stronger evidence of tag placement, voice fit, Stability, or surface issues.

Audio quality requires actual heard evidence.

## Stop rule

Stop when requested scope is current. Do not add parallel Voice HTML, expression manifests, settings databases, scorecards, or duplicate acceptance layers without a concrete need.
