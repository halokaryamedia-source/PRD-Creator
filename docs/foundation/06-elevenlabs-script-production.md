# Eleven v3 Performance Script Production

Status: active Flow 6 policy

## Purpose

Flow 6 turns `voice_requirements_ready` into canonical Eleven v3 wording and, when needed, a derived `Voice Production.docx` without changing upstream Voice scope or project meaning.

## Ownership

```text
work/voice-requirements.md
→ Flow 6 / SoundMaker v3
→ work/voice-production.md
→ output/Voice Production.docx (derived)
```

- `work/voice-requirements.md` owns which Voice moments exist and what they must communicate.
- `SOUNDMAKER.md` owns Eleven v3 preparation/generation quality.
- `work/voice-production.md` owns final spoken/performance wording.
- DOCX is derived operator presentation and never editable content authority.

## Preparation Mode

Default when audio generation is not requested.

```text
Voice Requirements
→ Voice Intent Completeness
→ internal Performance Fill Map
→ SoundMaker writing
→ Communication Conservation
→ integrated Voice Script Readiness
→ canonical script / derived DOCX
```

The Performance Fill Map resolves communication job, listener state, information payload, listener outcome, speaker identity, timing envelope, performance shape, and landing. It is reasoning only; do not create another schema or artifact.

Communication Conservation ensures every material `Must communicate` fact survives wording polish and duration compression while `Must not add/repeat` remains binding.

Integrated Voice Script Readiness reviews Communication, Listener, Character, Performance, Timing, Continuity, and Operator clarity as one semantic decision rather than separate gates/scores.

Preparation Mode may process the full current Voice scope, may use a Target Voice Profile before actual voice selection, and requires no audio test or per-line approval loop.

## Generation Mode

Used only when actual ElevenLabs output is requested.

```text
one active Voice ID
→ one exact reviewed prompt
→ actual selected voice/settings
→ generate / feedback / approve
→ canonical sync
```

## Static output contract

Every canonical entry contains only:

```text
Voice ID + Title
Type
Speaker
Estimated Duration
exact Eleven v3 performance block
```

`Type` and `Speaker` match Flow 5.

Do not duplicate Channel, Trigger, Purpose, requirement bullets, source refs, Performance Fill Map reasoning, WPM calculations, voice-fit ratings, or QA notes into every canonical entry.

The DOCX presents only stable operator-useful information: `Type · Speaker`, Voice ID/Title, Estimated Duration, and Performance Script.

## Scope guard

Flow 6 may refine delivery but may not silently change Voice scope, Speaker/Channel/Trigger, gameplay/lore/mechanics/rewards/outcomes, or required communication.

Production interpretation such as sentence splitting, punctuation, CAPS, tags, and pacing may be decided by SoundMaker inside approved intent. An unresolved material creative/project decision returns upstream.

## First wrong owner / bounded revision

Fix the earliest owner actually wrong. Reopen only invalidated Voice IDs/speaker scope plus continuity materially affected by the change.

Do not replay unaffected Voice work for ceremony.

## Flow 6 gate

Set `voice_script_ready` only when:

- current Flow 5 status is `voice_requirements_ready` for the same accepted PRD revision;
- Voice ID, Type, and Speaker parity are intact;
- every entry has title, Estimated Duration, and canonical performance wording;
- Voice Intent Completeness is sufficient for responsible authoring;
- Communication Conservation passes;
- integrated Voice Script Readiness passes;
- no unresolved placeholder/upstream contradiction remains;
- requested derived artifacts are current.

Generated-audio quality is not a prerequisite unless the current task explicitly includes audio.

## Stop rule

Stop after current Preparation Mode scope is ready. Do not add optional tags, schemas, scores, artifacts, approval layers, or speculative hardening without a concrete defect.
