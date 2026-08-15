# PRD-Creator Context

Status: active production repository
Working branch: `Local`

## Product

PRD-Creator turns uneven project discussion + source material into one approved project model, then produces a development-ready PRD core and the concrete Production Assets needed to build that same project.

The normal human-facing document can contain:

```text
01 Overview
02 Gameplay Flow
03 Development
04 Production Assets
```

01–03 keep the approved Golden PRD-core structure. 04 is an additive production surface generated from the **same approved project model**, not a second design pass over finished 01–03.

Current downstream presentation supports:

- non-Voice Production Assets through optional `work/asset-requirements.md`;
- Voice Production through the existing Flow 5–7 canonical sources.

Both are composed into the same objective/moment-first `04 Production Assets` section of `output/v<document.version>/prd.html`.

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

Non-Voice Production Assets do **not** introduce another numbered Flow. Their needs are recovered with the same project model during normal project understanding and materialized through the existing bounded 04 contract after approval. Voice Production is not a separate project/source intake; accepted project/PRD meaning remains its upstream authority.

Normal project creation/revision is **Production Execution**. `development-brief` is only for changing PRD-Creator itself.

## Operating direction

- source is triaged by authority/relevance before deep reading;
- Flow 2 resolves supported meaning before asking for decisions;
- the same understanding pass preserves Gameplay / Level Design / Developer meaning and real Production Asset needs;
- only unresolved material decisions are surfaced;
- bounded revisions touch only invalidated scope;
- information completeness must not be sacrificed for speed;
- implementation ceremony must not be added without a concrete need.

# PRD authority

The PRD owns product/gameplay truth: what the experience must contain, how gameplay/system behavior works, and which production resources are materially required.

Canonical PRD-core semantic owner:

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

## Protected 01–03 presentation

- Overview, Gameplay Flow, Global Development, Gameplay Overview, Level Design and Developer follow matching Golden composition.
- Gameplay Overview uses short context cards; detailed rules live in their owning Gameplay/Developer surfaces.
- Acceptance remains Flow 4 review state; no extra visible Acceptance panel is added to Developer pages.
- Terms Used stays where Golden defines it.
- generated HTML is derived and never manually patched.
- Golden template bytes remain unchanged when 04 Production Assets are added.
- adding or revising 04 is not permission to redesign, simplify, rename, move, or rewrite 01–03.

# Production Assets relationship

Use this ownership model:

```text
Discussion + Original Source + Approved Decisions
→ Complete Approved Project Model
   ├─ PRD Core 01–03
   └─ Production Assets 04
```

Do not use this as the normal design path:

```text
finished 01–03
→ reread generated document
→ brainstorm extra assets
→ invent 04
```

Production Asset need is part of understanding the project from the beginning. The canonical asset source is simply materialized after the project meaning is approved.

## Non-Voice Production Asset contract

Current bounded contract owner:

```text
kits/project-document-generator/PRODUCTION-ASSETS.md
```

When non-Voice asset requirements exist, the project may add:

```text
work/asset-requirements.md
```

04 is objective/moment-first and intentionally simple.

Visible resource types are:

```text
MODEL
ITEM
UI / TEXT
AUDIO
PARTICLE
```

Rules:

- include only concrete resources the team actually needs to create or prepare;
- MODEL / ITEM / PARTICLE use short `Function` + literal `Visual Brief`; optional `Size` appears only when a real approved numeric/block size exists;
- UI / TEXT uses `Function` + exact player-facing copy;
- non-dialogue AUDIO uses `Function` + short `Audio Brief`;
- Voice dialogue remains canonical in Voice Production and is presented as AUDIO in the matching moment;
- animation/visual change may stay inside a Visual Brief when it materially belongs to that asset;
- gameplay behavior, reset logic, route logic, thresholds, and generic sequences are not assets;
- do not use generic visible metadata such as `States`, `Position`, `Orientation`, `Reuse`, `Used At`, or `Build Specs`;
- do not invent visual style, lore, dimensions, animation, VFX, or sounds not supported by project authority;
- internal markdown storage headings may remain for parser compatibility, but they are not the visible 04 taxonomy/dashboard;
- Voice canonical content is never duplicated into `asset-requirements.md`.

