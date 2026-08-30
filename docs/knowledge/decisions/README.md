# Decision Index

This directory stores durable repository/product decisions whose reasons must survive future sessions.

**Current execution does not start from historical decision prose.** Use `../next-action.md` for active continuation, `../ownership.md` for current owners, `../source-authority.md` for precedence, and the nearest current foundation/kit contract for exact behavior.

## Current Durable Decisions

| Decision | Current status / owner |
|---|---|
| Repository development uses `develop → Local → main` with verified promotion boundaries and ancestry synchronization | [three-tier-branch-promotion.md](three-tier-branch-promotion.md) |
| The public PRD-Creator repository stores the system; live project packages remain ignored/local or external/private | [project-data-boundary.md](project-data-boundary.md) |
| PRD-Creator uses one categorized implementation package under `kits/prd-creator/` while Project/PRD and Voice semantics remain separate | Current architecture; see [Product Boundaries](../../foundation/00-product-boundaries.md), [Ownership](../ownership.md), and [kit routing](../../../kits/prd-creator/AGENTS.md) |
| Golden reference is the binding PRD-core representation/runtime prototype; project facts still come only from current project authority | [golden-reference-fidelity.md](golden-reference-fidelity.md) |
| Root skills remain semantic/product-contract owners; pure renderer/validator mechanics stay with exact implementation owners | [technical-ownership-boundary.md](technical-ownership-boundary.md) |
| Do not add frameworks, compatibility layers, extra skills, schemas, artifacts, or proof machinery without a demonstrated need | [anti-overdevelopment-simplification.md](anti-overdevelopment-simplification.md) |
| Formal durable change records require a real cross-owner/migration/compatibility threshold | [recording-policy.md](recording-policy.md) |
| Repository verification remains small, deterministic, and limited to repeatable repository invariants | [operating-parity-gates.md](operating-parity-gates.md), now historical/refined by current repository structure |

## Historical / Superseded Context

- [buildit-parity-reassessment.md](buildit-parity-reassessment.md) records a former parity-remediation phase. It is not active work unless `next-action.md` explicitly reopens it.
- [operating-parity-gates.md](operating-parity-gates.md) contains captured Phase 1–3 terminology and paths. Current routing/verification owners override stale captured paths.

Git history is the recovery mechanism for retired long-form decision registers and older architecture. Do not keep live snapshot files or compatibility paths solely for archaeology.

## How to Read Decisions

```text
Need current task/status?
→ ../next-action.md

Need current owner?
→ ../ownership.md

Need source/state precedence?
→ ../source-authority.md

Need why a durable current boundary exists?
→ this index → matching decision file

Need old rationale/provenance only?
→ historical review / Git history
```

A historical decision may be true for the boundary it proved while still containing old names, paths, or delivery surfaces. Current owners always win for execution.

## Recording Rule

Create or materially update a decision only when the reason must survive sessions and cannot be represented cleanly by current state/owner documentation alone. Ordinary fixes, bounded revisions, temporary implementation notes, and active task status do not become durable decisions.

See [recording-policy.md](recording-policy.md) for the threshold.
