# Workspace Context

Last verified: 2026-08-10
Stability: stable
Owner: workspace

## Purpose

This workspace supports a two-stage production system:

1. turn incomplete/uneven project direction into documentation that developers, level designers, and the wider production team can actually use;
2. derive production-ready voice scripts from sufficiently mature project/gameplay/story documentation for ElevenLabs.

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

Flow 4 deliberately separates generated output from production usability. Mechanical checks prove structure; New Reader, Level Designer, Developer, and Project Consistency audits prove whether the documentation is safe enough to start work without inventing product rules.

## Voice Production

Voice Production remains downstream:

```text
accepted mature project/gameplay/story documentation
→ justified voice moments
→ Main Story / Radio Communication
→ ElevenLabs-ready performance text
→ voice production delivery
```

It must not repair missing PRD decisions inside a voice script.

## Stable Terms

**Project Source** — original user/client/project material.

**Requirement Register** — normalized traceable project requirements/gaps/decisions from Flow 2.

**Canonical PRD Content** — `work/content.md`; authoritative PRD meaning for Flow 3/4.

**Render Projection** — `work/render-data.json`; derived data only for deterministic rendering.

**Rendered PRD** — `output/final.html`; presentation artifact, not automatically accepted.

**PRD Acceptance** — `work/acceptance.md`; concise evidence/findings from mechanical + four-perspective Flow 4 review.

**Handoff State** — `state/handoff-state.yaml`; revision-specific readiness status (`pending_review`, `needs_revision`, `development_ready`, `handoff_ready`, or `blocked`).

**Team Handoff** — `output/team-handoff.md`; concise navigation aid pointing the production team to the accepted PRD. It is not a second PRD.

**Golden Sample / Approved Reference** — structure/presentation/quality evidence only where explicitly defined; never automatic project facts.

**Voice Requirement** — a voice moment justified by accepted upstream documentation.

**Performance Script** — ElevenLabs-ready text with controlled direction, emphasis, pauses, and pacing.

## Archived Package

`Production Document Builder/` is Archived. It may provide migration evidence, but it does not override current root/foundation/kit owners and must not be extended by default.

## Stable Structure

- `docs/foundation/` — durable production policy.
- `docs/knowledge/` — continuity, decisions, ownership, backlog.
- `kits/project-document-generator/` — active PRD Flow 2–4 implementation.
- `workspace/active/` — active project packages.
- `workspace/saved/` — intentionally retained project packages.
- `Production Document Builder/` — Archived historical reference.

## Architecture Principle

```text
Source ≠ Interpretation ≠ Decision ≠ Requirement State ≠ Canonical Content ≠ Rendered Output ≠ Acceptance
```

`handoff_ready` does not mean client sign-off, implementation completion, QA completion, or release approval.

## Current Development State

Flows 1–4 are implemented on permanent branch `Local`. Flow 5 — Voice Requirement Extraction — is the next active boundary.
