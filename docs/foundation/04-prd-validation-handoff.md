# Flow 4 — PRD Validation & Team Handoff

Status: active durable policy

## Purpose

Separate generated project documentation from production-ready documentation and preserve only the minimum revision-specific acceptance/handoff evidence needed for continuation.

## Canonical owners

- mandatory PRD-core meaning + Golden composition → `kits/prd-creator/document/CONTENT-CONTRACT.md`;
- bounded non-Voice 04 Production Asset requirement/writing contract → `kits/prd-creator/production-assets/CONTRACT.md`;
- detailed Flow 4 procedure → `kits/prd-creator/document/VALIDATION.md`;
- project handoff state → `state/handoff-state.yaml`;
- compact document acceptance → `work/acceptance.md`;
- stable handoff/resume navigator → `output/README.md`;
- current versioned delivery bundle → `output/v<document.version>/{prd.html, context.md, index.json}`.

This foundation page does not maintain another Golden checklist, Production Asset checklist, or review matrix.

## Flow 4 sequence

```text
current canonical PRD core + current 04 source when present + current deterministic HTML
→ one mechanical validation
→ one integrated Semantic Readiness review
→ Material Conservation
→ targeted desktop visual sanity when the claim requires it
→ Critical/Major?
     yes → fix first wrong owner + recheck only invalidated scope
     no  → development_ready / handoff_ready
```

## Proof boundaries

Mechanical validation proves deterministic repository/render facts only. It does not prove source fidelity, production-role completeness, 04 production-readiness semantics, material conservation, or visual readability.

`Semantic Readiness` is the single persisted result for the integrated semantic lenses:

```text
New Reader
Level Designer
Developer
Production Assets       # when 04 exists
Content Purity
Project Consistency
Golden Placement
```

When 04 exists, apply the readiness gate owned by `kits/prd-creator/production-assets/CONTRACT.md` inside this same review. Do **not** add a separate Production Assets PASS field, review file, workflow, or approval layer.

Production Assets readiness asks whether all real required resources are covered once, supported by authority, actionable, assigned to natural gameplay moments, free of disguised behavior/filler, exact where exact facts exist, readable by the production role, and additive without rewriting 01–03.

Do not persist a separate PASS field for every lens. They are questions inside one review, not independent workflow gates.

`Material Conservation` remains separate because a document can read clearly while accidentally omitting an independently actionable approved rule or required production resource.

`Visual sanity` remains separate because browser/render evidence is a different proof channel. Static HTML inspection cannot claim visual PASS.

A production role needing to reopen source to recover a material rule or required production resource that belongs in the document is a **Major** completeness failure.

## Golden proof economy

The approved Golden prototype is already owned by `kits/prd-creator/document/CONTENT-CONTRACT.md`, `kits/prd-creator/renderer/CONTRACT.md`, the exact reference bytes, and focused regression coverage.

For ordinary content-only or 04-only production, do **not** repeat a full reverse Golden proof when Golden template/CSS/JS/PRD-core visible composition/semantic slot contract is unchanged. Validate the current project against the existing contract and inspect only representative/high-risk rendered pages.

Escalate to broader every-page/reference proof only when the Golden/template/PRD-core composition contract changed, a targeted finding suggests a global defect, or the user explicitly requests broader proof.

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

Do not duplicate checksum tables, CI transcripts, role-by-role PASS fields, a separate 04 PASS field, or review prose when Git state/validators/current review already own that evidence.

## Handoff boundary

Before Flow 5, `kits/prd-creator/validator/validate_handoff.py` confirms that current accepted revision, canonical inputs, acceptance state, `output/README.md`, versioned `prd.html` / `context.md` / `index.json`, handoff state, and `document.version` agree.

When 04 exists, `handoff_ready` also depends on the integrated Semantic Readiness review having applied the `kits/prd-creator/production-assets/CONTRACT.md` readiness gate. Mechanical source freshness alone does not prove that 04 is professionally actionable.

`handoff_ready` means only that the accepted project document may be used as the current production reference / downstream Voice input. It does not mean client approval, implementation completion, gameplay QA, release approval, or completed Voice Production.

## Bounded revision

```text
approved change
→ affected truth/content/04 source/projection only
→ one deterministic full-file rerender
→ one mechanical check
→ one integrated review of invalidated scope
→ visual check only where changed/high-risk
→ stop
```

Do not replay unchanged intake, unrelated packages, full Golden reverse proof, Voice tests, mobile QA, or every-page visual inspection for ceremony.