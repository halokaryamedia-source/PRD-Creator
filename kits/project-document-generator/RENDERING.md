# Rendering Contract

`CONTENT-CONTRACT.md` owns the gameplay PRD's mandatory Golden semantics. This file owns only projection/render mechanics.

## Authority chain

```text
work/content.md
→ work/render-data.json
→ current renderer + approved Golden template
→ output/final.html
```

The renderer does not decide whether a Golden function is optional. `CONTENT-CONTRACT.md` already decides that.

## Fail-closed mandatory shell

Before HTML is produced, render data must represent the complete fixed gameplay PRD shell:

```text
Overview
Gameplay Flow
  The Journey Begins
  one full Gameplay Flow page per gameplay package
Global Development
  Development Overview
  Session & Runtime System
  Data, Recovery & Reset
  Gameplay Package Integration
Gameplay packages
  Gameplay Overview
  Level Design
  Developer
```

Mandatory package/global blocks may contain an explicit negative or `Not Applicable` production statement where the semantic contract permits it, but they may not be silently omitted.

The renderer fails before writing `final.html` when deterministic mandatory shell data is missing. This includes current Overview document-control values and package-level `Acceptance & Verification` content.

## Projection shape

`render-data.json` remains a disposable structured projection, not a second semantic document.

```json
{
  "canonical_content_sha256": "<current content revision binding>",
  "document": {},
  "overview": {},
  "gameplay_flow": [],
  "global_development": [],
  "packages": []
}
```

The existing `canonical_content_sha256` is retained for now as a narrow stale-projection binding. It is not semantic proof and must not be treated as evidence of completeness.

`final.html` receives the current `render-data-sha256` marker so stale deterministic HTML cannot be mistaken for the current projection. No additional hash/checksum chain is added.

## Fixed deterministic identifiers

Global Development keeps stable IDs/order while using the professional display names owned by `CONTENT-CONTRACT.md`:

```text
development-overview  → Development Overview
game-system           → Session & Runtime System
data-reset             → Data, Recovery & Reset
gameplay-development   → Gameplay Package Integration
```

The first Gameplay Flow item uses `journey-begins`. Remaining Gameplay Flow IDs match package IDs in package order.

## Required Overview projection

Overview preserves the fixed Golden project facts:

```text
session-model
target-playtime
game-structure
```

It also carries `document_scope` and `intended_use` for the rendered Document Control block. Current approval/handoff state is intentionally not rendered there; lifecycle truth stays in Flow 4 state so approval does not require a cosmetic rerender.

Document Control renders as compact metadata. Main Systems renders as production content rather than reusing the same warning/note treatment.

Additional project facts are allowed when materially useful.

## Package projection

Gameplay Overview renders the short `player_flow` projection as **Objective Sequence**. The separate top-level Gameplay Flow collection remains the full chronological player narrative.

For a package-owned full Gameplay Flow page, renderer adds the owning package phase scope. This lets existing Golden runtime features—including package glossary indexing and active-package navigation—operate on the full narrative without creating another mapping artifact.

Package full Gameplay Flow may also render a compact orientation summary using already-defined Main Objective, previous flow position, and `next_destination`. This is derived presentation only; renderer must not invent missing project meaning.

Every package carries a non-empty `acceptance` list for the Developer-page **Acceptance & Verification** block. These are observable package-level definition-of-done statements, not a QA test-case framework.

Developer Flow keeps `trigger`, `behavior`, `data`, and `result` visibly separated when those fields exist. Renderer must not concatenate them into a dense punctuation-based sentence merely for compactness.

Level Design and Developer table labels follow `CONTENT-CONTRACT.md`; renderer code does not redefine their semantics.

## Scoring / Result projection

Every package carries exactly one result model:

```text
scoring
OR
completion_data
```

`scoring` represents an Objective Score. `completion_data` represents explicit `No Objective Score` behavior.

Both forms carry current project truth for final-result relationship, player-facing display, telemetry/export behavior, and interruption/duplicate behavior where required.

The renderer displays these distinctions and never infers `No Objective Score` from a display/export prohibition.

## Glossary Index projection

`packages[].terms` is the canonical package glossary source.

The renderer projects it to both:

```text
inline glossary JSON
→ approved Golden runtime can identify/highlight matching aliases

Terms Used
→ page/role-local term index
```

Package-owned full Gameplay Flow receives the same package term index as Gameplay Overview / Level Design / Developer according to role visibility. Do not duplicate the package term set inside `gameplay_flow[].terms`.

The runtime excludes `.terms-used-collapsible` from inline matching so a glossary definition does not recursively highlight itself.

The approved Golden tooltip engine remains the interaction authority. Renderer supplies correct package scope/data and a visible but restrained glossary affordance; it does not create a second tooltip system.

## Reading-experience layer

The approved Golden template remains the presentation foundation, but new PRD-specific refinements are centralized in the renderer-owned contract style/runtime rather than added as another sequence of versioned template patch styles.

Current screen-oriented refinements include:

- wider desktop reading surface while preserving print behavior;
- content-height sheets on screen instead of forcing print-height whitespace;
- compact Document Control metadata;
- distinct Main Systems cards;
- full Gameplay Flow orientation + readable narrative rhythm;
- structured Developer Flow (`Trigger / System Behavior / Data / Expected Result`);
- more readable production tables and stronger requirement-group/result hierarchy;
- observable Acceptance & Verification checks;
- active-focused package subnavigation;
- clear view labels: **Gameplay Journey** and **Full Production**;
- visible inline glossary affordance while keeping Terms Used clean.

These are reading/presentation rules only. They must not mutate project meaning.

## English and bilingual values

Default output is English-only.

For intentional EN + ID output, every user-visible textual value must explicitly provide both `en` and `id`. Structural values such as IDs, keys, version, weights, and step codes may remain language-neutral scalars.

This proves localization completeness only, not translation quality. Do not enable bilingual output merely because placeholder/machine-like Indonesian strings exist.

## Template boundary

The approved Golden template supplies the base visual/runtime behavior.

The renderer may replace or augment only project-owned/bounded surfaces already required by the family:

- metadata/title/brand;
- navigation;
- document pages inside `.document-main`;
- glossary data and package scope needed by the existing glossary engine;
- project local-storage namespace;
- language availability;
- bounded content-driven grid variables;
- centralized renderer reading-style/runtime overrides;
- current render-data revision marker.

Do not add another versioned template `<style>` patch merely to make a new generated surface readable when the renderer-owned reading layer is the correct owner.

Never patch `final.html` manually to repair missing semantics or presentation.

## Normal production

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

Normal authoring does not load the full template or generated HTML into model context. Renderer/validator may consume them directly; semantic review uses canonical content and actual rendered pages only where needed.

## Boundary

The renderer enforces deterministic shell completeness and presentation mechanics. It does not invent project meaning, decide materiality, repair Flow 2 gaps, or replace Flow 4 semantic acceptance.
