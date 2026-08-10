# PRD Validation & Team Handoff

Flow 4 decides whether the current Golden PRD is usable by the production team. Rendering success is necessary but not sufficient.

```text
current revision
→ mechanical validator
→ one integrated semantic + visual review
→ fix real findings
→ development_ready
→ current handoff boundary
```

Do not turn review lenses into separate approval ceremonies.

## Review input economy

The validator and reviewer must refer to the same current revision, but the model does **not** need to load every artifact in full.

- Requirement truth → inspect only relevant requirement state/provenance for the scope being reviewed.
- Semantic review → use `work/content.md` as primary reading source.
- Render projection → inspect only relevant `render-data.json` subtree when representation is questioned.
- Full HTML mechanics → let `validator/validate.py` consume `output/final.html` directly.
- Visual quality → inspect the actual rendered/browser/page result when available.
- HTML source → inspect only the exact page/component/marker implicated by a concrete finding.

Do not load the complete large Golden template or complete generated HTML into model context merely to say review was thorough.

## Step 1 — Mechanical validation

Run once for the finished revision:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

The validator covers the current mechanical contract, including:

- required artifact presence;
- unresolved placeholders;
- render-data/package invariants;
- scoring/completion exclusivity and numeric weight total;
- exact generated page IDs/order;
- duplicate HTML IDs;
- navigation reachability;
- project browser title;
- small Golden page-composition marker contract.

Mechanical PASS proves structural contracts only. It does not prove page appearance.

Do not expand this into pixel comparison, DOM snapshots, visual scoring, or a generic HTML schema.

## Step 2 — One integrated semantic review

Assess four lenses and record each finding once:

1. **New Reader / Player Context**
2. **Level Designer**
3. **Developer**
4. **Project Consistency**

### New Reader

Confirm the reader can understand experience, player role, progression, local objective/result, start/end/fail-or-retry behavior, handoff forward, and important terminology without guessing.

### Level Designer

Confirm Gameplay Overview → Level Design provides the areas/objects/routes/relationships, build/design flow when meaningful, known size constraints, Build and Visual requirements, Gameplay Function, and actionable notes needed for blockout/build work without invented detail.

### Developer

Confirm Gameplay Overview → Level Design → Developer + relevant global rules provide activation, progression/state, completion, required quantities/timing, scoring or completion behavior, necessary recording/interruption/reset, handoff/result, and verification behavior without invented product rules.

### Project Consistency

Check official names, package order, counts/quantities, conditions, timing boundaries, scoring, handoff, interruption/reset, and final-result relationship across relevant sections. Different wording is allowed; different meaning is not.

## Visual sanity inside the same review

When actual rendered/browser/page inspection is available, inspect only the current pages needed to establish visual quality:

- Golden composition/page rhythm;
- tabs/navigation/footer identity;
- table overflow/readability;
- grouped/child rows;
- score/completion placement;
- note/Terms behavior;
- density;
- responsive/print/page-break behavior only where actually inspected.

If visual inspection is unavailable, record `NOT PROVEN`. Do not substitute reading HTML source for visual proof.

## Writing quality and density

Inside the same four lenses, flag only issues that reduce usability:

- inflated/promotional or formulaic AI wording;
- vague filler/fake analysis;
- terminology drift;
- duplicated global rules hiding local requirements;
- non-actionable padding/invented detail;
- stylistic rewriting that changes technical meaning.

No AI detector, brevity score, or fifth lens.

## Severity

- **Critical** — can produce materially incorrect gameplay/build/scoring/data/reset/implementation behavior.
- **Major** — a production role must invent a material rule or cannot reliably use the page.
- **Minor** — implementable but local clarity/fidelity can improve without changing meaning.
- **Suggestion** — optional polish.

Critical/Major block development readiness.

## Finding ownership

- requirement/project meaning → requirement state + `work/content.md`;
- Golden representation → `CONTENT-CONTRACT.md` / affected render-data subtree;
- renderer mechanics → exact `renderer/*` owner;
- validator mechanics → `validator/validate.py`;
- template mechanics → approved template only when the template itself is proven wrong;
- unresolved product decision → Flow 2.

Never patch `final.html` as source of truth.

## Compact acceptance record

Keep `work/acceptance.md` short:

```text
# PRD Acceptance
Status: needs_revision | development_ready | handoff_ready
Mechanical: PASS / FAIL
Visual sanity: PASS / FAIL / NOT PROVEN
New Reader: PASS / FAIL
Level Designer: PASS / FAIL
Developer: PASS / FAIL
Project Consistency: PASS / FAIL
Findings: <table only when findings exist>
Critical: N
Major: N
```

Do not write expanded evidence prose when everything passes.

## Development-ready gate

Set `development_ready` only when mechanical/Golden structural checks pass, all four semantic lenses pass, Critical=0/Major=0, no material unresolved decision affects scope, requested language coverage is usable, and claims do not exceed actual visual/runtime evidence.

## Revision path

```text
approved change
→ affected requirement/content
→ affected projection + rerender
→ one mechanical check
→ targeted semantic/visual re-review
```

Do not replay unrelated source intake, full-document semantic review, or unchanged evidence.
