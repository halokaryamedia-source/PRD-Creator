# Production + Operating Validation Report

Updated: 2026-08-11

This file records the **current evidence state** only. Historical debugging belongs in Git history.

## Current status

Working branch: `Local`.

The PRD Generator now uses the approved Golden Sample as the **canonical visible page prototype**.

```text
SOURCE-INTAKE.md
→ project truth

CONTENT-CONTRACT.md
→ project semantics + locked Golden visible composition

approved-document.html + renderer
→ deterministic Golden-prototype projection

validator
→ deterministic mechanical composition checks

VALIDATION.md
→ semantic + Golden-fidelity + targeted visual review
```

## Corrected direction

The previous representative preview introduced visible composition that was not present in Golden, including:

- verbose 3-card Gameplay Overview summaries;
- orientation cards on Gameplay Flow;
- 2×2 Trigger / System Behavior / Data / Expected Result Developer Flow;
- extra Acceptance & Verification presentation;
- renamed Global Development pages;
- Terms Used on surfaces where Golden does not show it;
- a wider/looser document treatment that reduced reading clarity.

That preview is **rejected and superseded as visual evidence**. It must not be cited as a visual PASS.

The active generator has been rolled back to Golden page prototypes instead of adding another redesign layer.

## Current Golden composition

```text
Overview
Gameplay Flow
Development
  Development Overview
  Game System
  Data and Reset
  Gameplay Development
Gameplay package
  Gameplay Overview
  Level Design
  Developer
```

For `N` packages: `6 + 4N` pages.

Visible package rules now match Golden:

```text
Gameplay Overview
→ 3 short summary cards
→ Gameplay Information
→ Gameplay Flow
→ Terms Used

Level Design
→ Level Design Overview
→ 4-card Design Flow
→ Build Requirements
→ Important Build Notes

Developer
→ Developer Overview
→ 4-card Development Flow
→ Development Requirements
→ Important Development Notes
```

Acceptance remains required Flow 4 project/review meaning but is not rendered as a new Developer-page panel.

Terms Used is rendered only on Gameplay Flow, Global Development and Gameplay Overview. Inline glossary highlighting remains role-scoped.

## Anti-regression behavior

The focused PRD regression now explicitly rejects the discarded experimental visible vocabulary/components, including:

```text
Document Control
Session & Runtime System
Data, Recovery & Reset
Gameplay Package Integration
Objective Sequence
Failure / Retry / Recovery
Result / Scoring Model
Area / Spatial Constraint
Expected System Result
Critical Constraints & Notes
Acceptance & Verification
flow-orientation
developer-flow
System Behavior
```

Level Design and Developer are also checked not to render a visible Terms Used block.

## Stable version policy

`document.version` is project/release metadata, not an edit counter.

Clarification, Humanize, review correction, rerendering and representative testing keep the same version. AFTERSHOCK remains **2.4** until a real revision/release milestone is intentionally declared.

## AFTERSHOCK project truth retained

The previously approved v2.4 scoring decision remains project truth:

```text
Docks    → No Objective Score
Quarry   → 0–100 main Forge progress normalized to Gold; Stretch excluded
Ascent   → 100 on Signal Horn/cable-car valid completion; otherwise highest checkpoint progress
Beacon   → 0–100 final valid scaffold completion
Relay    → 100 on Relay activation; otherwise farthest valid route progress
Ending   → No Objective Score
Final Total = (Quarry + Ascent + Beacon + Relay) ÷ 4
```

Internal scores remain hidden from the player and excluded from raw telemetry/export.

## Evidence boundary

Current repository/regression evidence proves the strict Golden prototype contract and renderer/validator behavior. The old experimental AFTERSHOCK desktop preview is no longer valid visual evidence.

A fresh AFTERSHOCK v2.4 artifact must be regenerated with the locked Golden prototypes before representative desktop quality can be accepted.

No mobile or Voice proof is required for this correction.
