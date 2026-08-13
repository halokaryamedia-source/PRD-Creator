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
- DOCX is derived operator presentation and never becomes editable content authority.

## Flow 6 modes

### Preparation Mode

Default for script/DOCX production when audio generation is not requested.

- full current Voice scope may be prepared in one pass;
- each Voice ID receives SoundMaker pre-generation quality;
- run project-level speaker continuity / information progression / anti-template review;
- actual commercial voice selection may wait when a Target Voice Profile is sufficient;
- duration/pronunciation remain planned evidence;
- no audio test or per-line approval loop is required.

### Generation Mode

Used only when actual ElevenLabs output is requested.

- one active Voice ID;
- one exact reviewed prompt;
- actual selected voice/settings;
- feedback/approval loop;
- approved generated wording synchronizes back into canonical script.

## Static output contract

Every canonical Flow 6 entry contains only:

```text
Voice ID + Title
Type
Speaker
Estimated Duration
exact Eleven v3 performance block
```

`Type` and `Speaker` must match Flow 5.

Do not duplicate Channel, Trigger, Purpose, requirement bullets, source refs, WPM calculations, performance maps, voice-fit ratings, or QA notes into every canonical entry.

The generated DOCX presents only stable operator-useful information:

```text
Type · Speaker
Voice ID — Title
Estimated Duration
Performance Script
```

A separate operator handoff file is not required by default. A compact handoff can be derived from current authority and should expose shared speaker/voice/settings once plus the exact active prompt.

## Scope guard

Flow 6 may refine delivery but may not silently:

- create/drop/retype Voice IDs;
- change Speaker/Channel/Trigger;
- introduce gameplay/lore/mechanic/reward facts;
- turn Sound Effects into Voice scope;
- claim generated-audio quality without actual audio evidence.

Missing project meaning returns upstream. Existing project authority must be checked before asking the user.

## SoundMaker contract

Use `kits/voice-production-kit/SOUNDMAKER.md` for the operational procedure. Do not duplicate detailed prompting rules here.

Durable requirements are:

- model scope is Eleven v3;
- target duration is planned before final wording when timing matters;
- voice requirements/fit are considered before compensating with more direction;
- spoken wording/beat architecture precede punctuation/CAPS/Audio Tags;
- flat writing is not repaired by tag stacking;
- Preparation Mode includes cross-line continuity/anti-template review;
- exact approved generated wording synchronizes back into canonical `work/voice-production.md` when Generation Mode occurs;
- audio quality is established only from heard evidence and is optional unless requested.

## DOCX

The audited Aftershock Voice Production document remains the demonstrated presentation benchmark. `DOCX-FORMAT.md` owns the derived DOCX contract; project-specific Aftershock content/voice counts do not transfer.

## Flow 6 gate

Set `voice_script_ready` only when:

- current Flow 5 status is `voice_requirements_ready` for the same accepted PRD revision;
- Voice ID, Type, and Speaker parity are intact;
- every entry has title, Estimated Duration, and canonical performance wording;
- per-line SoundMaker quality and project-level continuity review were applied;
- no unresolved placeholders or known upstream contradictions remain;
- requested derived artifacts are rebuilt from canonical sources;
- required visual proof is complete when a visual-ready claim is made.

Flow 6 readiness may legitimately have `audio_evidence: not_provided`. Generated-audio quality is not a prerequisite unless the current task explicitly includes audio.
