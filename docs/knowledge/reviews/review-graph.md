# Review Graph

Updated: 2026-08-10

Use this note to understand how reviews/audits/evidence relate to current `Local`. Review bodies preserve what was observed at the time; do not rewrite their findings merely because later implementation changed.

## Current Review Status

| Evidence / review | Current meaning |
|---|---|
| [Production Engineering Quality Audit](production-engineering-quality-audit.md) | **Active execution evidence.** P1 identified nine material/conditional production-engineering findings. P1-F01 and P1-F02 are now implemented by P1.1 source head `04f306f8…`, which passed Production Verify `31377375929` and Repository Verify `31377377036`. P1-F03 and P1-F07 now govern active P1.2; Voice and remaining findings stay ordered behind them. |
| [BuildIT Current Parity Gap Audit](buildit-current-parity-gap-audit.md) | **Active evidence.** Reopened overall relevant parity against current BuildIT. Its broad gap classification remains current while detailed production-engineering execution is owned by the P1 audit/remediation plan. |
| [Technical Ownership Refinement Audit](technical-ownership-refinement-audit.md) | **Implemented / current P0.2 evidence.** Keep three semantic root skills, route pure executable mechanics module-locally, and keep dependency/test/CI under repository engineering. |
| [Operating Architecture Parity Audit](operating-architecture-parity-audit.md) | **Historical implemented evidence.** It identified the missing governance/routing layer and justified the earlier operating work. |
| [Operating Parity Acceptance](../operations/operating-parity-acceptance.md) | **Historical partial acceptance evidence.** Its governance/routing results remain valid; its overall parity conclusion is superseded. |
| [System Integration Proof](../operations/system-integration-proof.md) | **Current production evidence.** Real The Clockwork Vault Flow 2→7 run proved the replacement pipeline and a real defect→root-fix→revalidation cycle. |
| [Archived Retirement Audit](../operations/archived-retirement-audit.md) | **Historical implemented evidence.** It justified deleting the old `Production Document Builder/` live tree. |
| [Foundation Validation Report](../../foundation/validation-report.md) | **Current proof/status matrix.** It owns current production + parity-remediation evidence status. |
| [Review Template](review-template.md) | Reusable review shape when a dedicated review is actually justified. |

## Review Labels

- `active evidence` — current architecture still relies on the finding;
- `active execution evidence` — finding directly controls current work order;
- `implemented` — corresponding current-owner change exists;
- `current production evidence` — current production capability is supported by recorded proof;
- `historical partial acceptance evidence` — a prior acceptance remains valid for a narrower boundary but no longer supports the broader conclusion;
- `historical` — retained for reasoning/provenance, not current routing;
- `local proof required` — source/implementation exists but material local/browser/audio/runtime proof remains;
- `superseded` — a later decision/source replaced the old method or conclusion.

## Historical Integrity Rule

```text
keep review body historical
→ update this graph's current meaning
→ update current source/policy/next-action separately
```

Do not edit old review bodies merely to make them look current.

## Current Routing

For current work order always prefer:

`AGENTS.md → CONTEXT.md → next-action.md`

Use this graph only when historical evidence/review status materially affects the task.

## Related

- [Knowledge Dashboard](../index.md)
- [BuildIT Parity Remediation Plan](../operations/buildit-parity-remediation-plan.md)
- [Production Engineering Remediation Plan](../operations/production-engineering-remediation-plan.md)
- [Technical Ownership Decision](../decisions/technical-ownership-boundary.md)
- [Module Map](../modules/module-map.md)
