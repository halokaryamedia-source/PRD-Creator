# Production Assets Contract

This owner defines the non-Voice `04 Production Assets` contract. It extends the existing PRD production system; it does not create another Flow, Skill, PRD family, or asset-management framework. Voice keeps its existing Flow 5–7 owners and canonical production source.

## Purpose

The Project Document Generator must be able to start from project discussion + original source, understand the complete project, and produce both:

```text
approved project model
├─ PRD core 01–03
└─ 04 Production Assets
```

Production Assets are therefore planned from the **same approved project model** as 01–03. Do not discover 04 by rereading the finished HTML and brainstorming extra assets afterward.

The artifact may be materialized after approval, but the production need must already be recoverable from the original source, current user direction, approved proposals, and the complete project model.

The final human-facing result remains one project document:

```text
output/v<document.version>/prd.html
   01 Overview
   02 Gameplay Flow
   03 Development
   04 Production Assets
```

The approved 01–03 Golden structure, style, content contract, and renderer behavior are protected. Work on 04 must not redesign or rewrite them.

## Production coverage during project understanding

While Flow 2 recovers Gameplay, Level Design, and Developer meaning, also recover the concrete resources that production will actually need.

For each Introduction / Objective / Ending, ask:

> What must the team actually create or prepare so this approved gameplay can exist as described?

Use the original project evidence and approved model, not speculative decoration.

Keep a resource only when at least one of these is true:

1. **Explicit requirement** — the source or approved discussion names it.
2. **Necessary production implication** — the approved gameplay clearly cannot be produced without it.
3. **Approved material choice** — a form/content/behavior choice that changes gameplay, story, player communication, or another project fact was resolved through the existing Completion/Proposal process.

Do not create an approval step for obvious production implications. Do not invent decorative props, extra VFX, sounds, or presentation beats simply because they might look good.

The Simple Chat Preview does not need to list every resource. It only needs to expose material AI-chosen decisions that require approval. Production implications can remain in the underlying approved model.

## What counts as a Production Asset

A Production Asset is a concrete resource someone must prepare.

Visible resource types are intentionally small:

```text
MODEL
ITEM
UI / TEXT
AUDIO
PARTICLE
```

Use them literally:

- **MODEL** — custom character, machine, trap, puzzle object, door, prop, or other model that must be built.
- **ITEM** — custom held/projectile/inventory item that must be prepared as an item asset.
- **UI / TEXT** — player-facing HUD, prompt, instruction, warning, objective/result text, hologram text, or other exact readable copy.
- **AUDIO** — dialogue or a real standalone non-dialogue audio cue.
- **PARTICLE** — only a genuinely standalone reusable particle/effect resource.

Do **not** turn these into Production Assets:

- gameplay logic;
- reset/recovery behavior;
- percentage/threshold logic;
- route switching or power recalculation;
- checkpoint state;
- pure event sequencing;
- a generic `SEQUENCE` wrapper;
- camera/fade/transition behavior that is only part of implementation;
- animation/sound/particle that belongs to an existing MODEL or ITEM.

Animation or visible state changes may be mentioned inside a model's Visual Brief when they are required to build that asset. They are not separate taxonomy fields.

## Reader-first organization

04 follows the project journey and is grouped by **gameplay moment**, not by asset-category dashboard.

```text
04 Production Assets
   Global / Shared Assets      # only when truly shared resources exist
   Introduction
   Objective 1
   Objective 2
   ...
   Ending
```

A page body uses:

```text
Objective N · <Objective Name>

01 · <natural gameplay moment>
    <resource>
    <resource>

02 · <next natural gameplay moment>
    <resource>
```

Moment names must read like real project moments, for example:

```text
Throughout the Warden Halls
Entering the Warden Halls
Searching the Chamber
Gremlin Changes the Route
Vault Restored
```

Avoid template wording such as `Objective Start`, `Throughout Objective`, `Objective Complete`, `First Rollback`, or other internal mechanic labels when a normal reader-friendly name is available.

Moment numbering is generated from the order that actually appears: `01`, `02`, `03`, ... . Do not reuse unrelated Gameplay Flow numbering when it creates gaps or duplicates.

## Resource writing contract

### MODEL / ITEM / PARTICLE

Show only information that helps someone create the resource:

```text
TYPE
Resource Name

Function
<what it is used for>

Visual Brief
<what must be made>

Size
<only when a real approved numeric/Block size exists>
```

Rules:

- **Function**: one short direct sentence. Explain what the resource does in the project.
- **Visual Brief**: one or two short literal sentences. Describe the form that must be made. Include required animation or visible change only when it materially belongs to the asset.
- **Size**: optional. Use only a real approved size/footprint, preferably in Minecraft blocks when relevant. Omit it when unknown.

Never write placeholder or vague size values such as `Large`, `Small`, `TBD`, `[approved size]`, or invented dimensions.

Do not add generic metadata such as:

```text
States
Position
Orientation
Reuse
Placement
Variants
Build Specs
Used At
Create
Includes
```

If a sentence can be removed without changing what the artist/modeler must make, remove it.

Example:

```text
MODEL
Swinging Axe Trap

Function
Ceiling trap that swings across the corridor.

Visual Brief
Large double-sided axe hanging from the ceiling with a left-right swing animation.
```

Example:

```text
ITEM
Echo Pebble

Function
Thrown at wall sensors and selected hanging stones.

Visual Brief
Small ordinary stone used as the throwable item.
```

Do not add visual adjectives or lore that the project did not approve. `ordinary stone` must not become `magical stone`, `arcane stone`, or another invented interpretation.

