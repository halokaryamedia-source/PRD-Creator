# Eleven v3 Performance Script Production

Flow 6 converts approved Flow 5 Voice Requirements into canonical Eleven v3 wording and a production-ready DOCX. It does not add Voice scope or upstream project facts.

## Entry gate

Start only when `state/voice-state.yaml` has:

```yaml
status: voice_requirements_ready
```

The referenced Voice Requirements and accepted PRD revision must still be current.

## Authority

Use:

1. `work/voice-requirements.md` — Voice scope and required meaning;
2. accepted `work/content.md` — project context when needed;
3. current `work/voice-production.md` — canonical wording when revising;
4. `SOUNDMAKER.md` — one-entry-at-a-time Eleven v3 execution/quality procedure;
5. `references/elevenlabs/` — deep technical reference only when the active problem requires it;
6. `DOCX-FORMAT.md` + Aftershock reference — presentation only.

Production technique may shape **how** approved meaning is performed. It may not create a new project fact, Voice ID, speaker, channel, trigger, mechanic, reward, or outcome.

## Canonical Flow 6 output

Create/update `work/voice-production.md`:

```text
# <Project> Voice Production
Version: <script version>
Source Voice Requirements: <revision/reference>

## 01. <Gameplay Section>

### <VOICE-ID> — <Title>
Type: Main Story | Radio Communication | <explicit supported type>
Estimated Duration: <range>

```performance
<exact generation-ready Eleven v3 wording / performance notation>
```
```

Every Flow 5 Voice ID must appear exactly once unless Flow 5 is explicitly reopened.

## SoundMaker quality

For each entry, use `SOUNDMAKER.md`.

SoundMaker owns the operational path:

```text
requirement
→ duration when needed
→ voice fit
→ performance map
→ spoken beats
→ textual directing
→ minimal tags
→ pronunciation
→ generation setup
→ optional heard-audio diagnosis
```

Do not duplicate that detailed procedure here.

## Writing contract

Every entry must:

- satisfy its Flow 5 Purpose;
- communicate all required `Must communicate` facts that belong in the moment;
- respect `Must not add/repeat` guardrails;
- preserve approved speaker/channel/trigger/terminology/sequence/mechanics/outcomes/rewards;
- use natural spoken language rather than specification prose;
- omit implementation detail the player does not need;
- avoid unnecessary repetition of another Voice moment.

If required meaning cannot be written without inventing a fact, set `needs_upstream_decision` and return the issue upstream.

## Duration

Every entry requires an `Estimated Duration` range. It remains an estimate until actual audio exists.

When timing matters, SoundMaker routes to `references/elevenlabs/v3-duration-planning.md` **before** final wording.

## Actual generation / approval sync

Script/DOCX-only production does not require generated audio.

When actual ElevenLabs generation is part of the task:

1. work one Voice ID at a time;
2. present one best prompt;
3. use the exact reviewed prompt revision for generation;
4. if the user edits it before generation, that exact generated version supersedes the assistant draft;
5. after approval, synchronize it into `work/voice-production.md`;
6. rebuild/revalidate only affected derived scope if canonical wording changed.

Do not claim current script/audio alignment while canonical wording differs from the approved generated prompt.

## Section ordering

Keep gameplay sections in accepted project order. Within a section, order entries by approved trigger sequence.

## Flow 6 mechanical gate

Before building DOCX:

- every Flow 5 Voice ID appears exactly once;
- no extra Voice ID exists;
- Type matches Flow 5;
- title, Estimated Duration, and performance block are present;
- no `TBD`, `TODO`, `FIXME`, or `[OPEN]` placeholder remains;
- no required fact is knowingly omitted;
- no new upstream fact is introduced.

Build:

```bash
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  workspace/active/<project>/output/Voice\ Production.docx \
  --requirements workspace/active/<project>/work/voice-requirements.md
```

## Voice state after Flow 6

```yaml
flow: 6
status: voice_script_ready
source_prd_revision: <accepted PRD revision>
requirements: work/voice-requirements.md
script: work/voice-production.md
docx: output/Voice Production.docx
unresolved_upstream: 0
next_step: flow_7_voice_validation_delivery
```

Allowed statuses:

- `script_drafting`
- `needs_upstream_decision`
- `voice_script_ready`
- `blocked`

`no_voice_required` from Flow 5 bypasses Flow 6.

## Stop gate

Flow 6 stops when canonical wording exists for every justified Voice moment, SoundMaker quality has been applied, mechanical parity passes, required derived artifacts are rebuilt, and any requested current visual proof is complete.

Generated-audio quality and measured duration require actual audio evidence. Flow 7 owns current-revision acceptance.
