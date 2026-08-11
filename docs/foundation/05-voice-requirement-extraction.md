# Voice Requirement Extraction

Status: active Flow 5 policy

## Purpose

Convert a Flow 4 accepted PRD revision into a traceable, minimal set of justified voice moments before any ElevenLabs performance writing begins.

Flow 5 exists to prevent two failure modes:

1. Voice Production inventing upstream gameplay/story facts because the PRD was incomplete.
2. Voice Production creating dialogue for every section simply because a reference project used voice there.

## Entry boundary

Normal entry requires `state/handoff-state.yaml: handoff_ready` for the same PRD revision being extracted.

The accepted handoff revision is the existing PRD `document.version`, recorded as `accepted_prd_version` in `handoff-state.yaml`. Before extraction, run:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

PASS means the handoff state is ready, its accepted version matches the current PRD version, and the existing canonical/render/HTML/acceptance/team-handoff paths are present. This is a lightweight lifecycle guard, not a new checksum chain.

Rendering success or `development_ready` alone is not the normal Flow 5 entry because the repository sequence explicitly finishes the concise team handoff before downstream production begins.

## Canonical owner

`work/voice-requirements.md` owns Flow 5 voice meaning.

`state/voice-state.yaml` owns current status/revision/next step only and must not duplicate the full requirement content.

## Extraction principles

- extract player-facing communication needs, not implementation events;
- each voice moment must have an approved speaker/channel and trigger;
- preserve official names, sequence, outcomes, rewards, and terminology;
- Main Story and Radio Communication are roles, not quotas;
- a gameplay package may have zero voice moments;
- Radio requires an approved remote communication channel;
- avoid duplicating complete objective instructions in radio;
- reject invented lore/mechanics/rewards/triggers;
- return missing high-impact decisions upstream.

## Standard voice functions

Main Story commonly owns:

- briefing;
- arrival;
- transition;
- reveal/state change;
- completion;
- reward;
- farewell.

Radio Communication commonly owns:

- warning;
- progress;
- urgency;
- encouragement;
- reminder;
- setback/recovery.

These are demonstrated patterns. They do not require every project to use every function.

## Completion statuses

- `voice_requirements_ready` — justified/traceable requirements are ready for Flow 6;
- `no_voice_required` — accepted upstream evidence justifies no voice production for the current scope;
- `needs_upstream_decision` — a material speaker/channel/trigger/story decision must return upstream;
- `blocked` — required source/evidence is unavailable;
- `pending_extraction` — extraction incomplete or stale after upstream revision.

## Flow 5 output boundary

Flow 5 may define **what must be communicated, by whom, through what channel, and at what approved trigger**.

It must not define final spoken wording, performance tags, emphasis, pause punctuation, estimated duration, ElevenLabs settings, or voice selection. Those belong to Flow 6.
