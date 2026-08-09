# Workspace Context

Last verified: 2026-08-10
Stability: stable
Owner: workspace

## Purpose

This workspace supports a two-stage production system:

1. turn incomplete or uneven project direction into documentation that developers, level designers, and the wider production team can use to begin work;
2. derive production-ready voice scripts from sufficiently mature project/gameplay/story documentation for ElevenLabs.

## Stable Product Boundaries

### Project Document Generator

Primary responsibility:

```text
incomplete project source
→ preserve/inventory source
→ recover traceable requirements
→ resolve supported gaps / isolate real decisions
→ ready_for_prd
→ canonical human-readable PRD content
→ approved-template HTML render
```

The active implementation is `kits/project-document-generator/` (v1.1.0 after Flow 3).

It is not merely an HTML formatter. It owns requirement recovery and PRD generation, but it does not decide downstream team-handoff readiness or voice production.

### PRD Validation & Team Handoff

Flow 4 is a separate downstream acceptance boundary. A generated `final.html` is not automatically development-ready just because rendering succeeded.

### Voice Production

Primary responsibility remains:

```text
mature approved project/gameplay/story documentation
→ identify justified voice moments
→ Main Story / Radio Communication
→ ElevenLabs-ready performance text
→ voice production delivery
```

Voice Production must preserve official names/sequence/supported facts and must not invent missing gameplay/story decisions that belong upstream.

## Pre-existing Repository Package

`Production Document Builder/` predates the current architecture and is **Archived**. It contains a broader historical implementation, tests, schemas, renderer, and Aftershock Golden Sample. Current flows may inspect it as evidence and migrate bounded useful behavior, but it does not override active kit/foundation owners and must not be extended by default.

## Stable Terms

**Project Source**  
Original user/client/project material used to understand the project.

**Source Inventory**  
Persistent record of project sources, provenance, role, and authority/supersession state.

**Requirement Register**  
Normalized traceable project requirements, recovered gaps, conflicts, and decisions from Flow 2.

**Approved Decision**  
A material project-specific decision explicitly approved by the user/creative owner.

**Canonical PRD Content**  
`work/content.md`: the human-readable Flow 3 source of truth for project-document meaning.

**Render Projection**  
`work/render-data.json`: derived structured page/component data used only for deterministic HTML rendering. It must not introduce new meaning.

**Approved Template**  
`kits/project-document-generator/template/approved-document.html`: fixed shared HTML presentation shell.

**Golden Sample / Approved Reference**  
A demonstrated structure, presentation, tone, or quality reference. It does not automatically define project-specific requirements.

**Rendered PRD**  
`output/final.html`: presentation artifact generated from canonical PRD content through the approved shell. Rendering success is not the same as development-ready acceptance.

**Voice Requirement**  
A voice moment justified by mature upstream documentation, such as briefing, story progression, warning, progress update, urgency, encouragement, ending, or reward communication.

**Performance Script**  
Text prepared for ElevenLabs with controlled voice direction, emphasis, pauses, and line breaks.

## Stable Structure

- `docs/foundation/` — durable production policy.
- `docs/knowledge/` — project continuity, decisions, ownership, and backlog.
- `kits/project-document-generator/` — active PRD intake/generation implementation.
- `workspace/active/` — active project packages.
- `workspace/saved/` — intentionally retained completed/saved packages.
- `Production Document Builder/` — Archived historical reference.

## Architecture Principle

```text
Source ≠ Interpretation ≠ Decision ≠ Requirement State ≠ Canonical Content ≠ Rendered Output ≠ Approval
```

A polished document is not evidence that unresolved decisions were approved. A structurally valid HTML render is not evidence that the PRD is development-ready. A generated voice script is not evidence that upstream facts were complete.

## Current Development State

Flows 1–3 are implemented on permanent branch `Local`. Flow 4 — PRD Validation & Team Handoff — is the next active boundary. Voice Production remains deliberately downstream and unmigrated until Flow 5/6.
