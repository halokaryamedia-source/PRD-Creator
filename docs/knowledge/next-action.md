# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Adopt the useful repository/workflow architecture learned from BuildIT into the Project Document Generator + Voice Production system, one production flow at a time from upstream to downstream.

## Current Status

`FLOW_5_VOICE_REQUIREMENT_EXTRACTION_IMPLEMENTED`

## Completed Slice — Flow 5

Implemented:

- active repository-owned `kits/voice-production-kit/`;
- explicit `handoff_ready` PRD entry gate for normal downstream voice extraction;
- canonical `work/voice-requirements.md` voice-moment owner;
- revision/status owner `state/voice-state.yaml`;
- Main Story / Radio Communication / explicit source-defined other voice classification;
- functional classification for briefing, arrival, transition, reveal, warning, progress, urgency, encouragement, reminder, setback/recovery, completion, reward, and farewell;
- required/supporting necessity distinction;
- candidate and duplicate filters preventing redundant or unsupported voice;
- explicit rule that a package may have zero voice moments;
- explicit `no_voice_required` valid outcome;
- upstream return rule for missing speaker/channel/trigger/story decisions;
- original v1.0 script-writing instructions preserved as the Flow 6 baseline rather than executed early;
- active Voice Production Kit version advanced to 1.1.0.

## Preserved Boundaries

Flow 5 intentionally does **not** define:

- final spoken wording;
- square-bracket performance directions;
- CAPS emphasis;
- pause/line-break strategy;
- estimated duration;
- ElevenLabs voice/model/settings;
- final `Voice Production.docx` formatting;
- voice continuity/final delivery acceptance.

## Current Proof

- original Voice Production Kit source package was re-read before migration;
- original Aftershock gameplay/voice reference pair was re-inspected to verify the demonstrated functional split between Main Story and Radio Communication;
- Flow 5 contract/kit/state structure is implemented in the repository;
- no real project has yet exercised a full `handoff_ready` → voice-requirements extraction, so real-project execution remains `EXECUTION PROOF REQUIRED`;
- Aftershock binary/layout reference migration is deliberately deferred to Flow 6 because formatting/performance quality is not a Flow 5 concern.

## Next Step

Implement **Flow 6 — ElevenLabs Performance Script Production**: align the original v1.0 Voice Production instructions to consume `voice_requirements_ready`, migrate/reconcile the Aftershock production reference, define the final Voice Production document structure, and produce performance-ready wording without adding voice moments or upstream project facts outside Flow 5 scope.
