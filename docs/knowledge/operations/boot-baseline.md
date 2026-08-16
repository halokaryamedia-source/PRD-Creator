# Boot and Routing Baseline

Updated: 2026-08-17

This baseline records a small set of routing scenarios that protect context recovery without turning boot into repository-wide reading.

## Scenario A — new chat, observe/recover only

User intent examples: `amati repo ini`, inspect, understand, recover context.

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules when GitHub work is material
→ CONTEXT.md
→ next-action.md
→ smallest owner needed to explain current state
→ report understanding
→ STOP / NO EDIT
```

Pass when the agent can state what the repository is, current active boundary/next step, relevant constraints, and likely owner **without starting implementation or asking the user to reconstruct recoverable history**.

## Scenario B — non-trivial repository Developing

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules
→ CONTEXT.md
→ next-action.md
→ development-brief
→ smallest relevant owner/source
→ implementation only after the task is grounded
```

`CONTEXT.md` and `next-action.md` are mandatory here. Further reads remain bounded.

Pass when the agent preserves stable boundaries and active continuation, does not invent a new task from nearby TODO/audit/history, and uses the smallest owner/proof after bootstrap.

## Scenario C — bounded mechanical Maintenance

Example: an exact broken link or isolated implementation defect whose wider product context cannot change the correction.

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules when material GitHub work is involved
→ exact defect/owner
→ targeted proof
→ STOP
```

`CONTEXT.md` / `next-action.md` may be skipped only when they cannot materially change the decision. This fast path must not be used to bypass Developing continuity.

## Scenario D — normal project Production Execution

```text
AGENTS.md
→ current project state/evidence
→ matching production specialist
→ smallest active kit Flow owner
```

Normal production does not invoke `development-brief` merely because files are created or revised.

## Pass conditions

A route passes when:

- the user is not asked to repeat context that the repository can recover;
- observe/recover requests remain read-only unless implementation is also requested;
- non-trivial Developing always recovers stable context + active continuation first;
- bounded work does not broad-read unrelated repository/history;
- the correct semantic/technical owner is reached without redundant skills;
- backlog/reviews/old TODOs do not become active work automatically;
- evidence expectations match the execution channel;
- no ceremonial routing telemetry, session log, or extra state system is created.

Add or change a scenario only after a real routing failure exposes a missing case.
