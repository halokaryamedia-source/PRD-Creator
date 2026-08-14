# The Clockwork Vault

Current PRD Version: `v1.0.0`
Status: `handoff_ready`

## Start Here

- Human review: `v1.0.0/prd.html`
- AI/development: open `v1.0.0/index.json` first, then read only the relevant line range in `v1.0.0/context.md`.

## Resume Method

1. Use `index.json` to locate the affected objective/system and its context range.
2. Read only that range in `context.md`, plus directly relevant shared/global sections.
3. Inspect the current implementation for the same scope.
4. Apply the smallest correct change; preserve unrelated accepted behavior.
5. If a new product decision is required, surface it instead of inferring it from legacy/template code.

The PRD package describes accepted product/development context. Current code/runtime progress remains owned by the implementation repository.

## Versions

- `v1.0.0` — current

Version folders track PRD meaning. Downstream Production Assets may refresh inside the current PRD version when project meaning itself has not changed.
