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
- **Flow 2** — preserve/triage source, recover production meaning, use the Golden fill map to identify required detail, complete missing/conflicting material meaning with explicit AI proposals, then show one complete objective-by-objective Chat Preview and obtain user approval/corrections before `ready_for_prd`.
- **Flow 3** — turn preview-approved `ready_for_prd` meaning into canonical PRD content and deterministic **Golden hierarchy/page-composition HTML** without adding new project meaning.
- **Flow 4** — distinguish generated PRD from development-ready PRD and create current acceptance/handoff evidence; missed or newly exposed product/design meaning returns only the affected slice to Flow 2.
- **Flow 5** — derive justified Voice requirements from the accepted PRD without inventing upstream facts.
- **Flow 6** — create canonical ElevenLabs performance wording + derived reference-styled DOCX while preserving Voice scope.
- **Flow 7** — validate the current Voice Requirements → Script → DOCX chain; actual audio is reviewed only when supplied/in scope.

There is no canonical Flow 8. The Simple Chat Preview is the final user-facing checkpoint **inside Flow 2**, not a new flow or new artifact.

## Proposal boundary

Flow 2 may create concrete gameplay/design/development proposals so the preview is complete. A proposal is not source truth and is not approved project authority until the user approves or corrects the preview.

Golden/reference material tells Flow 2 **what questions the complete PRD must answer**. It does not supply unrelated project facts.

## Architecture rule

Fix the owning boundary instead of using downstream polish to compensate for unresolved upstream meaning. Derived artifacts may organize/represent canonical meaning but never become authority for it. Pending Flow 2 proposals become authority only through user preview approval.

Detailed policy/procedure lives in the matching `docs/foundation/` and `kits/*` owner; this file is only the high-level sequence.
