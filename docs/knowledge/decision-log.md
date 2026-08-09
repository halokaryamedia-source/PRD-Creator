# Decision Log

Use this note only for durable decisions whose reasons must survive future sessions. Active task status belongs in `next-action.md`.

## Current Decisions

### `Local` is the permanent development branch

- **Decision:** normal repository work continues directly on `Local`; do not create per-flow branches or routine PRs to `main`.
- **Reason:** this project is being developed iteratively by the same production workflow and per-flow PR ceremony adds friction without useful review value.
- **Boundary:** `main` remains a stable baseline and changes only when the user explicitly requests it.
- **Date:** 2026-08-10

### Repository is project memory

- **Decision:** repository state is authoritative for continuity; old chat is supporting context only.
- **Reason:** a new ChatGPT/Codex/developer session must be able to resume work without asking the user to reconstruct the full history.
- **Owners:** `AGENTS.md`, `CONTEXT.md`, `docs/knowledge/next-action.md`.
- **Date:** 2026-08-10

### Project Document Generator and Voice Production Kit remain separate production owners

- **Decision:** keep PRD/document design recovery upstream and voice performance production downstream.
- **Reason:** missing project decisions should be resolved in project documentation rather than invented in voice scripts.
- **Owner:** `docs/foundation/00-product-boundaries.md`.
- **Date:** 2026-08-10

### Source intake uses one slim persistent recovery model

- **Decision:** Flow 2 keeps original sources, one Source Inventory, one Requirement Register, one Intake State, and a concise human `review.md`.
- **Recovered from old package:** persistent state, source audit, conflict visibility, and explicit approval boundaries.
- **Not retained as default:** mandatory 12-phase ceremony, forced Guided Discussion rounds, or asking three-to-five questions when source evidence already supports completion.
- **Reason:** the user wants the system to fill obvious gaps itself and ask only when a real high-impact decision is missing.
- **Owner:** `docs/foundation/02-source-intake-recovery.md` and `kits/project-document-generator/SOURCE-INTAKE.md`.
- **Date:** 2026-08-10

### `Production Document Builder/` is Archived during migration

- **Decision:** preserve the package but do not treat it as active workflow authority or extend it by default.
- **Reason:** it contains useful historical tests/schemas/rendering/reference evidence, but deleting it before bounded migration would lose potentially useful proof and lineage.
- **Removal condition:** useful behavior/dependencies are migrated or intentionally retired in the owning flows.
- **Date:** 2026-08-10

### Golden Samples are references, not project requirements

- **Decision:** Golden Samples/approved references define demonstrated structure, presentation, tone, density, or quality only where explicitly stated.
- **Reason:** sample-specific objectives, mechanics, characters, or lines must not leak into unrelated projects.
- **Owner:** root `AGENTS.md`.
- **Date:** 2026-08-10

### Adopt BuildIT principles, not BuildIT domain structure 1:1

- **Decision:** reuse the ownership, continuity, validation, minimal-navigation, and anti-slop principles without copying Blockbench/MCP-specific architecture.
- **Reason:** this workspace has a different production domain and should remain compact.
- **Date:** 2026-08-10
