# Repository Ownership

Updated: 2026-09-07

Use this file only to answer **who owns what**. Exact field/schema/procedure contracts remain in the named owners; do not duplicate them here.

## Root operating owners

| Boundary | Owner |
|---|---|
| Top-level boot, work modes, continuity, authority, skill budget | `AGENTS.md` |
| GitHub branch/ref, write/history, CI/API/safety | `GITHUB_RULES.md` |
| Stable repository/product orientation | `CONTEXT.md` |
| Contribution and promotion procedure | `CONTRIBUTING.md` |
| Public-repository data handling | `SECURITY.md` |
| Active continuation | `docs/knowledge/next-action.md` |
| Source/state precedence | `docs/knowledge/source-authority.md` |
| Current validation evidence | `docs/knowledge/reviews/current-validation.md` |
| Durable decisions/rationale | `docs/knowledge/decisions/` |
| Future/non-active work | `docs/knowledge/operations/backlog.md` |

## Repository areas

| Area | Responsibility |
|---|---|
| `.agents/skills/` | reusable semantic judgment |
| `docs/foundation/` | durable Flow 1–7 policy |
| `docs/knowledge/` | continuation, routing, ownership, decisions, evidence |
| `kits/prd-creator/` | Flow 2–7 procedure and implementation |
| `tests/`, `tools/`, `.github/`, dependency locks | engineering verification and promotion |
| `workspace/active/`, `workspace/archive/` | ignored local/external project-package mount points |

The public repository owns workspace guidance, not live project-package contents.

## Package root owners

| Boundary | Owner |
|---|---|
| Package orientation / architecture map | `kits/prd-creator/README.md` |
| Package technical/file routing | `kits/prd-creator/AGENTS.md` |
| End-to-end Flow 2–7 execution router | `kits/prd-creator/SKILL.md` |

## Semantic / design / procedure owners

| Boundary | Owner |
|---|---|
| Reusable source/PRD/04/readiness semantic judgment | `.agents/skills/project-document-production/SKILL.md` |
| End-to-end production sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 durable policy | `docs/foundation/02-source-intake-recovery.md` |
| Flow 2 exact procedure/state contract | `kits/prd-creator/intake/SOURCE-INTAKE.md` |
| PRD-core semantic completeness + Material Conservation | `kits/prd-creator/document/CONTENT-CONTRACT.md` |
| Golden page/component grammar | `kits/prd-creator/document/DESIGN-CONTRACT.md` |
| non-Voice 04 exact resource contract | `kits/prd-creator/production-assets/CONTRACT.md` |
| Flow 4 durable policy | `docs/foundation/04-prd-validation-handoff.md` |
| Flow 4 acceptance/handoff procedure | `kits/prd-creator/document/VALIDATION.md` |
| Flow 5 Voice extraction | `kits/prd-creator/voice/EXTRACTION.md` |
| Flow 6 Eleven v3 craft | `kits/prd-creator/voice/PERFORMANCE-WRITING.md` |
| Flow 7 acceptance/evidence | `kits/prd-creator/voice/VALIDATION.md` |

`CONTENT-CONTRACT.md` owns **what meaning survives**. `DESIGN-CONTRACT.md` owns **where/how accepted meaning is presented**. Machine schemas do not own product meaning.

## Shared machine-contract owners

| Boundary | Owner |
|---|---|
| duplicate-safe YAML loading + YAML source-line diagnostics | `kits/prd-creator/shared/state.py` |
| strict Flow 2 source/requirement/intake state + approval hash | `kits/prd-creator/shared/intake.py` |
| normalized project-relative path safety | `kits/prd-creator/shared/paths.py` |
| strict handoff-state shape | `kits/prd-creator/shared/handoff.py` |
| strict Voice lifecycle-state shape | `kits/prd-creator/shared/lifecycle.py` |
| canonical render-data whitelist schema | `kits/prd-creator/shared/render_schema.py` |
| bilingual presence + numeric/unit/dimension/coordinate/negation parity | `kits/prd-creator/shared/localization.py` |
| stable non-Voice 04 parsing (`Owner → Moment → AST`) | `kits/prd-creator/shared/assets.py` |
| stable Voice requirement/production parsing (`Owner → Moment → VO`) | `kits/prd-creator/shared/voice.py` |
| canonical PRD owner topology | `kits/prd-creator/shared/topology.py` |
| structured machine issues/source diagnostics | `kits/prd-creator/shared/issues.py` |
| shared acceptance-field and exact-SHA parsing primitives | `kits/prd-creator/shared/acceptance.py` |

