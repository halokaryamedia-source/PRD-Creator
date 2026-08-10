# Knowledge Dashboard

Use this page to navigate current project memory.

```text
agent behavior/routing     → ../../AGENTS.md + flow.md
stable product context     → ../../CONTEXT.md
current task               → next-action.md
production policy/proof    → ../foundation/
skill inventory/routing    → skills/
module ownership           → modules/
source authority           → sources/
maintenance procedure      → maintenance/
review evidence lifecycle  → reviews/
durable decisions          → decision-log.md + decisions/
implementation location    → implementation-map.md
future/non-active work     → operations/task-board.md
```

## Start Here

1. `../../AGENTS.md`
2. `../../CONTEXT.md`
3. `next-action.md`
4. only the relevant foundation/source/kit/project owner after that
5. `skills/activation-matrix.md` only when selecting a skill

Do not load the task board, review graph, or every map during normal boot unless the active boundary requires them.

## Key Notes

- `minimal-nav.md` — shortest resume path.
- `flow.md` — agent Plan / Developing / Maintenance routing; separate from product Flow 2–7.
- `flows/development-flow.md` — mandatory Developing route and dual Build/Acceptance gate.
- `maintenance/maintenance-flow.md` — root-cause-first bug/regression/cleanup route.
- `skills/activation-matrix.md` — smallest-correct-owner skill routing.
- `skills/skill-map.md` — canonical root skill inventory, ownership, lineage, and freeze rule.
- `modules/module-map.md` — top-level repository responsibility boundaries and new-owner gate.
- `sources/source-map.md` — source/authority routing without duplicating source content.
- `reviews/review-graph.md` — current meaning of historical reviews/evidence.
- `decisions/change-decision-guide.md` — when to persist a durable decision or coordinated change contract.
- `next-action.md` — one active goal, current state, preserved boundaries, and one next step.
- `decision-log.md` — decisions whose reasons must survive later sessions.
- `implementation-map.md` — exact current product/code/procedure owners and locations.
- `workspace-map.md` — top-level repository map.
- `operations/context-boot-baseline.md` — expected efficient boot/routing scenarios.
- `operations/task-board.md` — future/non-active work only.

## Root Skill Set

```text
development-brief
project-document-production
voice-production
```

The root skill set is intentionally small. Detailed production procedures remain under `kits/`; do not duplicate them into `.agents/skills/`.

## Review / Decision / Status Separation

```text
historical evidence/current review meaning → reviews/
durable choice/reason                     → decision-log.md / decisions/
active work state                          → next-action.md
future work                                → operations/task-board.md
```

Do not allow one note to become all four.

## Maintenance Rule

One note, one job. Extend the canonical owner before creating another note. Historical information remains historical instead of being rewritten as if newly observed.

Do not create a new skill/note merely because BuildIT has a similarly named file; copy the ownership discipline and routing behavior, not its domain inventory.
