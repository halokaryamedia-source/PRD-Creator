# PRD-Creator Context

Status: active production repository
Working branch: `Local`

## Product

PRD-Creator turns uneven project material into development-ready PRD documentation and, when needed, downstream Voice Production assets.

## Production sequence

```text
Flow 1  Repository Boot & Project Memory
Flow 2  Source Intake & Requirement Recovery
Flow 3  Project Document / PRD Generation
Flow 4  PRD Validation & Team Handoff
Flow 5  Voice Requirement Extraction
Flow 6  ElevenLabs Performance Script Production
Flow 7  Voice Validation & Delivery
```

Normal project creation/revision is **Production Execution**. `development-brief` is only for changing PRD-Creator itself.

## PRD operating direction

User effort stays low:

- internal project/workspace/bootstrap is automatic;
- source is inventoried/triaged before deep reading;
- only materially relevant evidence is read to the depth needed;
- Flow 2 solves before asking: recover from authority, apply safe Completion, or form a responsible Proposal before escalating;
- unresolved material decisions are grouped and explained in clear user-facing language;
- bounded revisions update only affected scope;
- internal state/evidence stays internal during normal delivery.

Efficiency applies to **reading and proof**, not to deleting material production meaning from the PRD.

## Golden Mandatory Contract

The approved Golden Sample defines the minimum document function for this gameplay PRD family. Its single semantic owner is:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

Other Flow 2–4 owners point to that file instead of maintaining their own Golden checklists.

The fixed family preserves:

```text
Overview
→ Gameplay Flow
     The Journey Begins
     one full flow page per package
→ Global Development
     Development Overview
     Session & Runtime System
     Data, Recovery & Reset
     Gameplay Package Integration
→ Gameplay Package(s)
     Gameplay Overview
     Level Design
     Developer
```

Projects do not copy Golden-specific facts/counts/mechanics. They fill the fixed functions with current-project truth.

Mandatory concerns resolve as:

```text
Defined | Explicit No | Not Applicable | Blocked
```

A mandatory concern does not disappear silently.

Key interpretation:

- Gameplay Flow = chronological player journey/context, not a task summary;
- every package states Objective Score or explicit No Objective Score;
- internal scoring/result, player-facing display, and telemetry/export remain separate unless authority joins them;
- Level Design and Developer pages carry complete material role-owned meaning;
- package terms use one canonical package glossary index that powers both inline term help and Terms Used;
- PRD prose is human-readable production language and closes already-resolved cause/action/result questions without changing exact technical facts.

## Reading experience

HTML remains a professional document, not a dashboard. Current direction prioritizes clarity and scanability:

- clear reading orientation before dense detail;
- structured Developer Flow rather than flattened requirement sentences;
- active-focused package navigation;
- readable production tables;
- restrained inline glossary highlighting/tooltips;
- distinct **Gameplay Journey** and **Full Production** reading modes;
- desktop-first proof by default.

Presentation improvements must not create or change project meaning.

## Proof direction

Default PRD visual proof is desktop-only and targeted. Mobile/responsive QA is run only when explicitly required or when the active defect is mobile-specific.

PRD and Voice CI are scoped separately so one domain does not rerun unrelated production contracts.

Do not repeat unchanged visual interactions or cross-flow tests merely for ceremony.

## Anti-overdevelopment

Prefer the smallest complete solution. Do not add skills, generic schemas, workflow engines, approval layers, generic parsers, template systems, extra checksums, word-count gates, row-count gates, semantic similarity scoring, or other machinery without a proved current need.

## Continuation

Read `docs/knowledge/next-action.md` for current status and the single next step.
