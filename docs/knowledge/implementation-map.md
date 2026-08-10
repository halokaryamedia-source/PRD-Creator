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
| Flow 5 voice requirement extraction | `docs/foundation/05-voice-requirement-extraction.md` + `VOICE-EXTRACTION.md` |
| Flow 6 performance-script production | `docs/foundation/06-elevenlabs-script-production.md` + `SCRIPT-PRODUCTION.md` |
| Flow 6 DOCX format/build | `kits/voice-production-kit/DOCX-FORMAT.md` + `builder/build_docx.py` |
| Current evidence status | `docs/foundation/validation-report.md` |
| Active continuation state | `docs/knowledge/next-action.md` |
| Durable decisions/reasons | `docs/knowledge/decision-log.md` |
| Active PRD kit | `kits/project-document-generator/` |
| Active Voice kit | `kits/voice-production-kit/` |
| Active Voice reference contract | `kits/voice-production-kit/DOCX-FORMAT.md` + `REFERENCE/Aftershock/README.md` |
| Active project packages | `workspace/active/` |
| Saved project packages | `workspace/saved/` |
| Archived historical builder | `Production Document Builder/` |

## Project-level authority after Flow 6

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
Flow 7 final validation/delivery
```

`state/voice-state.yaml` records lifecycle status/revision/next step across Flow 5–7; it does not replace canonical voice content.

## Pending downstream boundary

- Flow 7 Voice Validation & Delivery is next.
- Real-project execution remains needed across the full Flow 2→6 chain.
- Archived builder remains non-authoritative.
