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

P0.2 keeps semantic/product-contract ownership in root specialists, routes pure executable mechanics to nearest kit owners, and keeps shared dependency/test/CI work under repository engineering.

## BuildIT Parity State

Overall full relevant parity remains open.

Broad audit:

`docs/knowledge/reviews/buildit-current-parity-gap-audit.md`

Production engineering audit:

`docs/knowledge/reviews/production-engineering-quality-audit.md`

Ordered engineering remediation:

`docs/knowledge/operations/production-engineering-remediation-plan.md`

The previous Phase 3 acceptance remains historical partial evidence for the governance/routing subset.

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

## P1 Engineering Progress

### P1.1 — PRD Mechanical Revision Integrity — COMPLETE

Source `04f306f8589528ccc8cb03e89333dba174a3d276`.

```text
Production Verify 31377375929  PASS
Repository Verify 31377377036  PASS
```

P1-F01/F02 are implemented at the mechanical boundary claimed.

### P1.2 — PRD Renderer Script/Shell Safety — COMPLETE

Source `802904856b69fd50008999f196cb72d48303e0ba`.

```text
Repository Verify 31378603894  PASS
Production Verify 31378603848  PASS
```

P1-F03/F07 are implemented at the static/mechanical boundary claimed. Browser runtime/visual quality remains separate evidence.

### P1.3 — Voice Revision + DOCX Entry Integrity — COMPLETE

Source `dcb9bdf54a5749d04be2362b9d33918ab332f4f2`.

```text
Repository Verify 31379718341  PASS
Production Verify 31379718339  PASS
```

Current Voice mechanical chain now uses:

```text
voice-requirements.md normalized-text SHA-256
→ declared in canonical voice-production.md
→ builder requires exact current hash
→ builder stores requirements + script SHA-256 in DOCX core identifier
→ Flow 7 requires current requirements == script declaration == DOCX identifier
```

Flow 7 also validates each DOCX entry as a bound section + Type + Voice ID/title + duration + performance unit, rather than relying on global token presence.

`voice-state.yaml` remains lifecycle/readiness ownership; it is not a duplicate hash registry.

P1-F04/F05 are implemented at the mechanical revision/entry-binding level claimed. Semantic, rendered-page, pronunciation/performance, and audio proof remain separate.

## Stable Authority Chain

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance
≠ Voice Requirements ≠ Voice Production Script ≠ DOCX
≠ Voice Acceptance ≠ Audio
```

## Stable Structure

- `.agents/skills/` — repository-wide semantic routing/judgment skills;
- `.github/workflows/` — repeatable repository/production gates;
- `requirements.lock.txt` + `tests/` + `tools/` — repository engineering contracts;
- `docs/foundation/` — durable production policy + proof matrix;
- `docs/knowledge/` — continuity, routing, ownership, reviews, decisions, operations;
- `kits/project-document-generator/` — active PRD Flow 2–4 owner + module-local mechanics;
- `kits/voice-production-kit/` — active Voice Flow 5–7 owner + module-local mechanics;
- `workspace/active/` / `workspace/saved/` — project-specific packages.

## Current Development State

P0.1, P0.2, P1 audit, P1.1, P1.2, and P1.3 are complete. The active source-remediation slice is **P1.4 — Voice Parser / Failure-State Hardening**, focused on the known zero-entry section uncontrolled failure path before advancing to P1.5.
