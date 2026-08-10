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
| Top-level parity remediation | `docs/knowledge/operations/buildit-parity-remediation-plan.md` |
| P0.2 technical ownership evidence | `docs/knowledge/reviews/technical-ownership-refinement-audit.md` + `docs/knowledge/decisions/technical-ownership-boundary.md` |
| P1 production engineering audit | `docs/knowledge/reviews/production-engineering-quality-audit.md` |
| P1 ordered source remediation | `docs/knowledge/operations/production-engineering-remediation-plan.md` |
| Static repository gate | `tools/verify_repository.py` + `.github/workflows/repository-verify.yml` |
| Executable production gate | `.github/workflows/production-verify.yml` + `tests/` + `requirements.lock.txt` |
| Active continuation state | `docs/knowledge/next-action.md` |

## Production Layer

| Boundary | Current owner |
|---|---|
| End-to-end product sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 intake/recovery | `docs/foundation/02-source-intake-recovery.md` + Project Document Generator |
| Flow 3 PRD semantic/product contract | `docs/foundation/03-prd-generation.md` + `.agents/skills/project-document-production/SKILL.md` |
| Flow 4 PRD readiness/handoff semantics | `docs/foundation/04-prd-validation-handoff.md` + `.agents/skills/project-document-production/SKILL.md` |
| Project Document kit-local contributor/technical routing | `kits/project-document-generator/AGENTS.md` |
| Project Document production/rendering contract | `kits/project-document-generator/SKILL.md` + `kits/project-document-generator/RENDERING.md` |
| Project Document renderer mechanics | `kits/project-document-generator/renderer/` |
| Project Document approved shell | `kits/project-document-generator/template/approved-document.html` |
| Project Document mechanical validator | `kits/project-document-generator/validator/validate.py` |
| Project Document focused regression | `tests/test_prd_contracts.py` |
| Flow 5 Voice semantic scope | `docs/foundation/05-voice-requirement-extraction.md` + `.agents/skills/voice-production/SKILL.md` |
| Flow 6 performance/artifact semantic contract | `docs/foundation/06-elevenlabs-script-production.md` + `.agents/skills/voice-production/SKILL.md` |
| Voice kit-local contributor/technical routing | `kits/voice-production-kit/AGENTS.md` |
| Flow 6 DOCX presentation contract | `kits/voice-production-kit/DOCX-FORMAT.md` |
| Voice DOCX builder mechanics | `kits/voice-production-kit/builder/build_docx.py` |
| Flow 7 Voice readiness/evidence semantics | `docs/foundation/07-voice-validation-delivery.md` + `.agents/skills/voice-production/SKILL.md` |
| Voice mechanical validator | `kits/voice-production-kit/validator/validate.py` |
| Voice focused regression | `tests/test_voice_contracts.py` |
| Voice direct dependency declaration | `kits/voice-production-kit/requirements.txt` |
| Exact Production Verify environment | `requirements.lock.txt` |
| Current production + parity evidence | `docs/foundation/validation-report.md` |
| Active/saved project packages | `workspace/active/` / `workspace/saved/` |
| Real System Integration Proof | `docs/knowledge/operations/system-integration-proof.md` |
| Retired-builder evidence | `docs/knowledge/operations/archived-retirement-audit.md` |

## Semantic / Technical / Repository-Engineering Separation

```text
semantic/product contract
= root semantic specialist + matching Flow policy/project authority

pure executable mechanics
= nearest kit AGENTS + exact renderer/template/validator/builder source

shared dependency/regression/CI
= requirements.lock.txt + tests/ + tools/ + workflows
```

## P1 Engineering Proof

P1.1:

```text
source head       04f306f8589528ccc8cb03e89333dba174a3d276
Production Verify 31377375929  PASS
Repository Verify 31377377036  PASS
```

Current PRD mechanical validator now proves current render-data ↔ HTML revision identity and exact generated page order/set, while malformed current projection collections fail structurally.

P1.2:

```text
source head       802904856b69fd50008999f196cb72d48303e0ba
Production Verify 31378603848  PASS
Repository Verify 31378603894  PASS
```

Current renderer now owns script-context-safe glossary serialization, supported alias-shape preflight, exact required shell-marker/metadata checks, inherited namespace-token checks, and controlled covered contract failures.

Neither proof replaces semantic PRD readiness, browser visual/runtime inspection, rendered DOCX page QA, pronunciation/performance judgement, or audio review.

## Project-Level Authority After Flow 7

```text
source/originals/*
      ↓
requirement state
      ↓
work/content.md                    canonical PRD
      ↓
work/render-data.json              derived PRD projection
      ↓
output/final.html                  derived PRD presentation
      ↓
PRD acceptance / handoff_ready
      ↓
work/voice-requirements.md         canonical voice-moment scope
      ↓
work/voice-production.md           canonical spoken/performance wording
      ↓
output/Voice Production.docx       derived Voice presentation artifact
      ↓
work/voice-acceptance.md           Flow 7 evidence/findings
state/voice-state.yaml             Voice lifecycle state
```

## Current Engineering Boundary

Production Flow 1–7 remains real-project proven for the recorded Clockwork Vault revision. Overall BuildIT parity remains open.

P1.1 and P1.2 are complete. The active source slice is **P1.3 — Voice Revision + DOCX Entry Integrity**.
