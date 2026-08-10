# Workspace Map

## Main Areas

- `../../AGENTS.md` — repository-wide work modes, branch policy, authority, root-cause/proof/anti-slop baseline.
- `../../CONTEXT.md` — stable product context/terminology and layer separation.
- `../../.agents/skills/` — canonical repository-wide agent skill root.
- `../foundation/` — durable production policy + current proof matrix.
- `flow.md` — agent Plan / Developing / Maintenance routing.
- `flows/development-flow.md` — Developing route.
- `maintenance/maintenance-flow.md` — root-cause-first Maintenance route.
- `skills/activation-matrix.md` — skill selection by semantic owner.
- `skills/skill-map.md` — root skill inventory, lineage, and freeze rule.
- `modules/module-map.md` — repository-area ownership and new-owner gate.
- `sources/source-map.md` — source/authority routing.
- `reviews/review-graph.md` — current meaning of historical review evidence.
- `decisions/change-decision-guide.md` — durable decision / coordinated-change threshold.
- `next-action.md` — one active continuation point.
- `decision-log.md` — durable decisions/reasons.
- `implementation-map.md` — exact current product/code/procedure owner map.
- `operations/context-boot-baseline.md` — expected efficient boot/routing scenarios.
- `operations/task-board.md` — future/non-active work.
- `../../kits/project-document-generator/` — detailed PRD Flow 2–4 production implementation/procedure.
- `../../kits/voice-production-kit/` — detailed Voice Flow 5–7 production implementation/procedure.
- `../../workspace/` — per-project source/state/canonical work/evidence/output.

## Root Skill Set

```text
.agents/skills/
├── development-brief/
├── project-document-production/
└── voice-production/
```

Root skills route/judge repository work. Kit-local `SKILL.md` files remain detailed production procedures and are not alternate root skill directories.

## Ownership Map Rule

```text
module-map         → repository area owner
source-map         → claim/source authority
implementation-map → exact implementation/procedure location
```

Use the smallest map needed; do not broad-read all three by default.

## Evidence / State Rule

```text
review body        → captured historical evidence
review-graph       → current meaning of that evidence
decision log       → durable chosen rule
next-action        → current active work state
task-board         → future/non-active work
```

Do not merge these responsibilities into one note.

## Fast Rule

```text
new session
→ AGENTS
→ CONTEXT
→ next-action
→ smallest relevant owner
→ activation matrix only if a skill must be selected
```

Historical implementation details are recovered from Git history only when genuinely needed; current project meaning comes from active owners.
