# Next Action

## Current Status

`GITHUB_OPERATING_DISCIPLINE_CONSOLIDATED`

The PRD 01–04 development boundary remains finished for now. ChatGPT ↔ GitHub execution rules are now consolidated in root `AGENTS.md` into one canonical sequence:

```text
PIN
→ READ MINIMUM
→ DIAGNOSE
→ TOOL FIT
→ WRITE ONCE
→ VERIFY MINIMUM
→ STOP
```

The root discipline now covers the recurring failure modes that previously caused slow or noisy repository work: broad reading, wrong-owner fixes, adjacent cleanup, full-file replacement from partial context, chunked `update_file`, SHA-type confusion, Git gymnastics after capability denial, repeated intermediate commits, CI/proof chasing, broad validation for unrelated changes, temporary workflows, verification workflows that mutate the branch, automatic publishing on every push, unchanged reruns, and failure to stop after sufficient proof.

Default efficiency budgets are explicit: 1–3 owner reads, zero history reads by default, zero new workflows/abstractions/files unless justified, one intentional write per file, at most one relevant CI gate, maximum two same-cause retries, zero capability-denial retries, and zero adjacent cleanup.

No new Skill, workflow, validator, framework, or orchestration layer was added. Existing PRD/Voice domain ownership remains unchanged.

## Next Step

Use the consolidated discipline during normal repository work. Change it again only when a concrete recurring execution defect shows that one of these rules is insufficient or incorrect.
