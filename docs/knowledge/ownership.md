# Repository Ownership

Updated: 2026-09-07

Use this file only to answer **who owns what**. Exact contracts remain in the named owners.

## Root operating owners

| Boundary | Owner |
|---|---|
| Top-level boot, work modes, continuity, authority, skill budget | `AGENTS.md` |
| GitHub branch/ref, tool fit, write/commit/history, CI/API/safety | `GITHUB_RULES.md` |
| Stable product/repository orientation | `CONTEXT.md` |
| Contribution + branch-promotion procedure | `CONTRIBUTING.md` |
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
| `docs/foundation/` | durable Flow 1–7 production policy |
| `docs/knowledge/` | continuity, routing, ownership, decisions, evidence, backlog |
| `kits/prd-creator/` | categorized Flow 2–7 + bounded 04 procedure/implementation |
| `tests/`, `tools/`, `.github/`, `requirements.lock.txt` | repository engineering / verification / promotion gates |
| `workspace/active/` | ignored local/external current project-package mount point |
| `workspace/archive/` | ignored local/external retained project-package mount point |

The public system repository owns workspace guidance, not live project-package contents.

## Unified package root owners

| Boundary | Owner |
|---|---|
| Package orientation + Requirement Map | `kits/prd-creator/README.md` |
| Package technical/file routing | `kits/prd-creator/AGENTS.md` |
| End-to-end Flow 2–7 execution router | `kits/prd-creator/SKILL.md` |

## PRD semantic / design / procedure owners

| Boundary | Owner |
|---|---|
| Reusable PRD/source/04/readiness semantic judgment | `.agents/skills/project-document-production/SKILL.md` |
| End-to-end production sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 durable policy | `docs/foundation/02-source-intake-recovery.md` |
| Flow 2 detailed procedure | `kits/prd-creator/intake/SOURCE-INTAKE.md` |
| PRD-core 01–03 semantic completeness + material conservation | `kits/prd-creator/document/CONTENT-CONTRACT.md` |
| PRD-core 01–03 Golden page/component design grammar | `kits/prd-creator/document/DESIGN-CONTRACT.md` |
| non-Voice 04 exact contract | `kits/prd-creator/production-assets/CONTRACT.md` |
| Flow 4 durable policy | `docs/foundation/04-prd-validation-handoff.md` |
| Flow 4 validation/handoff | `kits/prd-creator/document/VALIDATION.md` |

`CONTENT-CONTRACT.md` answers **what meaning must survive**. `DESIGN-CONTRACT.md` answers **where/how accepted meaning is presented**. Sample card/step counts do not become semantic ownership merely because the Golden example contains them.

## PRD implementation owners

| Boundary | Owner |
|---|---|
| PRD-core + shared HTML projection contract | `kits/prd-creator/renderer/CONTRACT.md` |
| versioned delivery orchestration | `kits/prd-creator/renderer/delivery.py` |
| PRD-core page projection / adaptive child cardinality | `kits/prd-creator/renderer/pages.py` |
| lower-level HTML renderer | `kits/prd-creator/renderer/render.py` + `kits/prd-creator/renderer/_engine.py` |
| reusable renderer primitives | `kits/prd-creator/renderer/core.py` |
| shared 04 compositor | `kits/prd-creator/renderer/production_assets_compositor.py` |
| Voice-specific 04 presentation primitives | `kits/prd-creator/renderer/production_assets.py` |
| canonical Golden bytes | `kits/prd-creator/template/golden-reference.html` |
| runtime Golden alias | `kits/prd-creator/template/runtime-template.html` |
| PRD mechanical validation | `kits/prd-creator/validator/_engine.py` + `kits/prd-creator/validator/validate.py` |
| PRD → Voice handoff consistency | `kits/prd-creator/validator/validate_handoff.py` |
| PRD regressions | `tests/test_prd_*` |

## Voice owners

| Boundary | Owner |
|---|---|
| Reusable Voice semantic judgment | `.agents/skills/voice-production/SKILL.md` |
| Flow 5 extraction | `kits/prd-creator/voice/EXTRACTION.md` |
| Flow 6 durable policy | `docs/foundation/06-elevenlabs-script-production.md` |
| Eleven v3 performance craft | `kits/prd-creator/voice/PERFORMANCE-WRITING.md` |
| Flow 7 validation/evidence | `kits/prd-creator/voice/VALIDATION.md` |
| Voice mechanical validation | `kits/prd-creator/validator/validate_voice.py` |
| Voice regressions | `tests/test_voice_contracts.py` |

## Project package owners

Paths below are relative to the authorized active project package:

| Boundary | Owner |
|---|---|
| source/provenance + requirement state | project `state/` owners |
| canonical PRD-core meaning | `work/content.md` |
| derived PRD-core projection | `work/render-data.json` |
| canonical non-Voice 04 requirements | `work/asset-requirements.md` |
| PRD acceptance | `work/acceptance.md` |
| PRD handoff state | `state/handoff-state.yaml` |
| canonical Voice requirements | `work/voice-requirements.md` |
| canonical Voice production | `work/voice-production.md` |
| Voice acceptance/state | `work/voice-acceptance.md` + `state/voice-state.yaml` |
| stable handoff/resume navigator | `output/README.md` |
| human-facing project document | `output/v<document.version>/prd.html` |
| AI development-context projection | `output/v<document.version>/context.md` |
| compact AI navigation/line-range index | `output/v<document.version>/index.json` |

Derived delivery is never manually patched to reconcile owners; fix the canonical/contract owner and regenerate.

## Ownership questions vs contract questions

```text
Who owns this?
→ ownership.md

What meaning must be present?
→ CONTENT-CONTRACT / matching semantic owner

How must it be presented?
→ DESIGN-CONTRACT / renderer contract

Which source/state outranks another?
→ source-authority.md
```

## New-owner rule

Create a new owner only when the responsibilities are genuinely different. `DESIGN-CONTRACT.md` exists because semantic completeness and approved presentation grammar require independent change/review boundaries; it is not a second PRD, schema, registry, or workflow.
