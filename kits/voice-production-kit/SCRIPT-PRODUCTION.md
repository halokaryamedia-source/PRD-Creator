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
5. `DOCX-FORMAT.md` + `REFERENCE/Aftershock/README.md` — codified formatting/performance-quality reference contract based on the audited original DOCX.

Do not use the Aftershock script as a source of project facts, voice counts, wording, speakers, channels, or pacing quotas.

## Canonical Flow 6 output

Create `work/voice-production.md`. This is the source of truth for final spoken wording and performance notation.

Use:

```text
# <Project> Voice Production
Version: <script version>
Source Voice Requirements: work/voice-requirements.md
Source Voice Requirements SHA-256: <current normalized-text SHA-256>

## 01. <Gameplay Section>

### <VOICE-ID> — <Title>
Type: Main Story | Radio Communication | <explicit supported type>
Estimated Duration: <range>

```performance
[clear performance direction]

Spoken text...
```
```

The SHA-256 line is mechanical revision identity, not project meaning. Compute it from the current UTF-8 text of `work/voice-requirements.md` using normalized text reading. The builder and Flow 7 validator must reject the script when this declared hash differs from the current requirements file.

Do not place the script hash in canonical prose. The builder computes the current script fingerprint during DOCX generation and stores both the requirements and script fingerprints in the derived DOCX core identifier.

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

Prefer clear spoken sentences, one communication purpose per entry, progressive information order, restrained character voice, and enough context to understand the moment without narrating every implementation detail.

Do not turn a developer specification into dialogue.

## Radio Communication

Radio Communication must stay concise and useful during active play.

Prefer immediate warning/actionable feedback, short progress acknowledgement, urgency/encouragement tied to the approved trigger, and concise reminder/recovery wording.

Do not repeat the full objective briefing. Do not add `[radio transmission]` or another radio effect unless that production direction is appropriate to the approved channel.

## Performance notation

### Square-bracket directions

Use square brackets for concise performance direction, for example:

```text
[calm, practical]
[becoming serious]
[radio transmission, controlled urgency]
```

Directions describe how the line should be performed. They must not introduce a new event, action, sound effect, speaker, or project fact.

### CAPS

Use selective CAPS only for words that genuinely need spoken emphasis. Avoid full-sentence CAPS or emphasizing every project term by default.

### Ellipses

Use `...` for purposeful hesitation, transition, suspense, or breathing room. Do not place ellipses after every sentence.

### Line breaks

Use short line breaks to support phrasing and breath. Do not break every few words merely to imitate the reference.

## Estimated duration

Every entry requires an `Estimated Duration` range. It is an estimate, not measured audio.

Estimate from intended natural delivery of the spoken text, excluding bracketed performance directions. Account for purposeful pauses and performance tone. Do not claim exact audio duration before generation/playback.

No fixed duration quota is inherited from Aftershock.

## Section ordering

Keep gameplay sections in accepted project order. Within a section, order entries according to the approved trigger sequence, not by voice type merely for visual symmetry.

The final DOCX displays the explicit type before each entry, so Main Story and Radio moments can remain in the correct chronological order.

## Flow 6 mechanical gate

Before building DOCX:

- `Source Voice Requirements SHA-256` matches the current `work/voice-requirements.md` text fingerprint;
- every Flow 5 voice ID appears exactly once;
- no extra voice ID exists;
- Type matches the Flow 5 requirement;
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

`--requirements` is required. Builder success mechanically proves current requirements hash parity + Voice ID/Type parity at build time and writes this derived DOCX revision identifier:

```text
voice-requirements-sha256=<requirements hash>;voice-script-sha256=<script hash>
```

The identifier is evidence for mechanical freshness only. It never makes the DOCX authoritative over the Markdown sources.

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

The state file remains lifecycle/status ownership. Do not duplicate the requirements/script SHA-256 contract into YAML merely to create another revision registry.

Allowed Flow 6 statuses:

- `script_drafting`
- `needs_upstream_decision`
- `voice_script_ready`
- `blocked`

`no_voice_required` from Flow 5 bypasses Flow 6; do not generate an empty DOCX merely to satisfy the pipeline.

## Flow 6 stop gate

Flow 6 stops when:

- canonical performance wording exists for every justified voice moment;
- the current requirements revision is mechanically bound to the canonical script;
- the mechanical gate passes;
- `Voice Production.docx` is generated from the current canonical script and carries the current requirements + script revision identifier;
- the DOCX structure/layout is visually inspected during actual project production;
- voice state is `voice_script_ready`.

Do **not** claim final voice delivery, continuity approval, terminology/pronunciation approval, or generated-audio quality. Those belong to Flow 7.
