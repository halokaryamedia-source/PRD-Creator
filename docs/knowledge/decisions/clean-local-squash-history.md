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

`Local` may require the promotion source to be up to date because `develop` is intentionally synchronized to each new Local milestone before the next cycle begins.

## Local → main release

A stable release moves from `Local` to `main` only after `Stable release gate` passes and the release is explicitly approved.

Use a normal merge commit for this boundary:

```text
Local approved milestones
→ release PR
→ Stable release gate on the PR merge candidate
→ merge commit on main
```

The release merge commit is a `main`-only release marker. Do not reset or merge `main` back into `Local` or `develop` merely to carry that marker downward. Future Local milestones continue from the clean Local sequence and future release PRs merge those milestones into `main`.

Because this divergence is intentional, `main` must not require `Local` to absorb prior main-only release-marker ancestry before a release PR can merge. Release verification instead validates GitHub's pull-request merge candidate against the current `main` base.

## Stable tags and repository releases

Git tags and GitHub Releases remain separate explicit publishing actions.

Stable repository tags use the `v*` namespace. Once created, a stable tag must not be moved or deleted. Creating the next tag remains an explicit release action and does not happen automatically after every `Local` or `main` update.

Repository release tags such as `v0.1` are separate from the PRD-Creator product/package version owned by `kits/prd-creator/README.md`.

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
- require `Local` to absorb main-only release markers;
- change PRD/Voice product semantics;
- authorize automatic tags or GitHub Releases;
- make force-push/history rewrite a normal repository maintenance tool.

## Enforcement

- repository development happens on `develop`;
- `Local Promotion Verify` is the integration gate;
- `develop` → `Local` uses squash merge;
- one approved promotion equals exactly one new `Local` commit;
- `develop` is synchronized to `Local` after promotion;
- `Local` retains linear-history, non-fast-forward, deletion, pull-request, squash-only, and required-check protection;
- `Stable release gate` validates `Local` → `main` release PR merge candidates;
- `main` uses normal merge commits for release promotions and retains non-fast-forward, deletion, pull-request, and required-check protection;
- `main` must not use a strict up-to-date requirement that forces prior release-marker ancestry into `Local`;
- stable tags matching `refs/tags/v*` are protected from update and deletion.
