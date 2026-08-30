# Repository Knowledge

Updated: 2026-08-30

This directory is the navigation and operating-memory layer for PRD-Creator. It does not define a second boot policy or duplicate contracts owned by root/foundation/kits.

## Boot ownership

Root `../../AGENTS.md` owns how a session boots.

```text
observe / recover repository context
→ read-only recovery + report

non-trivial Development
→ full continuity recovery before edit

bounded mechanical Maintenance
→ smaller boot only when wider context cannot change the decision
```

Do not use this directory index as a reason to broad-read every knowledge file.

## Current owners

| Need | Owner |
|---|---|
| Active continuation / resume checkpoint | `next-action.md` |
| Detailed work-routing explanation | `work-routing.md` |
| Repository/code/procedure ownership | `ownership.md` |
| Source/state authority | `source-authority.md` |
| Development lifecycle overview | `work-modes/development.md` |
| Maintenance workflow | `work-modes/maintenance.md` |
| Skill inventory | `skills/README.md` |
| Ambiguous specialist selection | `skills/activation-matrix.md` |
| Durable decision index | `decisions/README.md` |
| Current validation evidence | `reviews/current-validation.md` |
| Historical review evidence | `reviews/history/` |
| Future/non-active work | `operations/backlog.md` |
| Boot/routing regression scenarios | `operations/boot-baseline.md` |

Top-level work modes/session boot remain owned by root `AGENTS.md`. GitHub execution remains owned by root `GITHUB_RULES.md`.

## Directory structure

```text
docs/knowledge/
├── README.md
├── next-action.md
├── work-routing.md
├── ownership.md
├── source-authority.md
├── work-modes/
├── skills/
├── decisions/
├── reviews/
└── operations/
```

## Separation rule

```text
active continuation       → next-action.md
durable choice/reason     → decisions/
current proof             → reviews/current-validation.md
historical proof          → reviews/history/
future/non-active work    → operations/backlog.md
production policy         → ../foundation/
project-specific state    → external/local project package, normally mounted under ../../workspace/
```

Historical reviews/decisions are evidence and rationale, not automatic current work. Current execution follows root routing plus the nearest current owner.
