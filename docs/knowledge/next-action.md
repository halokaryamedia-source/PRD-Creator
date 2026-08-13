# Next Action

Updated: 2026-08-13

## Current Status

`PRODUCTION_ASSETS_VOICE_HTML_READY`

Working branch: **`Local` only**.

## Current state

Project Document Generator PRD core remains **v1.13.0**. The approved Golden template bytes and PRD-core page contract remain unchanged.

Voice Production Kit is now **v1.10.0** and remains **Eleven v3 only**.

The approved architecture is now implemented:

```text
accepted PRD
= product/gameplay truth
        ↓
Flow 5 voice-requirements.md
= what Voice assets must be produced
        ↓
Flow 6 voice-production.md
= actor selection + exact production text
        ↓
same output/final.html
= PRD core + Production Assets → Voice
```

Voice is a downstream development asset from the accepted PRD, not a separate project/source intake.

# One HTML

`output/final.html` is the single human-facing project document.

The renderer first creates the unchanged PRD core through the approved Golden contract. When `work/voice-production.md` exists, it then appends professional-only Voice production pages after the PRD core.

If no Voice Production exists, the Production Assets compositor is a no-op and normal PRD output remains unchanged.

PRD core still uses `6 + 4N` pages. Production Assets pages are downstream extensions and are not counted as PRD-core pages.

# Voice page contract

Visible Voice production is intentionally simple:

```text
Production Assets
└── Voice

Voice Cast
- Speaker → selected ElevenLabs voice

Gameplay order
01 <Voice title>
   Actor
   Estimated Duration
   exact Eleven v3 script
   Copy Text

02 ...
```

The page does not expose Flow 5 Purpose/Trigger/requirements/source refs, Performance Fill Map reasoning, WPM math, QA, or other internal process data.

`Copy Text` copies only the exact canonical fenced `performance` payload.

# Voice Cast

`work/voice-production.md` may define actor selection once before gameplay sections:

```text
Voice Cast:
- <Speaker>: <selected ElevenLabs voice>
```

A voice may remain unselected in Preparation Mode; the HTML shows `Voice selection pending` rather than inventing one.

Generation Mode requires the active Speaker's intended ElevenLabs voice to be selected.

# PRD vs Voice acceptance

```text
PRD canonical change
→ reopen affected PRD acceptance

Voice-only production change
→ keep PRD acceptance when PRD canonical sources are unchanged
→ update voice-production.md
→ rerender same final.html
→ validate affected Voice / Production Assets scope
```

This prevents Production Assets from becoming a second PRD while still keeping one project document for humans.

# DOCX

`Voice Production.docx` is now optional export only. It is not required for normal Voice Preparation/Delivery when consolidated `final.html` is current.

Voice validator always checks canonical requirements/script parity; it checks consolidated project HTML when present and DOCX only when that optional export exists.

# Implemented proof coverage

Focused regression coverage now proves:

- Voice Production is composed into the same PRD HTML;
- Voice Cast and exact scripts are present;
- script order follows canonical gameplay order;
- Copy Text panels are generated;
- a project without `voice-production.md` receives no Production Assets extension;
- optional `Voice Cast:` does not break existing Voice builder/validator behavior.

No audio generation/listening was performed.

# Overdevelopment guard

No generic Asset framework/schema, asset manifest, second Voice HTML, settings database, new Flow, Golden-template rewrite, SFX/Visual implementation, or audio-test requirement was added.

The current compositor is deliberately Voice-specific. Generalize only when another concrete asset domain is actually approved for implementation.

## Next Step

**Run the current architecture on a real project's Voice Preparation when requested, then evaluate the actual consolidated HTML visually; do not add more generic asset infrastructure before a concrete production need appears.**
