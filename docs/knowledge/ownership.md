# Repository Ownership

Updated: 2026-08-14

Use this file to locate the current owner before creating, moving, or editing repository structure. It combines area-level ownership and exact implementation/procedure routing so there is only one ownership map.

## Repository Areas

| Area | Responsibility |
|---|---|
| `AGENTS.md` | repository-wide work modes, proof, branch and edit rules |
| `CONTEXT.md` | stable product context and terminology |
| `.agents/skills/` | reusable semantic routing/judgment |
| `docs/foundation/` | durable Flow 1–7 production policy |
| `docs/knowledge/` | current repository memory, ownership, decisions, evidence and operations |
| `kits/project-document-generator/` | Flow 2–4 PRD implementation/procedure + bounded PRD-derived Production Assets requirement/presentation contract |
| `kits/voice-production-kit/` | Flow 5–7 Voice requirements/production/validation semantics and optional DOCX export |
| `tests/`, `tools/`, `.github/workflows/`, `requirements.lock.txt` | repository engineering and repeatable CI contracts |
| `workspace/active/` | current project production packages |
| `workspace/archive/` | inactive retained project packages |

## Operating Owners

| Boundary | Owner |
|---|---|
| Active continuation | `docs/knowledge/next-action.md` |
| Work-mode routing | `docs/knowledge/work-routing.md` |
| Developing workflow | `docs/knowledge/workflows/development.md` |
| Maintenance workflow | `docs/knowledge/workflows/maintenance.md` |
| Root skill routing | `docs/knowledge/skills/activation-matrix.md` |
| Source/state authority | `docs/knowledge/source-authority.md` |
| Review/evidence status | `docs/knowledge/reviews/README.md` |
| Durable decisions | `docs/knowledge/decisions/README.md` + `docs/knowledge/decisions/` |
| Decision-recording policy | `docs/knowledge/decisions/recording-policy.md` |
| Future/non-active work | `docs/knowledge/operations/backlog.md` |

## PRD / Project Delivery Owners

| Boundary | Owner |
|---|---|
| End-to-end PRD production sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 policy | `docs/foundation/02-source-intake-recovery.md` |
| Flow 2 detailed procedure | `kits/project-document-generator/SOURCE-INTAKE.md` |
| Flow 3 PRD + Golden semantic contract | `kits/project-document-generator/CONTENT-CONTRACT.md` |
| non-Voice Production Asset requirement contract | `kits/project-document-generator/PRODUCTION-ASSETS.md` + project `work/asset-requirements.md` |
| PRD-core rendering + shared project HTML composition contract | `kits/project-document-generator/RENDERING.md` |
| versioned delivery orchestration | `kits/project-document-generator/renderer/delivery.py` |
| PRD-core page projection | `kits/project-document-generator/renderer/pages.py` |
| lower-level HTML renderer orchestration | `kits/project-document-generator/renderer/render.py` |
| objective-first Production Assets composition | `kits/project-document-generator/renderer/production_assets_objective.py` |
| Voice-specific Production Assets parsing/presentation primitives | `kits/project-document-generator/renderer/production_assets.py` |
| stable project resume navigator | project `output/README.md` |
| human-facing project PRD | project `output/v<document.version>/prd.html` |
| AI development context projection | project `output/v<document.version>/context.md` |
| AI navigation / context line-range index | project `output/v<document.version>/index.json` |
| Flow 4 policy | `docs/foundation/04-prd-validation-handoff.md` |
| Flow 4 detailed validation/handoff | `kits/project-document-generator/VALIDATION.md` |
| PRD mechanical validator | `kits/project-document-generator/validator/validate.py` |
| PRD handoff consistency | `kits/project-document-generator/validator/validate_handoff.py` |
| PRD/render/delivery/compositor regressions | `tests/test_prd_*` |
| Current system/project evidence | `docs/knowledge/reviews/current-validation.md` |

`PRODUCTION-ASSETS.md` owns only the compact actionable non-Voice requirement contract. `renderer/production_assets_objective.py` owns presentation/composition mechanics and may not invent asset requirements. `renderer/production_assets.py` remains the Voice-specific helper and may not invent Voice scope, scripts, actor selection, or project meaning. `renderer/delivery.py` packages existing accepted meaning into the versioned human/AI handoff surfaces; it is not another semantic owner.

## Voice Owners

| Boundary | Owner |
|---|---|
| Flow 5 Voice Asset Requirement | `kits/voice-production-kit/VOICE-EXTRACTION.md` + project `work/voice-requirements.md` |
| Flow 6 lifecycle/output contract | `kits/voice-production-kit/README.md` + `docs/foundation/06-elevenlabs-script-production.md` |
| Flow 6 canonical Voice Asset Production | project `work/voice-production.md` |
| Eleven v3 performance craft | `kits/voice-production-kit/SOUNDMAKER.md` |
| default human/operator Voice presentation | shared `output/v<document.version>/prd.html → Production Assets → <gameplay section> → Audio → Voice Production` |
| optional DOCX presentation | `kits/voice-production-kit/DOCX-FORMAT.md` |
| optional DOCX builder | `kits/voice-production-kit/builder/build_docx.py` |
| Flow 7 Voice validation | `kits/voice-production-kit/VOICE-VALIDATION.md` + `validator/validate.py` |
| Voice semantic/validator regressions | `tests/test_voice_contracts.py` |
| same-HTML Production Assets/Voice composition regression | `tests/test_prd_voice_assets.py` |

The former duplicate `kits/voice-production-kit/SCRIPT-PRODUCTION.md` owner is retired and must not be used for current routing.

## Shared HTML ownership rule

`output/v<document.version>/prd.html` is one derived human-facing project document with separate canonical owners behind it:

```text
PRD core
← work/content.md + work/render-data.json

Production Assets — non-Voice
← optional work/asset-requirements.md

Production Assets — Voice
← work/voice-production.md
   with Flow 5 Trigger context from work/voice-requirements.md
```

Production Assets extends the accepted PRD sidebar. Gameplay/objective navigation stays under `03 Development`; `04 Production Assets` is additive and does not renumber accepted PRD page identity.

The Production Assets sidebar is objective-first. Categories (`3D Models`, `UI & Information`, `Audio`, `Visual Effects & Presentation`) appear inside matching pages only, and zero-count categories are omitted. Voice is merged into `Audio` for the matching gameplay section without duplicating canonical Voice data or creating a separate Voice sidebar category.

A downstream-only change may rerender the current versioned `prd.html` without changing PRD semantic ownership/acceptance when PRD canonical sources remain unchanged.

Never patch `prd.html`, `context.md`, or `index.json` manually to reconcile owners; fix the canonical source or delivery owner and regenerate the invalidated projection.

## Golden Ownership

```text
CONTENT-CONTRACT.md
→ PRD-core semantic + visible-composition authority

PRODUCTION-ASSETS.md
→ bounded non-Voice Production Asset requirement contract

RENDERING.md
→ deterministic PRD-core binding + downstream composition contract

template/golden-reference.html
→ canonical PRD reference bytes

template/runtime-template.html
→ renderer runtime alias; byte-identical to the reference
```

Production Assets does not modify the Golden template bytes or become part of the PRD-core Golden page family.

## New-Owner Rule

Create a new owner only when an existing owner cannot represent the responsibility without mixing unrelated jobs. Do not create a new map, generic Asset registry/framework, separate asset Flow/Kit, root skill, schema, or compatibility layer solely because a current filename is inconvenient.
