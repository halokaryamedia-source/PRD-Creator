# Next Action

Updated: 2026-08-11

## Current Status

`PRD_PROFESSIONAL_GOLDEN_CONTRACT_IMPLEMENTED_NEXT_REPRESENTATIVE_PROOF`

Working branch: **`Local` only**.

## Current PRD contract

PRD Flow 2–4 uses one semantic owner:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

The fixed gameplay PRD family remains:

```text
Overview
Gameplay Flow
  The Journey Begins
  one full flow page per gameplay package
Global Development
  Development Overview
  Session & Runtime System
  Data, Recovery & Reset
  Gameplay Package Integration
Gameplay Packages
  Gameplay Overview
  Level Design
  Developer
```

For `N` gameplay packages the shell produces `6 + 4N` pages.

Required concerns resolve only as:

```text
Defined
Explicit No
Not Applicable
Blocked
```

A mandatory concern may not silently disappear.

## Professional-quality improvements completed

The contract and renderer now standardize:

- Overview **Document Control** with version, scope, and intended production use;
- full Gameplay Flow as chronological player story;
- package **Objective Sequence** as the separate scan-friendly summary;
- **Failure / Retry / Recovery** and **Result / Scoring Model** labels;
- Level Design **Area / Spatial Constraint**;
- Developer/global **Expected System Result**;
- **Critical Constraints & Notes** with a narrow non-dumping-ground role;
- package **Acceptance & Verification** with observable definition-of-done statements;
- aggregate Final Result Contract ownership under **Data, Recovery & Reset** when applicable;
- explicit Objective Score vs `No Objective Score`, player-facing display, telemetry/export, and final-result relationship;
- English-only as default; bilingual output is intentional only when complete user-visible translation is available and reviewable.

Package Acceptance & Verification and Flow 4 document acceptance are deliberately separate concepts.

## Deterministic enforcement

The renderer fails before writing HTML when the mandatory deterministic shell is incomplete, including missing Document Control inputs or package Acceptance & Verification.

Focused regression coverage uses the professional Golden fixture rather than a minimal skeleton.

Current implementation proof:

```text
PRD Verify #73 — PASS
```

A syntax typo found by the first CI attempt of this slice was corrected at the exact renderer owner before this PASS.

Voice verification remains independent, so PRD-only work does not rerun Voice contracts by default.

## Deliberately not added

- no QA appendix/test-case framework;
- no RACI/risk-register/epic ceremony;
- no word-count or row-count quality gate;
- no semantic similarity engine;
- no permanent source-to-output matrix;
- no generic schema framework;
- no new checksum chain;
- no mobile QA as a default;
- no Voice feature changes.

The existing `content.md → render-data.json` SHA remains a separate simplification candidate, not semantic proof.

## Evidence boundary

The previous AFTERSHOCK sample remains diagnostic/mechanical evidence only. It is not semantic-quality proof for this professional contract.

The contract still needs one representative real-project run to prove that Flow 2 fills the mandatory surfaces correctly and Flow 3 produces complete, human-readable, production-usable content in practice.

## Next Step

Run **one new representative PRD Flow 2–4 production proof** using the professional Golden Mandatory Contract, then inspect the generated HTML with the user before closing Flow 2–4. Review semantic/content quality first, then use only targeted **desktop** visual sanity. Do not run mobile QA or unrelated Voice validation.
