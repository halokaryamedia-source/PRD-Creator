# PRD Design & Golden Contract

This file owns **how accepted PRD-core meaning is presented**. Semantic completeness is owned by [CONTENT-CONTRACT.md](CONTENT-CONTRACT.md).

## Core separation

```text
CONTENT-CONTRACT.md
→ what must be communicated

DESIGN-CONTRACT.md
→ where/how that meaning is presented
```

The approved Golden Reference remains the canonical design reference, but **reference-project cardinality is not automatically semantic truth for every project**.

## Golden artifact identity

The repository retains one canonical Golden artifact:

```text
template/golden-reference.html
```

It is both approved design evidence and the default runtime source. Current approved Git blob remains:

```text
2050b965768489feda98373c2920bbee8c7093b3
```

Do not clean, reconstruct, normalize, or replace those bytes merely to make implementation easier. A separate checked-in runtime-template alias is intentionally not maintained.

The renderer may prepare a temporary project-specific runtime copy through `TemplateAdapter`; that temporary representation never becomes a second Golden authority.

The Golden example remains evidence for visual language and component behavior. Its project facts never become another project's facts.

## Golden design evolution

The existing approved Golden remains the only design authority until an explicitly requested redesign or a browser-proven design-system defect justifies changing it. Do not create a second template, visual profile, experimental Golden branch, or per-project design system.

### Entry boundary

A Golden/design-system change is justified only when one of these is true:

```text
user explicitly requests a visual/design-system change
→ Development

actual browser evidence shows the approved component/page family cannot present valid meaning acceptably
→ Development
```

Ordinary project-specific density, wording, or content variation does not by itself justify redesign. First use the current component family, adaptive cardinality, wording/grouping, and natural wrapping behavior.

### Efficient design loop

Use the smallest visual surface that can settle the design decision:

```text
current approved Golden
→ define exact visual problem + affected component/page family
→ edit the smallest design/runtime owner needed for a temporary prototype
→ render one representative/high-risk page
→ user visual review when subjective style/taste changes
→ revise the same bounded prototype if needed
→ approval
→ apply the coherent canonical Golden/design/renderer/test change
→ post-approval regression proportional to design reach
→ STOP
```

Do not regenerate or manually inspect the whole document on every visual iteration. Do not run full desktop/dark/mobile/print regression before the visual direction is accepted unless the reported defect itself only reproduces in one of those modes.

Exploration output is temporary evidence only. It does not become a tracked alternate template or project authority. The current approved Golden remains canonical until the replacement direction is approved and the canonical change is sufficiently proven.

### Visual approval boundary

User review is required when the change alters subjective design choices such as hierarchy, spacing language, visual density, typography feel, component appearance, or interaction presentation. This approval applies to the design-system change, not to every downstream PRD that reuses the approved Golden.

No extra approval is needed for a behavior-preserving technical repair when the intended approved visual result is already unambiguous and browser evidence can prove it.

### Post-approval proof economy

After visual approval, proof scales with the actual reach of the design change:

| Change reach | Required browser/design proof before claiming the design change complete |
|---|---|
| one local component or one page family | affected representative page(s) + relevant short/long/dense content case; only directly affected modes |
| shared component used by several page families | representative affected page families + directly affected responsive/theme/print modes |
| shared typography, spacing tokens, sidebar, global CSS, shell, navigation, theme/language/runtime behavior | representative cross-family pages + desktop light/dark + mobile + print as applicable |
| canonical Golden shell/JS/global composition change | Golden regression + representative cross-family browser matrix + repository/integration proof required by the changed contract |

A mode is directly affected when the changed CSS/JS/component behavior can alter that mode. Do not run unrelated modes merely for ceremony, but do not claim a global visual change from one desktop screenshot.

When the canonical Golden itself changes, update the Golden artifact, this design contract when its grammar changes, affected renderer/runtime owners, and required tests as one coherent logical change. Do not promote a new Golden while tests or docs still describe the old approved grammar.

## Fixed design system

The following remain stable unless explicitly redesigned:

- PRD-core page family and order;
- section/page naming for 01 Overview, 02 Gameplay Flow and 03 Development;
- stable page IDs and navigation hierarchy;
- page header/footer, typography, spacing and interaction language;
- Overview fact component and its three named semantic facts;
- Gameplay Overview's three context-card roles;
- Gameplay Information's six named rows;
- Build Requirements and Development Requirements table column meanings;
- Terms Used placement;
- Golden component families and DOM vocabulary used by CSS/runtime;
- one Gameplay Overview / Level Design / Developer set per gameplay package.

For `N` gameplay packages, PRD-core page count remains `6 + 4N`.

## Adaptive design surfaces

The following use the Golden **component family** but their item count follows approved project meaning:

