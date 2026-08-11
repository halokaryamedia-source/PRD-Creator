# Next Action

Updated: 2026-08-11

## Current Status

`FLOW1_CURRENT_EVIDENCE_RECONCILED_NEXT_PRD_HTML_BINDING`

Working branch: **`Local` only**.

## Current PRD contract

- Golden Sample remains the required hierarchy, page-composition, component-language, and presentation authority.
- Normal PRD creation/revision is Production Execution; no `development-brief`.
- Flow 2 is the production-recovery/problem-solving stage, not only source extraction/provenance.
- Flow 3 receives resolved production meaning and must not silently decide material Flow 2 gaps.
- Flow 4 may expose missed recovery defects but returns new product/design choices to Flow 2.

## Flow 1 evidence correction completed

`docs/foundation/validation-report.md` is again aligned with its stated job as the current evidence owner.

The report now separates:

```text
current repository/static proof
≠ historical real-project proof
≠ current real-project/browser/DOCX/audio proof
```

The Clockwork Vault proof is preserved as historical evidence that Flow 1–7 was exercised on a real project. It is no longer presented as automatic `CURRENT-PROJECT VERIFIED` evidence for later repository revisions that were only checked through GitHub/static/CI.

The report also reconciles the earlier anti-overdevelopment decision with the later narrow `canonical_content_sha256` guard: the broad checksum/revision framework remains retired, while the single content→projection binding is documented as a concrete-defect exception rather than a restored framework.

No new evidence framework or semantic documentation validator was added in this slice.

## Current GitHub-side PRD safeguards

PRD production contracts currently protect these concrete cases:

- Flow 4 fails when `state/intake-state.yaml` is missing, ambiguous, or does not explicitly report both `status: ready_for_prd` and `ready_for_prd: true`;
- `render-data.json` carries `canonical_content_sha256`; Flow 4 rejects a missing/invalid binding or a projection left stale after `work/content.md` changes;
- weighted scoring accepts numeric values or numeric percentage strings, but every declared component weight must parse and weighted totals must equal 100;
- intentional EN + ID rendering requires explicit localized values for user-visible text instead of silently treating scalar English prose as Indonesian;
- Journey grids beyond six items and Flow grids beyond four items preserve wrapped-row separator mechanics.

These remain narrow guards for observed defects, not a generic document schema or semantic-comparison framework.

## Evidence boundary

The latest PRD correction work was performed through repository inspection and GitHub Actions only.

Current GitHub/static/CI evidence can prove repository routing, current documented contracts, renderer/validator regression behavior, and the explicit revision binding already implemented. It does **not** prove current real-project recovery quality, browser visual fidelity, DOCX visual quality, or generated-audio quality.

Per current user direction, **do not run local/manual real-project or browser proof yet**.

## Deliberately not changed in the Flow 1 repair

- no Flow 2 recovery mechanism changes;
- no renderer/validator behavior changes;
- no handoff-state gate changes;
- no Voice Flow 5–7 changes;
- no mass rename/refactor of inherited `quarry-*`/Aftershock renderer vocabulary;
- no generic content parser/schema or automatic semantic-comparison framework;
- no generalization beyond the current gameplay PRD document family.

## Next Step

Address the next concrete audited false-green boundary in **Flow 3 → Flow 4**: prevent an older `output/final.html` from validating against a newer `work/render-data.json` when page structure happens to remain unchanged. Use the smallest deterministic current-revision binding; do not add a generic artifact manifest, semantic parser, or broad checksum framework.