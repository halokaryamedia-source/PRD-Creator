# Project Workspace

This folder stores project-specific production packages. Reusable production-kit behavior does not belong here; durable workflow policy belongs under `docs/foundation/`, and kit implementation will be placed only when its owning flow is migrated.

## Lifecycle

```text
project is being worked on
→ workspace/active/<project>/

project is intentionally finalized/saved
→ workspace/saved/<project>/
```

Flow 2 will define the exact per-project package structure for source intake, working state, approvals, canonical content, and final outputs. Do not invent that structure before the Flow 2 contract is implemented.
