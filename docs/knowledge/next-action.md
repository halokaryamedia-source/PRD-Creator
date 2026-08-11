# Next Action

Updated: 2026-08-11

## Current Status

`PRD_HTML_REVISION_BOUND_NEXT_HANDOFF_BINDING`

Working branch: **`Local` only**.

## Completed current correction sequence

Flow 1 current-evidence ownership has been reconciled, and the audited PRD false-green chain is now protected through the generated HTML boundary:

```text
Flow 2 explicit ready state
↓
work/content.md
↓ canonical_content_sha256
work/render-data.json
↓ generated render-data-sha256 metadata
output/final.html
↓
Flow 4 mechanical validation
```

Current guards include:

- Flow 4 rejects missing/ambiguous/non-ready `state/intake-state.yaml`;
- `render-data.json` must match the exact current bytes of `work/content.md` through `canonical_content_sha256`;
- generated `final.html` must contain exactly one valid `render-data-sha256` marker matching the exact current bytes of `work/render-data.json`;
- stale HTML is rejected even when page IDs/composition remain unchanged;
- weighted scoring numeric/percentage-string totals remain enforced;
- bilingual user-visible text remains explicit EN/ID;
- wrapped Journey/Flow Golden-grid separator mechanics remain protected.

The HTML binding is intentionally narrow. It is not a generic artifact manifest/checksum framework and does not make generated HTML authoritative.

## Current proof

Latest implementation commit:

```text
8d177cea8e2119931c1a068ff6e924e47f60b490
```

GitHub evidence:

```text
Repository Verify #76 — PASS
Production Verify #33 — PASS
Project Document contracts — PASS
```

This is current repository/static/regression proof only. Per current user direction, do **not** run local/manual real-project or browser proof yet.

Historical The Clockwork Vault real-project proof remains historical evidence; it is not automatically proof of the latest repository revision.

## Deliberately not changed

- no generic artifact manifest or broad checksum framework;
- no semantic parser/comparison between arbitrary prose and generated HTML;
- no Flow 2 requirement-register/source-inventory consistency guard yet;
- no Voice Flow 5–7 changes in the HTML-binding slice;
- no mass renderer vocabulary refactor;
- no local/manual real-project or browser run.

## Next Step

Address the next concrete audited false-green boundary in **Flow 4 → Flow 5**: prevent an older `state/handoff-state.yaml: handoff_ready` from authorizing Voice Requirement Extraction after the accepted PRD revision has changed.

Use the smallest revision-consistency mechanism that can prove Flow 5 is entering from the same accepted PRD/handoff revision. Reuse existing `handoff-state.yaml`, `work/content.md`, `work/acceptance.md`, and `output/team-handoff.md` owners; do not introduce an artifact manifest, new lifecycle framework, or Voice-scope redesign.
