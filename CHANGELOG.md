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

These maintenance changes do **not** create a new repository version. The latest published repository release remains `v0.1` until an approved feature/capability change is promoted and published.

## Package 1.15.0 — 2026-09-07

Model-readiness and semantic-quality improvement for stronger reasoning models while preserving the current Golden renderer/output contract.

### Semantic production quality

- add integrated provisional cross-role synthesis in Flow 2 before the Simple Chat Preview so hidden lifecycle, quantitative, and role contradictions can surface earlier;
- distinguish routine reversible AI craft decisions from material project Proposals, reducing unnecessary approval ceremony without weakening project authority;
- add progressive context expansion so integrated work may open the smallest additional source/owner when a real cross-cutting dependency requires it;
- add explicit Flow 4 semantic reconciliation across approved source/requirements → canonical content → render projection → visible PRD;
- strengthen semantic readiness around source fidelity, decision completeness, role actionability, quantitative/lifecycle coherence, and cross-role consistency;
- preserve Material Conservation as a separate omission gate and avoid numeric semantic scorecards or requirement-to-sentence proof machinery.

### Verification quality

- make PRD CI compile the test package and discover every canonical `tests/test_prd_*.py` contract module automatically instead of maintaining an explicit test-module list.

Golden/runtime template bytes, visible PRD-core composition, deterministic renderer behavior, project-data boundaries, and Voice downstream authority remain unchanged in this package update.

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

Previous PRD-Creator product/package baseline before the 1.15.0 semantic-quality/model-readiness expansion. Exact earlier product-contract history remains recoverable from the package owners, durable decisions, audits, and Git history.
