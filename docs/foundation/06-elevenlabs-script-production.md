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
- `SOUNDMAKER.md` owns one-entry-at-a-time Eleven v3 execution quality.
- `work/voice-production.md` owns final spoken/performance wording.
- DOCX is derived presentation and never becomes the editable content authority.

## Scope guard

Flow 6 may refine delivery but may not silently:

- create/drop/retype Voice IDs;
- change speaker/channel/trigger;
- introduce new gameplay/lore/mechanic/reward facts;
- turn Sound Effects into Voice scope;
- claim generated-audio quality without actual audio evidence.

Missing project meaning returns upstream.

## SoundMaker contract

Use `kits/voice-production-kit/SOUNDMAKER.md` for the operational quality procedure. Do not duplicate its detailed prompting rules here.

Durable requirements are:

- model scope is Eleven v3;
- target duration is planned before final wording when timing matters;
- voice fit is checked before attempting to compensate with more direction;
- spoken wording and beat architecture precede punctuation/CAPS/Audio Tags;
- flat writing is not repaired by tag stacking;
- exact approved generated wording synchronizes back into canonical `work/voice-production.md`;
- audio quality is established only from heard evidence.

## Generated prompt alignment

When actual generation occurs, the exact prompt used matters.

If the user or ElevenLabs UI changes the prompt before generation, that changed text is a new revision. After approval, synchronize the exact generated version into `work/voice-production.md` before claiming current script/DOCX/audio alignment.

## DOCX

The audited Aftershock Voice Production document remains the demonstrated presentation benchmark. `DOCX-FORMAT.md` owns the derived DOCX contract; project-specific Aftershock content/voice counts do not transfer.

## Flow 6 gate

Set `voice_script_ready` only when:

- current Flow 5 status is `voice_requirements_ready` for the same accepted PRD revision;
- Voice ID/Type parity is intact;
- every entry has title, Estimated Duration, and canonical performance wording;
- SoundMaker quality has been applied;
- no unresolved placeholders or known upstream contradictions remain;
- requested derived artifacts are rebuilt from canonical sources;
- required visual proof is complete when a visual-ready claim is made.

Flow 6 readiness does not prove generated-audio quality. Flow 7 owns current-revision acceptance.
