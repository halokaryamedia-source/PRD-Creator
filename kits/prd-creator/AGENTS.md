# PRD Creator Kit Agent Rules

Root `AGENTS.md` owns repository routing, authority, continuity, branch policy, and proof boundaries. This file owns package-level file/mechanical routing and context economy. Normal Production Execution starts from `SKILL.md`.

## Open the smallest owner

| Need | Owner |
|---|---|
| Flow 2 source/recovery/conditional approval | `intake/SOURCE-INTAKE.md` |
| PRD semantic completeness | `document/CONTENT-CONTRACT.md` |
| Golden visual/component grammar | `document/DESIGN-CONTRACT.md` |
| Flow 4 acceptance/handoff | `document/VALIDATION.md` |
| non-Voice 04 meaning | `production-assets/CONTRACT.md` |
| renderer/compositor/delivery | `renderer/CONTRACT.md` |
| Flow 5 Voice extraction | `voice/EXTRACTION.md` |
| Flow 6 performance craft | `voice/PERFORMANCE-WRITING.md` |
| Flow 7 validation/delivery | `voice/VALIDATION.md` |
| end-to-end Flow 2–7 | `SKILL.md` |

Do not broad-read the kit. Open an adjacent owner only when an unresolved dependency can change the decision.

## Technical ownership

```text
shared/intake.py          Flow 2 machine state
shared/state.py           strict YAML loading + diagnostics
shared/paths.py           safe project-relative paths
shared/acceptance.py      exact acceptance/SHA primitives
shared/handoff.py         minimal handoff state
shared/render_schema.py   one render-data vocabulary
shared/localization.py    language/numeric invariants
shared/assets.py          Owner/Moment/Asset grammar
shared/voice.py           Flow 5/6 Voice grammar
shared/lifecycle.py       Voice state vocabulary
shared/topology.py        accepted 04 topology
shared/issues.py          structured validation issues

renderer/core.py                     presentation primitives
renderer/pages.py                    render-data → approved page families
renderer/prd_render_engine.py        deterministic PRD composition
renderer/template_adapter.py         only Golden shell mutation owner
renderer/production_assets_compositor.py  04 Asset/Voice merge
renderer/delivery.py                 transactional versioned delivery
renderer/render.py                   thin CLI/orchestration

validator/prd_validation_engine.py   PRD validation orchestration
validator/html_contract.py           derived HTML contract
validator/api.py                     canonical PRD validation API
validator/validate_handoff.py        Flow 4→5 proof
validator/voice_validation.py        Flow 5→7 proof
validator/validate.py                thin PRD CLI
validator/validate_voice.py          thin Voice CLI
```

Do not create a second parser/schema/acceptance implementation inside renderer, validator, or helpers.

## Machine invariants

### Flow 2

```text
requirement-register bytes
→ material Proposal exists?
   yes → review/approval required
   no  → continue
→ intake-state.approved_requirement_sha256
```

`status` is readiness truth. `preview_approved` is conditional evidence only; do not add readiness aliases.

### Projection

```text
approved requirement SHA
+ canonical content SHA
→ strict render schema
→ deterministic renderer
```

Unknown/legacy projection fields fail. Renderer never reconstructs missing semantics.

### Result model

```text
result_model.mode=scored          ↔ developer.scoring
result_model.mode=completion_only ↔ developer.completion_data
```

Gameplay and Developer presentation must agree on the same mode.

### 04 identity

```text
Owner ID → MOM-... → AST-... | VO-...
```

Display titles never join machine data.

### Acceptance and handoff

Flow 4 binds exact current Render Data and optional Asset Requirement SHA. Final Voice delivery binds exact Voice Production SHA.

Handoff state stays:

```yaml
status: handoff_ready
accepted_prd_version: X.Y.Z
```

Deterministic artifact paths are derived, not persisted as duplicate state.

### Paths

Persisted project paths are normalized project-relative POSIX refs. Reject absolute paths, backslashes, `.`/`..`, and workspace escapes.

## Canonical vs derived

```text
Flow 2 state
→ work/content.md
→ work/render-data.json
→ output/v<version>/prd.html

optional work/asset-requirements.md → same HTML 04
optional Voice sources             → same HTML 04 AUDIO
```

Generated HTML/context/index are derived. Repair upstream owners and regenerate instead of hand-patching output.

## Golden boundary

Approved Golden bytes and page/component grammar remain protected. Adaptive cardinality is allowed only inside approved component families. Historical reference-project markers stay quarantined in `renderer/template_adapter.py`.

Do not load the large Golden HTML unless DOM/runtime/visual evidence is materially required.

## Bounded technical change

```text
observe failure
→ first wrong owner
→ smallest complete correction
→ regenerate invalidated derived output once
→ cheapest proof that can falsify the correction
→ STOP
```

Structured failures should expose code/owner/path/field/line when available so repair stays narrow.

## Verification

During iteration use `tools/prd.py impact` and only affected proof domains. Final integration/promotion retains repository checks, full PRD + Voice regression, Ruff, type checking, coverage, and browser/audio evidence when claimed or required by the gate.

## Anti-overdevelopment

Do not add databases, dependency-injection frameworks, alternate PRD exports, caches, generic registries, renderer profiles, scorecards, or compatibility layers without a concrete product defect.

The desired package is explicit, deterministic, testable, and hard to misuse.