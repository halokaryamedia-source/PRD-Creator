# Workspace Context

Last verified: 2026-08-10
Stability: stable production system; normal project work ready
Owner: workspace

## Purpose

PRD-Creator supports two connected outcomes:

1. turn incomplete project direction into development-ready project documentation;
2. derive ElevenLabs-ready Voice Production from accepted project documentation without inventing upstream design.

## Production model

```text
Flow 2 Source Intake
→ Flow 3 PRD Generation
→ Flow 4 PRD Validation/Handoff
→ Flow 5 Voice Requirements
→ Flow 6 Voice Script + DOCX
→ Flow 7 Voice Validation/Delivery
```

Flow 1–7 is implemented and real-project proven on The Clockwork Vault. The retired `Production Document Builder/` is not a live owner.

## Agent operating model

```text
Plan | Developing | Maintenance
→ smallest correct owner
→ minimum complete change
→ minimum useful proof
```

Root skills remain:

- `development-brief`;
- `project-document-production`;
- `voice-production`.

Pure renderer/validator/builder mechanics stay module-local. Shared dependency/test/CI mechanics stay repository-engineering owned.

## Anti-overdevelopment rule

Current durable decision:

`docs/knowledge/decisions/anti-overdevelopment-simplification.md`

BuildIT is a **reference for discipline**, not a checklist of architecture/features that PRD-Creator must reproduce.

The repository must remain easy to use. Normal project production must not require operators to understand checksums, revision fingerprints, generated-artifact identifiers, or internal engineering ceremony.

Current production flow is intentionally:

```text
canonical input
→ generate
→ focused validate
→ semantic/visual/audio review only where that evidence is actually required
```

## Verification

- `Repository Verify` — static repository/routing/navigation/syntax/dependency invariants.
- `Production Verify` — locked dependency install, compile, focused PRD contracts, focused Voice contracts, fail-closed aggregate.

Latest simplification proof:

```text
source 08b6f9d6a98641c5f93932df015cb0d2dffe9a42
Repository Verify 31381677940 PASS
Production Verify 31381677946 PASS
```

These gates do not replace semantic review, browser visual QA, DOCX page inspection, pronunciation/performance judgement, or actual audio review.

## Stable authority chain

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance
≠ Voice Requirements ≠ Voice Production Script ≠ DOCX
≠ Voice Acceptance ≠ Audio
```

Derived artifacts stay derived. When an upstream canonical file changes, regenerate the affected downstream artifact rather than adding another revision-management system.

## Current development state

There is no automatic parity-remediation phase active.

The repository is ready for the next real project/task. New engineering work starts only from a concrete current need or observed defect.
