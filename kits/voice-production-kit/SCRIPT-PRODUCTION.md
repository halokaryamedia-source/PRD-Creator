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
4. `SOUNDMAKER.md` — Eleven v3 preparation/generation procedure;
5. `references/elevenlabs/` — deep technical reference only when needed;
6. `DOCX-FORMAT.md` + Aftershock reference — presentation only.

Before asking the user, recover available facts from these owners. Ask only for unresolved material decisions that cannot be recovered safely.

Production technique may shape **how** approved meaning is performed. It may not create a new project fact, Voice ID, speaker, channel, trigger, mechanic, reward, or outcome.

## Flow 6 working modes

### Preparation Mode — default for script/DOCX work

Use when audio generation is not requested.

```text
all current Voice Requirements
→ draft each Voice ID with SoundMaker
→ project-level continuity / anti-repetition pass
→ canonical work/voice-production.md
→ derived DOCX when requested
```

Batch preparation is allowed. Do not force an audio-generation approval loop during this mode.

### Generation Mode — only when actual ElevenLabs work is requested

```text
one active Voice ID
→ exact reviewed prompt
→ generate / revise / approve
→ synchronize approved prompt back to canonical script
```

Actual generation remains one Voice ID at a time to preserve prompt/settings/evidence clarity.

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

## Per-line SoundMaker quality

Every entry must pass `SOUNDMAKER.md` pre-generation construction even in Preparation Mode:

```text
requirement meaning
→ duration first when specified
→ voice fit
→ performance map
→ spoken beats
→ punctuation / line structure / selective CAPS
→ minimal Audio Tags
→ pronunciation planning
```

Do not duplicate the detailed technique here.

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

## Project-level continuity pass

After per-line drafting, review the full requested scope before Flow 6 is ready.

Check:

- recurring speaker identity remains coherent;
- sequential information progresses rather than re-briefing the same facts;
- nearby lines do not accidentally reuse the same opening, beat chain, tag placement, CAPS climax, sentence rhythm, or closing pattern;
- structural variety does not change approved facts or invent personality;
- Main Story / active-play communication remain appropriately differentiated by function.

Intentional repetition is valid when it is part of the approved character, terminology, or gameplay feedback language.

## Duration

Every entry requires an `Estimated Duration` range. It remains an estimate until actual audio exists.

When timing matters, SoundMaker routes to `references/elevenlabs/v3-duration-planning.md` **before** final wording.

No audio evidence is required to prepare a reasonable estimate; use the documented fallback hierarchy honestly.

## Pronunciation planning

Preparation Mode identifies material pronunciation risk but does not pretend it is verified.

Use the smallest appropriate strategy:

```text
normal word → normal text
ambiguous number/acronym/symbol → explicit spoken form
unusual isolated proper noun → inline v3 IPA when needed
repeated project term → project note/dictionary when appropriate
actual approved audio → project-calibrated lock
```

## Actual generation / approval sync

When Generation Mode is requested:

1. use one active Voice ID;
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

Preparation Mode can finish without any generated audio when canonical wording exists for every required Voice moment, SoundMaker pre-generation quality and project-level continuity pass, mechanical parity passes, and requested derived artifacts are current.

Generated-audio quality, measured duration, and heard pronunciation remain separate evidence and are not prerequisites unless the user explicitly requests Generation Mode/audio delivery.
