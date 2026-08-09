# Decision Log

Use this note only for durable decisions whose reasons must survive future sessions. Active task status belongs in `next-action.md`.

## Current Decisions

### Repository is project memory

- **Decision:** repository state is authoritative for continuity; old chat is supporting context only.
- **Reason:** a new ChatGPT/Codex/developer session must resume without reconstructing full history from the user.
- **Owners:** `AGENTS.md`, `CONTEXT.md`, `docs/knowledge/next-action.md`.
- **Date:** 2026-08-10

### `Local` is the permanent development branch

- **Decision:** normal work happens directly on `Local`; no routine per-flow branches/PRs.
- **Reason:** the user prefers one practical continuous working branch similar to BuildIT Local.
- **Date:** 2026-08-10

### Project Document Generator and Voice Production remain separate production owners

- **Decision:** keep PRD/content-definition work upstream and voice performance production downstream.
- **Reason:** missing project decisions should be resolved in project documentation rather than invented in voice scripts.
- **Owner:** `docs/foundation/00-product-boundaries.md`.
- **Date:** 2026-08-10

### Golden Samples are references, not project requirements

- **Decision:** Golden Samples define demonstrated structure/presentation/tone/density/quality only where explicitly stated.
- **Reason:** sample-specific objectives, mechanics, characters, or lines must not leak into unrelated projects.
- **Owner:** `AGENTS.md`.
- **Date:** 2026-08-10

### Adopt BuildIT principles, not BuildIT domain structure 1:1

- **Decision:** reuse ownership, continuity, validation, minimal-navigation, and anti-slop principles without copying Blockbench/MCP-specific architecture.
- **Reason:** this workspace has a different production domain and should remain compact.
- **Date:** 2026-08-10

### Archived Production Document Builder is preserved until bounded migration completes

- **Decision:** do not delete the old package yet; mark it Archived and adopt useful behavior only from the owning flow.
- **Reason:** it contains potentially useful renderer/tests/contracts, but treating it as current authority would create parallel systems and unnecessary ceremony.
- **Date:** 2026-08-10

### Canonical PRD content is human-readable `content.md`

- **Decision:** `work/content.md` owns Flow 3 project-document meaning; `work/render-data.json` is derived and `output/final.html` is presentation only.
- **Reason:** developers/level designers need a readable canonical source while deterministic rendering still benefits from a small structured projection.
- **Owner:** `docs/foundation/03-prd-generation.md` and active kit content/rendering contracts.
- **Date:** 2026-08-10

### Renderer preserves the approved shell but dynamically regenerates project-owned pages

- **Decision:** clone the Approved Template, preserve shared head/CSS/JS/controls/sidebar shell, and regenerate only project brand metadata, navigation, main pages, glossary data, and local-storage namespace.
- **Reason:** literal replacement/manual objective duplication was too fragile, while rebuilding the whole visual system would break template fidelity.
- **Adopted from Archived builder:** dynamic hierarchy/component vocabulary and renderer meaning-safety.
- **Not adopted:** mandatory schema registry, content freeze, Guided Discussion rounds, release/checksum/ZIP ceremony.
- **Date:** 2026-08-10
