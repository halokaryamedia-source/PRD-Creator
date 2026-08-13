---
name: voice-production-kit
description: Extract Voice requirements from accepted PRDs, prepare canonical Eleven v3 production wording, conserve required communication, and publish developer-ready Voice Production into the same project HTML without inventing upstream project facts.
version: 1.11.2
---

# Voice Production Kit

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted PRD → `work/voice-requirements.md`.
2. **Flow 6 — Eleven v3 Script Production**: Voice Requirements → canonical `work/voice-production.md` → same project `output/final.html`.
3. **Flow 7 — Voice Validation & Delivery**: current revision → compact acceptance + delivery state.

DOCX and audio remain optional downstream scopes.

## Routing

- Flow 5 → `VOICE-EXTRACTION.md`.
- Flow 6 lifecycle/output → `SCRIPT-PRODUCTION.md`.
- writing/performance procedure → `SOUNDMAKER.md`.
- Flow 7 → `VOICE-VALIDATION.md`.
- optional DOCX → `DOCX-FORMAT.md` + builder.

Do not load all reference material by default.

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
- Flow 6 owns canonical production wording and Estimated Duration.
- `final.html` is derived developer/operator presentation only.
- DOCX is optional export only.

# Flow 5 → Flow 6 interface

A Flow 5 entry is ready only when downstream production can recover without project-level guessing:

```text
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

Do not move performance-writing fields into Flow 5 and do not invent project facts to fill downstream presentation.

# Canonical Voice Production

Each canonical entry requires:

```text
Voice ID + Title
Type
Speaker
Estimated Duration
exact performance block
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

Each Voice section page shows:

```text
Voice Production
→ gameplay section title
→ accepted PRD package label + gameplay context
→ Voice line count + Primary Speaker
→ compact Voice Setup
```

Each line shows:

```text
title
→ <PRD package label> · Voice Line X/Y
→ Context = exact Flow 5 Trigger
→ Speaker + Estimated Duration
→ exact canonical prompt
→ Copy Prompt
```

The visible Context is the existing Flow 5 Trigger projected into HTML; it is not a new Flow 6 field. Internal Purpose/requirements/source refs/reasoning/QA stay in their owners.

`Copy Prompt` copies only the exact canonical performance payload.

## Optional DOCX

`output/Voice Production.docx` may be generated when specifically useful. It remains a derived export, not the normal human-facing Voice output.

# First wrong owner / bounded revision

```text
project fact → PRD authority
Voice scope/context → Flow 5
canonical Voice wording/duration → Flow 6
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
- exact current wording remains owned by `work/voice-production.md`.
- generated-audio quality requires actual heard evidence.
- do not create separate Voice HTML, asset manifest, settings database, score system, or extra approval layer without a concrete defect.
- stop when current requested scope is ready.
