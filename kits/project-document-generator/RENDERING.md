# Rendering Contract

The approved Golden Sample is the presentation **and page-composition authority** for this PRD family. The renderer must reproduce its reusable document language with project-specific content; merely injecting generic pages into the Golden CSS/JS shell is not sufficient.

Do not replace the Golden Sample with a reduced/minimal shell.

## Rendering model

```text
work/content.md                    canonical project meaning
        ↓
work/render-data.json              derived Golden projection
        ↓
template/approved-document.html    approved Golden Sample authority
        ↓
renderer/render.py + renderer/pages.py
        ↓
output/final.html                  derived project document
```

`render-data.json` and `final.html` are derived. When canonical meaning changes, regenerate them. Do not add revision/checksum machinery.

## What “preserve Golden” means

Preservation includes:

- document hierarchy and page rhythm;
- Overview / Gameplay Flow / Global Development / Gameplay Package organization;
- Gameplay Overview → Level Design → Developer package structure;
- Golden package titles/subtitles and 1/2/3 package tabs;
- storytelling-first Gameplay Flow composition;
- context blocks/cards;
- Golden production-table families and grouped rows;
- Level Design `Area Size / Build and Visual / Gameplay Function` separation;
- Developer grouped requirements with inline scoring/completion treatment;
- Important Notes card grids;
- Terms Used accordion treatment when used;
- project-branded footers and page codes;
- sidebar/navigation, typography, spacing, colors, controls, glossary interaction, responsive and print foundation.

The renderer may omit an optional block when the project has no meaningful content for it. It may **not** replace the Golden composition with unrelated generic cards/tables merely because that is easier to render.

## Projection rules

`render-data.json` remains a small structured projection, not another semantic authority.

Root shape:

```json
{
  "document": {},
  "overview": {},
  "gameplay_flow": [],
  "global_development": [],
  "packages": []
}
```

Each package keeps:

```text
gameplay
level_design
developer
```

The projection may carry fields needed to fill Golden surfaces, including:

- Gameplay purpose/time/start/end/fail/scoring summary/player flow;
- Level Design flow, object subtitle, area size, build/visual requirement, gameplay function, optional child rows, titled notes;
- Developer flow, grouped requirements, scoring/completion, reset, titled notes;
- page/role-specific Terms Used when needed.

Missing optional project facts remain absent/neutral. Do not synthesize exact dimensions, metrics, mechanics, persistence, architecture, or lore to populate a Golden component.

## Document language contract

Language availability is project-level and explicit.

```json
"document": {
  "languages": ["en"]
}
```

Supported modes are intentionally small:

```text
["en"]
→ default
→ English is the only selectable document language
→ the EN/ID control is hidden

["en", "id"]
→ bilingual document
→ the EN/ID control remains available
```

For bilingual output, a localized object that uses `en` / `id` must contain both values. Missing one side fails before rendering; the renderer must not silently copy the other language into it.

A scalar string is treated as intentionally shared text, such as a proper name, code, number, formula, or label that is meant to remain identical in both languages. Do not use a scalar merely to avoid translating ordinary bilingual prose.

This is a bounded language-availability rule, not a translation service, translation-memory system, or localization framework.

## Content-driven Golden grids

Golden composition stays fixed, but item distribution must not assume Aftershock's exact count.

On desktop:

- Overview `.journey` uses one column per item up to the Golden six-column capacity;
- Golden `.flow` cards use one column per item up to the Golden four-column capacity;
- lists above those capacities wrap using the existing Golden maximum instead of creating narrower card styles;
- existing mobile responsive behavior remains authoritative.

The renderer carries only the current item count through CSS variables. Do not create template profiles, layout scoring, or a separate responsive layout engine for this behavior.

## Role-specific Terms Used

Package terms remain one glossary source. Visible package Terms Used blocks are controlled by the optional `roles` field on each term:

```json
{
  "key": "example-term",
  "label": "Example Term",
  "definition": "Definition used by the package.",
  "roles": ["gameplay", "developer"]
}
```

Allowed role values:

```text
gameplay
level_design
developer
```

Behavior:

- omitted `roles` → visible on Gameplay Overview only;
- explicit roles → visible only on those role pages;
- `roles: []` → available to package glossary/tooltips without a visible package Terms Used block.

Do not repeat every package term on Level Design and Developer by default.

## Golden component ownership

`renderer/core.py` owns reusable Golden HTML helpers.

`renderer/pages.py` owns the current Golden page composition:

```text
Gameplay Flow
→ narrative page / narrative sequence

Global Development
→ shared tabs
→ context block
→ flow cards
→ grouped production table
→ notes cards

Gameplay Overview
→ package title/subtitle + 1/2/3 tabs
→ Gameplay Context / Main Objective / Result
→ Gameplay Information table
→ role sequence

Level Design
→ package title/subtitle + tabs
→ context block
→ Design Flow cards
→ Golden 5-column build table
→ notes cards

Developer
→ package title/subtitle + tabs
→ context block
→ Development Flow cards
→ grouped Golden development table
   including inline scoring/completion/reset
→ notes cards
```

Do not create another renderer profile/component framework to express this one approved document family.

## Golden fidelity guard

Mechanical validation checks a **small semantic marker set** for the generated pages, such as:

- `narrative-sequence` on Gameplay Flow pages;
- `package-tabs` on Golden development/package pages;
- `phase-context-grid`, `phase-overview-table`, and `role-sequence` on Gameplay Overview;
- `section-context`, `quarry-design-flow`, and `quarry-build-table` where applicable on Level Design;
- `section-context`, `quarry-development-flow`, `quarry-development-table`, and inline score/completion summary on Developer;
- Golden note grid when notes exist.

This protects against accidental regression back to generic page composition. It is **not** a pixel-diff system and does not prove visual quality.

Actual visual quality still requires final rendered/browser/page inspection when that claim is made.

## Glossary safety

Package glossary aliases may be a string array or an `en`/`id` object of string arrays. Malformed shapes fail before rendering.

Glossary data is inserted into an executable `<script>` block, so renderer serialization must remain script-context safe for `<`, `>`, `&`, U+2028, and U+2029.

This is a focused script-safety rule, not a sanitizer framework.

## Approved template mechanics

The renderer mutates only project-owned surfaces:

- title/metadata;
- sidebar project brand;
- generated navigation;
- generated pages inside `.document-main`;
- project glossary data;
- project-specific local-storage namespace;
- bounded project-dependent language availability and Golden grid-count behavior.

Required template markers are checked only where the renderer actually mutates the Golden Sample. Do not create a full-template snapshot framework.

## Commands

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

Use an alternate template only when the user explicitly approves a different document family.

## Boundary

Renderer code may organize approved project meaning into the Golden composition. It may never invent missing project facts, approve an unresolved decision, change scoring/completion meaning, or patch `final.html` as source of truth.

Keep production simple:

```text
canonical PRD
→ derive Golden projection
→ render Golden composition
→ validate
```
