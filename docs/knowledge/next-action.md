# Next Action

Updated: 2026-08-11

## Current Status

`PRD_PROFESSIONAL_READING_EXPERIENCE_IMPLEMENTED_AWAIT_USER_PROOF_APPROVAL`

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

## Professional content behavior

The contract standardizes:

- Overview Document Control;
- chronological full Gameplay Flow;
- separate Objective Sequence;
- Failure / Retry / Recovery;
- Result / Scoring Model;
- Level Design Area / Spatial Constraint;
- Developer/global Expected System Result;
- Critical Constraints & Notes;
- package Acceptance & Verification;
- aggregate Final Result Contract ownership under Data, Recovery & Reset;
- explicit Objective Score vs `No Objective Score`, player-facing display, telemetry/export, and final-result relationship;
- English-only default unless bilingual copy is complete and reviewable;
- Humanize prose that closes already-resolved trigger/action/response/result/next-state questions rather than leaving the reader to infer them.

## Reading experience completed

The renderer now also provides a clearer professional reading experience without changing project meaning:

- package Gameplay Flow gets a compact orientation summary;
- Developer Flow keeps Trigger / System Behavior / Data / Expected Result separate;
- production tables have more breathing room and clearer result hierarchy;
- Document Control is compact metadata rather than another note block;
- Main Systems is visually distinct;
- package subnavigation is active-focused;
- reading modes are **Gameplay Journey** and **Full Production**;
- web sheets use content height while print behavior stays bounded;
- new PRD reading refinements stay in one renderer-owned style/runtime layer instead of accumulating another template style patch.

## Glossary Index restored

The approved Golden tooltip engine was never removed, but new package Gameplay Flow pages were not scoped for it correctly.

Current wiring now uses one canonical source:

```text
packages[].terms
```

That term index drives both inline glossary help and role-local Terms Used. Package-owned full Gameplay Flow now receives package scope and the same gameplay-visible term index. Terms Used itself is excluded from recursive highlighting.

No second glossary engine or duplicate terminology artifact was added.

## Focused implementation proof

Current final implementation gate after `kits/**` contract/rendering alignment:

```text
PRD Verify #81 — PASS
```

The first UI-slice run correctly exposed one stale validator expectation for the previous Developer Flow class. The validator was updated to recognize the new structured Developer Flow instead of restoring the old compressed presentation.

This is repository/regression evidence only. It is not a browser/visual PASS.

## Deliberately not run

At the user's current direction, do not run:

- representative real-project PRD proof;
- browser/desktop visual proof;
- mobile QA;
- unrelated Voice validation.

The previous AFTERSHOCK sample remains diagnostic/mechanical evidence only and does not become proof for the new professional reading contract.

## Next Step

**Wait for explicit user approval before running the representative real-project semantic + targeted desktop proof.** Until that approval, only address a new concrete PRD readability/content defect if the user identifies one.
