# PRD-Creator Context

Status: active production repository
Working branch: `Local`

## Product

PRD-Creator turns uneven project material into development-ready PRD documentation and, when needed, downstream Voice Production assets.

## Production sequence

```text
Flow 1  Repository Boot & Project Memory
Flow 2  Source Intake & Requirement Recovery
Flow 3  Project Document / PRD Generation
Flow 4  PRD Validation & Team Handoff
Flow 5  Voice Requirement Extraction
Flow 6  Eleven v3 Performance Script Production
Flow 7  Voice Validation & Delivery
```

Normal project creation/revision is **Production Execution**. `development-brief` is only for changing PRD-Creator itself.

## Operating direction

- source is triaged by authority/relevance before deep reading;
- Flow 2 resolves supported meaning before asking for decisions;
- only unresolved material decisions are surfaced;
- bounded revisions touch only invalidated scope;
- information completeness must not be sacrificed for speed;
- implementation ceremony must not be added without a concrete need.

## Gameplay PRD authority

The single owner is:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

The approved Golden Sample is the **canonical visible page prototype**, not merely a style inspiration or loose quality reference.

Project facts are dynamic. The visible page composition is locked unless the user explicitly approves a Golden prototype change.

Fixed family:

```text
Overview
→ Gameplay Flow
     The Journey Begins
     one page per package
→ Development
     Development Overview
     Game System
     Data and Reset
     Gameplay Development
→ Gameplay Package(s)
     Gameplay Overview
     Level Design
     Developer
```

For `N` packages: `6 + 4N` pages.

Reference-project gameplay facts do not transfer automatically.

Mandatory concerns resolve as:

```text
Defined | Explicit No | Not Applicable | Blocked
```

## Golden presentation rules

- Overview, Gameplay Flow, Global Development, Gameplay Overview, Level Design and Developer each follow the matching Golden component order and labels.
- Gameplay Overview uses short 3-card summaries; detailed rules go to Gameplay Information/Gameplay Flow/Developer.
- Global/Level/Developer flow uses the Golden horizontal-card pattern rather than new matrices.
- Acceptance remains Flow 4 review state; no extra visible Acceptance panel is added to Developer pages.
- Terms Used is visible only where Golden shows it: Gameplay Flow, Global Development, Gameplay Overview.
- inline glossary highlighting may still help readers without changing page composition.
- generated HTML is derived and is never manually patched.

## Writing direction

Use direct production prose. One paragraph should answer one main question.

Avoid:

- long copy inside narrow summary cards;
- repeated explanation;
- generator/document meta-language;
- invented professional-sounding labels;
- database-like prose where Golden uses normal narrative;
- extra UI created merely to fit verbose content.

Humanize means clearer and shorter, not more prose.

## Voice Production direction

Voice Production Kit owns Flow 5–7. Flow 6 production model scope is **Eleven v3 only**.

`SOUNDMAKER.md` is the Flow 6 operational quality procedure and has two working modes:

```text
Preparation Mode
→ full current Voice scope may be prepared without audio testing
→ per-line construction + project-level continuity/anti-repetition

Generation Mode
→ actual ElevenLabs work only
→ one active Voice ID + exact prompt + feedback/approval loop
```

SoundMaker is not a new Flow or root skill.

Canonical Voice authority remains:

```text
accepted PRD
→ work/voice-requirements.md
→ SoundMaker v3 preparation/generation quality
→ work/voice-production.md
→ derived DOCX / optional generated-audio evidence
```

Preparation Mode may finish with no audio evidence. When actual generated wording is later approved, the exact prompt actually used must synchronize back into canonical `work/voice-production.md` before current script/DOCX/audio alignment is claimed.

## Version policy

`document.version` is project/release metadata, not an edit counter.

Normal drafting, Humanize, rerendering, review corrections and representative tests keep the same version. Change it only for an explicit user/source revision or intentionally declared release/handoff milestone.

## Proof direction

Default visual proof is targeted desktop-only. Compare affected pages directly with the matching Golden prototypes.

PRD and Voice CI remain scoped separately. Do not replay unchanged browser/mobile/cross-flow tests for ceremony.

## Anti-overdevelopment

Prefer the smallest complete solution. Do not add generic schemas, workflow engines, approval layers, extra checksums, semantic similarity scoring, word/row-count gates, or presentation variants without a proved current need.

## Continuation

Read `docs/knowledge/next-action.md` for current status and the single next step.
