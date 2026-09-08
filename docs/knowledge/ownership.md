# Repository Ownership

Updated: 2026-09-08

Use only to answer **who owns what**. Exact field/schema/procedure contracts remain in the named owners; do not duplicate them here.

## Root owners

| Boundary | Owner |
|---|---|
| Work modes, boot, authority, continuity, skill budget | `AGENTS.md` |
| GitHub mutation/history/CI/safety | `GITHUB_RULES.md` |
| Stable repository/product orientation | `CONTEXT.md` |
| Active continuation | `docs/knowledge/next-action.md` |
| Source/state precedence | `docs/knowledge/source-authority.md` |
| Durable decisions/rationale | `docs/knowledge/decisions/` |
| Current validation evidence | `docs/knowledge/reviews/current-validation.md` |

## Product/package owners

| Boundary | Owner |
|---|---|
| Reusable PRD/source/04/readiness semantic judgment | `.agents/skills/project-document-production/SKILL.md` |
| Reusable Voice semantic/performance judgment | `.agents/skills/voice-production/SKILL.md` |
| Package file/mechanical routing | `kits/prd-creator/AGENTS.md` |
| End-to-end Production Execution | `kits/prd-creator/SKILL.md` |
| Flow 2 source/recovery procedure | `kits/prd-creator/intake/SOURCE-INTAKE.md` |
| PRD semantic completeness | `kits/prd-creator/document/CONTENT-CONTRACT.md` |
| Golden page/component grammar | `kits/prd-creator/document/DESIGN-CONTRACT.md` |
| non-Voice 04 contract | `kits/prd-creator/production-assets/CONTRACT.md` |
| Flow 4 acceptance/handoff | `kits/prd-creator/document/VALIDATION.md` |
| Renderer/delivery contract | `kits/prd-creator/renderer/CONTRACT.md` |
| Voice Flow 5 extraction | `kits/prd-creator/voice/EXTRACTION.md` |
| Voice Flow 6 performance craft | `kits/prd-creator/voice/PERFORMANCE-WRITING.md` |
| Voice Flow 7 acceptance/evidence | `kits/prd-creator/voice/VALIDATION.md` |

`CONTENT-CONTRACT.md` owns **what meaning survives**. `DESIGN-CONTRACT.md` owns **how accepted meaning is represented**. Machine schemas do not own product meaning.

## Machine owners

| Boundary | Owner |
|---|---|
| Flow 2 machine state | `kits/prd-creator/shared/intake.py` |
| YAML loading/diagnostics | `kits/prd-creator/shared/state.py` |
| safe persisted paths | `kits/prd-creator/shared/paths.py` |
| acceptance/SHA primitives | `kits/prd-creator/shared/acceptance.py` |
| handoff state | `kits/prd-creator/shared/handoff.py` |
| render-data vocabulary | `kits/prd-creator/shared/render_schema.py` |
| localization invariants | `kits/prd-creator/shared/localization.py` |
| non-Voice 04 identity/parser | `kits/prd-creator/shared/assets.py` |
| Voice identity/parser | `kits/prd-creator/shared/voice.py` |
| Voice lifecycle state | `kits/prd-creator/shared/lifecycle.py` |
| canonical 04 topology | `kits/prd-creator/shared/topology.py` |
| structured validation issues | `kits/prd-creator/shared/issues.py` |

## Renderer / validator owners

| Boundary | Owner |
|---|---|
| reusable HTML primitives | `kits/prd-creator/renderer/core.py` |
| render-data → page families | `kits/prd-creator/renderer/pages.py` |
| deterministic PRD composition | `kits/prd-creator/renderer/prd_render_engine.py` |
| sole Golden shell adapter | `kits/prd-creator/renderer/template_adapter.py` |
| 04 Asset/Voice composition | `kits/prd-creator/renderer/production_assets_compositor.py` |
| Voice presentation formatting | `kits/prd-creator/renderer/production_assets.py` |
| transactional delivery | `kits/prd-creator/renderer/delivery.py` |
| canonical Golden source | `kits/prd-creator/template/golden-reference.html` |
| PRD validation orchestration | `kits/prd-creator/validator/prd_validation_engine.py` |
| derived HTML contract | `kits/prd-creator/validator/html_contract.py` |
| canonical PRD validation API | `kits/prd-creator/validator/api.py` |
| Flow 4→5 proof | `kits/prd-creator/validator/validate_handoff.py` |
| Voice mechanical validation | `kits/prd-creator/validator/voice_validation.py` |
| Voice validation CLI | `kits/prd-creator/validator/validate_voice.py` |

There is one tracked Golden/runtime source: `golden-reference.html`. Do not reintroduce a runtime-template alias.

## Project-package owners

Paths below are relative to an authorized project package.

| Boundary | Owner |
|---|---|
| source identity/provenance | `state/source-inventory.yaml` |
| material requirements | `state/requirement-register.yaml` |
| Flow 2 status/revision binding | `state/intake-state.yaml` |
| canonical PRD meaning | `work/content.md` |
| strict PRD projection | `work/render-data.json` |
| canonical non-Voice 04 resources | `work/asset-requirements.md` |
| PRD/04 acceptance | `work/acceptance.md` |
| PRD handoff state | `state/handoff-state.yaml` |
| canonical Voice requirements | `work/voice-requirements.md` |
| canonical Voice production | `work/voice-production.md` |
| Voice acceptance | `work/voice-acceptance.md` |
| Voice lifecycle state | `state/voice-state.yaml` |
| derived delivery | `output/README.md` + `output/v<document.version>/...` |

Derived output is never hand-patched to reconcile owners. Fix the first wrong canonical/contract owner and regenerate.

## Routing rule

```text
who owns this? → ownership.md
what meaning must exist? → semantic owner
what machine shape is legal? → shared/* owner
how is accepted meaning presented? → DESIGN-CONTRACT / renderer owner
which source outranks another? → source-authority.md
```

Create a new owner only when responsibility is genuinely different. Do not create parallel registries or duplicate schemas for convenience.
