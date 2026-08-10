# Source Intake & Requirement Recovery

Status: active Flow 2 policy

## Purpose

Turn uneven, duplicated, incomplete, or partially conflicting project material into a reliable intake state before canonical PRD generation, while minimizing unnecessary user questions and model context.

## Canonical sequence

```text
Incoming project material
↓
Preserve + inventory originals
↓
Relevance/authority triage
↓
Deep-read material authoritative source
+ targeted-read supporting/reference/generated source as needed
↓
Requirement recovery
↓
Clarification / Completion / Proposal / Blocked
↓
Resolve low-risk supported gaps automatically
↓
Ask only unresolved high-impact decisions
↓
ready_for_prd | needs_decision | blocked
```

Inventory completeness and reading depth are different concerns. All material sources are tracked, but the model does not need to consume every byte of every supporting/reference/generated file. If a source could materially alter current scope and relevance is uncertain, inspect it rather than assuming it is irrelevant.

## Source roles

- `authoritative` — intended to define project facts/requirements;
- `supporting` — explains or supplements authoritative material;
- `reference` — sample/Golden/reference material; not project fact by default;
- `generated` — prior generated output retained for continuity/audit, not automatic authority.

## Source precedence

1. current explicit user/creative-owner instruction;
2. approved project-specific decisions;
3. authoritative current project source;
4. source explicitly established as superseding older material;
5. supporting material;
6. generated prior output;
7. reference/Golden material for demonstrated structure/quality only.

Do not use file date alone to resolve material contradictions.

## Recovery classes

- **Clarification** — improve explanation without changing existing meaning.
- **Completion** — one low-risk completion is strongly supported by surrounding evidence.
- **Proposal** — a material project decision must be chosen; approval is required.
- **Blocked** — evidence is insufficient or materially conflicting.

Conflict is an evidence condition, not a fifth recovery class.

## Persistent state

Repository-backed Flow 2 uses:

- `state/source-inventory.yaml` — compact source identity/provenance/exception state;
- `state/requirement-register.yaml` — compact traceable requirements and only non-default recovery/approval exceptions;
- `state/intake-state.yaml` — one current status, explicit positive readiness, and one next step;
- `work/review.md` — conditional human-facing decision/recovery summary only when useful.

Do not persist empty/default fields merely to make records look uniform. Sparse state must preserve the same semantics and must never hide a conflict, pending approval, or material gap.

Detailed field/default contract: `kits/project-document-generator/SOURCE-INTAKE.md`.

## Question economy

Before asking the user:

1. triage all current source;
2. inspect material authoritative source and only the supporting/reference/generated portions needed for current scope;
3. inspect approved state/decisions;
4. apply low-risk Clarification/Completion;
5. ask only unresolved high-impact Proposal/Blocked decisions, grouped when possible.

Zero questions is preferred when the project is already sufficiently defined.

## Flow 2 completion gate

Flow 2 is complete only when:

- every source that can materially affect current scope is inventoried and inspected to sufficient depth or explicitly unavailable/unreadable;
- every material requirement is traceable to source evidence or approved state;
- material gaps/conflicts are resolved or visibly Proposal/Blocked;
- intake state truthfully reports readiness;
- `ready_for_prd: true` cannot coexist with an unresolved material Proposal/Blocked item affecting required output.

Flow 2 does not produce final PRD content or final HTML. Those belong to Flow 3.