---
name: project-document-generator
description: Recover incomplete project requirements, create canonical development-oriented PRD content, render it through the approved Golden Sample hierarchy and page composition, and validate whether the result is development-ready without inventing product decisions.
version: 1.5.0
---

# Project Document Generator

## Purpose

Use this skill for normal PRD **Production Execution** and PRD revisions. It owns project production through Flow 4 and does not require `development-brief` unless the user is changing how PRD-Creator itself works.

Normal user experience:

```text
source / approved change
→ understand automatically
→ one grouped decision review only if needed
→ build Golden-Sample PRD
→ review/fix
→ final PRD
```

## User burden rule

The user supplies project source, direction, and only decisions they must make. The agent owns project slug/workspace setup, source/requirement IDs, internal state, render data, commands, validation evidence, and normal repository mechanics.

Do not ask the user for internal project-package details unless ambiguity would put work in the wrong project or a material product decision cannot be recovered safely.

## Automatic project bootstrap

For a new PRD project:

1. derive the project name from explicit user wording or strongest authoritative source title;
2. derive a stable lowercase kebab-case slug;
3. reuse a clearly matching active project;
4. create only the minimum current-Flow package;
5. preserve supplied originals and assign internal IDs automatically.

## Three-step production flow

### 1. UNDERSTAND — Flow 2

Read `SOURCE-INTAKE.md` plus only current project sources/state needed.

- inspect all available source before asking questions;
- recover production-relevant requirements/constraints/decisions;
- apply supported Clarification/Completion automatically;
- batch remaining Proposal/Blocked decisions;
- when a decision is needed, give `Recommended / Reason / Impact` so the user can approve all or override named exceptions.

Exit truthfully as `ready_for_prd`, `needs_decision`, or `blocked`.

### 2. BUILD PRD — Flow 3

Read `CONTENT-CONTRACT.md` and create/update canonical `work/content.md`.

The Golden Sample is not only the outer HTML shell. It is the **output composition authority**.

Preserve:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

And preserve the reusable Golden page language inside those sections:

```text
Gameplay Flow
→ narrative sequence / transition treatment

Global Development
→ shared tabs
→ context
→ flow cards
→ grouped production table
→ note cards

Gameplay Overview
→ title/subtitle + 1/2/3 tabs
→ Gameplay Context / Main Objective / Result
→ Gameplay Information table
→ role-sequence

Level Design
→ title/subtitle + tabs
→ context
→ Design Flow cards
→ Golden 5-column Build Requirements table
→ note cards

Developer
→ title/subtitle + tabs
→ context
→ Development Flow cards
→ grouped Golden Development Requirements table
   with scoring/completion/reset integrated in hierarchy
→ note cards
```

**Do not treat use of the Golden CSS/JS shell as sufficient fidelity.** A generic card/table body inside that shell is a failed Golden projection for this document family.

Use minimum sufficient project detail inside the fixed composition. Optional component content may be omitted when no meaningful project fact exists; do not invent filler to make a page visually full.

Internal BUILD path:

```text
content.md
→ derive Golden-oriented render-data.json
→ renderer/pages.py composes Golden components
→ approved Golden Sample template
→ final.html
```

Read `RENDERING.md` when projection/rendering behavior matters.

### 3. REVIEW — Flow 4

Read `VALIDATION.md`.

Run one current-revision review:

```text
mechanical validation
+ Golden composition marker check
+ visual sanity when actual inspection is available
+ integrated New Reader / Level Designer / Developer / Consistency review
→ fix real findings
→ re-review only invalidated scope
```

Mechanical markers prevent regression to generic renderer output; they do not prove visual quality. Do not create pixel diff, screenshot baselines, visual scores, AI-quality detectors, or extra review phases.

## Golden fidelity rule

When a generated document feels materially different from the Golden Sample, diagnose in this order:

```text
project meaning correct?
↓
canonical content represents Golden page needs?
↓
render-data preserves that representation?
↓
renderer emits Golden component composition?
↓
actual rendered page visually behaves correctly?
```

Fix the **first wrong owner**. Never compensate for a simplified renderer by padding canonical prose, and never patch `final.html` directly.

Golden fidelity does not mean copying AFTERSHOCK-specific names, objective count, mechanics, lore, dimensions, scores, or runtime rules. It means reproducing the approved document structure, component composition, information hierarchy, visual density, and role readability with the new project's facts.

## Grouped decision interaction

When Flow 2 needs decisions, present one compact batch where possible:

```text
Decision 1 — <topic>
Recommended: <option>
Reason: <short evidence-based reason>
Impact: <what changes>
```

The user may approve all recommendations in one response or override only named items. A recommendation remains pending until explicitly approved.

## Revision fast path

For an approved bounded change:

```text
approved change
→ affected requirement/content only
→ necessary cross-references
→ regenerate Golden projection / HTML
→ one current mechanical check
→ targeted semantic/visual re-review only where invalidated
→ updated final PRD
```

Do not re-inventory unchanged sources, re-ask resolved decisions, rewrite unrelated packages, or replay full review unless the change invalidates them.

## Repository-backed project files

Internal artifacts, not user chores:

- `state/source-inventory.yaml`
- `state/requirement-register.yaml`
- `state/intake-state.yaml`
- `work/review.md` only when useful
- `work/content.md` — canonical meaning
- `work/render-data.json` — derived Golden projection
- `output/final.html` — rendered PRD
- `work/acceptance.md`
- `state/handoff-state.yaml`
- `output/team-handoff.md` under the current repository handoff boundary

Do not create release reports, checksums, packaging manifests, Content Freeze layers, new template profiles, or duplicate summaries without a real requirement.

## Default user-facing delivery

After normal production/revision show only what helps the user continue:

```text
Final PRD: <final.html>

Main adjustments / recovered decisions:
- material items only

Needs attention:
- none
```

Do not dump internal YAML, requirement IDs, render data, validator JSON, CI logs, or acceptance tables unless requested or needed to explain a blocker.

## Completion condition

Stop normal PRD production when:

- source/approved decisions support canonical meaning;
- canonical content satisfies the Golden hierarchy **and page-composition contract**;
- current HTML is generated through the approved Golden Sample;
- mechanical + Golden composition checks pass;
- New Reader, Level Designer, Developer, and Project Consistency pass with Critical=0/Major=0;
- visual claims do not exceed actual inspection evidence;
- no unresolved Proposal/Blocked item affects delivered scope;
- user receives the current final PRD plus concise continuation information.

Do not claim client approval, implementation completion, QA completion, release approval, or Voice Production readiness from this status.
