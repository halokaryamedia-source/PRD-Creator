# Project Production Workspace

A repository-first production workspace for turning incomplete project direction into development-ready project documentation, then deriving production-ready voice scripts for ElevenLabs.

The repository is the project memory. Chat history may help, but it is not the authority for current project state.

## Branch Model

- `Local` — permanent working/development authority. Normal project work is committed directly here.
- `main` — stable baseline. Do not open routine per-flow PRs or merge into `main` unless the user explicitly requests it.
- old `agent/*` branches are non-authoritative leftovers and must not be used for continuation.

## Production Flow

```text
Flow 1 — Repository Boot & Project Memory             ✓ implemented
    ↓
Flow 2 — Source Intake & Requirement Recovery         ✓ implemented
    ↓
Flow 3 — Project Document / PRD Generation            next
    ↓
Flow 4 — PRD Validation & Team Handoff
    ↓
Flow 5 — Voice Requirement Extraction
    ↓
Flow 6 — ElevenLabs Performance Script Production
    ↓
Flow 7 — Voice Validation & Delivery
```

The active Project Document Generator baseline now lives under `kits/project-document-generator/`. Flow 2 extends its intake/recovery boundary without yet redesigning canonical PRD drafting or HTML rendering. The Voice Production Kit remains a reviewed external baseline until its owning downstream flow is reached.

The pre-existing `Production Document Builder/` package is **Archived**. It is preserved during migration so useful tests, schema ideas, renderer behavior, and Golden Sample dependencies can be evaluated in the owning flow. It is not current workflow authority.

## Mandatory Session Boot

For a new ChatGPT or Codex session:

1. read `AGENTS.md`;
2. read `CONTEXT.md`;
3. read `docs/knowledge/next-action.md`;
4. read only the relevant foundation note and affected kit/source;
5. do not ask the user to reconstruct prior work until these owners have been checked.

## Repository Map

- `AGENTS.md` — repository-wide working rules, branch policy, authority, proof, and anti-slop baseline.
- `CONTEXT.md` — stable purpose, terminology, and boundaries.
- `docs/foundation/` — durable product/workflow policy.
- `docs/knowledge/` — current state, decisions, navigation, ownership, and backlog.
- `kits/project-document-generator/` — active upstream document-generation kit; Flow 2 intake/recovery is integrated here.
- `workspace/active/` — project packages currently in production.
- `workspace/saved/` — intentionally retained completed/saved project packages.
- `Production Document Builder/` — Archived historical package; retained only for bounded migration/reference.

## Core Rule

```text
Source ≠ Interpretation ≠ Decision ≠ Output ≠ Approval
```

Golden Samples and approved references define structure, quality, and presentation where explicitly stated. They do not automatically become project-specific requirements.
