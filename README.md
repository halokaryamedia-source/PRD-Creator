# PRD-Creator

PRD-Creator turns incomplete or uneven project material into a development-ready PRD, then optionally derives downstream Voice Production from the accepted PRD without reopening or rewriting project meaning.

## Current baseline

Working authority: **`Local`**. `main` remains stable unless promotion is explicitly requested.

Current production versions:

```text
Project Document Generator  v1.13.0
Voice Production Kit        v1.11.2
Voice model scope           Eleven v3 only
```

The current Clockwork reference project is complete for the requested **non-audio Voice Production** scope. Its canonical Voice requirements, production script, consolidated project HTML, acceptance state, and delivery state are stored under `workspace/active/the-clockwork-vault/`. Actual generated-audio review is intentionally outside that completed baseline.

## What the repository produces

The normal human-facing project output is one document:

```text
output/final.html
```

Without downstream assets it contains the accepted PRD core. When Voice Production exists, the same file is rerendered as:

```text
PRD core
+
04 Production Assets
   VOICE
   <gameplay section title>
   <accepted PRD package label>
```

Production Assets is additive. It does not rebuild PRD navigation, move gameplay/objective sections out of Development, or renumber accepted PRD page identities.

`Voice Production.docx` is an **optional derived export**, not the default Voice delivery surface.

## Production flow

```text
Flow 1  Repository Boot & Project Memory
Flow 2  Source Intake, Golden-Guided Completion & Preview
Flow 3  Project Document / PRD Generation
Flow 4  PRD Validation & Team Handoff
Flow 5  Voice Requirement Extraction
Flow 6  ElevenLabs Performance Script Production
Flow 7  Voice Validation & Delivery
```

Normal project work is **Production Execution**. `development-brief` is used only when changing PRD-Creator itself: policy, workflow, renderer, validator, builder, skills, repository structure, or shared tooling.

## PRD production path

```text
project source / current user instruction
→ authority + relevance recovery
→ requirement completion / problem solving
→ Golden fill-map completeness pass
→ concrete AI Proposal only where material meaning is genuinely missing/conflicting
→ complete Simple Chat Preview
→ user correction / approval
→ canonical work/content.md
→ direct work/render-data.json projection
→ deterministic approved-Golden render
→ mechanical + semantic validation
→ targeted visual sanity
→ PRD handoff
```

A Proposal is not project authority until the relevant preview is approved or corrected. Generated HTML never becomes source truth.

## Accepted PRD hierarchy

The approved Golden Sample defines the PRD-core visible composition:

```text
01 Overview

02 Gameplay Flow
   The Journey Begins
   one Gameplay Flow page per gameplay section

03 Development
   Development Overview
   Game System
   Data and Reset
   Gameplay Development
   gameplay/objective sections
      Gameplay Overview
      Level Design
      Developer
```

For `N` gameplay sections, the PRD core remains `6 + 4N` pages.

Gameplay/objective sections remain part of **Development**. A downstream `04 Production Assets` group may be appended to the sidebar, but it is not a new PRD-core semantic family.

The approved Golden/reference bytes live at:

```text
kits/project-document-generator/template/golden-reference.html
kits/project-document-generator/template/runtime-template.html
```

The two files remain byte-identical. Production Assets is composed after the base PRD render and does not modify the Golden template bytes.

## Voice production path

Voice Production starts from an already accepted PRD:

```text
accepted PRD
→ work/voice-requirements.md
→ work/voice-production.md
→ rerender same output/final.html
   → Production Assets → Voice
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

Current Voice presentation contract:

```text
04 Production Assets
   VOICE
   The Antechamber
      Introduction
   The Resonance Engine
      Objective 1
   ...
```

`VOICE` appears once. Each navigation entry shows the gameplay section title plus the accepted PRD package label so a developer can immediately see which Introduction / Objective / Ending the asset belongs to. Long labels wrap naturally rather than being intentionally truncated.

Each Voice section presents:

```text
Voice Production
→ gameplay section title
→ accepted PRD package label + gameplay context
→ Voice line count + Primary Speaker
→ compact Voice Setup
```

Each Voice line presents:

```text
title
→ <PRD package label> · Voice Line X/Y
→ Context = exact Flow 5 Trigger
→ Speaker · Estimated Duration
→ exact Eleven v3 production prompt
→ Copy Prompt
```

Voice requirements own scope and communication intent. Canonical `voice-production.md` owns final performance wording and selected actor voice when known. `final.html` is derived presentation only.

## Quality and ownership rules

- source fidelity before polish;
- solve from existing authority before asking the user to reconstruct known context;
- use the Golden fill map as a completeness guide, never as a source of another project's facts;
- one approved semantic model feeds canonical PRD meaning and render projection;
- derived HTML/DOCX is regenerated from canonical owners and is never hand-patched as authority;
- visual PASS requires actual rendered/browser evidence;
- generated-audio quality requires actual heard evidence;
- bounded revisions touch only invalidated scope;
- do not introduce a generic Asset framework, extra Flow, duplicate owner, new skill, or parallel artifact without a concrete production need.

## Repository ownership

Root semantic skills:

```text
.agents/skills/development-brief/
.agents/skills/project-document-production/
.agents/skills/voice-production/
```

Production kits:

```text
kits/project-document-generator/
kits/voice-production-kit/
```

Primary navigation:

```text
docs/knowledge/README.md             repository dashboard
docs/knowledge/ownership.md          exact owner lookup
docs/knowledge/source-authority.md   authority lookup
docs/knowledge/next-action.md        current continuation / stop state
workspace/README.md                  project package contract
```

Historical audits and changelog entries preserve capture-time history; current behavior is defined by the active owners above, not by rewriting old evidence.

## Current stop state

The current v1.13.0 PRD + v1.11.2 non-audio Voice baseline is complete. There is no standing cleanup/hardening backlog. New work should begin only from a real new project, an explicit product/system change, a concrete observed defect, or an explicitly requested next Voice/audio stage.
