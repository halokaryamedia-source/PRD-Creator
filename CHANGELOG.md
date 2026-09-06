# Changelog

PRD-Creator tracks two separate version domains:

- published repository releases use protected Git tags such as `v0.1` on `main`;
- the PRD-Creator product/package version is owned by `kits/prd-creator/README.md` and follows product/contract semantics.

A new repository tag/GitHub Release is created only when an approved PRD-Creator feature or capability changes and is promoted to stable release state. Repository hygiene, CI, governance, ruleset, documentation, and maintenance-only changes may be promoted without creating a repository release.

## Unreleased

### Repository maintenance — unversioned

- align stable main verification with the intentional `Local` / `main` ancestry model;
- validate GitHub's pull-request merge candidate for `Local` → `main` stable promotions;
- align pull-request and durable governance documentation with the clean-history migration;
- protect `v*` tags and preserve package/repository version separation;
- keep lightweight repository-governance verification;
- preserve safe `develop` resynchronization after squash promotion.

These maintenance changes do **not** create a repository version. The latest published repository release remains `v0.1` until an approved feature/capability change is promoted and published.

## Package 1.16.0 — 2026-09-07

Semantic/design separation and adaptive PRD composition while preserving the exact Golden artifact and deterministic renderer architecture.

### Semantic / design ownership

- split PRD semantic completeness into `document/CONTENT-CONTRACT.md` and Golden presentation grammar into `document/DESIGN-CONTRACT.md`;
- keep page family, navigation, stable component vocabulary, meaningful fixed summary slots, and exact Golden/runtime template bytes protected;
- record the durable Adaptive Semantic Composition decision as a refinement of the earlier Golden fidelity decision.

### Adaptive composition

- stop treating AFTERSHOCK sample counts such as four flow cards, four note cards, or five compact gameplay steps as universal project semantics;
- preserve project-driven child cardinality inside existing approved Flow / Note / Sequence component families;
- prohibit both filler items added merely to reach a sample count and destructive merging done merely to reduce to it;
- add focused adaptive-composition regression coverage proving non-sample counts render and mechanically validate through the same Golden component grammar.

This is backward-compatible for existing 1.15 data: a project that naturally uses the previous 4/5 counts still renders identically in structure. The change expands accepted semantic cardinality; it does not introduce arbitrary generated layouts.

## Package 1.15.0 — 2026-09-07

Model-readiness and semantic-quality improvement for stronger reasoning models while preserving the current Golden renderer/output contract.

### Semantic production quality

- add integrated provisional cross-role synthesis in Flow 2 before the Simple Chat Preview;
- distinguish routine reversible AI craft decisions from material project Proposals;
- add progressive context expansion for real cross-cutting dependencies;
- add explicit Flow 4 semantic reconciliation across approved source/requirements → canonical content → render projection → visible PRD;
- strengthen semantic readiness around source fidelity, decision completeness, role actionability, quantitative/lifecycle coherence, and cross-role consistency;
- preserve Material Conservation as a separate omission gate without numeric semantic scorecards.

### Verification quality

- make PRD CI discover every canonical `tests/test_prd_*.py` contract module automatically.

Golden/runtime template bytes, visible PRD-core composition, deterministic rendering, project-data boundaries, and Voice downstream authority remained unchanged in 1.15.

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

Previous package baseline before the 1.15/1.16 reasoning-quality and adaptive-composition expansions. Earlier product-contract history remains recoverable from package owners, durable decisions, audits, and Git history.
