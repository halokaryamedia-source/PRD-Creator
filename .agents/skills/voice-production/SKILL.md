---
name: voice-production
description: Semantic/product-contract specialist for PRD-Creator Flow 5–7. Use when the active boundary is Voice Requirement scope, performance-script meaning, what the Voice Production artifact must represent, or final Voice validation/delivery semantics. Do not select merely because DOCX builder/validator mechanics fail when canonical Voice semantics are already correct; pure technical Maintenance may route directly to the nearest kit implementation owner. Preserve exact upstream PRD/Voice scope and never invent gameplay, lore, speaker/channel, trigger, or audio evidence.
---

# Voice Production

Own semantic/product-contract judgment around Voice Production Kit Flow 5–7. Detailed production and executable mechanics remain in `kits/voice-production-kit/`; this skill protects the accepted-PRD → Voice scope → wording → artifact → acceptance contract instead of becoming a generic Python/DOCX/tooling owner.

## Trigger

Use when the actual wrong contract is one of:

- accepted PRD → Voice Requirements;
- Voice moment scope / ID / Type / speaker / channel / trigger;
- Voice Requirements → final spoken/performance wording;
- what the canonical script / DOCX is required to represent;
- script/DOCX acceptance and delivery-readiness semantics;
- a builder/validator change whose required behavior changes or misrepresents the Flow 5–7 product contract.

Do **not** select merely because:

- a task mentions ElevenLabs, DOCX, narration, dialogue, audio, or Python;
- `builder/build_docx.py` has a pagination/parser/formatting implementation bug while canonical script semantics are already correct;
- `validator/validate.py` has a mechanical implementation bug;
- CI/test/dependency tooling fails.

Pure technical Maintenance may route directly through `kits/voice-production-kit/AGENTS.md` to the exact implementation owner without a root specialist.

## Required Routing

1. Verify the upstream accepted PRD revision before Voice extraction.
2. Identify whether the defect is semantic/product-contract or executable mechanics.
3. For semantic/product-contract work, identify the active Flow owner:
   - Flow 5 → `VOICE-EXTRACTION.md` + `work/voice-requirements.md`;
   - Flow 6 → `SCRIPT-PRODUCTION.md`, `DOCX-FORMAT.md`, `work/voice-production.md`, artifact representation contract; when the task materially depends on Eleven v3 performance/model/voice/duration/pronunciation behavior, enter through `kits/voice-production-kit/references/elevenlabs/README.md` and read only the relevant supporting page;
   - Flow 7 → `VOICE-VALIDATION.md`, acceptance/delivery state.
4. Read only the smallest relevant kit procedure/source.
5. Route missing project facts upstream instead of repairing them in dialogue or formatting.

## Authority Guard

```text
accepted PRD
→ voice-requirements.md
→ voice-production.md
→ Voice Production.docx (derived)
→ voice-acceptance.md
→ voice-state.yaml
```

Rules:

- Flow 5 owns **which Voice moments exist and what they must communicate**;
- Flow 6 owns **final wording/performance notation**, not Voice scope;
- Flow 7 owns **revision-specific acceptance/delivery evidence**, not rewritten dialogue;
- DOCX is presentation, never the editable wording authority;
- generated audio, when supplied, is evidence/delivery material only and never upstream project authority;
- ElevenLabs references own production technique only and never become a project-fact source.

## Flow 5 Judgment

- extract only justified player-facing communication moments;
- every moment must trace to accepted PRD evidence;
- speaker/channel/trigger/function must already be supported or explicitly resolved;
- do not create a radio/communicator layer because a reference used one;
- deduplicate repeated objective narration unless function/trigger genuinely differs;
- `no_voice_required` is a valid result;
- implementation-only details that are not player-facing do not become narration merely because they exist in the PRD.

## Flow 6 Judgment

- preserve the exact Flow 5 Voice ID and Type set unless Flow 5 is explicitly reopened;
- performance directions describe delivery only;
- CAPS, punctuation, ellipsis, line breaks, and Audio Tags are purposeful performance notation, not decoration;
- when target duration matters, budget it before final wording rather than forcing an oversized script to fit afterward;
- estimated duration is an expectation, not measured audio proof;
- wording must preserve official terminology and project facts;
- use the evidence-backed ElevenLabs reference instead of inventing universal tag, duration, voice, or settings rules;
- builder output must be regenerated from canonical Markdown rather than edited directly;
- decide what the Voice artifact must represent, but leave pure parser/DOCX implementation mechanics to the kit-local owner when semantics are already correct.

## Flow 7 Judgment

Validate the exact current revision for:

- requirement coverage and factual fidelity;
- Voice ID / Type parity;
- speaker/channel/trigger consistency;
- terminology and material pronunciation risk;
- whole-project performance continuity, pacing, and notation;
- DOCX mechanical integrity;
- rendered-page visual quality when a visual-ready claim is made;
- actual generated-audio quality only when audio exists and was reviewed.

Critical/Major findings block `voice_delivery_ready`.

## Technical Handoff Rule

If investigation proves:

```text
Voice scope/wording/artifact contract is correct
+ executable builder/validator mechanics are wrong
```

then route Maintenance to:

`kits/voice-production-kit/AGENTS.md` → exact implementation source.

Do not keep this root specialist loaded solely as a Python/DOCX debugging wrapper. Shared dependency/test/CI failures belong to root repository-engineering owners (`requirements.lock.txt`, `tests/`, `tools/`, workflows).

The real blank-page defect is the model example: Voice semantics were correct; builder pagination mechanics owned the correction.

## Maintenance Rule

For a Voice defect:

```text
observe defect
→ classify semantic/product contract vs executable mechanics
→ semantic wrong: use this specialist + smallest Flow owner
→ semantics correct, mechanics wrong: nearest kit AGENTS + exact implementation owner
→ rebuild derived artifact when needed
→ rerun only the proof invalidated by the change
```

Do not patch the DOCX directly when canonical script/builder logic is wrong. Do not edit `voice-acceptance.md` to hide a defect in an upstream owner.

## Audio Evidence Boundary

Use truthful evidence state:

- `not_provided`;
- `partial_review`;
- `reviewed_passed`;
- `reviewed_with_findings`.

Never infer generated-audio quality from script quality or DOCX appearance.

## Acceptance Gate

Before completion re-check the original development-brief criteria and verify as applicable:

- no new unsupported Voice scope appeared;
- wording communicates the required facts without inventing upstream design;
- canonical script and DOCX materially agree;
- visual/audio claims match actual evidence;
- delivery state applies to the exact current revision.
