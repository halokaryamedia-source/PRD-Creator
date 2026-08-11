# Next Action

Updated: 2026-08-11

## Current Status

`PRD_FLOW1_4_STATIC_HARDENING_COMPLETE_NEXT_CURRENT_PROJECT_PROOF`

Working branch: **`Local` only**.

## Completed PRD-side correction sequence

The latest audit findings and final hierarchy contradiction pass for PRD Flow 1–4 are closed at the repository/static/regression level:

```text
Flow 2 intake declaration
↓ required persisted source + requirement evidence
↓ narrow current-blocker consistency
work/content.md
↓ canonical_content_sha256
work/render-data.json
↓ required Golden hierarchy/content + scoring/render contracts
↓ render-data-sha256
output/final.html
↓ Flow 4 mechanical + multi-lens acceptance
existing document.version
↓ accepted_prd_version + acceptance truth
handoff_ready
```

Current protections include:

- `state/intake-state.yaml` must explicitly report `status: ready_for_prd` + `ready_for_prd: true`;
- `state/source-inventory.yaml` and `state/requirement-register.yaml` must both exist and contain at least one stable `SRC-###` / `REQ-###` entry before readiness can pass;
- unambiguous current blockers fail readiness:
  - requirement `approval_status: pending`;
  - requirement `recovery_class: blocked`;
  - current source `inspection: blocked`;
- a source explicitly marked `status: superseded` does not block merely because its old inspection state is `blocked`;
- `evidence_status: conflict` alone remains allowed because the conflict may already have a valid higher-authority/approved resolution;
- the gameplay PRD hierarchy cannot silently collapse: at least one Gameplay Flow, one Global Development page, and one Gameplay Package are required;
- required Golden content presence is mechanically guarded: narrative presence, Gameplay Context/Main Objective/Result/player flow, Level Design overview/build requirement, Global Development overview/requirement, and Developer overview;
- numeric and percentage-string scoring weights render consistently with one `%`; unweighted scoring does not invent percentage markers;
- existing `content.md → render-data.json` and `render-data.json → final.html` SHA guards remain unchanged and narrow;
- Flow 4 → Flow 5 continues to use existing `document.version` / `accepted_prd_version`; no handoff SHA was added;
- `validate_handoff.py` requires `work/acceptance.md` to actually authorize `handoff_ready`: Mechanical and all four semantic lenses PASS, Critical/Major are zero, and Visual sanity is `PASS` or honestly `NOT PROVEN`;
- explicit `Visual sanity: FAIL` blocks handoff; `NOT PROVEN` is never upgraded into a visual claim;
- earlier bilingual display-text, scoring-total, generated-page/navigation, and wrapped Golden-grid guards remain active.

## Current proof

Final executable PRD-side proof anchor:

```text
3ccbf5196d3d3e4c173c440f0a2b5e0d2211a671
Repository Verify #104 — PASS
Production Verify #56 — PASS
Project Document contracts — PASS
```

Aligned canonical validation procedure:

```text
207f8c9e4aa0d0602b74c60c13c6c69fccdcc7e7
Repository Verify #105 — PASS
Production Verify #57 — PASS
```

These run numbers are proof anchors, not running state that documentation must chase after every later docs-only commit. Live GitHub Actions owns newer execution history.

This remains **repository/static/regression proof**. It does not prove current real-project recovery quality or current browser appearance.

## Explicit boundaries

- the bounded SRC/REQ entry reader is not a generic YAML parser/schema;
- required-hierarchy/content checks prove deterministic presence only, not semantic quality;
- `canonical_content_sha256` catches accidental stale projection but does not prove semantic equivalence between `content.md` and `render-data.json`;
- no new SHA/checksum, manifest, revision registry, semantic similarity engine, DOM snapshot, pixel comparison, or materiality classifier was added;
- no Voice Flow 5–7 behavior was changed in this correction sequence;
- no local/manual real-project or browser proof was run in this GitHub execution channel.

## Deliberately not changed

- no broad Flow 2 schema/completeness framework;
- no hash-chain extension beyond the two existing PRD mechanical boundaries;
- no automatic semantic acceptance;
- no generic renderer/profile framework;
- no Voice parser/builder/validator hardening yet;
- no claim that historical real-project proof validates the latest PRD changes.

## Next Step

Run **one representative current PRD Flow 2–4 production proof** before starting Voice hardening, including actual rendered/browser sanity when a suitable local/browser execution channel is available. Add no further PRD guard unless that current-project proof reveals a concrete defect.
