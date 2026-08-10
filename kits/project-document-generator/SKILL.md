---
name: project-document-generator
description: Recover incomplete project requirements, create canonical development-oriented PRD content, render it through the approved Golden Sample hierarchy/page composition, and validate whether the result is development-ready without inventing product decisions.
version: 1.5.0
---

# Project Document Generator

Use for normal PRD **Production Execution** and bounded PRD revisions. Do not route ordinary PRD creation through `development-brief`.

Normal user experience:

```text
source / approved change
→ understand automatically
→ one grouped decision review only if needed
→ build Golden PRD
→ review/fix
→ final PRD
```

## User burden

The user supplies source/direction and only decisions that genuinely require them. The agent owns project/workspace bootstrap, internal IDs/state, render projection, commands, validation evidence, and repository mechanics.

Do not ask the user to manage slugs, folders, YAML, JSON, renderer files, or validation output.

## 1. UNDERSTAND — Flow 2

Read `SOURCE-INTAKE.md` plus only relevant current source/state.

- inventory supplied/current source, then triage relevance/authority before deep reading;
- deep-read material authoritative source; targeted-read supporting/reference/generated source only to the depth needed for current scope;
- if a source could materially change the PRD and relevance is uncertain, inspect it rather than skipping it;
- recover production-relevant requirements;
- apply safe Clarification/Completion automatically;
- batch remaining material Proposal/Blocked decisions;
- when needed, use `Recommended / Reason / Impact` so the user can approve all or override named exceptions.

Do not interpret “inspect all source” as “load every byte of every source.” Completeness is about production meaning and conflict coverage.

Exit truthfully as `ready_for_prd`, `needs_decision`, or `blocked`.

## 2. BUILD PRD — Flow 3

Read `CONTENT-CONTRACT.md`. It owns Golden hierarchy, page composition, information density, role separation, language meaning, Terms Used semantics, and prose quality.

Canonical path:

```text
work/content.md
→ work/render-data.json (derived projection)
→ deterministic renderer
→ Golden Sample template
→ output/final.html
```

### HTML efficiency rules

Normal production treats the renderer as a deterministic black box.

- Write project meaning in `content.md`; do **not** hand-author `final.html`.
- Do **not** load `template/approved-document.html` into model context during normal production. The renderer reads it at runtime.
- Do **not** copy Golden HTML/CSS/JS into prompts or working notes.
- Finish/reconcile canonical content before doing the main render projection. Avoid rebuilding full JSON after every drafting edit.
- Initial production: derive `render-data.json` once when canonical content is stable enough to render.
- Bounded revision: patch only affected render-data subtree/cross-reference; do not reconstruct unrelated packages.
- English-only documents should use scalar strings for ordinary English values instead of duplicating `{en,id}` text. Use localized objects only for intentional bilingual content; language-neutral names/codes/formulas may remain scalar.
- Omit `roles` on package terms when the default Gameplay visibility is correct; add role metadata only when visibility differs.
- Read `RENDERING.md` only when projection shape, language/Terms behavior, or renderer mechanics are actually needed.

The Golden Sample remains the output authority. Efficiency comes from deterministic projection and small context, not from replacing the approved document family.

## 3. REVIEW — Flow 4

Read `VALIDATION.md`.

```text
mechanical validator
+ Golden composition markers
+ visual sanity when actual rendered inspection exists
+ New Reader / Level Designer / Developer / Consistency
→ fix real findings
→ re-review only invalidated scope
```

For review, do not load the entire generated HTML source. The validator owns full-file mechanical inspection. Semantic review uses canonical content/relevant requirement state; visual review uses the actual rendered page/browser when available. Inspect HTML source only for a concrete bounded defect.

For a large document or bounded revision, review only the relevant package + required global/cross-reference context unless the change invalidates wider consistency.

## Revision fast path

```text
approved bounded change
→ affected requirement/content only
→ required cross-references
→ patch affected projection
→ rerender final HTML
→ one mechanical check
→ targeted semantic/visual re-review
```

Do not re-inventory unchanged source, re-ask resolved decisions, or replay unrelated packages/reviews.

## Internal artifact lifecycle

Artifacts are system-owned and appear only when their Flow needs them.

```text
CORE
Flow 2 → source/originals + source-inventory + requirement-register + intake-state
Flow 3 → content.md
Flow 4 → acceptance + current handoff state/artifact under repository policy

CONDITIONAL
review.md → only when user decision/recovery summary is useful
project README → only when project-specific navigation/context helps

DERIVED
render-data.json
final.html

DOWNSTREAM
Voice state/work/output → only after entering Voice Flow
```

Use sparse state: omit empty/default fields where the owning contract defines safe defaults; always persist exceptions such as conflicts, pending approvals, blocked state, supersession, and explicit positive readiness.

Do not pre-create empty downstream files, checksums, packaging manifests, template profiles, duplicate summaries, or additional quality reports merely to make a package look complete.

## Default user-facing delivery

```text
Final PRD: <final.html>

Main adjustments / recovered decisions:
- material items only

Needs attention:
- none OR real blocker/decision
```

Keep YAML, IDs, render data, validator JSON, CI logs, and internal evidence out of normal delivery unless requested or required to explain a blocker.

## Stop condition

Stop when current source/decisions support the canonical PRD, Golden rendering/mechanical contracts pass, four semantic lenses have no Critical/Major finding, unresolved material decisions are absent, and user receives the current final PRD. Do not claim visual fidelity beyond actual visual inspection or claim downstream implementation/QA/Voice completion.