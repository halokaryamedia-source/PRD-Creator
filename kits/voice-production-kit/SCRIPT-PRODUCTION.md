# Eleven v3 Performance Script Production

Flow 6 converts approved Flow 5 Voice Requirements into final Eleven v3 performance wording and a production-ready DOCX. It does not add new Voice moments or upstream project facts.

## Entry gate

Start only when `state/voice-state.yaml` has:

```yaml
status: voice_requirements_ready
```

The referenced `work/voice-requirements.md` and accepted PRD revision must still be current. If the PRD or Voice Requirements changed, stop and re-open the owning upstream flow before scripting.

## Authority

Use this order:

1. `work/voice-requirements.md` — canonical Voice scope, speaker/channel/trigger/purpose, required facts, and guardrails;
2. accepted `work/content.md` — project context and official meaning;
3. current `work/voice-production.md` — existing canonical wording when revising;
4. `SOUNDMAKER.md` — one-entry-at-a-time Eleven v3 quality/execution procedure;
5. `references/elevenlabs/README.md` — Eleven v3 production technique;
6. `DOCX-FORMAT.md` + `references/aftershock/README.md` — DOCX presentation reference only.

Production references may shape **how** approved meaning is performed. They may not supply a project fact, speaker, channel, trigger, Voice ID, reward, mechanic, or new communication moment.

## SoundMaker execution profile

Every Flow 6 entry uses the SoundMaker quality order internally:

```text
requirement fidelity
→ target duration first when specified
→ voice-fit check
→ performance map
→ spoken wording
→ beat architecture
→ punctuation / line structure
→ selective CAPS
→ minimal Audio Tags
→ pronunciation safety
→ one generation-ready prompt
```

For a real one-line production/revision task, read `SOUNDMAKER.md` and only the relevant supporting v3 reference.

SoundMaker is not a separate wording authority. Its final prompt is written into the matching `work/voice-production.md` entry.

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
[concise audible direction when needed]

Spoken text...
```
```

Every Flow 5 Voice ID must appear exactly once unless Flow 5 scope is explicitly reopened. Do not create additional IDs in Flow 6.

## Writing contract

For every entry:

1. satisfy the requirement's **Purpose**;
2. communicate every required `Must communicate` fact that belongs in this moment;
3. obey every `Must not add/repeat` guardrail;
4. preserve approved speaker, channel, trigger, names, terminology, sequence, mechanics, outcomes, and rewards;
5. write natural spoken language, not documentation prose;
6. remove implementation detail the player never needs to hear;
7. avoid repeating another Voice moment unless Flow 5 justified a distinct trigger/function.

If the requirement cannot be satisfied without inventing a fact, set the Voice state to `needs_upstream_decision` and return the issue upstream.

## Performance quality contract

Detailed rules live in `SOUNDMAKER.md` and `references/elevenlabs/v3-performance-writing.md`.

Default construction order:

```text
spoken wording
→ beat structure
→ punctuation / line breaks
→ selective CAPS
→ minimal performance tags
```

### Emotional movement

For long-form narration, create performance changes only when the scene or communication function changes. Prefer a real arc such as:

```text
establish
→ reveal
→ react
→ escalate
→ instruct
→ payoff
```

Do not assign one global emotional tag to a long script that contains several real state changes. Do not manufacture emotion changes when the scene is actually stable.

### Punctuation / CAPS / line structure

Use punctuation semantically. Ellipses, em dashes, questions, exclamations, sentence boundaries, and line breaks shape rhythm but are not exact timing controls.

Use CAPS selectively for words that genuinely need stress.

### Audio Tags

Use audible directions only. Default to 0–1 tag at a beat; two are valid when they control distinct compatible dimensions. Triple stacks are exceptional. Do not use redundant or contradictory tag stacks.

Eleven v3 does not use SSML `<break>` tags for pause control.

### Reactions

Treat sighs, gasps, laughs, gulps, hesitation, and similar reactions as timeline events rather than decorative tag clusters.

## Duration contract

Every entry requires an `Estimated Duration` range. It is an estimate, not measured audio.

When timing matters, plan the word budget **before** final wording using `references/elevenlabs/v3-duration-planning.md`.

Do not finish an oversized script and try to force it under a cap with `[rushed]`, tag spam, or extreme speed changes.

If approved audio exists for the same project/voice/performance family, project-calibrated duration evidence is stronger than generic WPM planning.

## Actual generation / approval sync

Script/DOCX-only production does not require generated audio.

When actual ElevenLabs generation is part of the task:

1. work one Voice ID at a time;
2. show one best v3 prompt;
3. wait for `APPROVED` or specific feedback before moving to the next active line;
4. if the user edited the prompt before generation, the exact prompt actually used supersedes the assistant draft;
5. synchronize the exact approved prompt back into `work/voice-production.md`;
6. rebuild DOCX and reopen affected Flow 7 acceptance if canonical wording changed after an earlier ready state.

Do not keep a different generated prompt and canonical script while claiming current alignment.

## Section ordering

Keep gameplay sections in accepted project order. Within a section, order entries by approved trigger sequence, not voice type for visual symmetry.

## Flow 6 mechanical gate

Before building DOCX:

- every Flow 5 Voice ID appears exactly once;
- no extra Voice ID exists;
- Type matches Flow 5;
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

`no_voice_required` from Flow 5 bypasses Flow 6.

## Flow 6 stop gate

Flow 6 stops when:

- canonical performance wording exists for every justified Voice moment;
- SoundMaker pre-generation quality has been applied to the wording;
- the mechanical gate passes;
- `Voice Production.docx` is generated from canonical script when DOCX is in scope;
- current project DOCX is visually inspected during actual production.

Do **not** claim generated-audio quality or measured duration without actual audio evidence. Flow 7 owns final current-revision acceptance.
