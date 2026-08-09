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

Flows 1–3 are implemented on `Local`. The active Project Document Generator lives at `kits/project-document-generator/`. Voice Production remains intentionally deferred until its owning downstream flow.

The pre-existing `Production Document Builder/` package is **Archived**. It is preserved as historical/reference material until useful behavior has been migrated or intentionally retired; do not extend it as the current implementation.

## Branch Policy

- `Local` is the permanent development/work authority.
- Work directly on `Local`; do not create routine per-flow branches or PRs.
- `main` is a stable baseline and changes only when explicitly requested.

## Mandatory Session Boot

1. read `AGENTS.md`;
2. read `CONTEXT.md`;
3. read `docs/knowledge/next-action.md`;
4. read only the relevant foundation note and affected kit/source;
5. do not ask the user to reconstruct prior work until repository owners have been checked.

## Repository Map

- `AGENTS.md` — repository-wide working rules, authority, proof, and anti-slop baseline.
- `CONTEXT.md` — stable purpose, terminology, and product boundaries.
- `docs/foundation/` — durable production policy and flow contracts.
- `docs/knowledge/` — current state, decisions, navigation, ownership, and backlog.
- `kits/project-document-generator/` — active upstream PRD requirement-recovery/generation implementation.
- `workspace/active/` — project packages currently in production.
- `workspace/saved/` — intentionally retained completed/saved project packages.
- `Production Document Builder/` — Archived historical implementation.

## Authority rule

```text
Source ≠ Interpretation ≠ Decision ≠ Canonical Content ≠ Rendered Output ≠ Approval
```

For Flow 3 specifically:

```text
work/content.md        = canonical PRD meaning
work/render-data.json  = derived rendering projection
output/final.html      = presentation artifact
```

Golden Samples define demonstrated presentation/quality contracts where explicitly stated; they do not automatically become project-specific requirements.
