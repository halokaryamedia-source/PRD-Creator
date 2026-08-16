# Next Action

## Current Status

`GITHUB_EXECUTION_SIMPLIFICATION_ACTIVE`

The PRD 01–04 development boundary is considered finished for now. Current development focus is reducing ChatGPT ↔ GitHub execution waste and preventing connector misuse.

Root `AGENTS.md` now owns an explicit tool/channel fit gate before any write:

```text
need current state
→ direct branch/file fetch

small complete text edit
→ GitHub Contents API

large/multi-hunk/multi-file/atomic/binary work
→ Local/Codex-style git workspace

browser/audio/local runtime
→ actual matching capability
```

The gate also forbids partial-read full replacement, chunked `update_file`, SHA-type confusion, temporary GitHub Actions as a fallback shell, retrying permission/capability denials through Git gymnastics, and changing repository structure merely to make the connector easier to use.

`docs/knowledge/workflows/development.md` now routes Developing work through that root gate instead of treating ChatGPT → GitHub as a universal execution channel.

No new Skill, workflow, validator, framework, or regression suite was added for this change.

## Next Step

Simplify the remaining validation/commit discipline so normal GitHub work uses the minimum relevant proof and stops without proof-chasing or unnecessary intermediate commits.
