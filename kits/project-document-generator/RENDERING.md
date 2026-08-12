# Rendering Contract

`CONTENT-CONTRACT.md` owns PRD meaning and the approved visible page prototypes. This file owns only deterministic projection into those prototypes.

## Authority chain

```text
work/content.md
→ work/render-data.json
→ exact Golden template + deterministic projection
→ output/final.html
```

The renderer does not invent project meaning and does not choose a new layout.

## Exact Golden template identity

The repository intentionally keeps two paths pointing to the **same approved HTML bytes**:

```text
template/golden-sample.html
→ canonical Golden reference evidence

template/approved-document.html
→ default runtime template alias used by renderer
```

Both files must remain byte-identical to the approved Golden artifact. Current approved Git blob:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

Do not replace either path with a cleaned, normalized, reconstructed, or generic interpretation. A visual redesign requires explicit user approval and a deliberate Golden revision.

The runtime may perform only non-visual project binding in a temporary in-memory/on-disk copy before projection:

- strip Golden sample identity metadata;
- namespace localStorage keys for the current project;
- replace browser title/description/version metadata;
- replace sidebar navigation;
- replace document `<main>` pages;
- replace glossary data;
- bind render-data revision metadata.

The repository template itself stays unchanged. Runtime preprocessing must not rewrite Golden CSS, JS behavior, DOM vocabulary, spacing, or component design.

## Locked Golden DOM vocabulary

Generated HTML must project into the same Golden DOM contract instead of generic aliases.

Stable global page IDs:

```text
development-overview  → Development Overview
shared-systems        → Game System
shared-data-reset     → Data and Reset
phase-development     → Gameplay Development
```

Stable opening Gameplay Flow ID:

```text
flow-start             → The Journey Begins
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

Golden navigation/component namespaces are preserved, including:

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

Do not rename these to `package-*`, `global-*`, generic grid names, or other “cleaner” aliases. The runtime JavaScript and approved CSS are part of the Golden contract.

## Locked page family

```text
01 Overview

02 Gameplay Flow
   The Journey Begins
   one Gameplay Flow page per package

03 Development
   Development Overview
   Game System
   Data and Reset
   Gameplay Development

04+ Gameplay Packages
   Gameplay Overview
   Level Design
   Developer
```

For `N` packages the page count is `6 + 4N`.

## Golden prototype rule

The renderer may repeat project data inside the approved Golden components. It may not introduce a different visible component because the content is long or complex.

Do not render:

- Document Control or extra metadata panels on Overview;
- orientation cards on Gameplay Flow;
- numbered-card replacements for Golden story-flow;
- Trigger / System Behavior / Data / Expected Result matrices as Developer Flow;
- a visible Acceptance & Verification panel on Developer pages;
- Terms Used blocks on Level Design or Developer pages;
- renamed Global Development pages/table headings;
- generic component namespaces that bypass Golden CSS/runtime behavior.

If content does not fit clearly, improve or relocate the copy to the correct existing Golden surface. Do not redesign the page and do not delete material rules to make the surface look cleaner.

## Projection is lossless for material structure

`render-data.json` is derived, but it may not be a lossy summary of canonical content.

The projection must preserve structured material meaning needed by Golden components:

- several independent requirements in one canonical group remain several visible bullets/rows;
- independently meaningful table children are not concatenated into one prose scalar;
- Gameplay Flow action/response/recovery paragraphs remain distinct when they express distinct rules;
- scoring/result/reset sub-rules remain independently readable in the approved Developer hierarchy;
- package glossary terms are not silently removed by role-based projection.

The renderer may transform representation, not meaning cardinality. If current projection cannot represent canonical detail, fix projection/schema ownership rather than truncating content.

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

Scoring/result and Reset/Interruption stay inside Development Requirements.

## Glossary

`packages[].terms` is the canonical package glossary source. Projection uses the complete package term set for that package's Golden phase scope; role filters must not silently reduce the visible/reference glossary.

Visible Terms Used follows Golden:

```text
Gameplay Flow        yes when terms exist
Global Development   yes when terms exist
Gameplay Overview    yes when terms exist
Level Design         no
Developer            no
```

Inline highlighting may still appear on phase-owned prose. Terms Used never highlights its own definitions.

## Version

`document.version` is project/release metadata, not an edit counter. Normal writing fixes, rerenders, reviews, and tests do not change it.

## Render economy

Rendering is the **mechanical end of an approved semantic workflow**. Do not use HTML generation as the user-facing drafting loop.

### Initial project production

```text
Source / requirement recovery
→ complete Simple Chat Preview
→ user approval
→ content.md
→ compact render-data.json
→ one planned full final.html render
```

Do not generate preview HTML or repeatedly rerender `final.html` while the user is still correcting gameplay in chat. If a validator/review finding exposes a real defect after the planned render, fix the first wrong owner and rerender again. A concrete finding justifies the extra render; speculative iteration does not.

### Bounded revision

```text
approved affected meaning
→ patch affected content.md meaning
→ patch affected render-data projection
→ one planned full final.html rerender
```

The renderer may rewrite the **whole HTML file** even when only one objective changed. This is expected. Do not build partial-page rendering, per-page artifacts, incremental HTML caches, or a second preview renderer merely to avoid a cheap deterministic full-file write.

The expensive work to keep bounded is model reasoning/review: do not reread unchanged source, rebuild unchanged meaning, or semantically review unrelated pages just because `final.html` was regenerated as one file.

### Golden access economy

Normal project authoring should use the Reverse-derived Golden fill map in `CONTENT-CONTRACT.md`. Do **not** load the full Golden HTML into model context simply to remember what each page/slot needs.

Load the exact Golden artifact only when the artifact itself is required evidence, such as:

- Golden regression / reference audit;
- template/CSS/runtime investigation;
- renderer page-composition investigation;
- targeted visual comparison or fidelity defect.

### Compact render data

`render-data.json` contains only the structured fields needed to fill the approved Golden surfaces. Keep out:

- chain-of-thought/reasoning;
- source-audit notes;
- rejected alternatives;
- approval conversation/transcript;
- confidence scores;
- duplicate prose that exists only for convenience.

This keeps projection deterministic and reduces model/context work without sacrificing material detail.

## Normal production

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

Never patch generated `final.html` manually. The renderer/template organize approved meaning; they do not replace Flow 2 decisions or Flow 4 review.
