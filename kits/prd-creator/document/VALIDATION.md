# PRD Validation & Team Handoff

`CONTENT-CONTRACT.md` owns semantic completeness. `DESIGN-CONTRACT.md` owns approved page/component grammar. This file owns the minimum proof needed to accept the current revision.

## Default sequence

```text
current PRD revision + required current non-Voice 04 source when present
→ one mechanical validation
→ one integrated semantic-readiness + reconciliation review
→ Material Conservation
→ targeted visual sanity when the claim requires it
→ fix the first wrong owner
→ development_ready | handoff_ready
```

`development_ready` means the current PRD/required 04 scope is accepted for implementation. `handoff_ready` additionally binds the accepted revision to the current versioned delivery and is required before Flow 5.

Do not create separate workflow gates for every reader/role lens. They are questions inside one integrated review.

## 1. Mechanical validation

Run:

```bash
python kits/prd-creator/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation owns deterministic facts: Flow 2 readiness, required artifacts, freshness bindings, page order/IDs/navigation, arithmetic, required design-component markers, content-purity regressions, and current output integrity.

Mechanical PASS does **not** prove source fidelity, semantic completeness, material conservation, adaptive-cardinality quality, or browser readability.

## 2. Integrated semantic readiness

Review the current revision once using relevant lenses:

| Lens | Ready when... |
|---|---|
| Source Fidelity | material project claims remain supported by approved authority or explicit approved Proposal |
| Decision Completeness | implementation does not need to invent unresolved product behavior |
| New Reader | journey, objective, result, setback/recovery and transition are understandable |
| Level Designer | areas/objects/relationships/constraints/gameplay functions are actionable |
| Developer | trigger/state/progression/timing/scoring/result/reset/handoff behavior is actionable |
| Quantitative & Lifecycle Coherence | related timings/counts/capacities/states agree through start → active → result → retry/reset |
| Cross-role Consistency | Gameplay, Level Design, Developer and required 04 describe the same approved system |
| Content Purity | visible copy explains the project rather than PRD-Creator mechanics |
| Design Placement | accepted meaning uses the matching component/page grammar in `DESIGN-CONTRACT.md` |

Record one result:

```text
Semantic Readiness: PASS | FAIL
```

Adaptive child count is not itself a failure. A three-step sequence is valid when three semantic steps are sufficient; a seven-step sequence is valid when seven distinctions are material.

## 3. Semantic reconciliation

Before acceptance, reconcile material meaning across:

```text
approved source / requirement state
→ canonical work/content.md
→ work/render-data.json
→ visible PRD
```

Look for:

- **LOSS** — a material rule/condition/value disappears;
- **CONTRADICTION** — downstream wording changes the rule;
- **UNSUPPORTED** — a new material fact appears without authority/approval;
- **AMBIGUOUS** — representation makes a previously clear rule materially uncertain;
- **CROSS-ROLE DRIFT** — Gameplay / Level Design / Developer / 04 disagree.

This is meaning comparison, not literal-string parity, numeric scoring, or a persisted requirement-to-sentence matrix.

When a semantic list is projected into an approved Flow/Note/Sequence component, verify its meaningful children were conserved; do not compare against AFTERSHOCK's sample count.

## 4. Material Conservation

Material Conservation remains a separate gate because a document can be readable yet omit an independent rule.

For changed/regenerated scope, verify resolved PRD-scope conditions, values, exceptions, recovery rules, result behavior, technical constraints and role-owned requirements retain explicit readable representation.

Do not use word count, row count, or reference-card count as a proxy.

Record:

```text
Material Conservation: PASS | FAIL
```

## 5. Golden/design economy

The exact Golden artifact and stable page/component grammar are protected by `DESIGN-CONTRACT.md` plus focused regression coverage.

Normal content-only production does not reread/re-prove the full reference artifact. Reopen full Golden evidence only when template bytes, page/component grammar, CSS/runtime behavior, or a real browser defect is under review.

Adaptive semantic cardinality inside existing approved component families is a normal projection capability and does not by itself reopen Golden design.

## 6. Targeted visual sanity

Visual PASS requires actual rendered/browser evidence. Static HTML inspection cannot claim it.

For ordinary content work, inspect representative/high-risk pages, normally:

```text
Overview
+ one Gameplay Flow
+ one Gameplay Overview
+ one Level Design
+ one dense Developer page
```

When adaptive cardinality creates unusually dense surfaces, include those pages in browser sanity. Check wrapping/overflow, readable grouping and whether distinct semantic items remain visually separable.

Escalate to broader browser testing only when template/CSS/JS/page composition changed, a targeted defect suggests global impact, or the user asks for broader proof.

## 7. Acceptance record

Keep `work/acceptance.md` compact:

```text
# PRD Acceptance
Status: needs_revision | development_ready | handoff_ready
Mechanical: PASS | FAIL
Semantic Readiness: PASS | FAIL
Material Conservation: PASS | FAIL
Visual sanity: PASS | FAIL | NOT PROVEN
Findings: <only when findings exist>
Critical: N
Major: N
```

Do not persist a score per semantic lens.

## 8. Handoff

Only `handoff_ready` crosses into Flow 5. Before Flow 5 run:

```bash
python kits/prd-creator/validator/validate_handoff.py \
  workspace/active/<project>/
```

Handoff must point to current canonical/projection/acceptance state, `output/README.md`, and the matching versioned `prd.html` / `context.md` / `index.json` bundle. Accepted PRD version must use semantic `X.Y.Z` and agree across the bundle.

`output/README.md` is a resume navigator, not a second project-status database.

## Bounded revision

```text
approved change
→ first affected semantic/design owner
→ affected projection
→ one full-file rerender
→ one mechanical check
→ one integrated review of invalidated scope
→ visual check only where changed/high-risk
→ stop
```

Do not replay unchanged intake, packages, Voice work, mobile QA, every-page QA, or full Golden review for ceremony.
