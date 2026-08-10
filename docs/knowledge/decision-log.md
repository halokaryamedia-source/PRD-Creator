# Decision Log

Use this note only for durable decisions whose reasons must survive future sessions. Active task status belongs in `next-action.md`.

## Current Decisions

### Flow 6 canonical performance wording stays human-readable; DOCX is derived

- **Decision:** `work/voice-production.md` owns final spoken wording/performance notation; `output/Voice Production.docx` is generated presentation only.
- **Reason:** production wording needs an editable/reviewable canonical owner, while the team still needs a polished DOCX for ElevenLabs workflow.
- **Owner:** `docs/foundation/06-elevenlabs-script-production.md`, `kits/voice-production-kit/SCRIPT-PRODUCTION.md`.
- **Date:** 2026-08-10

### Flow 6 cannot change Flow 5 voice scope silently

- **Decision:** every Flow 5 Voice ID must appear exactly once with the same Type in Flow 6 unless Flow 5 is explicitly reopened.
- **Reason:** script polish must not become a hidden mechanism for adding/removing communication scope or changing a channel.
- **Mechanical proof:** `builder/build_docx.py --requirements` checks exact ID/type parity.
- **Date:** 2026-08-10

### Aftershock Voice Production reference is audited and codified, not duplicated

- **Decision:** use the original v1.0.0 `Voice Production.docx` as the audited Flow 6 layout/performance benchmark, record its SHA-256, and codify the demonstrated contract in `DOCX-FORMAT.md` + the builder rather than duplicating the binary through the current GitHub write connector.
- **SHA-256:** `c76ce2562ee1839ae9174373f510b26da09e7b05f90e43a3e1de820633c34020`.
- **Reason:** the source binary was re-read, rendered, and visually inspected, but the current GitHub connector does not provide a safe direct binary-file upload path. Runtime/build behavior should not depend on a reference binary.
- **Boundary:** the reference defines quality/formatting only, not another project's speaker, voice count, wording, or duration quota.
- **Owner:** `kits/voice-production-kit/DOCX-FORMAT.md`, `REFERENCE/Aftershock/README.md`, and `builder/build_docx.py`.
- **Date:** 2026-08-10

### Legacy paired Aftershock Gameplay HTML is not duplicated into active Voice kit

- **Decision:** keep the old `Gameplay.html` V1.2 out of the active Voice kit.
- **Reason:** active projects already have an accepted PRD as current factual authority; duplicating a stale paired gameplay document would create a competing source of truth.
- **Historical availability:** recoverable from the original v1.0.0 Voice kit/source when needed for audit.
- **Date:** 2026-08-10

### Flow 4 uses one development-readiness gate instead of Content Freeze ceremony

- **Decision:** generated PRD becomes development-ready only after mechanical + four-perspective audit passes with Critical=0 and Major=0.
- **Reason:** structure success is not production usability, but the old multi-layer Freeze ceremony is unnecessary.
- **Date:** 2026-08-10

### `Local` is the permanent development branch

- **Decision:** normal work continues directly on `Local`; no routine per-flow PRs to `main`.
- **Date:** 2026-08-10

### Repository is project memory

- **Decision:** repository owners are authoritative for continuity; chat is supporting context only.
- **Date:** 2026-08-10

### Project Document Generator and Voice Production remain separate owners

- **Decision:** upstream project definition/PRD work stays separate from downstream voice production.
- **Reason:** unresolved product decisions must not be invented inside voice text.
- **Date:** 2026-08-10

### Source intake uses one slim persistent recovery model

- **Decision:** Flow 2 uses originals + Source Inventory + Requirement Register + Intake State + concise review.
- **Date:** 2026-08-10

### Canonical PRD stays human-readable; renderer projection is derived

- **Decision:** `work/content.md` owns PRD meaning; `work/render-data.json` is derived only.
- **Date:** 2026-08-10

### Approved PRD template is preserved as a shell

- **Decision:** preserve the approved HTML presentation shell and regenerate only project-owned content surfaces.
- **Date:** 2026-08-10

### `Production Document Builder/` is Archived during migration

- **Decision:** preserve but do not extend/treat as active authority.
- **Date:** 2026-08-10

### Golden Samples are references, not project requirements

- **Decision:** samples demonstrate quality/structure only where explicitly defined.
- **Date:** 2026-08-10

### Adopt BuildIT principles, not BuildIT domain structure 1:1

- **Decision:** reuse ownership/continuity/validation/minimal-navigation principles without copying irrelevant MCP/Blockbench architecture.
- **Date:** 2026-08-10
