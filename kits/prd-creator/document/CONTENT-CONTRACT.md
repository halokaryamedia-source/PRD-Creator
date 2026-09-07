# PRD Semantic Content Contract

`work/content.md` is the canonical owner of PRD-core meaning. `work/render-data.json` is a strict machine projection of that meaning. Generated HTML is presentation only.

This file owns **what the PRD must communicate**. Visual/page composition is owned by [DESIGN-CONTRACT.md](DESIGN-CONTRACT.md). The exact render-data field schema is implemented by `shared/render_schema.py`; do not duplicate that schema in other docs.

## Authority

Project meaning follows:

1. current explicit user instruction;
2. approved project decisions;
3. current authoritative source;
4. the exact preview-approved requirement register;
5. representation references only for structure/quality.

Every material concern must resolve as:

```text
Defined | Explicit No | Not Applicable | Blocked
```

`missing` is not an accepted state.

## Material conservation

Flow 3 may rewrite wording and choose representation inside approved surfaces. It may not delete independently actionable meaning for brevity or sample-count fidelity.

Conserve every resolved rule that changes production or observable behavior, including conditions/exceptions, timing/counts, scoring/results, fail/retry/recovery, reset/interruption, shared/local ownership, build/spatial constraints, approved technical constraints, and required player-visible/system results.

```text
resolved material rule
→ one canonical readable representation
→ one appropriate visible PRD surface
```

Do not reintroduce incidental as-built evidence intentionally excluded by Flow 2, such as final coordinates, UUIDs, scoreboard names, function paths, or debug/setup residue that are not approved constraints.

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

For `N` gameplay packages, the core remains `6 + 4N` pages. Child-card/beat/note counts are data-driven.

## Overview

Overview establishes:

- project/session/journey context;
- **Session Model**;
- **Target Playtime**;
- **Game Structure**;
- chronological journey summary;
- project-wide gameplay direction/invariants.

The three named facts are fixed semantic questions, not sample filler.

## Gameplay Flow

Each page communicates chronological player-facing truth:

```text
situation
→ player action
→ visible/system response
→ setback/recovery
→ changed state/result
→ transition
```

Use only as many beats as the approved meaning needs.

## Global Development

The four project-wide Development pages have fixed ownership:

| Page | Owns |
|---|---|
| Development Overview | topology, package relationships, shared handoff/result structure |
| Game System | shared runtime/session ownership, isolation, global state |
| Data and Reset | timing/data/result persistence, interruption, recovery/reset/reuse |
| Gameplay Development | common implementation contract across gameplay packages |

Each page needs a clear responsibility overview, useful lifecycle steps, actionable requirements, and genuine risk/invariant notes when applicable.

## Gameplay Overview

Stable summary questions:

```text
Gameplay Context
Main Objective
Result
```

Stable Gameplay Information questions:

```text
Game Purpose
Gameplay Time
Starting Condition
End Condition
Fail Condition
Scoring Criteria / Completion Result
```

The last question is represented in machine projection through one explicit result model:

```json
{
  "result_model": {
    "mode": "scored | completion_only",
    "summary": "<player/production-facing result summary>"
  }
}
```

`mode: scored` requires Developer `scoring`. `mode: completion_only` requires Developer `completion_data`. The renderer never infers this mode or synthesizes the Gameplay result summary from Developer data.

## Level Design

Level Design communicates spatial/build responsibility, design flow, complete build requirements, and applicable spatial/readability/hazard/recovery constraints.

Stable columns:

```text
No. | Object | Area Size | Build and Visual Requirements | Gameplay Function
```

## Developer

Developer communicates runtime responsibility, lifecycle, complete implementation requirements, explicit scored/no-score result handling, interruption/reset/reuse/handoff, and applicable runtime invariants.

Stable columns:

```text
No. | Setup | Development Requirements | Gameplay Function
```

## Adaptive cardinality

Use the smallest child cardinality that preserves all material distinctions:

```text
1+ semantic steps/notes when applicable
→ no filler for sample counts
→ no destructive merging for compactness
```

## Strict projection boundary

`render-data.json` is not a tolerant intermediate format. It has exactly one supported field vocabulary.

Required invariants:

```text
content.md bytes
→ canonical_content_sha256 in render-data
→ exact strict projection
→ deterministic renderer
```

The projection must:

- bind `canonical_content_sha256` to the exact current `work/content.md` bytes;
- use only fields accepted by `shared/render_schema.py`;
- carry resolved `result_model` explicitly;
- preserve stable package/term IDs;
- contain no compatibility aliases or unknown keys;
- contain explicit `en/id` values when bilingual mode is active;
- preserve numeric, percentage, and stable-ID tokens across bilingual values.

The renderer must not:

- recover historical aliases;
- reinterpret a typo as another field;
- infer missing semantic meaning from another role;
- create scoring/completion meaning;
- copy Golden sample facts.

If canonical meaning is incomplete, return the affected slice to Flow 2. If canonical meaning is complete but cannot fit the approved presentation grammar, the design/projection layer is the first wrong owner.

## Humanize and direct writing

Prefer direct subject/action/result wording, specific project nouns, semantic note titles, chronological flow when chronology matters, and detail in the owning role.

Avoid generator narration, generic `Global Rule N` / `Important Note N`, vague ownership verbs without observable behavior, and repetitive cross-role restatement.

## Flow 3 completion

Flow 3 completes only when:

- Flow 2 approval is still bound to the current requirement-register bytes;
- `content.md` satisfies this semantic contract;
- `render-data.json` exactly binds current content bytes and satisfies the strict projection schema;
- no material project decision was silently introduced during authoring;
- semantic cardinality is conserved;
- current 01–03 HTML is deterministically rendered;
- no unresolved placeholder remains.

Flow 4, not renderer success, decides accepted production readiness.
