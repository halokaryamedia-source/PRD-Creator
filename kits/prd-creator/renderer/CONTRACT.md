# Rendering Contract

`../document/CONTENT-CONTRACT.md` owns PRD meaning. `../document/DESIGN-CONTRACT.md` owns approved page/component grammar. `../production-assets/CONTRACT.md` owns non-Voice 04 meaning. This file owns deterministic projection, Golden-shell adaptation, 04 composition, and delivery publication.

## Authority chain

```text
work/content.md
→ strict work/render-data.json + canonical_content_sha256
→ DESIGN-CONTRACT
→ exact Golden shell through TemplateAdapter
→ PRD core HTML
→ optional stable-ID 04 composition
→ transactional versioned delivery
```

The renderer may represent accepted data. It may not invent project/resource/Voice meaning.

## Shared machine contracts

Executable schemas live under `../shared/`:

```text
intake.py         Flow 2 source/requirement/approval state
state.py          duplicate-safe YAML loading
paths.py          safe project-relative persisted paths
handoff.py        strict Flow 4 handoff state
render_schema.py  one supported render-data field vocabulary
localization.py   bilingual presence + invariant parity
assets.py         strict non-Voice Owner/Moment/Asset grammar
voice.py          strict Voice requirement/production grammar
lifecycle.py      one Voice state vocabulary
topology.py       canonical 04 Owner topology
issues.py         structured validation issue model
```

Do not duplicate these schemas in renderer modules or prose.

## Strict projection

`work/render-data.json` has one supported vocabulary and must bind exact current `content.md` bytes through `canonical_content_sha256`.

Renderer behavior is intentionally narrow:

```text
validate strict projection
→ map already-resolved values to approved components
→ preserve semantic child cardinality
→ escape/localize
→ render
```

No renderer path may:

- recover historical aliases;
- infer a typo from another field;
- derive Gameplay scoring/completion meaning from Developer data;
- choose scored vs completion-only behavior;
- fill missing semantic content;
- copy reference-project facts.

`gameplay.result_model` explicitly owns result mode/summary. Developer `scoring` or `completion_data` must match that mode.

## Semantic cardinality

Existing approved component families accept data-driven child counts. Preserve every distinct semantic item without filler or destructive merging.

Stable semantic/page questions remain governed by Content/Design contracts; adaptive child counts do not change Golden grammar.

## Golden shell boundary

`template/golden-reference.html` and `template/runtime-template.html` remain byte-identical to the approved reference artifact unless an explicit Golden contract change is approved.

All shell mutation belongs to:

```text
renderer/template_adapter.py
```

`TemplateAdapter` alone may:

- strip retained sample metadata from generated output;
- quarantine retained reference-project storage/spec markers;
- namespace localStorage keys;
- set document language metadata;
- replace sidebar brand/navigation/main content;
- replace glossary assignment;
- bind title/description/specification metadata;
- inject head/body extensions.

Generic renderer modules do not contain or depend on historical reference-project vocabulary.

## PRD-core identity

Stable global pages:

```text
development-overview
shared-systems
shared-data-reset
phase-development
```

Opening flow:

```text
flow-start
```

Package pages:

```text
flow-<package>
dev-<package>-requirement
dev-<package>-level
dev-<package>-developer
```

For `N` gameplay packages the core remains `6 + 4N` pages. 04 pages are additive.

## 04 Production Assets composition

The compositor consumes strict canonical sources:

```text
accepted PRD Owner topology
+ optional work/asset-requirements.md
+ optional work/voice-requirements.md
+ optional work/voice-production.md
→ merge by Owner ID + Moment ID
→ deterministic resource ordering
→ additive 04 pages
```

Identity hierarchy:

```text
Owner ID
→ Moment ID
→ AST-... | VO-...
```

Display titles never perform machine joins.

The compositor embeds exact source bindings when present:

```text
asset-requirements-sha256
voice-requirements-sha256
voice-production-sha256
```

Production Assets presentation assets live under:

```text
renderer/static/production-assets.css
renderer/static/production-assets.js
```

They are inlined into the standalone HTML at render time. Large CSS/JS literals do not belong in Python compositor code.

## One project HTML

`output/v<document.version>/prd.html` remains the single human-facing project document:

```text
01 Overview
02 Gameplay Flow
03 Development
04 Production Assets   # when canonical downstream sources exist
```

04 may not rewrite accepted 01–03 meaning/page identity.

## Versioned delivery

Normal generation:

```bash
python kits/prd-creator/renderer/delivery.py \
  workspace/active/<project>/
```

produces:

```text
output/README.md
output/v<version>/prd.html
output/v<version>/context.md
output/v<version>/index.json
```

Publication is transactional at bundle level:

```text
build complete staged version directory + README
→ verify required staged files are non-empty
→ move current version/README to temporary backup
→ atomically rename staged version directory into place
→ atomically replace README
→ rollback both on any publication failure
```

A failed generation must leave the previous complete delivery intact; mixed old/new version bundles are invalid.

## Bilingual documents

Bilingual projection requires explicit `en` and `id` values. Numeric, percentage, and stable-ID tokens that carry project meaning must remain invariant across languages. Translation may change wording, not counts/values/identity.

## Freshness

Generated HTML binds exact render-data bytes. When non-Voice 04 exists, HTML also binds exact asset requirements bytes. Flow 4 acceptance separately authorizes exact render-data + asset source bytes.

Voice HTML binds exact current requirements + production bytes; final Voice delivery additionally binds exact production bytes in `voice-acceptance.md`.

## Economy

```text
approved meaning
→ one strict projection
→ one deterministic full-file render
→ optional stable-ID 04 composition
→ one transactional delivery publish
```

Do not add page caches, partial renderers, generic registries, compatibility alias layers, second default HTML, or speculative rendering frameworks without a concrete defect.
