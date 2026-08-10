# Decision Log

Use this note only for durable decisions whose reasons must survive future sessions. Active task status belongs in `next-action.md`.

## Current Decisions

### Flow 5 separates voice requirements from performance scripts

- **Decision:** `work/voice-requirements.md` owns which voice moments are justified and what each must communicate; final spoken wording/performance notation remains Flow 6.
- **Reason:** voice requirements are upstream production meaning, while performance wording is an implementation/art-direction layer. Combining them lets script polish silently invent or change project facts.
- **State:** `state/voice-state.yaml` stores status/revision/next step only.
- **Owners:** `docs/foundation/05-voice-requirement-extraction.md`, `kits/voice-production-kit/VOICE-EXTRACTION.md`.
- **Date:** 2026-08-10

### Flow 5 normally starts only from `handoff_ready`

- **Decision:** the normal downstream voice pipeline consumes the same accepted PRD revision already cleared for team handoff.
- **Reason:** the repository flow is intentionally sequential; using arbitrary generated/newer/older PRD content would make voice requirements drift from the production team document.
- **Revision rule:** if accepted PRD meaning changes, reset Flow 5 and re-check affected voice moments.
- **Date:** 2026-08-10

### Voice roles are functional patterns, not quotas

- **Decision:** Main Story and Radio Communication are standard roles demonstrated by the approved Voice Production reference, but no package is required to contain a fixed number of entries—or any voice at all.
- **Radio rule:** Radio requires an approved communicator/remote channel and must stay brief/useful during active play rather than repeat the full objective.
- **Other voice:** another type is allowed only when the PRD explicitly defines the speaker/channel; never use a generic invented `Other` role.
- **Reason:** Aftershock demonstrates varying counts and functions; copying its counts would turn a reference into a project requirement.
- **Date:** 2026-08-10

### `no_voice_required` is a valid Flow 5 result

- **Decision:** if accepted upstream evidence does not define or justify voice production for the current scope, stop with `no_voice_required` rather than inventing a narrator or dialogue system.
- **Reason:** the pipeline must serve project intent, not force every project through every artifact type.
- **Date:** 2026-08-10

### Flow 4 uses one development-readiness gate instead of Content Freeze ceremony

- **Decision:** generated PRD becomes `development_ready` only after mechanical validation plus New Reader, Level Designer, Developer, and Project Consistency audits pass with Critical=0 and Major=0.
- **Reason:** renderer success proves structure, not whether downstream roles can work without inventing product rules. One evidence-backed gate is sufficient; the Archived Mini Audit / Freeze / release layers are unnecessary ceremony for the current workflow.
- **Minor rule:** Minor may remain only when meaning stays safe/implementable and the open item is intentionally recorded.
- **Handoff:** `handoff_ready` adds a concise `team-handoff.md`; it is not client approval, QA, release approval, or implementation completion.
- **Owners:** `docs/foundation/04-prd-validation-handoff.md`, `kits/project-document-generator/VALIDATION.md`.
- **Date:** 2026-08-10

### `Local` is the permanent development branch

- **Decision:** normal repository work continues directly on `Local`; do not create per-flow branches or routine PRs to `main`.
- **Reason:** iterative same-workflow development does not benefit from per-flow PR ceremony.
- **Boundary:** `main` remains stable and changes only when explicitly requested.
- **Date:** 2026-08-10

### Repository is project memory

- **Decision:** repository state is authoritative for continuity; old chat is supporting context only.
- **Reason:** new sessions must resume without requiring the user to reconstruct history.
- **Owners:** `AGENTS.md`, `CONTEXT.md`, `docs/knowledge/next-action.md`.
- **Date:** 2026-08-10

### Project Document Generator and Voice Production remain separate production owners

- **Decision:** keep project requirement/PRD work upstream and voice production downstream.
- **Reason:** missing project decisions must not be invented inside voice scripts.
- **Owner:** `docs/foundation/00-product-boundaries.md`.
- **Date:** 2026-08-10

### Source intake uses one slim persistent recovery model

- **Decision:** Flow 2 keeps originals, one Source Inventory, one Requirement Register, one Intake State, and concise `review.md`.
- **Recovered from old package:** persistent state, source audit, conflict visibility, approval boundaries.
- **Not retained:** mandatory 12-phase ceremony or forced Guided Discussion when evidence already supports completion.
- **Owner:** `docs/foundation/02-source-intake-recovery.md`, `kits/project-document-generator/SOURCE-INTAKE.md`.
- **Date:** 2026-08-10

### Canonical PRD stays human-readable; renderer structure is derived

- **Decision:** `work/content.md` owns project-document meaning; `work/render-data.json` is a derived rendering projection only.
- **Reason:** developers/production reviewers need readable canonical content, while deterministic dynamic HTML still benefits from structured render data. Keeping the projection derived prevents a second competing source of truth.
- **Owner:** `kits/project-document-generator/CONTENT-CONTRACT.md`, `RENDERING.md`.
- **Date:** 2026-08-10

### Approved template is preserved as a shell, not reconstructed

- **Decision:** active renderer preserves the approved template head/CSS/JS/controls/sidebar shell and regenerates only project-owned metadata/navigation/pages/glossary.
- **Reason:** literal replacement was too fragile for dynamic packages, while rebuilding the full template would risk visual drift.
- **Owner:** `kits/project-document-generator/RENDERING.md`, `renderer/`.
- **Date:** 2026-08-10

### `Production Document Builder/` is Archived during migration

- **Decision:** preserve the package but do not treat it as active authority or extend it by default.
- **Reason:** it contains useful historical evidence but should not force heavy process architecture back into the active workflow.
- **Removal condition:** useful behavior/dependencies are migrated or intentionally retired in owning flows.
- **Date:** 2026-08-10

### Golden Samples are references, not project requirements

- **Decision:** Golden Samples define demonstrated structure/presentation/tone/density/quality only where explicitly stated.
- **Reason:** sample-specific objectives, mechanics, characters, scoring, counts, or lines must not leak into unrelated projects.
- **Owner:** `AGENTS.md`.
- **Date:** 2026-08-10

### Adopt BuildIT principles, not BuildIT domain structure 1:1

- **Decision:** reuse ownership, continuity, validation, minimal navigation, and anti-slop principles without copying Blockbench/MCP-specific architecture.
- **Reason:** this production domain should remain compact and purpose-specific.
- **Date:** 2026-08-10
