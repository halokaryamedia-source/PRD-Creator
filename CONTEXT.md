# Workspace Context

Last verified: 2026-08-10
Stability: stable
Owner: workspace

## Purpose

This workspace supports a two-stage production system:

1. turn incomplete or uneven project direction into documentation that developers, level designers, and the wider production team can use to begin work;
2. derive production-ready voice scripts from sufficiently mature project/gameplay/story documentation for use with ElevenLabs.

## Branch Authority

`Local` is the permanent development authority. Normal work continues directly on `Local`; `main` is a stable baseline and is not a routine merge target. Do not create per-flow branches or PRs unless the user explicitly changes this rule.

## Stable Product Boundaries

### Project Document Generator

Current repository owner: `kits/project-document-generator/`.

Primary responsibility:

```text
incomplete project source
→ preserve source/provenance
→ understand intent and structure
→ recover supported missing information
→ isolate true decisions that require approval
→ create development-ready canonical documentation
→ render through the approved HTML presentation
```

It is not merely an HTML formatter.

Flow 2 adds persistent source inventory, requirement recovery, conflict visibility, and resumable intake state. Flow 3 will own canonical PRD generation/redesign alignment.

### Voice Production Kit

Primary responsibility:

```text
mature project/gameplay/story documentation
→ identify voice moments
→ write Main Story and Radio Communication where appropriate
→ produce ElevenLabs-ready performance text
→ deliver Voice Production.docx
```

It must preserve official names, sequence, and supported project facts. It must not invent missing gameplay/story decisions that belong upstream in the project documentation stage.

The supplied Voice Production Kit has been reviewed but is not yet migrated into repository implementation; its owning flow is downstream.

## Archived Repository Package

`Production Document Builder/` predates this workspace architecture and is now **Archived**. It contains a broader historical document-production implementation, tests, schemas, and the same approved Aftershock Golden Sample file used by the current Project Document Generator baseline.

Archived means:

- preserved for migration evidence;
- not current workflow authority;
- do not extend it by default;
- do not delete it until its useful behavior/dependencies have been evaluated and migrated or intentionally retired.

## Stable Terms

**Project Source**  
Original user/client/project material used to understand the project. Originals are preserved and inventoried before being used as authority.

**Source Inventory**  
Persistent source list containing provenance, role, and current/superseded/unavailable state.

**Requirement Register**  
Persistent traceable set of recovered project facts, requirements, gaps, conflicts, and approval state.

**Intake State**  
Single resumable source-intake status and next step for one active project.

**Approved Decision**  
A project-specific material decision explicitly approved by the user/creative owner.

**Canonical Project Content**  
The approved content used as the source for final project documentation/rendering.

**Approved Template**  
The fixed HTML presentation currently owned by the Project Document Generator.

**Golden Sample / Approved Reference**  
A demonstrated structure, presentation, tone, or quality reference. It does not automatically define project-specific requirements.

**Voice Requirement**  
A voice moment justified by the mature project documentation, such as briefing, story progression, warning, progress update, urgency, encouragement, ending, or reward communication.

**Performance Script**  
Text prepared for ElevenLabs with controlled voice direction, emphasis, pauses, and line breaks.

## Stable Structure

- `kits/project-document-generator/` — active upstream kit.
- `docs/foundation/` — durable production policy.
- `docs/knowledge/` — project continuity and ownership.
- `workspace/active/` — active project packages.
- `workspace/saved/` — intentionally retained completed/saved packages.
- `Production Document Builder/` — Archived migration/reference package.

## Current Architecture Principle

```text
Source ≠ Interpretation ≠ Decision ≠ Output ≠ Approval
```

A polished document is not evidence that its unresolved decisions were approved. A generated voice script is not evidence that upstream project facts were complete.
