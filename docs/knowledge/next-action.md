# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Adopt the useful repository/workflow architecture learned from BuildIT into the Project Document Generator + Voice Production Kit production system, one production flow at a time from upstream to downstream.

## Current Status

`FLOW_2_SOURCE_INTAKE_REQUIREMENT_RECOVERY_IMPLEMENTED`

## Completed Slice — Flow 2

Implemented:

- permanent `Local` development-branch policy; routine per-flow PRs are retired;
- pre-existing `Production Document Builder/` marked Archived rather than deleted;
- active Project Document Generator migrated to `kits/project-document-generator/`;
- immutable original-source rule;
- persistent `Source Inventory`, `Requirement Register`, and `Intake State` contract;
- traceable source provenance and source roles;
- conflict handling without silent newest-file assumptions;
- `Clarification / Completion / Proposal / Blocked` recovery classes;
- question economy: recover low-risk supported gaps first; ask only unresolved high-impact decisions;
- per-project Flow 2 workspace package contract;
- explicit `ready_for_prd` gate before Flow 3.

## Preserved Boundaries

Flow 2 intentionally does **not** redesign:

- canonical PRD content structure beyond what the current Project Document Generator already defines;
- approved HTML template presentation;
- objective-package rendering behavior;
- PRD development-readiness/team-handoff validation;
- Voice Production Kit implementation;
- voice requirement extraction or ElevenLabs scripting.

## Current Proof

- repository and active kit contain the Flow 2 contract;
- the active approved HTML template is byte-identical to the historical approved Golden Sample file by SHA-256;
- Archived builder remains preserved;
- no real project intake has yet exercised the new Flow 2 state end-to-end, so that remains `EXECUTION PROOF REQUIRED`.

## Next Step

Implement **Flow 3 — Project Document / PRD Generation**: audit and align canonical content generation, document hierarchy, template adaptation, and renderer behavior so a `ready_for_prd` requirement state can become a practical development-ready PRD without reintroducing the Archived builder's unnecessary ceremony.
