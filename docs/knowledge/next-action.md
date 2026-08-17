# Next Action

## Current Status

`MAP_COMPOSITION_AUDIT_READY_FOR_NEW_SESSION`

The unified `kits/prd-creator/` migration and Clockwork browser visual QA are complete. The user has approved a new bounded audit phase focused on understanding the **professional composition of a finished/developed Minecraft map** from representative real development outputs before changing PRD-Creator.

## Active Boundary

This phase is **Map Composition Audit / Content Audit**. It is an evidence-gathering and synthesis phase, not immediate renderer, Golden, contract, architecture, or project implementation work.

The purpose is not merely to judge which document looks better. The purpose is to inspect actual developed maps and answer:

> What concrete design, level, runtime, content, asset, configuration, and QA components together make a professional map a finished playable product, and what information should a professional PRD/handoff capture so another team can understand, build, implement, test, maintain, or hand it off?

Do not implement PRD-Creator improvements until the sample evidence has been synthesized and the user explicitly approves the resulting proposal.

## Official Working Sample Set

The earlier combined archive `ChoosenSamples (2).zip` was split by the user into one ZIP per map to make inspection easier. **Use the six per-map ZIPs below as the current working sample set.** The combined ZIP does not need to be used when the six split archives are available.

```text
3#Angry bird.zip          47,250,776 bytes
6#Avatar_Legends.zip      35,917,220 bytes
16#Ice Age.zip           221,525,195 bytes
23#Sherlock Holmes.zip    54,752,510 bytes
24#Minions DLC.zip       111,197,100 bytes
29#NinjaWeaponAcademy.zip 36,383,129 bytes
```

The mistakenly uploaded Clockwork responsive-fix ZIP is explicitly excluded from this audit. Do not use prior unrelated Clockwork HTML/review artifacts as substitutes for these samples.

A new chat should expect the user to upload these same six archives again if conversation attachments are not available across sessions.

## Session Capability Note

The previous chat could see all six ZIP attachments correctly, but its local filesystem runtime failed with `ClientError` for both container and Python file access. Because of that environment failure, **none of the six map archives has been unpacked or audited yet**.

This is not evidence that the ZIPs are corrupt or unsupported.

In a new session:

```text
read repository boot owners
→ read this next-action.md
→ use the six per-map ZIPs as the audit source
→ attempt direct extraction/inventory with the local/container/Python runtime
→ if extraction works, continue the audit without asking the user to prepare FILE-TREE.txt or manually filter files
```

The user explicitly prefers ChatGPT to perform the extraction, inventory, and source selection itself. Do **not** ask the user to understand pack structure, create file lists, or manually select JSON/script files unless the new runtime genuinely cannot access the archives after one direct attempt.

If the new runtime also fails at filesystem access, report that capability blocker clearly rather than pretending the map contents were read.

## Audit Goal

Determine from the actual development samples **what concrete components together make each map a finished playable product** and what information a professional production document should represent.

The audit is not limited to prose/document quality. Inspect every relevant development artifact and recover the real production anatomy of the map.

Potential categories to test against evidence include:

```text
project / map identity and scope
player experience and intended flow
gameplay rules and objective progression
level / environment design
coordinates, zones, checkpoints, spawn and teleport points
logic / scripting / state machines / triggers
entities, NPCs, mobs and behavior
items, blocks, structures and interactables
UI, text, hints, tutorials and player feedback
audio, voice, music and sound effects
visual effects / particles / animation / camera
resource-pack / behavior-pack / world/data dependencies
models, textures and other production assets
scoring, timers, rewards, progression and persistence
multiplayer / session / arena behavior when present
reset, retry, fail, recovery and edge-case behavior
configuration / tuning values
testing / QA / known issues / acceptance evidence
build / developer handoff information
packaging / delivery / versioning where present
```

These are **audit hypotheses**, not assumed requirements. A category becomes part of the professional map model only when the sample evidence supports it or when a later explicit product decision approves it.

## Audit Method

For each of the six maps:

