# Rendering Contract

`../document/CONTENT-CONTRACT.md` owns PRD meaning and approved PRD-core composition. `../production-assets/CONTRACT.md` owns the bounded non-Voice 04 Production Asset requirement/writing contract. This file owns deterministic projection into the approved PRD composition and the downstream 04 Production Assets extension inside the same project HTML.

## Authority chain

```text
work/content.md
→ work/render-data.json
→ exact Golden template + deterministic projection
→ PRD core 01–03 in output/v<document.version>/prd.html
```

Optional downstream extension:

```text
approved project model
→ optional work/asset-requirements.md
→ optional Voice canonical production source
→ deterministic objective/moment-first 04 Production Assets projection
→ same output/v<document.version>/prd.html
```

The renderer may represent owned data. It does not invent project meaning, asset requirements, or Voice content.

## One project HTML

`output/v<document.version>/prd.html` is the single human-facing project document.

```text
PRD core pages 01–03
= accepted product/gameplay/level-design/developer truth
= owned by content.md + render-data.json

04 Production Assets pages
= production handoff material
= non-Voice requirement owner: work/asset-requirements.md
= Voice production owner: work/voice-production.md
```

Adding or revising 04 Production Assets does not reopen PRD-core acceptance while `content.md` and `render-data.json` remain unchanged.

## Versioned delivery package

Normal handoff generation uses one deterministic command:

```bash
python kits/prd-creator/renderer/delivery.py \
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

- `prd.html` is the only human-facing project document and keeps the approved Golden presentation for 01–03;
- `context.md` is a reasoning-friendly development projection of accepted PRD meaning plus only existing downstream non-Voice/Voice requirements that are relevant to implementation;
- `index.json` is a compact navigation tree with `context.md` line ranges, not a prose copy, schema registry, dependency engine, or second PRD;
- `output/README.md` is the stable resume entry point that identifies the current version and reading route;
- when `work/asset-requirements.md` exists, the consolidated `prd.html` carries one `asset-requirements-sha256` source binding so stale non-Voice 04 presentation can be rejected; this is a single freshness binding, not an asset manifest/checksum registry.

`document.version` must use semantic `X.Y.Z` for a handoff package. Version folders track PRD/project meaning; a downstream-only 04 refresh may regenerate files inside the same version when accepted PRD meaning did not change.

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
2050b965768489feda98373c2920bbee8c7093b3
```

Do not replace either path with a cleaned, reconstructed, or generic interpretation.

04 Production Assets does not rewrite Golden template bytes. The base PRD core is rendered first; downstream pages and narrowly scoped extension styles/interactions are appended only when at least one accepted downstream canonical source exists.

## Runtime binding

Base runtime preprocessing may perform only project binding needed for the PRD render:

- strip Golden sample identity metadata;
- namespace localStorage keys for the current project;
- bind browser title/description/version metadata;
- replace sidebar navigation with current PRD navigation;
- replace document `<main>` PRD pages;
- replace glossary data;
- bind render-data revision metadata.

After the PRD core is rendered, the 04 compositor may:

- append one professional-only `04 Production Assets` navigation group to the **existing** PRD sidebar;
- create one page per accepted gameplay/shared section that actually contains downstream resources;
- order pages by accepted project journey;
- group resource entries by natural gameplay moment inside the page;
- render visible resource types as `MODEL`, `ITEM`, `UI / TEXT`, `AUDIO`, or `PARTICLE`;
- merge canonical Voice Production into the matching moment as `AUDIO`;
- append downstream pages after PRD-core pages;
- inject narrowly scoped extension CSS/interactions;
- do nothing when no downstream canonical production source exists.

It must not:

- rebuild Overview, Gameplay Flow, or Development navigation;
- promote gameplay/objective sections out of Development;
- change 01–03 page composition or Golden template bytes;
- nest moments, types, or individual asset entries in the sidebar;
- render empty placeholder groups/cards;
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

04 Production Assets pages are additive downstream pages and are not counted as PRD-core pages.

## 04 Production Assets navigation

