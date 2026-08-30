# Clean Milestone and Release History

Status: current

## Decision

PRD-Creator separates working, approved milestone, and release history:

```text
develop  → active development history; may contain many working commits
Local    → approved milestone history; exactly one commit per approved update
main     → stable release history; explicit release boundaries
```

All three active branches originate from the same clean professional root baseline. Pre-reset history is retained only through dedicated legacy safety branches.

## Develop → Local promotion

A coherent approved update moves from `develop` to `Local` only after `Local Promotion Verify` passes.

The pull request must use **squash merge**:

```text
many develop commits
→ one approved logical update
→ squash merge
→ exactly +1 commit on Local
```

After the squash merge, `develop` must be synchronized/reset to the resulting `Local` HEAD before the next development cycle begins. Development must not continue from the pre-squash chain.

## Local → main release

A stable release moves from `Local` to `main` only after `Stable release gate` passes and the release is explicitly approved.

Use a normal merge commit for this boundary:

```text
Local approved milestones
→ release PR
→ Stable release gate
→ merge commit on main
```

The release merge commit is a `main`-only release marker. Do not reset `Local` or `develop` to that merge commit. Future Local milestones continue from the clean Local sequence and future release PRs merge those milestones into `main`.

Git tags and GitHub Releases remain separate explicit publishing actions.

## Clean baseline

The history migration established one root baseline commit shared by `develop`, `Local`, and `main`. Each root was verified from the same prepared repository tree before activation.

This was a one-time explicitly authorized history migration, not a routine cleanup technique.

Legacy recovery references:

```text
legacy/pre-clean-local-2026-08-30
legacy/pre-clean-main-2026-08-30
```

## Non-goals

This decision does not:

- require every development save to become a Local commit;
- preserve development checkpoint noise in Local history;
- make release merge commits part of Local milestone history;
- change PRD/Voice product semantics;
- authorize automatic tags or GitHub Releases;
- make force-push/history rewrite a normal repository maintenance tool.

## Enforcement

- repository development happens on `develop`;
- `Local Promotion Verify` is the integration gate;
- `develop` → `Local` uses squash merge;
- one approved promotion equals exactly one new `Local` commit;
- `develop` is synchronized to `Local` after promotion;
- `Stable release gate` validates `Local` → `main` release PRs;
- `Local` and `main` retain non-fast-forward/deletion protection after the one-time migration.
