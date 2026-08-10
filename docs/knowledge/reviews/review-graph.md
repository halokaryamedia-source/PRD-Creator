# Review Graph

Updated: 2026-08-10

Use this note to understand how reviews/audits/evidence relate to current `Local`. Review bodies preserve what was observed at capture time; current meaning belongs here.

## Current Review Status

| Evidence / review | Current meaning |
|---|---|
| [Production Engineering Quality Audit](production-engineering-quality-audit.md) | **Active execution evidence.** P1-F01/F02 are implemented by P1.1; P1-F03/F07 are implemented by P1.2. P1-F04/F05 now govern active P1.3 Voice revision/DOCX integrity work. Remaining F06/F08/F09 stay ordered behind it. |
| [BuildIT Current Parity Gap Audit](buildit-current-parity-gap-audit.md) | **Active evidence.** Overall relevant parity remains open; the broad gap classification still governs the top-level remediation track. |
| [Technical Ownership Refinement Audit](technical-ownership-refinement-audit.md) | **Implemented/current evidence.** Keep three semantic root skills; route pure mechanics to nearest kit owner and shared dependency/test/CI to repository engineering. |
| [Operating Architecture Parity Audit](operating-architecture-parity-audit.md) | **Historical implemented evidence.** Correctly identified the original governance/routing gap. |
| [Operating Parity Acceptance](../operations/operating-parity-acceptance.md) | **Historical partial acceptance evidence.** Agent-governance results remain valid; overall parity conclusion is superseded. |
| [System Integration Proof](../operations/system-integration-proof.md) | **Current production evidence.** Real Clockwork Vault Flow 2→7 execution and defect→root-fix→revalidation proof. |
| [Archived Retirement Audit](../operations/archived-retirement-audit.md) | **Historical implemented evidence.** Justified retiring `Production Document Builder/`. |
| [Foundation Validation Report](../../foundation/validation-report.md) | **Current proof/status matrix.** Owns current production and parity-remediation evidence status. |
| [Review Template](review-template.md) | Reusable review shape when a dedicated review adds durable evidence. |

## Review Labels

- `active evidence` — current architecture still relies on the finding;
- `active execution evidence` — finding directly controls current work order;
- `implemented` — corresponding current-owner change exists;
- `current production evidence` — current production capability is supported by recorded proof;
- `historical partial acceptance evidence` — prior acceptance remains valid only for a narrower boundary;
- `historical` — retained for reasoning/provenance, not current routing;
- `local proof required` — implementation exists but material local/browser/audio/runtime proof remains;
- `superseded` — later evidence/decision replaced the old conclusion.

## Historical Integrity Rule

```text
keep review body historical
→ update this graph's current meaning
→ update current source/policy/next-action separately
```

Do not rewrite old review bodies merely to make them look current.

## Current Routing

For current work order prefer:

`AGENTS.md → CONTEXT.md → next-action.md`

Use this graph only when historical review status materially affects the task.

## Related

- [Knowledge Dashboard](../index.md)
- [BuildIT Parity Remediation Plan](../operations/buildit-parity-remediation-plan.md)
- [Production Engineering Remediation Plan](../operations/production-engineering-remediation-plan.md)
- [Technical Ownership Decision](../decisions/technical-ownership-boundary.md)
- [Module Map](../modules/module-map.md)
