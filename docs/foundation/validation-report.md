# Production + Operating Validation Report

Updated: 2026-08-11

This file owns the **current evidence state** for PRD-Creator.

## Current status

Working branch: `Local`.

PRD Flow 2–4 now uses one **professional Golden Mandatory PRD Contract** plus a bounded renderer-owned reading layer. The previous AFTERSHOCK sample remains diagnostic evidence only; its old semantic PASS was revoked after direct review exposed scoring interpretation, Gameplay Flow, Development completeness, writing-quality, and readability failures.

The central semantic contract, deterministic shell, and current reading/glossary wiring are repository/regression-proven. A new representative real-project semantic/desktop proof has **not** been run because the user has not approved that testing step yet.

## Single semantic owner

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

It owns the fixed blueprint, mandatory-slot states, role completeness, Scoring / Result semantics, Humanize behavior, professional terminology, package glossary semantics, package definition of done, and semantic acceptance threshold. Other Flow 2–4 owners reference it instead of keeping competing Golden checklists.

## Professional Golden shell

For `N` gameplay packages:

```text
Overview                                      1
Gameplay Flow: Journey Begins + N packages    1 + N
Global Development                            4
Gameplay role pages                           3N
-----------------------------------------------
Total                                         6 + 4N
```

Global Development uses:

```text
Development Overview
Session & Runtime System
Data, Recovery & Reset
Gameplay Package Integration
```

Every package keeps Gameplay Overview, Level Design, and Developer pages.

## Professional content contract

The current contract requires:

- compact **Document Control** on Overview: version, scope, intended production use;
- full top-level Gameplay Flow as the chronological player story;
- package **Objective Sequence** as the separate scan-friendly summary;
- **Failure / Retry / Recovery** and **Result / Scoring Model** labels;
- Level Design **Area / Spatial Constraint**;
- Developer/global **Expected System Result**;
- **Critical Constraints & Notes** with a narrow non-dumping-ground role;
- package-level **Acceptance & Verification** with observable definition-of-done statements;
- aggregate scoring/final-result rules owned by **Data, Recovery & Reset** when applicable;
- explicit Objective Score vs `No Objective Score`, player-facing display, telemetry/export, and final-result relationship;
- English-only as the default baseline; bilingual output only when complete user-visible translation is available and reviewable;
- Humanize behavior that closes already-resolved trigger/action/response/result/next-state questions before moving on.

Package Acceptance & Verification is part of the PRD. It is distinct from `work/acceptance.md`, which records whether the document revision itself passed Flow 4.

## Reading-experience and glossary correction

The UI/readability audit found that the Golden template's inline glossary engine still existed, but newly generated full Gameplay Flow pages lacked the package phase scope required by that runtime. The generator also used package terms for inline glossary JSON while full Gameplay Flow could use a separate term collection, creating drift risk.

The current implementation now:

- uses `packages[].terms` as the canonical package glossary source;
- applies package scope to package-owned full Gameplay Flow pages so the existing Golden glossary engine can index them;
- uses the same package terms for full Gameplay Flow Terms Used according to gameplay role visibility;
- excludes the Terms Used disclosure from recursive inline term matching;
- gives glossary terms a restrained visible affordance rather than indistinguishable bold text;
- keeps the approved Golden tooltip engine as the interaction owner rather than adding a second glossary system.

Other bounded reading improvements now include:

- wider desktop reading surface while preserving print behavior;
- content-height document sheets on screen to reduce artificial empty space;
- Document Control rendered as metadata rather than another warning/note block;
- Main Systems separated visually from metadata;
- package Gameplay Flow orientation for Player Goal / previous stage / next destination using existing truth only;
- structured Developer Flow with distinct Trigger / System Behavior / Data / Expected Result;
- more readable production tables and stronger requirement/result hierarchy;
- Acceptance & Verification rendered as observable completion checks;
- active-focused package subnavigation rather than exposing all package subpages at once;
- reading mode labels changed from ambiguous `Overview / Full Detail` to **Gameplay Journey / Full Production**.

New PRD-specific UI refinements are centralized in the existing renderer-owned reading style/runtime rather than adding another versioned `<style>` patch to the large approved template.

## Scoring / Result correction

Every package carries exactly one explicit internal result model:

```text
Objective Score
OR
No Objective Score
```

The renderer keeps internal result, final-result relationship, player-facing display, and telemetry/export separate. A display/export prohibition cannot erase an internal Objective Score.

## Deterministic enforcement

The renderer fails before writing `final.html` when deterministic mandatory shell data is absent. Current checks include the fixed hierarchy/order, Overview document-control inputs, package role blocks, explicit result contract, reset/interruption data, and non-empty package Acceptance & Verification content.

The mechanical validator checks current generated composition but does not score prose quality or visual aesthetics.

During the reading-experience slice, the first PRD run failed because the validator still required the old `quarry-development-flow` presentation class on Developer pages. The generated Developer Flow had intentionally moved to the clearer structured `developer-flow` component. The stale composition expectation was corrected at the validator owner rather than reintroducing the old UI.

Current implementation proof after the final `kits/**` contract/rendering documentation alignment:

```text
PRD Verify #81 — PASS
```

This PASS covers compile + existing focused PRD contracts with the renderer, glossary wiring, reading composition, fixture assertions, validator composition marker, and current contract/rendering owners aligned.

Voice verification remains independent; PRD-only work does not rerun Voice contracts by default.

## What is deliberately not claimed

The current evidence does **not** yet prove:

- semantic quality on a fresh representative real project;
- that Flow 2 consistently recovers/fills all professional mandatory concerns from uneven source;
- that real project prose reaches the intended Humanize quality in practice;
- actual browser hover/click behavior of glossary tooltips on a newly generated representative artifact;
- desktop visual quality of a newly generated representative artifact;
- universal correctness for every future project shape.

Static/regression wiring is not presented as browser/visual proof.

## Deliberately not added

- no QA test-case appendix;
- no RACI/risk register/epic framework;
- no word-count or row-count quality scoring;
- no semantic similarity engine;
- no permanent traceability matrix;
- no generic schema framework;
- no second glossary system;
- no new checksum chain;
- no mobile QA as a default;
- no Voice feature changes.

The existing `content.md → render-data.json` SHA remains a separate simplification candidate; it is a stale-byte binding, not semantic proof.

## Current flow evidence

| Flow | Current evidence state |
|---|---|
| Flow 1 | current repository/static proof |
| Flow 2 | professional mandatory semantic contract implemented; representative proof pending |
| Flow 3 | professional Golden shell + current reading/glossary regression proof complete; representative semantic/desktop proof pending |
| Flow 4 | package definition-of-done + document acceptance boundaries aligned; representative proof pending |
| Flow 5–7 | unchanged; Voice verification remains separate |

## Current boundary

PRD Flow 2–4 is **not closed yet**.

The current implementation should remain in design/review state until the user explicitly approves a representative real-project proof. No browser/mobile/Voice proof should be run merely for ceremony.
