# Production + Operating Validation Report

Updated: 2026-08-11

This file owns the **current evidence state** for PRD-Creator.

## Current status

Working branch: `Local`.

PRD Flow 2–4 has been restructured around one **Golden Mandatory PRD Contract**. The previous AFTERSHOCK sample remains diagnostic evidence only; its earlier semantic PASS was revoked after direct review exposed scoring, Gameplay Flow, Development completeness, and writing-quality failures.

The new contract is implemented and regression-proven at repository level. It has **not yet received a new representative real-project semantic/desktop proof**.

## Single semantic owner

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

It now owns:

- the fixed gameplay PRD blueprint;
- mandatory surfaces and blocks;
- mandatory-slot states: Defined / Explicit No / Not Applicable / Blocked;
- Objective Score vs explicit `No Objective Score`;
- player-facing display vs telemetry/export distinctions;
- Gameplay Flow as chronological player journey;
- fixed four-page Global Development structure;
- Level Design and Developer completeness;
- bounded PRD Humanize behavior;
- semantic acceptance threshold.

Flow 2/3/4, skill, renderer policy, and validation policy point to this owner instead of carrying competing Golden checklists.

## Deterministic Golden shell now enforced before render

The renderer now fails before writing `final.html` when the deterministic shell is incomplete.

For `N` gameplay packages the fixed family is:

```text
Overview                                      1
Gameplay Flow: Journey Begins + N packages    1 + N
Global Development                            4
Gameplay role pages                           3N
-----------------------------------------------
Total                                         6 + 4N
```

Global Development is fixed to:

```text
Development Overview
Game System
Data and Reset
Gameplay Development
```

Every package requires:

```text
Gameplay Overview
Level Design
Developer
```

with the mandatory role blocks defined in `CONTENT-CONTRACT.md`.

## Scoring / Result correction

Every gameplay package now carries exactly one explicit internal result model:

```text
Objective Score
OR
No Objective Score
```

The renderer/result contract keeps these separate:

```text
internal score/result
player-facing result display
telemetry/export behavior
final-result relationship
```

A display/export prohibition cannot silently erase an internal Objective Score.

Non-scored packages render `No Objective Score` visibly rather than disappearing into generic completion text.

## Regression suite cleanup

The PRD regression fixture now represents the complete mandatory Golden shell instead of a minimal skeleton.

Focused regression coverage proves:

- complete mandatory shell renders and validates;
- missing Global Development function/package Gameplay Flow/core role blocks fail before HTML is written;
- non-scored packages visibly retain `No Objective Score` plus final/display/export behavior;
- percentage strings do not render double `%`;
- intentional bilingual output rejects implicit translation;
- stale HTML is rejected after projection change;
- glossary JSON remains script-safe;
- required Golden template shell markers remain present;
- existing Flow 2 and handoff consistency guards still pass their focused suites.

No word-count, row-count, semantic-similarity, or generic traceability framework was added.

## CI proof economy

Production CI is now split by domain.

### PRD Verify

PRD-only changes run PRD compile/contracts only. The latest implementation gate for this contract recorded:

```text
PRD Verify #68 — PASS
```

This run includes the final mandatory-shell renderer/result changes and focused PRD regression suite.

### Voice Verify

Voice now has an independent workflow. Creation of that workflow recorded:

```text
Voice Verify #1 — PASS
```

Future PRD-only changes no longer rerun Voice contracts merely because both systems share one repository.

## What is deliberately not claimed

The new mandatory contract does **not yet** prove:

- semantic quality on a new representative real project;
- that Flow 2 reliably fills every mandatory concern from uneven source in practice;
- humanized Gameplay Flow/Development prose quality on a real generated document;
- desktop visual quality of a newly generated representative document under the new contract;
- universal correctness for every future project shape.

The previous AFTERSHOCK sample cannot supply those claims because its semantic threshold was the defect that triggered this redesign.

## Existing mechanical boundaries

The current `content.md → render-data.json` SHA remains unchanged for now as a stale-byte binding only. It still does not prove semantic equivalence and remains a separate simplification candidate.

The deterministic `render-data.json → final.html` binding remains useful for stale rendered-output detection.

No new checksum chain was added.

## Current flow evidence

| Flow | Current evidence state |
|---|---|
| Flow 1 | current repository/static proof |
| Flow 2 | fixed mandatory semantic contract implemented; representative proof pending |
| Flow 3 | fixed Golden shell + focused regression proof complete; representative semantic/desktop proof pending |
| Flow 4 | acceptance routed through single mandatory contract; representative proof pending |
| Flow 5–7 | unchanged; Voice Verify separated |

## Current boundary

PRD Flow 2–4 is **not closed yet**.

The patch-by-patch rule problem has been replaced by one central mandatory contract and a fail-closed deterministic shell. The remaining useful proof is one new representative project produced under this contract and reviewed for content quality, followed by targeted desktop sanity only.
