# PRD Validation & Team Handoff

Flow 4 decides whether a generated PRD is actually usable by the production team. Rendering success is necessary but not sufficient.

The review stays simple:

```text
current PRD + HTML
→ mechanical check
→ visual sanity when inspection is available
→ one integrated four-lens review
→ fix only real findings
→ development_ready
→ concise team handoff
→ handoff_ready
```

Do not turn mechanical, visual, or four-lens review into separate user approval ceremonies.

## Status model

Use exactly one current PRD status in `state/handoff-state.yaml`:

- `pending_review` — Flow 3 output exists but Flow 4 audit is incomplete;
- `needs_revision` — one or more Critical/Major findings remain;
- `development_ready` — mechanical checks pass and all four semantic lenses pass with Critical=0 and Major=0;
- `handoff_ready` — `development_ready` plus `output/team-handoff.md` exists and points the team to the accepted PRD;
- `blocked` — required artifacts/evidence are unavailable or a required upstream decision must return to Flow 2.

`handoff_ready` means the documentation is ready for production use. It does **not** mean client sign-off, release approval, or implementation completion.

## Required inputs

Audit the same current revision of:

- `state/requirement-register.yaml` — traceability / unresolved requirement state;
- `work/content.md` — canonical PRD meaning;
- `work/render-data.json` — derived rendering projection;
- `output/final.html` — rendered presentation.

Do not audit an old HTML file against newer canonical content.

## Step 1 — Mechanical validation

Run once for the finished current revision:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

This check covers file presence, visible placeholders, render-data invariants, package role objects, scoring/completion exclusivity, numeric scoring weights, expected generated pages, duplicate HTML IDs, navigation reachability, and project browser title.

Mechanical `pass` is structural evidence only. It cannot issue `development_ready` by itself.

## Visual sanity inside the same review

When the execution channel provides actual rendered/browser/page inspection, inspect the current HTML once for obvious presentation defects that would make the Golden Sample output harder to use.

Check only practical failure surfaces:

- clipped/overflowing content;
- broken or unreadable tables/cards/tabs;
- broken visible navigation or controls;
- accidental blank/near-empty presentation caused by rendering/layout failure rather than intentionally concise content;
- text density that is visibly unreadable;
- responsive/print/page-break defects in the mode actually inspected.

Rules:

- visual sanity is part of Flow 4 REVIEW, not a new Flow, score, or screenshot-report system;
- do not create pixel-diff or Golden regression machinery without a proved need;
- visual inspection does not need a separate user approval round;
- if rendered/browser inspection is unavailable, record `NOT PROVEN` and do not claim visual quality was verified;
- semantic `development_ready` may still be evaluated from available evidence, but any visual-quality claim remains limited to what was actually inspected.

## Step 2 — One integrated four-lens review

Read the current PRD once, then assess it through four lenses. A finding may affect more than one lens, but record the finding **once** in the findings table.

### A. New Reader / Player Context

Assume the reviewer reads Overview + Gameplay Flow + the relevant Gameplay Overview page only.

They must be able to answer without guessing:

- What is this project / experience?
- What is the player/user role?
- What happens in what order?
- What starts this package?
- What counts as valid completion?
- What can fail, block, or retry?
- What result/handoff continues forward?
- Are project-specific terms understandable where first needed?

### B. Level Designer

Assume the level designer reads Gameplay Overview → Level Design for an assigned package.

They must be able to begin blockout/build work without inventing the main production requirements:

- required areas, objects, landmarks, routes, or relationships;
- entry, exit, return, or handoff path where relevant;
- build order / level-design flow;
- material dimensions and quantities where gameplay depends on them;
- visual/build requirement separated from gameplay function;
- interaction space/readability needed by the mechanic;
- package-local constraints that differ from global rules.

The Golden Sample Level Design page remains part of the package structure. If little package-specific build work exists, the page may be concise and rely on the relevant shared/global rule. Do not invent cosmetic dimensions or build requirements just to fill the page.

### C. Developer

Assume the developer reads Gameplay Overview → Level Design → Developer plus relevant Global Development pages.

They must be able to form an implementation plan without inventing product rules:

- activation/start trigger;
- progression/state transitions;
- valid completion validation;
- quantities/items/resources/state ownership when relevant;
- timer start/stop/excluded time when applicable;
- scoring **or** completion-data behavior;
- recorded/persistent data only when actually required;
- duplicate prevention when actually required;
- interruption/disconnect behavior when relevant;
- reset behavior;
- handoff/result to the next package;
- verification/acceptance behavior.

The Golden Sample Developer page remains part of the package structure. When a package has little local runtime complexity, keep the page focused on the actual trigger/behavior/result and do not invent architecture, persistence, analytics, APIs, or tracking merely to fill the surface.

### D. Project Consistency

Compare Overview, Gameplay Flow, Global Development, all package pages, scoring/completion, reset, and handoffs.

Different wording is allowed. Different meaning is not.

Check especially:

- official names and terminology;
- package order / progression;
- player/session/arena counts;
- quantities and important dimensions;
- start/end/fail/retry conditions;
- timer boundaries;
- score components/weights/inputs;
- recorded data and ownership where relevant;
- handoff items/state/results;
- interruption/disconnect/reset behavior;
- final-result relationship.

## Writing quality and information density inside the same review

Do not create a fifth perspective, AI score, detector, brevity score, or separate writing gate.

While reviewing the four lenses, flag prose/content only when it reduces usability, for example:

