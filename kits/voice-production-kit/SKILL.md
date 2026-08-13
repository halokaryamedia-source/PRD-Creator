---
name: voice-production-kit
description: Extract Voice requirements from accepted PRDs, prepare canonical Eleven v3 production content, conserve required communication, and publish developer-ready Voice Production into the same project HTML without inventing upstream project facts.
version: 1.11.2
---

# Voice Production Kit

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted PRD → `work/voice-requirements.md`.
2. **Flow 6 — Voice Production**: Voice Requirements → canonical `work/voice-production.md` → same project `output/final.html`.
3. **Flow 7 — Voice Validation & Delivery**: current revision → compact acceptance + delivery state.

DOCX and audio remain optional downstream scopes.

## Routing

- Flow 5 → `VOICE-EXTRACTION.md`.
- Flow 6 lifecycle/output → kit `README.md` + `docs/foundation/06-elevenlabs-script-production.md`.
- Flow 6 writing/performance detail → `SOUNDMAKER.md`.
- Flow 7 → `VOICE-VALIDATION.md`.
- optional DOCX → `DOCX-FORMAT.md` + builder.

The former duplicate `SCRIPT-PRODUCTION.md` lifecycle owner is retired in v1.11.2. Do not load all reference material by default.

# Authority chain

```text
accepted PRD
→ work/voice-requirements.md
→ work/voice-production.md
→ output/final.html → Production Assets → Voice
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

- PRD owns project/gameplay truth and the need for a Voice asset.
- Flow 5 owns which Voice assets exist and their communication intent/context.
- Flow 6 owns canonical production content.
- `final.html` is derived developer/operator presentation only.
- DOCX is optional export only.

# Flow 5 → Flow 6 interface

A Flow 5 entry is ready only when downstream production can recover communication job, listener state, required information, intended outcome, Speaker, optional source timing truth, and scope guardrails without project-level guessing.

Do not move downstream performance-writing fields into Flow 5 and do not invent project facts to fill downstream presentation.

# Canonical Voice Production

Each canonical entry requires:

```text
Voice ID + Title
Type
Speaker
Estimated Duration
canonical performance payload
```

`Type` and `Speaker` match Flow 5. Do not duplicate Trigger/Purpose/requirements/source refs/reasoning/QA into every canonical entry.

# Project HTML production surface

The same `output/final.html` is the default human-facing project document.

Production Assets extends the accepted PRD navigation rather than rebuilding it:

```text
03 Development
   global development pages
   gameplay/objective sections

04 Production Assets
   VOICE
   <gameplay section title>
   <accepted PRD package label>
```

Gameplay/objective sections remain under Development and accepted PRD page codes stay unchanged. `VOICE` appears once; every linked Voice section shows section title + accepted PRD label, with natural wrapping for long sidebar text.

Each Voice section page shows gameplay title, accepted PRD package label/context, Voice line count, Primary Speaker, and compact Voice Setup.

Each line shows:

```text
title
→ <PRD package label> · Voice Line X/Y
→ Context = exact Flow 5 Trigger
→ Speaker + Estimated Duration
→ canonical production text
→ Copy Prompt
```

The visible Context is the existing Flow 5 Trigger projected into HTML; it is not a new Flow 6 field. Internal Purpose/requirements/source refs/reasoning/QA stay in their owners.

## Optional DOCX

`output/Voice Production.docx` may be generated when specifically useful. It remains a derived export, not the normal human-facing Voice output.

# First wrong owner / bounded revision

```text
project fact → PRD authority
Voice scope/context → Flow 5
canonical Voice content → Flow 6
correct canonical Voice + wrong Production Assets HTML → PRD renderer compositor
optional DOCX-only defect → Voice builder
```

Revise only invalidated Voice/Speaker scope plus continuity materially affected by the change. Voice-only production changes do not reopen PRD acceptance when PRD canonical meaning is unchanged.

# Flow 7 proof

Use:

```text
Mechanical
+ Communication Conservation
+ integrated Voice Script Readiness
+ Project HTML Visual when claimed
+ optional DOCX Visual
+ optional Audio Evidence
```

Static HTML parity is not visual proof; visual PASS requires actual rendered/browser inspection.

# Non-negotiable rules

- SoundMaker scope is **Eleven v3 only**.
- Voice Production is downstream from accepted PRD, not a separate source-intake project.
- recover existing project context before asking the user.
- Voice scope cannot change silently after Flow 5.
- downstream performance/presentation cannot create project facts, Speakers, Channels, Triggers, mechanics, rewards, outcomes, or source timing truth.
- exact current production content remains owned by `work/voice-production.md`.
- generated-audio quality requires actual heard evidence.
- do not create separate Voice HTML, asset manifest, settings database, score system, or extra approval layer without a concrete defect.
- stop when current requested scope is ready.
