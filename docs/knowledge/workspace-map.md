# Workspace Map

## Main Areas

- `../../AGENTS.md` — repository-wide work modes, branch policy, authority, root-cause/proof/anti-slop baseline.
- `../../CONTEXT.md` — stable product context/terminology and layer separation.
- `../../.agents/skills/` — canonical repository-wide agent skill root.
- `../foundation/` — durable production policy.
- `flow.md` — agent Plan / Developing / Maintenance routing.
- `skills/activation-matrix.md` — skill selection by semantic owner.
- `skills/skill-map.md` — root skill inventory, lineage, and freeze rule.
- `next-action.md` — one active continuation point.
- `decision-log.md` — durable decisions/reasons.
- `implementation-map.md` — current product/code/procedure owner map.
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
