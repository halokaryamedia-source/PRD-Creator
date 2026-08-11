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

The latest PRD correction batch was performed through repository inspection and GitHub Actions only. The changed PRD contracts therefore have **current repository/static proof**, while real-project/browser proof for those changed contracts remains deferred by user direction.

| Flow | Current evidence state | Current note |
|---|---|---|
| 1. Repository Boot & Project Memory | **current repository/static proof** | Current-state owners are aligned again in this revision; historical and current proof are explicitly separated here. |
| 2. Source Intake & Requirement Recovery | **historical real-project proof + current static contract proof** | The Clockwork Vault previously proved practical recovery, but the latest Flow 2/4 readiness guards have not been re-run as a current real-project trial. |
| 3. PRD Generation | **historical real-project proof + current static contract proof** | Earlier canonical PRD/rendering production was proven; current projection-binding, bilingual, scoring, and wrapped-grid changes are regression/CI proven only. |
| 4. PRD Validation & Handoff | **historical real-project proof + current static contract proof** | Earlier development-readiness/handoff was exercised; the latest false-green guards are current static proof only. |
| 5. Voice Requirement Extraction | **historical real-project proof** | The Clockwork Vault previously exercised real Voice scope extraction. No new current-revision Voice production proof was created by the latest PRD-only correction batch. |
| 6. Voice Script + DOCX | **historical real-project proof** | Earlier Voice ID/Type parity and DOCX generation were exercised. No new current-revision Voice project run was performed in the latest batch. |
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

## Current PRD false-green correction batch

The current PRD-side corrections now protect these concrete cases:

- Flow 4 rejects missing/ambiguous/non-ready `state/intake-state.yaml` instead of accepting downstream artifacts while Flow 2 is not explicitly ready;
- `work/render-data.json` is bound to the exact current bytes of `work/content.md` through the narrow `canonical_content_sha256` revision field, so an older projection cannot silently validate after canonical content changes;
- weighted scoring validates numeric weights and numeric percentage strings and requires a complete weighted total of 100;
- intentional EN + ID output requires explicit localized user-visible text rather than silently duplicating scalar English prose into Indonesian;
- Journey grids beyond six items and Flow grids beyond four items include bounded wrapped-row separator handling.

Repository/CI evidence for the correction sequence includes Repository Verify #68–#73 and Production Verify #28–#32 on their respective commits.

These checks prove the exercised static/regression contracts. They do **not** prove current browser appearance, current real-project recovery quality, or semantic equivalence of arbitrary prose beyond the contracts actually implemented.

## Anti-overdevelopment decision — current interpretation

The earlier anti-overdevelopment cleanup remains valid: PRD-Creator does not restore a broad checksum/revision framework, package manifest system, generic schema registry, or deep artifact-binding architecture merely for theoretical safety.

The later `canonical_content_sha256` addition is a **narrow exception justified by a concrete false-green defect** between canonical `content.md` and its derived `render-data.json`. It must not be interpreted as restoring the retired general checksum protocol.

Likewise, prior decisions not to add stale-HTML, Voice artifact, handoff, or other revision machinery remain historical decisions only until newer concrete evidence justifies revisiting a specific boundary. A later audit may supersede one such decision without invalidating the anti-overdevelopment principle itself.

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
- exact `render-data.json` → `final.html` revision binding beyond current structural/content checks;
- exact Flow 4 handoff revision binding into Flow 5;
- current Voice requirement/script/DOCX revision integrity beyond the existing Voice contracts;
- generated-audio quality without supplied/reviewed audio.

These limitations are not permission to add broad preventive architecture. Address them only through a concrete bounded defect/current need and the smallest owner that can resolve it.

## Current boundary

The current evidence owner is now reconciled: historical real-project proof is preserved, while the latest PRD hardening is reported only at the GitHub/static/CI evidence level actually obtained.

Per current user direction, do not run local/manual real-project or browser proof until explicitly allowed. The next repository-side correction should address one concrete audited false-green boundary at a time.