# Next Action

Updated: 2026-08-13

## Current Status

`VOICE_FLOW5_FLOW6_INTERFACE_READY`

Working branch: **`Local` only**.

## Current state

Project Document Generator remains **v1.13.0**. The approved Clockwork production package remains unchanged.

Voice Production Kit is now **v1.9.0** and remains **Eleven v3 only**.

The Flow 5 → Flow 6 interface is now explicit enough for SoundMaker to complete Voice Intent without reopening the full PRD or inventing product meaning by default.

```text
Flow 5 Voice Requirement
│
├─ Function + Purpose        → Communication Job
├─ Trigger + Channel         → Listener State
├─ Must communicate         → Information Payload
├─ Purpose                  → Listener Outcome
├─ Speaker                  → Speaker Owner
├─ Timing Constraint?       → authoritative hard/fixed timing truth
└─ Must not add/repeat      → Scope Guardrails
        ↓
Voice Intent Completeness
→ Performance Fill Map
→ SoundMaker writing
→ Communication Conservation
→ Voice Script Readiness
```

### Field quality

Flow 5 now requires:

- Trigger to describe the actual gameplay/story event/state and relevant listener condition when material;
- Purpose to express what the listener should know/do/understand/acknowledge, not a vague `provide dialogue` instruction;
- independently actionable `Must communicate` facts to remain distinct enough for downstream conservation;
- `Must not add/repeat` to protect scope and information progression;
- optional `Timing Constraint` only when accepted upstream authority defines a material line/window/fixed-sync rule.

### Timing boundary

`Timing Constraint` is **Flow 5 authoritative truth** and is optional.

`Estimated Duration` remains **Flow 6 production planning**.

```text
Flow 5: Timing Constraint: fixed 12-second cinematic slot
        ↓
Flow 6: word-budget / performance planning
        ↓
Estimated Duration compatible with that source boundary
```

If Flow 5 has no Timing Constraint, SoundMaker may plan a reasonable Estimated Duration but must not invent a hard source limit.

### What remains Flow 6 craft

Flow 5 does not gain fields for:

- final spoken wording;
- Performance Shape;
- Landing wording;
- Audio Tags;
- CAPS/punctuation/pause strategy;
- Target Voice Profile / selected ElevenLabs voice;
- Stability / Surface / Enhance;
- production-estimated duration.

These remain SoundMaker production interpretation unless upstream authority actually constrains them.

### Review boundary

Communication Conservation and integrated Voice Script Readiness now explicitly verify that authoritative Flow 5 timing truth survives downstream planning alongside required communication.

The first-wrong-owner rule is:

```text
project fact → PRD
Voice scope/Speaker/Channel/Trigger/Purpose/required communication/timing truth → Flow 5
wording/performance/Estimated Duration → Flow 6
DOCX-only defect → builder
actual audio-only defect → Generation Mode
```

### Overdevelopment guard

No new artifact family, lifecycle state, Flow 6 canonical entry field, builder/validator timing engine, dependency, score system, or audio-test requirement was added.

The existing Voice contract fixture now includes an optional Flow 5 Timing Constraint to prove current builder/validator compatibility while keeping semantic timing decisions outside mechanical tooling.

## Next Step

**Stop generic SoundMaker hardening unless a concrete non-audio defect is identified; otherwise apply the current Flow 5 → Flow 6 Preparation Mode to a real project package when requested. Audio testing remains unnecessary until the user explicitly enters Generation Mode.**
