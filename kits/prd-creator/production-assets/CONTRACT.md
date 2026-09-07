# Production Assets Contract

This owner defines non-Voice `04 Production Assets`. It does not create another numbered Flow, asset registry, or document family. Voice keeps its Flow 5–7 semantic owners and joins the same 04 presentation through stable identity.

## Purpose and authority

04 comes from the same approved project model as PRD core 01–03:

```text
approved project model
├─ PRD core 01–03
└─ required concrete Production Assets
```

Do not discover 04 by rereading finished HTML and brainstorming decoration. Keep a resource only when it is explicit authority, a necessary production implication, or an approved material choice.

The human-facing result remains one project document:

```text
output/v<document.version>/prd.html
   01 Overview
   02 Gameplay Flow
   03 Development
   04 Production Assets
```

## Resource boundary

A Production Asset is a concrete resource somebody must prepare.

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

Machine identity is:

```text
Owner ID
  ↓
Moment ID
  ↓
Asset ID / Voice ID
```

Display titles are presentation only.

### Owner ID

Each `##` section defines one stable owner:

```text
Owner ID: shared
Owner ID: journey:<non-package gameplay-flow id>
Owner ID: package:<package id>
```

A package and its matching Gameplay Flow use only `package:<id>`. `journey:<id>` is reserved for non-package journey nodes such as the opening. Ownership is never inferred from a display title.

### Moment ID

Every resource carries:

```text
Moment ID: MOM-<STABLE-ID>
Moment: <reader-facing moment title>
```

`Moment ID` is machine identity. `Moment` is presentation. The same Owner + Moment ID must always map to the same current display title.

Moment order is the first canonical occurrence of each Moment ID inside that owner. Do not use numbered `Gameplay Flow` headings or a human-readable `Flow:` field for machine ordering.

### Resource ID

Every non-Voice asset has one globally unique:

```text
ID: AST-<STABLE-ID>
```

Voice uses its canonical `VO-...` ID.

Renaming an Owner/ moment/resource display title must not change its stable ID.

## Reader-first organization

04 follows project journey ownership and natural gameplay moments:

```text
04 Production Assets
   Shared Assets       # only when real shared resources exist
   Introduction
   Objective / Package 1
   Objective / Package 2
   ...
```

Within a page:

```text
01 · <Moment>
    <resource>
    <resource>

02 · <Moment>
    <resource>
```

The visible numbering is derived from Moment ID order and is not identity.

## Non-Voice source

When non-Voice assets exist, canonical source is:

```text
work/asset-requirements.md
```

The parser contract is implemented by `shared/assets.py`. New files use no compatibility aliases.

Internal grouping categories are exactly:

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

### AUDIO — dialogue

Dialogue scope and wording remain owned by Voice. 04 presents canonical Voice data only:

```text
AUDIO
<Character> — <Line Title>
Function
Voice Preset
ElevenLabs Model: Eleven v3
Estimated Duration
Prompt
```

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

### UI & Information

#### Trial Prompt
ID: AST-CORE-PROMPT
Moment ID: MOM-TRIAL-ACTIVATION
Moment: Trial Activation
Type: UI / TEXT
Function: Tells the player how to begin the trial.
Content:
```text
Activate Trial
```
````

New authoring must not use retired fields/headings:

```text
Flow
Gameplay Flow <n>
Create
Used
Includes
Group
For
Requirement
Usage
```

Unknown or duplicate fields fail instead of being silently ignored.

## Category/type rules

```text
3D Models                    → MODEL | ITEM
UI & Information             → UI / TEXT
Audio                        → AUDIO
Visual Effects & Presentation→ PARTICLE
```

`UI / TEXT` requires exact Content. MODEL/ITEM/PARTICLE/non-dialogue AUDIO require a production brief. Optional Size is used only when an approved numeric/build value exists.

## HTML presentation

The compositor:

```text
strict asset parser
+ strict Voice parser when present
+ accepted PRD Owner topology
→ merge by Owner ID + Moment ID
→ order resources deterministically
→ inject additive 04 pages
```

Derived HTML embeds exact source bindings:

```text
asset-requirements-sha256     # when non-Voice source exists
voice-requirements-sha256     # when Voice exists
voice-production-sha256       # when Voice exists
```

Production Assets CSS/JavaScript live under `renderer/static/` and are inlined during rendering. Python compositor code does not own large stylesheet/script literals.

## Acceptance boundary

When non-Voice `asset-requirements.md` exists, Flow 4 acceptance binds its exact bytes:

```text
Accepted Asset Requirements SHA256: <sha256>
```

When absent:

```text
Accepted Asset Requirements SHA256: none
```

Changing 04 source after acceptance makes handoff stale even when PRD semantic version is unchanged.

## Stop rules

- no asset-category dashboard;
- no title-based joins;
- no compatibility field aliases;
- no behavior disguised as assets;
- no duplicated canonical Voice wording in `asset-requirements.md`;
- no filler resource for visual symmetry;
- no ordinary 04 change that silently rewrites accepted 01–03 meaning;
- stop when every real resource has stable Owner/Moment/Resource identity and an actionable source-supported brief.
