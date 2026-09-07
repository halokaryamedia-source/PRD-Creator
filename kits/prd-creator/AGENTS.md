# PRD Creator Kit Agent Rules

Root `AGENTS.md` owns repository mode, continuity, authority, proof, and branch policy. This file owns package-level file/mechanical routing and context economy. Normal Production Execution starts from `SKILL.md`; exact semantic/design schemas stay with their named owners.

## Open the smallest active owner

| Need | Owner |
|---|---|
| Flow 2 source/recovery/approval | `intake/SOURCE-INTAKE.md` |
| PRD semantic completeness | `document/CONTENT-CONTRACT.md` |
| Golden visual/component grammar | `document/DESIGN-CONTRACT.md` |
| Flow 4 acceptance/handoff | `document/VALIDATION.md` |
| non-Voice 04 meaning | `production-assets/CONTRACT.md` |
| renderer/compositor/delivery | `renderer/CONTRACT.md` |
| Flow 5 Voice extraction | `voice/EXTRACTION.md` |
| Flow 6 performance craft | `voice/PERFORMANCE-WRITING.md` |
| Flow 7 validation/delivery | `voice/VALIDATION.md` |
| end-to-end Flow 2–7 routing | `SKILL.md` |

Do not broad-read the kit. Expand only for a material cross-owner dependency.

## Technical ownership

### Shared machine contracts

```text
shared/intake.py
→ strict Flow 2 source / requirement / approval state

shared/state.py
→ duplicate-safe YAML loader + state source-line diagnostics

shared/paths.py
→ safe project-relative persisted path normalization/resolution

shared/handoff.py
→ strict Flow 4 handoff state

shared/acceptance.py
→ shared acceptance field + exact SHA parsing primitives

shared/render_schema.py
→ one supported render-data vocabulary + explicit result model

shared/localization.py
→ language mode + bilingual numeric/unit/dimension/coordinate/negation invariants

shared/assets.py
→ strict Owner ID / Moment ID / AST resource grammar

shared/voice.py
→ strict Flow 5 requirement + Flow 6 production grammar

shared/lifecycle.py
→ one Voice state vocabulary

shared/topology.py
→ accepted 04 Owner topology / page identity

shared/issues.py
→ structured validation/parser issue model
```

Do not create a second parser/schema in a renderer, validator, or doc helper.

### Renderer

```text
renderer/core.py
→ presentation primitives only

renderer/pages.py
→ canonical render-data fields → approved page/component families

renderer/prd_render_engine.py
→ strict deterministic PRD-core composition

renderer/template_adapter.py
→ the only Golden shell mutation / retained reference compatibility owner,
   including additive 04 navigation/pages/head/body injection

renderer/production_assets_compositor.py
→ merge strict Asset + Voice sources by Owner ID + Moment ID

renderer/production_assets.py
→ small 04 presentation helpers / static resource loading

renderer/static/
→ Production Assets CSS/JavaScript inlined at render time

renderer/render.py
→ thin CLI + Golden/reference-shell orchestration

renderer/delivery.py
→ transactional complete-bundle publication + context/index/README
```

### Validators

```text
validator/prd_validation_engine.py
→ PRD source/projection/business-check orchestration

validator/html_contract.py
→ derived HTML freshness/composition/navigation contract

validator/api.py
→ canonical complete PRD validation API + content purity

validator/validate.py
→ thin PRD CLI

validator/validate_handoff.py
→ strict Flow 4→5 state/path/version/exact-acceptance proof

validator/voice_validation.py
→ lifecycle-aware Flow 5→7 Voice revision/identity/HTML/acceptance domain proof

validator/validate_voice.py
→ thin Voice CLI / public validation entrypoint
```

Generic `_engine.py` sibling modules and path-order-dependent internal imports are retired.

## Machine-contract invariants

### Flow 2

```text
requirement-register bytes
→ Simple Chat Preview approval
→ intake-state.approved_requirement_sha256
```

`status` is the only readiness truth. Do not reintroduce `ready_for_prd: true`, `next_step`, or another readiness alias.

### Projection

```text
intake-state.approved_requirement_sha256
+ content.md bytes
→ render-data.approved_requirement_sha256
+ render-data.canonical_content_sha256
→ strict render schema
→ renderer
```

Unknown/legacy projection fields fail. Renderer code does not infer semantic data from another role.

### Result model

```text
gameplay.result_model.mode=scored
↔ developer.scoring

gameplay.result_model.mode=completion_only
↔ developer.completion_data
```

Gameplay summary is explicit upstream; renderer never constructs it from Developer fields. Visible Gameplay/Developer presentation must use the same mode.

### 04 identity

```text
Owner ID
→ Moment ID: MOM-...
→ Asset ID: AST-... | Voice ID: VO-...
```

Display titles never join machine data. A package uses `package:<id>`; `journey:<id>` is reserved for non-package journey nodes.

### Exact acceptance

Flow 4:

```text
Accepted Render Data SHA256
Accepted Asset Requirements SHA256
```

Flow 7 final delivery:

```text
Accepted Voice Production SHA256
```

Semantic version is not an edit counter. Both PRD and Voice acceptance parsing use `shared/acceptance.py`; do not recreate label/SHA regex logic elsewhere.

### Persisted paths

State refs are normalized project-relative POSIX paths. Reject absolute paths, backslashes, `.`/`..`, and workspace escapes.

## Canonical vs derived

```text
approved requirement state
→ work/content.md
→ work/render-data.json
→ output/v<version>/prd.html

optional work/asset-requirements.md
→ same HTML 04

optional Voice requirements / production
→ same HTML 04 AUDIO
```

Generated HTML/context/index are derived. Never hand-patch them to hide an upstream defect.

## Golden boundary

The exact approved Golden bytes and component/page grammar stay protected. Adaptive semantic cardinality is allowed only inside existing approved component families.

Historical reference-project markers are quarantined in `renderer/template_adapter.py`; generic code must not spread them again. Production Assets may append derived 04 content only through `TemplateAdapter`, not by introducing another shell mutator.

## Context economy

```text
smallest owner/source
→ unresolved material dependency?
   no → continue
   yes → open the smallest adjacent owner
→ stop when grounded
```

Do not load the large Golden HTML unless DOM/runtime/visual evidence requires it. Deep Voice references load only for active Voice craft/evidence work.

Structured validation issues should identify code/owner/path/field (and line when available) so a model can repair the smallest scope without rereading unrelated context.

## Bounded technical changes

```text
observe drift
→ identify first wrong semantic/design/technical owner
→ smallest complete correction
→ regenerate invalidated derived output once
→ use the cheapest proof that can falsify the correction
→ stop
```

Do not solve an upstream contract defect with renderer defaults or polished copy.

## Verification routing

Final verification should exercise:

- repository contracts/routing;
- full PRD regression;
- full Voice regression;
- full Local promotion regression;
- Ruff over the maintained Python tree;
- type checking over shared/renderer/validator boundaries;
- coverage reporting;
- browser/audio evidence only when those claims are made.

During broad contract refactors, finish source/docs/fixtures first; run the final verification pass only after the tree is internally coherent.

## Anti-overdevelopment

Do not add databases, generic registries, dependency-injection frameworks, alternate PRD exports, page caches, renderer profiles, scorecard systems, or compatibility alias layers without a concrete product defect.

The desired package is small, explicit, deterministic, easy to test, and hard to misuse.
