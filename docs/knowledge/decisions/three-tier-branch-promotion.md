# Three-Tier Branch Promotion

Status: current

## Decision

PRD-Creator uses three repository authority levels:

```text
develop  → active repository development
Local    → verified integration / stable working baseline
main     → stable release
```

Normal repository Development occurs on `develop`. `Local` and `main` are promotion targets, not routine development branches.

## Why

The former two-branch model allowed active work to accumulate directly on `Local` while `main` also acquired stable-only commits. That produced diverged histories and made the next release boundary harder to reason about.

The three-tier model isolates incomplete work without sacrificing a durable integration baseline.

## Promotion contract

```text
develop → Local
→ Local promotion gate
→ merge commit
→ synchronize resulting Local ancestry back to develop

Local → main
→ Stable release gate
→ merge commit
→ synchronize resulting main ancestry back to Local, then develop
```

A candidate must contain current `main` ancestry before it is promoted to `Local`. A release must come from `Local` and contain current `main` ancestry.

## Non-goals

This decision does not:

- create routine task branches;
- require PRs for every local save or project-production artifact;
- change PRD/Voice product semantics;
- authorize automatic tags or GitHub Releases;
- rewrite old shared history merely to make the graph prettier.

## Enforcement

- `Repository Verify`, `PRD Verify`, and `Voice Verify` run on active `develop` changes when their paths are affected.
- `Local Promotion Verify` supplies the full integration gate.
- `Release Verify` keeps the existing `Stable release gate` context for `main`.
- Repository rulesets remain the GitHub-side enforcement owner where available.

If a GitHub setting cannot be changed through the active capability, policy and CI should remain correct without pretending that the setting was updated.
