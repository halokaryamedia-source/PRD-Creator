---
name: voice-production
description: Semantic/product-contract specialist for PRD-Creator Flow 5–7. Use when the active boundary is PRD-derived Voice asset scope, Flow 5→6 intent completeness, Eleven v3 wording/SoundMaker quality, actor selection, communication conservation, consolidated Production Assets output, or final Voice validation/delivery semantics. Preserve exact upstream PRD/Voice scope and never invent gameplay, lore, speaker/channel, trigger, timing truth, actor voice, or audio evidence.
---

# Voice Production

Own semantic/product-contract judgment around Voice Production Kit Flow 5–7. Detailed procedures remain in `kits/voice-production-kit/`.

## Trigger

Use when the wrong contract concerns:

- accepted PRD → Voice assets required for development;
- Voice ID / Type / Speaker / Channel / Trigger / Purpose / communication scope;
- Flow 5 requirement completeness for SoundMaker;
- Voice Requirements → exact Eleven v3 production wording;
- actor voice selection / Voice Cast ownership;
- Voice Intent Completeness, Communication Conservation, duration, or integrated readiness;
- consolidated `final.html → Production Assets → Voice` meaning;
- Voice validation/delivery semantics.

Do not select merely because a task mentions ElevenLabs, DOCX, audio, Python, or CI. Pure renderer/builder/validator mechanics route to the nearest technical owner.

## Routing

1. Verify accepted PRD revision and current Voice state.
2. Treat the accepted PRD as normal upstream source; do not ask the user to re-enter project source for Voice.
3. Recover existing project facts before asking the user.
4. Identify the active owner:
   - Flow 5 → `VOICE-EXTRACTION.md` + `work/voice-requirements.md`;
   - Flow 6 lifecycle/output → `SCRIPT-PRODUCTION.md`;
   - Flow 6 wording/Generation Mode → `SOUNDMAKER.md`;
   - Flow 7 → `VOICE-VALIDATION.md`;
   - optional DOCX → `DOCX-FORMAT.md`/builder;
   - correct canonical Voice but wrong same-HTML composition → Project Document Generator Production Assets compositor.
5. Open only the deep Eleven v3 reference required by the active issue.
6. Route missing project facts upstream rather than repairing them in performance wording.

## Authority

```text
accepted PRD
→ voice-requirements.md
→ voice-production.md
→ final.html → Production Assets → Voice
→ voice-acceptance.md
→ voice-state.yaml
```

- PRD owns product/gameplay truth and the requirement for a Voice asset.
- Flow 5 owns which Voice assets exist and their approved communication intent/context.
- Flow 6 owns exact Eleven v3 wording, Estimated Duration, and actor voice selection when known.
- `voice-production.md` is canonical production content; SoundMaker is a procedure, not a second wording owner.
- `final.html` is derived human/operator presentation, not another authority.
- DOCX is optional export only.
- generated audio is evidence/output, never upstream project authority.

# Flow 5 judgment

Extract only justified player-facing communication moments from the accepted PRD.

A Flow 5 entry is ready only when SoundMaker can recover without product-level guessing:

```text
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

Do not pre-write dialogue or add fields for Performance Shape, Landing, tags, CAPS/punctuation, selected actor voice, Stability, Surface, or production-estimated duration.

# Flow 6 / SoundMaker judgment

SoundMaker scope is **Eleven v3 only**.

Preparation quality follows:

```text
Voice Intent Completeness
→ internal Performance Fill Map
→ performance writing
→ Communication Conservation
→ script-ready
→ integrated Voice Script Readiness
```

SoundMaker may decide sentence split, beats, punctuation, CAPS, tags, pacing, Performance Shape, Landing, and Estimated Duration inside approved intent. Every standalone prepared Voice ID begins with at least one deliberate initial performance-direction tag; transition tags remain conditional on a real audible state change.

Return upstream when unresolved work would change project facts, Voice scope, Speaker/Channel/Trigger/Purpose, required communication, or source timing truth.

## Voice Cast

`voice-production.md` may store selected actor voices once:

```text
Voice Cast:
- <Speaker>: <selected ElevenLabs voice>
```

Do not repeat commercial voice names per line.

Preparation may leave selection pending while a Target Voice Profile is sufficient. Generation Mode requires the active Speaker's actual intended voice to be selected. Never invent a commercial voice to make a field look complete.

# Production output judgment

Default human-facing output is the **same project HTML**:

```text
PRD core
+
Production Assets
└── Voice
```

The Voice page stays minimal:

```text
Voice Setup once with the selected ElevenLabs voice prominent
→ gameplay-ordered Voice sections
→ title
→ Speaker + Estimated Duration as secondary metadata
→ exact Eleven v3 text with performance directions visually distinct
→ Copy integrated with the script panel
```

Do not expose Trigger/Purpose/requirements/source refs/reasoning/QA merely because they exist internally.

Do not create a separate Voice HTML or Asset Requirement HTML by default.

Optional DOCX remains allowed when specifically useful.

# First wrong owner / bounded revision

```text
project fact → PRD authority
Voice scope/Speaker/Channel/Trigger/Purpose/required communication/source timing → Flow 5
wording/performance/Estimated Duration/actor selection → Flow 6
correct canonical Voice + wrong Production Assets HTML → PRD renderer compositor
optional DOCX-only defect → Voice builder
audio-only defect → Generation Mode
```

Voice-only production changes rerender `final.html` but do not reopen PRD acceptance when PRD canonical sources are unchanged.

Revise only invalidated Voice/Speaker scope plus continuity materially affected by the change.

# Flow 7 judgment

Use:

```text
Mechanical
+ Communication Conservation
+ one integrated Voice Script Readiness review
+ Project HTML Visual when claimed
+ optional DOCX Visual
+ optional Audio Evidence
```

Static HTML parity is not visual proof. Audio quality requires actual heard evidence.

Critical/Major findings block `voice_delivery_ready`.

# Stop rule

Stop once current Voice Production is script-ready, Communication Conservation and integrated readiness pass, the requested consolidated HTML is current, and remaining evidence is stated honestly.

Do not add separate Voice HTML, asset manifests, settings databases, scores, extra approval layers, or speculative hardening without a concrete defect.
