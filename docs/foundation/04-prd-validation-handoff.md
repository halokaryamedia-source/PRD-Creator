# Flow 4 — PRD Validation & Team Handoff

Status: active durable policy

## Purpose

Separate generated project documentation from production-ready documentation and preserve only minimum revision-specific acceptance/handoff evidence needed for continuation.

## Canonical owners

- PRD semantic completeness + Material Conservation → `kits/prd-creator/document/CONTENT-CONTRACT.md`;
- PRD Golden page/component presentation grammar → `kits/prd-creator/document/DESIGN-CONTRACT.md`;
- bounded non-Voice 04 Production Asset contract → `kits/prd-creator/production-assets/CONTRACT.md`;
- detailed Flow 4 procedure → `kits/prd-creator/document/VALIDATION.md`;
- project handoff state → `state/handoff-state.yaml`;
- compact acceptance → `work/acceptance.md`;
- stable resume navigator → `output/README.md`;
- current versioned delivery → `output/v<document.version>/{prd.html, context.md, index.json}`.

This foundation page does not maintain another Golden checklist, semantic scorecard, or Production Asset review matrix.

## Flow 4 sequence

```text
current canonical PRD + current 04 source when present + deterministic HTML
→ one mechanical validation
→ one integrated Semantic Readiness + semantic reconciliation review
→ Material Conservation
→ targeted visual sanity when the claim requires it
→ Critical/Major?
     yes → fix first wrong owner + recheck invalidated scope
     no  → development_ready / handoff_ready
```

## Proof boundaries

Mechanical validation proves deterministic repository/render facts only. It does not prove source fidelity, production-role completeness, semantic conservation, 04 readiness, adaptive-cardinality quality, or visual readability.

`Semantic Readiness` is one integrated decision considering as relevant:

```text
Source Fidelity
Decision Completeness
New Reader
Level Designer
Developer
Production Assets
Quantitative/Lifecycle Coherence
Cross-role Consistency
Content Purity
Design Placement
```

Do not persist a separate PASS field for every lens.

### Semantic reconciliation

Before acceptance compare material meaning across:

```text
approved source / requirements
→ canonical content
→ render projection
→ visible PRD
```

Detect material loss, contradiction, unsupported invention, ambiguity, or cross-role drift. Literal prose equality is not required.

### Adaptive cardinality

Reference-project card/step counts are not a readiness metric. The accepted project may use a different number of children inside approved Flow / Note / Sequence components when that count better preserves its actual semantic distinctions.

A production failure exists when meaning is omitted, invented, contradictory, ambiguous, or unreadable—not merely because a component has three or six children instead of four/five.

`Material Conservation` remains separate because a document can be clear yet omit an independently actionable rule.

`Visual sanity` remains separate because browser/render evidence is a different proof channel. Static HTML inspection cannot claim visual PASS.

A production role needing to reopen source to recover material meaning that belongs in the document is a **Major** completeness failure.

## Golden/design proof economy

The exact Golden artifact is retained and design grammar is owned by `DESIGN-CONTRACT.md`, the renderer contract, exact reference bytes, and focused regressions.

For ordinary content work, do not repeat full Golden reference proof. Validate current project meaning against the existing semantic/design contracts and inspect representative/high-risk pages.

When adaptive cardinality creates a dense page, target that page for browser sanity. Escalate to broad visual/reference proof only when template/CSS/JS/page grammar changed, a targeted defect suggests global impact, or the user requests broader proof.

## Acceptance record

Keep `work/acceptance.md` compact:

```text
# PRD Acceptance
Status: needs_revision | development_ready | handoff_ready
Mechanical: PASS | FAIL
Semantic Readiness: PASS | FAIL
Material Conservation: PASS | FAIL
Visual sanity: PASS | FAIL | NOT PROVEN
Critical: N
Major: N
Findings: <only when findings exist>
```

Do not duplicate checksum tables, CI transcripts, role-by-role PASS fields, or a separate 04 PASS layer.

## Handoff boundary

Before Flow 5, `kits/prd-creator/validator/validate_handoff.py` confirms current accepted revision, canonical inputs, acceptance state, `output/README.md`, versioned `prd.html` / `context.md` / `index.json`, handoff state, and `document.version` agree.

When 04 exists, `handoff_ready` also depends on integrated semantic review applying the 04 readiness contract. Mechanical freshness alone does not prove professional actionability.

`handoff_ready` means the accepted project document may be used as the current production reference/downstream Voice input. It does not mean client approval, implementation completion, gameplay QA, release approval, or completed Voice Production.

## Bounded revision

```text
approved change
→ affected semantic/design/04 source/projection only
→ one deterministic full-file rerender
→ one mechanical check
→ one integrated review of invalidated scope
→ visual check only where changed/high-risk
→ stop
```

Do not replay unchanged intake, unrelated packages, full Golden proof, Voice tests, mobile QA, or every-page visual inspection for ceremony.
