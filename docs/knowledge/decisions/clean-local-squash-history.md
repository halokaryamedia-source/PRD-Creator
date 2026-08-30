# Clean Local Squash History

Status: current

## Decision

PRD-Creator separates working history from approved integration history:

```text
develop  → active development history; may contain many working commits
Local    → approved milestone history; exactly one commit per approved update
main     → existing stable/release lineage; intentionally unchanged until a separate migration decision
```

## Promotion contract

A coherent approved update moves from `develop` to `Local` only after `Local Promotion Verify` passes.

The pull request must be merged with **squash merge**.

```text
many develop commits
→ one approved logical update
→ squash merge
→ exactly +1 commit on Local
```

After the squash merge, `develop` must be synchronized/reset to the resulting `Local` HEAD before the next development cycle begins. Development must not continue from the pre-squash chain.

## Clean baseline

The current clean-history migration establishes one root baseline commit for `Local` and `develop`. The previous shared history is retained only through an explicit legacy safety reference for recovery/audit purposes.

This is a one-time explicitly authorized history migration, not a routine cleanup technique.

## Main boundary

`main` is outside the current `Local`/`develop` history reset. Because the new clean lineage is intentionally unrelated to the existing `main` lineage, normal `Local` → `main` promotion is paused.

A later explicit main migration/release decision must define how `main` adopts or replaces its legacy history before stable promotion resumes.

## Non-goals

This decision does not:

- require every development save to become a Local commit;
- preserve development checkpoint noise in Local history;
- rewrite `main` as part of this migration;
- change PRD/Voice product semantics;
- authorize automatic tags or GitHub Releases;
- make force-push/history rewrite a normal repository maintenance tool.

## Enforcement

- repository development happens on `develop`;
- `Local Promotion Verify` is the integration gate;
- `develop` → `Local` promotion uses squash merge;
- one approved promotion equals exactly one new `Local` commit;
- `develop` is synchronized to `Local` after promotion;
- `Local` keeps non-fast-forward/deletion protection after the one-time baseline migration;
- `main` release promotion remains deferred until its explicit migration decision.
