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

Mechanical validation owns only deterministic checks such as:

- Flow 2 readiness and persisted evidence presence;
- explicit current blocker contradictions;
- current content/projection and projection/HTML revision bindings;
- required files/placeholders;
- valid render-data collections/IDs;
- scoring numeric consistency;
- page IDs/order;
- duplicate IDs;
- navigation/browser title;
- Golden composition markers.

The renderer itself rejects missing deterministic mandatory Golden shell data before HTML generation.

Mechanical PASS does **not** prove:

- source fidelity;
- correct scoring interpretation;
- narrative quality;
- role completeness;
- Humanize quality;
- visual quality.

Do not add word-count gates, row-count gates, semantic hashing/similarity, DOM snapshots, pixel scoring, or a generic schema to imitate semantic review.

## One integrated semantic review

Read only the relevant authoritative/approved evidence plus the affected canonical PRD scope.

Use these lenses in one pass:

### New Reader / Player Context

Can a new team member understand the chronological player journey, context, objective/result, important cues/setbacks/recovery, and forward transition without reopening the original source?

### Level Designer

Can Level Design build the package from the Level Design page plus clearly referenced shared rules without reopening original source for a material build rule?

### Developer

Can Developer implement the package from the Developer page plus clearly referenced shared rules without reopening original source for material runtime behavior?

This includes the package's Scoring / Result contract and the distinction between:

```text
internal score/result
player-facing display
telemetry/export
```

### Project Consistency

Do terminology, topology, timing, quantities, scoring/result, global/local rules, interruption/reset, and handoff remain consistent across the current revision?

## Golden mandatory-contract check

Use `CONTENT-CONTRACT.md` directly.

The semantic reviewer checks that:

- all mandatory Golden functions are present;
- explicit negative and Not Applicable states are understandable rather than silently missing;
- The Journey Begins + one Gameplay Flow page per package form a coherent player journey;
- all four Global Development functions perform their intended jobs;
- every package has Gameplay Overview, Level Design, and Developer depth appropriate to current project evidence;
- every package explicitly communicates Objective Score or `No Objective Score`;
- material source meaning is represented on the surface used by the role that needs it;
- prose is readable production language without changing technical truth.

A **Major** finding exists when a production role must reopen original source to recover a material rule that belongs in the PRD, or when a mandatory Golden function has been reduced until it no longer performs its production role.

Do not compare word count or row count to Golden. A simpler project may legitimately be shorter. Missing material meaning is the failure, not shortness itself.

## Flow 2 fallback

Return a finding to Flow 2 when it requires a new product/design decision, authority reconciliation, scoring interpretation, or another material unresolved choice.

Flow 4 may improve wording only when approved meaning is already clear. It may not invent values, mechanics, formulas, workarounds, or project decisions merely to make the document pass.

## Humanized writing review

Flag prose when it materially reduces usability, especially:

- task-summary Gameplay Flow instead of player journey;
- comma-stacked database-like prose;
- generic statements that hide actual behavior;
- vague filler or promotional language;
- terminology drift;
- dense prose that removes cause/effect/context.

Do not create a separate Humanize approval round. Review writing inside the same semantic pass.

## Desktop visual sanity by default

Default PRD visual proof is desktop-only unless mobile/responsive behavior is explicitly requested or a current defect is mobile-specific.

A representative visual smoke normally inspects only:

```text
Overview
+ one Gameplay Flow page
+ one Level Design page
+ one dense Developer page
```

Check obvious layout/composition, navigation to the representative package, tabs, table readability/overflow, scoring/result placement, and broken visual structure.

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

Critical/Major block readiness.

## Handoff entry

Before Flow 5:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

The handoff validator confirms current status/version/artifact references and that the compact acceptance record actually authorizes `handoff_ready`.

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
