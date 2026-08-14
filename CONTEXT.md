# PRD-Creator Context

Status: active production repository
Working branch: `Local`

## Product

PRD-Creator turns uneven project material into a development-ready PRD and, when needed, downstream production assets derived from that accepted PRD.

Current downstream presentation supports:

- compact PRD-derived non-Voice asset requirements through optional `work/asset-requirements.md`;
- Voice Production through the existing Flow 5–7 canonical sources.

Both are composed into the same objective-first `04 Production Assets` section of `output/v<document.version>/prd.html`.

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

Non-Voice Production Assets do **not** introduce another numbered Flow. Their actionable requirement contract is a bounded downstream extension after the accepted PRD. Voice Production is not a separate project/source intake; the accepted PRD remains its normal upstream authority.

Normal project creation/revision is **Production Execution**. `development-brief` is only for changing PRD-Creator itself.

## Operating direction

- source is triaged by authority/relevance before deep reading;
- Flow 2 resolves supported meaning before asking for decisions;
- only unresolved material decisions are surfaced;
- bounded revisions touch only invalidated scope;
- information completeness must not be sacrificed for speed;
- implementation ceremony must not be added without a concrete need.

# PRD authority

The PRD owns product/gameplay truth: what the experience must contain, how gameplay/system behavior works, and which downstream production assets are materially required.

Canonical semantic owner:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

The approved Golden Sample remains the canonical **PRD-core** page prototype.

PRD-core family:

```text
Overview
→ Gameplay Flow
     The Journey Begins
     one page per gameplay section
→ Development
     Development Overview
     Game System
     Data and Reset
     Gameplay Development
     gameplay/objective sections
          Gameplay Overview
          Level Design
          Developer
```

Internally the renderer may call gameplay sections `packages`; user-facing project copy should use the project's natural Objective/Gameplay naming instead of exposing that implementation term.

For `N` gameplay sections the PRD core remains `6 + 4N` pages.

Reference-project gameplay facts do not transfer automatically.

Mandatory concerns resolve as:

```text
Defined | Explicit No | Not Applicable | Blocked
```

## Golden presentation rules

- Overview, Gameplay Flow, Global Development, Gameplay Overview, Level Design and Developer follow matching Golden composition.
- Gameplay Overview uses short context cards; detailed rules live in their owning Gameplay/Developer surfaces.
- Acceptance remains Flow 4 review state; no extra visible Acceptance panel is added to Developer pages.
- Terms Used stays where Golden defines it.
- generated HTML is derived and never manually patched.
- Golden template bytes remain unchanged when downstream Production Assets are added.

# Production Assets relationship

Use this ownership model:

```text
PRD
= product / gameplay truth
= establishes that an asset is required

Asset Requirement
= concrete production requirement derived from PRD

Asset Production
= exact material/configuration used to produce the asset when a dedicated production lane needs it

Final Asset
= generated/created file used by development
```

Do not turn Asset Requirements into a second PRD. Carry only the context/constraints needed to produce the asset correctly and retain traceability to PRD authority.

## Non-Voice Production Asset contract

Current bounded contract owner:

```text
kits/project-document-generator/PRODUCTION-ASSETS.md
```

When non-Voice asset requirements exist, the project may add:

```text
work/asset-requirements.md
```

The file is objective-first and intentionally simple. It supports only:

```text
3D Models
UI & Information
Audio
Visual Effects & Presentation
```

Rules:

- state what must be made, not a component inventory;
- animation/VFX/SFX directly attached to one model/UI/presentation stay inside that owning requirement;
- UI includes exact player-facing text when known;
- shared assets are defined once under `Global / Shared Assets`;
- zero-count categories are absent;
- Voice canonical content is never duplicated into this file.

## One project HTML

`output/v<document.version>/prd.html` is the single human-facing project document.

It contains:

```text
PRD core
+
optional downstream Production Assets
```

Production Assets is professional-only downstream content, not a new PRD semantic page family.

Current navigation is objective-first:

```text
04 Production Assets
   Global / Shared Assets      # only when present
   <gameplay section title>
      <Introduction | Objective N | Ending | accepted PRD label>
```

Categories appear inside the matching page only. They are not nested in the sidebar and empty categories are not rendered.

Therefore downstream-only production updates may rerender the current versioned `prd.html` without reopening PRD acceptance when `work/content.md` and `work/render-data.json` are unchanged.

PRD core and downstream asset production retain separate canonical owners and acceptance evidence even though humans see one consolidated HTML.

The same deterministic delivery pass also creates AI side documents beside the HTML:

```text
output/README.md
    navigator / resume entry point

output/v<document.version>/context.md
    reasoning-friendly accepted PRD + relevant Production Asset/Voice requirements

output/v<document.version>/index.json
    compact heading graph + exact context.md line ranges
```

