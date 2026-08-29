# Contributing

PRD-Creator is currently a personal/internal development repository. Public visibility is for development convenience and does not imply that external contributions or reuse are automatically accepted.

## Branch model

```text
Local
→ active development / working authority

main
→ stable / release branch
```

Routine work happens directly on `Local`. Do not create routine task branches or pull requests merely for normal development.

`main` is not a development branch. Promote `Local` to `main` only when the repository owner explicitly declares a stable/release promotion and the release gate passes.

A release promotion may use a dedicated pull request from `Local` to `main`. This is a release boundary only; it does not change the normal direct-to-`Local` workflow.

## Before committing

Run only the checks relevant to the change during normal development. At minimum, repository-level changes should pass:

```bash
python tools/verify_repository.py
```

PRD executable changes use the PRD regression suite. Voice executable changes use the Voice regression suite. A promotion to `main` uses the full `Release Verify` workflow.

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

## Repository data

Do not add credentials, secrets, private client data, or material that is not approved for the current repository visibility. Project artifacts remain subject to their own ownership and third-party rights.

## License

The repository is not open source. Use is restricted by the root `LICENSE` file. External reuse, redistribution, or commercial use requires prior written permission from the copyright holder.
