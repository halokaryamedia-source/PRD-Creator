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
| Project Document renderer mechanics + render identity emission | `kits/project-document-generator/renderer/render.py` |
| Project Document page/helper rendering | `kits/project-document-generator/renderer/core.py` + `renderer/pages.py` |
| Project Document approved shell | `kits/project-document-generator/template/approved-document.html` |
| Project Document mechanical validator + current-render identity/page-set checks | `kits/project-document-generator/validator/validate.py` |
| Project Document focused regression | `tests/test_prd_contracts.py` |
| Flow 5 Voice semantic scope | `docs/foundation/05-voice-requirement-extraction.md` + `.agents/skills/voice-production/SKILL.md` |
| Flow 6 performance/artifact semantic contract | `docs/foundation/06-elevenlabs-script-production.md` + `.agents/skills/voice-production/SKILL.md` |
| Voice kit-local contributor/technical routing | `kits/voice-production-kit/AGENTS.md` |
| Flow 6 DOCX presentation contract | `kits/voice-production-kit/DOCX-FORMAT.md` |
| Voice DOCX builder mechanics | `kits/voice-production-kit/builder/build_docx.py` |
| Flow 7 Voice readiness/evidence semantics | `docs/foundation/07-voice-validation-delivery.md` + `.agents/skills/voice-production/SKILL.md` |
| Voice mechanical validator | `kits/voice-production-kit/validator/validate.py` |
| Voice focused regression | `tests/test_voice_contracts.py` |
| Exact Production Verify environment | `requirements.lock.txt` |
| Current production + parity evidence | `docs/foundation/validation-report.md` |
| Active project packages | `workspace/active/` |
| Saved project packages | `workspace/saved/` |
| Real System Integration Proof | `docs/knowledge/operations/system-integration-proof.md` |

## Semantic / Technical / Repository-Engineering Separation

```text
semantic/product contract
= root semantic specialist + matching Flow policy/project authority

pure executable mechanics
= nearest kit AGENTS + exact renderer/template/validator/builder source

shared dependency/regression/CI
= requirements.lock.txt + tests/ + tools/ + workflows
```

## P1.1 Mechanical PRD Identity

Current generic mechanical chain:

```text
work/render-data.json
→ canonical sorted JSON SHA-256
→ output/final.html meta[name="render-data-sha256"]
→ validator exact fingerprint match
→ exact document-main generated section order/set
```

Proof on source head `04f306f8589528ccc8cb03e89333dba174a3d276`:

```text
Production Verify 31377375929  PASS
Repository Verify 31377377036  PASS
```

This proves current render-data ↔ final HTML mechanical identity for the contract implemented. It does not prove semantic `content.md` → render-data equivalence or browser visual quality.

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
state/voice-state.yaml             voice_delivery_ready / lifecycle state
```

## Current Engineering Boundary

Production Flow 1–7 remains real-project proven for the recorded Clockwork Vault revision. Overall BuildIT parity remains open.

P1 audit and P1.1 are complete. The active source slice is **P1.2 — PRD Renderer Script/Shell Safety**.
