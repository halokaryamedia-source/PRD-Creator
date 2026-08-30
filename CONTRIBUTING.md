# Contributing

PRD-Creator is currently a personal/internal development repository. Public visibility is for development convenience and does not imply that external contributions or reuse are automatically accepted.

## Branch model

```text
develop
→ active repository development

Local
→ verified integration / stable working baseline

main
→ stable / release branch
```

Routine repository work happens on `develop`.

Do not make routine changes directly on `Local` or `main`.

### Promote `develop` → `Local`

Use a dedicated pull request when a coherent development outcome is ready for the stable working baseline.

The PR must:

- come from `develop`;
- pass `Local promotion gate`;
- include the current `main` ancestry before promotion;
- be merged with a merge commit so `develop` remains part of the promoted ancestry.

After merge, fast-forward/synchronize `develop` to the resulting `Local` commit before continuing normal development.

### Promote `Local` → `main`

This is an explicit stable/release boundary only.

The PR must:

- come from `Local`;
- pass `Stable release gate`;
- be merged with a merge commit;
- represent an explicitly approved release/stable promotion.

After release, synchronize the resulting `main` commit back to `Local`, then to `develop`, before new development diverges again.

Creating a Git tag or GitHub Release is a separate explicit publishing action and is never automatic.

## Before committing

Run the cheapest relevant proof for the changed claim.

Repository-level changes:

```bash
python tools/verify_repository.py
```

PRD executable changes use the PRD regression suite. Voice executable changes use the Voice regression suite. Promotion gates run the broader suites required at integration/release boundaries.

## CI behavior

CI on `develop` is the active asynchronous regression safety net.

- Use the cheapest relevant proof before committing.
- Do not poll superseded runs.
- Diagnose only a failure on the current relevant HEAD.
- `Repository Verify`, `PRD Verify`, and `Voice Verify` remain path-targeted.
- `Local promotion gate` is the full integration boundary for `develop` → `Local`.
- `Stable release gate` is the full release boundary for `Local` → `main`.

## Commit discipline

Use one logical commit per coherent outcome where practical:

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

Do not use transfer experiments, placeholder files, generated fragments, or temporary helper architecture as repository history.

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

Use `.github/PULL_REQUEST_TEMPLATE.md` and keep the PR scoped to one logical delivery. Stable promotion PRs should state the proof run and whether downstream branches need synchronization after merge.

## License

The repository is not open source. External reuse, redistribution, or commercial use requires prior written permission from the copyright holder. See `LICENSE`.
