# Project Production Workspace

A repository-first production workspace for turning incomplete project direction into development-ready project documentation, then deriving production-ready voice scripts for ElevenLabs.

The repository is the project memory. Chat history may help, but it is not the authority for current project state.

## Production Flow

```text
Flow 1 — Repository Boot & Project Memory
    ↓
Flow 2 — Source Intake & Requirement Recovery
    ↓
Flow 3 — Project Document / PRD Generation
    ↓
Flow 4 — PRD Validation & Team Handoff
    ↓
Flow 5 — Voice Requirement Extraction
    ↓
Flow 6 — ElevenLabs Performance Script Production
    ↓
Flow 7 — Voice Validation & Delivery
```

Only Flow 1 is implemented in this revision. The supplied Project Document Generator and Voice Production Kit were reviewed as the intended upstream and downstream production baselines, but their implementation files are **not migrated during Flow 1**. Each kit will be adopted or reconciled only when its owning production flow is reached. The pre-existing `Production Document Builder/` package remains intact as historical/reference material pending a bounded migration audit.

## Mandatory Session Boot

For a new ChatGPT or Codex session:

1. read `AGENTS.md`;
2. read `CONTEXT.md`;
3. read `docs/knowledge/next-action.md`;
4. read only the relevant foundation note and affected kit/source;
5. do not ask the user to reconstruct prior work until these owners have been checked.

## Repository Map

- `AGENTS.md` — repository-wide working rules, authority, proof, and anti-slop baseline.
- `CONTEXT.md` — stable purpose, terminology, and boundaries.
- `docs/foundation/` — durable product/workflow policy.
- `docs/knowledge/` — current state, decisions, navigation, ownership, and backlog.
- `workspace/active/` — project packages currently in production.
- `workspace/saved/` — intentionally retained completed/saved project packages.
- `Production Document Builder/` — pre-existing historical package; preserved unchanged during Flow 1 and not treated as current authority until audited in the relevant flow.

## Core Rule

```text
Source ≠ Interpretation ≠ Decision ≠ Output ≠ Approval
```

Golden Samples and approved references define structure, quality, and presentation where explicitly stated. They do not automatically become project-specific requirements.
