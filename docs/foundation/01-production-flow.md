# Canonical Production Flow

Status: active architecture

```text
Flow 1  Repository Boot & Project Memory
Flow 2  Source Intake & Requirement Recovery
Flow 3  Project Document / PRD Generation
Flow 4  PRD Validation & Team Handoff
Flow 5  Voice Requirement Extraction
Flow 6  ElevenLabs Performance Script Production
Flow 7  Voice Validation & Delivery
```

## Flow ownership

- **Flow 1** — resume current repository/project state without asking the user to reconstruct it.
- **Flow 2** — preserve/triage source, recover production meaning, detect material gaps/conflicts, solve what can be resolved safely, and ask only the remaining material decisions.
- **Flow 3** — turn `ready_for_prd` meaning into canonical PRD content and deterministic **Golden hierarchy/page-composition HTML** without adding project meaning.
- **Flow 4** — distinguish generated PRD from development-ready PRD and create current acceptance/handoff evidence; missed product/design recovery returns to Flow 2.
- **Flow 5** — derive justified Voice requirements from the accepted PRD without inventing upstream facts.
- **Flow 6** — create canonical ElevenLabs performance wording + derived reference-styled DOCX while preserving Voice scope.
- **Flow 7** — validate the current Voice Requirements → Script → DOCX chain; actual audio is reviewed only when supplied/in scope.

There is no canonical Flow 8.

## Architecture rule

Fix the owning boundary instead of using downstream polish to compensate for unresolved upstream meaning. Derived artifacts may organize/represent canonical meaning but never become authority for it.

Detailed policy/procedure lives in the matching `docs/foundation/` and `kits/*` owner; this file is only the high-level sequence.
