# Next Action

Updated: 2026-08-11

## Current Status

`PRD_FLOW1_4_CURRENT_PROJECT_PROOF_COMPLETE_NEXT_FLOW5_REQUIREMENT_COMPLETENESS`

Working branch: **`Local` only**.

## Completed PRD-side correction and proof sequence

The latest PRD Flow 1–4 audit is now closed through both static/regression evidence and one representative current real-project/browser proof:

```text
real authoritative source
↓
Flow 2 persisted source + requirement recovery
↓ ready_for_prd
work/content.md
↓ canonical_content_sha256
work/render-data.json
↓ current Golden renderer/template
output/final.html
↓ current mechanical validation
one integrated semantic review
↓ source-fidelity findings corrected at canonical owner
rerender + revalidate
↓ actual Chromium desktop/mobile sanity
work/acceptance.md
↓ document.version / accepted_prd_version
handoff_ready
↓ current handoff validator PASS
```

## Representative proof result

Representative source:

```text
Aftershock-Adventure-Map FINAL v2.4
Minecraft Bedrock / Minecraft Education
```

The local proof used exact current `Local` renderer/validator/template blobs and produced a complete gameplay PRD with:

```text
28 generated pages
7 Gameplay Flow pages
2 Global Development pages
6 Gameplay Packages
```

Final mechanical result:

```text
PASS
errors: 0
warnings: 0
```

Final integrated semantic acceptance:

```text
New Reader: PASS
Level Designer: PASS
Developer: PASS
Project Consistency: PASS
Critical: 0
Major: 0
```

Current handoff validation also passed current version `2.4`, artifact references, `handoff_ready`, and acceptance truth.

## What the real-project proof taught us

The first semantic pass found real source-fidelity omissions even though mechanical validation had already passed. The missing emphasis concerned Docks demonstration/feedback, Quarry scripted-deposit and optional-stretch boundaries, Ascent's expected harmless failure, Beacon idle/external-storm behavior, and shared guidance/permission rules.

Those findings were corrected in the representative project's requirement/content/projection owners and then rerendered. **No new PRD validator guard, schema, checksum, semantic engine, or framework was added.**

This confirms the intended split:

```text
deterministic defect → deterministic guard
source fidelity / production judgment → Flow 2 + Flow 4 semantic review
```

Do not convert the semantic findings from this one project into generic mechanical fields merely because they occurred once.

## Browser proof

The final exact `final.html` passed Chromium sanity at desktop `1440×1000` and mobile `390×844`:

- no console/page errors;
- no document-level horizontal overflow;
- Overview/sidebar and generated package navigation rendered correctly;
- Beacon package navigation and Gameplay/Level Design/Developer tabs worked;
- Terms disclosure worked;
- theme and Overview/Full Detail controls worked;
- desktop dense Developer table remained bounded;
- mobile dense table used internal scrolling without breaking document width;
- mobile off-canvas Menu opened correctly.

Sandbox policy blocked direct HTTP/file URL navigation, so the exact self-contained HTML was injected into Chromium with Playwright `set_content`. This proves current browser layout/interaction sanity, but not URL-origin/localStorage persistence across a real navigation/reload.

## Existing PRD boundaries remain unchanged

- Flow 2 requires real persisted `SRC-###` / `REQ-###` evidence and rejects only unambiguous current blockers.
- Required Golden hierarchy/content remains fail-closed at deterministic presence boundaries.
- Existing content→projection and projection→HTML SHA guards remain narrow; no hash chain was extended.
- Handoff continues to use `document.version`, `accepted_prd_version`, and compact acceptance truth.
- One representative project is not universal proof for every possible source shape.
- Further PRD architecture work requires another concrete defect.

## Repository proof anchors

The executable PRD contracts remain anchored by:

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

Current representative proof details are owned by `docs/foundation/validation-report.md`.

## Deliberately not changed

- no additional PRD guard after the representative proof;
- no generic YAML/schema or semantic-comparison framework;
- no extra checksum/manifest/revision registry;
- no project-specific AFTERSHOCK rule promoted into global validator policy;
- no Voice Flow 5–7 behavior changed yet.

## Next Step

Address the already-audited **Flow 5 — Voice Requirement Extraction completeness** boundary: require the existing documented requirement fields (`Function`, `Necessity`, `Purpose`, non-empty `Must communicate`, `Must not add/repeat`, and `Source refs`) at the executable parser boundary before Flow 6 can rely on a Voice requirement entry. Keep the change fail-closed and bounded; do not add a Voice schema framework, semantic similarity engine, automatic lore/mechanic inference, or checksum chain.
