# Production + Operating Validation Report

Updated: 2026-08-11

This file owns the **current evidence state** for PRD-Creator.

## Current status

Working branch: `Local`.

PRD Flow 2–4 uses one professional Golden Mandatory PRD Contract plus one clean generic HTML presentation/runtime template. The previous AFTERSHOCK sample remains diagnostic evidence only; it is not current semantic or presentation authority.

The central semantic contract, deterministic shell, glossary wiring, professional reading composition, and current template cleanup are repository/regression-proven. A new representative real-project semantic/desktop proof has **not** been run because the user has not approved that testing step yet.

## Single semantic owner

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

It owns the fixed blueprint, mandatory-slot states, role completeness, Scoring / Result semantics, Humanize behavior, terminology/glossary semantics, package definition of done, and semantic acceptance threshold.

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

## Professional content behavior

The current contract requires:

- compact Document Control on Overview;
- full chronological Gameplay Flow;
- separate Objective Sequence;
- Failure / Retry / Recovery;
- Result / Scoring Model;
- Level Design Area / Spatial Constraint;
- Developer/global Expected System Result;
- Critical Constraints & Notes;
- package Acceptance & Verification;
- aggregate Final Result Contract ownership under Data, Recovery & Reset;
- explicit Objective Score vs `No Objective Score`, player-facing display, telemetry/export, and final-result relationship;
- English-only baseline unless bilingual copy is complete and reviewable;
- Humanize behavior that closes already-resolved trigger/action/response/result/next-state questions before moving on.

## Reading experience and glossary

Current presentation keeps the document readable without turning it into a dashboard:

- Gameplay Flow orientation before detailed narrative beats;
- structured Developer Flow with Trigger / System Behavior / Data / Expected Result;
- readable production tables and requirement/result hierarchy;
- package-focused navigation;
- Gameplay Journey and Full Production reading views;
- compact metadata vs production-content distinction;
- restrained inline glossary highlighting + Terms Used index;
- one canonical package glossary source: `packages[].terms`.

Package Gameplay Flow and its production pages use the same package ID for navigation and glossary scope. Terms Used does not recursively highlight its own definitions.

## AI-slop / template cleanup

A dedicated review found that the previously approved HTML template still contained implementation-history and reference-project residue: feature/CSS iteration labels masquerading as versions, version-suffixed style IDs, reference-project namespaces, old object-specific component names, obsolete phase-oriented presentation naming, extraction/source revision metadata, and multiple appended visual-polish patch layers.

These were not useful document versioning. They were implementation history leaking into active generator structure.

The active generator is now normalized:

- `approved-document.html` is a generic PRD template rather than an AFTERSHOCK-derived template artifact;
- the template contains one main stylesheet and stable generic document/glossary runtime;
- renderer no longer injects another UI stylesheet/runtime patch layer;
- project storage namespace comes from one generic template token and is replaced by the renderer;
- page/component hooks describe actual functions such as package, requirement, development, glossary, journey, production, and result;
- reference-project and obsolete object/phase hooks were removed from active template/renderer/validator composition;
- pseudo-version patch labels and extraction/source revision metadata were removed;
- legitimate `document.version` remains untouched as real project metadata.

A focused regression guard prevents the known reference/patch-history categories from returning to the approved template. This is a narrow anti-regression guard, not a generic naming framework.

## Deterministic enforcement

The renderer still fails before writing `final.html` when mandatory shell data is absent. The mechanical validator continues to check current generated composition, revision binding, navigation, IDs, scoring numeric consistency, and required files/state without pretending to judge prose or visual quality automatically.

Current focused gate after implementation **and** the final rendering-boundary documentation alignment:

```text
PRD Verify #89 — PASS
```

This PASS covers compilation, the full mandatory fixture, generic composition hooks, glossary safety, Flow 2 state contracts, handoff contracts, the narrow anti-slop template regression guard, and the current rendering contract.

Voice verification remains independent; PRD-only work does not rerun Voice contracts by default.

## What is deliberately not claimed

The current evidence does **not** yet prove:

- semantic quality on a fresh representative real project;
- that Flow 2 consistently recovers/fills all professional mandatory concerns from uneven source;
- that real project prose reaches the intended Humanize quality in practice;
- actual browser hover/click behavior of glossary tooltips on a newly generated representative artifact;
- desktop visual quality of a newly generated representative artifact;
- universal correctness for every future project shape.

Static/regression proof is not presented as browser/visual proof.

## Deliberately not added

- no QA test-case appendix;
- no RACI/risk register/epic framework;
- no word-count or row-count quality scoring;
- no semantic similarity engine;
- no permanent traceability matrix;
- no generic naming/versioning framework;
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
| Flow 3 | professional content + clean generic template + focused regression proof complete; representative semantic/desktop proof pending |
| Flow 4 | package definition-of-done + document acceptance boundaries aligned; representative proof pending |
| Flow 5–7 | unchanged; Voice verification remains separate |

## Current boundary

PRD Flow 2–4 is **not closed yet**.

The generator may continue through design/cleanup review without representative testing. No browser/mobile/Voice proof should be run merely for ceremony.
