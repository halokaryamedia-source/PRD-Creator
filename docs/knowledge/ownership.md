# Repository Ownership

Updated: 2026-08-13

Use this file to locate the current owner before creating, moving, or editing repository structure. It combines area-level ownership and exact implementation/procedure routing so there is only one ownership map.

## Repository Areas

| Area | Responsibility |
|---|---|
| `AGENTS.md` | repository-wide work modes, proof, branch and edit rules |
| `CONTEXT.md` | stable product context and terminology |
| `.agents/skills/` | reusable semantic routing/judgment |
| `docs/foundation/` | durable Flow 1–7 production policy |
| `docs/knowledge/` | current repository memory, ownership, decisions, evidence and operations |
| `kits/project-document-generator/` | Flow 2–4 PRD implementation/procedure + mechanical composition of accepted downstream Production Assets into shared project HTML |
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
| Durable decisions | `docs/knowledge/decisions/README.md` |
| Decision-recording policy | `docs/knowledge/decisions/recording-policy.md` |
| Future/non-active work | `docs/knowledge/operations/backlog.md` |

## PRD / Project HTML Owners

| Boundary | Owner |
|---|---|
| End-to-end PRD production sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 policy | `docs/foundation/02-source-intake-recovery.md` |
| Flow 2 detailed procedure | `kits/project-document-generator/SOURCE-INTAKE.md` |
| Flow 3 PRD + Golden semantic contract | `kits/project-document-generator/CONTENT-CONTRACT.md` |
| PRD-core rendering + shared project HTML composition contract | `kits/project-document-generator/RENDERING.md` |
| PRD-core page projection | `kits/project-document-generator/renderer/pages.py` |
| renderer orchestration | `kits/project-document-generator/renderer/render.py` |
| downstream Production Assets presentation mechanics | `kits/project-document-generator/renderer/production_assets.py` |
| Flow 4 policy | `docs/foundation/04-prd-validation-handoff.md` |
| Flow 4 detailed validation/handoff | `kits/project-document-generator/VALIDATION.md` |
| PRD mechanical validator | `kits/project-document-generator/validator/validate.py` |
| PRD handoff consistency | `kits/project-document-generator/validator/validate_handoff.py` |
| PRD/render/compositor regressions | `tests/test_prd_*` |
| Current system/project evidence | `docs/knowledge/reviews/current-validation.md` |

`renderer/production_assets.py` owns presentation mechanics only. It may not invent Voice/SFX/Visual requirements, scripts, actor selection, or project meaning.

## Voice Owners

| Boundary | Owner |
|---|---|
| Flow 5 Voice Asset Requirement | `kits/voice-production-kit/VOICE-EXTRACTION.md` + `work/voice-requirements.md` |
| Flow 6 canonical Voice Asset Production | `kits/voice-production-kit/SCRIPT-PRODUCTION.md` + `work/voice-production.md` |
| Eleven v3 performance craft | `kits/voice-production-kit/SOUNDMAKER.md` |
| default human/operator Voice presentation | shared `output/final.html → Production Assets → Voice`, mechanically composed by PRD renderer from canonical Voice Production |
| optional DOCX presentation | `kits/voice-production-kit/DOCX-FORMAT.md` |
| optional DOCX builder | `kits/voice-production-kit/builder/build_docx.py` |
| Flow 7 Voice validation | `kits/voice-production-kit/VOICE-VALIDATION.md` + `validator/validate.py` |
| Voice semantic/validator regressions | `tests/test_voice_contracts.py` |
| same-HTML Voice composition regression | `tests/test_prd_voice_assets.py` |

## Shared HTML ownership rule

`output/final.html` is one derived human-facing project document with separate canonical owners behind it:

```text
PRD core
← work/content.md + work/render-data.json

Production Assets → Voice
← work/voice-production.md
```

A downstream Voice-only change may rerender `final.html` without changing PRD semantic ownership/acceptance when PRD canonical sources remain unchanged.

Never patch `final.html` manually to reconcile owners.

## Golden Ownership

```text
CONTENT-CONTRACT.md
→ PRD-core semantic + visible-composition authority

RENDERING.md
→ deterministic PRD-core binding + downstream composition contract

template/golden-reference.html
→ canonical PRD reference bytes

template/runtime-template.html
→ renderer runtime alias; byte-identical to the reference
```

Production Assets does not modify the Golden template bytes or become part of the PRD-core Golden page family.

## New-Owner Rule

Create a new owner only when an existing owner cannot represent the responsibility without mixing unrelated jobs. Do not create a new map, generic Asset registry/framework, skill, schema, or compatibility layer solely because a current filename is inconvenient.
