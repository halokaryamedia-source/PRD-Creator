# Canonical Production Flow

Status: active architecture

```text
Flow 1  Repository Boot & Project Memory
Flow 2  Source Intake, Golden-Guided Completion & Preview
Flow 3  Project Document / PRD Generation
Flow 4  PRD Validation & Team Handoff
Flow 5  Voice Requirement Extraction
Flow 6  ElevenLabs Performance Script Production
Flow 7  Voice Validation & Delivery
```

## Flow ownership

- **Flow 1** — resume current repository/project state without asking the user to reconstruct it.
- **Flow 2** — preserve/triage source, recover production meaning, use the Golden fill map to identify required PRD-core detail, recover real Production Asset needs from the same project model, complete missing/conflicting material meaning with explicit AI proposals, then show one complete objective-by-objective Chat Preview and obtain user approval/corrections before `ready_for_prd`.
- **Flow 3** — turn preview-approved `ready_for_prd` meaning into canonical PRD-core content and deterministic **01–03 Golden hierarchy/page-composition HTML** without adding new project meaning.
- **Flow 4** — validate the current PRD plus any required materialized non-Voice 04 source as one accepted revision, then create development-ready or formal handoff evidence. Missed or newly exposed product/design meaning returns only the affected slice to Flow 2.
- **Flow 5** — derive justified Voice requirements from accepted `handoff_ready` project/PRD meaning without inventing upstream facts.
- **Flow 6** — create canonical Eleven v3 performance wording and publish its derived AUDIO resources into matching 04 gameplay moments while preserving Voice scope.
- **Flow 7** — validate the current Voice Requirements → Script → consolidated project-HTML chain; actual audio is reviewed only when present/in scope.

There is no canonical Flow 8. The Simple Chat Preview is the final user-facing checkpoint **inside Flow 2**, not a new flow or new artifact.

## Bounded 04 Production Assets completion

04 is a normal capability of PRD-Creator, not another numbered Flow.

The important authority shape is:

```text
project discussion + original source + approved decisions
→ complete approved project model
   ├─ PRD core 01–03
   └─ 04 Production Assets
```

Concrete Production Asset needs are recovered during the same Flow 2 understanding/completion pass. After approval, the system materializes the non-Voice 04 source in `work/asset-requirements.md` when real resources exist and merges canonical Voice data later when Voice exists.

Operational order when non-Voice 04 is required:

```text
Flow 2 approved project model
→ Flow 3 materialize PRD core 01–03
→ materialize work/asset-requirements.md from the same approved model
→ Flow 4 validate PRD + non-Voice 04 together
→ development_ready OR handoff_ready
→ Flow 5 only from handoff_ready when Voice is required
```

Do **not** use this as the normal design path:

```text
finished 01–03
→ reread generated document
→ brainstorm extra assets
→ invent 04
```

The 04 artifact may be written after PRD-core materialization, but its meaning comes from the same approved project model and must be present before Flow 4 acceptance when it is required for the current project scope.

## Proposal boundary

Flow 2 may create concrete gameplay/design/development proposals so the preview is complete. A proposal is not source truth and is not approved project authority until the user approves or corrects the preview.

The same rule applies to Production Assets: a necessary resource implication does not require a new approval layer, but a material choice that changes gameplay, story, player communication, scope, or another project fact must use the existing Proposal/approval boundary.

Golden/reference material tells Flow 2 **what questions the complete PRD core must answer**. It does not supply unrelated project facts or generic asset decoration.

## Architecture rule

Fix the owning boundary instead of using downstream polish to compensate for unresolved upstream meaning. Derived artifacts may organize/represent canonical meaning but never become authority for it. Pending Flow 2 proposals become authority only through user preview approval.

Detailed policy/procedure lives in the matching `docs/foundation/` and `kits/prd-creator/` domain owner; this file is only the high-level sequence.
