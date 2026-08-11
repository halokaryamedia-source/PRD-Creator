# Rendering Contract

`CONTENT-CONTRACT.md` owns PRD meaning and the approved visible page prototypes. This file owns only deterministic projection into those prototypes.

## Authority chain

```text
work/content.md
→ work/render-data.json
→ runtime template + renderer
→ output/final.html
```

The renderer does not invent project meaning and does not choose a new layout.

## Canonical Golden artifact versus runtime shell

Two different artifacts have different jobs and must not be conflated again:

```text
template/golden-sample.html
→ exact approved Golden reference artifact
→ canonical evidence for visible composition, spacing, component order, navigation behavior and information-density review

template/approved-document.html
→ maintained runtime shell consumed by renderer
→ may be cleaned internally only when the rendered result still matches the canonical Golden artifact
```

`golden-sample.html` is not a generic starter template and must not be replaced by a reduced or normalized interpretation of the reference. If the Golden Sample itself is intentionally redesigned, that requires explicit user approval and both the canonical artifact and runtime projection contract must be updated together.

A refactor of `approved-document.html`, renderer class names, CSS organization, or runtime JS is acceptable only when it is representation-preserving. “Cleaner code” is not evidence that Golden fidelity was preserved.

## Locked visible shell

The generated HTML follows the Golden Sample page prototypes exactly:

```text
Overview
Gameplay Flow
  The Journey Begins
  one page per gameplay package
Development
  Development Overview
  Game System
  Data and Reset
  Gameplay Development
Gameplay packages
  Gameplay Overview
  Level Design
  Developer
```

For `N` packages the page count is `6 + 4N`.

The canonical Golden reference uses these stable representative section IDs:

```text
development-overview  → Development Overview
shared-systems        → Game System
shared-data-reset     → Data and Reset
phase-development     → Gameplay Development
```

Project data may use internal semantic IDs such as `game-system`, `data-reset`, or `gameplay-development`, but projection must map them to the visible Golden page family instead of leaking alternate names/structure into the final HTML.

## Golden prototype rule

The renderer may repeat project data inside the approved Golden components. It may not introduce a different visible component because the content is long or complex.

In particular, do not render:

- Document Control or extra metadata panels on Overview;
- orientation cards on Gameplay Flow;
- numbered narrative-card replacements for Golden story-flow;
- Trigger / System Behavior / Data / Expected Result matrices as Developer Flow;
- a visible Acceptance & Verification panel on Developer pages;
- Terms Used blocks on Level Design or Developer pages;
- renamed Global Development pages or renamed Golden table headings.

If content does not fit clearly, improve or relocate the copy to the correct existing Golden surface. Do not redesign the page and do not delete material rules to make the surface look cleaner.

## Projection is lossless for material structure

`render-data.json` is derived, but it may not be a lossy summary of canonical content.

The projection must preserve structured material meaning needed by Golden components:

- several independent requirements in one canonical requirement group remain several visible bullets/rows;
- independently meaningful table children are not concatenated into one prose scalar;
- Gameplay Flow paragraphs that represent different action/response/recovery states are not collapsed merely for brevity;
- scoring/result/reset sub-rules remain independently readable in their approved Developer hierarchy;
- glossary terms supported by canonical content are not silently dropped during projection.

The renderer may transform representation, not meaning cardinality. If structured canonical detail cannot be represented by the current projection schema, fix the projection/schema owner rather than truncating the content.

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
→ Design Flow (4 Golden cards)
→ Build Requirements
→ Important Build Notes
```

Columns:

```text
No. | Object | Area Size | Build and Visual Requirements | Gameplay Function
```

### Developer

```text
Developer Overview
→ Development Flow (4 Golden cards)
→ Development Requirements
→ Important Development Notes
```

Columns:

```text
No. | Setup | Development Requirements | Gameplay Function
```

Scoring/result and Reset/Interruption stay inside the Development Requirements hierarchy.

## Glossary

`packages[].terms` remains the canonical package glossary source.

Inline highlighting may be role-scoped, but visible Terms Used follows Golden:

```text
Gameplay Flow        yes
Global Development   yes
Gameplay Overview    yes
Level Design         no
Developer            no
```

Terms Used never highlights its own definitions.

## Template ownership

`template/golden-sample.html` owns approved reference evidence for:

- visible page composition and component order;
- typography/spacing/reading rhythm;
- sidebar/navigation hierarchy;
- Overview / Full Detail behavior;
- light/dark presentation;
- glossary tooltip behavior;
- responsive/print behavior;
- representative information density.

`template/approved-document.html` owns the maintained runtime implementation of that behavior. It may not silently redefine the Golden reference.

The renderer owns only project metadata, pages, navigation contents, glossary data/scopes, language availability, storage namespace, and render revision binding.

Never patch generated `final.html` manually.

## Version

`document.version` is project/release metadata, not an edit counter. Normal writing fixes, rerenders, reviews, and tests do not change it.

## Normal production

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

The renderer/template organize approved meaning; they do not replace Flow 2 decisions or Flow 4 review.
