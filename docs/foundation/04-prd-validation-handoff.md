# Flow 4 — PRD Validation & Team Handoff

Status: active durable policy

## Purpose

Separate generated project documentation from production-ready documentation and preserve only the minimum revision-specific acceptance/handoff evidence needed for continuation.

## Canonical owners

- mandatory PRD-core meaning → `kits/prd-creator/document/CONTENT-CONTRACT.md`;
- Golden page/component grammar → `kits/prd-creator/document/DESIGN-CONTRACT.md`;
- bounded non-Voice 04 contract → `kits/prd-creator/production-assets/CONTRACT.md`;
- detailed Flow 4 procedure → `kits/prd-creator/document/VALIDATION.md`;
- canonical complete mechanical PRD validation → `kits/prd-creator/validator/api.py`;
- project handoff state → `state/handoff-state.yaml`;
- compact document acceptance → `work/acceptance.md`;
- stable handoff/resume navigator → `output/README.md`;
- current versioned delivery bundle → `output/v<document.version>/{prd.html, context.md, index.json}`.

This foundation page does not maintain another Golden checklist, Production Asset checklist, or review matrix.

## Flow 4 sequence

```text
current canonical PRD core + current 04 source when present + current deterministic HTML
→ one canonical mechanical validation
→ one integrated Semantic Readiness review
→ semantic reconciliation
→ Material Conservation
→ targeted desktop visual sanity when the claim requires it
→ Critical/Major?
     yes → fix first wrong owner + recheck only invalidated scope
     no  → bind exact reviewed render-data SHA → development_ready / handoff_ready
```

## Proof boundaries

Mechanical validation proves deterministic repository/render facts only. It does not prove source fidelity, production-role completeness, 04 production-readiness semantics, material conservation, or visual readability.

There is one complete mechanical PRD validation API. Handoff may not call a lower-level subset and therefore may not disagree with normal PRD validation about content purity/freshness.

`Semantic Readiness` is the single persisted result for integrated semantic lenses such as New Reader, Level Designer, Developer, Production Assets when present, Content Purity, Project Consistency, and Golden Placement.

Production Assets readiness asks whether all real required resources are covered once, supported by authority, actionable, assigned to natural gameplay moments, free of disguised behavior/filler, exact where exact facts exist, readable by the production role, and additive without rewriting 01–03.

`Material Conservation` remains separate because a document can read clearly while accidentally omitting an independently actionable approved rule or required production resource.

`Visual sanity` remains separate because browser/render evidence is a different proof channel. Static HTML inspection cannot claim visual PASS.

A production role needing to reopen source to recover a material rule or required production resource that belongs in the document is a **Major** completeness failure.

## Acceptance identity

`document.version` is project/release metadata, not an edit counter. Therefore `handoff_ready` acceptance must also bind the exact reviewed `work/render-data.json` bytes:

```text
Accepted Render Data SHA256: <sha256>
```

If render-data changes—even under the same semantic version—the previous acceptance cannot authorize handoff until the affected semantic/mechanical review is refreshed and the new hash is recorded.

## Golden proof economy

The approved Golden prototype is owned by `CONTENT-CONTRACT.md`, `DESIGN-CONTRACT.md`, `renderer/CONTRACT.md`, exact reference bytes, and focused regression coverage.

For ordinary content-only or 04-only production, do not repeat full reverse Golden proof when template/CSS/JS/PRD-core visible grammar is unchanged. Adaptive child cardinality inside approved component families is not itself a Golden change.

Escalate to broader every-page/reference proof only when Golden/template/PRD-core composition changed, a targeted finding suggests a global defect, or the user explicitly requests broader proof.

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
Accepted Render Data SHA256: <sha256>
Findings: <only when findings exist>
```

Do not duplicate CI transcripts, role-by-role PASS fields, a separate 04 PASS field, or review prose when current owners already hold that evidence.

## Handoff boundary

Before Flow 5, `kits/prd-creator/validator/validate_handoff.py` confirms current canonical validation, exact acceptance revision binding, current versioned `prd.html` / `context.md` / `index.json`, handoff state, and `document.version` agree.

When 04 exists, `handoff_ready` also depends on integrated Semantic Readiness having applied the 04 readiness gate. Mechanical source freshness alone does not prove that 04 is professionally actionable.

`handoff_ready` means only that the accepted project document may be used as the current production reference/downstream Voice input. It does not mean client approval, implementation completion, gameplay QA, release approval, or completed Voice Production.

## Bounded revision

```text
approved change
→ affected truth/content/04 source/projection only
→ one deterministic full-file rerender
→ one canonical mechanical check
→ one integrated review of invalidated scope
→ refresh exact acceptance hash when accepted projection changed
→ visual check only where changed/high-risk
→ stop
```

Do not replay unchanged intake, unrelated packages, full Golden reverse proof, Voice tests, mobile QA, or every-page visual inspection for ceremony.
