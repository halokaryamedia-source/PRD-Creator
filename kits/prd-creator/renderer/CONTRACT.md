# Rendering Contract

`../document/CONTENT-CONTRACT.md` owns PRD semantic meaning. `../document/DESIGN-CONTRACT.md` owns approved PRD-core page/component grammar. `../production-assets/CONTRACT.md` owns non-Voice 04 meaning. This file owns deterministic projection, composition, and delivery mechanics.

## Authority chain

```text
work/content.md                       semantic truth
→ work/render-data.json               derived projection
→ DESIGN-CONTRACT approved grammar
→ exact Golden runtime template
→ output/v<document.version>/prd.html
```

Optional downstream extension:

```text
approved project model
→ optional work/asset-requirements.md
→ optional canonical Voice source
→ deterministic 04 Production Assets composition
→ same project HTML
```

The renderer may represent owned data. It may not invent project meaning, resource requirements, Voice content, or product decisions.

## Semantic cardinality preservation

Projection must preserve the number of distinct semantic items when those distinctions matter.

The existing Golden component families accept **data-driven child counts** for:

- Global Development Flow and notes;
- gameplay compact sequence steps;
- Level Design Flow and notes;
- Developer Flow and notes;
- Gameplay Flow narrative sections;
- journey cards, requirement rows/groups, and glossary items.

Renderer behavior is:

```text
canonical distinct items
→ same distinct items in render-data
→ existing approved component family
→ natural HTML wrapping/layout
```

Do not insert filler to reach a reference count. Do not truncate/merge independent items to reduce to a reference count.

Stable semantic/design slots such as Overview facts, Gameplay Context/Main Objective/Result, Gameplay Information rows, table columns, page family, IDs and navigation remain governed by the semantic/design contracts.

## One project HTML

`output/v<document.version>/prd.html` is the single human-facing project document.

```text
PRD core 01–03
= accepted gameplay / level-design / developer truth
= content + render-data + design grammar

04 Production Assets
= production handoff material
= non-Voice owner: work/asset-requirements.md
= Voice owner: work/voice-production.md
```

Adding/revising 04 does not reopen PRD-core acceptance while PRD semantic meaning is unchanged.

## Versioned delivery package

Normal handoff generation:

```bash
python kits/prd-creator/renderer/delivery.py \
  workspace/active/<project>/
```

writes:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

- `prd.html` is the human-facing document;
- `context.md` is a reasoning-friendly projection of accepted meaning plus relevant existing downstream requirements;
- `index.json` is a compact navigation/line-range tree;
- `output/README.md` is the stable resume entry point.

Side documents reorganize owned information for reading efficiency; they may not invent project facts, implementation architecture, dependencies, or approval state.

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

Do not replace either with a cleaned/reconstructed/generic interpretation.

Adaptive cardinality does **not** modify Golden bytes. It changes only the number of project-derived children inserted into existing component containers.

## Runtime binding

Base preprocessing may only perform bounded project binding required for deterministic rendering:

- strip Golden sample identity metadata from generated output;
- namespace localStorage keys;
- bind project title/description/version metadata;
- replace sidebar navigation;
- replace document `<main>` pages;
- replace glossary data;
- bind render-data revision metadata;
- project variable semantic child counts into approved component families.

## Stable PRD-core identity

Stable global page IDs:

```text
development-overview
shared-systems
shared-data-reset
phase-development
```

Stable opening flow ID:

```text
flow-start
```

Package IDs remain:

```text
flow-<package>
dev-<package>-requirement
dev-<package>-level
dev-<package>-developer
```

Preserve Golden runtime/component vocabulary needed by CSS/JS and validation, including:

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

## Locked page family

```text
01 Overview

02 Gameplay Flow
   The Journey Begins
   one Gameplay Flow page per gameplay package

03 Development
   Development Overview
   Game System
   Data and Reset
   Gameplay Development
   gameplay packages
      Gameplay Overview
      Level Design
      Developer
```

For `N` gameplay packages, PRD-core page count remains `6 + 4N`. 04 pages are additive and excluded from that count.

## Projection is lossless for material structure

- independent requirements remain independently readable;
- table children are not flattened when independently meaningful;
- action/response/recovery paragraphs remain distinct when they express distinct rules;
- scoring/result/reset sub-rules remain readable in Developer hierarchy;
- glossary terms are not silently removed;
- variable flow/note/sequence cardinality survives projection.

If the current projection cannot represent canonical detail, fix projection/design ownership rather than truncating content.

## 04 Production Assets

After PRD-core rendering, the shared 04 compositor may append only accepted downstream Production Asset pages and narrowly scoped extension styles/interactions. It may not rebuild or alter 01–03 page composition, navigation identity, project meaning, or Golden template bytes.

04 remains objective/moment-first, uses the visible types `MODEL`, `ITEM`, `UI / TEXT`, `AUDIO`, `PARTICLE`, and follows `../production-assets/CONTRACT.md` plus Voice canonical owners for exact meaning.

If no downstream canonical source exists, 04 composition is a no-op.

## Glossary

`packages[].terms` remains the package glossary source. Visible Terms Used follows the design contract:

```text
Gameplay Flow        yes when terms exist
Global Development   yes when terms exist
Gameplay Overview    yes when terms exist
Level Design         no
Developer            no
Production Assets    no
```

## Version

`document.version` is project/release metadata, not an edit counter. A downstream-only 04 refresh does not change it unless accepted PRD/project meaning enters a new declared revision.

## Render economy

```text
approved semantic meaning
→ content.md
→ render-data.json
→ one deterministic full-file render
→ optional 04 composition
```

Do not create a second default HTML, partial-page renderer, page cache, renderer profile, generic asset registry/schema, or speculative preview renderer merely to avoid a cheap deterministic full-file write.
