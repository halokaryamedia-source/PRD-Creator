# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Bring PRD-Creator's **agent operating architecture** to the same level of discipline as BuildIT while preserving PRD-Creator's own domain boundaries and completed Flow 1–7 production pipeline.

## Current Status

`OPERATING_PARITY_PHASE_2_OWNERSHIP_REVIEW_MAINTENANCE_PROOF_IMPLEMENTED`

## Completed — Phase 1

Implemented:

- explicit work modes: Plan / Developing / Maintenance;
- root independent-judgment rule: user owns the goal, agent owns method quality;
- mandatory non-trivial Developing front door: `.agents/skills/development-brief/SKILL.md`;
- Build POV + Acceptance POV contract;
- 2–5 acceptance criteria + minimum-proof budget before implementation;
- root-cause/edit gate;
- ChatGPT→GitHub vs Local/Codex-style execution-channel distinction;
- BuildIT-style minimum useful proof and evidence escalation adapted to this product;
- canonical root skill set:
  - `development-brief`;
  - `project-document-production`;
  - `voice-production`;
- Developing skill budget: `development-brief` + at most one specialist;
- skill activation matrix + skill map/freeze rules;
- agent work-routing flow + Developing flow.

## Completed — Phase 2

Implemented:

- `docs/knowledge/modules/module-map.md` — repository-area ownership and new-file/module gate;
- `docs/knowledge/sources/source-map.md` — current authority/source routing without duplicating source content;
- `docs/knowledge/maintenance/maintenance-flow.md` + template — root-cause-first bug/regression/cleanup route;
- `docs/knowledge/reviews/review-graph.md` + template — historical review bodies remain immutable evidence while the graph owns current interpretation;
- `docs/knowledge/reviews/operating-architecture-parity-audit.md` — durable evidence for why parity work exists;
- `docs/knowledge/decisions/change-decision-guide.md` — decision-log vs review vs next-action vs task-board routing and cross-owner change threshold;
- `docs/knowledge/operations/context-boot-baseline.md` — expected efficient boot/routing scenarios and measurement fields;
- `docs/foundation/validation-report.md` — current evidence labels plus production and operating-layer status matrix;
- root/dashboard/navigation/ownership notes updated to route to these owners.

## Preserved Boundaries

Phase 2 does **not**:

- change Flow 2–7 production semantics;
- create a second state/planning hierarchy;
- convert reviews into current task trackers;
- make Maintenance use `development-brief` by default;
- create renderer/validator/DOCX/evidence skills;
- add CI/tests/frameworks merely because BuildIT has them;
- recreate retired schema/profile/freeze/packaging architecture.

## Current Operating Architecture

```text
boot
AGENTS → CONTEXT → next-action
↓
mode
Plan | Developing | Maintenance
↓
ownership / authority
module-map + source-map + implementation-map
↓
Developing only
 development-brief + at most one semantic specialist
↓
smallest owner change
↓
minimum useful proof
↓
review / decision / active-state owner updated only when applicable
```

## Remaining Operating-Parity Acceptance

Architecture is now substantially aligned, but final parity acceptance still needs actual usage evidence:

- exercise representative boot/routing scenarios from `operations/context-boot-baseline.md`;
- exercise at least one Maintenance route under the new structure;
- run a navigation/ownership consistency audit for stale/duplicate links;
- inspect nearest/local `AGENTS.md` value: Project Document kit currently has no local agent rules while Voice kit has a small local `AGENTS.md`;
- decide whether any additional automated engineering/CI gate is justified by current failure evidence rather than copied from BuildIT;
- produce a final current parity matrix.

## Next Step

Implement **Phase 3 — Operating Parity Acceptance**: exercise the new routing/maintenance architecture on representative repository scenarios, reconcile local-owner rules only where useful, audit navigation/ownership consistency, and decide evidence-first whether any engineering gate is still missing. Do not alter production semantics unless the acceptance run exposes a concrete defect.
