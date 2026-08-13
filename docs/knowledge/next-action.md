# Next Action

Updated: 2026-08-13

## Current Status

`SOUNDMAKER_V3_INTENT_CONSERVATION_READY`

Working branch: **`Local` only**.

## Current state

Project Document Generator remains **v1.13.0**. The approved Clockwork production package remains at `workspace/active/the-clockwork-vault/`; its accepted PRD meaning/rendered HTML were not changed.

Voice Production Kit is now **v1.8.0**.

SoundMaker remains **Eleven v3 only**. Preparation Mode requires no audio generation/testing; Generation Mode remains optional and one active Voice ID at a time.

The v1.8.0 quality model adopts only the useful reasoning patterns from PRD Creator without copying its artifact/state machinery.

```text
Voice Requirements
→ Voice Intent Completeness
→ internal Performance Fill Map
→ SoundMaker writing
→ Communication Conservation
→ per-line script-ready
→ integrated Voice Script Readiness
→ canonical script / derived DOCX
```

### Voice Intent Completeness

Before writing, SoundMaker resolves as applicable:

```text
communication job
listener state
information payload
listener outcome
speaker identity
timing envelope
performance shape
landing
```

This is internal reasoning only. No new Voice schema/artifact was added.

### Communication Conservation

Every independently actionable Flow 5 `Must communicate` fact that belongs in the moment must survive performance polish and duration compression clearly. `Must not add/repeat` remains binding.

Concision can improve wording; it cannot thin material communication.

### Integrated Voice Script Readiness

Current prepared scope is reviewed once through:

```text
Communication
Listener
Character
Performance
Timing
Continuity
Operator
```

One semantic readiness decision is recorded; no per-lens scorecards/gates were added.

Communication Conservation remains explicit because a polished script can still omit required meaning.

### Decision boundary

Normal production interpretation—sentence split, beats, punctuation, CAPS, tags, pacing—may be decided inside SoundMaker when approved project meaning remains unchanged.

Material new personality/accent identity, Voice scope, Speaker/Channel/Trigger, mechanic, reward, lore, outcome, or required communication returns upstream when unresolved.

### Review economy

Flow 7 now uses:

```text
Mechanical
+ Communication Conservation
+ one integrated Voice Script Readiness review
+ DOCX Visual when claimed
+ optional Audio Evidence
```

Existing `voice-state.yaml` fields remain compatibility summaries; no new lifecycle schema was created.

### First wrong owner / bounded revision

Fix the earliest owner actually wrong and replay only invalidated Voice/speaker scope plus continuity materially affected by the change.

Do not repair upstream defects with more complicated prompts and do not replay unaffected Voice work for ceremony.

### Existing output contract retained

Canonical `work/voice-production.md` remains minimal:

```text
Voice ID — Title
Type
Speaker
Estimated Duration
exact Eleven v3 performance block
```

Operator handoff remains derived/compact and DOCX remains derived presentation.

No builder/validator mechanics, dependency versions, canonical Flow 6 entry schema, PRD behavior, or audio generation were changed by v1.8.0.

## Next Step

**Continue only with another concrete non-audio workflow/content defect or apply Preparation Mode to a real project package when requested. Stop generic hardening when no concrete defect remains; do not require audio testing until the user explicitly enters Generation Mode.**
