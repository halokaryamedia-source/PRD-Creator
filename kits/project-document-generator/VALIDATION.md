# PRD Validation & Team Handoff

`CONTENT-CONTRACT.md` owns PRD meaning and Golden prototype fidelity. This file owns only how Flow 4 proves the current revision is ready.

## Golden proof model

Golden fidelity is proved in two directions, because either direction alone can miss a real failure:

```text
1. Reference → Fill Map
   Read the exact approved Golden first and verify that the fixed prototype contract
   actually matches what the Sample demonstrates.

2. Project Authority → Filled Golden
   Verify that current project meaning is placed into those same slots without
   omission, invention, relocation, or unapproved presentation changes.
```

The reverse/reference check owns **prototype truth**, not project facts. It may lock visible page family, labels, card/sequence cardinality, table columns, component order, glossary placement, and the semantic job of each slot. It must not turn AFTERSHOCK-specific story, object names, numeric values, package count, arena count, scoring values, or other project facts into generic requirements.

The forward/project check then asks whether the generated PRD fills the mapped prototype with the complete current-project meaning. A page can therefore fail even when its shell matches perfectly, and a project can also fail if the contract itself drifted away from what the approved Golden actually contains.

`tests/test_prd_golden_reference.py` is the focused static proof for the first direction. Normal renderer/validator contract tests and Flow 4 review cover the second direction. Do not add a generic schema, similarity score, word-count gate, or another reference model for the same job.

## Sequence

```text
current PRD revision
→ one mechanical validation
→ one integrated semantic + content-purity + material-conservation + Golden-fidelity review
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

Mechanical validation checks deterministic state such as Flow 2 readiness, required files, revision bindings, IDs/page order/navigation, scoring arithmetic, required Golden prototype markers, and a narrow set of observed project/document-process leakage patterns.

Mechanical PASS does not prove source fidelity, material-detail conservation, general writing quality, or visual readability.

The content-purity mechanical check is intentionally narrow. It blocks concrete observed leakage such as `Golden HTML`, `render-data.json`, `final.html`, visible `Gameplay Overview page / Level Design page / Developer page` narration, `three-page contract`, generic `Global Rule N` titles, and plain note strings that would render as generic `Important Note N` cards. It is **not** a prose score and must not grow into a broad keyword blacklist.

## 2. Integrated review

Review once through these lenses:

| Lens | Ready when... |
|---|---|
| New Reader | the gameplay journey, objective, result, setback/recovery and transition are clear without reopening source |
| Level Designer | build-owned requirements are sufficient and presented in the Golden Level Design prototype |
| Developer | runtime/scoring/reset/handoff requirements are sufficient and presented in the Golden Developer prototype |
| Content Purity | visible project copy explains the project/game, not PRD-Creator, Golden/template/page structure, approval workflow, or document-production mechanics |
| Material Conservation | every independent material rule recovered in Flow 2 still has an owned readable representation; structured rules were not flattened into summaries |
| Acceptance | package criteria in project state are observable and sufficient for Flow 4 review |
| Project Consistency | terminology, timing, scoring, reset and package handoff agree across the revision |
| Golden Fidelity | the reverse-derived fill map still matches the exact Golden, and each generated page uses the matching visible structure, labels, component order, reading pattern and comparable information density |

A **Major** finding exists when a production role must reopen source for a material rule, independent source rules were merged/omitted during Flow 3, internal generator/document process appears as project content, a summary surface becomes materially harder to scan because it carries the wrong role's detail, a new unapproved visible component replaces Golden composition, or prose becomes materially harder to scan than the Golden reference.

Acceptance criteria remain required project/review meaning, but they are **not a new visible Developer-page panel**. They are recorded in Flow 4 acceptance state.

Return to Flow 2 only for unresolved product/design decisions or authority conflicts. Flow 4 may improve wording, placement, decomposition, and terminology when the approved meaning is already clear.

## 3. Content-purity / AI-slop review

Before judging visual polish, read the visible copy as if the recipient has never seen PRD-Creator.

### Fail project/process leakage

Visible project content must not explain:

- Golden HTML / Golden Sample / reference mechanics;
- page or template structure;
- `content.md`, `render-data.json`, `final.html`, renderer or validator behavior;
- “one Gameplay Overview / one Level Design / one Developer page”;
- “three-page contract”, document order, content lock, or internal approval workflow;
- where the generator chose to store a rule merely because of document architecture.

Those belong to repository policy, not the project PRD.

### Flag common AI-slop behavior

- generic titles such as `Global Rule 1`, `Important Note 2`, or other numbering that says nothing about the rule;
- “completeness padding”: filling a Golden slot with document-process prose because project meaning is already covered elsewhere;
- mixed abstraction: player-facing Context/Objective/Result combined with telemetry, save/retry, scoring formula, or reset implementation;
- repeated restatement of the same fact in Overview facts, journey cards, context cards, and notes without adding a different role-owned meaning;
- role-label narration such as `Gameplay Overview: ... Level Design: ... Developer: ...` inside the document itself;
- terminology drift (`student` vs `player`, `package` vs `objective`) when no real technical distinction exists;
- multi-rule requirements stored as one dense prose blob when the independent actions can be scanned as bullets.

The correction rule is:

```text
wrong owner / meta copy
→ remove or relocate

long summary with technical detail
→ short summary
+ keep complete technical detail in the owning Developer/Level requirement

multi-rule dense cell
→ same material rules as separate bullets

