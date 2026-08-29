# Repository Knowledge

Updated: 2026-08-30

This directory is the navigation and operating-memory layer for PRD-Creator. It does **not** define a second boot policy or duplicate the contracts owned by root/foundation/kits.

## Boot ownership

Root `../../AGENTS.md` owns how a session boots.

Key distinction:

```text
observe / recover repository context
→ read-only recovery + report

non-trivial Developing
→ full continuity recovery before edit

bounded mechanical Maintenance
→ smaller boot allowed only when wider context cannot change the decision
```

Do not use this directory index as a reason to broad-read every knowledge file.

## Current owners

| Need | Owner |
|---|---|
| Active continuation / resume checkpoint | `next-action.md` |
| Detailed work-routing explanation | `work-routing.md` |
| Repository/code/procedure ownership | `ownership.md` |
| Source/state authority | `source-authority.md` |
| Developing lifecycle overview | `workflows/development.md` |
| Maintenance workflow | `workflows/maintenance.md` |
| Skill inventory | `skills/README.md` |
| Ambiguous specialist selection | `skills/activation-matrix.md` |
| Durable decision index + current decision records | `decisions/README.md` |
| Decision-recording threshold | `decisions/recording-policy.md` |
| Current + historical review evidence | `reviews/README.md` |
| Future/non-active work | `operations/backlog.md` |
| Boot/routing regression scenarios | `operations/boot-baseline.md` |

Top-level work modes and session boot remain owned by root `AGENTS.md`. GitHub execution discipline remains owned by root `GITHUB_RULES.md`.

## Directory structure

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
│   ├── <current decision records>.md
│   └── <historical snapshots>.md
├── reviews/
│   ├── README.md
│   ├── current-validation.md
│   ├── template.md
│   └── <historical evidence>.md
└── operations/
    ├── boot-baseline.md
    └── backlog.md
```

## Separation rule

```text
active continuation       → next-action.md
durable choice/reason     → decisions/
current/historical proof  → reviews/
future/non-active work    → operations/backlog.md
production policy         → ../foundation/
project-specific state    → ../../workspace/
```

Historical reviews/decisions are evidence and rationale, not automatic current work. Current execution follows root routing plus the nearest current owner.
