# Rendering Contract

`CONTENT-CONTRACT.md` owns PRD meaning and the approved PRD-core page prototypes. This file owns deterministic projection into those prototypes **and the approved downstream Production Assets composition into the same project HTML**.

## Authority chain

PRD core:

```text
work/content.md
→ work/render-data.json
→ exact Golden template + deterministic projection
→ PRD core pages in output/final.html
```

Optional downstream production extension:

```text
accepted PRD core
→ downstream canonical production source
   currently: work/voice-production.md
→ deterministic Production Assets projection
→ appended professional-only pages in the same output/final.html
```

The renderer does not invent project meaning, Voice wording, actor selection, or a new PRD layout. Production Assets consumes already-owned downstream production data.

## One project HTML, separate owners

`output/final.html` is the single human-facing project document.

Its content has two ownership layers:

```text
PRD core pages
= accepted product / gameplay / level-design / developer truth
= owned by content.md + render-data.json

Production Assets pages
= downstream operator-facing production material
= owned by the matching production source
```

For Voice:

```text
work/voice-requirements.md
= internal Voice asset requirement

work/voice-production.md
= canonical actor/script production content

output/final.html → Production Assets → Voice
= derived human/operator view only
```

Do not duplicate Flow 5 requirement reasoning, source refs, `Must communicate`, `Must not add/repeat`, Performance Fill Map reasoning, WPM math, QA notes, or other internal production state into the HTML merely because the renderer can access it.

## PRD acceptance vs downstream acceptance

Adding or updating downstream Production Assets does **not** change accepted PRD meaning when `work/content.md` and `work/render-data.json` are unchanged.

Therefore:

```text
PRD core change
→ reopen affected PRD acceptance

Voice production change only
→ keep PRD core acceptance
→ rebuild consolidated final.html
→ validate affected Voice / Production Assets scope
```

`output/final.html` may therefore receive a downstream Production Assets composition after PRD handoff without pretending that the PRD itself was re-authored.

## Exact Golden template identity

The repository intentionally keeps two paths pointing to the **same approved HTML bytes**:

```text
template/golden-reference.html
→ canonical Golden reference evidence

template/runtime-template.html
→ default runtime template alias used by renderer
```

Both files remain byte-identical to the approved Golden artifact. Current approved Git blob:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

Do not replace either path with a cleaned, normalized, reconstructed, or generic interpretation.

The approved Production Assets extension does **not** rewrite the Golden template. The renderer first creates the unchanged PRD core through the Golden contract, then deterministically appends downstream pages and their narrowly scoped extension CSS/JS only when the matching canonical production source exists.

This keeps the PRD prototype stable while allowing the same HTML to become the project production hub approved by the user.

## Runtime binding

Base runtime preprocessing may perform only non-visual project binding before PRD-core projection:

- strip Golden sample identity metadata;
- namespace localStorage keys for the current project;
- replace browser title/description/version metadata;
- replace sidebar navigation;
- replace document `<main>` PRD pages;
- replace glossary data;
- bind render-data revision metadata.

After the base PRD render, the Production Assets compositor may additionally:

- append a professional-only `Production Assets` navigation group;
- append downstream production pages after all PRD-core pages;
- inject narrowly scoped Production Assets CSS using existing Golden variables/visual language;
- inject operator interaction needed by the page, currently Voice `Copy Text`;
- do nothing when no canonical downstream production source exists.

It must not modify existing PRD-core page DOM, CSS, copy, IDs, or semantics.

## Locked Golden DOM vocabulary — PRD core

Generated PRD-core HTML must project into the same Golden DOM contract instead of generic aliases.

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

Do not rename these to `package-*`, `global-*`, generic grid names, or other cleaner aliases. The runtime JavaScript and approved CSS are part of the Golden PRD-core contract.

## Locked PRD-core page family

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

For `N` packages the **PRD-core page count** remains `6 + 4N`.

Production Assets pages are downstream professional-only extensions and are not counted as PRD-core pages.

## Production Assets — Voice visible contract

When `work/voice-production.md` exists beside `render-data.json`, the normal renderer composes Voice into the same `output/final.html` after the PRD core.

Navigation:

```text
Production Assets
└── Voice — <gameplay section>
```

Voice pages follow the canonical `voice-production.md` section/entry order, which Flow 6 already keeps aligned to gameplay/Trigger order.

The first Voice page shows the **Voice Cast** once. Each Voice entry then exposes only:

```text
sequence
Voice title
Actor
Estimated Duration
exact Eleven v3 performance text
Copy Text
```

Do not show internal Voice Requirement fields in this operator surface.

### Voice Cast

`work/voice-production.md` may contain one compact header block before gameplay sections:

```text
Voice Cast:
- <Speaker>: <selected ElevenLabs voice>
```

