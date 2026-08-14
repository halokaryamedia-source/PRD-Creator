# Rendering Contract

`CONTENT-CONTRACT.md` owns PRD meaning and approved PRD-core composition. `PRODUCTION-ASSETS.md` owns the compact non-Voice Production Asset requirement contract. This file owns deterministic projection into the approved PRD composition and the downstream Production Assets extension inside the same project HTML.

## Authority chain

```text
work/content.md
→ work/render-data.json
→ exact Golden template + deterministic projection
→ PRD core in output/v<document.version>/prd.html
```

Optional downstream extension:

```text
accepted PRD core
→ optional work/asset-requirements.md
→ optional Voice canonical production source
→ deterministic objective-first Production Assets projection
→ same output/v<document.version>/prd.html
```

The renderer may represent owned data. It does not invent project meaning, asset requirements, or Voice content.

## One project HTML

`output/v<document.version>/prd.html` is the single human-facing project document.

```text
PRD core pages
= accepted product/gameplay/level-design/developer truth
= owned by content.md + render-data.json

Production Assets pages
= downstream operator/developer material
= non-Voice requirement owner: work/asset-requirements.md
= Voice production owner: work/voice-production.md
```

Adding or revising downstream Production Assets does not reopen PRD acceptance while `content.md` and `render-data.json` remain unchanged.

## Versioned delivery package

Normal handoff generation uses one deterministic command:

```bash
python kits/project-document-generator/renderer/delivery.py \
  workspace/active/<project>/
```

It reads the current canonical project sources once and writes:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

Responsibilities stay narrow:

- `prd.html` is the only human-facing project document and keeps the approved Golden presentation;
- `context.md` is a reasoning-friendly development projection of accepted PRD meaning plus only existing downstream non-Voice/Voice requirements that are relevant to implementation;
- `index.json` is a compact navigation tree with `context.md` line ranges, not a prose copy, schema registry, dependency engine, or second PRD;
- `output/README.md` is the stable resume entry point that identifies the current version and reading route.

`document.version` must use semantic `X.Y.Z` for a handoff package. Version folders track PRD/project meaning; a downstream-only Production Assets refresh may regenerate files inside the same version when accepted PRD meaning did not change.

The AI reading path is intentionally bounded:

```text
output/README.md
→ current index.json
→ affected context.md range (+ directly relevant shared/global range)
→ current implementation
```

The side documents may reorganize already-owned canonical information for reading efficiency. They may not invent project facts, implementation architecture, dependencies, approval state, or compatibility requirements.

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

Production Assets does not rewrite Golden template bytes. The base PRD core is rendered first; downstream pages and narrowly scoped extension styles/interactions are appended only when at least one accepted downstream canonical source exists.

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
- create one page per accepted gameplay/shared Production Assets section that actually contains downstream assets;
- group only non-zero categories inside that page;
- merge canonical Voice Production into the matching gameplay page's `Audio` category;
- append downstream pages after PRD-core pages;
- inject narrowly scoped extension CSS/interactions;
- do nothing when no downstream canonical production source exists.

It must not:

- rebuild Overview, Gameplay Flow, or Development navigation;
- promote gameplay/objective sections out of Development;
- nest categories or individual asset entries in the sidebar;
- render empty/zero categories;
- duplicate Voice canonical data into generic asset requirements;
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

Production Assets is additive and **objective-first**:

```text
03 Development
   existing PRD global + gameplay/objective navigation

04 Production Assets
   Global / Shared Assets      # only when real shared assets exist
   <gameplay section title>
      <Introduction | Objective N | Ending | accepted PRD label>
```

The sidebar does not expose category or asset-entry nesting. Inside each page, only categories with at least one asset are rendered:

```text
3D Models
UI & Information
Audio
Visual Effects & Presentation
```

Rules:

- gameplay/objective navigation remains under Development;
- PRD page identities remain unchanged;
- Production Assets pages use their own identities (`04A`, `04B`, ...);
- page order follows accepted project journey, with `Global / Shared Assets` first only when present;
- zero-count categories are absent rather than shown as `0`, `None`, or empty headings;
- Voice appears inside `Audio` on the matching page and retains its detailed Voice Production card, exact Trigger context, Speaker, Estimated Duration, canonical Eleven v3 payload, and Copy Prompt;
- long sidebar labels wrap naturally; clipping/ellipsis is not the target behavior;
- non-Voice requirement integrity remains owned by `PRODUCTION-ASSETS.md` + project `work/asset-requirements.md`;
- Voice semantic/payload integrity remains owned by the Voice Production Kit and its project canonical sources.

## Golden visual language for Production Assets

Production Assets must look native to the same project document, not like a separate dashboard.

Reuse:

- Golden sidebar hierarchy;
- page header/footer and sheet width;
- existing typography;
- existing document variables and professional-view behavior;
- print behavior.

Production Assets pages should remain scan-first:

```text
section title + accepted label + short context
→ total asset count + non-zero category counts
→ category heading
→ direct actionable asset requirements
```

A generic non-Voice asset entry displays only what production needs:

```text
Asset Name
Requirement       # mandatory
Usage             # optional
Content           # optional exact player-facing content
```

Do not render component inventories such as Model / Texture / Animation / Particle / SFX when those are simply parts of one owning asset. Add only concrete asset-specific UI needed by the current production surface; do not introduce a generic asset-management framework or speculative dashboard controls.

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
→ one deterministic versioned prd.html render
```

Downstream extension:

```text
accepted PRD core
→ optional asset-requirements.md + optional Voice canonical production
→ one consolidated versioned prd.html rerender
```

If no downstream canonical source exists, Production Assets composition is a no-op.

Do not create a second default HTML, partial-page renderer, page cache, generic asset registry/schema, or speculative preview renderer merely to avoid a cheap deterministic full-file write.
