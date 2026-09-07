# PRD-Creator

PRD-Creator is an AI-assisted production system for turning game-project evidence and discussion into a revision-bound approved project model, a development-ready PRD, required Production Assets, and optional downstream Voice Production.

## Input → Output

| Input | Processing | Output |
|---|---|---|
| Project discussion / current instruction | authority-aware requirement recovery | approved requirement revision |
| Authoritative/reference sources | provenance + integrated synthesis | canonical PRD meaning |
| Approved gameplay/build needs | strict production-resource extraction | 04 Production Assets |
| Approved Voice needs | Flow 5–7 extraction/writing/validation | Eleven v3-ready Voice Production |

Normal delivery:

```text
output/
├── README.md
└── v<document.version>/
    ├── prd.html
    ├── context.md
    └── index.json
```

Generated delivery is never source of truth. Fix the first wrong canonical owner and regenerate.

## Branch Model

```text
develop  → default active repository development
Local    → clean verified integration baseline; one commit per approved update
main     → stable repository history
```

This is the repository default. A current explicit user instruction may select a different working branch for a specific task; that instruction does not silently redefine permanent branch governance.

Normal `develop` → `Local` promotion uses a verified squash boundary. `Local` → `main` remains explicit stable promotion. Version tags/releases are created only for approved feature/capability releases, not maintenance-only changes.

Repository behavior is routed by [AGENTS.md](AGENTS.md); GitHub execution policy by [GITHUB_RULES.md](GITHUB_RULES.md).

## Developer Quick Start

Prerequisite: **Python 3.11**.

Install pinned runtime + verification dependencies:

```bash
python -m pip install \
  -r requirements.lock.txt \
  -r requirements-dev.lock.txt
python -m pip check
```

Repository contracts:

```bash
python tools/verify_repository.py
```

Static source quality:

```bash
ruff format --check kits/prd-creator tests tools
ruff check kits/prd-creator tests tools
mypy \
  kits/prd-creator/shared \
  kits/prd-creator/renderer \
  kits/prd-creator/validator
```

PRD regression:

```bash
python -m unittest discover -s tests -p "test_prd_*.py" -v
```

Full regression + coverage:

```bash
coverage run -m unittest discover -s tests -p "test_*.py" -v
coverage report
```

Generate a project delivery:

```bash
python kits/prd-creator/renderer/delivery.py \
  workspace/active/<project>/
```

Validate current PRD:

```bash
python kits/prd-creator/validator/validate.py \
  workspace/active/<project>/
```

Project packages under `workspace/active/` / `workspace/archive/` are local/external production data and are not tracked in this public system repository.

## Package 3 Architecture

```text
kits/prd-creator/
├─ intake/              Flow 2 semantic procedure
├─ document/            PRD semantic/design/acceptance contracts
├─ production-assets/   04 resource contract
├─ voice/               Flow 5–7 semantic/craft/validation procedures
├─ shared/              strict machine contracts
├─ renderer/            deterministic rendering + transactional delivery
│  ├─ template_adapter.py
│  └─ static/
├─ validator/           canonical PRD/handoff/Voice mechanical gates
└─ template/            protected Golden/runtime bytes
```

Core machine invariants:

```text
requirement-register bytes
→ approved_requirement_sha256

content.md bytes
→ render-data.canonical_content_sha256

Owner ID
→ Moment ID
→ AST / VO resource identity

Flow 4 acceptance
→ exact render-data + asset-requirements SHA bindings

Flow 7 acceptance
→ exact voice-production SHA binding
```

Machine YAML is parsed by the shared duplicate-safe YAML loader. Persisted refs are normalized project-relative paths. Render data has one supported field vocabulary; renderer-side compatibility inference is retired.

## Repository Map

```text
.agents/skills/      reusable semantic judgment
docs/foundation/     durable Flow policy
docs/knowledge/      continuation, ownership, decisions, evidence
kits/prd-creator/    Flow 2–7 procedure + implementation
tests/               executable regression contracts
tools/               repository verification
workspace/           local/external project-package mount convention
.github/             CI / ownership / release policy
```

## Working Principle

```text
identify mode
→ find first wrong/changed owner
→ read only required context
→ update canonical source
→ regenerate derived output once
→ run the proof that can falsify the changed claim
→ stop
```

The current package version is owned by [kits/prd-creator/README.md](kits/prd-creator/README.md). See [CHANGELOG.md](CHANGELOG.md) for product history.

## License

This repository is **not open source**. It is publicly accessible for development convenience, but use is restricted to the copyright holder and explicitly authorized collaborators. See [LICENSE](LICENSE).
