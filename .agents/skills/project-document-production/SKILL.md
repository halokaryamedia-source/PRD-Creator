---
name: project-document-production
description: Semantic/product-contract specialist for PRD-Creator Flow 2–4. Use when the active boundary is source intake/recovery, canonical PRD meaning, render-projection meaning, approved-template product contract, PRD validation/readiness, or team handoff. Do not select merely because renderer/template/validator mechanics fail when semantics are already correct; pure technical Maintenance may route directly to the nearest kit implementation owner. Preserve source authority and project meaning; never use rendering or polished prose to invent unresolved design. Do not use for Voice-only work.
---

# Project Document Production

Own semantic/product-contract judgment around Project Document Generator Flow 2–4. Detailed production and executable mechanics remain in `kits/project-document-generator/`; this skill protects the authority, representation, writing quality, and acceptance contract instead of becoming a generic Python/HTML/tooling owner.

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

### PRD prose quality

Apply the writing-quality contract in `CONTENT-CONTRACT.md` to explanatory prose. The goal is not to make technical writing decorative or "more human" at the expense of precision; it is to remove formulaic AI-style filler while keeping the PRD easy to read.

Use these rules:

- prefer plain technical sentences over inflated wording;
- state the concrete mechanic, condition, action, or consequence instead of telling the reader that something is important, immersive, seamless, dynamic, or engaging;
- remove fake analysis, promotional wording, throat-clearing, and filler that does not change meaning;
- keep stable project terminology stable; do not rotate synonyms merely for style;
- do not force ideas into artificial groups of three or repeated sentence patterns;
- make the minimum effective edit and leave already-clear sentences alone;
- never rewrite IDs, official names, numbers, coordinates, timings, formulas, weights, triggers, conditions, state names, code/API names, or approved terminology for stylistic reasons;
- apply this most strongly to Overview, Gameplay explanation, narrative/context, Level Design explanation, Developer explanation, and notes; do not aggressively "humanize" tables, formulas, requirement lists, configuration values, or code.

Example:

```text
Avoid:
This mechanic plays a crucial role in creating an engaging and immersive gameplay experience.

Prefer:
When the timer ends, the bridge collapses. The player must cross before that happens.
```

Writing quality is subordinate to source fidelity and implementation clarity. If a smoother sentence changes product meaning, keep the precise sentence.

## Flow 4 Judgment

Audit from the perspectives that determine production usefulness:

- New Reader / Player context;
- Level Designer;
- Developer;
- Project Consistency;
- rendered-artifact integrity at the level actually proven.

While performing those existing reviews, also flag explanatory prose that is vague, inflated, repetitive, or formulaically AI-sounding when it makes the PRD harder to use. Do not create a separate AI score or writing gate.

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
- explanatory prose is plain, concrete, and free of unnecessary AI-style filler without altering technical meaning;
- structural/visual/runtime claims do not exceed actual evidence.

## Handoff Boundary

Once `handoff_ready` is valid, Voice may consume the accepted PRD. This specialist must not pre-write Voice Production or use downstream Voice artifacts as authority for missing upstream design.
