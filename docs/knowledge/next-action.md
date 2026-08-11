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

The contract standardizes Overview context/control, chronological Gameplay Flow, Objective Sequence, Failure / Retry / Recovery, Result / Scoring Model, role-specific production requirements, Acceptance & Verification, explicit scored/non-scored behavior, and bounded Humanize writing.

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

The old approved template contained reference-project and implementation-history residue even though current PRD semantics were already generic.

The active generator has now removed:

- internal feature/CSS iteration labels used as pseudo-versions;
- version-suffixed patch-style IDs;
- reference-project runtime/storage/component names;
- obsolete object/phase-specific presentation hooks;
- extraction/source revision metadata;
- stacked visual-polish patch layers.

Current ownership is:

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

The real `document.version` remains valid project metadata. Internal feature/CSS iteration numbers are not document versions and must not leak into template/component naming.

A narrow regression guard prevents the known reference/patch-history categories from returning to the approved template.

## Focused implementation proof

Current gate after implementation and rendering-boundary documentation alignment:

```text
PRD Verify #89 — PASS
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
