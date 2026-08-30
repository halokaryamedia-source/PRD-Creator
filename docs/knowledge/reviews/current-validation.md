# Current Validation Status

Updated: 2026-08-30

This file records the current evidence state after the clean-history migration of `develop`, `Local`, and `main`.

## Current system state

Working branch: `develop`.  
Verified integration baseline: `Local`.  
Stable/release branch: `main`.

PRD Creator package remains **v1.14.0**. The history-model migration does not change PRD/Voice product semantics, Golden design, or package behavior.

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
→ receives explicit Local release promotions
```

After each successful `develop` → `Local` squash promotion, `develop` is synchronized/reset to the resulting `Local` HEAD before new development starts.

A `Local` → `main` release uses the Stable release gate and a normal merge commit. That release merge commit remains on `main`; `Local` continues its clean milestone sequence independently.

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

`Local` and `main` were then reset to that same root through explicit one-time user-authorized migrations. `develop` began from the same root and now carries normal post-baseline working commits.

Legacy recovery references are retained separately:

```text
legacy/pre-clean-local-2026-08-30
legacy/pre-clean-main-2026-08-30
```

The active branch lineage does not depend on those legacy histories.

## Product evidence boundary

Earlier browser/real-project evidence remains historical evidence for the exact project bytes tested before live project packages were removed from the tracked public system tree. This history migration does not claim new browser, audio, or project QA.

RQ-09 remains closed: Golden marker adaptation happens in a temporary template passed to the existing engine instead of mutating `_engine.STORAGE_PREFIX_TOKEN` at module scope.

## Current continuation

Current continuation is owned by `docs/knowledge/next-action.md`.
