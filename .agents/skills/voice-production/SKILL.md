---
name: voice-production
description: Semantic/product-contract specialist for PRD-Creator Flow 5–7. Use when the active boundary is Voice Requirement scope, Eleven v3 performance wording/SoundMaker quality, what the Voice Production artifact must represent, or final Voice validation/delivery semantics. Preserve exact upstream PRD/Voice scope and never invent gameplay, lore, speaker/channel, trigger, or audio evidence.
---

# Voice Production

Own semantic/product-contract judgment around Voice Production Kit Flow 5–7. Detailed production mechanics remain in `kits/voice-production-kit/`; this skill protects the accepted-PRD → Voice scope → SoundMaker v3 wording → artifact → acceptance contract.

## Trigger

Use when the actual wrong contract is one of:

- accepted PRD → Voice Requirements;
- Voice moment scope / ID / Type / speaker / channel / trigger;
- Voice Requirements → final Eleven v3 spoken/performance wording;
- SoundMaker prompt quality, duration planning, performance arc, or canonical prompt sync;
- what the canonical script / DOCX is required to represent;
- script/DOCX/audio acceptance and delivery-readiness semantics.

Do **not** select merely because:

- a task mentions ElevenLabs, DOCX, narration, dialogue, audio, or Python;
- `builder/build_docx.py` has a pagination/parser/formatting implementation bug while canonical script semantics are already correct;
- `validator/validate.py` has a mechanical implementation bug;
- CI/test/dependency tooling fails.

Pure technical Maintenance may route directly through `kits/voice-production-kit/AGENTS.md` to the exact implementation owner without this semantic specialist.

## Required Routing

1. Verify the upstream accepted PRD revision before Voice extraction.
2. Identify whether the issue is semantic/product-contract or executable mechanics.
3. Identify the active Flow owner:
   - Flow 5 → `VOICE-EXTRACTION.md` + `work/voice-requirements.md`;
   - Flow 6 project-level script → `SCRIPT-PRODUCTION.md`;
   - Flow 6 actual one-line Eleven v3 generation/revision → `SOUNDMAKER.md` + only the relevant `references/elevenlabs/` page;
   - Flow 7 → `VOICE-VALIDATION.md`, acceptance/delivery state.
4. Read only the smallest relevant source.
5. Route missing project facts upstream instead of repairing them in performance wording.

## Authority Guard

```text
accepted PRD
→ voice-requirements.md
→ SoundMaker v3 execution quality
→ voice-production.md
→ Voice Production.docx (derived)
→ voice-acceptance.md
→ voice-state.yaml
```

Rules:

- Flow 5 owns **which Voice moments exist and what they must communicate**;
- Flow 6 owns **final Eleven v3 wording/performance notation**, not Voice scope;
- `SOUNDMAKER.md` is an execution/quality procedure inside Flow 6, not a second wording owner;
- Flow 7 owns **revision-specific acceptance/delivery evidence**, not rewritten dialogue;
- DOCX is presentation, never editable wording authority;
- generated audio, when supplied, is evidence/delivery material only and never upstream project authority;
- the exact prompt actually generated/approved must be synchronized into canonical `work/voice-production.md` before current alignment is claimed;
- ElevenLabs references own production technique only and never become project-fact sources.

## Flow 5 Judgment

- extract only justified player-facing communication moments;
- every moment must trace to accepted PRD evidence;
- speaker/channel/trigger/function must already be supported or explicitly resolved;
- do not create a radio/communicator layer because a reference used one;
- deduplicate repeated objective narration unless function/trigger genuinely differs;
- `no_voice_required` is valid;
- implementation-only details do not become narration merely because they exist in the PRD.

## Flow 6 / SoundMaker Judgment

SoundMaker model scope is **Eleven v3 only**.

Preserve the exact Flow 5 Voice ID and Type set unless Flow 5 is explicitly reopened.

Build quality in this order:

```text
requirement meaning
→ target duration first when specified
→ voice fit
→ performance arc
→ natural spoken wording
→ beat architecture
→ punctuation / line structure
→ selective CAPS
→ minimal Audio Tags
→ pronunciation safety
```

Rules:

- performance directions describe delivery only;
- CAPS, punctuation, ellipsis, line breaks, and Audio Tags are purposeful performance notation, not decoration;
- emotional changes need scene/communication reasons;
- a flat script is not repaired by stacking tags;
- reactions are timeline events;
- no SSML `<break>` for v3;
- when target duration matters, budget before final wording instead of forcing an oversized script to fit afterward;
- estimated duration is an expectation, not measured proof;
- use evidence-backed v3 references instead of inventing universal tag, duration, voice, or settings rules;
- if a user edits the exact prompt before generation and then approves it, that actually-used prompt becomes the canonical Flow 6 wording for the affected Voice ID;
- builder output is regenerated from canonical Markdown rather than edited directly.

## Flow 7 Judgment

Validate the exact current revision for:

- requirement coverage and factual fidelity;
- Voice ID / Type parity;
- speaker/channel/trigger consistency;
- terminology and material pronunciation risk;
- whole-project performance continuity, pacing, and notation;
- canonical prompt ↔ actual generated prompt alignment when audio is in scope;
- DOCX mechanical integrity;
- rendered-page visual quality when a visual-ready claim is made;
- actual generated-audio quality only when audio exists and was reviewed.

Critical/Major findings block `voice_delivery_ready`.

## Technical Handoff Rule

If Voice scope/wording/artifact contract is correct but executable builder/validator mechanics are wrong, route Maintenance to `kits/voice-production-kit/AGENTS.md` → exact implementation source.

Do not keep this root specialist loaded solely as a Python/DOCX debugging wrapper. Shared dependency/test/CI failures belong to root repository-engineering owners.

## Audio Evidence Boundary

Use truthful evidence state:

- `not_provided`;
- `partial_review`;
- `reviewed_passed`;
- `reviewed_with_findings`.

Never infer generated-audio quality from script quality or DOCX appearance.

## Acceptance Gate

Before completion verify as applicable:

- no unsupported Voice scope appeared;
- wording communicates required facts without inventing upstream design;
- v3 performance construction follows the current SoundMaker contract;
- canonical script and DOCX materially agree;
- if audio is claimed, the actual generated prompt is synchronized and the audio was actually reviewed;
- delivery state applies to the exact current revision.
