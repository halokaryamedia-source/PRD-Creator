---
name: voice-production-kit
description: Extract traceable voice requirements from accepted PRDs, create high-quality Eleven v3 performance prompts and a reference-styled Voice Production DOCX, then validate the current script/DOCX/audio evidence without inventing upstream project facts.
version: 1.4.0
---

# Voice Production Kit

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted PRD → `work/voice-requirements.md`.
2. **Flow 6 — Eleven v3 Performance Script Production**: voice requirements → SoundMaker quality pass → `work/voice-production.md` + `output/Voice Production.docx`.
3. **Flow 7 — Voice Validation & Delivery**: current script/DOCX → `work/voice-acceptance.md` + `voice_delivery_ready`.

## Routing

- Flow 5: read `VOICE-EXTRACTION.md`.
- Flow 6: read `SCRIPT-PRODUCTION.md`; for one actual Eleven v3 prompt/revision use `SOUNDMAKER.md`; read `DOCX-FORMAT.md` only when DOCX presentation/build mechanics are in scope.
- Flow 7: read `VOICE-VALIDATION.md`.

Do not skip the current project's state gate. Do not load every ElevenLabs reference by default.

## Canonical owners

- `work/voice-requirements.md` — which voice moments exist and what they must communicate;
- `work/voice-production.md` — final spoken wording/performance notation, including the exact approved SoundMaker prompt when actual generation occurs;
- `output/Voice Production.docx` — derived production presentation;
- `work/voice-acceptance.md` — revision-specific Flow 7 evidence/findings;
- `state/voice-state.yaml` — lifecycle status/revision/next step across Flow 5–7.

## SoundMaker boundary

`SOUNDMAKER.md` is the Eleven v3 **execution/quality profile inside Flow 6**. It is not a fourth production Flow and not a second wording authority.

```text
Voice Requirement
→ SoundMaker v3 quality engine
→ canonical work/voice-production.md
→ DOCX / optional actual generation
```

When a user actually generates or edits a prompt in ElevenLabs and approves that result, the exact prompt actually used must be synchronized back into `work/voice-production.md` before the project can claim current script/DOCX/audio alignment.

## Production references

- `references/aftershock/README.md` — demonstrated DOCX/performance presentation benchmark only;
- `references/elevenlabs/README.md` — evidence-backed **Eleven v3-only** production technique;
- `references/elevenlabs/v3-performance-writing.md` — spoken writing, beats, punctuation/CAPS/tags;
- `references/elevenlabs/v3-duration-planning.md` — target/max/fixed timing planning;
- `references/elevenlabs/v3-production-reference.md` — voice fit, Stability, pronunciation, generation behavior.

Production references never outrank current project Voice Requirements or canonical project meaning.

## Non-negotiable rules

- SoundMaker model scope is **Eleven v3 only**.
- Voice scope cannot change silently after Flow 5.
- Script polish cannot create a new project fact, speaker, channel, trigger, mechanic, reward, or outcome.
- Performance quality is built in this order: meaning → spoken wording → beat structure → punctuation/line structure → selective CAPS → minimal Audio Tags.
- Target duration is planned before final wording when timing matters.
- A flat script is not repaired by tag stacking.
- DOCX is generated from canonical Markdown and is never the editable authority.
- Critical/Major findings block `voice_delivery_ready`.
- Pronunciation is not called verified without evidence.
- Estimated duration is not measured audio duration.
- Generated-audio quality is never claimed unless actual audio was supplied and reviewed.
- `voice_delivery_ready` normally refers to script + DOCX delivery scope; audio is a separate evidence dimension unless explicitly included.
- Aftershock remains a demonstrated quality/layout reference only, never project content or quota.
- ElevenLabs prompting guidance shapes delivery only; it never invents upstream Voice scope or project meaning.
