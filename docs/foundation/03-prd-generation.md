# Flow 3 — Project Document / PRD Generation

Status: active durable policy

## Purpose

Turn a Flow 2 project marked `ready_for_prd` into canonical PRD meaning and a deterministic Golden-composed HTML presentation without reintroducing archived process ceremony.

## Authority chain

```text
Original Source + Approved Decisions
→ Requirement State / ready_for_prd
→ work/content.md                 canonical meaning
→ work/render-data.json           derived projection
→ Golden Sample renderer/template
→ output/final.html               derived presentation
```

Authority decreases downstream. Rendering cannot introduce project meaning.

## Canonical content

`work/content.md` is the Flow 3 source of truth. Detailed content/page-composition rules live in `kits/project-document-generator/CONTENT-CONTRACT.md`.

Required gameplay-document hierarchy:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Package/page counts follow the project. Golden authority means preserving hierarchy, information rhythm, component language, presentation foundation, **and the production function/depth of each surface**—not copying Aftershock-specific facts, counts, wording, or mechanics.

A shorter project may produce shorter pages. A detailed project must not be compressed into a skeletal document merely to minimize output. The target is **complete material information with no useless repetition**.

## Golden functional quality floor

For each corresponding surface, preserve the job the Golden Sample performs for its reader:

- Gameplay Flow → chronological player journey with context, actions, responses, consequences, and transitions;
- Gameplay Overview → enough local context to understand the package before implementation detail;
- Level Design → complete material build meaning;
- Developer → complete material runtime/state/scoring-or-result/data/interruption/reset/handoff meaning;
- Global Development → clear ownership of shared cross-package systems.

Do not use minimum word count, row count, or note count as a proxy for quality. Do not remove supported material meaning just because a compact representation is possible.

## Flow 2 intake boundary

Flow 3 receives resolved production meaning. It may organize, clarify, and humanize that meaning, but it must not silently choose a material product rule that Flow 2 should own.

Return the affected requirement to Flow 2 when drafting exposes a material gap in any of these areas:

- topology, package order, global/local ownership, transition, or final result;
- mechanic lifecycle behavior;
- contradictory numeric/timing/count/scoring facts;
- Objective Score versus No Objective Score;
- ambiguity between internal scoring/result, player-facing display, and telemetry/export behavior;
- wording so vague that materially different product behavior would still appear compliant;
- global/default rule conflicting with a package-specific exception;
- authoritative known project/platform/production constraint conflicting with requested behavior;
- missing Gameplay / Level Design / Developer implication;
- exclusion/removal or terminology ambiguity;
- another unresolved design/product choice.

Do not solve such a gap by inventing a metric, generic best practice, technical workaround, score rule, or renderer-friendly value. Qualitative direction may remain qualitative when it is intentionally so and production can proceed safely.

## Gameplay Flow authoring

Gameplay Flow is written as a concise player-facing production narrative, not an implementation checklist.

Use the actual project meaning to explain, where applicable:

```text
current player context
→ what the player sees/understands
→ NPC/system instruction or cue
→ player action
→ system/environment response
→ changed state / setback / recovery
→ result and next transition
```

The document should let a new developer or level designer understand the experience without reopening the source merely to learn what happens between objectives.

## Scoring / Result authoring

Every gameplay package states its result model explicitly:

```text
Objective Score exists
OR
No Objective Score
```

When a score exists, preserve applicable formula/components/timing/no-score/final-result behavior. When it does not, preserve valid completion/result and relationship to final result.

Do not treat `score not shown to player` or `score not exported` as `No Objective Score`. Keep internal score/result, player-facing display, and telemetry/export distinct whenever authority does.

## Development completeness

Flow 3 must preserve all material production meaning on the correct role surface.

- Level Design carries supported build-relevant areas, objects, routes/relationships, readability/sightlines, known size constraints, safe/recovery areas, interaction placement, boundaries, visual requirements, gameplay function, and important build notes when relevant.
- Developer carries supported activation/state/progression, interaction behavior, timing/quantities, scoring-or-result, display/export/data rules, interruption/disconnect, retry/reset/cleanup, transition/handoff, and important implementation notes when relevant.
- Shared rules may be referenced rather than copied, but a local page must still make the applicable shared behavior clear enough to work from.

If a role must reopen the original source to recover a material rule that belongs in the PRD, the canonical content is incomplete.

## Humanize before projection

After meaning is complete, apply one bounded Humanize pass to narrative/explanatory prose:

- use natural production sentences;
- explain context before dense detail;
- prefer cause → action → response → consequence;
- split unreadable comma-stacked requirement dumps;
- keep official terminology and exact technical values unchanged;
- keep tables/formulas/configuration precise;
- do not add unsupported cinematic/lore detail or promotional filler.

Humanize is part of authoring quality, not a new approval round or artifact.

## Projection and rendering

`render-data.json` is a compact disposable projection. It contains the values required to reproduce canonical meaning through the Golden surfaces. **Compact projection must not mean compressed meaning.**

The active renderer:

- derives project metadata/navigation/pages/glossary from render data;
- preserves Golden hierarchy/page composition/component language;
- uses the approved Golden template as runtime presentation authority;
- keeps project-specific local-storage/language/grid behavior bounded;
- never treats the template/sample as project fact.

Normal production does not load the full Golden HTML into model context; renderer/validator consume large HTML directly at runtime.

## Intentionally not adopted

Do not restore archived schema registries, mandatory Guided Discussion/Content Freeze rounds, generic template profiles, release/ZIP/checksum packaging, word-count validators, row-count validators, semantic similarity scoring, or visual similarity scoring without a concrete current need.

## Flow 3 completion

Flow 3 completes when:

- Flow 2 is truthfully `ready_for_prd`;
- canonical content satisfies the content/Golden composition **and functional quality** contract;
- Gameplay Flow explains the chronological player journey rather than only task labels;
- every gameplay package states Objective Score or explicit No Objective Score correctly;
- Level Design and Developer surfaces preserve complete material role-owned meaning;
- explanatory prose has received the bounded Humanize pass;
- no material Flow 2 intake issue was silently decided during drafting;
- derived render data passes applicable structural renderer checks;
- `final.html` is generated through the approved Golden family;
- generated navigation resolves;
- no required placeholder remains.

Flow 4—not rendering success—decides development readiness.