- inflated/promotional wording instead of concrete behavior;
- vague comments such as `important`, `immersive`, `seamless`, or `engaging` that add no production information;
- repeated filler or fake analysis;
- synonym cycling that makes one project term look like several concepts;
- duplicated global rules that hide the package-specific requirement;
- role pages padded with invented or non-actionable detail merely to fill visual space;
- stylistic rewriting that changes or obscures IDs, names, quantities, timings, scoring, triggers, conditions, state names, or other technical facts.

If the meaning is already clear and precise, leave it alone.

Writing/density findings are normally `Minor` or `Suggestion`. Escalate to `Major` only when vague, misleading, duplicated, or missing information forces a production role to invent a material rule.

## Severity

- **Critical** — can produce incorrect gameplay, scoring, data, build, ownership, reset, or implementation behavior.
- **Major** — required information is missing/contradictory enough that the role would need to invent a product decision.
- **Minor** — meaning is implementable but local clarity/consistency can improve without changing the product rule.
- **Suggestion** — optional polish; never blocks readiness.

Critical and Major always block `development_ready`.

A Minor may remain only when it does not change meaning, its owner/location is recorded, and leaving it open is intentional.

## Finding ownership

Classify the root owner before fixing:

- project meaning / requirement defect → fix `work/content.md` (and upstream requirement/decision state when needed), regenerate render-data, rerender;
- derived projection defect → regenerate/fix `work/render-data.json` from canonical content;
- renderer/template presentation defect → fix active renderer/template, then rerender;
- unresolved product decision → return the requirement to Flow 2; do not solve it during audit.

Never patch `final.html` as the source of truth.

## Acceptance record

Create/update `work/acceptance.md` as a concise integrated review.

When findings exist:

```text
# PRD Acceptance

Status: needs_revision | development_ready | handoff_ready
Reviewed revision: <content/html version or commit/reference>

Mechanical: PASS / FAIL
Visual sanity: PASS / FAIL / NOT PROVEN

Perspective Summary
New Reader: PASS / FAIL
Level Designer: PASS / FAIL
Developer: PASS / FAIL
Project Consistency: PASS / FAIL

Findings
ID | Lens | Severity | Owner | Location | Finding | Resolution Status

Gate
Critical: N
Major: N
Minor: N
Result: ...
```

When everything passes and there are no findings, keep the record compact:

```text
Status: development_ready
Mechanical: PASS
Visual sanity: PASS | NOT PROVEN
New Reader: PASS
Level Designer: PASS
Developer: PASS
Project Consistency: PASS
Critical: 0
Major: 0
Findings: none
```

Do not duplicate a finding under several perspective headings and then repeat it again in the table. Do not copy the PRD into the audit.

## Targeted re-review after revisions

An approved bounded revision should invalidate only the evidence that depends on it.

After the revision fast path:

- rerun the current mechanical validator for the regenerated output;
- visually re-inspect only when the changed output could affect presentation and visual inspection is available;
- re-review the changed package/section and directly dependent global/cross-reference meaning;
- preserve unaffected accepted findings/lenses instead of replaying the entire semantic review.

Use a full Flow 4 semantic review only when the change affects broad/shared meaning, multiple package dependencies, or the overall journey/consistency contract.

## Handoff state

Maintain `state/handoff-state.yaml`:

```yaml
flow: 4
status: handoff_ready
content: work/content.md
render_data: work/render-data.json
html: output/final.html
acceptance: work/acceptance.md
handoff: output/team-handoff.md
mechanical: passed
visual: passed_or_not_proven
perspectives:
  new_reader: passed
  level_designer: passed
  developer: passed
  project_consistency: passed
findings:
  critical: 0
  major: 0
  minor: 0
next_step: flow_5_voice_requirement_extraction
```

Use project-relative paths. Do not store chat-only claims in the state.

## Team handoff

After the gate passes, create `output/team-handoff.md` as a navigation aid, not a second PRD and not another authoring phase.

It should contain only:

- project / accepted PRD version or revision;
- canonical PRD path and rendered HTML path;
- short project purpose / current production scope;
- recommended reading route for Level Designer and Developer;
- package/stage inventory;
- genuinely global systems that affect multiple packages;
- accepted Minor findings or explicit non-blocking caveats, if any;
- statement that Critical=0 / Major=0 at the accepted revision.

Do not copy every requirement into the handoff file.

## Development-ready gate

Set `development_ready` only when:

- mechanical validation passes;
- New Reader lens passes;
- Level Designer lens passes;
- Developer lens passes;
- Project Consistency lens passes;
- Critical findings = 0;
- Major findings = 0;
- no unresolved Proposal/Blocked requirement affects the handed-off scope;
- scoring/completion and handoff/reset behavior are implementable where relevant;
- Golden Sample document structure remains intact for this document family;
- explanatory prose and information density are clear enough that the intended role does not need to decode filler or guess missing rules;
- requested language coverage is usable for the intended team.

Visual quality is claim-specific: mark it `PASS` only after actual current-output inspection; otherwise preserve `NOT PROVEN` rather than inventing evidence.

Then create the concise team handoff and set `handoff_ready`.

## Revisions after handoff

Prefer the revision fast path:

```text
approved bounded change
→ update affected requirement/decision owner when needed
→ update affected content.md section + necessary cross-references
→ regenerate render-data.json / final.html
→ reopen only invalidated review evidence
→ targeted re-review
→ updated handoff state
```

Escalate to broader re-audit only when the change invalidates broader project meaning. Do not silently keep an old `handoff_ready` status against a newer PRD revision.
