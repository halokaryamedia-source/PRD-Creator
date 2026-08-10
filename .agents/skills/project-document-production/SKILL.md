---
name: project-document-production
description: Semantic specialist for PRD-Creator Flow 2–4. Use when the active boundary is source intake/recovery, canonical PRD generation, approved-template rendering, PRD validation, or team handoff, including maintenance of the renderer/validator when those surfaces are the root owner. Preserve source authority and project meaning; never use rendering or polished prose to invent unresolved design. Do not use for Voice-only work.
---

# Project Document Production

Own the semantic procedure around Project Document Generator Flow 2–4. Detailed production contracts remain in `kits/project-document-generator/`; this skill selects and protects the correct owner instead of duplicating every kit rule.

## Trigger

Use when the actual boundary is one of:

- incomplete/uneven source → recovered requirements;
- requirement/provenance/conflict handling;
- `ready_for_prd` → canonical `work/content.md`;
- canonical PRD → derived render projection / `final.html`;
- PRD role/readiness validation;
- team handoff;
- renderer/validator maintenance where the defect belongs to Flow 2–4.

Do not select merely because a task mentions HTML, Markdown, JSON, or a document. Select because the semantic owner is Project Document production.

## Required Routing

1. Read the relevant Flow state/project package first.
2. Identify the active Flow owner:
   - Flow 2 → `SOURCE-INTAKE.md` + source/requirement state;
   - Flow 3 → `CONTENT-CONTRACT.md`, `RENDERING.md`, canonical content + renderer;
   - Flow 4 → `VALIDATION.md`, acceptance/handoff state.
3. Read only the smallest relevant kit procedure/source.
4. Preserve the authority chain; never repair an upstream definition problem in a downstream rendering/validation layer.

## Authority Guard

```text
originals + approved decisions
→ requirement state
→ canonical content.md
→ render-data.json (derived)
→ final.html (derived)
→ acceptance/handoff evidence
```

Rules:

- generated HTML never becomes canonical project meaning;
- a sample/Golden proves presentation/quality only where explicitly defined;
- renderer behavior must not invent mechanics, scoring, quantities, lore, triggers, or architecture;
- unresolved material conflicts/critical gaps route back to Flow 2;
- `handoff_ready` is revision-specific and cannot be inferred from successful rendering alone.

## Flow 2 Judgment

- inspect all relevant sources before questioning the user;
- preserve source roles/status/provenance;
- distinguish supported, conflicting, and missing evidence;
- use Clarification/Completion only for low-risk supported recovery;
- Proposal/Blocked material decisions require resolution rather than polished guessing;
- do not ask again for information already recoverable from current sources/state.

## Flow 3 Judgment

- `work/content.md` is the human-readable source of truth;
- `work/render-data.json` is a derived projection only;
- preserve Gameplay Overview / Level Design / Developer separation;
- scoring and completion-data semantics must remain implementation-ready;
- critical information must be explicit before final rendering;
- preserve the approved HTML shell instead of redesigning it opportunistically.

## Flow 4 Judgment

Audit from the perspectives that determine production usefulness:

- New Reader / Player context;
- Level Designer;
- Developer;
- Project Consistency;
- rendered-artifact integrity at the level actually proven.

Critical/Major findings block development readiness. Minor/Suggestion findings may remain only when they do not change material meaning or prevent the downstream role from working reliably.

## Maintenance Rule

For a renderer/validator/document artifact defect:

```text
observe concrete defect
→ determine whether cause is content, projection, renderer, validator, or template
→ fix the smallest owning layer
→ regenerate derived output when needed
→ run the cheapest proof that can falsify the fix
```

Do not patch `final.html` directly when the canonical content/projection/renderer is wrong.

## Acceptance Gate

Before completion verify the relevant original development-brief criteria, including as applicable:

- project facts trace to authority;
- no unresolved material gap was hidden;
- canonical content and derived artifact do not materially disagree;
- role-specific output is usable;
- structural/visual/runtime claims do not exceed actual evidence.

## Handoff Boundary

Once `handoff_ready` is valid, Voice may consume the accepted PRD. This specialist must not pre-write Voice Production or use downstream Voice artifacts as authority for missing upstream design.
