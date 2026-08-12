# Implementation Map

Updated: 2026-08-12

Use this note to locate the **current owner**. It is not a task tracker, review history, or backlog.

## Agent operating layer

| Boundary | Current owner |
|---|---|
| Repository-wide work rules / branch / proof / anti-slop | `AGENTS.md` |
| Stable workspace context | `CONTEXT.md` |
| Active continuation | `docs/knowledge/next-action.md` |
| Developing task contract | `.agents/skills/development-brief/SKILL.md` |
| Plan / Developing / Maintenance routing | `docs/knowledge/flow.md` |
| Maintenance procedure | `docs/knowledge/maintenance/maintenance-flow.md` |
| Root skill routing | `docs/knowledge/skills/activation-matrix.md` |
| Module ownership | `docs/knowledge/modules/module-map.md` |
| Source authority/routing | `docs/knowledge/sources/source-map.md` |
| Review current meaning | `docs/knowledge/reviews/review-graph.md` |
| Anti-overdevelopment engineering boundary | `docs/knowledge/decisions/anti-overdevelopment-simplification.md` |

## PRD production layer

| Boundary | Current owner |
|---|---|
| End-to-end Flow 1–7 sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 durable policy | `docs/foundation/02-source-intake-recovery.md` |
| Flow 2 detailed recovery/preview procedure | `kits/project-document-generator/SOURCE-INTAKE.md` |
| Flow 3 PRD semantic/Golden contract | `kits/project-document-generator/CONTENT-CONTRACT.md` + `project-document-production` |
| PRD rendering / exact Golden binding | `kits/project-document-generator/RENDERING.md` + `renderer/` |
| Flow 4 durable policy | `docs/foundation/04-prd-validation-handoff.md` |
| Flow 4 detailed acceptance/handoff procedure | `kits/project-document-generator/VALIDATION.md` |
| PRD mechanical validation | `kits/project-document-generator/validator/validate.py` |
| PRD handoff consistency | `kits/project-document-generator/validator/validate_handoff.py` |
| PRD focused regressions | `tests/test_prd_*` |
| Current production evidence | `docs/foundation/validation-report.md` |

## Voice production layer

| Boundary | Current owner |
|---|---|
| Flow 5 Voice scope | `docs/foundation/05-voice-requirement-extraction.md` + `voice-production` |
| Flow 6 Voice script semantics | `kits/voice-production-kit/SCRIPT-PRODUCTION.md` + `voice-production` |
| DOCX presentation | `kits/voice-production-kit/DOCX-FORMAT.md` |
| DOCX builder | `kits/voice-production-kit/builder/build_docx.py` |
| Flow 7 Voice validation | `kits/voice-production-kit/validator/validate.py` |
| Voice focused regressions | `tests/test_voice_contracts.py` |

## Repository engineering

```text
requirements.lock.txt
+ tests/
+ tools/
+ .github/workflows/
```

This layer owns the small repeatable CI baseline. It does not own project meaning and must not grow into a parallel production architecture.

## Current Golden/template ownership

```text
CONTENT-CONTRACT.md
→ semantic + visible-composition authority

RENDERING.md
→ deterministic projection/binding contract

template/golden-sample.html
→ canonical approved Golden reference bytes

template/approved-document.html
→ runtime template alias; byte-identical to Golden
```

Do not call the runtime template a generic redesign surface.

## Derived-artifact rule

```text
canonical input changes
→ regenerate affected derived artifact
→ run focused proof required by the changed claim
```

No PRD/Voice checksum registry, derived-artifact revision registry, or repeated unchanged proof cycle is part of normal production.

## Project authority chain

```text
current user instruction + approved decisions + source evidence/provenance
→ requirement state
→ work/content.md
→ work/render-data.json
→ output/final.html
→ PRD acceptance/handoff
→ work/voice-requirements.md
→ work/voice-production.md
→ output/Voice Production.docx
→ Voice acceptance/state
```

A file source may be retained in-repo or externally according to Flow 2 policy. Its storage location does not change authority; current provenance/approval/status do.

Each arrow is a derivation/handoff boundary, not permission for downstream output to overwrite upstream authority.
