# PRD Validation & Team Handoff

Flow 4 decides whether the generated Golden Sample PRD is usable by the production team. Rendering success is necessary but not sufficient.

```text
current PRD + Golden-rendered HTML
→ mechanical check
→ one integrated semantic + visual review
→ fix only real findings
→ development_ready
→ concise handoff under the current repository sequence
```

Do not turn review lenses or visual sanity into separate approval ceremonies.

## Status model

`state/handoff-state.yaml` uses one current status:

- `pending_review`;
- `needs_revision`;
- `development_ready`;
- `handoff_ready`;
- `blocked`.

`handoff_ready` means documentation is ready for the current production handoff boundary. It does not mean client sign-off, implementation completion, QA completion, or release approval.

## Required inputs

Audit the same current revision of:

- `state/requirement-register.yaml`;
- `work/content.md`;
- `work/render-data.json`;
- `output/final.html`.

Do not compare an old rendered file with newer canonical meaning.

## Step 1 — Mechanical validation

Run:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation covers:

- required artifact presence;
- unresolved placeholders;
- render-data root/collection/package invariants;
- scoring/completion exclusivity and numeric weight total;
- exact generated page IDs/order;
- duplicate HTML IDs;
- navigation reachability;
- project browser title;
- a small **Golden page-composition marker contract**.

### Golden composition marker contract

The validator does not attempt visual equivalence. It only prevents a renderer from silently replacing the approved Golden composition with generic pages.

Examples:

- Gameplay Flow → `narrative-page` + `narrative-sequence`;
- Global Development → `package-tabs` + `section-context`, plus Golden flow/table markers when those blocks exist;
- Gameplay Overview → `package-tabs` + `phase-context-grid` + `phase-overview-table`, plus `role-sequence` when player flow exists;
- Level Design → `package-tabs` + `section-context`, plus `quarry-design-flow`, `quarry-build-table`, and note grid when their source blocks exist;
- Developer → `package-tabs` + `section-context` + `quarry-development-table` + inline score/completion summary, plus flow/note markers when used.

This is intentionally small. Do not expand it into screenshot regression, pixel comparison, DOM snapshotting, component scoring, or a general HTML schema.

Mechanical PASS proves only these structural contracts. It does not prove the page looks correct.

## Step 2 — One integrated review

Read the current document once and assess four lenses:

1. **New Reader / Player Context**
2. **Level Designer**
3. **Developer**
4. **Project Consistency**

Record each finding once even when several lenses are affected.

### New Reader

Overview + Gameplay Flow + relevant Gameplay Overview must answer without guessing:

- what the experience is;
- the player role;
- progression order;
- local objective/result;
- start/end/fail or retry behavior;
- handoff forward;
- important terminology.

Also confirm the page reads like the Golden Sample family rather than a generic report: context before detail, narrative Gameplay Flow, and clear package hierarchy.

### Level Designer

Gameplay Overview → Level Design must allow blockout/build work without inventing material production requirements:

- required areas/objects/routes/relationships;
- build/design flow when meaningful;
- Area Size only when known or materially constrained;
- Build and Visual requirement separated from Gameplay Function;
- local constraints vs shared/global rules;
- notes only when actionable.

The Golden 5-column Build Requirements structure must remain legible. Do not invent dimensions or decorative requirements to make it look full.

### Developer

Gameplay Overview → Level Design → Developer + relevant Global Development must allow an implementation plan without inventing product rules:

- activation/start;
- progression/state transition;
- completion validation;
- quantities/items/resources where relevant;
- timing when relevant;
- scoring or completion behavior;
- recording/duplicate/interruption/reset only when actually required;
- handoff/result;
- verification behavior.

Developer requirements should preserve Golden grouped hierarchy. Scoring/completion belongs inside that hierarchy instead of being detached as a generic appendix table.

### Project Consistency

Compare Overview, Gameplay Flow, Global Development, package pages, scoring/completion, reset, and handoffs.

Different wording is allowed. Different meaning is not.

Check official names, package order, counts, quantities, start/end/fail conditions, timer boundaries, scoring, data ownership where relevant, handoff, interruption, reset, and final-result relationship.

## Visual sanity inside the same REVIEW

When actual rendered/browser/page inspection is available, inspect the Golden output for:

- page/component composition matching the approved Golden family;
- broken or missing package/global tabs;
- wrong footer project brand/page title/code;
- table overflow or unreadable density;
- visibly broken grouped/child rows;
- scoring/completion block placement;
- note grids/Terms Used behavior;
- responsive/print/page-break defects at the level actually inspected.

Do not create another Flow, visual score, screenshot report, pixel-diff gate, or automated “looks like Golden” evaluator.

If visual inspection is unavailable, record `NOT PROVEN` and do not claim Golden visual fidelity was verified.

## Writing quality and density

Inside the same four-lens review, flag only prose/density issues that reduce usability:

- promotional/inflated language instead of concrete behavior;
- vague AI-style filler/fake analysis;
- terminology drift;
- duplicated global rules hiding local requirements;
- pages padded with invented/non-actionable content;
- stylistic rewriting that changes technical meaning.

Do not add an AI score, detector, brevity score, or fifth review lens.

## Severity

- **Critical** — can produce incorrect gameplay/build/scoring/data/reset/implementation behavior.
- **Major** — required information or Golden composition is wrong enough that a production role must invent a material rule or cannot reliably use the page.
- **Minor** — implementable, but local clarity/fidelity can improve without changing meaning.
- **Suggestion** — optional polish.

Critical/Major block `development_ready`.

## Finding ownership

- requirement/project meaning defect → upstream requirement state + `work/content.md`;
- Golden representation/composition defect → `CONTENT-CONTRACT.md` / `work/render-data.json` as appropriate;
- renderer/helper defect → `renderer/core.py` / `renderer/pages.py` / `renderer/render.py`;
- shared template defect → approved template only when the Golden shell itself is proven wrong;
- unresolved product decision → Flow 2.

Never patch `final.html` as source of truth.

## Acceptance record

Keep `work/acceptance.md` compact:

```text
# PRD Acceptance
Status: needs_revision | development_ready | handoff_ready
Reviewed revision: ...

Mechanical: PASS / FAIL
Visual sanity: PASS / FAIL / NOT PROVEN

New Reader: PASS / FAIL
Level Designer: PASS / FAIL
Developer: PASS / FAIL
Project Consistency: PASS / FAIL

Findings
ID | Lens | Severity | Owner | Location | Finding | Resolution Status

Critical: N
Major: N
Result: ...
```

If everything passes, do not expand the report merely to look rigorous.

## Development-ready gate

Set `development_ready` only when:

- mechanical validation passes;
- Golden composition markers pass;
- all four semantic lenses pass;
- Critical=0 and Major=0;
- no material Proposal/Blocked requirement affects scope;
- scoring/completion/handoff/reset behavior is implementable where relevant;
- Golden Sample hierarchy and page composition are preserved;
- writing/density are usable without filler or guessing;
- requested language coverage is usable;
- visual claims do not exceed actual inspection evidence.

The current repository sequence may then create its concise team handoff and mark `handoff_ready`.

## Revisions after handoff

Use the delta path:

```text
approved change
→ update affected requirement/content
→ regenerate affected projection + final HTML
→ reopen affected review boundary
→ one current mechanical check
→ targeted semantic/visual re-review
→ updated accepted PRD
```

Do not replay unrelated source intake or unchanged findings.
