# PRD Semantic Content Contract

`work/content.md` is the canonical owner of PRD-core meaning. `work/render-data.json` and the generated PRD HTML are derived projections.

This file owns **what the PRD must communicate**. Visual/page composition is owned separately by [DESIGN-CONTRACT.md](DESIGN-CONTRACT.md).

## Authority

Project meaning follows, in descending authority:

1. current explicit user instruction;
2. approved project decisions;
3. current authoritative project source;
4. normalized approved requirement state;
5. references only for representation/quality, never another project's facts.

Every material concern resolves as:

```text
Defined | Explicit No | Not Applicable | Blocked
```

`missing` is not a valid accepted state.

## Material conservation

Flow 3 may rewrite wording and choose representation inside approved surfaces. It may not delete independently actionable meaning merely to make the PRD shorter or to match a sample count.

Conserve every resolved PRD-scope rule that changes production or observable behavior, including:

- conditions and exceptions;
- timing, counts, capacities, scoring/result values;
- success/fail/retry/recovery behavior;
- interruption/reset behavior;
- shared/local ownership boundaries;
- build/spatial constraints;
- explicit approved technical constraints;
- required player-visible/system results.

The invariant is:

```text
resolved material rule
→ one canonical readable representation
→ one appropriate visible PRD surface
```

Two rules may be merged only when they remain independently understandable. Humanize/concise writing changes wording, not meaning cardinality.

Do not reintroduce incidental as-built evidence that Flow 2 intentionally excluded from canonical project meaning, such as final map coordinates, UUIDs, scoreboard names, function paths, debug/setup residue, or implementation identifiers that are not approved constraints.

## Semantic document family

The PRD core remains:

```text
01 Overview

02 Gameplay Flow
   The Journey Begins
   one flow page per gameplay package

03 Development
   Development Overview
   Game System
   Data and Reset
   Gameplay Development

04+ Gameplay Packages
   Gameplay Overview
   Level Design
   Developer
```

For `N` gameplay packages, the PRD core remains `6 + 4N` pages. This is information architecture, not a rule about how many cards or beats must appear inside a page.

## Overview meaning

Overview must establish:

- one readable project/session/journey context;
- **Session Model**;
- **Target Playtime**;
- **Game Structure**;
- one chronological journey summary per gameplay package plus the opening when applicable;
- project-wide gameplay direction/invariants that materially affect multiple packages.

The three named fact slots are stable semantic questions, not arbitrary sample filler.

## Gameplay Flow meaning

Each Gameplay Flow page is chronological player-facing truth. It must make clear, as applicable:

```text
situation
→ player action
→ visible/system response
→ setback/recovery
→ changed state/result
→ transition
```

Narrative sections/paragraphs are **data-driven**. Use as many as the material meaning requires. Do not create filler beats and do not compress distinct conditions merely to imitate the reference project.

## Global Development meaning

The four project-wide Development pages have stable responsibilities:

| Page | Owns |
|---|---|
| Development Overview | project-wide topology, package relationships, shared handoff/result structure |
| Game System | shared runtime/session ownership, isolation, global player/objective state |
| Data and Reset | timing/data/result persistence, interruption, recovery/reset and reuse |
| Gameplay Development | common implementation contract across gameplay packages |

Each page requires:

- a compact overview of responsibility/boundary;
- one or more useful lifecycle/orientation steps;
- actionable Development Requirements;
- one or more genuinely important risk/invariant notes when such notes exist;
- relevant Terms Used when needed.

**Do not force four flow cards or four notes.** Cardinality follows project meaning.

## Gameplay Overview meaning

The stable summary questions are:

- Gameplay Context;
- Main Objective;
- Result.

Gameplay Information keeps these six semantic questions:

- Game Purpose;
- Gameplay Time;
- Starting Condition;
- End Condition;
- Fail Condition;
- Scoring Criteria.

A negative rule remains explicit, e.g. `No Objective Score` or `There is no fail state`.

The compact Gameplay Flow is **data-driven**. Use one or more high-level steps sufficient to communicate the actual sequence. Five steps are valid when the project naturally has five; five is not a universal contract.

## Level Design meaning

Level Design must communicate:

- spatial/build responsibility and relationships;
- one or more useful Design Flow stages/areas;
- complete Build Requirements;
- important spatial/readability/hazard/recovery constraints when they exist.

Build Requirements retain the stable semantic columns:

```text
No. | Object | Area Size | Build and Visual Requirements | Gameplay Function
```

Flow-card and note-card counts are data-driven. Requirement row/group counts are data-driven.

## Developer meaning

Developer must communicate:

- runtime responsibility;
- one or more useful implementation lifecycle steps;
- complete Development Requirements;
- result/scoring or explicit no-score completion behavior;
- interruption/reset/reuse/handoff behavior;
- important runtime invariants when they exist.

Development Requirements retain:

```text
No. | Setup | Development Requirements | Gameplay Function
```

Flow-card and note-card counts are data-driven. Requirement row/group counts are data-driven.

## Adaptive cardinality rule

The model must not ask, “How do I make this exactly four cards/five beats?” It must ask, “How many distinct steps are actually needed to communicate the approved meaning clearly?”

Use the smallest cardinality that preserves material distinctions:

```text
1+ semantic steps/notes when applicable
→ no filler to reach a sample count
→ no destructive merging to reduce to a sample count
```

The renderer may wrap/reflow variable item counts inside the same approved component family. That is representation, not a new project decision.

## Humanize and direct writing

Prefer:

- direct subject/action/result wording;
- specific project nouns;
- semantic note titles;
- compact summaries with detail in the owning requirement surface;
- chronological flow where chronology matters.

Avoid:

- generator/template narration;
- generic `Global Rule N` / `Important Note N` visible copy;
- vague `handle`, `manage`, `support` wording without observable behavior;
- repeated explanation across Gameplay, Level Design and Developer when ownership differs.

## Flow 3 completion

Flow 3 is complete when:

- Flow 2 truthfully remains `ready_for_prd`;
- canonical PRD meaning satisfies this semantic contract;
- no material project decision was silently invented during authoring;
- all material meaning can be projected through the approved design contract;
- no unresolved placeholder remains.

If a material project/design decision is unresolved, return the affected slice to Flow 2. If the meaning is correct but presentation cannot represent it, the first wrong owner is the design/projection layer—not the project facts.

## Compatibility routing for older instructions

Older procedure text may refer to the “Reverse-derived Golden fill map” in this file. That presentation map now belongs to [DESIGN-CONTRACT.md](DESIGN-CONTRACT.md). The semantic questions remain here; the Golden visual grammar and reference evidence live there.
