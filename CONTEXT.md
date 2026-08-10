# Workspace Context

Last verified: 2026-08-10
Stability: stable
Owner: workspace

## Purpose

This workspace supports a two-stage production system:

1. turn incomplete/uneven project direction into documentation that developers, level designers, and the wider production team can use;
2. derive validated ElevenLabs-ready voice production from accepted project/gameplay/story documentation without inventing upstream design.

## Project Document Generator

Current owner: `kits/project-document-generator/`.

```text
project source
→ requirement recovery
→ ready_for_prd
→ canonical content.md
→ rendered final.html
→ PRD acceptance
→ handoff_ready
```

## Voice Production Kit

Current owner: `kits/voice-production-kit/`.

```text
handoff_ready PRD
→ Flow 5 voice-requirements.md
→ voice_requirements_ready
→ Flow 6 voice-production.md
→ Voice Production.docx
→ voice_script_ready
→ Flow 7 voice-acceptance.md
→ voice_delivery_ready
```

Flow 5 owns **which communications exist and what they must communicate**. Flow 6 owns **final spoken wording/performance notation**. Flow 7 owns **revision-specific script/DOCX validation and delivery readiness**.

## Stable Terms

**Canonical PRD Content** — `work/content.md`; accepted project meaning used by downstream production.

**Voice Requirement** — justified player-facing communication moment with approved speaker/channel/trigger/purpose/required facts.

**Voice Requirements** — `work/voice-requirements.md`; canonical Flow 5 voice-scope owner.

**Voice Production Script** — `work/voice-production.md`; canonical Flow 6 final spoken/performance wording.

**Voice Production DOCX** — `output/Voice Production.docx`; derived presentation artifact.

**Voice Acceptance** — `work/voice-acceptance.md`; Flow 7 evidence/findings for an exact script/DOCX revision.

**Voice State** — `state/voice-state.yaml`; lifecycle/status owner across Flow 5–7.

**Voice Delivery Ready** — script + DOCX scope has passed current Flow 7 gates. It does not imply generated audio was reviewed unless audio evidence explicitly says so.

**Performance Direction** — concise square-bracket delivery direction; never a new project fact/event.

**Estimated Duration** — expected spoken-duration range; not measured audio proof.

**Audio Evidence** — explicit record of whether actual generated audio was supplied/reviewed (`not_provided`, `partial_review`, `reviewed_passed`, `reviewed_with_findings`).

**Golden Sample / Approved Reference** — demonstrated structure/presentation/performance-quality reference; never automatic project fact or quota.

## Reference State

`kits/voice-production-kit/REFERENCE/Aftershock/README.md` records the audited original Aftershock Voice Production reference contract and source SHA-256. The active builder/validator does not depend on that binary at runtime.

The old paired Aftershock Gameplay HTML V1.2 is not active factual authority; current accepted project PRDs own upstream facts.

## Retired Historical Package

`Production Document Builder/` v0.2.0 has been removed from the live `Local` tree after real-project integration proof and final retirement audit. Its Golden Sample is preserved byte-identically by the active approved template, and Git history is the recovery path for old implementation details.

## Stable Structure

- `docs/foundation/` — durable production policy.
- `docs/knowledge/` — continuity, decisions, ownership, backlog.
- `kits/project-document-generator/` — active PRD Flow 2–4 owner.
- `kits/voice-production-kit/` — active Voice Flow 5–7 owner.
- `workspace/active/` — active project packages.
- `workspace/saved/` — retained project packages.

## Architecture Principle

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance ≠ Voice Requirements ≠ Voice Production Script ≠ DOCX ≠ Voice Acceptance ≠ Audio
```

A mechanically valid or visually correct DOCX is not generated-audio proof. A final script cannot introduce Voice IDs or project facts absent from accepted upstream owners.

## Current Development State

Flows 1–7 are implemented on permanent branch `Local` and have now been exercised end-to-end on the real **The Clockwork Vault** project. The proof produced `handoff_ready` PRD state and `voice_delivery_ready` script/DOCX state, while truthfully recording `audio_evidence: not_provided`. Migration is complete. The next operational step is to use the active pipeline for the next project and apply only evidence-backed fixes.