### 04 Humanize direction

04 should read like a production note from a lead to the person making the resource.

Use three checks:

1. Does the sentence help someone make the resource?
2. Is the detail supported by project authority?
3. Can a new reader understand what to make without decoding internal terminology?

If not, delete or clarify it. Do not make it longer to sound professional.

## One project HTML

`output/v<document.version>/prd.html` is the single human-facing project document.

It contains:

```text
PRD core 01–03
+
optional 04 Production Assets
```

Current 04 navigation is objective-first:

```text
04 Production Assets
   Global / Shared Assets      # only when present
   <gameplay section title>
      <Introduction | Objective N | Ending | accepted PRD label>
```

Inside a page, resources are grouped by natural gameplay moment:

```text
Objective N · <Name>

01 · <Moment>
   TYPE
   Resource Name
   ...

02 · <Moment>
   ...
```

Do not add moment/type/asset nesting to the sidebar. Do not duplicate a second `Production Assets` title inside the body when page chrome already identifies Section 04.

A downstream-only 04 update may rerender the current versioned `prd.html` without reopening PRD-core acceptance when `work/content.md` and `work/render-data.json` are unchanged.

PRD core and downstream asset production retain separate canonical owners even though humans see one consolidated HTML.

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

Production Assets extends the existing PRD navigation; it does not rebuild or renumber it. Gameplay/objective navigation remains under **03 Development** with the same accepted PRD page identities. Production Assets owns its separate professional top-level number **04**.

# Voice Production direction

Voice Production Kit owns Flow 5–7. Flow 6 model scope is **Eleven v3 only**.

Normal authority:

```text
accepted project / PRD meaning
→ work/voice-requirements.md
→ work/voice-production.md
→ output/v<document.version>/prd.html
   → 04 Production Assets
      → matching gameplay moment
         → AUDIO
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

### Production Assets → Voice presentation

Voice does not own a separate sidebar category. Canonical Voice is merged into the matching 04 moment as an AUDIO resource.

Visible dialogue form is:

```text
AUDIO
<Character> — <Line Title>

Function
<communication/story purpose at this moment>

Voice Preset
<selected actor voice>

ElevenLabs Model
Eleven v3

Estimated Duration
<duration>

Prompt
<exact canonical performance payload>
```

Performance-direction tags are visually distinct from spoken dialogue. `Copy Prompt` copies only the exact canonical performance payload.

Flow 5 Trigger/Purpose/requirements/source refs and SoundMaker reasoning remain in their canonical owners; 04 does not duplicate that internal metadata.

### DOCX

`Voice Production.docx` is optional portable export only. It is not required for normal Voice Production delivery when the consolidated project HTML is current.

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

- 01–03 PRD-core rules/renderer are not invalidated by an instruction-only 04 contract update unless a shared owner actually changed;
- PRD 04 renderer/compositor changes → PRD contracts;
- Voice canonical/validator changes → Voice contracts;
- consolidated HTML visual PASS requires actual rendered/browser evidence;
- generated audio quality requires actual audio review.

Do not replay unchanged browser/mobile/cross-flow tests for ceremony.

# Anti-overdevelopment

Prefer the smallest complete solution.

04 is a bounded capability of the existing Project Document Generator. It does **not** justify a generic asset-management system.

Do not add generic asset schemas/registries/frameworks, separate asset Flows/Kits, new root skills, second HTML outputs, asset manifests, component databases, workflow engines, approval layers, extra checksums, semantic scoring, or audio-test requirements without a proved current need.

# Continuation

Read `docs/knowledge/next-action.md` for current status and the single next step.
