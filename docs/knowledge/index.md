# Knowledge Dashboard

Use this page to navigate current project memory.

```text
agent behavior/routing     → ../../AGENTS.md + flow.md
stable product context     → ../../CONTEXT.md
current task               → next-action.md
production policy          → ../foundation/
skill inventory/routing    → skills/
durable decisions          → decision-log.md
implementation ownership   → implementation-map.md
future work                → operations/task-board.md
```

## Start Here

1. `../../AGENTS.md`
2. `../../CONTEXT.md`
3. `next-action.md`
4. only the relevant foundation/source/kit after that
5. `skills/activation-matrix.md` only when selecting a skill

## Key Notes

- `minimal-nav.md` — shortest resume path.
- `flow.md` — agent Plan / Developing / Maintenance routing; separate from product Flow 2–7.
- `flows/development-flow.md` — mandatory Developing route and dual Build/Acceptance gate.
- `skills/activation-matrix.md` — smallest-correct-owner skill routing.
- `skills/skill-map.md` — canonical root skill inventory, ownership, lineage, and freeze rule.
- `next-action.md` — one active goal, current state, preserved boundaries, and one next step.
- `decision-log.md` — decisions whose reasons must survive later sessions.
- `implementation-map.md` — current product/code/procedure owners and locations.
- `workspace-map.md` — top-level repository map.
- `operations/task-board.md` — future/non-active work only.

## Root Skill Set

```text
development-brief
project-document-production
voice-production
```

The root skill set is intentionally small. Detailed production procedures remain under `kits/`; do not duplicate them into `.agents/skills/`.

## Maintenance Rule

One note, one job. Do not duplicate current status across every document. Historical information should remain historical instead of being rewritten as if newly observed.

Do not create a new skill/note merely because BuildIT has a similarly named file; copy the ownership discipline and routing behavior, not its domain inventory.
