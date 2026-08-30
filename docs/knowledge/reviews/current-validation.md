# Current Validation Status

Updated: 2026-08-31

This file records the current repository evidence state after the clean-history migration, branch-governance hardening, stable-routing alignment, and first published repository release.

## Current system state

Working branch: `develop`.  
Verified integration baseline: `Local`.  
Stable branch: `main`.  
Latest published repository release: `v0.1`.

PRD Creator package remains **v1.14.0**. Repository release versioning is separate from the product/package version rule; governance-only changes do not change PRD/Voice product semantics, Golden design, package behavior, or published repository version.

The current `main` contains later untagged repository-maintenance alignment after `v0.1`. No `v0.2` tag or GitHub Release exists. Historical commit/PR wording does not create a repository version; version publication requires the protected tag/GitHub Release action defined by the durable policy.

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
→ stable repository history
→ receives explicit Local stable promotions through normal merge commits
```

After each successful `develop` → `Local` squash promotion, `develop` is synchronized/reset to the resulting `Local` HEAD before new development starts.

A `Local` → `main` stable promotion uses `Stable release gate` and a normal merge commit. That main-only stable marker remains on `main`; `Local` continues its clean milestone sequence independently.

A new protected `v*` tag/GitHub Release is published only when the stable state includes an approved PRD-Creator feature/capability change. Maintenance-only governance, CI, ruleset, documentation, and repository-hygiene changes remain untagged.

## Current governance evidence

Repository rules currently establish:

- `develop` is protected from deletion only; normal direct development, working commits, and required post-squash synchronization remain available;
- `Local` is protected from deletion and non-fast-forward updates, requires linear history, requires a pull request, permits **squash only**, requires `Local promotion gate`, and uses strict up-to-date status checks;
- `main` is protected from deletion and non-fast-forward updates, requires a pull request, permits **merge only**, and requires `Stable release gate`;
- `main` intentionally uses non-strict required status checks, so `Local` is not forced to absorb prior main-only stable-marker commits before a stable PR can merge;
- Release Verify validates GitHub's pull-request merge candidate against the current `main` base;
- tags matching `refs/tags/v*` are protected from deletion and update;
- no configured ruleset bypass actor is present for these protected boundaries.

Repository release `v0.1` remains the latest published version. The server-side governance state matches the durable branch/stable-history decision, so repository professionalization is considered complete.

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