These side documents are derived navigation/reading projections only. They do not create another product authority, and `index.json` must not duplicate the PRD prose as a second structured PRD.

Production Assets extends the existing PRD navigation; it does not rebuild or renumber it. Gameplay/objective navigation remains under **03 Development** with the same accepted PRD page identities. Production Assets owns its separate professional top-level number **04**. A project without Production Assets keeps the same PRD-core navigation, and adding Production Assets does not shift PRD package/page codes.

# Voice Production direction

Voice Production Kit owns Flow 5–7. Flow 6 model scope is **Eleven v3 only**.

Normal authority:

```text
accepted PRD
→ work/voice-requirements.md
→ work/voice-production.md
→ output/v<document.version>/prd.html
   → Production Assets
      → matching gameplay section
         → Audio
            → Voice Production
```

### Flow 5

`voice-requirements.md` is the internal Voice Asset Requirement owner. It records which Voice moments are required and enough approved communication context for SoundMaker to write without product-level guessing.

### Flow 6

`voice-production.md` is canonical Voice Asset Production. It owns:

- exact Voice ID/Type/Speaker parity;
- Estimated Duration;
- exact Eleven v3 `performance` text, beginning with at least one deliberate initial performance-direction tag;
- selected ElevenLabs actor voice once per recurring Speaker when known.

Optional cast header:

```text
Voice Cast:
- <Speaker>: <selected ElevenLabs voice>
```

An actor voice may remain pending during Preparation Mode when a Target Voice Profile is enough to prepare wording. Actual Generation Mode requires the active Speaker's intended voice to be selected.

### Production Assets → Voice

Voice no longer owns a separate sidebar category. The objective-first Production Assets navigation identifies the gameplay section and accepted PRD label; Voice then appears inside that page's `Audio` category.

```text
04 Production Assets
   <gameplay section title>
      <Introduction | Objective N | Ending>

page content
→ Audio
   → Voice Production
```

Navigation labels may wrap naturally inside the sidebar and must remain readable without clipping or ellipsis.

A gameplay page containing Voice shows the common Production Assets section header, asset counts, then the `Audio` group. The detailed Voice Production block keeps:

```text
Voice line count + Primary Speaker
→ compact Voice Setup
→ Voice entries
```

Each Voice entry shows:

```text
title
→ PRD package label · Voice Line X/Y
→ Context = exact Flow 5 Trigger
→ Speaker + Estimated Duration
→ exact Eleven v3 text with performance directions visually distinct
→ Copy Prompt
```

The developer-facing Context does not create a new Voice field: it is a presentation of the existing Flow 5 Trigger. Flow 5 Purpose, `Must communicate`, `Must not add/repeat`, source refs, SoundMaker reasoning, WPM math, QA, and other internal fields stay out of the HTML.

`Copy Prompt` copies only the exact canonical performance payload.

Production Assets pages use their own page identity (`04A`, `04B`, ...). They do not borrow or alter PRD gameplay package numbering.

### DOCX

`Voice Production.docx` is optional portable export only. It is no longer required for normal Voice Production delivery when the consolidated project HTML is current.

## SoundMaker modes

```text
Preparation Mode
→ full current Voice scope may be prepared without audio testing
→ per-line construction + project-level readiness/anti-repetition

Generation Mode
→ actual ElevenLabs work only
→ one active Voice ID
→ actor voice selected
→ exact prompt + feedback/approval
→ canonical sync + rerender when changed
```

Preparation Mode may finish with no audio evidence. Generated-audio quality can be claimed only from actual heard evidence.

# Version policy

`document.version` is PRD project/release metadata, not an edit counter. Accepted development handoff versions use semantic `X.Y.Z`; the folder adds the `v` prefix.

Adding or revising downstream Production Assets does not change PRD `document.version` unless PRD/project meaning itself enters a new declared revision.

Voice Production maintains its own script/kit versioning. A shared compositor/presentation change does not require a Voice semantic version bump when Voice scope/content behavior is unchanged.

# Proof direction

PRD and Voice CI remain scoped separately.

- PRD renderer/compositor changes → PRD contracts;
- Voice canonical/validator changes → Voice contracts;
- consolidated HTML visual PASS requires actual rendered/browser evidence;
- generated audio quality requires actual audio review.

Do not replay unchanged browser/mobile/cross-flow tests for ceremony.

# Anti-overdevelopment

Prefer the smallest complete solution.

The concrete non-Voice asset need justified a narrow objective-first requirement/compositor extension. It did **not** justify a generic asset-management system.

Do not add generic asset schemas/registries/frameworks, separate asset Flows/Kits, new root skills, second HTML outputs, asset manifests, component databases, workflow engines, approval layers, extra checksums, semantic scoring, or audio-test requirements without a proved current need.

# Continuation

Read `docs/knowledge/next-action.md` for current status and the single next step.
