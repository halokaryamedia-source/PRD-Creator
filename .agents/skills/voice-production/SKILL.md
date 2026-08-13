---
name: voice-production
description: Semantic/product-contract specialist for PRD-Creator Flow 5–7. Use when the active boundary is Voice Requirement scope, Eleven v3 wording/SoundMaker quality, what Voice artifacts represent, or final Voice validation/delivery semantics. Preserve exact upstream PRD/Voice scope and never invent gameplay, lore, speaker/channel, trigger, or audio evidence.
---

# Voice Production

Own semantic/product-contract judgment around Voice Production Kit Flow 5–7. Detailed procedures remain in `kits/voice-production-kit/`.

## Trigger

Use when the wrong contract concerns:

- accepted PRD → Voice Requirements;
- Voice ID / Type / speaker / channel / trigger / communication scope;
- Voice Requirements → final Eleven v3 wording;
- SoundMaker preparation/generation behavior, duration planning, voice-fit judgment, or canonical prompt sync;
- what script/DOCX/audio acceptance is allowed to claim.

Do not select merely because a task mentions ElevenLabs, DOCX, audio, Python, or CI. Pure builder/validator mechanics route to the nearest technical owner.

## Routing

1. Verify the accepted PRD revision and current Voice state.
2. Recover existing project facts before asking the user.
3. Identify the active owner:
   - Flow 5 → `VOICE-EXTRACTION.md` + `work/voice-requirements.md`;
   - Flow 6 lifecycle/full-project preparation → `SCRIPT-PRODUCTION.md` + `SOUNDMAKER.md`;
   - Flow 6 actual Eleven v3 generation/revision → `SOUNDMAKER.md`;
   - Flow 7 → `VOICE-VALIDATION.md`.
4. Open only the deep Eleven v3 reference required by the active problem.
5. Route missing project facts upstream instead of repairing them in performance wording.

## Authority

```text
accepted PRD
→ voice-requirements.md
→ SoundMaker v3 preparation/generation quality
→ voice-production.md
→ Voice Production.docx (derived)
→ voice-acceptance.md
→ voice-state.yaml
```

Rules:

- Flow 5 owns **which Voice moments exist and what they must communicate**;
- Flow 6 owns **final Eleven v3 wording/performance notation**, not Voice scope;
- `SOUNDMAKER.md` is the operational procedure, not a second wording owner;
- Flow 7 owns **revision-specific evidence**, not rewritten dialogue;
- generated audio is evidence/output, never upstream project authority;
- exact generated/approved wording must synchronize into `work/voice-production.md` before current alignment is claimed;
- ElevenLabs references own production technique only.

## Flow 5 judgment

- extract only justified player-facing communication moments;
- preserve supported speaker/channel/trigger/function;
- do not invent a radio/communicator layer from references;
- deduplicate repeated briefing unless trigger/function genuinely differs;
- `no_voice_required` is valid;
- implementation-only detail does not automatically become narration.

## Flow 6 / SoundMaker judgment

SoundMaker scope is **Eleven v3 only**.

### Preparation Mode

Use for script/DOCX work when audio generation is not requested.

- full current Voice scope may be prepared in one bounded pass;
- do not require audio testing or per-line generation approval;
- apply per-line SoundMaker construction plus project-level speaker continuity/anti-repetition review;
- duration and pronunciation remain planned/unverified until evidence exists.

### Generation Mode

Use only when actual ElevenLabs generation/revision is requested.

- one active Voice ID;
- one exact reviewed prompt;
- actual feedback/approval loop;
- approved generated wording syncs back to canonical script.

Semantic guardrails:

- preserve the exact Flow 5 Voice ID/Type set unless Flow 5 is reopened;
- performance direction may shape delivery but not create facts/events;
- duration targets are planned before final wording;
- a flat script is not repaired by tag stacking;
- batch preparation must detect accidental template repetition across related lines;
- builder output is regenerated from canonical Markdown.

## Flow 7 judgment

Validate the exact current revision for:

- requirement coverage / factual fidelity;
- Voice ID / Type parity;
- speaker/channel/trigger consistency;
- terminology/pronunciation risk;
- project-level performance continuity and accidental template repetition;
- canonical prompt ↔ actual generated prompt alignment only when audio is in scope;
- DOCX mechanical/visual integrity when claimed;
- actual generated-audio quality only when audio was reviewed.

Critical/Major findings block `voice_delivery_ready`.

## Technical handoff

If semantic Voice scope/wording/artifact meaning is correct but builder/validator mechanics are wrong, route Maintenance to `kits/voice-production-kit/AGENTS.md` and the exact implementation source.

## Audio evidence

Use truthful states:

- `not_provided`;
- `partial_review`;
- `reviewed_passed`;
- `reviewed_with_findings`.

Preparation Mode may legitimately finish with `not_provided`. Never infer audio quality from script quality or DOCX appearance.

## Acceptance gate

Before completion verify as applicable:

- no unsupported Voice scope appeared;
- wording preserves required project meaning;
- SoundMaker v3 procedure was applied where relevant;
- Preparation Mode includes project-level continuity/anti-template review;
- canonical script and derived artifacts agree;
- actual audio claims match actual reviewed evidence only when audio is in scope;
- delivery state applies to the exact current revision.
