# Flow 4 — PRD Validation & Team Handoff

Status: active durable policy

## Purpose

Separate a generated PRD from a production-ready PRD and preserve only the minimum revision-specific acceptance/handoff evidence needed for continuation.

## Canonical owners

- mandatory PRD meaning + Golden composition → `kits/project-document-generator/CONTENT-CONTRACT.md`;
- detailed Flow 4 procedure → `kits/project-document-generator/VALIDATION.md`;
- project handoff state → `state/handoff-state.yaml`;
- compact document acceptance → `work/acceptance.md`;
- human-facing handoff navigation/status → `output/team-handoff.md`.

This foundation page does not maintain another Golden checklist or another review matrix.

## Flow 4 sequence

```text
current canonical PRD + current deterministic HTML
→ one mechanical validation
→ one integrated Semantic Readiness review
→ Material Conservation
→ targeted desktop visual sanity when the claim requires it
→ Critical/Major?
     yes → fix first wrong owner + recheck only invalidated scope
     no  → development_ready / handoff_ready
```

## Proof boundaries

Mechanical validation proves deterministic repository/render facts only. It does not prove source fidelity, production-role completeness, material conservation, or visual readability.

`Semantic Readiness` is the single persisted result for the integrated semantic lenses:

```text
New Reader
Level Designer
Developer
Content Purity
Project Consistency
Golden Placement
```

Do not persist a separate PASS field for every lens. They are questions inside one review, not independent workflow gates.

`Material Conservation` remains separate because a document can read clearly while accidentally omitting an independently actionable approved rule.

`Visual sanity` remains separate because browser/render evidence is a different proof channel. Static HTML inspection cannot claim visual PASS.

A production role needing to reopen source to recover a material rule that belongs in the PRD is a **Major** completeness failure.

## Golden proof economy

The approved Golden prototype is already owned by `CONTENT-CONTRACT.md`, `RENDERING.md`, the exact reference bytes, and focused regression coverage.

For ordinary content-only production, do **not** repeat a full reverse Golden proof when template/CSS/JS/visible page composition/semantic slot contract is unchanged. Validate the current project against the existing contract and inspect only representative/high-risk rendered pages.

Escalate to broader every-page/reference proof only when the Golden/template/composition contract changed, a targeted finding suggests a global defect, or the user explicitly requests broader proof.

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

Do not duplicate checksum tables, CI transcripts, role-by-role PASS fields, or review prose when Git state/validators/current review already own that evidence.

## Handoff boundary

Before Flow 5, `validate_handoff.py` confirms that current accepted revision, artifact paths, acceptance state, handoff state, and `document.version` agree.

`handoff_ready` means only that the accepted PRD may be used as the current production reference / downstream Voice input. It does not mean client approval, implementation completion, gameplay QA, release approval, or completed Voice Production.

## Bounded revision

```text
approved change
→ affected truth/content/projection only
→ one deterministic full-file rerender
→ one mechanical check
→ one integrated review of invalidated scope
→ visual check only where changed/high-risk
→ stop
```

Do not replay unchanged intake, unrelated packages, full Golden reverse proof, Voice tests, mobile QA, or every-page visual inspection for ceremony.
