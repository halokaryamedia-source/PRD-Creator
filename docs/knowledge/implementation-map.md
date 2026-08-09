# Implementation Map

Updated: 2026-08-10

Use this note to answer where current behavior/policy lives. It is not the active task tracker.

## Repository Areas

| Boundary | Current owner |
|---|---|
| Repository-wide rules / branch policy / authority | `AGENTS.md` |
| Stable product context / terminology | `CONTEXT.md` |
| End-to-end production sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 intake/recovery policy | `docs/foundation/02-source-intake-recovery.md` |
| Flow 3 PRD generation policy | `docs/foundation/03-prd-generation.md` |
| Flow 4 validation/handoff policy | `docs/foundation/04-prd-validation-handoff.md` |
| Current evidence status | `docs/foundation/validation-report.md` |
| Active continuation state | `docs/knowledge/next-action.md` |
| Durable decisions/reasons | `docs/knowledge/decision-log.md` |
| Active PRD kit | `kits/project-document-generator/` |
| Source intake procedure | `kits/project-document-generator/SOURCE-INTAKE.md` |
| Canonical PRD contract | `kits/project-document-generator/CONTENT-CONTRACT.md` |
| Rendering contract | `kits/project-document-generator/RENDERING.md` |
| Flow 4 acceptance/handoff contract | `kits/project-document-generator/VALIDATION.md` |
| PRD shell renderer | `kits/project-document-generator/renderer/` |
| PRD mechanical validator | `kits/project-document-generator/validator/validate.py` |
| Approved HTML shell | `kits/project-document-generator/template/approved-document.html` |
| Active project packages | `workspace/active/` |
| Saved project packages | `workspace/saved/` |
| Archived historical builder | `Production Document Builder/` |

## Project-level authority after Flow 4

```text
source/originals/*
      ↓
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
      ↓
work/content.md                 canonical PRD meaning
      ↓
work/render-data.json           derived renderer projection
      ↓
output/final.html               rendered PRD artifact
      ↓
work/acceptance.md              Flow 4 evidence/findings
state/handoff-state.yaml        revision-specific readiness state
      ↓
output/team-handoff.md          concise team navigation aid
```

`acceptance.md` and handoff state do not replace canonical PRD meaning; they record whether that exact revision is usable by the production team.

## Pending downstream migration

- Flow 5 Voice Requirement Extraction is next.
- Voice Production Kit remains reviewed but unmigrated until Flow 5/6.
- Archived builder is not an active owner even when cited as historical evidence.
