# Current Validation Status

Updated: 2026-09-07

This file records current repository evidence after clean-history/governance professionalization, package 1.15 reasoning-quality improvements, package 1.16 semantic/design separation, and package 2.0 source-code/identity hardening.

## Current system state

Working branch: `develop`.  
Verified integration baseline: `Local`.  
Stable branch: `main`.  
Latest published repository release: `v0.1`.

PRD Creator package remains **v2.0.0** on `develop`. Repository release versioning is separate from package versioning; this package change does not itself publish a new repository tag/release.

Current authority/delivery shape:

```text
project discussion + original source + approved decisions
→ recovered project model + integrated cross-role synthesis
→ material Proposal review / approved project model
→ work/content.md semantic PRD truth
→ work/render-data.json deterministic projection
→ DESIGN-CONTRACT Golden component grammar
→ canonical mechanical validation + semantic reconciliation
→ exact render-data acceptance binding
→ output/README.md
→ output/v<document.version>/prd.html
→ output/v<document.version>/context.md
→ output/v<document.version>/index.json
```

Project package contents remain local/external production data rather than tracked public system-repository content.

## Package 2.0 evidence boundary

Package 2.0 hardens the software boundary without changing approved Golden/runtime bytes:

- machine-owned `*.yaml` state is parsed with pinned PyYAML rather than regex/line emulation;
- `validator/api.py` is the canonical complete PRD validator and handoff uses the same API;
- Flow 4 acceptance binds the exact reviewed `work/render-data.json` SHA-256, preventing stale same-version acceptance reuse;
- renderer/validator generic `_engine.py` names are retired in favor of domain-specific engine module names;
- shared typed Voice parsing is centralized in `shared/voice.py` rather than duplicated across renderer/validator;
- Production Assets sections use stable Owner IDs and non-Voice resources use stable `AST-...` IDs;
- title-based Production Assets/Voice machine joins and silent duplicate collapse are rejected;
- versioned delivery is staged before current outputs are replaced;
- locked runtime dependencies are separated from locked dev-quality tooling;
- Ruff, mypy, coverage reporting, compilation, and full regression remain CI evidence boundaries;
- GitHub Actions references used by active workflows are pinned to immutable commit SHAs.

This is a major package contract because current Production Asset/Voice source files must carry explicit machine identity instead of relying on display-title joins. Existing canonical project meaning remains upstream authority and can be regenerated into the new internal format.

## Package 1.16 evidence retained

- `document/CONTENT-CONTRACT.md` owns semantic completeness and Material Conservation;
- `document/DESIGN-CONTRACT.md` owns stable Golden page/component grammar;
- exact Golden/runtime template bytes remain unchanged;
- repeatable Flow / Note / Sequence child counts are data-driven rather than fixed to AFTERSHOCK sample counts;
- `tests/test_prd_adaptive_composition.py` protects non-sample cardinality;
- Golden reference tests continue to protect exact retained artifact bytes.

## Package 1.15 evidence retained

- Flow 2 performs integrated provisional cross-role synthesis before approval;
- routine reversible craft decisions do not become artificial approval gates;
- material AI choices remain explicit Proposals;
- context loading uses progressive expansion;
- Flow 4 reconciles approved source/requirements → canonical content → projection → visible PRD;
- semantic review remains one integrated judgment rather than a numeric scorecard.

## Clean history contract

```text
develop
→ active working history

Local
→ approved milestone history
→ one approved promotion = exactly one squash commit

main
→ stable repository history
→ explicit Local stable promotions through normal merge commits
```

After a successful `develop` → `Local` squash promotion, `develop` is resynchronized to the resulting `Local` HEAD before new development. A `Local` → `main` stable promotion uses the stable release gate. Protected `v*` tags are published only for approved stable capability releases.

## Governance evidence

Current repository policy keeps:

- `develop` available for direct active development while protected from deletion;
- `Local` PR/squash/linear-history promotion rules;
- `main` PR/merge-only stable promotion rules;
- protected release tags;
- deterministic Repository / PRD / Voice / promotion verification boundaries;
- public-repository project-data restrictions.

Repository release `v0.1` remains the latest published version until a later stable feature release is explicitly published.

## Product evidence boundary

Repository/static CI proves source contracts, typed parser behavior, deterministic rendering/validation, and regression behavior. It does not establish browser visual PASS, generated-audio quality, or live-project semantic review unless those capabilities are actually exercised.

RQ-09 remains closed: Golden marker adaptation uses a temporary template instead of mutating renderer module-global storage-prefix state.

## Current continuation

Current continuation is owned by `docs/knowledge/next-action.md`.
