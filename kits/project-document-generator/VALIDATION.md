# PRD Validation & Team Handoff

Flow 4 decides whether the current Golden PRD is usable by production. Rendering success is necessary but not sufficient.

```text
current revision
→ mechanical validation
→ one-read source/requirement-to-PRD semantic review
→ targeted desktop visual sanity when available
→ fix real findings at first wrong owner
→ development_ready / current handoff boundary
```

## Review input economy

The reviewer/validator must refer to the same revision, but the model does not load every artifact in full.

- requirement truth → relevant requirement/provenance state plus only authoritative source slices needed to verify material coverage;
- semantic reading → `work/content.md`;
- representation question → affected `render-data.json` subtree only;
- full HTML mechanics → `validator/validate.py` consumes `output/final.html`;
- visual quality → actual rendered/browser/page result when available;
- HTML source → only the bounded page/class/marker implicated by a concrete defect.

Do not load the full Golden template, complete generated HTML, or every source file to appear thorough. **Input economy must not become output incompleteness.**

## Mechanical validation

Run once for the finished revision:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

The validator first requires `state/intake-state.yaml` to explicitly declare both `status: ready_for_prd` and `ready_for_prd: true`. Missing, ambiguous, or non-ready Flow 2 state fails validation instead of allowing a rendered artifact to bypass the Flow 2 readiness boundary.

When Flow 2 claims readiness, repository-backed validation also requires the two persisted evidence owners to exist and contain at least one stable entry:

- `state/source-inventory.yaml` → at least one `SRC-###` entry;
- `state/requirement-register.yaml` → at least one `REQ-###` entry.

Missing or empty evidence owners fail instead of being interpreted as “no blocker found.” The validator then checks only **unambiguous explicit blocker markers** inside current entries. It fails on `approval_status: pending` or `recovery_class: blocked` in `requirement-register.yaml`, and on `inspection: blocked` for a current source entry in `source-inventory.yaml`. A source explicitly marked `status: superseded` does not block readiness merely because its old inspection state is `blocked`.

Approved proposals, `inspection: targeted`, omitted defaults, advisory ideas, and other nonblocking detail remain allowed. `evidence_status: conflict` alone is not a blocker because the conflict may already have an approved/higher-authority resolution. This remains a bounded SRC/REQ-entry contradiction guard, not a generic YAML schema validator or automated materiality engine.

The existing `canonical_content_sha256` and `render-data-sha256` checks remain mechanical stale-derivation guards for now. They do **not** prove semantic completeness or source fidelity. Do not treat a matching hash as evidence that the projection carries all material meaning.

### Required Golden content versus Golden markers

Mechanical validation distinguishes **required content presence** from **semantic quality**.

For the existing gameplay PRD family, the required hierarchy itself must be present: at least one `Gameplay Flow`, at least one `Global Development` page, and at least one Gameplay Package. Empty required hierarchy collections fail rather than being reduced to an optional warning.

It also fails when deterministic Golden slots that are already mandatory are absent, including:

- a Gameplay Flow page with no usable narrative beat/context;
- Gameplay Overview without Context, Main Objective, Result, or a player-flow step;
- Level Design without an overview or any Build Requirement row;
- a Global Development page that exists but has no overview or Development Requirement row;
- Developer without an overview.

These checks prove **presence only**. They do not prove that Gameplay Flow is narratively complete, that Development pages carry all material role-owned requirements, or that scoring/result was interpreted correctly. Those remain Flow 2/Flow 4 semantic responsibilities.

The renderer also normalizes scoring display text consistently. Numeric weights and numeric percentage strings such as `60` and `"60%"` render as one percentage marker, while unweighted scoring components are described without inventing percentage signs or equal weighting.

The validator owns current mechanical contracts including Flow 2 readiness/evidence presence, unambiguous current blocker detection, stale derivation bindings, artifact presence, placeholders, required Golden hierarchy/content slots, render-data/package invariants, scoring/completion numeric rules, generated page IDs/order, duplicate IDs, navigation, browser title, and the small Golden composition-marker set.

Mechanical PASS is **not development readiness**. Do not expand the mechanical validator into generic YAML schemas, semantic hashing, word-count checks, minimum-row rules, semantic similarity scoring, DOM snapshots, pixel comparison, artifact manifests, or a generic HTML schema.

