# Repository Ownership

Updated: 2026-08-30

Use this file only to answer **who owns what**. It maps responsibilities to current owners/paths; it does not duplicate the detailed contracts inside those owners.

## Root operating owners

| Boundary | Owner |
|---|---|
| Top-level boot, work modes, continuity behavior, authority and skill budget | `AGENTS.md` |
| GitHub branch/ref, tool fit, write/commit/history, CI/API/safety and STOP discipline | `GITHUB_RULES.md` |
| Stable product/repository orientation | `CONTEXT.md` |
| Active continuation / resume checkpoint | `docs/knowledge/next-action.md` |
| Detailed work-routing explanation | `docs/knowledge/work-routing.md` |
| Developing lifecycle overview | `docs/knowledge/work-modes/development.md` |
| Canonical non-trivial Developing procedure | `.agents/skills/development-brief/SKILL.md` |
| Maintenance procedure | `docs/knowledge/work-modes/maintenance.md` |
| Ambiguous specialist selection | `docs/knowledge/skills/activation-matrix.md` |
| Source/state precedence | `docs/knowledge/source-authority.md` |
| Review/evidence current interpretation | `docs/knowledge/reviews/README.md` |
| Current validation evidence | `docs/knowledge/reviews/current-validation.md` |
| Historical review evidence | `docs/knowledge/reviews/history/` |
| Durable decisions/rationale | `docs/knowledge/decisions/README.md` + `docs/knowledge/decisions/` |
| Decision-recording threshold | `docs/knowledge/decisions/recording-policy.md` |
| Future/non-active work | `docs/knowledge/operations/backlog.md` |

## Repository areas

| Area | Responsibility |
|---|---|
| `.agents/skills/` | reusable semantic judgment |
| `docs/foundation/` | durable Flow 1–7 production policy |
| `docs/knowledge/` | continuity, routing, ownership, decisions, evidence, backlog |
| `kits/prd-creator/` | categorized Flow 2–7 + bounded 04 procedure/implementation |
| `tests/`, `tools/`, `.github/workflows/`, `requirements.lock.txt` | repository engineering / repeatable verification |
| `workspace/active/` | current project packages |
| `workspace/archive/` | inactive retained project packages |

## Unified package root owners

| Boundary | Owner |
|---|---|
| Package orientation + Requirement Map | `kits/prd-creator/README.md` |
| Package technical/file routing | `kits/prd-creator/AGENTS.md` |
| End-to-end Flow 2–7 Production Execution router | `kits/prd-creator/SKILL.md` |

## PRD semantic and procedure owners

| Boundary | Owner |
|---|---|
| Reusable PRD/source/04/readiness semantic judgment | `.agents/skills/project-document-production/SKILL.md` |
| End-to-end production sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 durable policy | `docs/foundation/02-source-intake-recovery.md` |
| Flow 2 detailed procedure | `kits/prd-creator/intake/SOURCE-INTAKE.md` |
| PRD-core 01–03 exact semantic/visible-composition contract | `kits/prd-creator/document/CONTENT-CONTRACT.md` |
| non-Voice 04 exact resource/writing/readiness contract | `kits/prd-creator/production-assets/CONTRACT.md` |
| Flow 4 durable policy | `docs/foundation/04-prd-validation-handoff.md` |
| Flow 4 detailed validation/handoff procedure | `kits/prd-creator/document/VALIDATION.md` |

## PRD implementation owners

| Boundary | Owner |
|---|---|
| PRD-core rendering + shared project HTML composition contract | `kits/prd-creator/renderer/CONTRACT.md` |
| versioned delivery orchestration | `kits/prd-creator/renderer/delivery.py` |
| PRD-core page projection | `kits/prd-creator/renderer/pages.py` |
| lower-level HTML renderer orchestration | `kits/prd-creator/renderer/render.py` |
| reusable renderer primitives | `kits/prd-creator/renderer/core.py` |
| shared objective/moment-first 04 compositor | `kits/prd-creator/renderer/production_assets_compositor.py` |
| Voice-specific 04 parsing/presentation primitives | `kits/prd-creator/renderer/production_assets.py` |
| canonical Golden bytes | `kits/prd-creator/template/golden-reference.html` |
| runtime Golden alias | `kits/prd-creator/template/runtime-template.html` |
| PRD mechanical validation | `kits/prd-creator/validator/_engine.py` + `kits/prd-creator/validator/validate.py` |
| PRD → Voice handoff consistency | `kits/prd-creator/validator/validate_handoff.py` |
| PRD/render/delivery/compositor regressions | `tests/test_prd_*` |

## Voice owners

| Boundary | Owner |
|---|---|
| Reusable Voice semantic judgment | `.agents/skills/voice-production/SKILL.md` |
| Flow 5 durable policy | `docs/foundation/05-voice-requirement-extraction.md` |
| Flow 5 detailed extraction procedure | `kits/prd-creator/voice/EXTRACTION.md` |
| Flow 6 durable policy | `docs/foundation/06-elevenlabs-script-production.md` |
| Eleven v3 performance-writing craft | `kits/prd-creator/voice/SOUNDMAKER.md` |
| Flow 7 durable policy | `docs/foundation/07-voice-validation-delivery.md` |
| Flow 7 detailed validation/evidence procedure | `kits/prd-creator/voice/VALIDATION.md` |
| Voice mechanical validation | `kits/prd-creator/validator/validate_voice.py` |
| Voice semantic/validator regressions | `tests/test_voice_contracts.py` |
| mixed Voice/non-Voice 04 composition regression | `tests/test_prd_voice_assets.py` |

## Project package owners

| Boundary | Owner |
|---|---|
| source/provenance + requirement state | project `state/` owners |
| canonical PRD-core meaning | project `work/content.md` |
| derived PRD-core projection | project `work/render-data.json` |
| canonical non-Voice 04 requirements when present | project `work/asset-requirements.md` under `kits/prd-creator/production-assets/CONTRACT.md` |
| PRD acceptance | project `work/acceptance.md` |
| PRD handoff state | project `state/handoff-state.yaml` |
| canonical Voice requirements | project `work/voice-requirements.md` |
| canonical Voice production | project `work/voice-production.md` |
| Voice acceptance/state | project `work/voice-acceptance.md` + `state/voice-state.yaml` |
| stable handoff/resume navigator | project `output/README.md` |
| human-facing project document | project `output/v<document.version>/prd.html` |
| AI development-context projection | project `output/v<document.version>/context.md` |
| compact AI navigation/line-range index | project `output/v<document.version>/index.json` |

Derived delivery artifacts are never manually patched to reconcile owners; fix the canonical owner and regenerate.

## Ownership questions vs contract questions

```text
Who owns this?
→ ownership.md

What exactly must this owner produce/accept?
→ open the owner named here

Which source/state outranks another?
→ source-authority.md
```

Do not copy exact resource fields, presentation schemas, Golden checklists, Voice line formats, or validation matrices into this ownership map.

## New-owner rule

Create a new owner only when an existing owner cannot represent the responsibility without mixing unrelated jobs. Do not create a new map, generic asset registry/framework, Flow/Kit, root skill, schema, compatibility layer, or workflow solely because a current filename is inconvenient.
