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

The validator first requires `state/intake-state.yaml` to explicitly declare both `status: ready_for_prd` and `ready_for_prd: true`. Missing, ambiguous, or non-ready Flow 2 state fails validation instead of allowing a rendered artifact to bypass the Flow 2 readiness boundary.

When Flow 2 claims readiness, the validator also checks only **unambiguous explicit blocker markers** in the existing persisted state. It fails on `approval_status: pending` or `recovery_class: blocked` in `requirement-register.yaml`, and on `inspection: blocked` in `source-inventory.yaml`. Approved proposals, `inspection: targeted`, omitted defaults, advisory ideas, and other nonblocking detail remain allowed. `evidence_status: conflict` alone is not a blocker because the conflict may already have an approved/higher-authority resolution. This is a narrow contradiction guard, not a YAML schema validator or automated materiality engine.

It also requires `work/render-data.json` to carry `canonical_content_sha256` matching the current exact bytes of `work/content.md`. If canonical content changes without regenerating the projection binding, validation fails as stale instead of accepting an older projection as current.

The generated `output/final.html` must also contain exactly one `render-data-sha256` metadata marker matching the current exact bytes of `work/render-data.json`. A missing, duplicate, invalid, or mismatched marker fails validation. This prevents an older HTML artifact from passing merely because page IDs/composition still resemble the newer projection.

The validator owns current mechanical contracts including Flow 2 readiness declaration, unambiguous persisted Flow 2 blocker detection, canonical-content/projection revision binding, projection/HTML revision binding, artifact presence, placeholders, render-data/package invariants, scoring/completion numeric rules, generated page IDs/order, duplicate IDs, navigation, browser title, and the small Golden composition-marker set.

Mechanical PASS proves these implemented structure/current-revision/explicit-state contracts only—not semantic equivalence, completeness of arbitrary Flow 2 reasoning, or visual quality. Do not expand this into generic YAML schemas, semantic hashing, pixel comparison, DOM snapshots, visual scoring, artifact manifests, or a generic HTML schema.

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

Cross-check material facts only:

- official names and terminology;
- package/order/topology;
- counts/quantities/timing/scoring;
- conditions, handoff, interruption/reset, and final-result relationship;
- shared/global defaults versus explicit package exceptions;
- materially vague requirements that could yield different product behavior;
- authoritative known project/platform/production constraints when they are part of accepted project evidence.

Different wording is allowed; different meaning is not. A legitimate local exception is not inconsistency when it is explicit and supported.

Record each finding once and tag all affected lens(es) if needed.

## Flow 2 fallback boundary

Flow 4 may reveal a requirement-recovery defect that earlier stages missed. If a finding requires a new product/design decision—such as resolving material ambiguity, choosing a global/local exception, reconciling contradictory values, or deciding how to handle a known feasibility conflict—return that finding to Flow 2.

Flow 4 may fix wording when the underlying approved meaning is already clear. It may not invent a metric, workaround, rule, or product choice merely to make the PRD pass review.

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
- unresolved product/design choice or missing Flow 2 recovery → Flow 2 requirement state;
- Golden representation → `CONTENT-CONTRACT.md` / affected projection;
- renderer mechanics → exact `renderer/*` owner;
- validator mechanics → `validator/validate.py`;
- template mechanics → Golden template only when proven responsible.

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

Set `development_ready` only when Flow 2 explicitly remains `ready_for_prd`, no unambiguous persisted Flow 2 blocker contradicts that readiness, current canonical content is bound to the current render projection, current `final.html` is bound to that exact projection, mechanical/Golden structural checks pass, all four lenses pass, Critical=0/Major=0, no material unresolved decision affects scope, requested language coverage is usable, and claims do not exceed actual visual/runtime evidence.

## Revision path

```text
approved change
→ affected requirement/content
→ affected projection + refreshed canonical-content binding + rerender
→ one mechanical check
→ one targeted multi-lens/visual review
```

Do not replay unrelated source intake, full-document review, or unchanged evidence.
