# Production Assets Contract

This owner defines **Production Assets**: concrete project resources somebody must prepare. It is a bounded capability, not a numbered workflow stage. Voice keeps its own Voice Requirements / Voice Production / Voice Delivery owners and joins the same Production Assets presentation through stable identity.

## Purpose and authority

Production Assets come from the same approved project model as the PRD:

```text
approved project model
├─ canonical PRD meaning
└─ required concrete Production Assets
```

Do not discover Production Assets by rereading finished HTML and brainstorming decoration. Keep a resource only when it is explicit authority, a necessary production implication, or an approved material choice.

The generated project document displays this capability simply as **Production Assets**. It does not use `04` or another workflow-number alias. Core PRD section ordinals remain a separate Golden document-layout concern.

## Resource boundary

Supported visible types:

```text
MODEL
ITEM
UI / TEXT
AUDIO
PARTICLE
```

Do not turn gameplay logic, reset behavior, thresholds, route switching, checkpoint state, sequencing, or implementation-only transition behavior into fake assets.

## Stable identity hierarchy

```text
Owner ID
→ Moment ID
→ Asset ID / Voice ID
```

Display titles are presentation only.

### Owner ID

```text
Owner ID: shared
Owner ID: journey:<non-package gameplay-flow id>
Owner ID: package:<package id>
```

A package and its matching Gameplay meaning use only `package:<id>`. Ownership is never inferred from a display title.

### Moment ID

Every resource carries:

```text
Moment ID: MOM-<STABLE-ID>
Moment: <reader-facing moment title>
```

`Moment ID` is machine identity; `Moment` is presentation. Moment order is the first canonical occurrence inside that owner. Do not use human-readable numbered headings as machine ordering keys.

### Resource ID

Every non-Voice asset has one globally unique:

```text
ID: AST-<STABLE-ID>
```

Voice uses its canonical `VO-...` ID. Renaming display titles must not change stable IDs.

## Reader-first organization

Production Assets follows project journey ownership and natural gameplay moments:

```text
Production Assets
  Shared Assets       # only when real shared resources exist
  Introduction
  Objective / Package 1
  Objective / Package 2
  ...
```

Within a page, visible moment numbering is derived from Moment ID order and is not identity.

## Non-Voice source

When non-Voice assets exist, canonical source is:

```text
work/asset-requirements.md
```

The parser contract is implemented by `shared/assets.py`.

Internal authoring categories remain exactly:

```text
3D Models
UI & Information
Audio
Visual Effects & Presentation
```

They group source authoring only; visible navigation remains owner-based.

### MODEL / ITEM / PARTICLE

```text
TYPE
Resource Name

Function
<what it does>

Visual Brief
<what must be made>

Size
<optional approved value>
```

### UI / TEXT

```text
UI / TEXT
Resource Name

Function
<why the player needs it>

Player Text
<exact copy>
```

`Content` is mandatory for `UI / TEXT`.

### AUDIO — non-dialogue

```text
AUDIO
Resource Name

Function
<what event/information it supports>

Audio Brief
<what sound must be produced>
```

`Audio Brief` owns required sound meaning. `SOUND-EFFECTS.md` may derive ElevenLabs generation prompt/settings without creating another canonical asset source.

### AUDIO — Voice

Voice scope and wording remain owned by Voice Requirements / Voice Production. Production Assets presents canonical Voice data only:

```text
AUDIO
<Character> — <Line Title>
Function
Voice Preset
ElevenLabs Model: Eleven v3
Estimated Duration
Prompt
```

Text to Dialogue grouping is generation context; canonical identity remains the ordered `VO-...` resources under their approved Moment.

## Canonical authoring example

````markdown
# Production Asset Requirements

## Core Trial
Owner ID: package:core

### 3D Models

#### Trial Console
ID: AST-CORE-CONSOLE
Moment ID: MOM-TRIAL-ACTIVATION
Moment: Trial Activation
Type: MODEL
Function: Gives the player the required trial interaction point.
Visual Brief: Build the approved console form with the readable interaction surface.
````

Unknown or duplicate fields fail instead of being silently ignored.

## Category/type rules

```text
3D Models                     → MODEL | ITEM
UI & Information              → UI / TEXT
Audio                         → AUDIO
Visual Effects & Presentation → PARTICLE
```

`UI / TEXT` requires exact Content. MODEL/ITEM/PARTICLE/non-dialogue AUDIO require a production brief. Optional Size is used only when an approved value exists.

## HTML presentation

```text
strict asset parser
+ strict Voice parser when present
+ accepted PRD Owner topology
→ merge by Owner ID + Moment ID
→ deterministic resource ordering
→ Production Assets pages in the same project HTML
```

Derived HTML embeds exact source bindings when present:

```text
asset-requirements-sha256
voice-requirements-sha256
voice-production-sha256
```

## Acceptance boundary

When `work/asset-requirements.md` exists, **PRD Handoff** binds its exact bytes:

```text
Accepted Asset Requirements SHA256: <sha256>
```

When absent:

```text
Accepted Asset Requirements SHA256: none
```

Changing Production Assets after acceptance makes PRD Handoff stale even when the PRD semantic version is unchanged.

## Stop rules

- no asset-category dashboard;
- no title-based joins;
- no compatibility field aliases;
- no behavior disguised as assets;
- no duplicated canonical Voice wording in `asset-requirements.md`;
- no generation-settings database or SFX manifest by default;
- no filler resource for visual symmetry;
- no Production Assets change that silently rewrites accepted PRD meaning;
- stop when every real resource has stable Owner/Moment/Resource identity and an actionable source-supported brief.
