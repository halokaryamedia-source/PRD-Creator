# Implementation Map

Updated: 2026-08-10

Use this note to answer where current behavior/policy lives. It is not the active task tracker.

## Repository Areas

| Boundary | Current owner |
|---|---|
| Repository-wide rules / branch policy / authority | `AGENTS.md` |
| Stable product context / terminology | `CONTEXT.md` |
| End-to-end sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 intake/recovery | `docs/foundation/02-source-intake-recovery.md` + Project Document Generator |
| Flow 3 PRD generation | `docs/foundation/03-prd-generation.md` + Project Document Generator |
| Flow 4 PRD validation/handoff | `docs/foundation/04-prd-validation-handoff.md` + `VALIDATION.md` |
| Flow 5 Voice Requirement Extraction | `docs/foundation/05-voice-requirement-extraction.md` + `VOICE-EXTRACTION.md` |
| Flow 6 performance-script production | `docs/foundation/06-elevenlabs-script-production.md` + `SCRIPT-PRODUCTION.md` |
| Flow 6 DOCX format/build | `kits/voice-production-kit/DOCX-FORMAT.md` + `builder/build_docx.py` |
| Flow 7 Voice validation/delivery | `docs/foundation/07-voice-validation-delivery.md` + `VOICE-VALIDATION.md` |
| Flow 7 mechanical validator | `kits/voice-production-kit/validator/validate.py` |
| Current evidence status | `docs/foundation/validation-report.md` |
| Active continuation state | `docs/knowledge/next-action.md` |
| Durable decisions/reasons | `docs/knowledge/decision-log.md` |
| Active PRD kit | `kits/project-document-generator/` |
| Active Voice kit | `kits/voice-production-kit/` |
| Active Voice reference contract | `kits/voice-production-kit/DOCX-FORMAT.md` + `REFERENCE/Aftershock/README.md` |
| Active project packages | `workspace/active/` |
| Saved project packages | `workspace/saved/` |
| Archived historical builder | `Production Document Builder/` |

## Project-level authority after Flow 7

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

## Next engineering boundary

All seven production flows are implemented. Next is **System Integration Proof**: run one real project through Flow 2→7, capture defects/revisions, then perform the final Archived-package retirement audit before deletion.
