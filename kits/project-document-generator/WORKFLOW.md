# Workflow

Project Document Generator has three macro steps. Internal files/checks support them; they are not extra user approval stages.

```text
1. UNDERSTAND — Flow 2
2. BUILD PRD  — Flow 3
3. REVIEW     — Flow 4
```

Normal production is **Production Execution**, not repository Developing.

## 1. UNDERSTAND

Owner: `SOURCE-INTAKE.md`.

```text
inspect all relevant source
→ reconcile authority / duplicates
→ recover production-relevant requirements
→ safe Clarification / Completion
→ group only remaining high-impact decisions
```

If user approval is needed, present `Recommended / Reason / Impact` in one compact batch where possible. Do not create a review ceremony when no material decision exists.

**Exit:** `ready_for_prd`, `needs_decision`, or `blocked`.

## 2. BUILD PRD

Semantic/page-composition owner: `CONTENT-CONTRACT.md`.

Normal build is one production operation:

```text
canonical work/content.md
→ compact derived work/render-data.json
→ deterministic renderer
→ approved Golden Sample
→ output/final.html
```

Golden hierarchy/page language comes from `CONTENT-CONTRACT.md`; do not repeat/rederive it from the 794 KB template source during normal production.

### Efficient build behavior

- finish/reconcile canonical meaning before the main render projection;
- do not rebuild full render data after every drafting edit;
- do not hand-write final HTML;
- do not load the full Golden template into model context;
- for English-only documents, use scalar strings instead of duplicated localized values;
- during revisions, update only affected content/render-data subtree and necessary cross-references;
- read `RENDERING.md` only when projection shape or HTML mechanics actually matter.

If drafting exposes a material unresolved product decision, return to UNDERSTAND rather than guessing.

**Exit:** current canonical meaning is represented by the generated Golden PRD without unresolved placeholders.

## 3. REVIEW

Owner: `VALIDATION.md`.

```text
mechanical validator
+ Golden composition markers
+ actual visual sanity when available
+ New Reader / Level Designer / Developer / Consistency
→ fix real findings
→ re-review only invalidated scope
```

The validator may read the complete generated files at runtime. The model should not load `final.html` in full merely to perform semantic review. Inspect source only for a concrete bounded HTML defect.

**Exit:** mechanical/semantic gates pass, Critical=0, Major=0, and evidence claims match what was actually inspected.

## Revision fast path

```text
approved bounded change
→ affected requirement/content
→ required cross-references
→ affected render projection
→ rerender
→ one mechanical check
→ targeted semantic/visual review
```

Do not replay unchanged source intake, resolved decisions, unrelated packages, or unaffected review evidence.

## User-facing delivery

Default delivery is only the final PRD plus material adjustments and any real remaining attention item. Internal state/render data/validator output stay internal unless requested or needed to explain a blocker.

## Stop rule

Do not add more Flow stages, template profiles, quality scores, screenshot/pixel systems, or HTML frameworks to make the process look rigorous. Fix only concrete defects in the smallest owner.
