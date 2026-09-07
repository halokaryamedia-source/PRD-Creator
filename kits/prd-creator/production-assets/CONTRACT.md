# Production Assets Contract

This owner defines non-Voice `04 Production Assets` inside the unified PRD Creator package. It does not create another Flow, Skill, PRD family, or asset-management framework. Voice keeps its Flow 5–7 semantic owners and canonical production source.

## Purpose and authority

Production Assets come from the **same approved project model** as PRD core 01–03:

```text
approved project model
├─ PRD core 01–03
└─ 04 Production Assets
```

Do not discover 04 by rereading finished HTML and brainstorming additions. Keep a resource only when it is explicit in authority, a necessary production implication of approved gameplay, or an approved material choice. Do not create decorative props, VFX, sounds, or presentation beats merely because they may look good.

The final human-facing result remains one project document:

```text
output/v<document.version>/prd.html
   01 Overview
   02 Gameplay Flow
   03 Development
   04 Production Assets
```

Work on 04 must not redesign or rewrite approved 01–03 meaning or Golden composition.

## Resource boundary

A Production Asset is a concrete resource somebody must prepare.

Visible types are intentionally small:

```text
MODEL
ITEM
UI / TEXT
AUDIO
PARTICLE
```

Use them literally:

- **MODEL** — custom character, machine, trap, puzzle object, door, prop, or other model to build;
- **ITEM** — custom held/projectile/inventory item;
- **UI / TEXT** — player-facing HUD, prompt, instruction, warning, objective/result text, hologram text, or other exact readable copy;
- **AUDIO** — dialogue or a real standalone non-dialogue cue;
- **PARTICLE** — a genuinely standalone reusable effect resource.

Do not turn gameplay logic, reset/recovery behavior, thresholds, route switching, checkpoint state, pure sequencing, generic `SEQUENCE` wrappers, or implementation-only camera/fade/transition behavior into assets. Animation/sound/particle that materially belongs to a MODEL or ITEM stays in that resource brief rather than becoming a separate taxonomy item.

## Stable machine identity

Human-readable titles are presentation, not identity.

Every source section in `work/asset-requirements.md` must define one stable `Owner ID` immediately below the `##` heading:

```text
Owner ID: shared
Owner ID: journey:<gameplay_flow.id>
Owner ID: package:<package.id>
```

Every non-Voice asset entry must define one globally unique stable `ID`:

```text
ID: AST-CORE-CONSOLE
```

Rules:

- Owner IDs map directly to accepted PRD stable IDs; do not infer ownership by matching display titles.
- Asset IDs remain stable when a resource title is polished or localized.
- Duplicate Owner IDs and duplicate Asset IDs are invalid.
- A missing/unknown Owner ID is invalid; the compositor does not guess.
- New project files do not use title-based compatibility fallback.

## Reader-first organization

04 follows the project journey and is grouped by natural gameplay moment, not by asset-category dashboard.

```text
04 Production Assets
   Global / Shared Assets      # only when truly shared resources exist
   Introduction
   Objective 1
   Objective 2
   ...
   Ending
```

Within a page:

```text
Objective N · <Objective Name>

01 · <natural gameplay moment>
    <resource>
    <resource>

02 · <next natural gameplay moment>
    <resource>
```

Use project-facing moment names such as `Entering the Warden Halls`, `Searching the Chamber`, or `Vault Restored`; avoid template labels such as `Objective Start` or `Objective Complete` when natural wording exists. Moment numbering is derived from actual presentation order.

## Resource writing contract

### MODEL / ITEM / PARTICLE

Show only production-useful information:

```text
TYPE
Resource Name

Function
<what it does>

Visual Brief
<what must be made>

Size
<optional approved numeric/block size only>
```

Function is one short direct sentence. Visual Brief is one or two literal sentences. Size is optional and must be an approved value; never invent dimensions or use `TBD`, `Large`, or similar placeholders.

Do not add generic metadata such as `States`, `Position`, `Orientation`, `Reuse`, `Placement`, `Variants`, `Build Specs`, `Used At`, `Create`, or `Includes` when it does not change the production task.

### UI / TEXT

```text
UI / TEXT
Resource Name

Function
<why the player needs it>

Player Text
<exact copy>
```

Player Text is real player-facing copy. Keep implementation language out unless the project explicitly uses it in-game.

### AUDIO — dialogue

Voice wording remains owned by Voice Production. 04 presents canonical Voice data:

```text
AUDIO
<Character> — <Line Title>

Function
<what this line does>

Voice Preset
<selected ElevenLabs voice>

ElevenLabs Model
Eleven v3

Estimated Duration
<duration>

Prompt
<exact canonical performance payload>
```

Do not render a redundant Speaker field when the character is already in the title. Copy Prompt must preserve the exact canonical payload.

### AUDIO — non-dialogue

```text
AUDIO
Resource Name

Function
<what event/information the cue supports>

Audio Brief
<short description of the sound to make>
```

Do not create a standalone audio asset for every object action; sound that belongs to an existing MODEL/ITEM stays in that asset brief when materially required.

## Humanize / anti-AI-SLOP gate

04 is a production brief, not design prose. For each sentence ask:

1. Does it help someone make the resource?
2. Is it supported by project authority?
3. Can a new reader act on it without decoding internal terminology?

Delete filler and unsupported decorative adjectives. Prefer literal production language.

## Canonical project file

When non-Voice Production Assets exist, store the actionable source in:

```text
work/asset-requirements.md
```

Internal category headings remain:

```text
3D Models
UI & Information
Audio
Visual Effects & Presentation
```

They are source grouping only; they are not the visible 04 navigation or visible resource taxonomy.

New authoring uses the minimum current fields:

````markdown
# Production Asset Requirements

## <reader-facing accepted section title>
Owner ID: <shared | journey:<flow-id> | package:<package-id>>

### Gameplay Flow 01 — <accepted flow title>

### 3D Models

#### <Resource Name>
ID: AST-<STABLE-ID>
Flow: 01 — <accepted flow title>
Moment: <natural reader-facing moment>
Type: MODEL
Function: <short direct function>
Visual Brief: <short literal production brief>
Size: <optional approved size only>

### UI & Information

#### <Resource Name>
ID: AST-<STABLE-ID>
Flow: 01 — <accepted flow title>
Moment: <natural reader-facing moment>
Type: UI / TEXT
Function: <short direct function>
Content:
```text
<exact player-facing copy>
```
````

Do not generate retired metadata (`Create`, `Used`, `Includes`, `Group`, `For`, `Requirement`, `Usage`) for new projects. The current compositor no longer uses those fields to invent presentation meaning.

## HTML presentation

The sidebar stays simple:

```text
04 Production Assets
   <gameplay/shared section title>
      <Introduction | Objective N | Ending | accepted label>
```

Do not nest moments, types, or resources in the sidebar. Inside a page use:

```text
moment
→ resource type
→ resource name
→ resource-specific fields
```

The type label must be easy to scan. 04 uses the same project-document language but must not modify Golden PRD-core bytes or 01–03 composition.

## Scope and stop rules

- no new Production Asset Flow, root Skill, separate kit, generic asset registry, or second default HTML;
- no asset-category dashboard or generic metadata inventory;
- no behavior/`SEQUENCE` disguised as an asset;
- no duplicated Voice canonical data inside `asset-requirements.md`;
- no filler asset invented to make 04 look complete;
- no change to approved 01–03 style/meaning during ordinary 04 authoring;
- stop when every real required resource is explicit, stable-identified, source-supported, and clear enough to hand off.
