# Current Validation Status

Updated: 2026-08-14

This file records the **current evidence state only**. Historical debugging and superseded review detail remain in historical review files and Git history.

## Current system state

Working branch: `Local`.

Project Document Generator remains **v1.14.0**. Voice Production Kit remains **v1.11.2**.

Current delivery path:

```text
accepted PRD
→ asset discovery / production-implication check
→ optional work/asset-requirements.md
→ optional Voice canonical sources
→ one deterministic versioned delivery pass
→ output/README.md
→ output/v<document.version>/prd.html
→ output/v<document.version>/context.md
→ output/v<document.version>/index.json
```

`prd.html` remains the single human-facing project document. `context.md` and `index.json` are derived AI reading/navigation surfaces from the same accepted project truth; neither is another product authority. The Golden Sample remains the canonical PRD-core prototype. Production Assets is additive downstream presentation and does not change accepted PRD meaning, Golden bytes, or PRD page identity.

## Repository quality remediation

The full 2026-08-14 audit is preserved in `repository-quality-audit-2026-08-14.md`. RQ-01/RQ-15/RQ-16 are closed with real Clockwork validation; RQ-02/RQ-03/RQ-12 are closed by current-context synchronization and PRD CI coverage. Remaining findings are ordered in `../operations/backlog.md` and are not a bulk-refactor mandate.

## Versioned delivery proof

Current delivery contract:

```text
output/README.md                         stable resume entry point
output/v<document.version>/prd.html      human review
output/v<document.version>/context.md    AI semantic/development context
output/v<document.version>/index.json    compact navigation + context line ranges
```

Current mechanical evidence:

- versioned delivery contracts: 5/5 PASS;
- semantic `X.Y.Z` document version is required for handoff delivery;
- the delivery index is smaller than the full development context and points to exact context line ranges;
- handoff validation requires the current versioned PRD/context/index bundle to agree with `document.version`;
- repository routing now names `renderer/delivery.py` as the delivery orchestrator;
- current routing owners are guarded against returning to the retired unversioned delivery paths/taxonomy.

Clockwork is the first real migrated package at PRD version `1.0.0`:

```text
workspace/active/the-clockwork-vault/output/README.md
workspace/active/the-clockwork-vault/output/v1.0.0/prd.html
workspace/active/the-clockwork-vault/output/v1.0.0/context.md
workspace/active/the-clockwork-vault/output/v1.0.0/index.json
```

## Objective-first Production Assets proof

Current navigation contract:

```text
03 Development
   accepted global development navigation
   accepted gameplay/objective navigation

04 Production Assets
   Global / Shared Assets      # only when present
   <gameplay section title>
      <accepted PRD label>
```

Categories are page content, not sidebar nesting:

```text
3D Models
UI & Information
Audio
Visual Effects & Presentation
```

Only non-zero categories are rendered. The semantic contract also requires explicit asset discovery: necessary custom assets implied by accepted gameplay are not omitted merely because source material did not name them. Material choices that change project meaning use the existing Completion/Proposal process; production-only choices may use one practical recommendation without adding a new approval layer.

Current contract/mechanical evidence:

- Production Assets focused contracts: 7/7 PASS;
- Voice focused contracts: 8/8 PASS;
- a non-zero `Visual Effects & Presentation` fixture renders successfully;
- no-downstream PRD path remains a no-op;
- generic asset-only rendering works without Voice sources;
- generic + Voice content can share one objective-first page;
- unsupported/empty asset categories fail closed;
- Voice exact prompt/context parity remains enforced.

## Refreshed Production Assets browser proof

After RQ-05/RQ-13 changed Production Assets page identity/footer codes, the current Clockwork `v1.0.0/prd.html` was regenerated and inspected in actual headless Chromium layout at **1500×1000** and **1000×1000**. Every Production Assets navigation target became visible, every page exposed the expected `PA-##` footer code inside page bounds, Production Assets navigation had no horizontal overflow, the document had no horizontal viewport overflow, and the scanned Production Assets summary/card/Voice surfaces had no horizontal content overflow.

Result: `Production Assets visual sanity: PASS` for the RQ-05/RQ-13 identity change at the two claimed desktop widths. This proof does not broaden the claim to unrelated mobile widths or later visual changes.

## Browser proof

Existing objective-first browser proof remains PASS at 1500px and 1000px desktop widths for Clockwork and the earlier generic fixture, with no sidebar/card/page overflow and no zero-count category.

That earlier generic browser fixture did not contain a non-zero fourth category. Therefore no separate browser PASS is claimed for the exact longer `Visual Effects & Presentation` label; it is mechanically covered and should receive fresh visual proof only when a real project renders it or a visual defect is observed.

The versioned delivery/routing cleanup changed documentation, navigation ownership, and derived file locations only. It did not change the human PRD page composition, so no new browser PASS is claimed from that cleanup.

## The Circuit benchmark

The supplied completed Minecraft Bedrock `The Circuit v1.0.1.mcworld` was used only as a reference audit. It supported objective-first grouping, shared assets, function-based classification, primary-owner bundling, and the final four-category boundary. No The Circuit asset requirement, project package, or production output was generated.

## Current Clockwork state

Clockwork PRD remains `handoff_ready` and Voice remains `voice_delivery_ready` for the non-audio scope.

```text
PRD Version: 1.0.0
Mechanical: PASS
Voice Script Readiness: PASS
Communication Conservation: PASS
Project HTML Visual: PASS
Audio Evidence: not_provided
Critical: 0
Major: 0
```

Clockwork currently has no generic `work/asset-requirements.md`; no non-Voice Clockwork assets were invented merely to exercise the final taxonomy.

## Current project owners

```text
kits/project-document-generator/SOURCE-INTAKE.md
    production-completeness + implied-asset meaning check

kits/project-document-generator/PRODUCTION-ASSETS.md
    non-Voice objective-first asset discovery/category/requirement contract

kits/project-document-generator/renderer/delivery.py
    deterministic versioned human + AI handoff bundle

kits/project-document-generator/renderer/production_assets_objective.py
    deterministic objective-first Production Assets presentation mechanics

kits/voice-production-kit/
    Voice Flow 5–7 semantic/canonical ownership
```

No generated-audio review has been performed.

Current continuation is owned by `docs/knowledge/next-action.md`.