- Complete Gameplay Journey cards: package/journey driven;
- Gameplay Flow story sections/paragraphs: data-driven;
- Global Development Flow cards: data-driven;
- Global Important Development Notes: data-driven;
- package Gameplay Flow steps: data-driven;
- Level Design Flow cards: data-driven;
- Important Build Notes: data-driven;
- Developer Flow cards: data-driven;
- Important Development Notes: data-driven;
- requirement groups/rows: data-driven;
- glossary entries: data-driven.

A generated PRD may therefore contain three, five, six, seven, or another justified count inside the same approved surface.

### No sample-count coercion

Do not:

- invent filler stages merely to reach four/five items;
- merge distinct semantic rules merely to reduce to four/five items;
- reject otherwise valid project meaning because its natural sequence count differs from AFTERSHOCK;
- treat exact article counts in the Golden artifact as universal project requirements.

The exact counts in `tests/test_prd_golden_reference.py` prove what the retained reference artifact contains. They are **reference evidence**, not universal authoring cardinality.

## Visible page composition

### 01 Overview

Order remains:

```text
page header
→ eyebrow / project type
→ project title
→ specification subtitle
→ project-context lead
→ Session Model / Target Playtime / Game Structure
→ Complete Gameplay Journey
→ Global Gameplay Direction
→ page footer
```

No extra document-control/status/acceptance panels are added to Overview by default.

### 02 Gameplay Flow

Order remains:

```text
page header
→ title / eyebrow / intro
→ chronological story-flow sections
→ transition
→ Terms Used when present
→ page footer
```

Story-flow section count is adaptive.

### 03 Global Development

Stable pages remain:

1. Development Overview
2. Game System
3. Data and Reset
4. Gameplay Development

Each page remains:

```text
title + subtitle
→ four-tab Development navigation
→ Overview context
→ Development Flow
→ Development Requirements
→ Important Development Notes
→ Terms Used when present
```

`Development Flow` and `Important Development Notes` item counts are adaptive.

Development Requirements columns remain:

```text
No. | Setup | Development Requirements | System Result
```

### Gameplay Overview

Order remains:

```text
package title + subtitle
→ Gameplay Overview / Level Design / Developer tabs
→ Gameplay Context / Main Objective / Result
→ Gameplay Information
→ Gameplay Flow
→ Terms Used when present
```

Gameplay Information rows remain:

```text
Game Purpose
Gameplay Time
Starting Condition
End Condition
Fail Condition
Scoring Criteria
```

Gameplay Flow item count is adaptive.

### Level Design

Order remains:

```text
package title + subtitle
→ package tabs
→ Level Design Overview
→ Design Flow
→ Build Requirements
→ Important Build Notes
```

No separate Terms Used block is rendered here.

Build Requirements columns remain:

```text
No. | Object | Area Size | Build and Visual Requirements | Gameplay Function
```

Design Flow and Important Build Notes counts are adaptive.

### Developer

Order remains:

```text
package title + subtitle
→ package tabs
→ Developer Overview
→ Development Flow
→ Development Requirements
→ Important Development Notes
```

No separate Terms Used block is rendered here.

Development Requirements columns remain:

```text
No. | Setup | Development Requirements | Gameplay Function
```

Development Flow and Important Development Notes counts are adaptive.

## Stable DOM/navigation vocabulary

Preserve the current Golden runtime vocabulary needed by the existing CSS/JS and validators, including:

```text
flow-start
development-overview
shared-systems
shared-data-reset
phase-development
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
```

Adaptive cardinality changes the number of children inside these components, not their semantic identity.

## Runtime projection allowance

The renderer may make only bounded project-specific runtime changes required for deterministic projection, including:

- remove sample identity metadata in generated output;
- namespace localStorage keys;
- bind project title/description/version metadata;
- replace navigation and document main content;
- replace glossary data;
- bind source/render freshness metadata;
- render data-driven item counts inside the approved component families.

This does not authorize arbitrary new visual component types.

## Visual quality rule

Adaptive cardinality does not mean unlimited density. If a surface becomes unreadable:

1. confirm the semantic items are genuinely distinct;
2. improve wording/grouping without deleting meaning;
3. use the existing component's natural wrapping/row behavior;
4. collect actual browser evidence;
5. change the design system only when browser evidence proves a real presentation defect.

Do not solve visual pressure by deleting semantic rules.

## Proof

Two independent questions remain:

```text
Semantic proof
→ does current project meaning satisfy CONTENT-CONTRACT.md?

Design proof
→ is that meaning projected into the approved component/page grammar here?
```

Browser-level claims require actual rendered/browser evidence. Static tests prove structure and projection behavior only. Golden evolution additionally follows the bounded prototype → approval → proportional post-approval proof contract above.
