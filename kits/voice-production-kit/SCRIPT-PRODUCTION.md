# Eleven v3 Performance Script Production

Flow 6 converts approved Flow 5 Voice Requirements into canonical Eleven v3 wording and publishes that production content into the **same project HTML** as the accepted PRD. It does not add Voice scope or upstream project facts.

## Entry gate

Start only when `state/voice-state.yaml` has:

```yaml
status: voice_requirements_ready
```

The referenced Voice Requirements and accepted PRD revision must still be current.

## Authority

Use:

1. `work/voice-requirements.md` — Voice scope and required communication;
2. accepted `work/content.md` — project context only when the requirement does not already carry enough context;
3. current `work/voice-production.md` — canonical production wording/cast when revising;
4. `SOUNDMAKER.md` — Eleven v3 preparation/generation procedure;
5. matching `references/elevenlabs/` file only when deeper production technique is needed.

Production technique may shape **how** approved meaning is performed. It may not create a new project fact, Voice ID, Speaker, Channel, Trigger, mechanic, reward, or outcome.

# Working modes

## Preparation Mode — default

```text
Voice Requirements
→ Voice Intent Completeness / Performance Fill Map
→ SoundMaker authoring per Voice ID
→ Communication Conservation
→ integrated Voice Script Readiness
→ canonical work/voice-production.md
→ consolidated output/final.html
```

Batch preparation is allowed. Do not force audio generation/testing or per-line approval loops.

## Generation Mode — only when actual ElevenLabs work is requested

```text
one active Voice ID
→ actual actor voice selected
→ exact reviewed prompt
→ generate / revise / approve
→ synchronize approved prompt + actor selection to canonical production source
```

Generation remains one Voice ID at a time.

# Canonical `work/voice-production.md`

The canonical script owns the minimum stable production information needed downstream.

```text
# <Project> Voice Production
Version: <script version>
Source Voice Requirements: <revision/reference>

Voice Cast:
- <Speaker>: <selected ElevenLabs voice>

## 01. <Gameplay Section>

### <VOICE-ID> — <Title>
Type: <exact Flow 5 type>
Speaker: <exact Flow 5 speaker>
Estimated Duration: <range>

```performance
[<initial performance direction>]
<exact Eleven v3 text>
```
```

## Voice Cast

`Voice Cast` is optional during early Preparation Mode and appears **once**, before gameplay sections.

Use:

```text
Voice Cast:
- Foreman Brann: William Shanks - Rich and Deep
- Vex: <selected ElevenLabs voice>
```

Rules:

- store the selected ElevenLabs voice once per recurring Speaker;
- do not repeat commercial voice names in every Voice entry;
- do not invent a voice name merely to fill the field;
- if no voice is selected yet, the consolidated HTML may honestly show `Voice selection pending`;
- Generation Mode requires the actual intended voice to be selected before generation;
- changing actor voice is production configuration, not a PRD gameplay change.

## Entry fields

Every Voice entry still requires exactly:

- stable Voice ID + title;
- `Type`;
- `Speaker`;
- `Estimated Duration`;
- exact fenced `performance` block whose first non-blank line is at least one initial Audio/Performance Direction Tag.

`Type` and `Speaker` must match Flow 5.

Do not duplicate Channel, Trigger, Purpose, `Must communicate`, `Must not add/repeat`, source refs, Performance Fill Map reasoning, WPM math, voice-fit ratings, or QA notes into the canonical entry.

# Production presentation

## Primary human-facing output — same project HTML

`output/final.html` remains the one project document.

After `voice-production.md` exists, rerun the normal PRD renderer:

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

The renderer automatically composes:

```text
PRD core
+
Production Assets
└── Voice
```

The Voice pages are professional-only downstream views. They do not become a second PRD or Voice wording authority.

### Visible Voice contract

Each gameplay Voice section uses the same shell:

```text
Gameplay Order / objective title
→ accepted PRD package label + gameplay context
→ Voice line count + Primary Speaker
→ compact Voice Setup for that gameplay section
```

Each Voice line then shows:

```text
title
→ <accepted PRD package label> · Voice Line X/Y
→ Context = exact Flow 5 Trigger
→ Speaker + Estimated Duration as secondary metadata
→ exact Eleven v3 prompt with performance tags visually distinct
→ Copy Prompt
```

The developer-facing `Context` is derived directly from Flow 5 `Trigger`. Do **not** add a duplicate `Context` field to `voice-production.md` or rewrite the Trigger independently in Flow 6.

The copied text is **only** the exact canonical `performance` block.

