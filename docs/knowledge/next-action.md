# Next Action

## Current Status

`PACKAGE_3_SOURCE_CLEANUP_COMPLETE`

PRD-Creator Package 3.0 source/contract synchronization is complete on `develop`. Final verification has not yet been claimed.

Current relevant branch roles:

- `develop` → exact Package 3 candidate and next verification target;
- `Local` → protected verified integration baseline; unchanged during the current task;
- `main` → stable repository history.

The previous Local-targeted PR was closed without merge. Do not open or merge a Local promotion until explicitly requested after final verification and development acceptance.

## Active Boundary

Package 3 now uses one synchronized production chain:

```text
Flow 2 exact requirement approval
→ Flow 3 canonical content + strict projection
→ deterministic renderer
→ non-Voice 04 stable identity
→ Flow 4 exact-byte acceptance/handoff
→ Flow 5 Voice requirements
→ Flow 6 Voice production
→ Flow 7 exact-byte Voice acceptance/delivery
```

Keep these boundaries intact:

- strict source/provenance state and revision-bound preview approval;
- exact Flow 2 requirement SHA + canonical content SHA projection bindings;
- safe project-relative persisted paths;
- one whitelist render projection vocabulary;
- explicit `scored | completion_only` result model;
- stable Owner → Moment → Resource identity;
- exact PRD/asset/Voice acceptance bindings;
- package-relative business-module imports with CLI-only bootstrap;
- one Golden `TemplateAdapter` mutation boundary;
- transactional version-directory publication;
- structured machine diagnostics with source location where mechanically available;
- one owner for each validation responsibility;
- one static-quality contract across development/promotion/release gates;
- protected Golden reference/runtime bytes.

Do not reintroduce compatibility aliases or duplicate checks merely to preserve old internal project-state formats. Package 3.0 is intentionally a major machine-contract boundary.

## Next Step

**Final verification on the exact current `develop` HEAD, when explicitly requested.**

Run one evidence pass:

1. Repository Verify;
2. Ruff format check;
3. Ruff lint/import check;
4. mypy for shared + renderer + validator;
5. full `test_*.py` regression + coverage;
6. PRD Verify;
7. Voice Verify.

If any gate fails, fix the first wrong owner on `develop` and rerun the final pass. Do not merge or otherwise update `Local` until a later explicit promotion request.
