# Voice Production Kit v1.1.0

Repository-backed downstream voice production for accepted PRD projects.

## Current flow

```text
Flow 4 handoff_ready PRD
→ Flow 5 Voice Requirement Extraction
→ work/voice-requirements.md
→ state/voice-state.yaml = voice_requirements_ready
→ Flow 6 ElevenLabs Performance Script Production
```

Flow 5 is implemented. Flow 6 remains the next boundary.

## Flow 5 outputs

- `work/voice-requirements.md` — canonical list of justified voice moments;
- `state/voice-state.yaml` — revision/status/next-step owner.

A valid Flow 5 result can also be `no_voice_required`.

## Reference principle

The original Aftershock Voice Production package established useful patterns:

- Main Story for briefing, arrival, transition, story-state change, completion, reward, and farewell;
- Radio Communication for brief warning, progress, urgency, encouragement, reminder, and recovery;
- Main Story and Radio grouped by gameplay section;
- no requirement that every section have the same number of lines.

Those are demonstrated patterns, not fixed project quotas.

## Flow 6 baseline

`INSTRUCTIONS.md` preserves the original v1.0 script-writing rules. Performance wording, ElevenLabs directions, CAPS emphasis, pauses, duration, and DOCX formatting are deliberately deferred until Flow 6.
