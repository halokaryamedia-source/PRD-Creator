# PRD Validation & Team Handoff

`CONTENT-CONTRACT.md` owns PRD meaning and Golden prototype fidelity. This file owns only how Flow 4 proves the current revision is ready.

## Sequence

```text
current PRD revision
→ one mechanical validation
→ one integrated semantic + Golden-fidelity review
→ targeted desktop visual sanity when needed
→ fix first wrong owner
→ development_ready | handoff_ready
```

## 1. Mechanical validation

Run:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation checks deterministic state such as Flow 2 readiness, required files, revision bindings, IDs/page order/navigation, scoring arithmetic, and required Golden prototype markers.

Mechanical PASS does not prove source fidelity, writing quality, or visual readability.

## 2. Integrated review

Review once through these lenses:

| Lens | Ready when... |
|---|---|
| New Reader | the gameplay journey, objective, result, setback/recovery and transition are clear without reopening source |
| Level Designer | build-owned requirements are sufficient and presented in the Golden Level Design prototype |
| Developer | runtime/scoring/reset/handoff requirements are sufficient and presented in the Golden Developer prototype |
| Acceptance | package criteria in project state are observable and sufficient for Flow 4 review |
| Project Consistency | terminology, timing, scoring, reset and package handoff agree across the revision |
| Golden Fidelity | each page uses the matching Golden visible structure, labels, component order and information density |

A **Major** finding exists when a production role must reopen source for a material rule, a new unapproved visible component replaces Golden composition, or prose becomes materially harder to scan than the Golden reference.

Acceptance criteria remain required project/review meaning, but they are **not a new visible Developer-page panel**. They are recorded in Flow 4 acceptance state.

Return to Flow 2 only for unresolved product/design decisions or authority conflicts. Flow 4 may improve wording when the approved meaning is already clear.

## 3. Writing usability

Flag:

- long paragraphs inside narrow summary cards;
- repeated explanation of the same rule;
- meta-language about the generator/document;
- task/database-like prose where Golden uses normal player-story paragraphs;
- implementation detail placed in Gameplay Context/Main Objective/Result instead of the correct table;
- vague wording that leaves the next material question unanswered.

Humanize means **clearer and shorter**, not more prose.

## 4. Targeted desktop visual sanity

Default visual proof is desktop-only unless a mobile defect is specifically under review.

Normally inspect only:

```text
Overview
+ one Gameplay Flow page
+ one Gameplay Overview page
+ one Level Design page
+ one dense Developer page
```

Compare them directly against the corresponding Golden page prototype. Check:

- same visible section order and labels;
- readable summary-card copy;
- 4-card Development/Design Flow where Golden uses it;
- table width/wrapping and information density;
- scoring/reset placement inside Developer requirements;
- Terms Used only on Golden-approved surfaces;
- glossary affordance when relevant;
- no obvious overflow/broken structure.

Do not routinely retest mobile, every link, theme, localStorage, or unrelated Voice behavior.

If browser proof is unavailable, record `Visual sanity: NOT PROVEN`. Static HTML inspection is never a visual PASS.

## 5. Acceptance record

Keep `work/acceptance.md` compact:

```text
# PRD Acceptance
Status: needs_revision | development_ready | handoff_ready
Mechanical: PASS | FAIL
Visual sanity: PASS | FAIL | NOT PROVEN
New Reader: PASS | FAIL
Level Designer: PASS | FAIL
Developer: PASS | FAIL
Acceptance: PASS | FAIL
Project Consistency: PASS | FAIL
Golden Fidelity: PASS | FAIL
Findings: <only when findings exist>
Critical: N
Major: N
```

## 6. Handoff

Before Flow 5:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

Handoff must refer to the current accepted document version. Normal review corrections do not bump `document.version`.

## Bounded revision

```text
update affected truth/content
→ regenerate projection + HTML
→ one mechanical check
→ targeted semantic/Golden/desktop review
→ stop
```

Do not replay unchanged intake, mobile QA, or Voice tests for ceremony.
