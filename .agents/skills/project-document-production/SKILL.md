---
name: project-document-production
description: Semantic/product-contract specialist for PRD-Creator Flow 2–4. Use when the active boundary is source intake/recovery, canonical PRD meaning, render-projection meaning, approved-template product contract, PRD validation/readiness, or team handoff. Do not select merely because renderer/template/validator mechanics fail when semantics are already correct; pure technical Maintenance may route directly to the nearest kit implementation owner. Preserve source authority and project meaning; never use rendering or polished prose to invent unresolved design. Do not use for Voice-only work.
---

# Project Document Production

Own semantic/product-contract judgment around Project Document Generator Flow 2–4. Detailed production and executable mechanics remain in `kits/project-document-generator/`; this skill protects the authority, representation, and acceptance contract instead of becoming a generic Python/HTML/tooling owner.

## Trigger

Use when the actual wrong contract is one of:

- incomplete/uneven source → recovered requirements;
- requirement/provenance/conflict handling;
- `ready_for_prd` → canonical `work/content.md`;
- what canonical PRD data/pages must represent;
- approved-template/product presentation contract;
- PRD role/readiness validation;
- team handoff semantics;
- a renderer/validator change whose required behavior changes or misrepresents the Flow 2–4 product contract.

Do **not** select merely because:

- a task mentions HTML, JSON, Markdown, Python, or a document;
- `renderer/render.py` crashes while the semantic render contract is already correct;
- `validator/validate.py` has a mechanical implementation bug;
- CI/test/dependency tooling fails.

Pure technical Maintenance may route directly through `kits/project-document-generator/AGENTS.md` to the exact implementation owner without a root specialist.

## Required Routing

1. Read the relevant Flow state/project package first.
2. Identify whether the defect is semantic/product-contract or executable mechanics.
3. For semantic/product-contract work, identify the active Flow owner:
   - Flow 2 → `SOURCE-INTAKE.md` + source/requirement state;
   - Flow 3 → `CONTENT-CONTRACT.md`, `RENDERING.md`, canonical content + affected representation contract;
   - Flow 4 → `VALIDATION.md`, acceptance/handoff state.
4. Read only the smallest relevant kit procedure/source.
5. Preserve the authority chain; never repair an upstream definition problem in downstream rendering/validation.

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
- preserve the approved HTML shell instead of redesigning it opportunistically;
- decide what the renderer must represent, but leave pure implementation mechanics to the kit-local owner when semantics are already correct.

## Flow 4 Judgment

Audit from the perspectives that determine production usefulness:

- New Reader / Player context;
- Level Designer;
- Developer;
- Project Consistency;
- rendered-artifact integrity at the level actually proven.

Critical/Major findings block development readiness. Minor/Suggestion findings may remain only when they do not change material meaning or prevent the downstream role from working reliably.

## Technical Handoff Rule

If investigation proves:

```text
canonical meaning/representation contract is correct
+ executable renderer/template/validator mechanics are wrong
```

then route Maintenance to:

`kits/project-document-generator/AGENTS.md` → exact implementation source.

Do not keep this root specialist loaded solely as a Python/HTML debugging wrapper. Shared dependency/test/CI failures belong to root repository-engineering owners (`requirements.lock.txt`, `tests/`, `tools/`, workflows).

## Maintenance Rule

For a Project Document defect:

```text
observe concrete defect
→ classify semantic/product contract vs executable mechanics
→ semantic wrong: use this specialist + smallest Flow owner
→ semantics correct, mechanics wrong: nearest kit AGENTS + exact implementation owner
→ regenerate derived output when needed
→ run the cheapest proof that can falsify the fix
```

Do not patch `final.html` directly when canonical content/projection/renderer is wrong.

## Acceptance Gate

Before completion verify the relevant original development-brief criteria, including as applicable:

- project facts trace to authority;
- no unresolved material gap was hidden;
- canonical content and derived artifact do not materially disagree;
- role-specific output is usable;
- structural/visual/runtime claims do not exceed actual evidence.

## Handoff Boundary

Once `handoff_ready` is valid, Voice may consume the accepted PRD. This specialist must not pre-write Voice Production or use downstream Voice artifacts as authority for missing upstream design.
