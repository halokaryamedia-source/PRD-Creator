# Workspace Context

Last verified: 2026-08-10
Stability: stable
Owner: workspace

## Purpose

This workspace supports a two-stage production system:

1. turn incomplete/uneven project direction into documentation that developers, level designers, and the wider production team can actually use;
2. derive production-ready voice scripts from accepted project/gameplay/story documentation for ElevenLabs.

## Project Document Generator

Current owner: `kits/project-document-generator/`.

```text
incomplete project source
→ preserve/inventory source
→ recover traceable requirements
→ ready_for_prd
→ canonical content.md
→ render-data.json projection
→ approved-template final.html
→ mechanical + 4-perspective acceptance
→ development_ready
→ concise team-handoff.md
→ handoff_ready
```

Flow 4 separates generated output from production usability. Mechanical checks prove structure; New Reader, Level Designer, Developer, and Project Consistency audits prove whether the documentation can be used without inventing product rules.

## Voice Production Kit

Current owner: `kits/voice-production-kit/`.

Flow 5 now owns the boundary between accepted PRD and script production:

```text
handoff_ready PRD
→ inspect accepted player-facing narrative/communication needs
→ extract justified voice moments
→ deduplicate / reject unsupported moments
→ work/voice-requirements.md
→ state/voice-state.yaml = voice_requirements_ready
→ Flow 6 script production
```

Flow 5 does not write spoken text. Flow 6 owns final wording, performance notation, duration, and `Voice Production.docx`.

## Stable Terms

**Project Source** — original user/client/project material.

**Requirement Register** — normalized traceable project requirements/gaps/decisions from Flow 2.

**Canonical PRD Content** — `work/content.md`; authoritative PRD meaning for Flow 3/4.

**Render Projection** — `work/render-data.json`; derived data only for deterministic rendering.

**Rendered PRD** — `output/final.html`; presentation artifact, not automatically accepted.

**PRD Acceptance** — `work/acceptance.md`; concise evidence/findings from mechanical + four-perspective Flow 4 review.

**Handoff State** — `state/handoff-state.yaml`; revision-specific PRD readiness state.

**Team Handoff** — `output/team-handoff.md`; concise navigation aid pointing production roles to the accepted PRD.

**Voice Requirement** — a justified player-facing communication moment derived from an accepted PRD revision. It defines speaker/channel/trigger/purpose/required facts, not final spoken wording.

**Voice Requirements** — `work/voice-requirements.md`; canonical Flow 5 source of truth for which voice moments exist and what each must communicate.

**Voice State** — `state/voice-state.yaml`; Flow 5 status, accepted upstream revision, and next step.

**Performance Script** — ElevenLabs-ready spoken text produced in Flow 6 with controlled direction, emphasis, pauses, pacing, and duration.

**Golden Sample / Approved Reference** — structure/presentation/quality evidence only where explicitly defined; never automatic project facts or quotas.

## Archived Package

`Production Document Builder/` is Archived. It may provide migration evidence, but it does not override current root/foundation/kit owners and must not be extended by default.

## Stable Structure

- `docs/foundation/` — durable production policy.
- `docs/knowledge/` — continuity, decisions, ownership, backlog.
- `kits/project-document-generator/` — active PRD Flow 2–4 implementation.
- `kits/voice-production-kit/` — active Flow 5 voice-requirement owner; Flow 6 follows next.
- `workspace/active/` — active project packages.
- `workspace/saved/` — intentionally retained project packages.
- `Production Document Builder/` — Archived historical reference.

## Architecture Principle

```text
Source ≠ Interpretation ≠ Decision ≠ Requirement State ≠ Canonical PRD ≠ Rendered Output ≠ PRD Acceptance ≠ Voice Requirements ≠ Performance Script ≠ Delivery
```

A voice requirement may be valid without final wording. A final script must not introduce a new voice moment or project fact that Flow 5 did not justify.

## Current Development State

Flows 1–5 are implemented on permanent branch `Local`. Flow 6 — ElevenLabs Performance Script Production — is the next active boundary.
