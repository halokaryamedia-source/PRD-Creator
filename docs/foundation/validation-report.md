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

## Current deterministic proof

The three pre-test blockers remain closed:

1. glossary role visibility is consistent between inline highlighting and Terms Used;
2. Reset / Interruption requires a non-empty Expected System Result;
3. Flow 4/handoff requires explicit `Acceptance: PASS`.

Current focused production gate after the stable-version policy update:

```text
PRD Verify #109 — PASS
```

Repository verification after that policy update:

```text
Repository Verify #197 — PASS
```

## Stable document-version policy

`document.version` is project/release metadata, not an edit counter.

Normal clarification, Humanize, rerendering, review correction, and representative testing keep the same version. A version changes only when the user/source explicitly defines a new revision or the team intentionally declares a new release/handoff milestone.

The representative AFTERSHOCK document therefore remains **2.4** throughout this proof.

## Representative AFTERSHOCK proof

Representative testing uses current AFTERSHOCK `Gameplay Development Specification | FINAL v2.4` as project authority and the approved Golden Sample only as a document-function/quality reference.

The user approved the current progress-based internal scoring model:

```text
Docks    → No Objective Score
Quarry   → 0–100 main Forge progress normalized to Gold; Stretch excluded
Ascent   → 100 on Signal Horn/cable-car valid completion; otherwise highest checkpoint progress
Beacon   → 0–100 final valid scaffold completion
Relay    → 100 on Relay activation; otherwise farthest valid route progress
Ending   → No Objective Score
Final Total = (Quarry + Ascent + Beacon + Relay) ÷ 4
```

All internal scores remain hidden from the player and excluded from raw telemetry/export.

### Flow 2

PASS / `ready_for_prd` after the scoring decision.

Recovered project truth also preserves:

- isolated concurrent lanes and start-gate boundary;
- Adventure Mode with package-specific scripted permissions;
- game-time pause and disconnect/rejoin behavior;
- Quarry scripted deposits, optional no-reward Stretch, and configurable Flat Mode that launches OFF;
- Ascent harmless fall/recovery and assistance rules;
- Beacon deterministic 25%/35% storms, idle scheduling, external-cause presentation, and nearby free pickups;
- Relay ~100–120 block route, configurable ~75-second rhythm with roughly six meaningful gale cycles, equal routes, and safe recovery;
- Ending persistence before lobby return/reset.

### Flow 3 semantic candidate

The representative candidate contains six gameplay packages and the fixed 30-page family (`6 + 4N`).

The first semantic pass found and corrected project-document quality issues before proof was accepted:

- generator/repository meta-language had leaked into Global Development notes and was removed;
- Global Development was rewritten around actual runtime/package handoff rather than authoring-process instructions;
- Final Total now explicitly refuses missing/invalid inputs instead of substituting zero/duplicates;
- Beacon free-pickup recovery and Relay target gale pacing were restored from source;
- glossary coverage was expanded with source-grounded package terms;
- document version remained 2.4 throughout all corrections.

Integrated semantic review after correction:

```text
New Reader          PASS
Level Designer      PASS
Developer           PASS
Acceptance          PASS
Project Consistency PASS
Critical            0
Major               0
```

### Targeted desktop proof

A representative standalone HTML preview was rendered from the current canonical candidate and inspected in Chromium at 1440×1050. This is a desktop-only proof; mobile was intentionally not run.

Observed checks:

```text
30 document sections                         PASS
browser console/page errors                  0
horizontal document overflow                 none
Gameplay Journey / Full Production switch    PASS
Quarry Gameplay Flow readability             PASS
Quarry Level Design table readability        PASS
Quarry Developer scoring/result readability  PASS
Reset Expected System Result                 present
Acceptance & Verification                    readable
inline glossary tooltip                      PASS
role-scoped glossary                          PASS
Flat Mode highlighted on Gameplay             no
Flat Mode highlighted on Level Design         no
Flat Mode highlighted on Developer            yes
Terms Used self-highlighting                  none
```

The desktop preview shows the intended information hierarchy, role separation, glossary affordance, and scoring/reset/acceptance presentation without changing document version 2.4.

## Evidence boundary

The representative semantic candidate and desktop preview are proven, and the active production renderer/template contracts are regression-proven by PRD Verify.

However, the exact representative `render-data.json` was **not executed through the repository's production renderer/validator inside this sandbox** because the execution environment could inspect GitHub through the connector but could not materialize those repository source files into the local runtime. Therefore this report does not claim exact candidate production-renderer E2E or handoff PASS yet.

Do not convert the standalone preview proof into a claim that canonical `output/final.html` has passed the exact production renderer/validator.

## Current flow evidence

| Flow | Evidence state |
|---|---|
| Flow 1 | repository/static proof current |
| Flow 2 | representative AFTERSHOCK source recovery + approved scoring decision PASS |
| Flow 3 | representative canonical content semantic PASS; production renderer contract regression PASS; exact candidate renderer execution pending |
| Flow 4 | integrated semantic PASS + targeted desktop preview PASS; canonical mechanical/handoff acceptance pending exact candidate execution |
| Flow 5–7 | unchanged; Voice verification remains separate |

## Current boundary

The generator is ready for the final representative mechanical step. No additional architecture redesign or document-version bump is required before that proof.
