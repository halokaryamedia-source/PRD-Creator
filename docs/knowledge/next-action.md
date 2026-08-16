# Next Action

## Current Status

`GITHUB_RULES_PRD_ACTIVE`

The PRD 01–04 development boundary remains finished for now.

Current scope is **PRD-Creator only**. ChatGPT ↔ GitHub operating policy is active in this repository through:

```text
GITHUB_RULES.md
→ GitHub/AI working discipline used by PRD-Creator

AGENTS.md
→ PRD-Creator-specific branch, ownership, domain, skill, and communication rules
```

`GITHUB_RULES.md` owns the common repository-working sequence:

```text
PIN
→ READ MINIMUM
→ DIAGNOSE
→ TOOL FIT
→ WRITE ONCE
→ VERIFY MINIMUM
→ STOP
```

It also owns the recurring failure-prevention rules for GitHub work, including exact branch/ref authority, bounded reading, first-wrong-owner diagnosis, safe Contents API/SHA usage, no partial-read full replacement or chunked `update_file`, tool/capability hard stops, serialized/coherent writes, minimum relevant validation, API/rate-limit handling, scoped/read-only GitHub Actions, repository-governance safety, secret handling, bounded retries, no unnecessary repository side effects, and an explicit STOP state.

Root `AGENTS.md` points to `GITHUB_RULES.md` instead of duplicating that policy. Existing PRD/Voice domain ownership remains unchanged.

The same rules are **not being rolled out to BuildIT, TranslateIT, or other repositories yet**. Those repositories remain outside this development scope until the user explicitly requests adoption there.

No new Skill, framework, workflow, sync bot, validator, or orchestration layer was added for this policy.

## Next Step

Use and observe `GITHUB_RULES.md` during normal PRD-Creator repository work; change it again only when a concrete recurring GitHub failure shows a missing or incorrect rule.