04 is additive and **objective-first**:

```text
03 Development
   existing PRD global + gameplay/objective navigation

04 Production Assets
   Global / Shared Assets      # only when real shared resources exist
   <gameplay section title>
      <Introduction | Objective N | Ending | accepted PRD label>
```

The sidebar does not expose moment/type/asset-entry nesting.

Inside each page, the body is **moment-first**, not a category dashboard:

```text
Objective N · <Objective Name>

01 · <natural gameplay moment>
   TYPE
   Resource Name
   resource-specific fields

02 · <next natural gameplay moment>
   ...
```

Rules:

- gameplay/objective navigation remains under Development;
- PRD page identities remain unchanged;
- 04 keeps top-level navigation number `04`, while its page footer codes use the distinct `PA-01`, `PA-02`, ... namespace so they cannot be confused with accepted PRD Development page codes;
- DOM page IDs are stable semantic identities derived from the owning shared/journey/package section rather than current list position;
- page order follows accepted project journey, with `Global / Shared Assets` first only when present;
- moment numbering follows the actual displayed order and remains sequential;
- reader-facing page titles use `Objective N · Name`, `Introduction · Name`, `Ending · Name`, or the matching accepted label;
- body copy does not repeat a second `Production Assets` heading when page chrome already identifies Section 04;
- visible type labels are `MODEL`, `ITEM`, `UI / TEXT`, `AUDIO`, `PARTICLE`;
- internal markdown storage headings are parser/source organization only and must not become the visible dashboard;
- Voice appears as `AUDIO` in the matching moment and retains canonical Voice payload while using the approved 04 visible fields: Function, Voice Preset, ElevenLabs Model, Estimated Duration, Prompt;
- performance-direction tags are visually distinct from spoken dialogue while Copy Prompt copies the exact canonical payload;
- long sidebar labels wrap naturally; clipping/ellipsis is not the target behavior;
- non-Voice requirement integrity remains owned by `../production-assets/CONTRACT.md` + project `work/asset-requirements.md`;
- Voice semantic/payload integrity remains owned by the Voice domain and its project canonical sources.

## Visual language for 04 Production Assets

04 must look native to the same project document, not like a separate dashboard.

Reuse:

- Golden sidebar hierarchy;
- page header/footer and sheet width;
- existing typography;
- existing document variables and professional-view behavior;
- print behavior.

A non-Voice visual resource renders as:

```text
TYPE
Resource Name

Function
<short direct function>

Visual Brief
<short literal production brief>

Size
<optional; only when a real approved size exists>
```

`Size` is omitted when unknown. Do not render placeholder size, vague `Large/Small`, or invented dimensions.

UI / TEXT renders:

```text
UI / TEXT
Resource Name

Function
...

Player Text
<exact copy>
```

Non-dialogue AUDIO renders:

```text
AUDIO
Resource Name

Function
...

Audio Brief
...
```

Do not render generic `States`, `Position`, `Orientation`, `Reuse`, `Used At`, `Create`, `Includes`, or `Build Specs` metadata for new 04 presentation. Do not render component inventories such as Model / Texture / Animation / Particle / SFX when those are simply parts of one owning resource.

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

`packages[].terms` is the canonical package glossary source. 04 Production Assets does not create glossary definitions.

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

Adding/updating downstream 04 Production Assets does not change `document.version` unless accepted PRD/project meaning also enters a new declared revision.

## Render economy

Initial PRD-core production:

```text
approved project meaning
→ content.md
→ render-data.json
→ one deterministic versioned prd.html render
```

04 extension:

```text
same approved project model
→ optional asset-requirements.md + optional Voice canonical production
→ one consolidated versioned prd.html rerender
```

The file materialization can happen after PRD-core approval, but asset needs should not be rediscovered by brainstorming over generated 01–03.

If no downstream canonical source exists, 04 composition is a no-op.

Do not create a second default HTML, partial-page renderer, page cache, generic asset registry/schema, or speculative preview renderer merely to avoid a cheap deterministic full-file write.
