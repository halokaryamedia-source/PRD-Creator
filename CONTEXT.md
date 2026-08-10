# Workspace Context

Last verified: 2026-08-10
Stability: stable production system; BuildIT parity remediation active
Owner: workspace

## Purpose

This repository supports a two-stage production system:

1. turn incomplete/uneven project direction into development-ready project documentation;
2. derive validated ElevenLabs-ready Voice Production without inventing upstream design.

Production and agent-operation layers remain separate:

```text
Agent Operating Layer
Plan / Developing / Maintenance
→ owner + proof boundary

Production Layer
Flow 2 → Flow 3 → Flow 4 → Flow 5 → Flow 6 → Flow 7
```

## Stable Production State

Production Flow 1–7 is implemented and real-project proven on The Clockwork Vault. The old `Production Document Builder/` remains retired from live `Local`.

## Agent Governance Layer

Canonical repository-wide skills remain:

- `development-brief`;
- `project-document-production`;
- `voice-production`.

P0.2 keeps semantic/product-contract ownership in root specialists and routes pure executable mechanics to nearest kit owners. Shared dependency/test/CI work belongs to repository engineering.

## BuildIT Parity State

Overall full relevant parity remains open.

Broad audit:

`docs/knowledge/reviews/buildit-current-parity-gap-audit.md`

Production engineering audit:

`docs/knowledge/reviews/production-engineering-quality-audit.md`

Ordered engineering remediation:

`docs/knowledge/operations/production-engineering-remediation-plan.md`

## Verification Baseline

P0.1:

```text
source head       0eb0485f117fa6ed419572a66539331f99114002
Production Verify 31372363843  PASS
Repository Verify 31372363802  PASS
```

P0.2:

```text
source head       a0a51d97523ab07f87ef6deeffdafc8094febea4
Production Verify 31374226078  PASS
Repository Verify 31374226049  PASS
```

## P1.1 — PRD Mechanical Revision Integrity — COMPLETE

Source head:

`04f306f8589528ccc8cb03e89333dba174a3d276`

Current mechanical PRD contract now includes:

- structured fail-closed collection/item/stable-ID preflight before page calculation;
- deterministic SHA-256 render-data fingerprint embedded in `final.html`;
- validator rejection when current render-data and final HTML fingerprint differ;
- exact generated document section/page order/set validation.

Proof:

```text
Production Verify 31377375929  PASS
Repository Verify 31377377036  PASS
```

P1-F01 stale PRD HTML false-PASS and P1-F02 malformed render-data traceback path are implemented at the mechanical level claimed.

This does not automate semantic `content.md` → render-data correctness and does not replace browser visual review.

## Stable Authority Chain

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance
≠ Voice Requirements ≠ Voice Production Script ≠ DOCX
≠ Voice Acceptance ≠ Audio
```

## Current Development State

P0.1, P0.2, P1 audit, and P1.1 are complete. The active source-remediation slice is **P1.2 — PRD Renderer Script/Shell Safety**, covering glossary `<script>`-context safety, alias-shape preflight, and the minimum approved-shell marker/metadata contract.
