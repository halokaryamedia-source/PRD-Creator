# Source Intake & Requirement Recovery

Status: active Flow 2 policy

## Purpose

Turn uneven project evidence into one coherent, revision-bound requirement model before PRD authoring, without inserting a user approval round-trip when current authority already settles the material decisions.

The exact machine schema and operational procedure live in `kits/prd-creator/intake/SOURCE-INTAKE.md` and `shared/intake.py`. This foundation file does not maintain another YAML contract.

## Authority and provenance

Every material traced requirement must remain grounded in current project authority or an explicitly approved AI Proposal.

Authority remains:

```text
current explicit user instruction
→ approved decisions
→ current authoritative source
→ supporting evidence
→ generated/reference material only as bounded evidence
```

`current` and `authoritative` are different properties. A current supporting/reference/generated source remains evidence only; it cannot independently ground a normal requirement. An explicit Proposal becomes authority only after the user approval boundary.

## Source retention

Retain source bytes in the project only when later direct inspection/reproduction materially benefits from them. Repository-retained sources are freshness-bound by SHA-256. External retention is valid only after relevant authority has been sufficiently inspected and recovered meaning is persisted.

A current source whose necessary inspection is blocked prevents readiness.

## Requirement recovery

Recover material facts, constraints, exclusions, topology, terminology, quantitative rules, lifecycle behavior, build/spatial intent, approved technical constraints, and required production-resource implications.

Use explicit `REQ-###` records for material rules that benefit from traceability. Do not turn every descriptive sentence, ordinary grouping choice, or explanatory detail into requirement-database administration.

Treat negative statements as first-class requirements.

Do not promote incidental as-built identifiers such as final coordinates, UUIDs, scoreboard names, function paths, or debug/setup residue unless current authority explicitly makes them production constraints.

## Completion vs Proposal

```text
existing authority settles the answer
→ recover it and continue

one necessary evidence-backed implication exists
→ Completion and continue

multiple plausible material answers exist
→ one concrete Proposal → user review

no responsible answer can be formed
→ Blocked / direct decision
```

Proposal means an AI-chosen material project default, not ordinary wording/grouping/order craft.

## Integrated completeness

Before Flow 3, reason across the same model through:

```text
player journey
→ Gameplay
→ Level Design
→ Developer state/lifecycle/data
→ Production Asset implications
→ result/transition/retry/reset
```

Resolve cross-role contradictions before downstream authoring. Do not use writing polish to hide upstream uncertainty.

## Conditional Simple Chat Preview

The preview is an **exception-driven user checkpoint**, not a mandatory Flow 2 phase.

When current authority already settles the project model and no material Proposal remains:

```text
recover model
→ bind exact requirement revision
→ ready_for_prd
→ continue directly to Flow 3
```

When a material AI Proposal exists:

```text
recover model + Proposal
→ compact preview showing that Proposal once
→ user approval/correction
→ update exact accepted requirement revision
→ ready_for_prd
```

Natural-language approval is sufficient for the represented material Proposal. Do not ask the user to approve facts they already supplied or previously approved.

## Revision binding

Flow 2 always binds the exact current requirement revision:

```text
current requirement-register bytes
→ approved_requirement_sha256
```

The field name is retained as the established machine contract, but the digest is a freshness binding—not proof that every authoritative-only project passed through a separate preview ceremony.

Any later requirement-register edit changes the digest and makes downstream use of the old revision stale. If the changed scope includes a material Proposal, only that affected Proposal must cross the user review boundary again.

Do not maintain duplicate state such as `ready_for_prd: true`, `next_step`, or a second revision/approval registry.

## Readiness boundary

Flow 3 may start only when:

- current material authority is sufficiently inspected;
- retained source bytes/provenance are current;
- each normal requirement has current authoritative grounding;
- each material AI Proposal is explicitly approved;
- no material requirement is blocked/pending/rejected-active;
- topology/lifecycle/quantities/terminology/role ownership are coherent;
- `preview_approved: true` exists when an accepted material Proposal required user review;
- the revision digest matches exact current requirement-register bytes.

If these become stale, reopen only the affected Flow 2 slice. Do not replay unrelated review for ceremony.
