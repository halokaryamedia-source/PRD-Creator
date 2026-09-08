# Flow 4 — PRD Validation & Team Handoff

Status: active durable policy

## Purpose

Separate generated documentation from an accepted production reference and preserve only revision-specific evidence required for continuation.

Detailed procedure and exact acceptance/state formats live in `kits/prd-creator/document/VALIDATION.md`. This page owns only durable boundaries.

## Canonical owners

- semantic PRD meaning → `document/CONTENT-CONTRACT.md`;
- Golden page/component grammar → `document/DESIGN-CONTRACT.md`;
- non-Voice 04 source → `production-assets/CONTRACT.md`;
- mechanical PRD validation → `validator/api.py`;
- minimal handoff identity → `state/handoff-state.yaml`;
- acceptance → `work/acceptance.md`;
- delivery → `output/README.md` + `output/v<version>/`.

## Sequence

```text
current Flow 2 requirement revision
+ current content/projection
+ required current non-Voice 04 source
+ deterministic HTML
→ canonical mechanical validation
→ semantic reconciliation/readiness
→ Material Conservation
→ visual sanity when claimed
→ bind exact reviewed bytes
→ development_ready | handoff_ready
```

There is one complete mechanical PRD validator. Handoff may not call a weaker validation subset.

## Proof boundaries

Mechanical validation proves repository/state/schema/freshness/composition facts. It does not prove semantic fidelity or browser visual quality.

`Semantic Readiness` is one integrated decision across source fidelity, production-role completeness, cross-role consistency, 04 readiness, and appropriate design placement.

`Material Conservation` stays separate because readable output can still omit an independently actionable rule/resource.

`Visual sanity` requires rendered/browser evidence when marked `PASS`.

## Exact acceptance identity

`document.version` is release/project metadata, not an edit counter. `handoff_ready` binds both current machine sources:

```text
Accepted Render Data SHA256: <current render-data SHA-256>
Accepted Asset Requirements SHA256: <current asset-requirements SHA-256 | none>
```

Changing either source invalidates prior acceptance even if the semantic version remains unchanged.

When no non-Voice 04 source exists, the second binding is exactly `none`.

## Minimal handoff state

`state/handoff-state.yaml` stores only the status and accepted PRD revision:

```yaml
status: handoff_ready
accepted_prd_version: <X.Y.Z>
```

Do not persist deterministic artifact paths in this state. The canonical paths are derived from project root + accepted revision, for example `work/render-data.json` and `output/v<X.Y.Z>/prd.html`.

Before Flow 5, `validator/validate_handoff.py` confirms:

- the canonical PRD validator still passes;
- accepted semantic version matches current render-data;
- canonical derived work/delivery artifacts for that revision exist;
- delivery metadata identifies the same revision;
- acceptance binds exact current render-data + non-Voice asset bytes.

`handoff_ready` means the document may be used as the current production reference/downstream Voice input. It does not mean client sign-off, implementation completion, gameplay QA, release approval, or completed Voice production.

## Bounded revision

```text
approved change
→ first wrong canonical owner
→ affected projection/04 source
→ deterministic rerender
→ canonical validation
→ review invalidated meaning only
→ refresh exact-byte acceptance
→ visual check only where changed/high-risk
→ stop
```

Do not replay unrelated intake/packages/Voice/Golden proof for ceremony.
