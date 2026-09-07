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

The renderer may represent owned data. It may not invent project meaning, resource requirements, Voice content, ownership, or product decisions.

## Implementation boundary

Renderer and validator engines use domain-specific module names. Do not reintroduce generic sibling `_engine.py` modules that depend on `sys.path` ordering and can collide in `sys.modules`.

Shared machine parsing lives under `../shared/`:

```text
shared/state.py  → YAML state
shared/voice.py  → typed Voice requirements/production grammar
```

The 04 compositor consumes stable Owner/Asset IDs from canonical sources; display titles are not machine joins.

## Semantic cardinality preservation

Projection preserves distinct semantic items when those distinctions matter. Existing Golden component families accept data-driven child counts for Global Development Flow/notes, gameplay compact sequences, Level Design Flow/notes, Developer Flow/notes, Gameplay Flow narrative sections, journey cards, requirement rows/groups, and glossary items.

```text
canonical distinct items
→ same distinct items in render-data
→ existing approved component family
→ natural HTML wrapping/layout
```

Do not insert filler to reach a reference count or merge independent items merely to reduce to a reference count.

Stable semantic/design slots such as Overview facts, Gameplay Context/Main Objective/Result, Gameplay Information rows, table columns, page family, IDs and navigation remain governed by semantic/design contracts.

## One project HTML

`output/v<document.version>/prd.html` is the single human-facing project document.

```text
PRD core 01–03
= accepted gameplay / level-design / developer truth

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

produces:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

Generation is staged. Renderer/context/index/README are built in a temporary delivery directory first; current outputs are replaced only after all staged artifacts are successfully produced. A failed generation must not partially replace the last complete delivery.

- `prd.html` is the human-facing document;
- `context.md` is a reasoning-friendly projection of accepted meaning plus relevant current downstream requirements;
- `index.json` is compact navigation/line-range data;
- `output/README.md` is the stable resume entry point.

Side documents reorganize owned information for reading efficiency; they may not invent project facts, implementation architecture, dependencies, or approval state.

## Exact Golden template identity

The repository keeps:

```text
template/golden-reference.html
template/runtime-template.html
```

byte-identical to approved Golden artifact. Current approved Git blob:

```text
2050b965768489feda98373c2920bbee8c7093b3
```

Do not replace either with a cleaned/reconstructed/generic interpretation. Adaptive cardinality does not modify Golden bytes.

## Runtime binding

Base preprocessing may only perform bounded project binding required for deterministic rendering:

- strip Golden sample identity metadata from generated output;
- namespace localStorage keys;
- bind project title/description/version metadata;
- replace sidebar navigation and document pages;
- replace glossary data;
- bind render-data revision metadata;
- project variable semantic child counts into approved component families.

Template surgery remains bounded to exact known markers. Do not spread new ad hoc HTML mutation paths when an existing adapter/marker can own the change.

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

Preserve Golden runtime/component vocabulary required by CSS/JS/validation, including `phase-navigation`, package tabs, approved flow/table/sequence/note classes, and score-summary classes.

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

If the projection cannot represent canonical detail, fix projection/design ownership rather than truncating content.

## 04 Production Assets

After PRD-core rendering, the shared 04 compositor may append only accepted downstream pages and narrowly scoped extension styles/interactions. It may not rebuild or alter 01–03 page composition, navigation identity, project meaning, or Golden template bytes.

04 uses visible types `MODEL`, `ITEM`, `UI / TEXT`, `AUDIO`, `PARTICLE`. Source identity must follow `../production-assets/CONTRACT.md` and `../voice/VALIDATION.md`:

```text
section placement → stable Owner ID
non-Voice resource → stable AST-... ID
Voice resource → stable VO-... ID
```

The compositor rejects ambiguous/duplicate/missing identity and does not synthesize missing resource Function/Moment/ownership copy.

If no downstream canonical source exists, 04 composition is a no-op.

## Glossary

`packages[].terms` remains the package glossary source. Visible Terms Used follows the design contract: Gameplay Flow and Global Development when terms exist, Gameplay Overview when terms exist, and no glossary panel on Level Design, Developer, or Production Assets pages.

## Version

`document.version` is project/release metadata, not an edit counter. Exact Flow 4 acceptance uses render-data SHA-256 in addition to semantic version identity.

## Render economy

```text
approved semantic meaning
→ content.md
→ render-data.json
→ one deterministic full-file render
→ optional stable-ID 04 composition
→ staged delivery publish
```

Do not create a second default HTML, partial-page renderer, page cache, renderer profile, generic asset registry/schema, or speculative preview renderer merely to avoid a cheap deterministic full-file write.
