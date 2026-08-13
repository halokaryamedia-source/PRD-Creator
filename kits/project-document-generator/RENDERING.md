# Rendering Contract

`CONTENT-CONTRACT.md` owns PRD meaning and approved PRD-core composition. This file owns deterministic projection into that composition and the approved downstream Production Assets extension inside the same project HTML.

## Authority chain

```text
work/content.md
→ work/render-data.json
→ exact Golden template + deterministic projection
→ PRD core in output/final.html
```

Optional downstream extension:

```text
accepted PRD core
→ downstream canonical production source
→ deterministic Production Assets projection
→ same output/final.html
```

The renderer may represent owned data. It does not invent project meaning or redesign the PRD.

## One project HTML

`output/final.html` is the single human-facing project document.

```text
PRD core pages
= accepted product/gameplay/level-design/developer truth
= owned by content.md + render-data.json

Production Assets pages
= downstream operator/developer material
= owned by the matching downstream canonical source
```

Adding a downstream Production Assets view does not reopen PRD acceptance while `content.md` and `render-data.json` remain unchanged.

## Exact Golden template identity

The repository keeps:

```text
template/golden-reference.html
template/runtime-template.html
```

byte-identical to the approved Golden artifact. Current approved Git blob:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

Do not replace either path with a cleaned, reconstructed, or generic interpretation.

Production Assets does not rewrite Golden template bytes. The base PRD core is rendered first; downstream pages and narrowly scoped extension styles/interactions are appended only when the matching canonical source exists.

## Runtime binding

Base runtime preprocessing may perform only project binding needed for the PRD render:

- strip Golden sample identity metadata;
- namespace localStorage keys for the current project;
- bind browser title/description/version metadata;
- replace sidebar navigation with current PRD navigation;
- replace document `<main>` PRD pages;
- replace glossary data;
- bind render-data revision metadata.

After the PRD core is rendered, the Production Assets compositor may:

- append one professional-only `Production Assets` navigation group to the **existing** PRD sidebar;
- append downstream pages after PRD-core pages;
- inject narrowly scoped extension CSS/interactions;
- do nothing when no downstream canonical production source exists.

It must not:

- rebuild Overview, Gameplay Flow, or Development navigation;
- promote gameplay/objective sections out of Development;
- renumber accepted PRD package/page codes;
- hand-patch project meaning into generated HTML.

## Locked Golden DOM vocabulary — PRD core

Stable global page IDs:

```text
development-overview  → Development Overview
shared-systems        → Game System
shared-data-reset     → Data and Reset
phase-development     → Gameplay Development
```

Stable opening Gameplay Flow ID:

```text
flow-start            → The Journey Begins
```

Package IDs remain:

```text
flow-<package>
dev-<package>-requirement
dev-<package>-level
dev-<package>-developer
```

Golden phase/runtime binding uses:

```text
data-phase="dev-flow"
data-phase="dev-system"
data-phase="dev-<package>"
data-clean-target="summary"
```

Preserve Golden navigation/component namespaces, including:

```text
phase-navigation
phase-nav-item
phase-nav-main
phase-page-list
phase-page-link professional-nav-item
phase-context-grid
quarry-development-flow
quarry-design-flow
quarry-dev-table
quarry-overview-table
quarry-build-table
quarry-development-table
quarry-sequence
quarry-note-grid
quarry-score-summary
quarry-inline-score-table
```

Do not rename these merely to create cleaner implementation aliases.

## Locked PRD-core family

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

For `N` gameplay sections the PRD-core page count remains `6 + 4N`.

Production Assets pages are downstream extensions and are not counted as PRD-core pages.

## Production Assets navigation

Production Assets is additive:

```text
03 Development
   existing PRD global + gameplay/objective navigation

04 Production Assets
   <asset category>
   <asset-specific links>
```

Current Voice implementation uses one `VOICE` category. Each Voice link shows:

```text
<gameplay section title>
<accepted PRD package label>
```

Rules:

- `VOICE` appears once;
- gameplay/objective navigation remains under Development;
- PRD page identities remain unchanged;
- Voice pages use their own Production Assets identities (`04A`, `04B`, ...);
- long sidebar labels wrap naturally; clipping/ellipsis is not the target behavior;
- asset-specific semantic/payload integrity remains owned by the matching downstream procedure/validator.

## Golden visual language for Production Assets

Production Assets must look native to the same project document, not like a separate dashboard.

Reuse:

- Golden sidebar hierarchy;
- page header/footer and sheet width;
- existing typography;
- existing document variables and professional-view behavior;
- print behavior.

Add only concrete asset-specific UI needed by the current production surface. Do not introduce a generic asset framework or speculative dashboard controls.

## Golden prototype rule — PRD core

The renderer may repeat project data inside approved Golden PRD components. It may not introduce a different PRD-core component because content is long or complex.

Do not render in PRD core:

- extra document-control panels on Overview;
- orientation cards on Gameplay Flow;
- replacement flow layouts that bypass Golden composition;
- visible Acceptance panels on Developer pages;
- Terms Used on Level Design or Developer pages;
- renamed Global Development pages/table headings;
- generic component namespaces that bypass Golden CSS/runtime behavior.

If PRD content does not fit clearly, improve or relocate the copy to the correct existing Golden surface. Do not redesign the PRD page and do not delete material rules to make the surface cleaner.

## Projection is lossless for material PRD structure

`render-data.json` is derived, but it may not be a lossy summary of canonical PRD content.

- independent requirements remain independently readable;
- independently meaningful table children are not flattened into one prose scalar;
- Gameplay Flow action/response/recovery paragraphs remain distinct when they express distinct rules;
- scoring/result/reset sub-rules remain readable in the owning Developer hierarchy;
- package glossary terms are not silently removed by role-based projection.

The renderer may transform representation, not meaning cardinality. If projection cannot represent canonical detail, fix projection ownership instead of truncating content.

## Visible package composition

### Gameplay Overview

```text
3 short context cards
→ Gameplay Information
→ Gameplay Flow
→ Terms Used
```

Gameplay Information labels remain:

```text
Game Purpose
Gameplay Time
Starting Condition
End Condition
Fail Condition
Scoring Criteria
```

### Level Design

```text
Level Design Overview
→ Design Flow
→ Build Requirements
→ Important Build Notes
```

### Developer

```text
Developer Overview
→ Development Flow
→ Development Requirements
→ Important Development Notes
```

Scoring/result and Reset/Interruption stay inside Development Requirements.

## Glossary

`packages[].terms` is the canonical package glossary source. Production Assets does not create glossary definitions.

Visible Terms Used follows Golden:

```text
Gameplay Flow        yes when terms exist
Global Development   yes when terms exist
Gameplay Overview    yes when terms exist
Level Design         no
Developer            no
Production Assets    no
```

## Version

`document.version` remains PRD project/release metadata, not an edit counter.

Adding/updating downstream Production Assets does not change `document.version` unless accepted PRD/project meaning also enters a new declared revision.

## Render economy

Initial PRD production:

```text
approved project meaning
→ content.md
→ render-data.json
→ one deterministic full final.html PRD-core render
```

Downstream extension:

```text
accepted PRD core
→ downstream canonical production source
→ one consolidated final.html rerender
```

If no downstream canonical source exists, Production Assets composition is a no-op.

Do not create a second default HTML, partial-page renderer, page cache, or speculative preview renderer merely to avoid a cheap deterministic full-file write.
