# Document Profiles

## Purpose

Document Profile defines hierarchy, mandatory sections, package structure, and
rendering behavior. Action Mode remains separate.

## 1. Complete Game/Map — `complete_game_map`

Use for story maps, adventure maps, campaigns, or connected objectives where one
package result becomes the next package input.

```text
01 — Overview
02 — Gameplay Flow
     Opening / major gameplay pages / Ending
03 — Development
     Development Overview
     Game System
     Data and Reset
     Gameplay Development
     Each package: Gameplay Overview / Level Design / Developer
```

Validate journey order, package handoffs, item transfer, scoring dependencies,
ending result, and global-system consistency.

## 2. Multi-Stage Game — `multi_stage_game`

Use for stations, rounds, tiers, or arenas in one session where rotation, global
scoring, leaderboard, and reset are central.

```text
01 — Overview
02 — Gameplay Flow
     Pre-game / session / station pages / final result
03 — Development
     Session and Arena System
     Global Scoring
     Data and Leaderboard
     Reset System
     Each stage: Gameplay Overview / Level Design / Developer
```

Validate stage order, session/stage timers, score aggregation, leaderboard data,
retry/skip behavior, concurrency, and reset isolation.

## 3. Single Gameplay — `single_gameplay`

Use for one standalone gameplay loop or minigame.

```text
01 — Overview
02 — Gameplay Flow
03 — Development
     Optional global pages
     Gameplay Overview / Level Design / Developer
```

Level Design is optional only when no world or arena build is required.

## 4. Game System or Module — `game_system_module`

Use for reusable modules, frameworks, databases, kit systems, arena systems, or
integration-focused mechanics.

```text
01 — System Overview
02 — System Flow
03 — Development
     Architecture
     Requirements
     Configuration
     Integration
     Data Handling
     Error Handling
     Lifecycle and Cleanup
     Usage Guide
```

Do not include Level Design by default. Add it only for physical world anchors,
regions, NPCs, machines, or layouts.

## 5. Specialized Document — `specialized_document`

Supported specializations:

- `gameplay_design_only`
- `level_design_only`
- `developer_only`
- `scoring_and_data_only`
- `audit_only`

A focused document must still contain enough local context for its reader.

## Selection Rules

Choose `complete_game_map` for a connected player journey; `multi_stage_game` for
independent scored stages in one session; `single_gameplay` for one loop;
`game_system_module` for reusable logic; `specialized_document` for a focused
role artifact.

When two profiles are plausible, ask one decisive question rather than listing
all profiles.

## Profile Change

A profile change requires impact analysis, user approval, state update,
Structured Content remapping, and re-audit. Never delete previously approved
content automatically.

## Golden Sample Use

AFTERSHOCK is the exact visual and interaction benchmark for
`complete_game_map`. Other profiles adapt the hierarchy but remain in the same
visual family. Never copy AFTERSHOCK-specific story content into unrelated work.