When a speaker has no stored selected voice yet, the HTML shows `Voice selection pending` rather than inventing one.

The cast is shown once; per-line cards show only the Actor name.

### Exact prompt integrity

The HTML script panel is derived verbatim from the canonical fenced `performance` block, HTML-escaped for safety while preserving text and line breaks.

`Copy Text` copies only that exact prompt text. Requirement metadata, UI instructions, labels, and internal notes never enter the copied payload.

## Golden visual language for Production Assets

Production Assets must look native to the same project document, not like a separate dashboard.

Reuse:

- Golden sidebar/navigation hierarchy;
- page header/footer and sheet width;
- existing typography;
- `--navy`, `--blue`, `--amber`, `--line`, `--soft`, `--paper`, `--ink`, and `--muted` variables;
- existing professional-view behavior;
- print behavior.

New component styling is limited to the concrete operator need: Voice Cast cards, exact script panels, and Copy Text action. Do not clone the ElevenLabs UI, add dark code-editor styling, status dashboards, audio players, settings databases, or speculative asset controls.

## Golden prototype rule — PRD core

The renderer may repeat project data inside approved Golden PRD components. It may not introduce a different PRD-core component because the content is long or complex.

Do not render in PRD core:

- Document Control or extra metadata panels on Overview;
- orientation cards on Gameplay Flow;
- numbered-card replacements for Golden story-flow;
- Trigger / System Behavior / Data / Expected Result matrices as Developer Flow;
- a visible Acceptance & Verification panel on Developer pages;
- Terms Used blocks on Level Design or Developer pages;
- renamed Global Development pages/table headings;
- generic component namespaces that bypass Golden CSS/runtime behavior.

If PRD content does not fit clearly, improve or relocate the copy to the correct existing Golden surface. Do not redesign the PRD page and do not delete material rules to make the surface look cleaner.

## Projection is lossless for material PRD structure

`render-data.json` is derived, but it may not be a lossy summary of canonical PRD content.

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
Production Assets    no
```

Production Assets does not create glossary definitions; it consumes exact downstream production text.

## Version

`document.version` remains PRD project/release metadata, not an edit counter.

Adding/updating downstream Voice Production does not change `document.version` unless the accepted PRD/project itself also enters a new declared revision.

Voice Production maintains its own script version/evidence according to the Voice workflow.

## Render economy

Rendering is the mechanical end of an approved semantic workflow.

### Initial PRD production

```text
Source / requirement recovery
→ complete Simple Chat Preview
→ user approval
→ content.md
→ compact render-data.json
→ one planned full final.html PRD-core render
```

If no `voice-production.md` exists, Production Assets composition is a no-op and the normal PRD output stays unchanged.

### Downstream Voice preparation

```text
accepted PRD core
→ voice-requirements.md
→ voice-production.md
→ one consolidated final.html rerender
→ Production Assets → Voice appears after PRD core
```

Do not create `voice-production.html` as a second default operator document. The same project HTML is the approved human-facing surface.

DOCX may remain an optional derived Voice export when requested/current workflow still needs it.

### Bounded revision

PRD change:

```text
approved affected PRD meaning
→ patch affected content.md meaning
→ patch affected render-data projection
→ one full final.html rerender
```

Voice-only change:

```text
approved/current Voice production change
→ patch voice-production.md
→ one full final.html rerender
→ review only affected Production Assets / continuity scope
```

The renderer may rewrite the whole HTML file. Do not build partial-page rendering, per-page artifacts, incremental HTML caches, or a second preview renderer merely to avoid a cheap deterministic full-file write.

## Golden access economy

Normal project authoring should use the Reverse-derived Golden fill map in `CONTENT-CONTRACT.md`. Do not load the full Golden HTML into model context simply to remember what each PRD page/slot needs.

Load the exact Golden artifact only when the artifact itself is required evidence, such as:

- Golden regression / reference audit;
- template/CSS/runtime investigation;
- renderer page-composition investigation;
- targeted visual comparison or fidelity defect.

Production Assets extension work should reuse the already-defined Golden variables/components and does not require copying the Golden HTML into another template.

## Compact render data

`render-data.json` contains only the structured fields needed to fill approved PRD-core Golden surfaces. Keep downstream Voice wording out of it.

Do not add:

- Voice scripts;
- actor selections;
- chain-of-thought/reasoning;
- source-audit notes;
- rejected alternatives;
- approval conversation/transcript;
- confidence scores;
- duplicate prose that exists only for convenience.

Voice remains in its existing canonical `work/voice-production.md`; the compositor reads that source directly.

## Normal production

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

The same command automatically includes `work/voice-production.md` when it exists in the same project work directory.

Never patch generated `final.html` manually. The renderer/compositor organizes approved meaning and production content; it does not replace Flow 2 decisions, Flow 4 PRD review, or Flow 7 Voice review.
