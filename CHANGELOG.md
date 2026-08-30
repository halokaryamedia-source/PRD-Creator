# Changelog

PRD-Creator tracks two separate version domains:

- repository stable releases use Git tags such as `v0.1` on `main`;
- the PRD-Creator product/package version is owned by `kits/prd-creator/README.md` and follows product/contract semantics.

Repository hygiene, CI, governance, and documentation changes can therefore ship without changing the package version.

## Unreleased

No repository release changes are currently queued beyond the `v0.2` candidate below.

## Repository v0.2 — 2026-08-31

Governance alignment and development-safety hardening for the professional branch model.

### Governance synchronization

- align stable release verification with the intentional `Local` / `main` release-marker topology;
- validate the GitHub pull-request merge candidate for `Local` → `main` releases;
- align the pull-request template and durable governance documentation with the completed clean-history migration;
- record protected `v*` stable-tag policy and the separation between repository release versioning and package versioning;
- add lightweight CI checks so required governance surfaces cannot disappear silently;
- document safe local `develop` resynchronization after squash promotion without adding a new development gate.

Repository release `v0.2` does not change the PRD-Creator product/package contract version.

## Repository v0.1 — 2026-08-30

First stable repository baseline of the professionalized PRD-Creator workflow.

### Repository professionalization

- establish the three-tier `develop → Local → main` promotion model;
- isolate active repository development from the verified `Local` baseline;
- prevent live project-package subdirectories from being tracked in the public system repository;
- add explicit project-data/security guidance;
- add Local integration and stable release promotion gates;
- add CODEOWNERS and a pull-request template;
- remove renderer module-global mutation while preserving Golden rendering behavior;
- simplify the public README/front-door orientation.

Repository release `v0.1` does not change the PRD-Creator product/package contract version.

## Package 1.14.0

Current PRD-Creator product/package baseline. Exact product-contract history before this changelog remains recoverable from the package owners, durable decisions, audits, and Git history.
