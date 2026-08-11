# Rendering Contract

`CONTENT-CONTRACT.md` owns gameplay PRD meaning. This file owns only projection, template, and generated-HTML mechanics.

## Authority chain

```text
work/content.md
→ work/render-data.json
→ generic approved PRD template + renderer
→ output/final.html
```

The renderer does not decide whether a Golden function is optional and does not repair missing project meaning.

## Mandatory shell

Before HTML is produced, render data must represent the complete gameplay PRD family:

```text
Overview
Gameplay Flow
  The Journey Begins
  one full Gameplay Flow page per gameplay package
Global Development
  Development Overview
  Session & Runtime System
  Data, Recovery & Reset
  Gameplay Package Integration
Gameplay packages
  Gameplay Overview
  Level Design
  Developer
```

Mandatory package/global blocks may contain an explicit negative or `Not Applicable` production statement where `CONTENT-CONTRACT.md` permits it, but they may not silently disappear.

## Projection boundary

`render-data.json` is a disposable structured projection, not another semantic document.

```json
{
  "canonical_content_sha256": "<current content revision binding>",
  "document": {},
  "overview": {},
  "gameplay_flow": [],
  "global_development": [],
  "packages": []
}
```

The existing `canonical_content_sha256` remains a narrow stale-projection binding only. `final.html` receives the current `render-data-sha256` marker for stale rendered-output detection. Neither hash proves semantic quality.

No additional checksum chain is added.

## Stable identifiers

Global Development keeps these internal IDs while displaying the professional names owned by `CONTENT-CONTRACT.md`:

```text
development-overview  → Development Overview
game-system           → Session & Runtime System
data-reset             → Data, Recovery & Reset
gameplay-development   → Gameplay Package Integration
```

The first Gameplay Flow ID is `journey-begins`. Remaining Gameplay Flow IDs match package IDs in package order.

## Generic template rule

`template/approved-document.html` is a **generic PRD presentation/runtime template**.

It may contain stable component names such as:

```text
package
requirement
development
glossary
journey
production
result
```

It must not carry implementation-history or reference-project naming such as:

```text
V19 / V20 / V90 / V94
v14-style / v18-style
"final polish" iteration labels
source-document revision chains
aftershock-*
quarry-*
phase-* when the actual concept is gameplay package
```

The document's real `document.version` is valid project metadata and is not the same thing as internal CSS/feature iteration numbering.

When presentation needs improvement, edit the correct stable component/template rule. Do **not** create a new version-labeled style/script patch at the end of the template.

## Template / renderer ownership

The generic template owns stable presentation and browser interaction:

- document/sidebar layout;
- light/dark presentation;
- Gameplay Journey / Full Production reading views;
- package-focused navigation behavior;
- glossary tooltip interaction;
- responsive/print presentation.

The renderer owns project projection into that template:

- metadata/title/brand;
- document pages inside `.document-main`;
- navigation contents;
- package/glossary scope attributes;
- glossary JSON;
- project-local storage prefix;
- language availability;
- current render-data revision marker.

The renderer must not inject another stylesheet/runtime layer merely to compensate for a badly structured template. The template must not contain project facts.

Never patch generated `final.html` manually.

## Overview projection

Overview carries:

```text
session-model
target-playtime
game-structure
document_scope
intended_use
```

Document Control is compact metadata. Main Systems is production information and remains visually distinct from metadata.

## Package projection

Gameplay Overview renders `player_flow` as **Objective Sequence**. Top-level Gameplay Flow remains the complete chronological player journey.

Package-owned Gameplay Flow and its three production pages use the same stable package ID for:

- active package navigation;
- glossary scope;
- role-local Terms Used.

A package Gameplay Flow may derive its orientation summary from already-defined Main Objective, previous flow position, and `next_destination`. Renderer must not invent missing meaning.

Developer Flow keeps `trigger`, `behavior`, `data`, and `result` visually distinct when those fields exist.

Every package also renders non-empty `Acceptance & Verification` content on the Developer page.

## Scoring / Result projection

Every package carries exactly one result model:

```text
scoring
OR
completion_data
```

`scoring` represents an Objective Score. `completion_data` represents explicit `No Objective Score` behavior.

Both preserve final-result relationship, player-facing display, telemetry/export behavior, and interruption/duplicate behavior required by the semantic contract.

A display/export prohibition must never be interpreted as `No Objective Score`.

## Glossary projection

`packages[].terms` is the canonical package glossary source.

The renderer projects it to:

```text
inline glossary JSON
+ role-local Terms Used index
```

Package Gameplay Flow uses the owning package term index. `The Journey Begins` may carry its own opening-specific terms only when those terms genuinely do not belong to a package.

The Terms Used block does not recursively highlight its own definitions.

## Language

Default output is English-only.

For intentional EN + ID output, every user-visible text value must explicitly provide both `en` and `id`. Structural values such as IDs, keys, version, weights, and step codes may remain language-neutral scalars.

This validates localization completeness only, not translation quality.

## Normal production

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

Normal authoring does not load the full template or generated HTML into model context. Inspect template/HTML source only for a concrete presentation defect and only at the smallest useful range.

## Boundary

The template and renderer organize approved meaning into a stable readable artifact. They do not invent product meaning, decide materiality, repair Flow 2 gaps, or replace Flow 4 semantic acceptance.
