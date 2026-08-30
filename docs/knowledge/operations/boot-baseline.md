# Boot and Routing Baseline

Updated: 2026-08-30

This baseline protects context recovery without turning boot into repository-wide reading. It is a small routing regression contract, not another workflow engine or telemetry system.

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

## Canonical Routing Regression Set

Use these examples when routing behavior is questioned. They define expected direction and the most important route that must **not** happen.

| Example request | Expected route | Must not |
|---|---|---|
| `Amati repo ini dan jelaskan statusnya.` | Plan / observe only | edit files, start `next-action`, run broad CI |
| `Update Objective 3 using this approved project change.` | bounded Production Execution → affected project owner | load `development-brief`, re-audit all source, replay unrelated objectives |
| `Create Voice Production from the accepted PRD.` | Production Execution → affected Flow 5–7 owner | treat as repository Developing |
| `Fix this renderer class; canonical content is already correct.` | Maintenance → exact renderer implementation owner | reopen project semantics or Voice without evidence |
| `Change how incomplete project sources are recovered before PRD creation.` | Developing → `development-brief` → source/intake semantic owner | treat as a one-project content revision |
| `Change GitHub transfer/retry behavior.` | Developing → `development-brief` + `GITHUB_RULES.md` owner | modify project/PRD production contracts |

If a real request does not fit these examples exactly, route by intent and first wrong owner rather than forcing analogy.

## Pass Conditions

A route passes when:

- the user is not asked to repeat context the repository can recover;
- observe/recover requests remain read-only unless implementation is also requested;
- non-trivial Developing recovers stable context + active continuation first;
- bounded work does not broad-read unrelated repository/history;
- the correct semantic/technical owner is reached without redundant skills;
- backlog/reviews/old TODOs do not become active work automatically;
- evidence expectations match the execution channel;
- Production revisions touch only invalidated scope unless an explicit expansion trigger is proven;
- no ceremonial routing telemetry, session log, or extra state system is created.

Add or change a scenario only after a real routing failure exposes a missing case.
