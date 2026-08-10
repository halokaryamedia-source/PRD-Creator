# Review Graph

Updated: 2026-08-10

Use this note to understand how reviews/audits/evidence relate to current `Local`. Review bodies preserve what was observed at the time; do not rewrite their findings merely because later implementation changed.

## Current Review Status

| Evidence / review | Current meaning |
|---|---|
| [Operating Architecture Parity Audit](operating-architecture-parity-audit.md) | **Historical active evidence.** It established that production completion did not equal BuildIT-style operating parity and justified Phases 1–3. Its gap findings are now implemented/accepted; use the Phase 3 acceptance for current status. |
| [Operating Parity Acceptance](../operations/operating-parity-acceptance.md) | **Current operating acceptance evidence.** Representative routing passed, a real Maintenance defect was corrected, nearest-agent decisions were grounded, and Repository Verify run `31367001967` passed. Current result: `OPERATING_PARITY_ACCEPTED`. |
| [System Integration Proof](../operations/system-integration-proof.md) | **Current production evidence.** Real The Clockwork Vault Flow 2→7 run proved the replacement pipeline and a real defect→root-fix→revalidation cycle. |
| [Archived Retirement Audit](../operations/archived-retirement-audit.md) | **Historical implemented evidence.** It justified deleting the old `Production Document Builder/` live tree. Do not use it as current production procedure. |
| [Foundation Validation Report](../../foundation/validation-report.md) | **Current proof/status matrix.** It summarizes current production and operating evidence, not historical reasoning. |
| [Review Template](review-template.md) | Reusable review shape when a dedicated review is actually justified. |

## Review Labels

- `active evidence` — current architecture still relies on the finding;
- `active execution evidence` — finding directly controls current work order;
- `implemented` — corresponding current-owner change exists;
- `current production evidence` — current production capability is supported by recorded proof;
- `current operating acceptance evidence` — current operating architecture has explicit acceptance proof;
- `historical` — retained for reasoning/provenance, not current routing;
- `local proof required` — source/implementation exists but material local/browser/audio/runtime proof remains;
- `superseded` — a later decision/source replaced the old method or conclusion.

A review may carry more than one meaning over time; this graph owns its **current** interpretation.

## Review Rules

When adding a review, answer:

1. what concrete failure/decision is being reviewed;
2. which current owner/source is relevant;
3. what evidence can disprove the conclusion;
4. what is observed vs inferred vs proposed;
5. what later implementation/decision should move out of review prose into its canonical owner.

Do not create a review for routine bounded work whose evidence fits directly in the changed owner/commit/validation note.

## Historical Integrity

A review body is a time-captured evidence record. If later work changes the result:

```text
keep review body historical
→ update this graph's current meaning
→ update current source/policy/next-action separately
```

Do not rewrite an old review until it falsely appears to have predicted later implementation.

## Current Routing

For current work order always prefer:

`AGENTS.md → CONTEXT.md → next-action.md`

Use this graph only when historical evidence/review status materially affects the task.

## Related

- [Knowledge Dashboard](../index.md)
- [Module Map](../modules/module-map.md)
- [Operating Parity Acceptance](../operations/operating-parity-acceptance.md)
