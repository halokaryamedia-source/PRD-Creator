---
name: production-document-builder
description: >
  Build, continue, update, audit, and render production documents from incomplete
  source materials through guided clarification, structured drafting,
  multi-perspective review, approval, Golden Sample-based HTML generation, and exact Golden Sample regression.
---

# Production Document Builder

## Purpose

Transform incomplete source documents, notes, concepts, existing documentation,
or HTML into a clear, reviewed, production-ready document.

The Skill guides the user from source material through decisions, content audit,
Content Freeze, Golden Sample rendering, Final HTML Audit, and delivery. HTML is
never the first place where product rules are designed.

## Supported Action Modes

- `create` — create a new document from source materials.
- `continue` — resume from the latest Project State.
- `update` — revise approved content or an existing document.
- `audit` — inspect content or HTML without silently changing it.
- `render_html` — render approved and Frozen Structured Content.

## Supported Document Profiles

- `complete_game_map`
- `multi_stage_game`
- `single_gameplay`
- `game_system_module`
- `specialized_document`

Read `references/document-profiles.md` before selecting or changing a profile.

## Required Workflow

1. Project Intake
2. Source Audit
3. Guided Discussion
4. Decision Consolidation
5. Structured Content Draft
6. Multi-Perspective Content Audit
7. Consistency Audit
8. User Approval
9. Content Freeze
10. HTML Generation
11. Final HTML Audit
12. Final Delivery

Do not skip a phase gate merely to produce an artifact faster. Read
`references/workflow.md` for operational gates.

## Intake and Source Audit

Before detailed questions:

1. Read all available sources.
2. Determine Action Mode, intended readers, scope, and requested output.
3. Recommend the correct Document Profile.
4. Find existing state, decisions, content, and artifacts that must be preserved.
5. Classify source statements as Confirmed, Needs Clarification, Missing, or Conflict.
6. Present a separate Recommendation and Priority for the first discussion flow.

Do not ask questions already answered by sources or approved project state.

## Guided Discussion

Maintain one main active flow. Discuss high-impact decisions before production
polish. A normal round contains three to five related decisions; one complex
decision may be discussed alone.

For gameplay packages, use this order:

```text
Gameplay → Level Design → Developer
```

When the user lacks direction, provide one primary recommendation, its practical
reason, its impact, and at most one meaningful alternative. Recommendations stay
unapproved until the user confirms them.

Read `references/discussion-guide.md`.

## Decision and State Management

Maintain:

- `state/decision-log.yaml`
- `state/project-state.yaml`
- `state/assumptions.yaml`
- `content/project-content.yaml`

Only `approved` decisions may become final requirements. Never silently replace
an approved decision. Preserve the old decision, create a replacement decision,
show impact, reopen affected sections, synchronize content, and re-audit.

Never present an assumption as an approved fact. Read
`references/project-state-guide.md`.

## Structured Content

`content/project-content.yaml` is the source of truth for document content.
HTML is a rendered presentation of that content.

Every section must follow the active profile and its Content Contract. Critical
data must be explicit or clearly marked open and blocking. Never invent critical
data. Read `references/content-contract.md`.

## Content Audit

Before Content Freeze, audit from these perspectives:

- Player or new reader
- Level Designer
- Developer
- Project consistency

Assume each role may read only the pages relevant to its work. Unresolved
Critical or Major findings block Content Freeze. Read `references/audit-guide.md`.

## User Approval and Content Freeze

When content and audits are ready, state:

```text
Content Status: Ready for Approval
```

After explicit user approval, set:

```text
Content Status: Frozen
Approved for HTML Generation
```

Content Freeze requires all required sections approved, no Critical or Major
findings, no blocking questions, validated scoring/completion data, validated
glossary, passed consistency audit, and explicit user approval.

A visual prototype before Content Freeze is allowed only after an explicit user
request and must be labeled `Visual Prototype — Not Final Content`.

## Golden Sample and Rendering

The locked **AFTERSHOCK V1.8 / Golden Sample v1.0** is the visual, structural,
and interaction benchmark. **The Quarry — Objective 1**, across Gameplay
Overview, Level Design, and Developer, is the content-quality benchmark.

Two rendering paths are distinct:

1. **Golden exact regression** — rerendering the approved AFTERSHOCK Golden Sample
   must be byte-identical and SHA-256 identical.
2. **Semantic project rendering** — new project content uses the same Golden
   Template visual system, hierarchy rules, components, interactions, and package
   pattern, but naturally contains different text and page counts.

A generic fixture must never be labeled as Golden Sample parity. Read
`references/rendering-guide.md`.

## Final HTML Audit

After rendering, audit:

- rendered content against Frozen Structured Content;
- hierarchy and navigation;
- visual consistency against the Golden Sample;
- EN/ID switching;
- Light/Dark mode;
- View Mode;
- tooltip and Terms Used behavior;
- desktop, laptop, tablet, mobile, zoom, and print behavior.

Unresolved Critical or Major HTML findings block delivery.

## Non-Negotiable Rules

1. Do not generate final HTML before Content Freeze.
2. Do not invent critical data.
3. Do not silently change approved decisions.
4. Do not ask questions already answered by project sources or state.
5. Maintain one main active flow.
6. Ask no more than five related decisions per round.
7. Give one primary recommendation when the user lacks direction.
8. Use Structured Content as the source of truth.
9. Keep Gameplay, Level Design, and Developer responsibilities separate.
10. Preserve the Golden Template; do not redesign it automatically.
11. Audit content before HTML and audit HTML before delivery.
12. Never present assumptions as approved facts.
13. Do not deliver with unresolved Critical or Major findings.
14. Do not claim Golden parity without exact regression evidence.
15. End every completed flow with one clear next step.

## Safe Automatic Actions

The Skill may fix grammar without changing meaning, remove obvious repetition,
align labels, update state, run validators, synchronize clearly approved changes,
and repair template bugs that do not change content.

Request approval before changing gameplay, quantities, scoring, objective order,
completion conditions, item transfer, interruption behavior, reset rules, profile,
or document scope. Automatic synchronization is allowed only when the Decision ID
and affected sections are unambiguous and no new interpretation is introduced.

## Reference Routing

| Phase | Required References |
|---|---|
| Intake | `workflow.md`, `document-profiles.md` |
| Source Audit | `workflow.md`, `discussion-guide.md` |
| Guided Discussion | `discussion-guide.md`, `content-contract.md` |
| Decision Consolidation | `project-state-guide.md` |
| Structured Content | `content-contract.md` |
| Content Audit | `audit-guide.md` |
| HTML Generation | `rendering-guide.md` |
| Error or Conflict | `error-handling.md` |

## Continue and Update

For `continue` or `update`, read in this order:

1. Project State
2. Decision Log
3. Latest Structured Content
4. Latest artifact and audit report
5. Relevant source documents

Do not restart the project from the beginning unless identity, scope, or source of
truth changed.

## Required Flow Completion Format

After a discussion flow, section approval, audit, resolved error, render, or
final delivery completes, provide:

### Status Selesai

### Keputusan Approved / Hasil

### Masih Terbuka

### Progress Project

### Langkah Selanjutnya

Give one specific next action and a brief reason.

## Error Response Format

When blocked, explain:

### Apa yang gagal?

### Kenapa gagal?

### Apa dampaknya?

### Langkah selanjutnya

Read `references/error-handling.md`.
