# Rendering Contract

`../document/CONTENT-CONTRACT.md` owns PRD meaning. `../document/DESIGN-CONTRACT.md` owns approved page/component grammar. `../production-assets/CONTRACT.md` owns Production Assets meaning. This file owns deterministic projection, Golden-shell adaptation, Production Assets composition, and delivery publication.

## Authority chain

```text
approved Project Requirements revision
+ work/content.md
→ strict work/render-data.json
→ DESIGN-CONTRACT
→ exact Golden shell through TemplateAdapter
→ PRD core HTML
→ optional Production Assets composition through the same TemplateAdapter
→ transactional versioned delivery
```

The renderer may represent accepted data. It may not invent project/resource/Voice meaning.

## Shared machine contracts

```text
intake.py         Project Requirements source/state
state.py          duplicate-safe YAML loading + diagnostics
paths.py          safe persisted paths
handoff.py        strict PRD Handoff state
acceptance.py     acceptance/SHA primitives
render_schema.py  strict render-data vocabulary
localization.py   bilingual invariants
assets.py         Production Assets Owner/Moment/Asset grammar
voice.py          Voice Requirements/Production grammar
lifecycle.py      Voice state vocabulary
topology.py       canonical Production Assets Owner topology
issues.py         structured validation issues
```

## Strict projection

`work/render-data.json` has one supported vocabulary and must bind both current approved Project Requirements bytes and exact current `content.md` bytes through:

```text
approved_requirement_sha256
canonical_content_sha256
```

Renderer behavior:

```text
validate strict projection
→ map already-resolved values to approved components
→ preserve semantic cardinality
→ escape/localize
→ render
```

No renderer path may recover historical aliases, infer missing meaning from another field/role, choose scoring/completion semantics, fill missing semantic content, or copy reference-project facts.

## Golden shell boundary

`template/golden-reference.html` is the single tracked Golden artifact and default runtime source. Only `renderer/template_adapter.py` may mutate the temporary project-specific shell.

`production_assets_compositor.py` may compute/render Production Assets content, but shell mutation still goes through `TemplateAdapter`.

## PRD identity

Stable page IDs, navigation, and Golden component grammar remain unchanged. Generated PRD section numbers are **document ordinals only**. They must never be used as workflow/capability names.

## Production Assets composition

```text
accepted PRD Owner topology
+ optional work/asset-requirements.md
+ optional work/voice-requirements.md
+ optional work/voice-production.md
→ merge by Owner ID + Moment ID
→ deterministic resource ordering
→ Production Assets pages
```

Identity hierarchy:

```text
Owner ID → Moment ID → AST-... | VO-...
```

Display titles never perform machine joins.

The compositor embeds exact source bindings when present:

```text
asset-requirements-sha256
voice-requirements-sha256
voice-production-sha256
```

Preparation may present unresolved Voice selection as `Voice selection pending`. `voice_delivery_ready` must not publish unresolved cast selection/profile.

Production Assets CSS/JavaScript live under `renderer/static/` and are inlined during rendering.

## One project HTML

`output/v<document.version>/prd.html` remains the single human-facing project document. The approved visual navigation may show numbered section ordinals such as Overview, Gameplay Flow, Development, and Production Assets. Those ordinals do not define workflow terminology.

Production Assets may not rewrite accepted PRD-core meaning/page identity.

## Versioned delivery

```bash
python kits/prd-creator/renderer/delivery.py workspace/active/<project>/
```

produces:

```text
output/README.md
output/v<version>/prd.html
output/v<version>/context.md
output/v<version>/index.json
```

Publication is transactional at bundle level. A failed generation must leave the previous complete delivery intact; mixed old/new bundles are invalid.

## Bilingual documents

Bilingual projection requires explicit `en` and `id` values. Numbers, percentages, stable IDs, recognized units, dimensions, coordinates, and material negation must remain aligned across languages.

## Freshness

Generated HTML binds exact Render Data bytes and, when present, exact Production Assets and Voice source bytes. PRD Handoff authorizes exact PRD + Production Assets bytes. Voice Delivery authorizes exact Voice Production bytes.

## Economy

```text
approved meaning
→ one strict projection
→ one deterministic full-file render
→ optional Production Assets composition
→ one transactional delivery publish
```

Do not add page caches, partial renderers, generic registries, compatibility aliases, a second default HTML, or alternate workflow naming layers without a concrete defect.