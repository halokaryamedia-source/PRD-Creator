# Repository Knowledge

Updated: 2026-08-13

This directory is the navigation and operating-memory layer for PRD-Creator. Use one owner per question; do not broad-read the whole directory.

## Start Here

For a normal session:

1. `../../AGENTS.md` — repository rules, work modes, proof, branch policy.
2. `../../CONTEXT.md` — stable product context and production boundaries.
3. `next-action.md` — current status and the single continuation point.
4. Open only the smallest owner needed after that.

## Current Owners

| Need | Owner |
|---|---|
| Work-mode routing | `work-routing.md` |
| Repository/code/procedure ownership | `ownership.md` |
| Source/state authority | `source-authority.md` |
| Developing workflow | `workflows/development.md` |
| Maintenance workflow | `workflows/maintenance.md` |
| Skill inventory | `skills/README.md` |
| Skill selection | `skills/activation-matrix.md` |
| Durable decision register | `decisions/README.md` |
| Decision-recording threshold | `decisions/recording-policy.md` |
| Current + historical review evidence | `reviews/README.md` |
| Future/non-active work | `operations/backlog.md` |
| Boot/routing regression baseline | `operations/boot-baseline.md` |

## Directory Structure

```text
docs/knowledge/
├── README.md
├── next-action.md
├── work-routing.md
├── ownership.md
├── source-authority.md
├── workflows/
│   ├── development.md
│   ├── maintenance.md
│   └── maintenance-note-template.md
├── skills/
│   ├── README.md
│   └── activation-matrix.md
├── decisions/
│   ├── README.md
│   ├── recording-policy.md
│   └── <decision records>.md
├── reviews/
│   ├── README.md
│   ├── current-validation.md
│   ├── template.md
│   └── <historical evidence>.md
└── operations/
    ├── boot-baseline.md
    └── backlog.md
```

## Separation Rule

```text
active task              → next-action.md
durable choice/reason    → decisions/
current/historical proof → reviews/
future work              → operations/backlog.md
production policy        → ../foundation/
project-specific state   → ../../workspace/
```

Historical review bodies remain capture-time evidence. Current policy comes from active owners, not from whichever audit has the strongest wording.