### UI / TEXT

Use:

```text
UI / TEXT
Resource Name

Function
<why the player needs this information>

Player Text
<exact copy>
```

Player Text is real player-facing copy. Keep internal implementation language out of it unless the project explicitly uses that language in-game.

Avoid leaking terms such as checkpoint state, local reset, validated progress, authored threshold, rotator count, run state, or internal mechanic names into player-facing text.

### AUDIO — dialogue

Voice scope and canonical wording remain owned by the Voice Production system. The 04 compositor only presents canonical Voice data.

Visible dialogue form:

```text
AUDIO
<Character> — <Line Title>

Function
<what this line does for the player/story>

Voice Preset
<selected ElevenLabs voice>

ElevenLabs Model
Eleven v3

Estimated Duration
<duration>

Prompt
<exact canonical performance payload>
```

Do not render a separate `Speaker` field when the character is already identified in the title. Performance-direction tags such as `[serious]` or `[mischievous]` must be visually distinguishable from spoken dialogue, while Copy Prompt still copies the exact canonical payload.

### AUDIO — non-dialogue

Use:

```text
AUDIO
Resource Name

Function
<what event/information the cue supports>

Audio Brief
<short description of the sound to make>
```

When there is no speech and ambiguity is possible, say it directly: `No spoken dialogue.`

Do not create a non-dialogue audio asset for every object action. Sound that only belongs to a MODEL/ITEM interaction stays in that asset's brief when it is materially required.

## Humanize / anti-AI-SLOP gate

04 is a production brief, not design prose.

Write as if a lead is handing a task to an artist, modeler, audio producer, or developer who has not memorized the project.

Use three checks:

1. **Does this sentence help someone make the resource?** If not, delete it.
2. **Is this detail supported by project authority?** If not, do not invent it.
3. **Can a new reader tell what to make without decoding internal terminology?** If not, make the wording clearer, not longer.

Avoid filler such as:

- `clearly readable visual language`;
- `visually recognizable while fitting naturally`;
- `enhances the player experience`;
- `supports strong visual feedback`;
- decorative adjectives that do not change the production task.

Prefer direct wording:

```text
Wall-mounted mechanical laser emitter with a visible beam.
```

over:

```text
A visually readable sensor treatment that clearly communicates the active hazard state to the player.
```

## Canonical project file

When non-Voice Production Assets exist, store the actionable source in:

```text
work/asset-requirements.md
```

The current parser keeps four internal storage headings for compatibility:

```text
3D Models
UI & Information
Audio
Visual Effects & Presentation
```

These are **source grouping only**. They are not the visible 04 navigation or visible resource taxonomy.

New authoring should use only the minimum fields needed by the current compositor:

````markdown
# Production Asset Requirements

## <Global / Shared Assets | accepted gameplay/journey section title>

### Gameplay Flow 01 — <accepted flow title>
### Gameplay Flow 02 — <accepted flow title>

### 3D Models

#### <Resource Name>
Flow: 01 — <accepted flow title>
Moment: <natural reader-facing moment>
Type: <MODEL | ITEM>
Function: <short direct function>
Visual Brief: <short literal production brief>
Size: <optional approved size only>

### UI & Information

#### <Resource Name>
Flow: 01 — <accepted flow title>
Moment: <natural reader-facing moment>
Type: UI / TEXT
Function: <short direct function>
Content:
```text
<exact player-facing copy>
```

### Audio

#### <Resource Name>
Flow: 02 — <accepted flow title>
Moment: <natural reader-facing moment>
Type: AUDIO
Function: <short direct function>
Audio Brief: <short non-dialogue sound brief>

### Visual Effects & Presentation

#### <Resource Name>
Flow: 02 — <accepted flow title>
Moment: <natural reader-facing moment>
Type: PARTICLE
Function: <short direct function>
Visual Brief: <short literal particle brief>
````

Do not generate legacy metadata (`Create`, `Used`, `Includes`, `Group`, `For`, `Requirement`, `Usage`) for new projects unless a concrete compatibility need requires it. Existing project files may retain those fields; the compositor remains backward-compatible.

Every non-shared section must map to an accepted journey/gameplay section. Material choices that change project meaning return to the existing approval model; the asset source or renderer must not invent them.

## HTML presentation

The sidebar stays simple:

```text
04 Production Assets
   <gameplay/shared section title>
      <Introduction | Objective N | Ending | accepted label>
```

Do not nest moments, types, or individual resources in the sidebar.

The body starts with the reader-facing section identity, for example:

```text
Objective 3 · Warden Halls
```

Do not repeat a second `Production Assets` heading inside the body when the page chrome already identifies Section 04.

Inside the page:

```text
moment
→ resource type
→ resource name
→ resource-specific fields
```

The type label must be visually easy to scan and appear above/before the resource name. 04 uses the same project document typography/layout language but must not modify Golden PRD-core bytes or 01–03 composition.

## Scope and stop rules

- no new Production Asset Flow;
- no new root Skill or separate Production Asset Kit;
- no generic asset schema/registry/manifest;
- no asset-category dashboard;
- no generic `States / Position / Orientation / Reuse` metadata;
- no component checklist for Model / Texture / Animation / Particle / SFX;
- no gameplay behavior or `SEQUENCE` disguised as an asset;
- no duplicated Voice canonical data inside `asset-requirements.md`;
- no second default HTML;
- no decorative/filler asset invented to make 04 look complete;
- no change to the approved 01–03 style, structure, Golden contract, or PRD-core renderer as part of ordinary 04 authoring;
- stop when every real required production resource is clear enough to hand off and the consolidated document is readable.
