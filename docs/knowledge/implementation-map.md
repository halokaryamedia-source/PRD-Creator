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
| Operating parity acceptance evidence | `docs/knowledge/operations/operating-parity-acceptance.md` |
| Operating parity gate decisions | `docs/knowledge/decisions/operating-parity-gates.md` |
| Repository engineering gate | `tools/verify_repository.py` + `.github/workflows/repository-verify.yml` |
| Active continuation state | `docs/knowledge/next-action.md` |

## Production Layer

| Boundary | Current owner |
|---|---|
| End-to-end product sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 intake/recovery | `docs/foundation/02-source-intake-recovery.md` + Project Document Generator |
| Flow 3 PRD generation | `docs/foundation/03-prd-generation.md` + Project Document Generator |
| Flow 4 PRD validation/handoff | `docs/foundation/04-prd-validation-handoff.md` + `kits/project-document-generator/VALIDATION.md` |
| Project Document kit-local routing/edit rules | `kits/project-document-generator/AGENTS.md` |
| Project Document production procedure | `kits/project-document-generator/SKILL.md` |
| Flow 5 Voice Requirement Extraction | `docs/foundation/05-voice-requirement-extraction.md` + `kits/voice-production-kit/VOICE-EXTRACTION.md` |
| Flow 6 performance-script production | `docs/foundation/06-elevenlabs-script-production.md` + `kits/voice-production-kit/SCRIPT-PRODUCTION.md` |
| Flow 6 DOCX format/build | `kits/voice-production-kit/DOCX-FORMAT.md` + `builder/build_docx.py` |
| Flow 7 Voice validation/delivery | `docs/foundation/07-voice-validation-delivery.md` + `kits/voice-production-kit/VOICE-VALIDATION.md` |
| Voice kit-local routing/edit rules | `kits/voice-production-kit/AGENTS.md` |
| Current production + operating evidence status | `docs/foundation/validation-report.md` |
| Active PRD kit | `kits/project-document-generator/` |
| Active Voice kit | `kits/voice-production-kit/` |
| Active project packages | `workspace/active/` |
| Saved project packages | `workspace/saved/` |
| Real System Integration Proof | `docs/knowledge/operations/system-integration-proof.md` |
| Retired-builder evidence | `docs/knowledge/operations/archived-retirement-audit.md` |

## Layer Separation

```text
AGENTS / root skills
= how the agent frames/routes/proves work

module/source/implementation maps
= how the agent finds the correct owner

kit-local AGENTS + kit SKILL/procedures
= scoped production/read/edit discipline

workspace project package
= project-specific source/state/canonical work/artifacts

Repository Verify
= cheap static repository invariants only
```

Do not use the automated repository gate as a substitute for Flow-specific semantic or visual/audio proof.

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

Actual generated audio, when supplied, is evidence/delivery material only and never becomes upstream project authority.

## Current Engineering Boundary

Production Flow 1–7 and BuildIT-style operating parity are accepted on `Local`.

Phase 3 representative routing/Maintenance acceptance passed, and the first `Repository Verify` GitHub Actions run (`31367001967`) succeeded on commit `5970c47c15c8e9e83df185be7c5472e976739062`.

No additional parity phase is planned. Future engineering starts from the smallest current owner and changes only when a real project defect, capability gap, or repeatable invariant failure provides evidence.
