---
name: voice-production-kit
description: Extract traceable voice requirements from accepted PRDs, prepare high-quality Eleven v3 performance wording through SoundMaker, derive Voice Production DOCX output, and optionally support one-line-at-a-time generation/revision without inventing upstream project facts.
version: 1.6.0
---

# Voice Production Kit

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted PRD → `work/voice-requirements.md`.
2. **Flow 6 — Eleven v3 Performance Script Production**: Voice Requirements → canonical `work/voice-production.md` + derived DOCX.
3. **Flow 7 — Voice Validation & Delivery**: current revision → `work/voice-acceptance.md` + delivery state.

## Routing

- Flow 5 → `VOICE-EXTRACTION.md`.
- Flow 6 lifecycle/artifact → `SCRIPT-PRODUCTION.md`.
- Eleven v3 wording quality → `SOUNDMAKER.md`.
- DOCX mechanics → `DOCX-FORMAT.md`.
- Flow 7 → `VOICE-VALIDATION.md`.
- Deep Eleven v3 question → only the matching file under `references/elevenlabs/`.

Do not load all reference material by default.

## Canonical owners

- `work/voice-requirements.md` — which Voice moments exist and what they must communicate;
- `work/voice-production.md` — final spoken/performance wording, including exact approved generated wording when generation occurs;
- `output/Voice Production.docx` — derived presentation;
- `work/voice-acceptance.md` — revision-specific evidence;
- `state/voice-state.yaml` — lifecycle state.

## SoundMaker modes

`SOUNDMAKER.md` is the single operational Eleven v3 procedure inside Flow 6.

### Preparation Mode

Use for script/DOCX work when audio generation is not requested.

- full current Voice scope may be prepared in one pass;
- every Voice ID gets per-line SoundMaker quality;
- run project-level speaker continuity and anti-repetition review;
- duration/pronunciation remain planned evidence, not generated proof;
- do not require audio testing or `APPROVED` per line.

### Generation Mode

Use only when actual ElevenLabs generation/revision is requested.

- one active Voice ID;
- one exact reviewed prompt;
- actual feedback/approval loop;
- exact approved generated wording syncs back into `work/voice-production.md`.

## Default v3 baseline

When no stronger approved project calibration exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance on directed SoundMaker prompt: OFF
```

Long-form instability may route to Studio while keeping Eleven v3.

## Non-negotiable rules

- SoundMaker scope is **Eleven v3 only**.
- Recover existing project context before asking the user; ask only unresolved material decisions.
- Voice scope cannot change silently after Flow 5.
- Performance technique cannot create project facts/speakers/channels/triggers/mechanics/rewards/outcomes.
- Duration is planned before final wording when timing matters.
- Voice fit is evaluated before adding more direction.
- Spoken wording/beat architecture precede punctuation/CAPS/Audio Tags.
- A flat script is not repaired by tag stacking.
- Batch preparation includes cross-line continuity/anti-template review.
- Any Enhance/UI rewrite of a directed prompt is a new draft requiring review.
- Exact approved generated wording synchronizes into `work/voice-production.md`.
- Generated-audio quality requires actual heard evidence only when audio is in scope.
- DOCX is always derived from canonical Markdown.
- Critical/Major findings block `voice_delivery_ready`.
- Aftershock remains a presentation benchmark only, never project content authority.