## One-read semantic acceptance review

Read each relevant package/document slice once and evaluate all applicable lenses together. Include only the relevant authoritative requirement/source evidence needed to verify material coverage.

Recommended slice:

```text
relevant authoritative/approved requirement evidence
+ relevant global/shared rules
+ Gameplay Flow / Gameplay Overview
+ Level Design
+ Developer
```

For a bounded revision, include only affected package(s) + required cross-references unless wider consistency was invalidated.

### Source / requirement → PRD coverage

This is the central semantic gate.

For material/high-impact requirements in the reviewed scope, ask:

```text
What does authority require?
→ where is that meaning represented in the PRD?
→ is it represented on the surface used by the role that needs it?
→ did compression change, weaken, or omit the meaning?
```

Do not create a permanent coverage matrix or generic traceability framework. Use the existing requirement/provenance state and the smallest relevant source slices.

A PRD is **Major-incomplete** when a Level Designer or Developer must reopen the original source to discover a material requirement that should have been carried into the PRD.

### New Reader / Player Context

Can a new team member understand:

- where the player starts and why;
- chronological progression through the experience;
- what the player sees/understands;
- important NPC/system/environment cues;
- what the player does and how the world responds;
- setbacks/recovery when material;
- objective/result;
- forward transition and important carried state/items;
- terminology needed to follow the experience?

Gameplay Flow must read as a concise **player journey**, not a developer checklist or generic task summary.

If the reader understands only “what tasks exist” but not “what the player experiences and why the next beat happens,” this lens fails.

### Level Designer

Can Level Design build the package from its page + clearly referenced shared rules without reopening source for missing material behavior?

Check applicable meaning such as:

- required areas/objects/routes and relationships;
- readable destination, sightlines, warnings, guidance, and visual state;
- known size/dimension constraints;
- safe/recovery/landing areas;
- interaction placement/access;
- entry/exit/reset boundaries;
- build/visual requirements;
- gameplay function;
- important build notes that prevent a materially wrong result.

Do not require information the project intentionally leaves open. Do require information the source actually defines and production needs.

### Developer

Can Developer implement the package from its page + clearly referenced shared rules without reopening source for missing material behavior?

Check applicable meaning such as:

- activation/precondition;
- interaction behavior;
- progression/state;
- quantities/timing;
- success/completion;
- **Objective Score or explicit `No Objective Score`**;
- scoring components/weights/timer/no-score condition where applicable;
- relationship to final result;
- player-facing score/result display;
- telemetry/export/data behavior;
- interruption/disconnect/pause;
- retry/reset/cleanup;
- transition/handoff;
- important implementation notes.

Keep these three meanings separate unless authority explicitly joins them:

```text
internal score/result
player-facing score/result display
telemetry/export payload
```

A statement such as “do not display scores” or “do not export scores” must not silently erase internal Objective Score calculation.

### Project Consistency

Cross-check material facts only:

- official names and terminology;
- package/order/topology;
- counts/quantities/timing/scoring;
- Objective Score vs `No Objective Score`;
- score/result display and telemetry/export distinctions;
- conditions, handoff, interruption/reset, and final-result relationship;
- shared/global defaults versus explicit package exceptions;
- materially vague requirements that could yield different product behavior;
- authoritative known project/platform/production constraints when they are part of accepted project evidence.

Different wording is allowed; different meaning is not. A legitimate local exception is not inconsistency when it is explicit and supported.

Record each finding once and tag all affected lens(es) if needed.

## Golden quality-floor review

Do not judge Golden fidelity only by hierarchy/classes/tables.

Ask whether each corresponding surface performs the same **production function** as the approved Golden Sample using current-project meaning:

```text
Gameplay Flow → understandable player journey
Gameplay Overview → complete local context/objective/result
Level Design → actionable complete build meaning
Developer → actionable complete runtime/result meaning
Global Development → visible shared ownership across packages
```

Do not compare word count or row count. A shorter page may be correct when the project is genuinely simpler. A short page is not correct when the source contains material information that was compressed away.

## Flow 2 fallback boundary

Flow 4 may reveal a requirement-recovery defect that earlier stages missed. If a finding requires a new product/design decision, authority reconciliation, scoring interpretation, or material ambiguity resolution, return that finding to Flow 2.

