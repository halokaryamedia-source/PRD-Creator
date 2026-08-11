# Production + Operating Validation Report

Updated: 2026-08-11

This file owns the **current evidence state** for PRD-Creator. Historical project proof remains useful evidence, but it must not be presented as proof that a later repository revision was re-executed on the same real project.

## Evidence boundary

Keep these evidence classes separate:

- **Current repository/static proof** — current `Local` code, documentation, regression contracts, and GitHub Actions have been inspected/executed for the stated repository claim.
- **Historical real-project proof** — an earlier repository revision was exercised on a real project and may still demonstrate product/workflow feasibility, but it does not automatically prove later changed contracts.
- **Current real-project/browser/DOCX/audio proof** — requires the current changed behavior to be exercised on an actual project or rendered/reviewed in the relevant medium.

Root evidence labels remain authoritative. Static/GitHub proof must not be upgraded into a current-project browser/audio/runtime claim.

## Current revision status

Current working branch: `Local`.

The latest correction work was performed through repository inspection and GitHub Actions only. The changed contracts therefore have **current repository/static proof**, while real-project/browser proof for those changed contracts remains deferred by user direction.

| Flow | Current evidence state | Current note |
|---|---|---|
| 1. Repository Boot & Project Memory | **current repository/static proof** | Current-state owners separate current versus historical proof. |
| 2. Source Intake & Requirement Recovery | **historical real-project proof + current static contract proof** | Flow 4 now rejects only unambiguous persisted blockers that contradict `ready_for_prd`; this narrow guard has not been re-run on a current real project. |
| 3. PRD Generation | **historical real-project proof + current static contract proof** | Earlier canonical PRD/rendering production was proven; current content→projection and projection→HTML bindings plus bilingual/scoring/grid corrections are regression/CI proven. |
| 4. PRD Validation & Handoff | **historical real-project proof + current static contract proof** | Current mechanical checks cover explicit Flow 2 readiness blockers, stale projection/HTML, and handoff-version consistency. |
| 5. Voice Requirement Extraction | **historical real-project proof** | The Clockwork Vault previously exercised real Voice scope extraction. No current-revision Voice production proof was created by the current PRD-side correction batch. |
| 6. Voice Script + DOCX | **historical real-project proof** | Earlier Voice ID/Type parity and DOCX generation were exercised. |
| 7. Voice Validation & Delivery | **historical real-project proof** | Earlier real DOCX visual QA found/fixed the blank-page defect. Audio evidence for that proof remained `not_provided`. |

## Historical real-project proof

The Clockwork Vault remains valid historical evidence that the end-to-end Flow 1–7 production model has been exercised on a real project.

That means:

```text
real-project feasibility was demonstrated on the revision exercised at that time
```

not:

```text
all later repository changes are automatically CURRENT-PROJECT VERIFIED
```

## Current PRD false-green correction sequence

Current PRD-side contracts now protect these concrete cases:

- Flow 4 rejects missing/ambiguous/non-ready `state/intake-state.yaml`;
- if Flow 2 claims readiness, Flow 4 rejects only unambiguous persisted blockers already present in the existing state files:
  - `requirement-register.yaml`: `approval_status: pending` or `recovery_class: blocked`;
  - `source-inventory.yaml`: `inspection: blocked`;
- `evidence_status: conflict` alone is intentionally **not** a blocker because conflicting evidence may already have a valid higher-authority/approved resolution;
- approved proposals, targeted inspection, omitted defaults, optional/advisory ideas, and non-material open detail are not mechanically promoted into blockers;
- `work/render-data.json` remains bound to current `work/content.md` through the narrow existing `canonical_content_sha256` field;
- generated `output/final.html` remains bound to current `work/render-data.json` through one `render-data-sha256` marker;
- Flow 4 → Flow 5 uses the existing `document.version` / `accepted_prd_version` lifecycle rather than adding another hash;
- weighted scoring, intentional bilingual display text, and bounded wrapped-grid mechanics remain protected.

Repository/CI evidence for the final narrowed Flow 2 persisted-state behavior before documentation synchronization:

```text
70139643c799d451d5a671d5768392fb19ab1e4d  initial validator guard
25104df7e15bad3ed424fd7dc7bcf50070ce29a2  initial focused regression tests
432eef641b695102d7446337a297e35136d3bc95  Production Verify includes Flow 2 state contracts
efcd194b33bce08519d6d586d6948f4bdae67949  remove ambiguous conflict-only blocker
114df1b4c6a7de1c3359091a98338820d5a1adc5  prove resolved conflict remains allowed

Repository Verify #89 — PASS
Production Verify #45 — PASS
Project Document contracts — PASS
```

These checks prove the exercised static/regression contracts. They do **not** prove current real-project recovery quality, browser appearance, or semantic completeness beyond the exact contracts implemented.

## Anti-overdevelopment decision — current interpretation

PRD-Creator does not restore a broad checksum/revision framework, generic YAML/schema registry, semantic-comparison engine, package manifest system, or deep artifact-binding architecture merely for theoretical safety.

The two existing SHA boundaries remain narrow mechanical guards:

```text
content.md → render-data.json
render-data.json → final.html
```

No SHA was added for handoff or Flow 2 persisted-state consistency.

The Flow 2 check is not a YAML validator. It scans only exact, unambiguous blocker markers already meaningful to the production state and does not infer materiality from missing/optional fields.

## Verification gates

### Repository Verify

Owns static repository/routing/navigation/syntax/dependency-pin and explicitly codified repository invariant checks.

### Production Verify

Owns the repeatable executable baseline:

```text
locked dependencies
→ Python compile
→ PRD renderer/validator + handoff + Flow 2 state contracts
→ Voice builder/validator contracts
→ fail-closed aggregate
```

A PASS does not replace project semantic review, browser visual QA, DOCX page inspection, pronunciation/performance judgment, or actual audio review.

## Known current limitations

The current revision still does not claim proof for:

- practical Flow 2 recovery quality after the latest guards on a new/current real-project run;
- browser visual fidelity of the latest renderer changes;
- hidden semantic omissions or unresolved meaning that were never persisted with an unambiguous blocker marker;
- operator mistakes that change accepted PRD meaning without advancing the existing `document.version` lifecycle;
- Flow 5 requirement completeness at the executable parser boundary;
- current Voice requirement/script/DOCX revision integrity beyond existing Voice checks;
- generated-audio quality without supplied/reviewed audio.

These limitations are not permission to add broad preventive architecture. Address only concrete bounded defects/current needs through the smallest owner.

## Current boundary

The audited PRD-side false-ready boundary for unambiguous persisted Flow 2 blockers is closed at the static/regression level. Per current user direction, do not run local/manual real-project or browser proof until explicitly allowed.
