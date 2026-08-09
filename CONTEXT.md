# Workspace Context

Last verified: 2026-08-10
Stability: stable
Owner: workspace

## Purpose

This workspace supports a two-stage production system:

1. turn incomplete or uneven project direction into documentation that developers, level designers, and the wider production team can use to begin work;
2. derive production-ready voice scripts from sufficiently mature project/gameplay/story documentation for use with ElevenLabs.

## Stable Product Boundaries

### Project Document Generator

Primary responsibility:

```text
incomplete project source
→ understand intent and structure
→ recover supported missing information
→ isolate true decisions that require approval
→ create development-ready canonical documentation
→ render through the approved HTML presentation
```

It is not merely an HTML formatter.

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

## Pre-existing Repository Package

`Production Document Builder/` predates this workspace architecture. It contains a broader historical document-production implementation, tests, schemas, and an Aftershock Golden Sample. During Flow 1 it is preserved unchanged as historical/reference material. It does not override the current two-kit production boundary unless a later bounded audit explicitly adopts part of it.

## Stable Terms

**Project Source**  
Original user/client/project material used to understand the project.

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

- `docs/foundation/` — durable production policy.
- `docs/knowledge/` — project continuity and ownership.
- `workspace/active/` — active project packages.
- `workspace/saved/` — intentionally retained completed/saved packages.

## Current Architecture Principle

```text
Source ≠ Interpretation ≠ Decision ≠ Output ≠ Approval
```

A polished document is not evidence that its unresolved decisions were approved. A generated voice script is not evidence that upstream project facts were complete.

## Current Development State

Repository/project-memory architecture is introduced first. The supplied Project Document Generator and Voice Production Kit define the intended production boundaries, but their implementation files are intentionally deferred to their owning flows. The pre-existing `Production Document Builder/` remains historical/reference material until a bounded audit explicitly adopts part of it.
