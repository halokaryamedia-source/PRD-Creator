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
Flow 3 — Project Document / PRD Generation            ✓ implemented
    ↓
Flow 4 — PRD Validation & Team Handoff                ✓ implemented
    ↓
Flow 5 — Voice Requirement Extraction                 ✓ implemented
    ↓
Flow 6 — ElevenLabs Performance Script Production     next
    ↓
Flow 7 — Voice Validation & Delivery
```

The active Project Document Generator owns Flow 2–4 under `kits/project-document-generator/`.

The active Voice Production Kit now lives under `kits/voice-production-kit/`. Flow 5 extracts traceable voice requirements from a `handoff_ready` PRD and stops before performance-script writing. Flow 6 remains the next boundary.

The pre-existing `Production Document Builder/` remains **Archived** and non-authoritative.

## Mandatory Session Boot

1. read `AGENTS.md`;
2. read `CONTEXT.md`;
3. read `docs/knowledge/next-action.md`;
4. open only the relevant foundation/kit/source owner;
5. do not ask the user to reconstruct prior work until these owners have been checked.

## Repository Map

- `AGENTS.md` — repository-wide rules, branch policy, authority, proof, and anti-slop baseline.
- `CONTEXT.md` — stable purpose, terminology, and boundaries.
- `docs/foundation/` — durable production policy.
- `docs/knowledge/` — current state, decisions, navigation, ownership, and backlog.
- `kits/project-document-generator/` — active PRD intake/generation/validation kit.
- `kits/voice-production-kit/` — active downstream voice-requirement kit; Flow 6 script production follows next.
- `workspace/active/` — project packages currently in production.
- `workspace/saved/` — intentionally retained completed/saved project packages.
- `Production Document Builder/` — Archived historical package retained only for bounded migration/reference.

## Core Rule

```text
Source ≠ Interpretation ≠ Decision ≠ Requirement State ≠ Canonical PRD ≠ Rendered Output ≠ PRD Acceptance ≠ Voice Requirements ≠ Performance Script ≠ Delivery
```

Rendering success is not development-readiness. `handoff_ready` is revision-specific production-document readiness, not client approval or implementation completion. Voice requirements define **what communication is justified**; they are not final spoken scripts.
