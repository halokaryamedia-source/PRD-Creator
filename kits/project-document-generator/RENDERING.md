# Rendering Contract

`CONTENT-CONTRACT.md` owns PRD meaning and the approved visible page prototypes. This file owns only deterministic projection into those prototypes.

## Authority chain

```text
work/content.md
→ work/render-data.json
→ approved-document.html + renderer
→ output/final.html
```

The renderer does not invent project meaning and does not choose a new layout.

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

Stable internal IDs remain:

```text
development-overview  → Development Overview
game-system           → Game System
data-reset             → Data and Reset
gameplay-development   → Gameplay Development
```

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

If content does not fit clearly, improve or relocate the copy to the correct existing Golden surface. Do not redesign the page.

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

`template/approved-document.html` owns stable Golden presentation/runtime:

- page size, spacing, typography, tables and flow cards;
- sidebar/navigation;
- Overview / Full Detail view mode;
- light/dark presentation;
- glossary tooltip;
- responsive/print behavior.

The template uses one maintained stylesheet/runtime layer. Do not append version-labelled CSS/JS patches or reference-project namespaces.

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
