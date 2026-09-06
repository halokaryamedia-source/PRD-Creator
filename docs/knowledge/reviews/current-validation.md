# Current Validation Status

Updated: 2026-09-07

This file records current repository evidence after clean-history/governance professionalization, package 1.15 reasoning-quality improvements, and package 1.16 semantic/design separation with adaptive PRD composition.

## Current system state

Working branch: `develop`.  
Verified integration baseline: `Local`.  
Stable branch: `main`.  
Latest published repository release: `v0.1`.

PRD Creator package remains **v1.16.0** on `develop`. Repository release versioning is separate from package versioning; this package change does not itself publish a new repository tag/release.

Current authority/delivery shape:

```text
project discussion + original source + approved decisions
→ recovered project model + integrated cross-role synthesis
→ material Proposal review / approved project model
→ work/content.md semantic PRD truth
→ work/render-data.json deterministic projection
→ DESIGN-CONTRACT Golden component grammar
→ semantic reconciliation + acceptance evidence
→ output/README.md
→ output/v<document.version>/prd.html
→ output/v<document.version>/context.md
→ output/v<document.version>/index.json
```

Project package contents remain local/external production data rather than tracked public system-repository content.

## Package 1.16 evidence boundary

Package 1.16 separates semantic and presentation ownership:

- `document/CONTENT-CONTRACT.md` owns semantic completeness and Material Conservation;
- `document/DESIGN-CONTRACT.md` owns stable Golden page/component grammar;
- exact Golden/runtime template bytes remain unchanged;
- the PRD core page family and `6 + 4N` topology remain unchanged;
- stable summary questions/rows/table meanings remain unchanged;
- repeatable Flow / Note / Sequence child counts are now data-driven rather than fixed to AFTERSHOCK sample counts;
- renderer projection preserves variable child cardinality inside the same approved component families;
- `tests/test_prd_adaptive_composition.py` provides focused regression coverage for non-sample cardinality;
- `tests/test_prd_golden_reference.py` continues to prove exact retained Golden reference bytes/structure and therefore may retain exact AFTERSHOCK reference counts as artifact evidence.

The durable rationale is recorded in `docs/knowledge/decisions/adaptive-semantic-composition.md`, which refines rather than removes the earlier Golden fidelity decision.

No new browser, generated-audio, or live-project visual-quality claim is made by this repository-level migration. Browser visual PASS still requires actual browser evidence.

## Package 1.15 evidence retained

- Flow 2 performs integrated provisional cross-role synthesis before approval;
- routine reversible craft decisions do not become artificial user-approval gates;
- material AI choices remain explicit Proposals;
- context loading uses progressive expansion;
- Flow 4 reconciles approved source/requirements → canonical content → projection → visible PRD;
- semantic review remains one integrated judgment rather than a numeric scorecard;
- PRD CI discovers canonical `tests/test_prd_*.py` modules automatically.

These behaviors remain current in 1.16.

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

## Baseline evidence

Clean root baseline:

```text
29aec52a2d78cabfedd3abb771c8a31d67979ce7
```

The baseline was constructed from a verified prepared tree and passed repository verification plus the full regression suite before activation. Legacy recovery references remain separate from active branch lineage.

## Product evidence boundary

Earlier browser/real-project evidence remains historical evidence for the exact project bytes tested before live project packages were removed from the public system tree.

RQ-09 remains closed: Golden marker adaptation uses a temporary template instead of mutating renderer module-global storage-prefix state.

## Current continuation

Current continuation is owned by `docs/knowledge/next-action.md`.
