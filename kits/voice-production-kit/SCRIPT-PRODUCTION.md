# ElevenLabs Performance Script Production

Flow 6 converts approved Flow 5 voice requirements into final performance wording and a production-ready DOCX. It does not add new voice moments or upstream project facts.

## Entry gate

Start only when `state/voice-state.yaml` has:

```yaml
status: voice_requirements_ready
```

The referenced `work/voice-requirements.md` and accepted PRD revision must still be current. If the PRD or voice requirements changed, stop and re-open the owning upstream flow before scripting.

## Authority

Use this order:

1. `work/voice-requirements.md` — canonical voice-moment scope, speaker/channel/trigger/purpose, required facts, and guardrails;
2. accepted `work/content.md` — project context and official meaning;
3. `state/requirement-register.yaml` — requirement traceability when needed;
4. `output/team-handoff.md` — navigation/scope aid only;
5. `references/elevenlabs/README.md` — ElevenLabs production technique only when model/voice/performance/duration/pronunciation/generation guidance is in scope;
6. `DOCX-FORMAT.md` + `references/aftershock/README.md` — codified formatting/performance-quality reference contract based on the audited original DOCX.

The ElevenLabs reference may shape **how** approved meaning is performed. It may not supply a project fact, speaker, channel, trigger, Voice ID, reward, mechanic, or new communication moment.

Do not use the Aftershock script as a source of project facts, voice counts, wording, speakers, channels, or pacing quotas.

## Eleven v3 production routing

When the final script is intended for Eleven v3, or the user specifies an emotional-performance or duration target:

1. read `references/elevenlabs/README.md`;
2. open only the relevant supporting page:
   - wording/tags/punctuation/CAPS/long emotional arc → `references/elevenlabs/v3-performance-writing.md`;
   - target/max/fixed duration → `references/elevenlabs/v3-duration-planning.md`;
   - model/voice/settings/pronunciation/generation behavior → `references/elevenlabs/v3-production-reference.md`;
3. return to the canonical Flow 6 script owner.

Do not load the full research set by default.

## Canonical Flow 6 output

Create `work/voice-production.md`. This is the source of truth for final spoken wording and performance notation.

Use:

```text
# <Project> Voice Production
Version: <script version>
Source Voice Requirements: <revision/reference>

## 01. <Gameplay Section>

### <VOICE-ID> — <Title>
Type: Main Story | Radio Communication | <explicit supported type>
Estimated Duration: <range>

```performance
[clear performance direction]

Spoken text...
```
```

Every Flow 5 voice ID must appear exactly once unless upstream scope is explicitly reopened. Do not create additional IDs in Flow 6.

## Writing contract

For every entry:

1. satisfy the requirement's **Purpose**;
2. communicate every required `Must communicate` fact that belongs in this moment;
3. obey every `Must not add/repeat` guardrail;
4. preserve approved speaker, channel, trigger, names, terminology, sequence, mechanics, outcomes, and rewards;
5. write for natural spoken delivery rather than documentation prose;
6. remove implementation detail that the player would never need to hear;
7. avoid repeating another voice moment unless Flow 5 explicitly justified a distinct trigger/function.

If the requirement cannot be satisfied without inventing a fact, set the voice state to `needs_upstream_decision` and return the issue upstream.

## Main Story

Main Story may carry more context than Radio Communication. Use it for narrative briefing, arrival, transition, reveal, completion, reward, or farewell when the corresponding Flow 5 moment exists.

Prefer:

- clear spoken sentences;
- one communication purpose per entry;
- progressive information order;
- character-appropriate but restrained wording;
- enough context to understand the moment without narrating every implementation detail.

Do not turn a developer specification into dialogue.

## Radio Communication

Radio Communication must stay concise and useful during active play.

Prefer:

- immediate warning/actionable feedback;
- short progress acknowledgement;
- urgency or encouragement tied to the approved trigger;
- reminder/recovery wording that repeats only the minimum needed fact.

Do not repeat the full objective briefing. Do not add `[radio transmission]` or another radio effect unless that production direction is appropriate to the approved channel.

## Performance notation

For Eleven v3, follow the detailed production contract in `references/elevenlabs/v3-performance-writing.md`.

Default construction order:

```text
spoken wording
→ beat structure
→ punctuation / line breaks
→ selective CAPS
→ minimal performance tags
```

### Square-bracket directions

Use square brackets for concise audible performance direction, for example:

```text
[calm, practical]
[becoming serious]
[controlled urgency]
```

Directions describe how the line should be performed. They must not introduce a new event, action, sound effect, speaker, or project fact.

Use only as many direction changes as the performance needs. Avoid decorative, redundant, or contradictory tags.

### CAPS

Use selective CAPS only for words that genuinely need spoken emphasis.

Good:

```text
We MUST restore the beacon.
```

Avoid full-sentence CAPS or emphasizing every project term by default.

### Ellipses / punctuation

Use `...` for purposeful hesitation, transition, suspense, or weight. Standard punctuation and sentence boundaries should carry natural rhythm before extra tags are added.

Eleven v3 does not use SSML `<break>` tags for pause control.

### Line breaks

Use line breaks to support phrasing and beat structure. Do not treat a newline as an exact-duration pause command.

## Estimated duration

Every entry requires an `Estimated Duration` range. It is an estimate, not measured audio.

When timing matters, plan the word budget **before** final writing using `references/elevenlabs/v3-duration-planning.md`.

Estimate from the intended natural delivery of the spoken text, excluding bracketed performance directions. Account for purposeful pauses and the performance tone. Do not claim exact audio duration before generation/playback.

No fixed duration quota is inherited from Aftershock. Radio is normally shorter than Main Story because of its gameplay function, not because of a hard numeric rule.

## Section ordering

Keep gameplay sections in accepted project order. Within a section, order entries according to the approved trigger sequence, not by voice type merely for visual symmetry.

The final DOCX displays the explicit type before each entry, so Main Story and Radio moments can remain in the correct chronological order.

## Flow 6 mechanical gate

Before building DOCX:

- every Flow 5 voice ID appears exactly once;
- no extra voice ID exists;
- type matches the Flow 5 requirement;
- title, duration, and performance block are present;
- no `TBD`, `TODO`, `FIXME`, or `[OPEN]` placeholder remains;
- no required fact is knowingly omitted;
- no new upstream fact is introduced.

Then build:

```bash
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  workspace/active/<project>/output/Voice\ Production.docx \
  --requirements workspace/active/<project>/work/voice-requirements.md
```

## Voice state after Flow 6

Update the same `state/voice-state.yaml` lifecycle owner:

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

Allowed Flow 6 statuses:

- `script_drafting`
- `needs_upstream_decision`
- `voice_script_ready`
- `blocked`

`no_voice_required` from Flow 5 bypasses Flow 6; do not generate an empty DOCX merely to satisfy the pipeline.

## Flow 6 stop gate

Flow 6 stops when:

- canonical performance wording exists for every justified voice moment;
- the mechanical gate passes;
- `Voice Production.docx` is generated from the canonical script;
- the DOCX structure/layout is visually inspected during actual project production;
- voice state is `voice_script_ready`.

Do **not** claim final voice delivery, continuity approval, terminology/pronunciation approval, or generated-audio quality. Those belong to Flow 7.
