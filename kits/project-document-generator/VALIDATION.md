# PRD Validation & Team Handoff

`CONTENT-CONTRACT.md` is the single semantic owner for the gameplay PRD family. This file defines only how Flow 4 proves that the current revision satisfies it.

## Flow 4 sequence

```text
current canonical PRD revision
→ mechanical validation once
→ one integrated semantic review against CONTENT-CONTRACT.md
→ targeted desktop visual sanity when available
→ fix the first wrong owner
→ development_ready / handoff_ready
```

Rendering success is necessary but not sufficient.

## Mechanical validation

Run:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation owns deterministic checks only: Flow 2 readiness/evidence, explicit blockers, stale revision bindings, required files/placeholders, valid collections/IDs, scoring numeric consistency, generated page order/IDs, duplicate IDs, navigation/browser title, and Golden composition markers.

The renderer rejects deterministic missing mandatory shell data before HTML generation, including current Document Control inputs and non-empty package Acceptance & Verification content.

Mechanical PASS does **not** prove source fidelity, correct scoring interpretation, narrative quality, role completeness, quality of acceptance criteria, Humanize quality, or visual quality.

Do not add word-count, row-count, semantic similarity, DOM snapshot, pixel scoring, or generic-schema machinery as a substitute for semantic review.

## One integrated semantic review

Read only relevant authoritative/approved evidence plus the affected canonical PRD scope.

### New Reader / Player Context

Can a new team member understand the full chronological Gameplay Flow, context, objective/result, important cues/setbacks/recovery, and forward transition without reopening source?

The shorter **Objective Sequence** on Gameplay Overview is for scanability; it should not be mistaken for or duplicate the full narrative.

### Level Designer

Can Level Design build the package from its page plus clearly referenced shared rules without reopening source for a material build rule?

Check that `Area / Spatial Constraint`, build/visual requirements, gameplay function, and Critical Constraints & Notes communicate the actual project truth without invented dimensions.

### Developer

Can Developer implement the package from its page plus clearly referenced shared rules without reopening source for material runtime behavior?

This includes Scoring / Result, `Expected System Result`, interruption/recovery/reset, and the distinction between internal result, player-facing display, and telemetry/export.

### Acceptance & Verification

Does the package close with concise **observable conditions** that actually prove its material behavior?

Acceptance is inadequate when it only says `works correctly`, restates a requirement without an observable result, or ignores a material entry/completion/result/recovery/handoff behavior needed by the package.

Do not require a QA test-case appendix. This is package definition of done, not a second testing framework.

### Project Consistency

Do terminology, topology, timing, quantities, scoring/result, global/local rules, interruption/reset, acceptance statements, and handoff remain consistent across the revision?

When a project has an aggregate result, confirm that its Final Result Contract lives coherently under **Data, Recovery & Reset** rather than drifting across packages.

## Golden mandatory-contract check

Use `CONTENT-CONTRACT.md` directly. Do not maintain another full checklist here.

The reviewer confirms that mandatory functions perform their intended production job with current-project truth, explicit negative/N/A states are understandable, role-owned material meaning is on the correct surface, and prose remains readable without changing technical facts.

A **Major** finding exists when a production role must reopen source to recover a material rule, a mandatory Golden function has been reduced until it no longer works for its reader, or Acceptance & Verification fails to prove a material behavior the package depends on.

Do not compare word or row counts with Golden.

## Flow 2 fallback

Return a finding to Flow 2 when it requires a new product/design decision, authority reconciliation, scoring interpretation, acceptance meaning that depends on an unresolved behavior, or another material choice.

Flow 4 may improve wording only when approved meaning is already clear. It may not invent values, mechanics, formulas, workarounds, or acceptance behavior merely to make the PRD pass.

## Humanized writing review

Flag prose when it materially reduces usability, especially task-summary full Gameplay Flow, comma-stacked database prose, generic statements hiding behavior, vague/promotional filler, terminology drift, or dense prose that removes cause/effect/context.

Do not create a separate Humanize approval round.

## Desktop visual sanity by default

Default PRD visual proof is desktop-only unless mobile/responsive behavior is explicitly requested or a current defect is mobile-specific.

A representative visual smoke normally inspects only:

```text
Overview
+ one Gameplay Flow page
+ one Level Design page
+ one dense Developer page including Acceptance & Verification
```

Check obvious composition, representative navigation/tabs, table readability/overflow, scoring/result placement, acceptance placement, and broken visual structure.

Do not routinely retest every navigation link, every Terms disclosure, themes, localStorage, or mobile viewport.

If browser/page proof is unavailable, record `Visual sanity: NOT PROVEN` rather than claiming PASS.

## Acceptance record

Keep `work/acceptance.md` compact:

```text
# PRD Acceptance
Status: needs_revision | development_ready | handoff_ready
Mechanical: PASS | FAIL
Visual sanity: PASS | FAIL | NOT PROVEN
New Reader: PASS | FAIL
Level Designer: PASS | FAIL
Developer: PASS | FAIL
Project Consistency: PASS | FAIL
Findings: <only when findings exist>
Critical: N
Major: N
```

Package-level Acceptance & Verification lives in the PRD. `work/acceptance.md` records whether the document itself passed Flow 4; do not merge these two meanings.

Critical/Major findings block readiness.

## Handoff entry

Before Flow 5:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

The handoff validator confirms current status/version/artifact references and that compact document acceptance authorizes `handoff_ready`.

`Visual sanity: NOT PROVEN` remains allowed when actual browser proof was unavailable; it is not a visual PASS claim.

Do not add another handoff checksum, artifact manifest, or approval framework.

## Revision economy

For an approved bounded change:

```text
update affected requirement/content
→ regenerate affected projection + HTML
→ one mechanical check
→ one targeted semantic/desktop review of invalidated scope
→ stop
```

Do not replay unchanged source intake, unrelated packages, mobile QA, or Voice tests merely for ceremony.