Flow 4 may improve wording when the underlying approved meaning is already clear. It may not invent a metric, workaround, score rule, interaction, or product choice merely to make the PRD pass review.

## Humanized writing review

PRD prose should be natural production writing rather than database-like requirement dumps.

Flag when it materially hurts comprehension:

- comma-stacked lists turned into unreadable paragraphs;
- fragments that remove cause/effect/context;
- Gameplay Flow written as implementation bullets rather than player experience;
- generic sentences such as “implement the mechanic and data” that hide what actually happens;
- inflated/promotional/formulaic AI wording;
- vague filler/fake analysis;
- terminology drift;
- stylistic edits that alter technical meaning.

Prefer context → action → response → consequence. Tables/formulas/IDs/timings/weights remain precise and are not rewritten merely for style.

No AI detector, readability score, word-count gate, or separate Humanize approval round.

## Visual sanity — desktop by default

The default PRD visual proof is **desktop-only** unless the user/project explicitly requires mobile/responsive behavior or a current defect is mobile-specific.

For a representative visual smoke test, inspect only enough to disprove obvious rendering problems, normally:

```text
Overview
+ one Gameplay Flow page
+ one Level Design page
+ one dense Developer page
```

Check as relevant:

- Golden composition/page rhythm;
- sidebar/navigation reachability;
- tabs on one representative package;
- table overflow/readability;
- grouped/child rows;
- scoring/result placement;
- obvious density/broken-layout issues.

Do **not** routinely test mobile viewport, every navigation entry, every Terms disclosure, theme persistence, every tab, or localStorage behavior unless the changed scope requires it.

If actual desktop browser/page inspection is unavailable, use `NOT PROVEN`. HTML-source review is not visual proof.

## Severity and ownership

- **Critical** — can produce materially incorrect gameplay/build/scoring/data/reset/implementation behavior.
- **Major** — a production role must invent a material rule, reopen source to recover an omitted material rule, or cannot reliably use the page.
- **Minor** — implementable; local clarity/fidelity can improve without changing meaning.
- **Suggestion** — optional polish.

Critical/Major block readiness.

Fix the first wrong owner:

- requirement/project meaning or authority interpretation → requirement state + Flow 2;
- canonical content incomplete/over-compressed → `content.md` / `CONTENT-CONTRACT.md` behavior;
- Golden representation → affected projection/content representation;
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

## Flow 5 handoff entry guard

Before Flow 5 starts, run:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

The handoff validator checks the existing `handoff_ready` status, `accepted_prd_version`, canonical artifact paths, and compact acceptance truth. `Visual sanity: NOT PROVEN` remains allowed when actual desktop evidence was unavailable; it is not visual PASS.

This uses the existing lifecycle/acceptance owners and `document.version`. Do not add a handoff hash, artifact manifest, or second approval framework.

## Development-ready gate

Set `development_ready` only when:

- Flow 2 explicitly remains `ready_for_prd`;
- required persisted evidence owners exist and no explicit current blocker contradicts readiness;
- current derived artifacts pass applicable mechanical checks;
- material/high-impact source/requirement meaning is represented on the correct PRD surfaces;
- Gameplay Flow communicates the actual player journey;
- every package states Objective Score or explicit `No Objective Score` correctly and preserves display/export distinctions when relevant;
- Level Design and Developer can work without reopening original source for omitted material requirements;
- Golden functional quality is preserved without copying sample-specific facts;
- prose is human-readable and precise;
- all four lenses pass;
- Critical=0/Major=0;
- no material unresolved decision affects scope;
- claims do not exceed actual visual/runtime evidence.

Set `handoff_ready` only after the same accepted revision is represented truthfully in `work/acceptance.md` and `state/handoff-state.yaml`.

## Revision and proof economy

```text
approved/material change
→ affected requirement/content
→ affected projection + rerender
→ one applicable mechanical check
→ one targeted semantic review
→ desktop visual smoke only when visual behavior was invalidated or proof is required
```

Do not replay unrelated source intake, full-document review, mobile QA, Voice tests, browser interactions, or unchanged proof merely for ceremony. Use the cheapest evidence that can falsify the claim, then stop.
