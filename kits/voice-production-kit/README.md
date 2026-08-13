# Voice Production Kit v1.11.2

Repository-backed workflow for accepted PRD → Voice requirements → canonical production content → **Production Assets inside the same project HTML**. DOCX and audio remain optional downstream scopes.

## Flow

```text
accepted PRD
→ Flow 5 Voice Requirements
→ Flow 6 canonical Voice Production
→ same output/final.html
   PRD core
   + Production Assets → Voice
→ Flow 7 validation/delivery
```

## Active owners

- `VOICE-EXTRACTION.md` — Flow 5 Voice scope/context;
- this `README.md` + `docs/foundation/06-elevenlabs-script-production.md` — Flow 6 lifecycle/output contract;
- `SOUNDMAKER.md` — detailed Eleven v3 writing/performance procedure;
- `VOICE-VALIDATION.md` — Flow 7 readiness/evidence;
- `DOCX-FORMAT.md` — optional DOCX export only.

`SCRIPT-PRODUCTION.md` is no longer an active owner in v1.11.2 because the same lifecycle/output contract is already owned here and in the Flow 6 foundation policy.

## Authority

```text
accepted PRD
= project/gameplay truth

work/voice-requirements.md
= Voice scope + approved communication context

work/voice-production.md
= canonical production content

output/final.html → Production Assets → Voice
= derived developer/operator presentation
```

Derived HTML never becomes a second Voice authority.

## Production Assets → Voice

Production Assets extends the accepted PRD navigation. It does not rebuild Development or renumber PRD pages.

```text
03 Development
   global development pages
   gameplay/objective sections

04 Production Assets
   VOICE
   <gameplay section title>
   <accepted PRD package label>
```

Rules:

- gameplay/objective sections remain under Development;
- accepted PRD page identities remain unchanged;
- `VOICE` appears once;
- each Voice link shows section title + accepted PRD label;
- long sidebar labels wrap naturally rather than being truncated;
- Voice pages use their own Production Assets identities such as `04A`, `04B`, and later pages.

Each Voice section page shows gameplay title, accepted PRD label/context, Voice line count, Primary Speaker, and compact Voice Setup.

Each Voice line shows:

```text
title
→ <PRD package label> · Voice Line X/Y
→ Context = exact Flow 5 Trigger
→ Speaker · Estimated Duration
→ canonical production text
→ Copy Prompt
```

The developer-facing Context is a direct presentation of the existing Flow 5 Trigger; it is not a new Flow 6 field. Internal Purpose/requirements/source refs/reasoning/QA remain in their canonical owners.

`Copy Prompt` copies only the exact canonical production payload.

## Optional DOCX

`output/Voice Production.docx` is produced only when a portable export is requested or materially useful. It is not the default operator surface.

## Validation

Default non-audio readiness uses:

```text
Mechanical parity
+ Communication Conservation
+ integrated Voice Script Readiness
+ Project HTML Visual when claimed
+ optional DOCX Visual
+ optional Audio Evidence
```

When `final.html` exists, validation requires preserved PRD hierarchy/page identity, one Voice category, section title/package-label parity, per-line position/context parity, exact Flow 5 Trigger Context, and exact canonical Copy payload.

Visual PASS requires rendered/browser evidence.

## Revision discipline

Fix the first wrong owner and replay only invalidated scope. Voice-only changes do not reopen PRD acceptance when PRD canonical meaning is unchanged.

## Stop rule

Stop when current Voice Production and the requested consolidated output are current. Do not add a second Voice HTML, generic asset framework, duplicate Context field, extra workflow layer, or speculative proof system without a concrete need.
