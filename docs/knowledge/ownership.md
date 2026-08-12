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
| `kits/project-document-generator/` | Flow 2–4 PRD implementation/procedure |
| `kits/voice-production-kit/` | Flow 5–7 Voice implementation/procedure |
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

## PRD Owners

| Boundary | Owner |
|---|---|
| End-to-end production sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 policy | `docs/foundation/02-source-intake-recovery.md` |
| Flow 2 detailed procedure | `kits/project-document-generator/SOURCE-INTAKE.md` |
| Flow 3 PRD + Golden contract | `kits/project-document-generator/CONTENT-CONTRACT.md` |
| PRD rendering | `kits/project-document-generator/RENDERING.md` + `renderer/` |
| Flow 4 policy | `docs/foundation/04-prd-validation-handoff.md` |
| Flow 4 detailed validation/handoff | `kits/project-document-generator/VALIDATION.md` |
| PRD mechanical validator | `kits/project-document-generator/validator/validate.py` |
| PRD handoff consistency | `kits/project-document-generator/validator/validate_handoff.py` |
| PRD regressions | `tests/test_prd_*` |
| Current system/project evidence | `docs/knowledge/reviews/current-validation.md` |

## Voice Owners

| Boundary | Owner |
|---|---|
| Flow 5 Voice extraction | `kits/voice-production-kit/VOICE-EXTRACTION.md` |
| Flow 6 performance wording | `kits/voice-production-kit/SCRIPT-PRODUCTION.md` |
| DOCX presentation | `kits/voice-production-kit/DOCX-FORMAT.md` |
| DOCX builder | `kits/voice-production-kit/builder/build_docx.py` |
| Flow 7 Voice validation | `kits/voice-production-kit/VOICE-VALIDATION.md` + `validator/validate.py` |
| Voice regressions | `tests/test_voice_contracts.py` |

## Golden Ownership

```text
CONTENT-CONTRACT.md
→ semantic + visible-composition authority

RENDERING.md
→ deterministic binding contract

template/golden-reference.html
→ canonical reference bytes

template/runtime-template.html
→ renderer runtime alias; byte-identical to the reference
```

## New-Owner Rule

Create a new owner only when an existing owner cannot represent the responsibility without mixing unrelated jobs. Do not create a new map, registry, skill, schema, or compatibility layer solely because a current filename is inconvenient.
