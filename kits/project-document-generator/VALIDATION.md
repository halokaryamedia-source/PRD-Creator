# PRD Validation & Team Handoff

`CONTENT-CONTRACT.md` owns gameplay PRD semantics. This file owns only how Flow 4 proves the current revision is ready.

## Flow 4 sequence

```text
current canonical PRD revision
→ mechanical validation once
→ one integrated semantic review
→ targeted desktop visual sanity when required/available
→ fix first wrong owner
→ development_ready | handoff_ready
```

Rendering success is necessary but not sufficient.

## 1. Mechanical validation

Run:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation checks deterministic state only, including:

- Flow 2 readiness and explicit blockers;
- required files and unresolved placeholders;
- revision bindings;
- collection/ID/page/navigation consistency;
- scoring numeric consistency;
- generated generic component composition.

The renderer already rejects deterministic missing mandatory shell data before HTML output.

Mechanical PASS does **not** prove source fidelity, scoring interpretation, narrative quality, role completeness, Humanize quality, acceptance quality, or visual quality.

Do not replace semantic review with word counts, row counts, semantic similarity, DOM snapshots, pixel scoring, or generic schemas.

## 2. One integrated semantic review

Read only relevant authoritative/approved evidence plus the affected canonical PRD scope.

Assess the document once through these lenses:

| Lens | Ready when... |
|---|---|
| New Reader | chronological experience, objective/result, important feedback/recovery, and transition are understandable without reopening source |
| Level Designer | build-owned areas/objects/routes/spatial/readability/function requirements are sufficient without rediscovering material source rules |
| Developer | activation/state/progression/result/data/interruption/reset/handoff behavior is sufficient without hidden product decisions |
| Acceptance | package criteria are observable and prove material entry/completion/result/recovery/handoff behavior |
| Project Consistency | terminology, topology, timing, quantities, scoring/result, global/local rules, reset, and handoff agree across the revision |

Use `CONTENT-CONTRACT.md` directly for required content functions. Do not maintain another complete content checklist here.

A **Major** finding exists when a production role must reopen source to recover a material rule, a mandatory content function no longer serves its reader, or package Acceptance & Verification fails to prove a material behavior it depends on.

Critical/Major findings block readiness.

### Return upstream when needed

Return a finding to Flow 2 when it requires a new product/design decision, authority reconciliation, scoring interpretation, or another unresolved material choice.

Flow 4 may improve wording only when the approved underlying meaning is already clear.

### Writing usability

Flag prose when it materially reduces production usability, especially:

- task-summary text used where chronological Gameplay Flow is required;
- comma-stacked/database-like prose;
- vague statements hiding behavior;
- unnecessary promotional/filler wording;
- terminology drift;
- missing cause → response → consequence where those relationships are already known.

Do not create a separate Humanize approval stage.

## 3. Desktop visual sanity

Default visual proof is desktop-only unless the task is specifically mobile/responsive.

A representative smoke normally inspects only:

```text
Overview
+ one Gameplay Flow page
+ one Level Design page
+ one dense Developer page including Acceptance & Verification
```

Check obvious composition, representative navigation/tabs, table readability/overflow, scoring/result placement, acceptance placement, glossary affordance when relevant, and broken structure.

Do not routinely retest every navigation link, Terms disclosure, theme, localStorage behavior, or mobile viewport.

If browser/page proof is unavailable, record:

```text
Visual sanity: NOT PROVEN
```

Never convert static source inspection into a visual PASS claim.

## 4. Acceptance record

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

Package-level `Acceptance & Verification` is part of the PRD. `work/acceptance.md` records whether the document revision passed Flow 4; these are different concepts.

## 5. Handoff entry

Before Flow 5:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

The handoff validator confirms the current accepted PRD version, artifact references, acceptance status, and `handoff_ready` state.

`Visual sanity: NOT PROVEN` remains allowed when browser proof was unavailable; it is not a visual PASS claim.

Do not add another handoff checksum, artifact manifest, or approval framework.

## Bounded revision

```text
update affected truth/content
→ regenerate affected projection + HTML
→ one mechanical check
→ targeted semantic/desktop review of invalidated scope
→ stop
```

Do not replay unchanged intake, unrelated packages, mobile QA, or Voice tests merely for ceremony.
