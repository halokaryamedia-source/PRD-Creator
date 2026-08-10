# PRD Validation & Team Handoff

Flow 4 decides whether the current Golden PRD is usable by production. Rendering success is necessary but not sufficient.

```text
current revision
→ mechanical validation
→ one-read multi-lens semantic review
→ actual visual sanity when available
→ fix real findings
→ development_ready / current handoff boundary
```

## Review input economy

The reviewer/validator must refer to the same revision, but the model does not load every artifact in full.

- requirement truth → only relevant requirement/provenance state;
- semantic reading → `work/content.md`;
- representation question → affected `render-data.json` subtree only;
- full HTML mechanics → `validator/validate.py` consumes `output/final.html`;
- visual quality → actual rendered/browser/page result when available;
- HTML source → only the bounded page/class/marker implicated by a concrete defect.

Do not load the full Golden template or complete generated HTML to appear thorough.

## Mechanical validation

Run once for the finished revision:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

The validator owns current mechanical contracts including artifact presence, placeholders, render-data/package invariants, scoring/completion numeric rules, generated page IDs/order, duplicate IDs, navigation, browser title, and the small Golden composition-marker set.

Mechanical PASS proves structure only—not visual quality. Do not expand this into pixel comparison, DOM snapshots, visual scoring, or a generic HTML schema.

## One-read multi-lens review

Read each relevant package/document slice **once** and evaluate all applicable lenses together. Do not reread the same prose separately as New Reader, Level Designer, Developer, and Consistency.

Recommended slice:

```text
relevant global/shared rules
+ Gameplay Overview
+ Level Design
+ Developer
```

For a bounded revision, include only affected package(s) + required cross-references unless wider consistency was invalidated.

### New Reader / Player Context

Can the reader understand the experience, player role, progression, objective/result, start/end/fail-or-retry behavior, forward handoff, and important terminology without guessing?

### Level Designer

Does the package provide required areas/objects/routes/relationships, meaningful design flow, known size constraints, Build and Visual requirements, Gameplay Function, and actionable notes without invented detail?

### Developer

Does the package + relevant global rules provide activation, progression/state, completion, quantities/timing, scoring/completion behavior, necessary recording/interruption/reset, handoff/result, and verification behavior without invented product rules?

### Project Consistency

Cross-check material facts only: official names, order, counts/quantities, conditions, timing, scoring, handoff, interruption/reset, and final-result relationship. Different wording is allowed; different meaning is not.

Record each finding once and tag all affected lens(es) if needed.

## Visual sanity

When actual rendered/page inspection is available, check only what is required to support the visual claim:

- Golden composition/page rhythm;
- tabs/navigation/footer identity;
- table overflow/readability;
- grouped/child rows;
- scoring/completion placement;
- note/Terms behavior;
- density;
- responsive/print/page-break behavior only where actually inspected.

If unavailable, use `NOT PROVEN`. HTML-source review is not visual proof.

## Writing/density inside the same review

Flag only issues that reduce usability or meaning:

- inflated/promotional/formulaic AI wording;
- vague filler/fake analysis;
- terminology drift;
- duplicated global rules hiding local requirements;
- non-actionable/invented padding;
- stylistic edits that alter technical meaning.

No AI detector, brevity score, or fifth lens.

## Severity and ownership

- **Critical** — can produce materially incorrect gameplay/build/scoring/data/reset/implementation behavior.
- **Major** — a production role must invent a material rule or cannot reliably use the page.
- **Minor** — implementable; local clarity/fidelity can improve without changing meaning.
- **Suggestion** — optional polish.

Critical/Major block readiness.

Fix the first wrong owner:

- requirement/project meaning → requirement state + `content.md`;
- Golden representation → `CONTENT-CONTRACT.md` / affected projection;
- renderer mechanics → exact `renderer/*` owner;
- validator mechanics → `validator/validate.py`;
- template mechanics → Golden template only when proven responsible;
- unresolved product choice → Flow 2.

Never patch `final.html` as source of truth.

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

Do not add evidence prose when everything passes.

## Development-ready gate

Set `development_ready` only when mechanical/Golden structural checks pass, all four lenses pass, Critical=0/Major=0, no material unresolved decision affects scope, requested language coverage is usable, and claims do not exceed actual visual/runtime evidence.

## Revision path

```text
approved change
→ affected requirement/content
→ affected projection + rerender
→ one mechanical check
→ one targeted multi-lens/visual review
```

Do not replay unrelated source intake, full-document review, or unchanged evidence.
