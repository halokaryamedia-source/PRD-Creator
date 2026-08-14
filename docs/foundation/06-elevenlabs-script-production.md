# Eleven v3 Performance Script Production

Status: active Flow 6 policy

## Purpose

Flow 6 turns `voice_requirements_ready` into canonical Eleven v3 production wording and publishes it into the **same project HTML** without changing upstream Voice scope or PRD meaning.

## Ownership

```text
accepted PRD
→ work/voice-requirements.md
→ Flow 6 / SoundMaker v3
→ work/voice-production.md
→ output/v<document.version>/prd.html → Production Assets → Voice
```

- accepted PRD owns project/gameplay truth;
- `voice-requirements.md` owns Voice asset scope, communication intent/context, and authoritative timing truth when one exists;
- `SOUNDMAKER.md` owns Eleven v3 preparation/generation procedure;
- `voice-production.md` owns selected actor voice when known, Estimated Duration, and exact performance wording;
- project HTML is derived presentation only;
- DOCX is optional export.

# Flow 5 → Flow 6 interface

Flow 6 consumes the Flow 5 entry as the normal authoring interface:

```text
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

Use accepted PRD context only when the requirement still lacks genuinely necessary delivery-relevant context.

`Timing Constraint` is optional upstream truth. It is not Flow 6 `Estimated Duration`.

Performance Shape, Landing, final wording, punctuation/CAPS/tags, Target Voice Profile, selected actor voice, Stability, Surface, and production-estimated duration remain Flow 6 decisions unless upstream meaning explicitly constrains them.

# Preparation Mode

Default when audio generation is not requested.

```text
Voice Requirements
→ Voice Intent Completeness
→ internal Performance Fill Map
→ SoundMaker writing
→ Communication Conservation
→ integrated Voice Script Readiness
→ canonical voice-production.md
→ consolidated final.html
```

Preparation Mode may process the full current Voice scope, may use a Target Voice Profile before actual actor selection, and requires no audio test or per-line approval loop.

# Voice Cast

The canonical production script may store actor selection once before gameplay sections:

```text
Voice Cast:
- <Speaker>: <selected ElevenLabs voice>
```

Do not repeat commercial voice names in every line.

An unselected actor voice may remain pending during Preparation Mode when a clear Target Voice Profile is enough to write responsibly. Actual Generation Mode requires the active Speaker's intended voice to be selected.

Never invent a commercial voice to make preparation look complete.

# Canonical entry

Every Voice entry contains:

```text
Voice ID + Title
Type
Speaker
Estimated Duration
exact Eleven v3 performance block beginning with at least one initial performance-direction tag
```

`Type` and `Speaker` match Flow 5.

Do not duplicate Channel, Trigger, Purpose, Timing Constraint, requirement bullets, source refs, Performance Fill Map reasoning, WPM calculations, voice-fit ratings, or QA notes into every canonical entry.

# Consolidated project HTML

After canonical Voice Production exists, the normal renderer publishes it into the same `output/v<document.version>/prd.html` as a professional-only downstream section while preserving the existing accepted PRD navigation/page identity.

```text
03 Development
   global development pages
   gameplay/objective sections

04 Production Assets
   VOICE
   <gameplay section title>
   <accepted PRD package label>
```

Production Assets is additive. It does not promote gameplay packages out of Development and does not renumber PRD package/page codes.

Each Voice section page uses:

```text
Voice Production
→ gameplay section title
→ accepted PRD package label + gameplay context
→ Voice line count + Primary Speaker
→ compact Voice Setup for that gameplay section
```

Each Voice line shows:

```text
title
→ accepted PRD package label · Voice Line X/Y
→ Context = exact Flow 5 Trigger
→ Speaker + Estimated Duration
→ exact Eleven v3 prompt with performance directions visually distinct
→ Copy Prompt
```

The visible `Context` is a direct projection of the existing Flow 5 Trigger, not a duplicate Flow 6 field. Purpose, `Must communicate`, `Must not add/repeat`, source refs, SoundMaker reasoning, WPM calculations, QA notes, and other internal production metadata stay out of the HTML.

Voice navigation labels may wrap naturally and must remain readable without clipping. `Copy Prompt` copies only the exact canonical performance block.

No separate Voice HTML is created by default.

# Optional DOCX

`Voice Production.docx` remains available only when explicitly requested or materially useful as a portable export. It is not a normal Flow 6 readiness requirement.

# Generation Mode

Used only when actual ElevenLabs output is requested.

```text
one active Voice ID
→ actual actor voice selected
→ exact reviewed prompt
→ generate / feedback / approve
→ canonical sync
→ rerender same final.html when actor/prompt changed
```

# Scope guard

Flow 6 may refine delivery but may not silently change Voice scope, Speaker/Channel/Trigger/Purpose, gameplay/lore/mechanics/rewards/outcomes, required communication, or authoritative timing truth.

Production interpretation such as sentence splitting, performance shape, landing, punctuation, CAPS, tags, pacing, Estimated Duration, and actor selection may be decided by SoundMaker inside approved Voice/project boundaries.

# First wrong owner / bounded revision

```text
project fact → PRD authority
Voice scope/Speaker/Channel/Trigger/Purpose/required communication/source timing → Flow 5
wording/performance/Estimated Duration/actor selection → Flow 6
correct canonical Voice + wrong Production Assets HTML → PRD renderer compositor
optional DOCX-only defect → Voice DOCX builder
audio-only defect → Generation Mode
```

Reopen only invalidated Voice/Speaker scope plus continuity materially affected by the change. Voice-only production changes do not reopen PRD acceptance when PRD canonical sources are unchanged.

# Flow 6 gate

Set `voice_script_ready` only when:

- current Flow 5 status is `voice_requirements_ready` for the same accepted PRD revision;
- Flow 5 intent is complete enough to author without product-level guessing;
- Voice ID, Type, and Speaker parity are intact;
- authoritative timing constraints are honored when present;
- every entry has title, Estimated Duration, and canonical performance wording;
- every performance block begins with at least one deliberate initial direction tag;
- Voice Intent Completeness is sufficient;
- Communication Conservation passes;
- integrated Voice Script Readiness passes;
- no unresolved placeholder/upstream contradiction remains.

The consolidated project HTML is regenerated when project HTML delivery is current scope. Generated-audio quality is not a prerequisite unless audio is explicitly requested.

# Stop rule

Stop after current Preparation Mode scope is ready and requested output is current. Do not add separate Voice HTML, asset manifests, schemas, scores, settings databases, approval layers, or speculative hardening without a concrete defect.