generic title
→ name the actual invariant
```

Do not delete material meaning to make the page look cleaner.

## 4. Material-conservation review

Do not use word count or raw row count as a quality score. Instead, compare material meaning at the affected authority boundary.

For each changed or regenerated package, sample the dense source-owned surfaces and ask:

```text
What independent rules existed before Flow 3?
Where is each rule represented now?
Did any condition/value/exception/recovery/result disappear?
Did a multi-rule list/table cell become one vague summary?
Could Level Design or Development implement without reopening source?
```

For a representative regeneration of the same project used to establish the Golden Sample, perform direct page-family comparison against the approved reference as well as current project authority. A matching page shell with materially thinner content is **FAIL**, not Golden Fidelity PASS.

Do not mark `Golden Fidelity: PASS` solely because the page count, headings, or CSS classes match.

## 5. Writing usability

Flag:

- long paragraphs inside narrow summary cards;
- repeated explanation of the same rule;
- meta-language about the generator/document;
- generic numbered titles that read like AI placeholders;
- task/database-like prose where Golden uses normal player-story paragraphs;
- implementation detail placed in Gameplay Context/Main Objective/Result instead of the correct table;
- detailed scoring formula in Gameplay Overview when high-level scoring inputs are sufficient there;
- one requirement cell containing several actionable sentences that should be separate bullets;
- inconsistent visible terminology for the same project concept;
- vague wording that leaves the next material question unanswered;
- aggressive shortening that removes distinct constraints instead of only improving wording.

Humanize means **clearer ownership, clearer labels, shorter summaries, and decomposed detail**, not fewer material facts.

There is no universal word/character limit. Judge whether each Golden slot answers its single intended question and whether dense requirements remain easy to scan.

## 6. Validation economy

Validation should prove the current revision without turning every content change into a full regression campaign.

### Normal initial production

For a content-only project generation where the Golden/template/renderer foundation is unchanged:

```text
narrow mechanical/content-purity validator
+ one integrated semantic/material-conservation review
+ representative desktop visual sanity
```

Perform the Content Purity + Humanize pass **before the planned render** so obvious copy/ownership defects are corrected before HTML generation. The validator then catches concrete regressions; it should not be used as an interactive writing loop.

The mechanical validator may inspect the full generated structure. The model should not semantically reread the entire generated HTML merely because the file is large; review canonical/render-data meaning and the relevant rendered page families instead.

### Representative visual set

Normally inspect:

```text
Overview
+ one Gameplay Flow page
+ one Gameplay Overview page
+ one Level Design page
+ one dense Developer page
```

Choose the densest or highest-risk package where useful. If a glossary-heavy or special scoring page is materially different, include that page instead of blindly adding more pages.

### Escalate to full visual sweep only when justified

Inspect every page / broader browser behavior only when at least one is true:

- Golden template, CSS, JS/runtime behavior, or page-composition renderer changed;
- a targeted finding suggests a global layout/overflow defect;
- a new page family/component behavior was explicitly approved;
- the user explicitly requests full visual proof.

Do not run full every-page/mobile/theme/localStorage/Voice checks merely because project content changed.

### Bounded revision

For an approved bounded change:

```text
affected truth/content
→ purity/humanize affected scope
→ affected render projection
→ one full-file rerender
→ one mechanical check
→ semantic/material/Golden review only where invalidated
→ visual check only for affected/high-risk page(s)
```

A full-file HTML rewrite does **not** imply a full-project reasoning/review restart.

## 7. Targeted desktop visual sanity

Default visual proof is desktop-only unless a mobile defect is specifically under review.

Compare representative pages directly against `template/golden-sample.html`, the canonical approved Golden artifact. Check:

- same visible section order and labels;
- readable summary-card copy;
- concise Overview fact values that can be scanned before the detailed journey;
- semantic note titles rather than numbered filler labels;
- 4-card Development/Design Flow where Golden uses it;
- table width/wrapping and information density;
- independent long rules presented as readable list items where appropriate;
- scoring/reset placement inside Developer requirements;
- Terms Used only on Golden-approved surfaces;
- glossary affordance when relevant;
- no obvious overflow/broken structure;
- no suspiciously thin page caused by omitted material rules.

Do not routinely retest mobile, every link, theme, localStorage, or unrelated Voice behavior.

If browser proof is unavailable, record `Visual sanity: NOT PROVEN`. Static HTML inspection is never a visual PASS.

## 8. Acceptance record

Keep `work/acceptance.md` compact:

```text
# PRD Acceptance
Status: needs_revision | development_ready | handoff_ready
Mechanical: PASS | FAIL
Visual sanity: PASS | FAIL | NOT PROVEN
New Reader: PASS | FAIL
Level Designer: PASS | FAIL
Developer: PASS | FAIL
Material Conservation: PASS | FAIL
Acceptance: PASS | FAIL
Project Consistency: PASS | FAIL
Golden Fidelity: PASS | FAIL
Findings: <only when findings exist>
Critical: N
Major: N
```

Content Purity is part of Mechanical + integrated review readiness; do not add another acceptance field solely for ceremony.

`Material Conservation: PASS` is required for a new handoff. Older acceptance records without the field remain historical evidence only and must not be reused as proof for a regenerated revision.

## 9. Handoff

Before Flow 5:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

Handoff must refer to the current accepted document version. Normal review corrections do not bump `document.version`.

## Bounded revision

```text
update affected truth/content
→ purity/humanize affected scope
→ verify material conservation in affected scope
→ regenerate projection + full HTML once
→ one mechanical check
→ targeted semantic/Golden/desktop review of invalidated scope
→ stop
```

Do not replay unchanged intake, mobile QA, every-page visual QA, or Voice tests for ceremony.
