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
| Root skill routing | `docs/knowledge/skills/activation-matrix.md` |
| Root skill inventory/lineage/freeze | `docs/knowledge/skills/skill-map.md` |
| Project Document semantic specialist | `.agents/skills/project-document-production/SKILL.md` |
| Voice semantic specialist | `.agents/skills/voice-production/SKILL.md` |
| Active continuation state | `docs/knowledge/next-action.md` |
| Durable decisions/reasons | `docs/knowledge/decision-log.md` |

## Production Layer

| Boundary | Current owner |
|---|---|
| End-to-end product sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 intake/recovery | `docs/foundation/02-source-intake-recovery.md` + Project Document Generator |
| Flow 3 PRD generation | `docs/foundation/03-prd-generation.md` + Project Document Generator |
| Flow 4 PRD validation/handoff | `docs/foundation/04-prd-validation-handoff.md` + `kits/project-document-generator/VALIDATION.md` |
| Flow 5 Voice Requirement Extraction | `docs/foundation/05-voice-requirement-extraction.md` + `kits/voice-production-kit/VOICE-EXTRACTION.md` |
| Flow 6 performance-script production | `docs/foundation/06-elevenlabs-script-production.md` + `kits/voice-production-kit/SCRIPT-PRODUCTION.md` |
| Flow 6 DOCX format/build | `kits/voice-production-kit/DOCX-FORMAT.md` + `builder/build_docx.py` |
| Flow 7 Voice validation/delivery | `docs/foundation/07-voice-validation-delivery.md` + `kits/voice-production-kit/VOICE-VALIDATION.md` |
| Flow 7 mechanical validator | `kits/voice-production-kit/validator/validate.py` |
| Current production evidence status | `docs/foundation/validation-report.md` |
| Active PRD kit | `kits/project-document-generator/` |
| Active Voice kit | `kits/voice-production-kit/` |
| Active Voice reference contract | `kits/voice-production-kit/DOCX-FORMAT.md` + `REFERENCE/Aftershock/README.md` |
| Active project packages | `workspace/active/` |
| Saved project packages | `workspace/saved/` |
| Real System Integration Proof | `docs/knowledge/operations/system-integration-proof.md` |
| Retired-builder evidence | `docs/knowledge/operations/archived-retirement-audit.md` |

## Layer Separation

```text
AGENTS / root skills
= how the agent frames/routes/proves work

kits + foundation Flow rules
= how PRD/Voice production is performed

workspace project package
= project-specific source/state/canonical work/artifacts
```

Do not move detailed Flow procedure into root skills and do not use kit-local `SKILL.md` files as parallel repository-wide routing roots.

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

Production Flow 1–7 and real-project integration are complete. BuildIT-style Operating Architecture Parity Phase 1 is now implemented.

Next operating boundary: module/source ownership routing, Maintenance workflow, review evidence lifecycle, durable-decision threshold, and boot/proof baseline. Do not modify production semantics during that phase unless a concrete inconsistency is found.
