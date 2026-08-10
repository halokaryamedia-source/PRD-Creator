# Implementation Map

Updated: 2026-08-10

Use this note to locate the current owner. It is not a task tracker.

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
| Source authority | `docs/knowledge/sources/source-map.md` |
| Review current meaning | `docs/knowledge/reviews/review-graph.md` |
| Anti-overdevelopment engineering boundary | `docs/knowledge/decisions/anti-overdevelopment-simplification.md` |

## Production layer

| Boundary | Current owner |
|---|---|
| End-to-end production sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 Source Intake | `docs/foundation/02-source-intake-recovery.md` + Project Document kit |
| Flow 3 PRD semantics | `docs/foundation/03-prd-generation.md` + `project-document-production` |
| PRD rendering | `kits/project-document-generator/renderer/` + `RENDERING.md` |
| Flow 4 PRD mechanical validation | `kits/project-document-generator/validator/validate.py` |
| PRD focused regression | `tests/test_prd_contracts.py` |
| Flow 5 Voice scope | `docs/foundation/05-voice-requirement-extraction.md` + `voice-production` |
| Flow 6 Voice script semantics | `kits/voice-production-kit/SCRIPT-PRODUCTION.md` + `voice-production` |
| DOCX builder | `kits/voice-production-kit/builder/build_docx.py` |
| Flow 7 Voice mechanical validation | `kits/voice-production-kit/validator/validate.py` |
| Voice focused regression | `tests/test_voice_contracts.py` |
| DOCX presentation rules | `kits/voice-production-kit/DOCX-FORMAT.md` |
| Current production evidence | `docs/foundation/validation-report.md` |

## Repository engineering

```text
requirements.lock.txt
+ tests/
+ tools/
+ .github/workflows/
```

This layer owns the small repeatable CI baseline. It does not own project meaning and must not grow into a parallel production architecture.

## Current derived-artifact rule

```text
canonical input changes
→ regenerate affected derived artifact
→ run focused validation
```

No PRD/Voice checksum or derived-artifact revision registry is part of the normal production contract.

## Project authority chain

```text
source/originals
→ requirement state
→ work/content.md
→ work/render-data.json
→ output/final.html
→ PRD acceptance
→ work/voice-requirements.md
→ work/voice-production.md
→ output/Voice Production.docx
→ Voice acceptance/state
```

Each arrow is a derivation/handoff boundary, not permission for downstream output to overwrite upstream authority.
