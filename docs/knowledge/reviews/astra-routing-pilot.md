# Astra Routing Pilot

Purpose: validate that a strong reasoning model uses the current PRD-Creator ownership system efficiently **without introducing an Astra-specific mode or alternate workflow**.

This is a manual behavioral pilot, not a machine validator. Repository/PRD/Voice tests continue to prove executable contracts; this note records routing expectations for real model runs.

## Pass criteria

For each case, record only:

```text
mode
first owner
root semantic specialist loaded? yes/no
unnecessary approval? yes/no
unnecessary regeneration? yes/no
proof scope
result correct? yes/no
```

PASS requires the correct mode/first owner, no unnecessary specialist or approval round-trip, bounded downstream work, and sufficient proof for the claim.

## Cases

| # | Prompt shape | Expected route |
|---|---|---|
| 1 | Inspect repository state; do not change anything | Plan → current state + smallest owner → STOP |
| 2 | Revise one already-approved PRD requirement | Production Execution → changed canonical owner; add `project-document-production` only if semantic judgment is needed |
| 3 | PRD meaning is correct but visible UI/component behavior is wrong | `kits/prd-creator/document/DESIGN-CONTRACT.md` → exact implementation owner; no PRD semantic specialist by default |
| 4 | Renderer/validator executable defect with correct contracts | Maintenance → `kits/prd-creator/AGENTS.md` → exact technical owner |
| 5 | Voice wording changes an upstream gameplay/story fact | `voice-production` → nearest Voice semantic owner |
| 6 | One test/CI failure identifies a concrete implementation owner | Maintenance → first wrong owner → targeted proof; no redesign/full regression by default |
| 7 | Explicit Golden redesign | Development → `development-brief` → design contract → representative browser prototype → subjective review when needed |
| 8 | Multiple plausible material project decisions require AI choice | Flow 2 semantic owner → one concrete Proposal → user review; authoritative facts/Completions continue without redundant approval |

## Pilot protocol

1. Run the cases during normal ChatGPT/Astra sessions using the current `develop` repository state.
2. Do not pre-load adjacent owners to make the test pass.
3. Record only observed routing/proof behavior; do not score wording style.
4. A failure becomes actionable only when it is reproducible or materially costly.
5. Fix the first wrong owner; do not create model-specific modes, duplicate prompts, or compatibility layers.

## Efficiency signals

Across real project runs, optionally track only these counts when easy to observe:

- owner/files opened;
- semantic specialists loaded;
- approval round-trips;
- regenerations;
- validation runs;
- wrong-owner corrections.

Use these as evidence for later simplification. Do not build a dashboard/database solely to collect them.
