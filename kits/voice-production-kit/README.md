# Voice Production Kit v1.11.0

Repository-backed workflow for accepted PRD → Voice asset requirements → high-quality Eleven v3 production wording → **Production Assets inside the same project HTML**, with audio generation and DOCX export optional.

## Flow

```text
handoff_ready PRD
→ Flow 5 Voice Requirements
→ Flow 6 Preparation Mode
     Voice Intent Completeness
     → Performance Fill Map
     → SoundMaker writing
     → Communication Conservation
     → integrated Voice Script Readiness
→ canonical work/voice-production.md
→ rerender same output/final.html
     PRD core
     + Production Assets → Voice
→ Flow 7 validation/delivery
→ optional Generation Mode later
```

## Owners

- `VOICE-EXTRACTION.md` — which Voice assets are required by the accepted PRD;
- `SCRIPT-PRODUCTION.md` — canonical production/output lifecycle;
- `SOUNDMAKER.md` — Eleven v3 preparation/generation quality;
- `VOICE-VALIDATION.md` — Flow 7 readiness/evidence;
- `DOCX-FORMAT.md` — optional DOCX export only;
- `references/elevenlabs/` — deep v3 reference only when needed.

## Project authority

```text
PRD
= project/gameplay truth

voice-requirements.md
= what Voice assets must be produced

voice-production.md
= selected actor voice when known + exact text to produce

final.html → Production Assets → Voice
= human/operator presentation
```

The HTML is derived. It never becomes a second Voice wording authority.

## Flow 5 → Flow 6 interface

A Voice Requirement lets SoundMaker recover:

```text
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

Flow 5 does not pre-write dialogue or choose performance craft.

`Timing Constraint` is optional accepted source truth. `Estimated Duration` remains Flow 6 production planning.

## Canonical Voice Production

The canonical script may define Voice Cast once:

```text
Voice Cast:
- Foreman Brann: William Shanks - Rich and Deep
- Vex: <selected ElevenLabs voice>
```

Then gameplay-ordered entries use:

```text
### <VOICE-ID> — <Title>
Type: <Flow 5 type>
Speaker: <Flow 5 speaker>
Estimated Duration: <range>

```performance
[<initial performance direction>]
<exact Eleven v3 text>
```
```

Do not repeat actor voice names in every entry.

## Production Assets → Voice

The normal project renderer uses the same HTML:

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

If `work/voice-production.md` exists, the renderer appends a professional-only section after the PRD core.

Visible content stays intentionally simple:

```text
Voice Setup
selected ElevenLabs voice

01 Gameplay moment
Speaker · Estimated Duration
exact Eleven v3 text with visible performance-direction tags
Copy

02 Next gameplay moment
...
```

Scripts remain in gameplay/Trigger order. `Copy Text` copies only the exact performance block.

Do not display Flow 5 `Purpose`, `Must communicate`, `Must not add`, source refs, Performance Fill Map, WPM math, or QA notes in this operator view.

## Preparation Mode

Preparation Mode may prepare the full Voice scope without audio testing or per-line generation approval. Every standalone Voice ID begins with at least one deliberate initial performance-direction tag; extra transition tags are used only when the scene changes audibly.

An actor voice can remain unselected while a Target Voice Profile is sufficient for script preparation. The HTML honestly shows `Voice selection pending` rather than inventing one.

Actual Generation Mode requires the active Speaker's intended ElevenLabs voice to be selected.

## Generation Mode

```text
one Voice ID
→ actor voice selected
→ exact reviewed prompt
→ generate / feedback / approve
→ sync canonical production
→ rerender same final.html if changed
```

Default when no stronger project calibration exists:

```text
Model: Eleven v3
Stability: Natural
Surface: Speech Synthesis
Enhance: OFF on directed SoundMaker prompts
```

## Optional DOCX

Generate `output/Voice Production.docx` only when a portable export is requested or materially useful. It is not a prerequisite for normal project HTML Voice delivery.

## Validation

```text
Mechanical parity
+ Communication Conservation
+ integrated Voice Script Readiness
+ Project HTML Visual when claimed
+ optional DOCX Visual
+ optional Audio Evidence
```

Mechanical validation:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

When `final.html` exists, the validator checks current canonical prompt parity in the Production Assets Voice panels. When DOCX exists, it checks that optional export too.

## Revision discipline

Fix the first wrong owner and replay only invalidated scope.

A Voice-only wording/actor change rerenders the consolidated HTML but does not reopen PRD acceptance when PRD canonical meaning is unchanged.

## Stop rule

Stop when current Voice Production is ready and the requested consolidated output is current. Do not create a separate Voice HTML, asset manifest, settings database, generic asset framework, extra score system, or audio test requirement without a concrete need.
