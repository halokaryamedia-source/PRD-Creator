# Source Intake & Requirement Recovery

Status: active Flow 2 policy

## Purpose

Turn uneven project material into a trustworthy production requirement state before PRD drafting. Flow 2 must recover explicit meaning, project structure, required implications, exclusions, terminology, missing material behavior, and practical resolutions without inventing unsupported design choices.

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
Production coverage + mechanic lifecycle + quantitative coherence
↓
Problem framing + Resolution Ladder
↓
Impact propagation
↓
Humanized grouped decision package only if needed
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
- Normalize terminology when multiple labels may refer to one concept; unresolved ambiguity is surfaced rather than synonym-cycled.
- For each material mechanic/system, inspect necessary implications for Gameplay, Level Design, Developer, and result/reset/handoff.
- Record only implications logically required by source/approved state; do not invent exact quantities, timings, objects, dimensions, implementation architecture, or decorative detail.

## Coverage, lifecycle, and quantitative coherence

Before readiness, scan only applicable concerns for:

- project topology/global ownership;
- Gameplay objective/start/end/fail-or-retry/result;
- Level Design areas/objects/relationships/known constraints/gameplay function;
- Developer activation/state/completion-or-score/timing/data/reset/interruption/result;
- critical counts, timing boundaries, scoring, handoff, reset/disconnect, and final-result rules.

For each material mechanic, inspect relevant lifecycle stages: precondition, trigger, active behavior, success, fail/timeout/interruption, result/transition, and retry/reset. Missing lifecycle stages are material only when a downstream role cannot proceed safely without them.

When related numeric facts exist, check that they can coexist: total duration vs phase durations, capacity/count assumptions, scoring weights, repeated object/stage counts, and other directly related values. A mismatch is evidence to resolve, not permission to silently change a number.

This is not a mandatory-field form. Irrelevant or intentionally unspecified detail is not a gap.

## Problem-solving boundary

Flow 2 should help solve a material issue before asking the user.

First frame the actual problem using observed issue, consequence, project constraints, intended outcome, and affected roles. Then use the least-assumptive Resolution Ladder:

1. existing authority resolves it → recover;
2. one necessary evidence-backed result exists → Completion;
3. multiple options exist but one responsible recommendation follows from project goals/constraints → Proposal with one recommendation;
4. no responsible resolution can be made → Blocked/direct decision.

A source can also expose a concrete gameplay/production concern even when documentation is complete. Such concern is advisory only until approved; it does not become a new recovery class.

## Safe Completion and materiality

Use Completion only when one reliable result follows from evidence/necessary implication at the abstraction needed by the PRD, without choosing among multiple plausible designs or inventing unsupported values/implementation detail.

A missing detail is material only when leaving it unresolved forces a downstream role to make a product/design decision or changes player experience, build scope, runtime behavior, scoring/completion, timing, handoff, reset/interruption, or final result.

If a material gap does not meet the Completion test, use Proposal or Blocked. Clarification only improves existing meaning.

## Impact propagation

A recovered Completion or approved Proposal must be reconciled across all actually affected requirements: topology/global ownership, Gameplay, Level Design, Developer, timing/quantities/scoring, transition/handoff, and retry/reset/interruption where relevant.

Use existing requirements + `affects`; do not create a dependency-graph artifact. Resolve partial supersession at claim level.

## User-facing resolution communication

Group related issues into one solution package when one root decision resolves them. Default to one recommended option; add at most 1–2 alternatives only when they represent meaningful tradeoffs.

Use a bounded Humanize pass on Flow 2 user-facing explanations:

```text
Masalah
Saran
Kenapa
Dampak
Alternatif — only when useful
```

Humanize improves clarity/order and hides unnecessary internal jargon. It must never alter official terminology, quantities, timings, formulas, triggers, mechanics, uncertainty, provenance, or approval state. It is presentation behavior, not a new authority/recovery class/root skill.

## Persistent state

Repository-backed Flow 2 uses:

- `state/source-inventory.yaml` — compact source/provenance/inspection/exception state;
- `state/requirement-register.yaml` — explicit and recovered production requirements, including exclusions/topology/terminology/cross-role implications where material;
- `state/intake-state.yaml` — one status, explicit positive readiness, and one next step;
- `work/review.md` — conditional human-facing solution/decision summary only when useful.

Sparse state may omit defaults, but must never hide conflict, pending approval, blocker, supersession, inspection boundary needed for continuation, or material recovery class.

Detailed contract: `kits/project-document-generator/SOURCE-INTAKE.md`.

## Question economy

Ask only after explicit recovery, topology/terminology/exclusion reconciliation, cross-role implications, coverage/lifecycle/quantitative checks, problem framing, and the Resolution Ladder have been attempted. Group related Proposal/Blocked items into one understandable decision package when possible. Zero questions is preferred when evidence is sufficient.

## Flow 2 completion gate

`ready_for_prd` requires:

- materially relevant source inspected to sufficient depth;
- material user instructions persisted;
- explicit rules/exclusions recovered;
- sufficient project topology for Flow 3;
- material terminology ambiguity resolved or surfaced;
- necessary cross-role implications recovered;
- applicable lifecycle and quantitative coherence checked;
- production coverage scan complete for applicable concerns;
- every material issue passed through the Resolution Ladder before escalation;
- every recovered/approved resolution propagated to affected meaning;
- every material requirement traceable to evidence/approved state;
- every Completion within the safe-completion boundary;
- no unresolved material Proposal/Blocked item affecting requested output.

Flow 3 may organize and polish approved meaning, but must not become the first place required product structure, lifecycle behavior, numeric consistency, implications, or decisions are invented.
