# Next Action

## Current Status

`GITHUB_RULES_PORTABLE_AND_ACTIVE`

The PRD 01–04 development boundary remains finished for now.

ChatGPT ↔ GitHub operating policy is now separated cleanly:

```text
GITHUB_RULES.md
→ universal GitHub/AI working discipline

AGENTS.md
→ PRD-Creator-specific branch, ownership, domain, skill, and communication rules
```

`GITHUB_RULES.md` is the reusable/copy-safe policy for other GitHub repositories. It owns the common sequence:

```text
PIN
→ READ MINIMUM
→ DIAGNOSE
→ TOOL FIT
→ WRITE ONCE
→ VERIFY MINIMUM
→ STOP
```

It also owns the recurring failure prevention rules: minimal reading, first-wrong-owner diagnosis, no partial-read full replacement, no chunked `update_file`, correct SHA use, hard stop on unavailable capabilities, one intentional write per file by default, minimum relevant validation, scoped/read-only GitHub Actions, no automatic publish-on-push, bounded retries, no adjacent cleanup, and an explicit STOP state.

Root `AGENTS.md` now points to that file instead of duplicating the GitHub policy. Existing PRD/Voice domain ownership remains unchanged.

No Skill, framework, workflow, sync bot, validator, or orchestration layer was added for this policy split.

## Next Step

Use `GITHUB_RULES.md` as the portable GitHub rule file when adopting the same working discipline in another repository; preserve that repository's own domain rules in its `AGENTS.md`.
