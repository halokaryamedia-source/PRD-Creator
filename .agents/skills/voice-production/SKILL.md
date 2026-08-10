---
name: voice-production
description: Semantic specialist for PRD-Creator Flow 5–7. Use when the active boundary is Voice Requirement Extraction, ElevenLabs performance-script production, Voice Production DOCX generation/formatting, or final Voice validation/delivery, including maintenance of the Voice builder/validator when those surfaces are the root owner. Preserve exact upstream PRD/Voice scope and never invent gameplay, lore, speaker/channel, trigger, or audio evidence.
---

# Voice Production

Own the semantic procedure around Voice Production Kit Flow 5–7. Detailed production contracts remain in `kits/voice-production-kit/`; this skill routes work to the correct Flow and protects upstream authority.

## Trigger

Use when the actual boundary is one of:

- accepted PRD → Voice Requirements;
- Voice Requirements → final spoken/performance wording;
- canonical script → `Voice Production.docx`;
- script/DOCX validation and delivery readiness;
- Voice builder/validator maintenance where the defect belongs to Flow 5–7.

Do not select merely because a task mentions ElevenLabs, DOCX, narration, dialogue, or audio. Select because the semantic owner is the Voice production chain.

## Required Routing

1. Verify the upstream accepted PRD revision before Voice extraction.
2. Identify the active Flow owner:
   - Flow 5 → `VOICE-EXTRACTION.md` + `work/voice-requirements.md`;
   - Flow 6 → `SCRIPT-PRODUCTION.md`, `DOCX-FORMAT.md`, `work/voice-production.md`, builder;
   - Flow 7 → `VOICE-VALIDATION.md`, validator, acceptance/delivery state.
3. Read only the smallest relevant kit procedure/source.
4. Route missing project facts upstream instead of repairing them in dialogue.

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
- generated audio, when supplied, is evidence/delivery material only and never upstream project authority.

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
- CAPS, ellipsis, and line breaks are purposeful performance notation, not decoration;
- estimated duration is an expectation, not measured audio proof;
- wording must preserve official terminology and project facts;
- builder output must be regenerated from canonical Markdown rather than edited directly.

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

## Maintenance Rule

For a Voice artifact defect:

```text
observe defect
→ classify owner: requirement / script / builder / validator / evidence
→ fix the smallest root owner
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
