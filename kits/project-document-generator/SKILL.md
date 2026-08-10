---
name: project-document-generator
description: Recover incomplete project requirements, create canonical development-oriented PRD content, render it through the approved Golden Sample HTML foundation, and validate whether the result is development-ready for team handoff without inventing product decisions.
version: 1.4.0
---

# Project Document Generator

## Purpose

Use this skill for normal PRD **Production Execution** and PRD revisions. It owns project production through Flow 4 and does not require `development-brief` unless the user is changing how PRD-Creator itself works.

The normal user experience should stay close to:

```text
source / approved change
→ understand automatically
→ one grouped decision review only if needed
→ build Golden-Sample PRD
→ review/fix
→ final PRD
```

The skill owns PRD production through Flow 4. It does not own downstream Voice Requirement extraction or ElevenLabs scripting.

## User burden rule

The user supplies project source, direction, and any decisions only they can make. The agent owns the internal production work.

Do not ask the user to manage:

- project slug/folder naming;
- workspace setup;
- `SRC-###` or `REQ-###` IDs;
- source inventory or requirement-register formatting;
- `render-data.json`;
- validation state/evidence files;
- renderer commands;
- internal handoff state.

Ask only when a material product decision cannot be recovered safely from source, approved state, or an already-authorized default.

## Automatic project bootstrap

For a new PRD project, bootstrap `workspace/active/<project-slug>/` automatically.

Use this order:

1. derive the project name from the user's explicit name or strongest authoritative source title;
2. derive a stable lowercase kebab-case slug;
3. reuse an existing matching active project when it is clearly the same project;
4. create the minimum project package required by the active Flow;
5. preserve supplied originals and assign internal source/requirement IDs automatically.

Do not ask the user for a slug, folder name, source ID, requirement ID, or boilerplate project metadata unless ambiguity would cause work to be written into the wrong project.

## Three-step production flow

### 1. UNDERSTAND — Flow 2

Read `SOURCE-INTAKE.md` plus only the current project sources/state needed.

- inspect all available source before asking questions;
- recover only production-relevant requirements/constraints/decisions;
- apply supported Clarification/Completion automatically;
- batch remaining Proposal/Blocked decisions;
- when a decision is needed, give a recommended option with a short reason and impact so the user can approve all recommendations or override only exceptions.

Exit when the project is truthfully `ready_for_prd`, `needs_decision`, or `blocked`.

### 2. BUILD PRD — Flow 3

Read `CONTENT-CONTRACT.md` and create/update canonical `work/content.md`.

Preserve the approved Golden Sample structure and presentation foundation:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Use minimum sufficient detail inside that fixed structure. Keep short role pages concise instead of inventing filler.

Treat projection/rendering as internal work in the same BUILD step:

```text
content.md
→ derive render-data.json
→ render through approved Golden Sample template
→ final.html
```

Read `RENDERING.md` only when projection/rendering behavior is relevant.

### 3. REVIEW — Flow 4

Read `VALIDATION.md`.

Run one review cycle for the current revision:

```text
mechanical validation
+ visual sanity when visual inspection is available
+ integrated New Reader / Level Designer / Developer / Consistency review
→ fix only real findings
→ re-review only invalidated scope
```

Do not create a separate AI-writing, brevity, visual-score, or quality-score gate.

Set `development_ready` only when the semantic readiness contract is satisfied. Visual quality may be claimed only when the current rendered output was actually inspected at that level.

## Grouped decision interaction

When Flow 2 needs user decisions, present one compact batch where possible.

Recommended format:

```text
Decision 1 — <topic>
Recommended: <option>
Reason: <short evidence-based reason>
Impact: <what changes>

Decision 2 — <topic>
Recommended: <option>
Reason: <short evidence-based reason>
Impact: <what changes>
```

The user may respond with:

```text
Approve all recommendations.
```

or override only named items:

```text
Approve all except Decision 2: use <other option>.
```

A recommendation is not approved until the user approves it. Do not force separate approval messages for each Proposal.

## Revision fast path

For an existing project, an explicit approved user change should normally use a delta path rather than replaying full Flow 2–4.

```text
approved change
→ identify affected requirement(s)/section(s)
→ update only affected canonical content + required cross-references
→ regenerate derived render data / HTML
→ mechanical check for current output
→ re-review affected scope + dependencies only
→ updated final PRD
```

Do not re-inventory unchanged sources, re-ask resolved decisions, rewrite unrelated packages, or rerun a full semantic audit unless the change invalidates those areas.

Return to full Flow 2 only when the revision changes source authority, introduces a material conflict, changes broad project scope, or exposes an unresolved product decision outside the local delta.

## Repository-backed project files

These are internal production artifacts, not user chores.

Flow 2 state:

- `state/source-inventory.yaml`
- `state/requirement-register.yaml`
- `state/intake-state.yaml`
- `work/review.md` only when a human-facing decision/recovery summary is useful

Flow 3 work/output:

- `work/content.md` — canonical PRD meaning
- `work/render-data.json` — derived renderer projection
- `output/final.html` — rendered PRD artifact

Flow 4 acceptance/handoff:

- `work/acceptance.md` — concise integrated audit/findings
- `state/handoff-state.yaml` — current readiness status
- `output/team-handoff.md` — current repository handoff boundary/navigation aid

Do not create release reports, checksums, packaging manifests, Content Freeze layers, or duplicate PRD summaries unless a concrete requirement needs them.

## Default user-facing delivery

After normal PRD production/revision, show the user only what helps them continue:

```text
Final PRD: <final.html>

Main adjustments / recovered decisions:
- only material items worth knowing

Needs attention:
- none
```

If decisions remain, show them instead of pretending the PRD is final.

Do not dump internal YAML, requirement IDs, validator JSON, CI logs, acceptance tables, or repository-state details into the normal delivery unless the user asks or a blocker requires explanation.

## Completion condition

Stop normal PRD production when:

- current source/approved decisions support the canonical PRD;
- current Golden Sample HTML is generated;
- mechanical validation passes;
- New Reader, Level Designer, Developer, and Project Consistency lenses pass with Critical=0 and Major=0;
- visual-quality claims do not exceed actual visual evidence;
- unresolved Proposal/Blocked items do not affect the delivered scope;
- the user receives the current final PRD plus only the concise information needed to continue.

Do not claim client approval, implementation completion, QA completion, release approval, or Voice Production readiness from this status.
