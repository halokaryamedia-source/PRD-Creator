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
develop  → active repository development; working commits may be numerous
Local    → clean approved integration history; one commit per approved update
main     → stable repository history; tagged releases are feature-bearing publish points
```

Normal repository changes happen on `develop`.

A coherent approved update is promoted from `develop` to `Local` through a dedicated pull request after the Local promotion gate passes. The promotion must use **squash merge**, so all working commits for that approved update become exactly one new commit on `Local`.

After a successful squash promotion, synchronize `develop` back to the resulting `Local` HEAD before starting the next development cycle.

An approved stable update is promoted from `Local` to `main` through a dedicated pull request after `Stable release gate` passes. Use a normal merge commit so `main` records the stable boundary while `Local` keeps its clean milestone sequence.

A `main` promotion is not automatically a versioned release. Create a new protected `v*` tag and GitHub Release only when an approved PRD-Creator feature/capability changes. Governance, CI, ruleset, documentation, and other maintenance-only updates remain untagged.

Repository behavior is routed by [AGENTS.md](AGENTS.md). GitHub execution is governed by [GITHUB_RULES.md](GITHUB_RULES.md). Stable product orientation lives in [CONTEXT.md](CONTEXT.md).

## Developer Quick Start

Prerequisite: **Python 3.11**.

Install exact runtime + verification dependencies:

```bash
python -m pip install --no-deps \
  -r requirements.lock.txt \
  -r requirements-dev.lock.txt
```

Repository contract check:

```bash
python tools/verify_repository.py
```

Static source quality:

```bash
ruff check \
  kits/prd-creator/shared \
  kits/prd-creator/validator \
  kits/prd-creator/renderer/render.py \
  kits/prd-creator/renderer/delivery.py \
  kits/prd-creator/renderer/production_assets.py \
  kits/prd-creator/renderer/production_assets_compositor.py

mypy kits/prd-creator/shared
```

PRD regression suite:

```bash
python -m unittest discover -s tests -p "test_prd_*.py" -v
```

Full regression suite:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
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

Project packages under `workspace/active/` and `workspace/archive/` are **local/external production data and are not tracked by this public system repository**. Only workspace guides are committed. See [workspace/README.md](workspace/README.md) and [SECURITY.md](SECURITY.md).

## Source Architecture

```text
kits/prd-creator/
├─ shared/              typed shared state/Voice parsers
├─ renderer/            deterministic projection + delivery
├─ validator/           canonical PRD/handoff/Voice gates
├─ document/            semantic/design/acceptance contracts
├─ production-assets/   non-Voice 04 resource contract
├─ voice/               Flow 5–7 Voice contracts
└─ template/            approved Golden/runtime bytes
```

Machine-owned YAML is parsed as real YAML. Production Assets/Voice placement uses stable IDs rather than display-title joins. PRD handoff acceptance binds exact render-data bytes.

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

The current package version is owned by [kits/prd-creator/README.md](kits/prd-creator/README.md). Repository hygiene, CI, documentation clarification, and branch-governance changes do not bump the package version by themselves and do not create a new repository release unless a feature/capability also changes.

## License

This repository is **not open source**. It is publicly accessible for development convenience, but use is restricted to the copyright holder and explicitly authorized collaborators. See [LICENSE](LICENSE).
