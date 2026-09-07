# Current Validation Status

Updated: 2026-09-07

This file records the current validation boundary for the PRD-Creator 3.0 synchronization work. It distinguishes implemented source state from final verification evidence.

## Current system state

Working branch: `develop`.  
Verified integration baseline: `Local`.  
Stable branch: `main`.  
Latest published repository release: `v0.1`.

PRD Creator package candidate is **v3.0.0** on `develop`. Repository release versioning is separate from package versioning; this candidate does not itself publish a repository tag/release.

Package 3.0 **source/contract cleanup is complete on `develop`**. Final Package 3.0 validation is still **pending** until the full repository/static/regression verification is run on the exact final `develop` state. No promotion to `Local` is part of the current task.

## Current authority and revision chain

```text
project discussion + original source + approved decisions
→ strict source inventory + requirement register
→ Simple Chat Preview
→ approved_requirement_sha256
→ work/content.md canonical PRD meaning
→ render-data.approved_requirement_sha256
+ render-data.canonical_content_sha256
→ strict render-data projection
→ deterministic PRD core
→ work/asset-requirements.md when non-Voice 04 exists
→ exact render-data + asset-requirements acceptance
→ handoff_ready
→ Flow 5 Voice Requirements + Owner/Moment identity when justified
→ Flow 6 Voice Production + exact requirements SHA
→ consolidated project HTML + exact Voice source bindings
→ Flow 7 exact voice-production acceptance
→ voice_delivery_ready
```

Derived delivery remains:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

Generated output never outranks canonical `state/` or `work/` sources.

## Package 3.0 implementation boundary

The current candidate intentionally makes machine contracts stricter and incompatible with older internal project-state formats:

- Flow 2 readiness has one status truth; redundant `ready_for_prd: true` / stale `next_step` aliases are retired;
- Simple Chat Preview approval is bound to exact current `requirement-register.yaml` bytes;
- current retained repository sources are path-safe and SHA-bound;
- requirement provenance must resolve to known current authority or an explicitly approved Proposal;
- all persisted project paths use normalized project-relative POSIX references and cannot escape the workspace;
- render-data uses one whitelist projection vocabulary and binds both the exact approved Flow 2 requirement revision and exact `content.md` bytes;
- gameplay result mode is explicit (`scored` or `completion_only`) and must agree with Developer result data and visible result presentation;
- renderer-side semantic fallback/alias inference is removed from the valid production path;
- `TemplateAdapter` is the single Golden-shell mutation boundary for both PRD core and additive 04 insertion; retained reference-project vocabulary is quarantined there;
- non-Voice 04 uses stable `Owner ID → Moment ID → AST-...` identity;
- Voice uses stable `Owner ID → Moment ID → VO-...` identity from Flow 5 through Flow 7;
- PRD acceptance binds exact current render-data and non-Voice asset-requirements bytes;
- Voice Production binds exact current Voice Requirements bytes;
- final Voice acceptance binds exact current voice-production bytes;
- PRD and Voice acceptance field/SHA parsing share one `shared/acceptance.py` primitive instead of duplicate regex contracts;
- Production Assets/Voice HTML carries exact source SHA metadata;
- `voice_delivery_ready` cannot render an unresolved Voice Cast selection/profile, while Preparation Mode may still show a truthful pending selection;
- Production Assets CSS/JavaScript live in `renderer/static/` and are inlined during standalone HTML generation;
- delivery publishes a complete version directory transactionally and rolls back on publication failure;
- parsers expose structured issue identity and source-location diagnostics for machine-facing failures;
- Flow 2 YAML parse failures preserve the exact state-file path and YAML line through structured issue output;
- machine YAML uses the duplicate-key-safe shared PyYAML loader and reports parse-line location when available;
- derived PRD HTML validation is isolated in `validator/html_contract.py` instead of mixed into source/projection validation;
- top-level PRD page tracking is nesting-safe and does not lose page identity when nested sections appear;
- Flow 5–7 mechanical domain validation is isolated in `validator/voice_validation.py`; `validate_voice.py` is a thin CLI/public entrypoint;
- `validator/api.py` does not reimplement projection/requirement checks owned by `prd_validation_engine.py`; it only adds content-purity to the canonical engine result;
- bilingual validation preserves numeric, percentage, stable-ID, recognized unit, dimension, coordinate, and material-negation invariants across `en`/`id`;
- renderer/validator business engines use package boundaries; CLI wrappers alone may bootstrap the kit path;
- active GitHub Actions dependencies are pinned to immutable commit SHAs;
- runtime and verification dependencies are pinned separately, including current dev-tool transitive dependencies;
- Repository / PRD / Voice / Local / Release verification now share the same static-quality contract where applicable;
- repository verification routing covers all Package 3 implementation owners and workflows.

The protected Golden reference/runtime artifact remains unchanged unless a separate approved design-contract change explicitly authorizes it.

## Final verification still required

No Package 3.0 readiness claim is made yet. The next evidence step, when explicitly requested, is one final pass on the exact final `develop` HEAD:

```text
Repository Verify
→ Ruff format check
→ Ruff lint/import check
→ mypy shared + renderer + validator
→ full test_*.py regression suite
→ PRD Verify
→ Voice Verify
→ coverage report
```

If any gate fails, fix the first wrong owner on `develop` and rerun the final verification. Do not weaken a contract merely to recover a green check.

## Evidence boundaries

Repository/static verification may establish source contracts, parser behavior, deterministic rendering, exact revision bindings, transactional delivery, and regression behavior.

It does **not** establish:

- browser visual PASS without rendered/browser evidence;
- generated-audio quality without heard audio evidence;
- live-project semantic quality without an actual project review;
- client sign-off, gameplay QA, implementation completion, or stable repository release.

## Branch/history boundary

```text
develop
→ Package 3 source/contract cleanup complete
→ final verification pending

Local
→ protected verified integration baseline
→ unchanged during the current task

main
→ stable repository history
```

Promotion `develop → Local` is a separate later action and must not happen until explicitly requested after the development state is accepted.

## Current continuation

Keep Package 3 on `develop`. Run the single final verification pass only as the next explicit verification step; do not open or merge a Local promotion as part of the current task.
