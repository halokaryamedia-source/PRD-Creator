# Voice Production Kit v1.11.2

Repository-backed workflow for accepted PRD → Voice asset requirements → Eleven v3 production wording → **Production Assets inside the same project HTML**. DOCX and audio remain optional downstream scopes.

## Flow

```text
handoff_ready PRD
→ Flow 5 Voice Requirements
→ Flow 6 Preparation
   Voice Intent Completeness
   → SoundMaker writing
   → Communication Conservation
   → Voice Script Readiness
→ canonical work/voice-production.md
→ rerender same output/final.html
   PRD core
   + Production Assets → Voice
→ Flow 7 validation/delivery
```

## Owners

- `VOICE-EXTRACTION.md` — which Voice assets are required by the accepted PRD;
- `SCRIPT-PRODUCTION.md` — canonical script/output lifecycle;
- `SOUNDMAKER.md` — Eleven v3 writing/performance procedure;
- `VOICE-VALIDATION.md` — Flow 7 readiness/evidence;
- `DOCX-FORMAT.md` — optional DOCX export only.

## Authority

```text
accepted PRD
= project/gameplay truth

work/voice-requirements.md
= Voice asset scope + Trigger/Purpose/required communication

work/voice-production.md
= exact production wording + Estimated Duration + Speaker parity

output/final.html → Production Assets → Voice
= derived developer/operator presentation
```

The HTML is derived. It never becomes a second Voice wording authority.

## Canonical Voice Production

The script may define shared production setup once before gameplay sections. Each Voice entry then requires:

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

`Type` and `Speaker` must match Flow 5. Do not duplicate Trigger, Purpose, requirement bullets, source refs, reasoning, or QA fields into every canonical Flow 6 entry.

## Production Assets → Voice

The normal project renderer uses the same HTML:

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

Production Assets **extends the accepted PRD navigation**. It does not rebuild Development or renumber PRD pages.

```text
03 Development
   global development pages
   gameplay/objective sections

04 Production Assets
   VOICE
   <gameplay section title>
   <accepted PRD package label>
```

`VOICE` appears once. Each link shows the section title plus its accepted PRD label (`Introduction`, `Objective N`, `Ending`, or the project's actual label). Sidebar labels wrap naturally instead of being truncated.

Each Voice section page shows:

```text
Voice Production
→ gameplay section title
→ accepted PRD package label + gameplay context
→ Voice line count + Primary Speaker
→ compact Voice Setup
```

Each Voice line shows:

```text
title
→ <PRD package label> · Voice Line X/Y
→ Context = exact Flow 5 Trigger
→ Speaker · Estimated Duration
→ exact Eleven v3 prompt
→ Copy Prompt
```

The developer-facing Context is the existing Flow 5 Trigger projected into HTML; it is not a new Flow 6 field. `Copy Prompt` copies only the exact canonical `performance` block.

Do not display Flow 5 Purpose, `Must communicate`, `Must not add/repeat`, source refs, SoundMaker reasoning, WPM math, or QA notes in this operator view.

## Preparation boundary

Preparation may process the full current Voice scope without audio evidence. Every standalone Voice ID begins with at least one deliberate initial performance-direction tag; extra transition tags are used only when the scene changes audibly.

## Optional DOCX

Generate `output/Voice Production.docx` only when a portable export is requested or materially useful. It is not a prerequisite for normal project-HTML Voice delivery.

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

When `final.html` exists, validation requires:

- accepted PRD navigation/page identity is preserved;
- one Production Assets Voice category exists;
- section link title/package-label parity exists;
- objective shell/page count matches canonical Voice sections;
- line-position/context presentation exists for every canonical Voice entry;
- visible developer Context preserves the exact Flow 5 Trigger;
- hidden Copy source preserves exact canonical `performance` text.

Visual PASS still requires actual rendered/browser evidence.

## Revision discipline

Fix the first wrong owner and replay only invalidated scope. A Voice-only wording/setup change rerenders the consolidated HTML but does not reopen PRD acceptance when PRD canonical meaning is unchanged.

## Stop rule

Stop when current Voice Production is ready and the requested consolidated output is current. Do not create a separate Voice HTML, asset manifest, settings database, generic asset framework, extra score system, or proof layer without a concrete need.
