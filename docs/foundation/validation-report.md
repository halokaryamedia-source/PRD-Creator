# Production + Operating Validation Report

Updated: 2026-08-11

This file records the **current evidence state** for PRD-Creator. Historical debugging belongs in Git history, not here.

## Current status

Working branch: `Local`.

PRD Flow 2–4 currently uses:

```text
CONTENT-CONTRACT.md
→ single semantic/content authority

SOURCE-INTAKE.md
→ source recovery + one integrated production-readiness pass

approved-document.html
→ generic stable PRD presentation/runtime

renderer
→ deterministic project projection

validator
→ deterministic mechanical checks only

VALIDATION.md
→ semantic/document acceptance procedure
```

## Current gameplay PRD family

For `N` gameplay packages:

```text
Overview                                      1
Gameplay Flow: Journey Begins + N packages    1 + N
Global Development                            4
Gameplay role pages                           3N
-----------------------------------------------
Total                                         6 + 4N
```

Global Development uses Development Overview, Session & Runtime System, Data, Recovery & Reset, and Gameplay Package Integration. Every package keeps Gameplay Overview, Level Design, and Developer.

## Current semantic behavior

The contract requires explicit project context/session/playtime/structure, chronological Gameplay Flow plus Objective Sequence, complete Level Design and Developer meaning, Failure / Retry / Recovery, explicit Objective Score or `No Objective Score`, separate final-result/display/telemetry behavior, package Acceptance & Verification, one canonical package glossary index, and bounded Humanize writing.

Mandatory concerns resolve only as:

```text
Defined | Explicit No | Not Applicable | Blocked
```

## Pre-test blocker corrections

The three deterministic blockers found immediately before representative testing are closed:

1. **Glossary role visibility** — omitted `roles` now means all package reader roles; explicit roles constrain both inline glossary highlighting and Terms Used through role-scoped glossary data.
2. **Reset / Interruption result** — `developer.reset_result` is mandatory, so a reset requirement cannot render with a blank Expected System Result.
3. **Acceptance lens persistence** — Flow 4 acceptance records and handoff validation now require explicit `Acceptance: PASS` in addition to New Reader, Level Designer, Developer, and Project Consistency.

Focused contract proof after these corrections:

```text
PRD Verify #108 — PASS
```

This proves the corrected deterministic contracts compile and pass the focused PRD regression suite.

## Representative AFTERSHOCK test — Flow 2 result

Representative testing has now started using the current authoritative AFTERSHOCK `Gameplay Development Specification | FINAL v2.4` plus the approved Golden Sample as a document-quality/reference source.

Flow 2 found a real material scoring conflict and correctly **did not** advance to Flow 3:

- current v2.4 explicitly forbids player-facing scores/results and excludes scores/aggregates/interpretations from raw telemetry;
- current v2.4 records objective-specific progress/outcome data but does not define an internal Objective Score formula;
- the older Golden Sample contains internal Quarry/Ascent/Beacon/Relay scoring and Final Total, but several Golden scoring formulas depend on mechanics that no longer match v2.4;
- therefore `No Objective Score` cannot be inferred from display/export prohibitions, while old Golden formulas also cannot be copied as current project truth.

Examples of material mechanic drift include:

```text
Quarry
v2.4 → timed mining/deposit milestones + optional no-reward stretch
old Golden scoring → Time Score + Surplus Score

Beacon
v2.4 → guided Beacon Brick build + deterministic 25%/35% storm removal
old Golden scoring → Time Score + Storm Exposure model

Relay
v2.4 → waypoint braziers + repeated gale pushback
old Golden scoring → previous relay/cable scoring model
```

This is a **correct Flow 2 block**, not a renderer failure. Inventing a new scoring formula or silently restoring incompatible Golden mechanics would violate current authority and the mandatory-slot contract.

## Evidence boundary

Not yet proven on a fresh representative final artifact:

- Flow 3 Humanize quality on the resolved AFTERSHOCK project;
- complete role-page semantic parity after current scoring is resolved;
- actual browser/desktop visual quality;
- glossary hover/click behavior in the new representative artifact;
- Flow 4 handoff on the representative artifact.

The representative test is paused at the first material unresolved decision rather than manufacturing downstream output.

## Current flow evidence

| Flow | Evidence state |
|---|---|
| Flow 1 | repository/static proof current |
| Flow 2 | representative test correctly detected current AFTERSHOCK scoring ambiguity and blocked downstream authoring |
| Flow 3 | deterministic contracts current; representative authoring waits for scoring resolution |
| Flow 4 | corrected Acceptance/handoff contract current; representative review waits for Flow 3 output |
| Flow 5–7 | unchanged; Voice verification remains separate |

## Current boundary

PRD Flow 2–4 is not yet end-to-end proven. The next representative action must resolve the current AFTERSHOCK internal scoring model from current authority/approved decision before Flow 3 can continue.
