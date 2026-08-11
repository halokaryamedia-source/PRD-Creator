# Next Action

Updated: 2026-08-11

## Current Status

`PRD_GENERIC_TEMPLATE_CLEANUP_COMPLETE_AWAIT_FURTHER_REVIEW_OR_PROOF_APPROVAL`

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

## Reading and glossary behavior

Current generated HTML provides:

- Gameplay Flow orientation;
- structured Developer Flow;
- readable production tables;
- compact Document Control;
- package-focused navigation;
- **Gameplay Journey** / **Full Production** reading views;
- package glossary highlighting and local Terms Used from `packages[].terms`.

No second glossary engine is used.

## Generic template cleanup completed

The old approved template still contained reference-project and implementation-history residue even though current PRD semantics were already generic.

That residue has now been removed from the active generator:

```text
V90 / V94 / V1.2 style comments
v14-style ... v18-style patch IDs
aftershock-* hooks/storage/runtime names
quarry-* component names
obsolete phase-* presentation naming
source-document / template-extraction revision metadata
stacked visual-polish patch styles
```

Current ownership is cleaner:

```text
CONTENT-CONTRACT.md
→ semantic document truth

approved-document.html
→ one generic stable PRD presentation/runtime

renderer
→ project data + pages + navigation + glossary data + project namespace

validator
→ current generic mechanical composition
```

The real `document.version` remains valid project metadata. Internal feature/CSS iteration numbers are not treated as document versions and must not leak into template/component naming.

A narrow regression guard prevents the known reference/patch-history tokens from returning to the approved template.

## Focused implementation proof

Current cleanup implementation gate:

```text
PRD Verify #88 — PASS
```

This is repository/regression evidence only. It is not a browser/visual PASS.

## Deliberately not run

At the user's current direction, do not run:

- representative real-project PRD proof;
- browser/desktop visual proof;
- mobile QA;
- unrelated Voice validation.

The previous AFTERSHOCK sample remains diagnostic evidence only.

## Next Step

Continue **manual/architectural review for any remaining concrete AI-slop or unclear PRD Generator behavior** without starting representative testing. Run the representative semantic + targeted desktop proof only after explicit user approval.