Do not expose Flow 5 Purpose, `Must communicate`, `Must not add/repeat`, source refs, SoundMaker reasoning, WPM calculations, QA notes, or internal readiness fields in the HTML.

### Consolidated navigation

When Production Assets exists, the professional navigation uses:

```text
01 Overview
02 Gameplay Flow
03 Development
04 Production Assets
05+ gameplay/objective packages
```

The +1 package numbering is presentation-only in the consolidated HTML. It does not change PRD canonical meaning, package identity, or project version. If Production Assets is absent, the original PRD-core navigation/page numbering remains unchanged.

## DOCX — optional export

`output/Voice Production.docx` is no longer the default human-facing Voice artifact.

Build it only when a portable DOCX export is requested or materially useful:

```bash
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  workspace/active/<project>/output/Voice\ Production.docx \
  --requirements workspace/active/<project>/work/voice-requirements.md
```

DOCX remains derived presentation and never becomes a second wording authority.

# Authoring contract

Use `SOUNDMAKER.md` as the single operational quality procedure.

For each Voice ID:

1. complete Voice Intent from Flow 5;
2. honor authoritative Timing Constraint when present;
3. plan Estimated Duration when timing matters;
4. write the exact performance beginning with one deliberate initial direction tag;
5. add transition tags only for justified audible state changes;
6. run Communication Conservation;
7. mark script-ready only when the SoundMaker gate passes.

After all requested lines are ready, perform one integrated Voice Script Readiness review over Communication, Listener, Character, Performance, Timing, Continuity, and Operator clarity.

Do not create separate scorecards or persisted per-lens gates.

# Ordering

Gameplay sections follow the accepted project/gameplay order. Within a section, Voice entries follow their approved Trigger order.

The consolidated HTML uses this canonical order directly; the renderer does not reorder Voice production.

# First wrong owner

```text
project/gameplay/story fact
→ PRD authority

Voice moment / Speaker / Channel / Trigger / Purpose / required communication / authoritative timing truth
→ Flow 5 voice-requirements.md

wording / performance / Estimated Duration / actor-voice selection
→ Flow 6 / SoundMaker / voice-production.md

project HTML composition / objective shell / navigation defect with correct canonical sources
→ PRD renderer Production Assets compositor

optional DOCX-only defect
→ Voice DOCX builder

actual generated-audio-only defect
→ Generation Mode evidence/settings/voice
```

Do not repair upstream defects by complicating the prompt.

# Mechanical gate

Before `voice_script_ready`:

- every Flow 5 Voice ID appears exactly once;
- no extra Voice ID exists;
- `Type` matches Flow 5;
- `Speaker` matches Flow 5;
- title, Estimated Duration, and performance block are present;
- the first non-blank performance line contains at least one initial direction tag;
- no unresolved placeholder remains;
- no required fact is knowingly omitted;
- no new upstream fact is introduced;
- gameplay/Trigger order is coherent;
- Communication Conservation passes;
- integrated Voice Script Readiness passes.

When consolidated project HTML is present, validation also requires objective-shell parity, per-line position/context presentation, exact Flow 5 Trigger context, and exact canonical Copy payload parity.

`Voice Cast` may still contain an unselected voice during Preparation Mode, but actual generation cannot begin until the active Speaker's ElevenLabs voice is intentionally selected.

# Publish gate

After canonical wording changes:

```text
voice-production.md
→ rerender the same output/final.html
→ validate affected Voice scope
```

After presentation-only changes, rerender from the unchanged canonical PRD/Voice sources and validate the generated HTML; do not hand-patch `final.html`.

Do not create `voice-production.html` as another default output.

# Voice state

Keep the existing lifecycle schema. `docx` is optional presentation metadata, not a required canonical owner.

```yaml
flow: 6
status: voice_script_ready
source_prd_revision: <accepted PRD revision>
requirements: work/voice-requirements.md
script: work/voice-production.md
project_html: output/final.html
unresolved_upstream: 0
next_step: flow_7_voice_validation_delivery
```

Existing projects may still carry a `docx` path when that export exists.

# Stop gate

Preparation Mode stops when:

- every required Voice ID is script-ready;
- Communication Conservation passes;
- integrated Voice Script Readiness passes;
- canonical Voice Production is current;
- consolidated project HTML is rebuilt when project HTML delivery is in scope;
- material pronunciation risks are represented honestly;
- no generated-audio or measured-duration claim is made without evidence.

Stop after readiness. Do not add separate Voice HTML, asset manifests, settings databases, extra approval layers, or speculative hardening without a concrete defect.
