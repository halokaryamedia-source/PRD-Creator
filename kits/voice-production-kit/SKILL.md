---
name: voice-production-kit
description: Extract traceable voice requirements from accepted PRDs, create high-quality Eleven v3 performance wording through SoundMaker, derive Voice Production DOCX output, and validate current script/DOCX/audio evidence without inventing upstream project facts.
version: 1.5.0
---

# Voice Production Kit

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted PRD → `work/voice-requirements.md`.
2. **Flow 6 — Eleven v3 Performance Script Production**: Voice Requirements → canonical `work/voice-production.md` + derived DOCX.
3. **Flow 7 — Voice Validation & Delivery**: current revision → `work/voice-acceptance.md` + delivery state.

## Routing

- Flow 5 → `VOICE-EXTRACTION.md`.
- Flow 6 lifecycle/artifact → `SCRIPT-PRODUCTION.md`.
- Actual Eleven v3 line/generation/revision → `SOUNDMAKER.md`.
- DOCX mechanics → `DOCX-FORMAT.md`.
- Flow 7 → `VOICE-VALIDATION.md`.
- Deep Eleven v3 question → only the matching file under `references/elevenlabs/`.

Do not load all reference material by default.

## Canonical owners

- `work/voice-requirements.md` — which Voice moments exist and what they must communicate;
- `work/voice-production.md` — final spoken/performance wording, including exact approved generated wording;
- `output/Voice Production.docx` — derived presentation;
- `work/voice-acceptance.md` — revision-specific evidence;
- `state/voice-state.yaml` — lifecycle state.

## SoundMaker boundary

`SOUNDMAKER.md` is the **single operational Eleven v3 execution procedure inside Flow 6**. It is not a fourth Flow and not a second wording authority.

Default when no stronger approved project calibration exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance on directed SoundMaker prompt: OFF
```

Long-form instability may route to Studio while keeping Eleven v3.

## Non-negotiable rules

- SoundMaker scope is **Eleven v3 only**.
- Voice scope cannot change silently after Flow 5.
- Performance technique cannot create new project facts/speakers/channels/triggers/mechanics/rewards/outcomes.
- Duration is planned before final wording when timing matters.
- Voice fit is evaluated before adding more direction.
- Spoken wording/beat architecture precede punctuation/CAPS/Audio Tags.
- A flat script is not repaired by tag stacking.
- Any Enhance/UI rewrite of a directed prompt is a new draft requiring review.
- Exact approved generated wording synchronizes into `work/voice-production.md`.
- Generated-audio quality requires actual heard evidence.
- DOCX is always derived from canonical Markdown.
- Critical/Major findings block `voice_delivery_ready`.
- Aftershock remains a presentation benchmark only, never project content authority.
