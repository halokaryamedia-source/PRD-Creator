# Changelog

PRD-Creator package versioning follows the product/contract version rule in `kits/prd-creator/README.md`. Repository hygiene, CI, governance, and documentation changes can appear here without changing the package version.

## Unreleased

### Repository professionalization

- introduce the three-tier `develop → Local → main` promotion model;
- isolate active repository development from the verified `Local` baseline;
- prevent live project-package subdirectories from being tracked in the public system repository;
- add explicit project-data/security guidance;
- add Local integration and stable release promotion gates;
- add CODEOWNERS and a pull-request template;
- remove renderer module-global mutation while preserving Golden rendering behavior;
- simplify the public README/front-door orientation.

No PRD-Creator product-contract version bump is implied by this repository-only tranche.

## 1.14.0

Current PRD-Creator package baseline. Exact product-contract history before this changelog remains recoverable from the package owners, durable decisions, audits, and Git history.