These modules centralize machine behavior only. They never outrank canonical project sources.

## Renderer owners

| Boundary | Owner |
|---|---|
| PRD/04 projection contract | `kits/prd-creator/renderer/CONTRACT.md` |
| transactional version-directory delivery + rollback | `kits/prd-creator/renderer/delivery.py` |
| PRD page projection / adaptive cardinality | `kits/prd-creator/renderer/pages.py` |
| renderer CLI / orchestration | `kits/prd-creator/renderer/render.py` |
| lower-level deterministic PRD engine | `kits/prd-creator/renderer/prd_render_engine.py` |
| reusable HTML primitives | `kits/prd-creator/renderer/core.py` |
| sole Golden-shell mutation/reference adapter, including additive 04 injection | `kits/prd-creator/renderer/template_adapter.py` |
| stable Owner/Moment/Resource 04 composition | `kits/prd-creator/renderer/production_assets_compositor.py` |
| Voice presentation formatting | `kits/prd-creator/renderer/production_assets.py` |
| 04 static presentation resources | `kits/prd-creator/renderer/static/` |
| canonical Golden bytes | `kits/prd-creator/template/golden-reference.html` |
| byte-identical runtime Golden alias | `kits/prd-creator/template/runtime-template.html` |

Reference-project/Golden compatibility vocabulary belongs only in `TemplateAdapter`, not generic business logic.

## Validator owners

| Boundary | Owner |
|---|---|
| PRD source/projection validation orchestration | `kits/prd-creator/validator/prd_validation_engine.py` |
| derived PRD HTML freshness/composition/navigation contract | `kits/prd-creator/validator/html_contract.py` |
| one canonical complete PRD validation API | `kits/prd-creator/validator/api.py` |
| PRD validation CLI | `kits/prd-creator/validator/validate.py` |
| PRD → Voice handoff + exact render/asset acceptance bindings | `kits/prd-creator/validator/validate_handoff.py` |
| Flow 5–7 lifecycle / exact Voice source and acceptance domain validation | `kits/prd-creator/validator/voice_validation.py` |
| Voice validation CLI / public entrypoint | `kits/prd-creator/validator/validate_voice.py` |
| PRD regressions | `tests/test_prd_*` |
| Voice regressions | `tests/test_voice_contracts.py` |

Generic `_engine.py` module names and title-based machine joins are retired.

## Project-package owners

Paths below are relative to an authorized project package.

| Boundary | Owner |
|---|---|
| source identity/provenance | `state/source-inventory.yaml` |
| recovered/approved requirements | `state/requirement-register.yaml` |
| Flow 2 status + exact approved requirement SHA | `state/intake-state.yaml` |
| canonical PRD-core meaning | `work/content.md` |
| strict derived PRD projection + exact Flow 2/content SHA bindings | `work/render-data.json` |
| canonical non-Voice 04 `Owner → Moment → AST` resources | `work/asset-requirements.md` |
| PRD/04 acceptance + exact render-data/asset SHA bindings | `work/acceptance.md` |
| PRD handoff refs/status | `state/handoff-state.yaml` |
| canonical Voice `Owner → Moment → VO` requirements | `work/voice-requirements.md` |
| canonical Voice wording/performance + exact requirement SHA | `work/voice-production.md` |
| exact Voice Production acceptance | `work/voice-acceptance.md` |
| Voice lifecycle refs/status | `state/voice-state.yaml` |
| stable resume navigator | `output/README.md` |
| human-facing consolidated document | `output/v<document.version>/prd.html` |
| AI development-context projection | `output/v<document.version>/context.md` |
| compact AI navigation/line-range index | `output/v<document.version>/index.json` |

Derived output is never hand-patched to reconcile owners. Fix the first wrong canonical/contract owner and regenerate.

## Routing rule

```text
Who owns this?
→ ownership.md

What meaning must exist?
→ semantic owner

What machine shape is legal?
→ shared/* exact machine owner

How is accepted meaning presented?
→ DESIGN-CONTRACT / renderer owner

Which source/state outranks another?
→ source-authority.md
```

Create a new owner only when responsibility is genuinely different. Do not create parallel registries or duplicate schemas for convenience.
