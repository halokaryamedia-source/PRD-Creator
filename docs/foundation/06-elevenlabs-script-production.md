# Eleven v3 Performance Script Production

Status: active Flow 6 policy

## Purpose

Flow 6 turns mechanically ready Flow 5 requirements into canonical Eleven v3 wording without changing upstream project/Voice meaning.

Detailed performance craft lives in `kits/prd-creator/voice/PERFORMANCE-WRITING.md`; this page owns lifecycle and authority boundaries.

## Ownership

```text
accepted project meaning
→ work/voice-requirements.md
   → Voice scope + Owner ID + Moment ID/Moment + communication intent + source timing truth
→ Flow 6 performance writing
→ work/voice-production.md
   → exact wording + Estimated Duration + selected voice/profile when known
→ consolidated project HTML
```

Flow 6 preserves Flow 5 Owner ID, Moment ID, Type, Speaker, and scope. It does not choose new placement identity.

## Entry gate

Enter only after `voice-state.yaml.status: voice_requirements_ready` and `validator/validate_voice.py` passes the Flow 5 requirement/revision/topology contract.

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

Flow 6 may decide wording, beat shape, punctuation/CAPS/tags, Estimated Duration, Target Voice Profile or actor selection, Stability, generation surface, and other production interpretation inside that boundary.

## Preparation Mode

```text
voice_requirements_ready
→ Voice Intent Completeness
→ performance writing
→ Communication Conservation
→ integrated Voice Script Readiness
→ canonical voice-production.md
→ voice_script_ready
→ rerender consolidated project HTML when in scope
```

No per-line audio approval is required in Preparation Mode.

## Voice Cast

Store shared speaker selection/profile once:

```text
Voice Cast:
- <Speaker>: <selected ElevenLabs voice or explicit target profile>
```

Preparation may use a clear target profile before final commercial voice selection. `voice_delivery_ready` requires a non-empty selection/profile for every represented speaker; actual Generation Mode requires the intended generation voice.

## Exact Flow 5 binding

`voice-production.md` binds exact current requirement bytes:

```text
Source Voice Requirements: <accepted PRD revision> / work/voice-requirements.md | sha256:<current SHA-256>
```

Same-version requirement edits invalidate the older production script.

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

Moment ID/Moment remain canonical in Flow 5 and are intentionally not duplicated into every Flow 6 line. The compositor joins each Voice ID back to its requirement before 04 rendering.

## Consolidated 04 presentation

```text
Owner ID       → Production Assets page
Moment ID      → stable moment grouping
Moment         → reader-facing moment title
Function       → visible communication function
Voice Cast     → visible selection/profile
Duration       → visible Estimated Duration
Prompt         → exact performance payload
```

Derived HTML embeds exact SHA bindings for current Voice requirements and production. No separate Voice HTML is created by default.

## Scope guard

Flow 6 may not silently change Owner/Moment identity, Voice scope, Speaker/Channel/Trigger/Purpose, required communication/exclusions, gameplay/lore/reward/result, or authoritative timing truth.

If those are wrong, return to Flow 5/project authority. Wording/performance/Estimated Duration/selection/generation surface remain Flow 6.

## Flow 6 gate

Set `voice_script_ready` only when:

- current Flow 5 requirements still validate against accepted PRD meaning;
- every required Voice ID has one canonical production entry;
- Owner ID, Type, and Speaker parity are exact;
- every performance block starts with a deliberate initial direction tag;
- Estimated Duration is present;
- authoritative timing constraints remain respected;
- Communication Conservation and integrated Voice Script Readiness pass;
- exact Source Voice Requirements SHA binding is current;
- no unresolved placeholder/upstream contradiction remains.

Run the lifecycle-aware Voice validator again after setting `voice_script_ready`; it then checks production binding/parity as well.

## Generation Mode

Actual ElevenLabs generation is entered only when requested. Generation surface is selected from the approved Moment and communication relationship:

```text
independent single-speaker Voice ID
→ Eleven v3 Text to Speech

multiple speakers in the same Moment
+ later turns materially respond to earlier turns
→ Eleven v3 Text to Dialogue using the existing ordered VO IDs

long-form editorial production / continuity work
→ current ElevenCreative Studio when useful
```

Text to Dialogue grouping is **ephemeral production routing**. It does not create a Dialogue ID, duplicate canonical script, or change Flow 5/6 identity. Each constituent `VO-...` prompt remains canonical in `voice-production.md`.

When timing/subtitle synchronization is materially required, the current Text to Dialogue timestamps endpoint may provide generated segment/character timing evidence. Generated timing never replaces authoritative upstream timing truth.

A weak isolated take should normally be compared with available same-prompt variants/regenerations before rewriting correct canonical wording. Repeated failure at the same beat is stronger evidence that prompt, settings, surface, or voice fit needs revision.

Audio quality requires actual audio evidence and remains separate from script readiness.

## Stop rule

Stop when requested preparation/generation scope is current. Do not add parallel Voice HTML, settings databases, manifests, Dialogue schemas, scorecards, or approval layers without a concrete need.
