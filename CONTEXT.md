# PRD-Creator Context

Status: active production repository
Working branch: `Local`

## Product

PRD-Creator turns uneven project material into a development-ready PRD and, when needed, downstream production assets derived from that accepted PRD.

Voice is the currently implemented downstream asset lane.

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

Voice Production is not a separate project/source intake. The accepted PRD is its normal upstream authority.

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
→ Gameplay Sections
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
= concrete asset requirement derived from PRD

Asset Production
= exact material/configuration used to produce that asset

Final Asset
= generated/created file used by development
```

Do not turn Asset Requirements into a second PRD. Carry only the context/constraints needed to produce the asset correctly and retain traceability to PRD authority.

## One project HTML

`output/final.html` is the single human-facing project document.

It contains:

```text
PRD core
+
optional downstream Production Assets
```

Production Assets is professional-only downstream content, not a new PRD semantic page family.

Therefore a Voice-only production update may rerender `final.html` without reopening PRD acceptance when `work/content.md` and `work/render-data.json` are unchanged.

PRD core and downstream asset production retain separate canonical owners and acceptance evidence even though humans see one consolidated HTML.

# Voice Production direction

Voice Production Kit owns Flow 5–7. Flow 6 model scope is **Eleven v3 only**.

Normal authority:

```text
accepted PRD
→ work/voice-requirements.md
→ work/voice-production.md
→ output/final.html → Production Assets → Voice
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

The same project HTML shows only what the operator needs:

```text
Voice Setup once with the selected ElevenLabs voice prominent
→ scripts in gameplay order
→ per script:
   title
   Speaker + Estimated Duration as secondary metadata
   exact Eleven v3 text with performance directions visually distinct
   Copy integrated with the script panel
```

Flow 5 Purpose/Trigger/requirements/source refs, SoundMaker reasoning, WPM math, QA, and other internal fields stay out of the HTML.

`Copy Text` copies only the exact canonical performance payload.

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

`document.version` is PRD project/release metadata, not an edit counter.

Adding or revising downstream Voice Production does not change PRD `document.version` unless PRD/project meaning itself enters a new declared revision.

Voice Production maintains its own script/kit versioning.

# Proof direction

PRD and Voice CI remain scoped separately.

- PRD renderer/compositor changes → PRD contracts;
- Voice canonical/validator changes → Voice contracts;
- consolidated HTML visual PASS requires actual rendered/browser evidence;
- generated audio quality requires actual audio review.

Do not replay unchanged browser/mobile/cross-flow tests for ceremony.

# Anti-overdevelopment

Prefer the smallest complete solution.

Do not add generic asset schemas/frameworks, separate Voice HTML, asset manifests, settings databases, workflow engines, approval layers, extra checksums, semantic scoring, or audio-test requirements without a proved current need.

Current Production Assets implementation is Voice-specific by design; do not generalize it to SFX/Visual/etc. until a concrete downstream domain is actually being built.

# Continuation

Read `docs/knowledge/next-action.md` for current status and the single next step.
