# Workspace Context

Last verified: 2026-08-10
Stability: stable
Owner: workspace

## Purpose

This workspace supports a two-stage production system:

1. turn incomplete/uneven project direction into documentation that developers, level designers, and the wider production team can use;
2. derive ElevenLabs-ready voice production from accepted project/gameplay/story documentation without inventing upstream design.

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
→ Flow 5 voice requirements
→ work/voice-requirements.md
→ voice_requirements_ready
→ Flow 6 canonical performance script
→ work/voice-production.md
→ derived Voice Production.docx
→ voice_script_ready
→ Flow 7 validation/delivery
```

Flow 5 owns **which communications exist and what they must communicate**. Flow 6 owns **the final spoken wording and performance notation**. Flow 7 owns final validation/delivery.

## Stable Terms

**Project Source** — original user/client/project material.

**Canonical PRD Content** — `work/content.md`; accepted project meaning used by downstream production.

**PRD Handoff State** — `state/handoff-state.yaml`; revision-specific readiness for production use.

**Voice Requirement** — justified player-facing communication moment with approved speaker/channel/trigger/purpose/required facts.

**Voice Requirements** — `work/voice-requirements.md`; canonical Flow 5 source of truth for voice-moment scope.

**Voice Production Script** — `work/voice-production.md`; canonical Flow 6 source of truth for final spoken wording, performance direction, emphasis, pauses, line breaks, and Estimated Duration.

**Voice Production DOCX** — `output/Voice Production.docx`; derived formatted artifact built from the canonical Voice Production Script.

**Voice State** — `state/voice-state.yaml`; lifecycle owner across Flow 5–7.

**Performance Direction** — concise square-bracket direction describing delivery, not a new project fact or event.

**Estimated Duration** — expected spoken-duration range; not measured audio proof.

**Golden Sample / Approved Reference** — demonstrated structure/presentation/performance-quality reference; never automatic project fact or quota.

## Reference State

`kits/voice-production-kit/REFERENCE/Aftershock/README.md` records the audited original Aftershock Voice Production reference contract and source SHA-256. The original v1.0.0 DOCX was re-read, rendered, and visually inspected during Flow 6, but its binary is not duplicated into the active repository because the current GitHub write surface does not safely materialize binary files. The active builder does not depend on that binary at runtime.

The old paired Aftershock Gameplay HTML V1.2 is also not duplicated into the active Voice kit because current accepted project PRDs are the factual upstream authority.

## Archived Package

`Production Document Builder/` remains Archived and non-authoritative.

## Stable Structure

- `docs/foundation/` — durable production policy.
- `docs/knowledge/` — continuity, decisions, ownership, backlog.
- `kits/project-document-generator/` — active PRD Flow 2–4 owner.
- `kits/voice-production-kit/` — active Voice Flow 5–6 owner.
- `workspace/active/` — active project packages.
- `workspace/saved/` — retained project packages.
- `Production Document Builder/` — Archived historical reference.

## Architecture Principle

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance ≠ Voice Requirements ≠ Voice Production Script ≠ DOCX ≠ Audio ≠ Delivery
```

A visually correct DOCX is not proof of final voice quality. A performance script must not introduce voice moments or facts absent from accepted upstream owners.

## Current Development State

Flows 1–6 are implemented on permanent branch `Local`. Flow 7 — Voice Validation & Delivery — is the next active boundary.
