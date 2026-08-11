# Rendering Contract

`CONTENT-CONTRACT.md` owns the gameplay PRD's mandatory Golden semantics. This file owns only projection/render mechanics.

## Authority chain

```text
work/content.md
→ work/render-data.json
→ current renderer + approved Golden template
→ output/final.html
```

The renderer does not decide whether a Golden function is optional. `CONTENT-CONTRACT.md` already decides that.

## Fail-closed mandatory shell

Before HTML is produced, render data must represent the complete fixed gameplay PRD shell:

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

Mandatory package/global blocks may contain an explicit negative or `Not Applicable` production statement where the semantic contract permits it, but they may not be silently omitted.

The renderer fails before writing `final.html` when deterministic mandatory shell data is missing. This includes current Overview document-control values and package-level `Acceptance & Verification` content.

## Projection shape

`render-data.json` remains a disposable structured projection, not a second semantic document.

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

The existing `canonical_content_sha256` is retained for now as a narrow stale-projection binding. It is not semantic proof and must not be treated as evidence of completeness.

`final.html` receives the current `render-data-sha256` marker so stale deterministic HTML cannot be mistaken for the current projection. No additional hash/checksum chain is added.

## Fixed deterministic identifiers

Global Development keeps stable IDs/order while using the professional display names owned by `CONTENT-CONTRACT.md`:

```text
development-overview  → Development Overview
game-system           → Session & Runtime System
data-reset             → Data, Recovery & Reset
gameplay-development   → Gameplay Package Integration
```

The first Gameplay Flow item uses `journey-begins`. Remaining Gameplay Flow IDs match package IDs in package order.

## Required Overview projection

Overview preserves the fixed Golden project facts:

```text
session-model
target-playtime
game-structure
```

It also carries `document_scope` and `intended_use` for the rendered Document Control block. Current approval/handoff state is intentionally not rendered there; lifecycle truth stays in Flow 4 state so approval does not require a cosmetic rerender.

Additional project facts are allowed when materially useful.

## Package projection

Gameplay Overview renders the short `player_flow` projection as **Objective Sequence**. The separate top-level Gameplay Flow collection remains the full chronological player narrative.

Every package also carries a non-empty `acceptance` list for the Developer-page **Acceptance & Verification** block. These are observable package-level definition-of-done statements, not a QA test-case framework.

Level Design and Developer table labels follow `CONTENT-CONTRACT.md`; renderer code does not redefine their semantics.

## Scoring / Result projection

Every package carries exactly one result model:

```text
scoring
OR
completion_data
```

`scoring` represents an Objective Score. `completion_data` represents explicit `No Objective Score` behavior.

Both forms carry current project truth for final-result relationship, player-facing display, telemetry/export behavior, and interruption/duplicate behavior where required.

The renderer displays these distinctions and never infers `No Objective Score` from a display/export prohibition.

## English and bilingual values

Default output is English-only.

For intentional EN + ID output, every user-visible textual value must explicitly provide both `en` and `id`. Structural values such as IDs, keys, version, weights, and step codes may remain language-neutral scalars.

This proves localization completeness only, not translation quality. Do not enable bilingual output merely because placeholder/machine-like Indonesian strings exist.

## Terms Used

Terms remain project-driven. A Terms block may be omitted when no production-critical terminology exists for that surface; this is a genuinely conditional component under `CONTENT-CONTRACT.md`.

## Template boundary

The approved Golden template supplies presentation/runtime behavior only.

The renderer may replace only project-owned surfaces already required by the family:

- metadata/title/brand;
- navigation;
- document pages inside `.document-main`;
- glossary data;
- project local-storage namespace;
- language availability;
- bounded content-driven grid variables;
- current render-data revision marker.

Never patch `final.html` manually to repair missing semantics.

## Normal production

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

Normal authoring does not load the full template or generated HTML into model context. Renderer/validator may consume them directly; semantic review uses canonical content and actual rendered pages only where needed.

## Boundary

The renderer enforces deterministic shell completeness and presentation mechanics. It does not invent project meaning, decide materiality, repair Flow 2 gaps, or replace Flow 4 semantic acceptance.
