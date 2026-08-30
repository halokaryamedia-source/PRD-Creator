# Contributing

PRD-Creator is currently a personal/internal development repository. Public visibility is for development convenience and does not imply that external contributions or reuse are automatically accepted.

## Branch model

```text
develop
→ active repository development
→ working commits may be numerous

Local
→ verified integration / stable working baseline
→ exactly one commit per approved promoted update

main
→ existing stable / release branch
→ unchanged until an explicit main-history migration/release decision
```

Routine repository work happens on `develop`.

Do not make routine changes directly on `Local` or `main`.

### Promote `develop` → `Local`

Use a dedicated pull request when one coherent development outcome is ready for the stable working baseline.

The PR must:

- come from `develop`;
- pass `Local promotion gate`;
- represent one approved logical update;
- be merged with **squash merge** so the complete update becomes exactly one new commit on `Local`.

After squash merge, reset/synchronize `develop` to the resulting `Local` HEAD before starting the next development cycle. The pre-squash working commit chain is development history, not permanent Local milestone history.

This invariant is intentional:

```text
one approved develop → Local promotion
= exactly +1 commit on Local
```

### `main` boundary

`main` retains its existing history for now and is outside the clean-history migration of `Local`/`develop`.

Do not attempt a normal `Local` → `main` promotion while the two lineages are unrelated. A future explicit main migration/release decision must define how `main` adopts the clean lineage before release promotion resumes.

Creating a Git tag or GitHub Release is a separate explicit publishing action and is never automatic.

## Before committing

Run the cheapest relevant proof for the changed claim.

Repository-level changes:

```bash
python tools/verify_repository.py
```

PRD executable changes use the PRD regression suite. Voice executable changes use the Voice regression suite. Promotion gates run the broader suites required at integration boundaries.

## CI behavior

CI on `develop` is the active asynchronous regression safety net.

- Use the cheapest relevant proof before committing.
- Do not poll superseded runs.
- Diagnose only a failure on the current relevant HEAD.
- `Repository Verify`, `PRD Verify`, and `Voice Verify` remain path-targeted.
- `Local promotion gate` is the full integration boundary for `develop` → `Local`.
- Stable release work against `main` remains deferred until the explicit main-history migration decision.

## Commit discipline

Working commits on `develop` may be as granular as needed for safe development, but each commit should still communicate useful intent where practical.

```text
feat:      new capability
fix:       behavior correction
refactor:  internal restructuring without intended behavior change
docs:      documentation/policy-only change
test:      test-only change
ci:        workflow/CI change
build:     dependency/toolchain change
release:   explicit stable/release state
chore:     bounded maintenance when no better category fits
```

`Local` is different: it is milestone history. One approved promotion equals one squash commit. Do not preserve development checkpoint noise in `Local`.

Do not use transfer experiments, placeholder files, generated fragments, or temporary helper architecture as permanent repository history.

## Project-data boundary

The public PRD-Creator repository tracks the production **system**, not live project packages.

Project-specific packages under `workspace/active/<project>/` and `workspace/archive/<project>/` are ignored by Git and must be retained locally or in a separate authorized/private location.

Do not add:

- credentials or secrets;
- private client/source data;
- live project requirement registers or source inventories;
- project outputs containing material not approved for public visibility;
- temporary transfer payloads.

See `SECURITY.md` and `workspace/README.md`.

## Pull requests

Use `.github/PULL_REQUEST_TEMPLATE.md` and keep the PR scoped to one logical delivery. A `develop` → `Local` promotion PR must state the verification evidence and must be squash-merged.

## License

The repository is not open source. External reuse, redistribution, or commercial use requires prior written permission from the copyright holder. See `LICENSE`.
