# Eleven v3 Performance Script Production

Status: active Flow 6 policy

## Purpose

Flow 6 turns mechanically ready Flow 5 requirements into canonical Eleven v3 wording without changing upstream project/Voice meaning.

## Ownership

```text
accepted project meaning
→ work/voice-requirements.md
   → owns Voice scope, Owner ID, Moment, communication intent, source timing truth
→ Flow 6 performance writing
→ work/voice-production.md
   → owns exact wording, Estimated Duration, selected voice/profile when known
→ consolidated project HTML
```

Flow 6 **preserves** Flow 5 Owner ID. It does not choose a new placement owner.

## Entry gate

Enter Flow 6 only after `state/voice-state.yaml.status: voice_requirements_ready` and:

```bash
python kits/prd-creator/validator/validate_voice.py \
  workspace/active/<project>/
```

passes the Flow 5 requirement/revision/topology contract.

## Flow 5 → Flow 6 interface

Flow 6 consumes:

```text
Placement           ← Owner ID + Moment
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

Flow 6 may decide final wording, beat shape, punctuation/CAPS/tags, Estimated Duration, Target Voice Profile or actual actor selection, Stability, Surface, and other production interpretation inside that boundary.

## Preparation Mode

Default when actual audio generation is not requested:

```text
voice_requirements_ready
→ Voice Intent Completeness
→ performance writing
→ Communication Conservation
→ integrated Voice Script Readiness
→ canonical voice-production.md
→ voice_script_ready
→ rerender consolidated project HTML when current delivery is in scope
```

No per-line audio approval is required in Preparation Mode.

## Voice Cast

Store shared speaker selection/profile once:

```text
Voice Cast:
- <Speaker>: <selected ElevenLabs voice or explicit target profile>
```

Preparation Mode may use a clear target profile before final commercial voice selection. Do not invent a commercial voice merely to fill the field.

`voice_delivery_ready` requires a non-empty cast selection/profile for every speaker represented in canonical production. Actual Generation Mode requires the intended generation voice, not merely an abstract profile.

## Canonical source binding

`work/voice-production.md` binds exact current Flow 5 bytes:

```text
Source Voice Requirements: <accepted PRD revision> / work/voice-requirements.md | sha256:<current SHA-256>
```

Same-version edits to requirements invalidate the older production binding.

## Canonical production format

```text
# Voice Production

Source Voice Requirements: <revision> / work/voice-requirements.md | sha256:<sha>

Voice Cast:
- <Speaker>: <selection/profile>

## <Gameplay Section>
Owner ID: <exact Flow 5 Owner ID>

### VO-... — <Line Title>
Type: <exact Flow 5 Type>
Speaker: <exact Flow 5 Speaker>
Estimated Duration: <production estimate>

```performance
[initial direction]
<exact Eleven v3 payload>
```
```

Per-line canonical metadata is intentionally small. Do not duplicate Channel, Trigger, Purpose, Moment, Timing Constraint, requirement bullets, source refs, reasoning, WPM calculations, or QA notes; those remain with their owners.

## Consolidated 04 presentation

The renderer combines Flow 5 requirement metadata and Flow 6 canonical production:

```text
Owner ID  → Production Assets page
Moment    → natural page grouping
Function  → visible resource function
Voice Cast→ visible selection/profile
Duration  → visible Estimated Duration
Prompt    → exact performance payload
```

The HTML embeds SHA-256 bindings for current `voice-requirements.md` and `voice-production.md`; a stale HTML projection is not current Voice delivery.

No separate Voice HTML is created by default.

## Scope guard

Flow 6 may not silently change:

- Owner ID or Moment;
- Voice scope;
- Speaker / Channel / Trigger / Purpose;
- required communication / exclusions;
- gameplay, lore, reward, result, or authoritative timing truth.

If those are wrong, return to Flow 5 or project authority. Wording/performance/Estimated Duration/selection remain Flow 6.

## Flow 6 gate

Set `voice_script_ready` only when:

- current requirements still mechanically pass for the accepted PRD revision;
- every required Voice ID has one canonical production entry;
- Owner ID, Type, and Speaker parity are exact;
- every performance block begins with at least one deliberate initial direction tag;
- every Estimated Duration is present;
- authoritative timing constraints remain respected;
- Communication Conservation passes;
- integrated Voice Script Readiness passes;
- exact Source Voice Requirements SHA binding is current;
- no unresolved placeholder/upstream contradiction remains.

After setting `voice_script_ready`, run the same lifecycle-aware validator again. At this status it additionally checks production binding and parity.

## Generation Mode

Actual ElevenLabs generation is only entered when requested:

```text
one active Voice ID
→ actual actor voice selected
→ exact reviewed prompt
→ generate / hear / revise or approve
→ canonical sync when wording/selection changes
→ rerender current project HTML
```

Generated-audio quality requires actual audio evidence and remains separate from script readiness.

## Stop rule

Stop when the requested preparation/generation scope is current. Do not create parallel Voice HTML, settings databases, manifests, scorecards, or approval layers without a concrete need.
