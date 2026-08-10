# Implementation Map

Updated: 2026-08-10

Use this note to answer where current behavior/policy lives. It is not the active task tracker.

## Agent Operating Layer

| Boundary | Current owner |
|---|---|
| Repository-wide rules / branch policy / authority / work modes / proof | `AGENTS.md` |
| Stable product context / terminology | `CONTEXT.md` |
| Agent Plan / Developing / Maintenance routing | `docs/knowledge/flow.md` |
| Developing task contract | `.agents/skills/development-brief/SKILL.md` + `docs/knowledge/flows/development-flow.md` |
| Maintenance workflow | `docs/knowledge/maintenance/maintenance-flow.md` |
| Root skill routing | `docs/knowledge/skills/activation-matrix.md` |
| Root skill inventory/lineage/freeze | `docs/knowledge/skills/skill-map.md` |
| Repository-area ownership | `docs/knowledge/modules/module-map.md` |
| Source/authority routing | `docs/knowledge/sources/source-map.md` |
| Review evidence current meaning | `docs/knowledge/reviews/review-graph.md` |
| Durable cross-owner decision threshold | `docs/knowledge/decisions/change-decision-guide.md` |
| Current BuildIT parity gap evidence | `docs/knowledge/reviews/buildit-current-parity-gap-audit.md` |
| Ordered parity remediation | `docs/knowledge/operations/buildit-parity-remediation-plan.md` |
| Static repository gate | `tools/verify_repository.py` + `.github/workflows/repository-verify.yml` |
| Executable production gate | `.github/workflows/production-verify.yml` + `tests/` + `requirements.lock.txt` |
| Active continuation state | `docs/knowledge/next-action.md` |

## Production Layer

| Boundary | Current owner |
|---|---|
| End-to-end product sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 intake/recovery | `docs/foundation/02-source-intake-recovery.md` + Project Document Generator |
| Flow 3 PRD generation | `docs/foundation/03-prd-generation.md` + Project Document Generator |
| Flow 4 PRD validation/handoff | `docs/foundation/04-prd-validation-handoff.md` + `kits/project-document-generator/VALIDATION.md` |
| Project Document kit-local rules | `kits/project-document-generator/AGENTS.md` |
| Project Document production procedure | `kits/project-document-generator/SKILL.md` |
| Project Document renderer | `kits/project-document-generator/renderer/` |
| Project Document mechanical validator | `kits/project-document-generator/validator/validate.py` |
| Project Document focused regression | `tests/test_prd_contracts.py` |
| Flow 5 Voice Requirement Extraction | `docs/foundation/05-voice-requirement-extraction.md` + `kits/voice-production-kit/VOICE-EXTRACTION.md` |
| Flow 6 performance-script production | `docs/foundation/06-elevenlabs-script-production.md` + `kits/voice-production-kit/SCRIPT-PRODUCTION.md` |
| Flow 6 DOCX build | `kits/voice-production-kit/DOCX-FORMAT.md` + `kits/voice-production-kit/builder/build_docx.py` |
| Flow 7 Voice validation/delivery | `docs/foundation/07-voice-validation-delivery.md` + `kits/voice-production-kit/VOICE-VALIDATION.md` |
| Voice mechanical validator | `kits/voice-production-kit/validator/validate.py` |
| Voice focused regression | `tests/test_voice_contracts.py` |
| Voice direct dependency declaration | `kits/voice-production-kit/requirements.txt` |
| Exact Production Verify environment | `requirements.lock.txt` |
| Current production + parity evidence | `docs/foundation/validation-report.md` |
| Active project packages | `workspace/active/` |
| Saved project packages | `workspace/saved/` |
| Real System Integration Proof | `docs/knowledge/operations/system-integration-proof.md` |
| Retired-builder evidence | `docs/knowledge/operations/archived-retirement-audit.md` |

## Verification Separation

```text
Repository Verify
= static repository/routing/navigation/pin invariants

Production Verify
= locked dependency install + compile + focused executable production contracts

Flow validators / semantic audits / visual/audio review
= project-specific readiness and evidence
```

P0.1 Production Verify is proven on source head `0eb0485f117fa6ed419572a66539331f99114002` by run `31372363843`; Repository Verify on the same source head passed as run `31372363802`.

Neither gate replaces browser visual inspection, rendered DOCX page QA, or audio review.

## Project-Level Authority After Flow 7

```text
source/originals/*
      ↓
requirement state
      ↓
work/content.md                    canonical PRD
      ↓
PRD acceptance / handoff_ready
      ↓
work/voice-requirements.md         canonical voice-moment scope
      ↓
work/voice-production.md           canonical spoken/performance wording
      ↓
output/Voice Production.docx       derived production artifact
      ↓
work/voice-acceptance.md           Flow 7 evidence/findings
state/voice-state.yaml             voice_delivery_ready / lifecycle state
```

## Current Engineering Boundary

Production Flow 1–7 remains real-project proven. Overall BuildIT parity remains open.

P0.1 executable production verification is complete. The active boundary is **P0.2 — Technical Ownership Refinement**; current skill ownership must be audited before any root-skill architecture change.
