# Production Assets Contract

This owner defines the PRD-derived, non-Voice Production Asset Requirement contract. Voice keeps its own Flow 5–7 owners and canonical production source.

## Purpose

After the PRD is accepted, Production Assets should tell a developer or artist exactly what must be made for each gameplay section without creating a second PRD or a technical component inventory.

The default human-facing result remains the same project document:

```text
accepted PRD
→ optional work/asset-requirements.md
→ optional Voice canonical sources
→ same output/final.html
   PRD core
   + 04 Production Assets
```

## Objective-first organization

Production Assets follows the project journey, not an asset-category dashboard:

```text
04 Production Assets
   Global / Shared Assets      # only when shared assets exist
   Introduction
   Objective 1
   Objective 2
   ...
   Ending
```

Each gameplay/shared page shows only categories that actually contain assets.

Allowed categories are intentionally small:

```text
3D Models
UI & Information
Audio
Visual Effects & Presentation
```

A category with zero assets is omitted completely. Do not render empty headings, `0 Assets`, `None`, or placeholder cards.

## Asset discovery and recommendation pass

Production Assets must not depend on the source explicitly naming every model, UI element, sound, or presentation asset.

After the gameplay/PRD meaning is complete, inspect each shared/journey/gameplay section once and ask:

```text
What custom player-visible, player-readable, player-heard, or authored presentation asset
must exist for this accepted gameplay to work as specified?
```

Use this rule:

1. **Explicit requirement** — if accepted authority already names or clearly requires the asset, carry it directly into Production Assets.
2. **Necessary production implication** — if accepted gameplay logically requires a custom asset even though the source never named it, derive the asset need rather than leaving production to guess. Example: a gameplay rule that requires the player to repair three broken power nodes justifies a `Power Node` model requirement with the necessary Broken/Restored states.
3. **Material design choice** — if choosing a specific form, name, content, or behavior would change gameplay, lore, player communication, or another accepted project fact, resolve that choice upstream through the existing Completion/Proposal process before finalizing the asset requirement.
4. **Production-only recommendation** — when several production forms can satisfy the same accepted gameplay without changing project meaning, choose one practical recommendation at the production layer. Do not create another approval framework or pretend the recommendation came from the source.

Recommend only assets with a real gameplay, information, audio, or presentation function. Do not invent decorative models, extra VFX, UI, or sounds merely to fill a category or make the document look complete.

## Asset requirement rule

An asset entry describes the production result, not its implementation components.

Good:

```text
Main Generator
Requirement: Create one large objective generator with clearly different Inactive and Active states. When activated, its moving parts start, the energy core lights, a short electrical spark appears, and the mechanical startup sound plays.
Usage: Starts Inactive and changes permanently to Active when the objective is completed.
```

Do not replace that with a component checklist such as Model / Texture / Animation / Particle / SFX.

Animation, particle/VFX, texture treatment, state changes, and SFX that belong directly to one model/UI/presentation stay inside that owning asset requirement.

## Category boundaries

### 3D Models

Use for a concrete custom model/object that must be produced, such as a character/NPC, enemy, objective entity, machine, interactive object, door, puzzle object, tool/item, or custom environmental prop.

State exactly which model must be created and what visible/interactive states it needs. Attached animation, VFX, and SFX remain in the same requirement when they are part of that model's behavior.

Do not move terrain, room composition, paths, arena construction, or normal block-by-block level building here; those remain Level Design.

### UI & Information

Use for player-facing information such as HUD, hologram, objective text, interaction prompt, tutorial/instruction, waypoint, icon, warning, or result information.

State its function, when it appears/changes/disappears, and include the exact player-facing text whenever that text is already knowable.

Classify by player-facing function rather than implementation technique. A health bar or hologram still belongs here even if its Minecraft implementation uses geometry, entities, textures, or animation.

### Audio

Use only for audio that is a meaningful independent production asset, such as Voice Over, narration, music, ambience, countdown/global cue, or other sound not better owned by a model/UI/presentation requirement.

An SFX that exists only because one model/object performs an action stays inside that model/object requirement.

Voice entries are not duplicated into `asset-requirements.md`; the renderer merges canonical Voice Production into the Audio section of the matching gameplay page.

### Visual Effects & Presentation

Use for standalone visual effects or complete authored presentation sequences whose primary function is not owned by one model/UI asset. Examples include environmental/area VFX, directional or boundary effects, intro/ending presentation, cutscene, objective reveal, camera sequence, fade, or transition presentation.

Describe what the player must see, when it appears/runs, and any important state or timing relationship. Do not split one presentation sequence into separate Camera / Animation / VFX / SFX asset entries.

A spark, glow, animation, or effect that exists only as part of one model/UI asset remains inside that owning requirement instead of becoming a separate Visual Effects & Presentation entry.

## Shared assets

Use `Global / Shared Assets` only for a real asset reused across multiple gameplay sections. Define it once rather than duplicating the same production requirement under several objectives.

## Canonical project file

When non-Voice Production Asset requirements exist, store only the actionable requirement set in:

```text
work/asset-requirements.md
```

Format:

````markdown
# Production Asset Requirements

## <Global / Shared Assets | accepted gameplay section title>

### <3D Models | UI & Information | Audio | Visual Effects & Presentation>

#### <Asset Name>
Requirement: <exactly what must be made and the important result/state behavior>
Usage: <optional; when/where it is used, changes, or stops>
Content:
```text
<optional exact player-facing text/content>
```
````

`Requirement` is mandatory. `Usage` and `Content` are included only when useful. Do not add IDs, component lists, status matrices, confidence scores, recommendation flags, or implementation-file metadata by default.

Every non-shared section must map to an accepted PRD gameplay/journey section. If a material asset choice would change accepted project meaning, resolve that semantic gap upstream instead of inventing it in the asset file or renderer. Production-only recommendations that preserve accepted gameplay may stay at this downstream abstraction.

## HTML presentation

The sidebar stays scan-first:

```text
04 Production Assets
   <gameplay section title>
      <Introduction | Objective N | Ending | accepted label>
```

Do not add category or individual-asset nesting to the sidebar.

Each page uses:

```text
Production Assets
<gameplay section title>
<accepted PRD label>
<context>
<total assets + non-zero category counts>

<non-zero category>
  asset requirement
  asset requirement

<next non-zero category>
  ...
```

Voice keeps its current detailed production card (Trigger/Context, Speaker, Estimated Duration, exact Eleven v3 prompt, Copy Prompt) but appears inside the matching page's Audio section.

## Anti-slop / stop rules

- no new Production Asset Flow;
- no new root Skill or separate Production Asset Kit;
- no generic asset schema/registry/manifest;
- no Model/Texture/Animation/Particle/SFX component checklist;
- no empty category headings or zero-count categories;
- no duplicate shared assets per objective;
- no second default HTML;
- no duplicated Voice canonical data inside `asset-requirements.md`;
- no asset requirement invented by the renderer;
- no optional/decorative asset invented merely to fill a taxonomy;
- stop once the accepted PRD-derived requirements are actionable and the consolidated output is readable.
