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
| Flow 5 voice extraction policy | `docs/foundation/05-voice-requirement-extraction.md` |
| Current evidence status | `docs/foundation/validation-report.md` |
| Active continuation state | `docs/knowledge/next-action.md` |
| Durable decisions/reasons | `docs/knowledge/decision-log.md` |
| Active PRD kit | `kits/project-document-generator/` |
| PRD source intake / content / rendering / validation | `kits/project-document-generator/` owners |
| Active Voice Production kit | `kits/voice-production-kit/` |
| Voice requirement extraction procedure | `kits/voice-production-kit/VOICE-EXTRACTION.md` |
| Flow 6 baseline instructions | `kits/voice-production-kit/INSTRUCTIONS.md` |
| Active project packages | `workspace/active/` |
| Saved project packages | `workspace/saved/` |
| Archived historical builder | `Production Document Builder/` |

## Project-level authority after Flow 5

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
work/acceptance.md
state/handoff-state.yaml        accepted PRD revision / readiness
output/team-handoff.md
      ↓
work/voice-requirements.md      canonical voice-moment requirements
state/voice-state.yaml          Flow 5 revision/status/next step
```

`voice-requirements.md` does not contain final spoken scripts. It defines justified voice scope and required communication facts for Flow 6.

## Pending downstream migration

- Flow 6 ElevenLabs Performance Script Production is next.
- Original Voice Production v1.0 script instructions are preserved as a baseline but not yet aligned to the new canonical voice-requirement handoff.
- Flow 7 validation/delivery remains unimplemented.
- Archived builder remains non-authoritative.
