# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Operate the completed PRD + Voice Production pipeline under the accepted BuildIT-style agent operating architecture.

## Current Status

`BUILD_IT_STYLE_OPERATING_PARITY_ACCEPTED`

## Completed Production System

- Flow 1–7 implemented on permanent branch `Local`;
- The Clockwork Vault completed real Flow 2→7 integration proof;
- real DOCX blank-page defect was found by visual QA, fixed at the builder root, rebuilt, and revalidated;
- old `Production Document Builder/` was audited `SAFE_TO_DELETE` and removed from the live tree;
- generated audio remains a separate evidence dimension and is never inferred from script/DOCX quality.

## Completed Operating Architecture

### Phase 1 — Agent Routing + Skill Architecture

- Plan / Developing / Maintenance modes;
- mandatory non-trivial `development-brief`;
- Build POV + Acceptance POV;
- 2–5 acceptance criteria + proof budget;
- frozen root skills:
  - `development-brief`;
  - `project-document-production`;
  - `voice-production`;
- activation matrix + skill map;
- agent flow + Developing flow.

### Phase 2 — Ownership + Review + Maintenance + Proof Infrastructure

- module ownership map;
- source-authority map;
- Maintenance workflow/template;
- review graph / historical-evidence lifecycle;
- durable decision / coordinated-change threshold;
- context-boot baseline;
- production + operating validation matrix.

### Phase 3 — Operating Parity Acceptance

- representative Project Document and Voice routing scenarios passed;
- real Project Document broad-read routing defect found and corrected;
- nearest `kits/project-document-generator/AGENTS.md` added from evidence;
- existing Voice nearest `AGENTS.md` retained;
- narrow repository engineering gate implemented;
- first `Repository Verify` GitHub Actions run passed on commit `5970c47c15c8e9e83df185be7c5472e976739062`, run `31367001967`.

Canonical acceptance evidence:

`docs/knowledge/operations/operating-parity-acceptance.md`

## Current Operating Rule

```text
boot
AGENTS → CONTEXT → next-action
↓
mode
Plan | Developing | Maintenance
↓
smallest semantic owner
↓
Developing only: development-brief + at most one specialist
↓
smallest complete change
↓
minimum useful proof
↓
update only the canonical state/decision/review owner that actually changed
```

`Repository Verify` protects static repository invariants only. PRD semantic, HTML visual, DOCX visual, and generated-audio claims still require their own evidence.

## Preserved Boundaries

- no Phase 4 is created merely to continue parity work;
- no BuildIT MCP/Blockbench domain structure is copied into this repository;
- no new skill/module/workflow is added without a proved current ownership or repeatable-invariant need;
- `main` remains untouched unless explicitly requested.

## Next Step

Use the active pipeline on the **next real project**, starting at the smallest correct Flow (normally Flow 2 for new/incomplete source). Any future defect or architecture change must follow the accepted Plan / Developing / Maintenance routing and be evidence-driven.
