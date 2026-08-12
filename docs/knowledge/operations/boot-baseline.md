# Boot and Routing Baseline

Updated: 2026-08-13

This baseline checks that a new session reaches the correct owner without unnecessary repository-wide reading.

## Expected Boot

```text
AGENTS.md
→ CONTEXT.md
→ docs/knowledge/next-action.md
→ smallest relevant owner
```

Use `skills/activation-matrix.md` only when the correct specialist is genuinely ambiguous.

## Expected Routing

| Scenario | Mode | Expected route |
|---|---|---|
| Create/revise a PRD with the existing system | Production Execution | `project-document-production` → active PRD Flow owner |
| Create/revise Voice output from an accepted PRD | Production Execution | `voice-production` → active Voice Flow owner |
| Change PRD-Creator policy/skills/repository structure | Developing | `development-brief` + at most one useful specialist |
| Fix a concrete bug/regression | Maintenance | first wrong owner → smallest correction |
| Clean stale docs without changing architecture | Maintenance | current doc owner → link/ownership proof |
| Decide an ungrounded high-impact architecture change | Plan | inspect authority/ownership before editing |

Normal project Production Execution does **not** use `development-brief`.

## Pass Condition

A route passes when:

- the correct owner is reached without broad-reading unrelated docs/projects;
- project production is not misclassified as repository development;
- no redundant skill/state system is activated;
- evidence expectations match the execution channel;
- known repository context is reused instead of asking the user to reconstruct it.

Add a scenario only after a real routing failure exposes a missing case. Do not maintain ceremonial routing telemetry.
