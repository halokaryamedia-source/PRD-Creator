# Minimal Navigation

Use this as the shortest resume path.

## Resume First

1. `../../AGENTS.md` — work modes, authority, root-cause/proof rules, skill budget.
2. `../../CONTEXT.md` — stable product facts and terminology.
3. `next-action.md` — single active task/state and next step.

Do not ask the user to reconstruct previous work before checking these owners.

## Then, Only If Needed

- `flow.md` — when the correct Plan / Developing / Maintenance route is unclear.
- `skills/activation-matrix.md` — when selecting a repository specialist.
- `modules/module-map.md` — when repository-area ownership/new-file placement is unclear.
- `sources/source-map.md` — when the authoritative source/state/artifact for a claim is unclear.
- `maintenance/maintenance-flow.md` — for bugs/regressions/cleanup.
- `reviews/review-graph.md` — only when historical review/evidence status matters.
- `decisions/change-decision-guide.md` — only when a durable/cross-owner decision threshold is unclear.
- `decision-log.md` — when the reason behind a durable decision matters.
- `../foundation/README.md` — when stable production policy matters.
- `implementation-map.md` — when exact current product/code/procedure owner is unclear.
- affected kit/project source — when actual implementation/content behavior must be inspected.

## Developing Shortcut

For non-trivial create/change work:

```text
boot
→ .agents/skills/development-brief/SKILL.md
→ at most one specialist when useful
→ affected kit/project owner
```

Do not open every root skill. The activation matrix chooses the smallest semantic owner.

## Maintenance Shortcut

For a concrete bug/regression/cleanup:

```text
boot
→ observe defect/drift
→ maintenance/maintenance-flow.md
→ smallest semantic owner
→ targeted proof
```

Do not invoke `development-brief` by default for Maintenance.

## Stop Rule

If the answer is not in the boot context, open the smallest relevant owner next. Do not broad-scan saved projects, all references, generated output, every skill, reviews, task board, or old chats by default.
