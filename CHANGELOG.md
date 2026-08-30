# Changelog

PRD-Creator tracks two separate version domains:

- published repository releases use protected Git tags such as `v0.1` on `main`;
- the PRD-Creator product/package version is owned by `kits/prd-creator/README.md` and follows product/contract semantics.

A new repository tag/GitHub Release is created only when an approved PRD-Creator feature or capability changes. Repository hygiene, CI, governance, ruleset, documentation, and other maintenance-only changes may be promoted without creating a new repository release or changing the package version.

## Unreleased

### Repository maintenance — unversioned

- align stable main verification with the intentional `Local` / `main` ancestry model;
- validate GitHub's pull-request merge candidate for `Local` → `main` stable promotions;
- align the pull-request template and durable governance documentation with the completed clean-history migration;
- record protected `v*` tag policy and the separation between repository release versioning and package versioning;
- add lightweight CI checks so required governance surfaces cannot disappear silently;
- document safe local `develop` resynchronization after squash promotion without adding a new development gate;
- add deletion-only protection for `develop` while preserving direct push and post-squash synchronization.

These maintenance changes do **not** create a new repository version. The latest published repository release remains `v0.1` until an approved feature/capability change justifies the next release.

## Repository v0.1 — 2026-08-30

First stable repository baseline of the professionalized PRD-Creator workflow.

### Repository professionalization

- establish the three-tier `develop → Local → main` promotion model;
- isolate active repository development from the verified `Local` baseline;
- prevent live project-package subdirectories from being tracked in the public system repository;
- add explicit project-data/security guidance;
- add Local integration and stable main promotion gates;
- add CODEOWNERS and a pull-request template;
- remove renderer module-global mutation while preserving Golden rendering behavior;
- simplify the public README/front-door orientation.

Repository release `v0.1` does not change the PRD-Creator product/package contract version.

## Package 1.14.0

Current PRD-Creator product/package baseline. Exact product-contract history before this changelog remains recoverable from the package owners, durable decisions, audits, and Git history.
