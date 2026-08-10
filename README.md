# Project Production Workspace

A repository-first workspace for turning incomplete project direction into development-ready project documentation, then deriving validated ElevenLabs-ready Voice Production.

The repository is project memory. Chat history is supporting context, not current-state authority.

## Branch model

- `Local` — permanent working/development authority.
- `main` — stable baseline; change only when explicitly requested.
- no routine per-task/per-flow branches or PRs.

## Production flow

```text
Source Intake
→ PRD
→ Validate / Handoff
→ Voice Requirements
→ Voice Script
→ Build DOCX
→ Validate / Deliver
```

Flow 1–7 is implemented and real-project proven.

## Operating flow

```text
Plan | Developing | Maintenance
→ correct owner
→ smallest complete change
→ minimum useful proof
```

Canonical root skills:

```text
development-brief
project-document-production
voice-production
```

## Keep it simple

BuildIT is used as a reference for repository discipline, not as a checklist of mechanisms to copy.

Current anti-overdevelopment decision:

`docs/knowledge/decisions/anti-overdevelopment-simplification.md`

Normal project work must not require manual checksum/revision metadata. Derived files are regenerated from canonical inputs when needed.

The cleanup that removed unnecessary PRD/Voice revision machinery is:

`08b6f9d6a98641c5f93932df015cb0d2dffe9a42`

with Repository Verify and Production Verify both passing.

## Verification layers

- **Repository Verify** — static repository/routing/navigation/syntax checks.
- **Production Verify** — locked dependencies, compile, focused real PRD/Voice executable contracts.
- **Semantic / visual / audio evidence** — performed only where the production claim actually requires it.

CI is a guard, not a reason to keep adding engineering machinery.

## Repository map

- `AGENTS.md` — repository-wide work rules;
- `CONTEXT.md` — stable current context;
- `.agents/skills/` — semantic routing/judgment skills;
- `docs/foundation/` — durable production policy;
- `docs/knowledge/` — current state, ownership, decisions, reviews, operations;
- `kits/project-document-generator/` — Flow 2–4 implementation;
- `kits/voice-production-kit/` — Flow 5–7 implementation;
- `tests/`, `tools/`, `.github/workflows/` — focused repository engineering;
- `workspace/` — project-specific production packages.

## Current work

No automatic parity-hardening phase is active. See `docs/knowledge/next-action.md` for the single current continuation point.
