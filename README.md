# PRD-Creator

PRD-Creator is an AI-assisted production system for turning game-project discussion and source material into an approved project model, a development-ready PRD, required Production Assets, and optional downstream Voice Production.

## What Goes In / What Comes Out

| Input | PRD-Creator | Output |
|---|---|---|
| Project discussion and approved decisions | requirement recovery | structured project model |
| Reference/source documents | authority-aware intake | development-ready PRD |
| Approved gameplay/build requirements | production planning | 04 Production Assets |
| Approved Voice needs | Voice extraction + writing | Eleven v3-ready Voice Production |

Normal versioned delivery:

```text
output/
├── README.md
└── v<document.version>/
    ├── prd.html       # human-facing project document
    ├── context.md     # AI/development context
    └── index.json     # compact navigation + line ranges
```

Generated delivery is never source of truth. Fix canonical project state first, then regenerate only the invalidated output.

## Branch Model

```text
develop  → active repository development
Local    → verified integration / stable working baseline
main     → stable release branch
```

Normal repository changes happen on `develop`. Promote `develop` to `Local` through a dedicated pull request after the Local promotion gate passes. Promote `Local` to `main` only for an explicit release after the Stable release gate passes.

Use merge commits at both promotion boundaries, then fast-forward the lower branch(es) to the promoted branch so ancestry stays synchronized:

```text
develop → Local → main
   ↑         ↑       │
   └─────────┴───────┘ sync promoted ancestry back down
```

Do not develop independently on `Local` or `main`. `Local` exists so active work can be isolated without moving the current verified baseline.

Repository behavior is routed by [AGENTS.md](AGENTS.md). GitHub execution is governed by [GITHUB_RULES.md](GITHUB_RULES.md). Stable product orientation lives in [CONTEXT.md](CONTEXT.md).

## Developer Quick Start

Prerequisite: **Python 3.11**. The current verification environment has no third-party Python runtime dependencies.

Repository contract check:

```bash
python tools/verify_repository.py
```

PRD regression suite:

```bash
python -m unittest \
  tests.test_prd_contracts \
  tests.test_prd_content_purity \
  tests.test_prd_delivery \
  tests.test_prd_voice_assets \
  tests.test_prd_handoff_contracts \
  tests.test_prd_flow2_state_contracts \
  tests.test_prd_hierarchy_contracts \
  tests.test_prd_golden_reference
```

Voice regression suite:

```bash
python -m unittest tests.test_voice_contracts
```

Generate the current delivery for a project package:

```bash
python kits/prd-creator/renderer/delivery.py \
  workspace/active/<project>/
```

Validate a project revision:

```bash
python kits/prd-creator/validator/validate.py \
  workspace/active/<project>/
```

Project packages under `workspace/active/` and `workspace/archive/` are **local/external production data and are not tracked by this public system repository**. Only the workspace guides are committed. See [workspace/README.md](workspace/README.md) and [SECURITY.md](SECURITY.md).

## Repository Map

```text
.agents/skills/      reusable semantic judgment
docs/foundation/     durable Flow policy
docs/knowledge/      continuation, ownership, decisions, evidence
kits/prd-creator/    Flow 2–7 procedure + implementation
tests/               executable regression contracts
tools/               repository verification
workspace/           local/external project-package mount points
.github/             CI, ownership, and pull-request policy
```

For product history, see [CHANGELOG.md](CHANGELOG.md). For contribution and promotion rules, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Working Principle

```text
identify mode
→ find first changed owner
→ read affected context only
→ change canonical source
→ regenerate only invalidated output
→ run the cheapest relevant proof
→ stop
```

## Package Version

The current package version is owned by [kits/prd-creator/README.md](kits/prd-creator/README.md). Repository hygiene, CI, documentation clarification, and branch-governance changes do not bump the package version by themselves.

## License

This repository is **not open source**. It is publicly accessible for development convenience, but use is restricted to the copyright holder and explicitly authorized collaborators. See [LICENSE](LICENSE).
