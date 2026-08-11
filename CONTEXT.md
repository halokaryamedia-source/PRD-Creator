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

- workspace/bootstrap is automatic;
- source is triaged by authority/relevance before deep reading;
- Flow 2 resolves supported meaning before asking for decisions;
- only unresolved material decisions are surfaced;
- bounded revisions update only invalidated scope;
- internal state/evidence stays internal during normal delivery.

Efficiency applies to reading and proof, not to deleting material production meaning.

## Gameplay PRD contract

The approved Golden Sample defines the minimum document function/quality expected from this gameplay PRD family. The single semantic owner is:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

The fixed family is:

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

Projects fill these functions with current-project truth; reference-project facts/mechanics do not transfer automatically.

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
- `packages[].terms` is the canonical package glossary index;
- PRD prose is human-readable production language and closes already-resolved cause/action/result questions without changing technical facts.

## Presentation direction

HTML remains a professional document, not a dashboard.

- `approved-document.html` is generic PRD presentation/runtime infrastructure;
- stable component/runtime names describe function, not implementation history or a reference project;
- project `document.version` is real document metadata, not presentation-patch numbering;
- Gameplay Journey and Full Production are the two reading views;
- package terminology can be highlighted through the shared glossary index;
- generated HTML is derived and is never manually patched.

## Proof direction

Default PRD visual proof is desktop-only and targeted. Mobile/responsive QA is run only when explicitly required or when the active defect is mobile-specific.

PRD and Voice CI are scoped separately so one domain does not rerun unrelated production contracts.

Do not repeat unchanged visual interactions or cross-flow tests merely for ceremony.

## Anti-overdevelopment

Prefer the smallest complete solution. Do not add skills, generic schemas, workflow engines, approval layers, generic parsers, template systems, extra checksums, word-count gates, row-count gates, semantic similarity scoring, or other machinery without a proved current need.

## Continuation

Read `docs/knowledge/next-action.md` for current status and the single next step.
