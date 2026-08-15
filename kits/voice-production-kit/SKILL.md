---
name: voice-production-kit
description: Extract Voice requirements from accepted PRDs, prepare canonical Eleven v3 production content, conserve required communication, and publish developer-ready Voice Production into matching 04 AUDIO resources without inventing upstream project facts.
version: 1.11.2
---

# Voice Production Kit

## Flow ownership

1. **Flow 5 — Voice Requirement Extraction**: accepted project/PRD meaning → `work/voice-requirements.md`.
2. **Flow 6 — Voice Production**: Voice Requirements → canonical `work/voice-production.md` → matching AUDIO resources in the same project `output/v<document.version>/prd.html`.
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
accepted project / PRD meaning
→ work/voice-requirements.md
→ work/voice-production.md
→ output/v<document.version>/prd.html
   → 04 Production Assets
      → matching gameplay moment
         → AUDIO
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

- PRD/project authority owns gameplay/story truth and the need for a Voice asset.
- Flow 5 owns which Voice assets exist and their communication intent/context.
- Flow 6 owns canonical production content, Estimated Duration, and actor selection when known.
- `output/v<document.version>/prd.html` is derived developer/operator presentation only.
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

The canonical script may also store one selected ElevenLabs actor voice per recurring Speaker in its `Voice Cast` header when known.

# Project HTML production surface

The same `output/v<document.version>/prd.html` is the default human-facing project document.

Production Assets extends the accepted PRD navigation rather than rebuilding it:

```text
03 Development
   global development pages
   gameplay/objective sections

04 Production Assets
   <gameplay section title>
      <accepted PRD package label>
```

Voice does not own a separate sidebar category or an `Audio → Voice Production` dashboard. Canonical Voice entries are merged as normal `AUDIO` resources inside their matching gameplay moments.

Visible dialogue resource:

```text
AUDIO
<Character> — <Line Title>

Function
<communication/story purpose>

Voice Preset
<selected actor voice>

ElevenLabs Model
Eleven v3

Estimated Duration
<duration>

Prompt
<exact canonical performance payload>
```

Do not require visible line count, Primary Speaker, compact Voice Setup, Flow 5 Context/Trigger, or separate Speaker field in 04. Those are not current reader-first Production Asset fields.

Performance-direction tags are visually distinct from spoken text. `Copy Prompt` copies the exact canonical performance payload.

Internal Purpose/Trigger/requirements/source refs/reasoning/QA stay in their owners.

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
- Voice Production is downstream from accepted project/PRD meaning, not a separate source-intake project.
- recover existing project context before asking the user.
- Voice scope cannot change silently after Flow 5.
- downstream performance/presentation cannot create project facts, Speakers, Channels, Triggers, mechanics, rewards, outcomes, or source timing truth.
- exact current production content remains owned by `work/voice-production.md`.
- generated-audio quality requires actual heard evidence.
- do not create separate Voice HTML, asset manifest, settings database, score system, or extra approval layer without a concrete defect.
- stop when current requested scope is ready.
