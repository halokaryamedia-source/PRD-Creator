# Decision Log

Use this note only for durable decisions whose reasons must survive future sessions. Active task status belongs in `next-action.md`.

## Current Decisions

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

### Golden Samples are references, not project requirements

- **Decision:** Golden Samples/approved references define demonstrated structure, presentation, tone, density, or quality only where explicitly stated.
- **Reason:** sample-specific objectives, mechanics, characters, or lines must not leak into unrelated projects.
- **Owner:** root `AGENTS.md`.
- **Date:** 2026-08-10

### Adopt BuildIT principles, not BuildIT domain structure 1:1

- **Decision:** reuse the ownership, continuity, validation, minimal-navigation, and anti-slop principles without copying Blockbench/MCP-specific architecture.
- **Reason:** this workspace has a different production domain and should remain compact.
- **Date:** 2026-08-10