```text
1. Inventory actual archive contents and folder/file structure.
2. Identify the world, Behavior Pack, Resource Pack, scripts/functions, configuration, data, and production assets actually present.
3. Read relevant text/source artifacts such as manifest, JSON, JS/TS, mcfunction, lang/text/UI/config files, and documentation.
4. Identify what each artifact contributes to the map instead of classifying by extension alone.
5. Map dependencies between world/level content, gameplay logic, entities/interactables, assets, UI/audio, configuration, and runtime state.
6. Reconstruct the player-facing flow: start → objectives/progression → feedback → fail/retry/reset → completion.
7. Reconstruct the implementation-facing flow: initialization → state/trigger logic → content/assets → persistence/reset → delivery.
8. Identify what configuration/tuning data is required to reproduce behavior.
9. Identify what QA/proof is needed to know the map is actually complete.
10. Record evidence before deciding whether a component is core, optional, or sample-specific.
```

Do not spend audit effort deeply inspecting every heavy binary asset when filenames, manifests, references, and source/config already establish its production role. Inspect binary/media content only when needed to resolve a material question.

Then compare across all six maps:

```text
sample-specific content
vs
recurring professional map component
vs
optional / specialized component
vs
redundant / noisy development artifact
```

The audit must distinguish:

```text
sample fact
→ directly evidenced by supplied development output

inference
→ derived from relationships between supplied artifacts

professional synthesis
→ reusable map-production model proposed from recurring evidence

PRD-Creator requirement
→ remains a proposal until explicitly approved
```

## Expected Audit Output

After the six samples are readable and inspected, produce:

1. **Per-map inventory** — what each developed map actually contains and what those artifacts do.
2. **Cross-sample matrix** — which production components occur in which maps.
3. **Professional Map Anatomy / Map Production Model** — the recurring components that make a map complete.
4. **Core vs Conditional vs Specialized** — evidence-based classification, not theory-first assumptions.
5. **Dependency chain** — how design, level/world, runtime logic, assets, player communication, configuration, reset/persistence, and QA depend on each other.
6. **Professional documentation needs** — what information a PRD/handoff should capture for each component so a builder/developer/designer/production/QA team can act on it.
7. **PRD-Creator comparison** — what current sections already cover, what is missing, too vague, duplicated, or owned in the wrong place.
8. **Prioritized improvement proposal** — recommended content/system improvements with exact owner boundaries, without implementation until user approval.

The desired end result is a professional answer to:

> “What is actually inside a finished map, and what must we know/document in advance to build one professionally?”

## Existing Accepted Baseline

The previous visual acceptance remains valid and is not reopened by this audit:

```text
Golden/runtime template Git blob
2050b965768489feda98373c2920bbee8c7093b3

Clockwork prd.html Git blob
3267b2f97e7335418a43edd6b0e81f6077aeeb51

Project HTML Visual: PASS
```

## Protected Boundary

Until the actual sample artifacts are read and the audit is synthesized:

- do not change gameplay/project meaning;
- do not change Voice requirements or wording;
- do not change Golden/template/renderer to imitate assumptions;
- do not redesign repository architecture;
- do not change accepted Clockwork output;
- do not promote conditional backlog items;
- do not turn theoretical categories above into mandatory schemas/requirements;
- do not infer sample contents from file names, IP/theme knowledge, or general Minecraft conventions.

## Recovery for a New Chat

The shortest correct continuation is:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules
→ CONTEXT.md
→ this next-action.md
→ receive/access the six per-map ZIPs
→ extract and inventory them directly
→ begin Map Composition Audit
```

Do not repeat the completed unified-kit migration or Clockwork browser QA. Do not ask the user to restate the audit goal. Do not ask them to manually prepare `FILE-TREE.txt` if direct ZIP extraction works in the new runtime.

## Next Step

**In a fresh runtime/session, directly unpack and inventory the six per-map development ZIPs, inspect the relevant source/config/assets relationships, reconstruct each map's real production anatomy, then perform the cross-sample Map Composition Audit. Do not modify PRD-Creator until the evidence-backed improvement proposal is presented to and approved by the user.**
