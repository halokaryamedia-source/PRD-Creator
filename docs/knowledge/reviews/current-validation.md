# Current Validation Status

Updated: 2026-09-07

This file records the current validation boundary for the PRD-Creator 3.0 synchronization candidate. It must distinguish **implemented source state** from **final verification evidence**.

## Current system state

Target working milestone: `Local`.  
Current bounded candidate: `local-sync-hardening` → `Local`.  
Stable branch: `main`.  
Latest published repository release: `v0.1`.

PRD Creator package remains **v3.0.0** in the current Local synchronization candidate. Repository release versioning is separate from package versioning; this package candidate does not itself publish a repository tag/release.

Final Package 3.0 validation is **pending** until source/contract cleanup is complete and the full repository/static/regression/promotion gate is run once on the final one-commit Local candidate.

## Current authority and revision chain

```text
project discussion + original source + approved decisions
→ strict source inventory + requirement register
→ Simple Chat Preview
→ approved_requirement_sha256
→ work/content.md canonical PRD meaning
→ render-data.canonical_content_sha256
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
- requirement provenance must resolve to known current source identity;
- all persisted project paths use normalized project-relative POSIX references and cannot escape the workspace;
- render-data uses one whitelist projection vocabulary and binds exact `content.md` bytes;
- gameplay result mode is explicit (`scored` or `completion_only`) and must agree with Developer result data;
- renderer-side semantic fallback/alias inference is removed from the valid production path;
- `TemplateAdapter` is the single Golden-shell mutation boundary and retained reference-project vocabulary is quarantined there;
- non-Voice 04 uses stable `Owner ID → Moment ID → AST-...` identity;
- Voice uses stable `Owner ID → Moment ID → VO-...` identity from Flow 5 through Flow 7;
- PRD acceptance binds exact current render-data and non-Voice asset-requirements bytes;
- Voice Production binds exact current Voice Requirements bytes;
- final Voice acceptance binds exact current voice-production bytes;
- Production Assets/Voice HTML carries exact source SHA metadata;
- Production Assets CSS/JavaScript live in `renderer/static/` and are inlined during standalone HTML generation;
- delivery publishes a complete version directory transactionally and rolls back on publication failure;
- parsers expose structured issue identity and source-location diagnostics for machine-facing failures;
- machine YAML uses the duplicate-key-safe shared PyYAML loader;
- renderer/validator business engines use package boundaries; CLI wrappers alone may bootstrap the kit path;
- active GitHub Actions dependencies are pinned to immutable commit SHAs;
- runtime and verification dependencies are pinned separately.

The protected Golden reference/runtime artifact remains unchanged unless a separate approved design-contract change explicitly authorizes it.

## Final verification still required

No Package 3.0 readiness claim is made yet. The final candidate must first be reduced to **one commit whose parent is current `Local`**, then the following evidence must all pass on that exact commit:

```text
Repository Verify
→ static quality across shared + validator + renderer
→ full test_*.py regression suite
→ PRD Verify
→ Voice Verify
→ Local promotion gate
→ coverage report
```

If any gate fails, fix the first wrong owner, recreate the one-commit candidate, and rerun the final verification. Do not weaken a contract merely to recover a green check.

## Evidence boundaries

Repository/static verification may establish source contracts, parser behavior, deterministic rendering, exact revision bindings, transactional delivery, and regression behavior.

It does **not** establish:

- browser visual PASS without rendered/browser evidence;
- generated-audio quality without heard audio evidence;
- live-project semantic quality without an actual project review;
- client sign-off, gameplay QA, implementation completion, or stable repository release.

## Branch/history boundary

```text
Local
→ milestone integration target
→ one approved promotion = one squash commit

local-* candidate
→ allowed only as a bounded one-commit candidate parented directly on current Local

develop
→ may be resynchronized from Local when that workflow is needed again

main
→ stable repository history
→ explicit Local stable promotion only
```

`Local` remains protected; direct force updates are not part of the workflow.

## Current continuation

Complete remaining source/contract cleanup on the bounded Local candidate, recreate it as one commit against current `Local`, then run the single final verification pass described above. Do not merge the candidate before that evidence is complete.
