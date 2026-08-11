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

The latest PRD correction work was performed through repository inspection and GitHub Actions only. The changed PRD contracts therefore have **current repository/static proof**, while real-project/browser proof for those changed contracts remains deferred by user direction.

| Flow | Current evidence state | Current note |
|---|---|---|
| 1. Repository Boot & Project Memory | **current repository/static proof** | Current-state owners separate current versus historical proof. |
| 2. Source Intake & Requirement Recovery | **historical real-project proof + current static contract proof** | The Clockwork Vault previously proved practical recovery; the latest readiness guards have not been re-run as a current real-project trial. |
| 3. PRD Generation | **historical real-project proof + current static contract proof** | Earlier canonical PRD/rendering production was proven; current content→projection and projection→HTML revision bindings plus bilingual/scoring/grid corrections are regression/CI proven. |
| 4. PRD Validation & Handoff | **historical real-project proof + current static contract proof** | Earlier development-readiness/handoff was exercised; current Flow 4 now rejects stale projection and stale HTML revision boundaries mechanically. |
| 5. Voice Requirement Extraction | **historical real-project proof** | The Clockwork Vault previously exercised real Voice scope extraction. No new current-revision Voice production proof was created by the current PRD correction batch. |
| 6. Voice Script + DOCX | **historical real-project proof** | Earlier Voice ID/Type parity and DOCX generation were exercised. No new current-revision Voice project run was performed in the current batch. |
| 7. Voice Validation & Delivery | **historical real-project proof** | Earlier real DOCX visual QA found/fixed the blank-page defect. Audio evidence for that proof remained `not_provided`; no new current-revision Voice visual/audio proof was performed. |

## Historical real-project proof

The Clockwork Vault remains valid historical evidence that the end-to-end Flow 1–7 production model has been exercised on a real project.

That proof must be read as:

```text
real-project feasibility was demonstrated on the revision exercised at that time
```

not as:

```text
all later repository changes are automatically CURRENT-PROJECT VERIFIED
```

Do not erase this evidence when newer static-only changes are introduced. Preserve it as historical proof and state the newer proof boundary explicitly.

## Current PRD false-green correction sequence

Current PRD-side contracts now protect these concrete cases:

- Flow 4 rejects missing/ambiguous/non-ready `state/intake-state.yaml` instead of accepting downstream artifacts while Flow 2 is not explicitly ready;
- `work/render-data.json` is bound to the exact current bytes of `work/content.md` through the narrow `canonical_content_sha256` revision field, so an older projection cannot silently validate after canonical content changes;
- generated `output/final.html` carries one `render-data-sha256` marker derived from the exact current bytes of `work/render-data.json`; Flow 4 rejects missing/duplicate/invalid/mismatched markers so an older HTML artifact cannot silently validate against a newer projection with the same page structure;
- weighted scoring validates numeric weights and numeric percentage strings and requires a complete weighted total of 100;
- intentional EN + ID output requires explicit localized user-visible text rather than silently duplicating scalar English prose into Indonesian;
- Journey grids beyond six items and Flow grids beyond four items include bounded wrapped-row separator handling.

Repository/CI evidence for the latest projection→HTML correction:

```text
Commit: 8d177cea8e2119931c1a068ff6e924e47f60b490
Repository Verify #76 — PASS
Production Verify #33 — PASS
Project Document contracts — PASS
```

These checks prove the exercised static/regression contracts. They do **not** prove current browser appearance, current real-project recovery quality, or semantic equivalence of arbitrary canonical prose beyond the contracts actually implemented.

## Anti-overdevelopment decision — current interpretation

The earlier anti-overdevelopment cleanup remains valid: PRD-Creator does not restore a broad checksum/revision framework, package manifest system, generic schema registry, or deep artifact-binding architecture merely for theoretical safety.

The current SHA fields/markers are two **narrow boundary guards justified by concrete false-green defects**:

```text
content.md → render-data.json
render-data.json → final.html
```

They must not be interpreted as a generic artifact manifest/checksum framework. Additional revision machinery requires its own concrete defect/current need.

## Verification gates

### Repository Verify

Owns static repository/routing/navigation/syntax/dependency-pin and explicitly codified repository invariant checks.

A PASS proves only the checks implemented by that gate. It does not prove that every current-state Markdown statement is semantically synchronized unless that relationship is explicitly checked.

### Production Verify

Owns the repeatable executable baseline:

```text
locked dependencies
→ Python compile
→ PRD renderer/validator contracts
→ Voice builder/validator contracts
→ fail-closed aggregate
```

A PASS proves those current regression contracts. It does not replace project semantic review, browser visual QA, DOCX page inspection, pronunciation/performance judgment, or actual audio review.

## Known current limitations

The current revision still does not claim proof for:

- practical Flow 2 recovery quality after the latest PRD guard changes on a new/current real-project run;
- browser visual fidelity of the latest renderer changes;
- whether persisted Flow 2 requirement/source state can explicitly contradict a manually declared `ready_for_prd` state without being detected mechanically;
- exact Flow 4 accepted handoff revision binding into Flow 5;
- Flow 5 requirement completeness at the executable parser boundary;
- current Voice requirement/script/DOCX revision integrity beyond the existing Voice ID/Type/content checks;
- generated-audio quality without supplied/reviewed audio.

These limitations are not permission to add broad preventive architecture. Address them only through a concrete bounded defect/current need and the smallest owner that can resolve it.

## Current boundary

The Flow 3 → Flow 4 stale-HTML false-green is closed at the static/regression level. Per current user direction, do not run local/manual real-project or browser proof until explicitly allowed.

The next repository-side correction should address the concrete **Flow 4 → Flow 5 handoff revision boundary** identified by audit: a stale `handoff_ready` state must not authorize Voice extraction for a newer PRD revision.
