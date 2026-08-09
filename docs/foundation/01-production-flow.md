# Canonical Production Flow

Status: active architecture

## Flow 1 — Repository Boot & Project Memory

Purpose: make the repository independently resumable without relying on old chat context.

Status: implemented.

## Flow 2 — Source Intake & Requirement Recovery

Purpose: preserve incoming project source, record provenance/authority, recover requirements, expose conflicts, and ask only for real high-impact decisions.

Canonical owners:

- `docs/foundation/02-source-intake-recovery.md`;
- `kits/project-document-generator/SOURCE-INTAKE.md`;
- per-project Source Inventory, Requirement Register, and Intake State.

Status: implemented.

## Flow 3 — Project Document / PRD Generation

Purpose: turn `ready_for_prd` requirement state into canonical PRD content and render it through the approved presentation shell without introducing new project meaning.

Canonical owners:

- `docs/foundation/03-prd-generation.md`;
- `kits/project-document-generator/CONTENT-CONTRACT.md`;
- `kits/project-document-generator/RENDERING.md`;
- active renderer modules.

Status: implemented.

## Flow 4 — PRD Validation & Team Handoff

Purpose: distinguish generated PRD from development-ready PRD and issue a concise team handoff only for an accepted current revision.

Canonical owners:

- `docs/foundation/04-prd-validation-handoff.md`;
- `kits/project-document-generator/VALIDATION.md`;
- `kits/project-document-generator/validator/validate.py`;
- per-project `work/acceptance.md`, `state/handoff-state.yaml`, and `output/team-handoff.md`.

Acceptance uses:

```text
mechanical validation
+ New Reader
+ Level Designer
+ Developer
+ Project Consistency
```

Critical/Major findings block handoff. Mechanical pass alone never establishes semantic readiness.

Status: implemented at contract/tool level; first real-project handoff remains execution proof.

## Flow 5 — Voice Requirement Extraction

Purpose: derive justified voice moments from the accepted/mature project documentation without inventing upstream design facts.

This is the next active boundary.

## Flow 6 — ElevenLabs Performance Script Production

Purpose: produce natural Main Story / Radio Communication performance scripts with controlled ElevenLabs notation.

Current baseline was reviewed but is not yet migrated.

## Flow 7 — Voice Validation & Delivery

Purpose: validate terminology, coverage, pacing, hierarchy, and delivery state before voice production is declared complete.

Not yet implemented.

## Architecture Rule

Implement one flow boundary at a time. Do not change a downstream flow to compensate for an unresolved upstream contract.
