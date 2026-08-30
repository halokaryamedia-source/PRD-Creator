# Current Validation Status

Updated: 2026-08-31

This file records the current repository evidence state after the clean-history migration, branch-governance hardening, release-routing alignment, and first stable repository release.

## Current system state

Working branch: `develop`.  
Verified integration baseline: `Local`.  
Stable/release branch: `main`.  
First stable repository release: `v0.1`.

PRD Creator package remains **v1.14.0**. Repository release versioning is separate from the product/package version rule; governance-only changes do not change PRD/Voice product semantics, Golden design, or package behavior.

Current project-document authority shape remains:

```text
project discussion + original source + approved decisions
→ complete approved project model
→ canonical PRD / Production Assets / optional Voice
→ deterministic versioned delivery
→ output/README.md
→ output/v<document.version>/prd.html
→ output/v<document.version>/context.md
→ output/v<document.version>/index.json
```

Project package contents remain local/external production data rather than tracked public system-repository content.

## Clean history contract

```text
develop
→ active working history
→ may contain multiple implementation commits

Local
→ approved milestone history
→ one approved promotion = exactly one squash commit

main
→ clean stable/release history
→ receives explicit Local release promotions through normal merge commits
```

After each successful `develop` → `Local` squash promotion, `develop` is synchronized/reset to the resulting `Local` HEAD before new development starts.

A `Local` → `main` release uses the Stable release gate and a normal merge commit. That release merge commit remains on `main`; `Local` continues its clean milestone sequence independently.

## Current governance evidence

Repository rules currently establish:

- `Local` is protected from deletion and non-fast-forward updates, requires linear history, requires a pull request, permits **squash only**, requires `Local promotion gate`, and uses strict up-to-date status checks;
- `main` is protected from deletion and non-fast-forward updates, requires a pull request, permits **merge only**, and requires `Stable release gate`;
- `main` intentionally uses non-strict required status checks, so `Local` is not forced to absorb prior main-only release-marker commits before a release PR can merge;
- `Release Verify` validates GitHub's pull-request merge candidate against the current `main` base;
- tags matching `refs/tags/v*` are protected from deletion and update;
- no configured ruleset bypass actor is present for these protected boundaries.

Repository release `v0.1` points to the first explicit `main` release merge boundary. The server-side governance state now matches the durable branch/release decision, so repository professionalization is considered complete.

## Baseline evidence

Clean root baseline:

```text
29aec52a2d78cabfedd3abb771c8a31d67979ce7
```

The root commit has no parent and was created from the verified prepared repository tree. Before activation, the baseline construction passed:

- root-parent check;
- exact prepared-tree equality check;
- `python tools/verify_repository.py`;
- full `python -m unittest discover -s tests -p "test_*.py" -v` regression suite.

`Local` and `main` were then reset to that same root through explicit one-time user-authorized migrations. `develop` began from the same root and follows the normal working-history model from that baseline.

Legacy recovery references are retained separately:

```text
legacy/pre-clean-local-2026-08-30
legacy/pre-clean-main-2026-08-30
```

The active branch lineage does not depend on those legacy histories.

## Product evidence boundary

Earlier browser/real-project evidence remains historical evidence for the exact project bytes tested before live project packages were removed from the tracked public system tree. This repository-governance work does not claim new browser, audio, or project QA.

RQ-09 remains closed: Golden marker adaptation happens in a temporary template passed to the existing engine instead of mutating `_engine.STORAGE_PREFIX_TOKEN` at module scope.

## Current continuation

Current continuation is owned by `docs/knowledge/next-action.md`.
