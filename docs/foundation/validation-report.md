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

The audited PRD-side Flow 1–4 correction set is complete at the **repository/static/regression** level. The latest changes were not re-executed on a current real project or browser, so those proof classes remain intentionally separate.

| Flow | Current evidence state | Current note |
|---|---|---|
| 1. Repository Boot & Project Memory | **current repository/static proof** | Current-state owners separate current versus historical proof; CI bookkeeping no longer requires chasing the newest run number after every documentation-only sync. |
| 2. Source Intake & Requirement Recovery | **historical real-project proof + current static contract proof** | `ready_for_prd` now requires persisted source/requirement evidence owners, rejects unambiguous current blockers, and does not let an explicitly superseded source's old blocked inspection invalidate current readiness. |
| 3. PRD Generation | **historical real-project proof + current static contract proof** | Existing stale-derivation guards remain; scoring display normalization and deterministic required Golden content presence are regression proven. |
| 4. PRD Validation & Handoff | **historical real-project proof + current static contract proof** | Handoff now requires current version/path consistency and a compact acceptance record that actually authorizes `handoff_ready`. |
| 5. Voice Requirement Extraction | **historical real-project proof** | The Clockwork Vault previously exercised real Voice scope extraction. No current-revision Voice hardening is claimed by this PRD-side batch. |
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

## Current PRD-side correction set

The current PRD contracts now protect these concrete cases:

- `state/intake-state.yaml` must explicitly report `ready_for_prd`;
- `state/source-inventory.yaml` and `state/requirement-register.yaml` must both exist and contain at least one stable `SRC-###` / `REQ-###` entry before `ready_for_prd` can pass;
- current requirement blockers `approval_status: pending` and `recovery_class: blocked` fail readiness;
- current source `inspection: blocked` fails readiness, while an entry explicitly marked `status: superseded` does not block merely because that old source was unreadable/uninspected;
- `evidence_status: conflict` alone remains nonblocking because a higher-authority approved resolution may already exist;
- deterministic Golden slots that the gameplay PRD family already defines as mandatory cannot disappear silently: narrative presence, Gameplay Context/Main Objective/Result/player flow, Level Design overview/build requirement, Global Development overview/requirement, and Developer overview are mechanically checked for presence;
- numeric weights and percentage strings render with one `%`; unweighted scoring components do not receive invented percentage markers or equal weights;
- `work/render-data.json` remains bound to current `work/content.md` through the existing narrow `canonical_content_sha256` stale-projection guard;
- generated `output/final.html` remains bound to current `work/render-data.json` through the existing `render-data-sha256` stale-render guard;
- Flow 4 → Flow 5 continues to use existing `document.version` / `accepted_prd_version`, not another hash;
- `validate_handoff.py` now rejects a `handoff_ready` state when `work/acceptance.md` says `needs_revision`, mechanical/review failure, explicit visual failure, or non-zero Critical/Major blockers;
- `Visual sanity: NOT PROVEN` remains valid when no actual browser/page proof exists and is never promoted to visual PASS;
- prior weighted-scoring, intentional bilingual display-text, and bounded wrapped-grid protections remain active.

## Stable repository proof anchor

The executable correction set is anchored by:

```text
d37fa3655e62548aeec0be153b42bca6077cb9ad
```

GitHub Actions on that implementation state recorded:

```text
Repository Verify #96 — PASS
Production Verify #52 — PASS
Project Document contracts — PASS
```

The aligned kit validation procedure at:

```text
ebf1e784850b5f2eb3b6229494e7dea6fa21feb3
```

also recorded:

```text
Repository Verify #99 — PASS
Production Verify #53 — PASS
```

These are **proof anchors**, not a requirement that this report be edited whenever a later documentation-only commit creates a newer run number. Live GitHub Actions remains the authoritative execution history for newer commits. Update this report when the evidence class, protected claim, or known limitation materially changes—not merely to chase CI numbering.

## Anti-overdevelopment decision — final PRD-side interpretation

PRD-Creator does not add a broad checksum/revision framework, generic YAML/schema registry, semantic-comparison engine, package manifest system, DOM/pixel scoring, or deep artifact-binding architecture merely for theoretical safety.

The two existing SHA boundaries remain narrow mechanical stale-derivation guards:

```text
content.md → render-data.json
render-data.json → final.html
```

The first does **not** prove semantic equivalence between canonical content and projection; semantic agreement remains part of Flow 4 review. The second is appropriate for the deterministic renderer boundary. No SHA was added for Flow 2 state, handoff, acceptance, or Voice.

Do not extend the hash chain without a concrete failing current use case.

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
- semantic equivalence of `content.md` and `render-data.json` beyond revision binding + human/semantic review;
- operator mistakes that change accepted PRD meaning without advancing the existing `document.version` lifecycle;
- Flow 5 requirement completeness at the executable parser boundary;
- current Voice requirement/script/DOCX revision integrity beyond existing Voice checks;
- generated-audio quality without supplied/reviewed audio.

These limitations are not permission to add preventive machinery. The next useful evidence for PRD Flow 2–4 is a representative current-project production run, not another generic guard.

## Current boundary

All **concrete PRD-side Flow 1–4 defects identified in the latest audit** are closed at the static/regression level. Further PRD guard work should be driven by a failing representative current-project run or another concrete defect, not by hypothetical completeness.
