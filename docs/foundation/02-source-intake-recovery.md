# Source Intake & Requirement Recovery

Status: active Flow 2 policy

## Purpose

Turn uneven project material into a trustworthy production requirement state before PRD drafting. Flow 2 must recover not only explicit statements, but also project topology, required cross-role implications, exclusions, terminology, and material gaps without inventing unsupported design choices.

## Canonical sequence

```text
Preserve + inventory source
↓
Authority/relevance triage + sufficient inspection
↓
Recover explicit facts/rules/exclusions
↓
Recover project topology + terminology
↓
Cross-role implication pass
↓
Production coverage scan
↓
Clarification / Completion / Proposal / Blocked
↓
One grouped material decision batch only if needed
↓
ready_for_prd | needs_decision | blocked
```

Inventory completeness and reading depth are different concerns. Supporting/reference/generated material need only be read to the depth required by current scope; uncertain evidence that could materially change the PRD must still be inspected.

## Source authority and persistence

Precedence:

1. current explicit user/creative-owner instruction;
2. approved project decisions;
3. current authoritative project source;
4. explicitly superseding source/decision;
5. supporting material;
6. generated prior output;
7. reference/Golden material for demonstrated structure/quality only.

Material user instructions must be persisted in source inventory even when no file exists. Do not rely on chat history as the only durable authority.

Persist reading coverage compactly (`targeted` + scope or `full`) when it materially helps resumability. Source-level supersession applies only when the whole source is superseded; partial changes are resolved at the affected claim/requirement.

## Recovery behavior

- Recover explicit positive and negative constraints (`remove`, `do not use`, `replaced by`, `only`, etc.).
- Recover ordered packages/stages, shared/global ownership, dependencies/transitions, and final result when needed by the project.
- Normalize terminology when multiple labels may refer to one project concept; unresolved ambiguity is surfaced rather than synonym-cycled.
- For each material mechanic/system, inspect necessary implications for Gameplay, Level Design, Developer, and result/reset/handoff.
- Record only implications logically required by source/approved state; do not invent exact quantities, timings, objects, dimensions, implementation architecture, or decorative detail.

## Coverage and materiality

Before readiness, scan applicable concerns for:

- project topology/global ownership;
- Gameplay objective/start/end/fail-or-retry/result;
- Level Design areas/objects/relationships/known constraints/gameplay function;
- Developer activation/state/completion-or-score/timing/data/reset/interruption/result;
- critical counts, timing boundaries, scoring, handoff, reset/disconnect, and final-result rules when relevant.

This is not a mandatory-field form. Irrelevant or intentionally unspecified detail is not a gap.

A missing detail is material only when leaving it unresolved forces a downstream role to make a product/design decision or changes player experience, build scope, runtime behavior, scoring/completion, timing, handoff, reset/interruption, or final result.

## Safe Completion boundary

Use Completion only when one reliable completion follows from existing evidence/necessary implication at the abstraction needed by the PRD, without choosing among multiple plausible designs or inventing unsupported values/implementation detail.

If a material gap does not meet that test, use Proposal or Blocked. Clarification only improves existing meaning.

## Persistent state

Repository-backed Flow 2 uses:

- `state/source-inventory.yaml` — compact source/provenance/inspection/exception state;
- `state/requirement-register.yaml` — explicit and recovered production requirements, including exclusions/topology/terminology/cross-role implications where material;
- `state/intake-state.yaml` — one status, explicit positive readiness, and one next step;
- `work/review.md` — conditional decision/recovery summary only when useful.

Sparse state may omit defaults, but must never hide conflict, pending approval, blocker, supersession, inspection boundary needed for continuation, or material recovery class.

Detailed contract: `kits/project-document-generator/SOURCE-INTAKE.md`.

## Question economy

Ask only after explicit recovery, topology/terminology/exclusion reconciliation, cross-role implications, and coverage scan have been attempted. Group remaining high-impact Proposal/Blocked decisions. Zero questions is preferred when evidence is sufficient.

## Flow 2 completion gate

`ready_for_prd` requires:

- materially relevant source inspected to sufficient depth;
- material user instructions persisted;
- explicit rules/exclusions recovered;
- sufficient project topology for Flow 3;
- material terminology ambiguity resolved or surfaced;
- necessary cross-role implications recovered;
- production coverage scan complete for applicable concerns;
- every material requirement traceable to evidence/approved state;
- every Completion within the safe-completion boundary;
- no unresolved material Proposal/Blocked item affecting requested output.

Flow 3 may organize and polish approved meaning, but must not become the first place required product structure/implications/decisions are invented.
