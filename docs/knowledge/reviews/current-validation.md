# Current Validation Status

Updated: 2026-08-30

This file records the current evidence state for the clean `Local` / `develop` baseline.

## Current system state

Working branch: `develop`.  
Verified integration baseline: `Local`.  
Existing stable/release lineage: `main` (unchanged; explicit migration required before normal release promotion resumes).

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
→ existing legacy stable/release lineage
→ not rewritten by this migration
```

After each successful `develop` → `Local` squash promotion, `develop` is synchronized/reset to the resulting `Local` HEAD before new development starts.

## Baseline evidence

The clean baseline is created from the approved repository tree after repository professionalization. The baseline-construction proof requires all of the following before the root is accepted:

- root commit has no parent;
- root tree matches the prepared clean baseline source exactly;
- `python tools/verify_repository.py` passes;
- full `python -m unittest discover -s tests -p "test_*.py" -v` passes;
- `develop` and the clean Local candidate point to the same root commit before the protected `Local` ref is migrated.

Previous history is retained only through an explicit legacy safety reference for recovery/audit. The active clean lineage does not depend on that history.

## Product evidence boundary

Earlier browser/real-project evidence remains historical evidence for the exact project bytes tested before live project packages were removed from the tracked public system tree. This history migration does not claim new browser, audio, or project QA.

RQ-09 remains closed: Golden marker adaptation happens in a temporary template passed to the existing engine instead of mutating `_engine.STORAGE_PREFIX_TOKEN` at module scope.

## Current continuation

Current continuation is owned by `docs/knowledge/next-action.md`.
