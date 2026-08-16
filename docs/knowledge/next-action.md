# Next Action

## Current Status

`RULE_OWNERSHIP_CONTINUITY_CLEANUP_COMPLETE`

PRD-Creator `Local` uses repository-backed continuity so a new ChatGPT session can recover the current development context without asking the user to restate prior work.

The current continuity chain is:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules for material GitHub work
→ CONTEXT.md
→ next-action.md
→ development-brief for non-trivial Developing
→ smallest relevant owner/source
```

## Active Boundary

Normal PRD-Creator work may continue using the current Flow/product owners. Repository governance is not an active hardening project by default.

For a new chat where the user only says `amati repo ini` / inspect / understand / recover context:

```text
recover repository context
→ report current understanding
→ no edit
→ no next-step execution
```

When the user explicitly asks to continue/implement non-trivial repository Developing, recover the full continuity chain above before editing.

Current rollout scope remains **PRD-Creator only**. BuildIT, TranslateIT, and other repositories are not part of this policy rollout until the user explicitly requests them.

## Last Completed

- `GITHUB_RULES.md` established GitHub operating, commit/history, CI/API, safety, and STOP discipline for PRD-Creator.
- Commit history discipline uses one categorized logical delivery by default rather than micro-commits.
- Repository continuity/routing ownership was simplified so stable context is preserved while duplicated rule authorities are reduced.
- Existing PRD/Voice product behavior, Golden bytes, detailed production contracts, renderer/validator behavior, and project outputs remain outside that cleanup.

## Deferred / Do Not Continue

- Do not promote `docs/knowledge/operations/backlog.md`, historical review findings, old TODOs, or Git history into active work unless current user intent or this file explicitly promotes one boundary.
- Do not continue speculative governance hardening merely because another cleanup is theoretically possible.
- Do not roll these repository rules into BuildIT, TranslateIT, or another repository without explicit user instruction.

## Next Step

Use the current continuity/routing model during normal PRD-Creator work; change repository governance again only when a concrete recurring failure or user-requested improvement proves that the current model is insufficient.
