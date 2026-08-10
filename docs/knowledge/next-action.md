# Next Action

Updated: 2026-08-11

## Current Status

`PRD_PRE_SAMPLE_READY_BOOT_AND_PROCEDURE_CONTEXT_COMPACTED`

Working branch: **`Local` only**.

## Current PRD contract

- Golden Sample remains the required hierarchy, page-composition, component-language, and presentation authority.
- Normal PRD creation/revision is Production Execution; no `development-brief`.
- Source work uses inventory/authority-relevance triage before deep reading.
- Internal state is sparse but every non-default conflict/approval/blocker/supersession/readiness condition remains explicit.
- Artifacts are created by lifecycle: Core / Conditional / Derived / Downstream.
- Canonical content is completed before the main projection; bounded revisions patch only affected scope.
- Large Golden/generated HTML is consumed by renderer/validator runtime, not loaded into model context during normal production.
- Flow 4 uses one-read multi-lens review rather than four repeated document reads.

## Context-loading rule

Normal PRD work loads progressively:

```text
mandatory boot
AGENTS.md
→ CONTEXT.md
→ next-action.md

then only the smallest active owner
Flow 2 → SOURCE-INTAKE.md
Flow 3 → CONTENT-CONTRACT.md
Flow 4 → VALIDATION.md
```

`RENDERING.md`, kit `AGENTS.md`, `WORKFLOW.md`, ownership maps, and activation matrix are conditional references—not default context. The activation matrix is used only when ownership/skill routing is actually ambiguous.

## Efficiency boundary

Do not load or recreate information merely to appear thorough:

- no full Golden template/final HTML in model context during normal production;
- no repeated reading of unchanged project packages/source;
- no separate four-pass semantic review;
- no duplicated default YAML fields;
- no pre-created downstream artifacts;
- no duplicate policy/procedure stacks when one active owner is enough.

Quality boundaries remain unchanged: source authority, requirement traceability, Golden fidelity, role usability, scoring/completion correctness, mechanical validation, and truthful visual evidence.

## Do not add now

No source indexer/RAG/vector store, state-schema/artifact framework, new template/profile system, HTML schema, pixel/screenshot scoring, AI detector, generic parser, checksum/revision machinery, or `content.md → render-data.json` architecture rewrite without real evidence.

Handoff-state simplification remains deferred to the later PRD → Voice boundary review.

## Evidence boundary

This compaction changes routing/procedure text only; Golden template, renderer behavior, validator implementation, and production semantics are intentionally unchanged. Repository/Production Verify on the active implementation revision is the engineering proof. No real-project visual/usage test has been run yet for the fully refined system.

## Next Step

Run **one real project through Flow 2 → 4** as the first coherent practical sample. Measure actual user friction, context/source-reading cost, state/artifact overhead, Golden visual fidelity, and output usability; fix only defects demonstrated by that run.
