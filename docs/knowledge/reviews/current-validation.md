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

The full 2026-08-14 repository-quality / AI-Slop audit is preserved in `repository-quality-audit-2026-08-14.md`, so continuation does not depend on chat history.

Closed with current code/docs/proof:

- RQ-01 — Flow 4 resolves the versioned `prd.html`;
- RQ-02 — current semantic/procedure owners no longer teach retired unversioned HTML or separate Voice-sidebar routing;
- RQ-03 — decision history is explicitly separated from current routing;
- RQ-04 — every material AI-chosen Proposal is disclosed once before preview approval;
- RQ-05 — Production Assets uses distinct `PA-##` footer codes;
- RQ-06 — non-Voice Production Asset requirements have a bounded current-source freshness binding;
- RQ-07 — the retired Voice-only compositor path is removed;
- RQ-08 — validator monkey-patch ownership is removed without a wholesale rewrite;
- RQ-12 — the existing content-purity regression runs in `PRD Verify`;
- RQ-13 — Production Assets DOM IDs use stable semantic section identity;
- RQ-15 — Clockwork migration canonical-content binding is current;
- RQ-16 — Flow 4 preserves exact PRD-core order while accepting only valid additive Production Assets pages.

Remaining audit items are intentionally conditional/design-sensitive and stay in `../operations/backlog.md`: RQ-09/RQ-11 only with a concrete same-owner maintenance need, RQ-10 only after explicit Golden-design approval, and RQ-14 only when a real project can exceed the current page-letter range. They are **not** a bulk-refactor mandate.

## Verification economy audit

Observed CI history showed the repository-wide gate was the main avoidable cost: `Repository Verify` had run about **549** times on `Local`, while `PRD Verify` had about **51** runs and `Voice Verify` about **103** at the audit point. The root cause was structural: `Repository Verify` ran on every push, and both domain workflows watched whole kit directories even when the changed file could not affect the tested executable contract.

Current CI boundary:

- `Repository Verify` runs only for repository/routing/shared-engineering owners, not normal `workspace/active/**` project production or PRD/Voice Python already owned by domain gates;
- `PRD Verify` watches renderer, validator, Golden template, PRD test files, locked dependencies, and only the Flow 2 markdown owners that its tests explicitly assert;
- `Voice Verify` watches builder, validator, Voice test files, and dependency owners rather than every Voice documentation/reference file;
- all three workflows use `cancel-in-progress` concurrency, so rapid superseding commits do not need multiple complete runs;
- compile/unit suites themselves remain unchanged where relevant; no semantic, handoff, visual, DOCX, or audio proof requirement was removed.

This is a routing/usage optimization, not a reduction of correctness criteria. Browser/audio/runtime proof still runs only when the claim being made requires it.

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
- repository routing names `renderer/delivery.py` as the delivery orchestrator;
- current routing owners are guarded against returning to retired unversioned delivery paths/taxonomy;
- real Clockwork Flow 4 validates the exact 30-page PRD core plus valid additive Production Assets pages;
- real Clockwork handoff and Voice validation remain current after the remediation.

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

Current contract/mechanical evidence includes generic asset-only, Voice-only, mixed asset + Voice, no-downstream no-op behavior, unsupported/empty category rejection, exact Voice prompt/context parity, stable Production Assets semantic IDs, and non-Voice source-freshness rejection when stale.

## Refreshed Production Assets browser proof

After RQ-05/RQ-13 changed Production Assets page identity/footer codes, the current Clockwork `v1.0.0/prd.html` was regenerated and inspected in actual headless Chromium layout at **1500×1000** and **1000×1000**. Every Production Assets navigation target became visible, every page exposed the expected `PA-##` footer code inside page bounds, Production Assets navigation had no horizontal overflow, the document had no horizontal viewport overflow, and the scanned Production Assets summary/card/Voice surfaces had no horizontal content overflow.

Result: `Production Assets visual sanity: PASS` for the RQ-05/RQ-13 identity change at the two claimed desktop widths. This proof does not broaden the claim to unrelated mobile widths or later visual changes.

## Browser proof

Existing objective-first browser proof remains PASS at 1500px and 1000px desktop widths for Clockwork and the earlier generic fixture, with no sidebar/card/page overflow and no zero-count category.

The earlier generic browser fixture did not contain a non-zero fourth category. Therefore no separate browser PASS is claimed for the exact longer `Visual Effects & Presentation` label; it is mechanically covered and should receive fresh visual proof only when a real project renders it or a visual defect is observed.

The versioned delivery/routing cleanup changed documentation, navigation ownership, and derived file locations only. It did not change the human PRD page composition, so no visual claim is inferred from that cleanup alone.

## The Circuit benchmark

The supplied completed Minecraft Bedrock `The Circuit v1.0.1.mcworld` was used only as a reference audit. It supported objective-first grouping, shared assets, function-based classification, primary-owner bundling, and the final four-category boundary. No The Circuit asset requirement, project package, or production output was generated.

## Current Clockwork state

Clockwork PRD remains `handoff_ready` and Voice remains `voice_delivery_ready` for the non-audio scope.

```text
Mechanical: PASS
Voice Script Readiness: PASS
Communication Conservation: PASS
Project HTML Visual: PASS
Audio Evidence: not_provided
Critical: 0
Major: 0
```

No generated-audio review has been performed.

Current continuation is owned by `docs/knowledge/next-action.md`.
