# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Complete **Phase 3 — Operating Parity Acceptance** by proving the BuildIT-style routing/ownership architecture in actual repository use without reopening completed Flow 1–7 production semantics.

## Current Status

`OPERATING_PARITY_PHASE_3_REPOSITORY_VERIFY_PENDING`

## Completed — Phase 1

- Plan / Developing / Maintenance mode routing;
- mandatory non-trivial `development-brief`;
- Build POV + Acceptance POV;
- 2–5 acceptance criteria + proof budget;
- frozen root `.agents/skills/` architecture:
  - `development-brief`;
  - `project-document-production`;
  - `voice-production`;
- skill activation matrix / skill map;
- agent flow + Developing flow.

## Completed — Phase 2

- module ownership map;
- source-authority map;
- Maintenance flow/template;
- review evidence lifecycle / review graph;
- durable-decision / coordinated-change threshold;
- context-boot baseline;
- production + operating validation matrix.

## Phase 3 Evidence Completed

Representative routes were exercised for:

- new/incomplete project → `development-brief` + `project-document-production` → Flow 2;
- PRD content/rendering change → Project Document semantic owner;
- Voice scope/script change → `development-brief` + `voice-production`;
- documentation/routing Maintenance.

The Maintenance run found a real defect: Project Document Generator's kit `SKILL.md` forced broad reading across Flow 2–4. The root correction is prepared as Flow-first routing plus a nearest `kits/project-document-generator/AGENTS.md`.

Nearest-owner decision:

- Project Document local `AGENTS.md` → justified and added;
- existing Voice local `AGENTS.md` → retained; no extra local layer.

Engineering-gate decision:

- add one small `Repository Verify` gate because current architecture depends on frozen skill/owner/navigation invariants and executable Python sources;
- do not add a broad testing/packaging framework;
- CI does not substitute for PRD semantic, HTML visual, DOCX visual, or generated-audio proof.

Canonical Phase 3 evidence:

`docs/knowledge/operations/operating-parity-acceptance.md`

Durable gate decision:

`docs/knowledge/decisions/operating-parity-gates.md`

## Preserved Boundaries

Phase 3 does not:

- change Project Document or Voice production meaning;
- add a new root skill;
- create another project state hierarchy;
- treat static CI as visual/audio acceptance;
- revive retired schemas/profiles/freeze/package architecture.

## Remaining Gate

The Phase 3 implementation must be committed to `Local`, then the first GitHub Actions **Repository Verify** run must pass before final `OPERATING_PARITY_ACCEPTED` status is recorded.

## Next Step

Observe the first **Repository Verify** run for the Phase 3 `Local` commit. If it fails, fix only the reported invariant/root owner; if it passes, record final operating-parity acceptance and return to normal project operation.
