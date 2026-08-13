# Voice Requirement Extraction

Status: active Flow 5 policy

## Purpose

Convert a Flow 4 accepted PRD revision into a traceable, minimal set of justified Voice moments that are **complete enough for Flow 6/SoundMaker to author without inventing project meaning**.

Flow 5 exists to prevent three failure modes:

1. Voice Production inventing upstream gameplay/story facts because the PRD/requirement is incomplete.
2. Voice Production creating dialogue for every section simply because a reference project used Voice there.
3. Flow 6 reopening the full PRD or guessing listener/timing context because `voice-requirements.md` is too vague.

## Entry boundary

Normal entry requires `state/handoff-state.yaml: handoff_ready` for the same PRD revision being extracted.

Before extraction, run:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

PASS proves the current accepted handoff/revision paths are coherent. It does not replace semantic PRD acceptance.

If accepted PRD meaning changes later, reopen only affected Flow 5 Voice requirements before downstream production continues.

## Canonical owner

`work/voice-requirements.md` owns Flow 5 Voice meaning.

`state/voice-state.yaml` owns lifecycle status/revision/next step only and must not duplicate the requirement content.

## Extraction principles

- extract player-facing communication needs, not implementation events;
- every included moment must have approved Speaker, Channel, Trigger, Purpose, and required communication;
- preserve official names, sequence, outcomes, rewards, terminology, and authoritative timing truth when it materially constrains the asset;
- Main Story and Radio Communication are roles, not quotas;
- a gameplay package may have zero Voice moments;
- Radio requires an approved remote communication channel;
- avoid duplicating complete objective instructions in reminders/radio;
- reject invented lore/mechanics/rewards/triggers;
- return missing high-impact decisions upstream.

## Flow 5 → Flow 6 interface

A competent Flow 6 reader should be able to recover:

```text
communication job  ← Function + Purpose
listener state     ← Trigger + Channel
information load   ← Must communicate
listener outcome   ← Purpose
speaker owner      ← Speaker
hard timing truth  ← optional Timing Constraint
scope exclusions   ← Must not add/repeat
```

Field quality requirements:

- **Function** — primary communication job, not a performance tag.
- **Trigger** — concrete gameplay/story event/state; include the relevant player/listener condition when it materially affects delivery.
- **Purpose** — listener-facing result: what the player should know, do, understand, or acknowledge after the line.
- **Must communicate** — separate independently actionable facts into concise bullets where practical.
- **Must not add/repeat** — material scope, continuity, and anti-repetition guardrails.
- **Timing Constraint** — optional and authoritative only; use when accepted project meaning defines a hard line/window/sync constraint. Omit when none exists.

`Timing Constraint` is **not** Flow 6 `Estimated Duration`. Flow 5 must not invent production duration targets merely to make the interface look complete.

Performance Shape, Landing, final wording, Audio Tags, CAPS/punctuation, Target Voice Profile, selected ElevenLabs voice, Stability, Surface, Enhance settings, and production-estimated duration remain Flow 6 responsibilities.

## Standard Voice functions

Common functions include:

```text
briefing | arrival | transition | reveal | warning | progress | urgency
encouragement | reminder | setback_recovery | completion | reward | farewell
```

These are demonstrated communication patterns, not required quotas.

## Candidate/readiness rule

Keep a Voice moment only when it is player-facing, source-supported, tied to an approved Speaker/Channel/Trigger, useful at that moment, and non-duplicative without a distinct gameplay reason.

Set `voice_requirements_ready` only when each included moment is justified/traceable and the interface above is complete enough that SoundMaker can fill Voice Intent Completeness without making a product-level guess.

If a material Speaker/Channel/Trigger, listener state/outcome, required fact, result/reward, terminology/sequence, or authoritative timing rule remains unresolved and different answers would materially change the asset, return that issue upstream.

## Completion statuses

- `voice_requirements_ready` — justified/traceable requirements are ready for Flow 6;
- `no_voice_required` — accepted upstream evidence justifies no Voice production for current scope;
- `needs_upstream_decision` — a material project decision must return upstream;
- `blocked` — required evidence is unavailable;
- `pending_extraction` — extraction incomplete or stale after upstream revision.

## Output boundary

Flow 5 defines **what must be communicated, by whom, through what approved channel, at what trigger/state, for what listener-facing purpose, and any authoritative Voice/timeline constraint**.

It does not define final spoken wording, performance direction, Estimated Duration, ElevenLabs settings, or voice selection.
