# Source Intake & Requirement Recovery

Status: active Flow 2 policy

## Purpose

Turn incomplete, uneven, duplicated, or partially conflicting project material into a reliable, traceable intake state before canonical PRD generation begins.

Flow 2 answers:

- what source exists;
- which source is authoritative, supporting, reference-only, generated, superseded, unavailable, or conflicting;
- what facts/requirements can be recovered directly;
- what can be clarified or completed safely;
- what is a real proposal requiring approval;
- what is blocked;
- whether the project is ready to enter Flow 3.

## Canonical Intake Sequence

```text
Incoming project material
↓
Preserve originals
↓
Source Inventory
↓
Read all available authoritative/supporting source
↓
Requirement Register
↓
Gap + conflict detection
↓
Clarification / Completion / Proposal / Blocked
↓
Resolve low-risk supported gaps automatically
↓
Ask only unresolved high-impact decisions
↓
Intake State
↓
ready_for_prd | needs_decision | blocked
```

## Source Roles

- `authoritative` — intended to define project facts/requirements;
- `supporting` — explains or supplements authoritative material;
- `reference` — sample/Golden/reference material; not project fact by default;
- `generated` — prior generated output retained for continuity/audit, not automatic authority.

## Source Precedence

Within a project:

1. current explicit user/creative-owner instruction;
2. approved project-specific decisions;
3. explicitly authoritative project source;
4. source explicitly established as superseding an older source;
5. supporting material;
6. generated prior output;
7. reference/Golden material for demonstrated structure/quality only.

Do not use file date alone to silently resolve a material contradiction.

## Recovery Classes

### Clarification

Meaning already exists. Improve wording/explanation without changing intent.

### Completion

Information is missing but strong surrounding evidence supports one reliable completion without defining a new material design choice.

### Proposal

The agent must define or choose a material project decision. Proposal requires approval and never self-approves.

### Blocked

Evidence is insufficient or materially conflicting and a reliable decision cannot be recovered.

`Conflict` is an evidence condition, not a fifth recovery class. If authority/supersession cannot resolve the conflict, the affected requirement is Blocked.

## Persistent Project State

Repository-backed projects use:

- `state/source-inventory.yaml` — source provenance and role;
- `state/requirement-register.yaml` — traceable requirement/gap/approval state;
- `state/intake-state.yaml` — one status and one next step;
- `work/review.md` — concise human-readable view.

Detailed field contract: `kits/project-document-generator/SOURCE-INTAKE.md`.

## Question Economy

Before asking the user:

1. inspect all available source;
2. inspect approved state/decisions;
3. recover obvious terminology and supported relationships;
4. use Clarification/Completion for low-risk supported gaps;
5. ask only unresolved high-impact Proposal/Blocked decisions.

Do not require a guided discussion merely because source wording is incomplete.

## Flow 2 Completion Gate

Flow 2 is complete only when:

- every available source is inventoried and inspected or explicitly unavailable/unreadable;
- every material requirement is traceable to source evidence or approved state;
- each identified gap has exactly one recovery class;
- conflicts are resolved or visibly Blocked;
- `intake-state.yaml` truthfully reports readiness;
- `ready_for_prd: true` is impossible while unresolved material Proposal/Blocked items still affect required output.

Flow 2 does not produce final PRD content or final HTML. Those belong to Flow 3.
