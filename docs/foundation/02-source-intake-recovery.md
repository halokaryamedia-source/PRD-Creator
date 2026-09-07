# Source Intake & Requirement Recovery

Status: active Flow 2 policy

## Purpose

Turn uneven project evidence into one coherent, reviewable, revision-bound requirement model before PRD authoring.

The exact machine schema and operational procedure live in `kits/prd-creator/intake/SOURCE-INTAKE.md` and `shared/intake.py`. This foundation file does not maintain another YAML contract.

## Authority and provenance

Every material requirement must remain traceable to current project authority or an explicitly approved AI Proposal.

Authority remains:

```text
current explicit user instruction
→ approved decisions
→ current authoritative source
→ supporting evidence
→ generated/reference material only as bounded evidence
```

Reference or generated material never silently becomes project truth.

## Source retention

Retain source bytes in the project only when later direct inspection/reproduction materially benefits from them. Repository-retained sources are freshness-bound by SHA-256. External retention is valid only after relevant authority has been sufficiently inspected and recovered meaning is persisted.

A current source whose necessary inspection is blocked prevents readiness.

## Requirement recovery

Recover material facts, constraints, exclusions, topology, terminology, quantitative rules, lifecycle behavior, build/spatial intent, approved technical constraints, and required production-resource implications.

Treat negative statements as first-class requirements.

Do not promote incidental as-built identifiers such as final coordinates, UUIDs, scoreboard names, function paths, or debug/setup residue unless current authority explicitly makes them production constraints.

## Completion vs Proposal

```text
existing authority settles the answer
→ recover it

one necessary evidence-backed implication exists
→ Completion

multiple plausible material answers exist
→ one concrete Proposal

no responsible answer can be formed
→ Blocked / direct decision
```

Proposal means an AI-chosen material project default, not ordinary wording/grouping/order craft.

## Integrated completeness

Before preview, reason across the same model through:

```text
player journey
→ Gameplay
→ Level Design
→ Developer state/lifecycle/data
→ Production Asset implications
→ result/transition/retry/reset
```

Resolve cross-role contradictions before approval. Do not use downstream writing to hide upstream uncertainty.

## Simple Chat Preview

The preview is the single user checkpoint inside Flow 2 and is not another artifact. Show a compact project/objective view and disclose each material AI Proposal once.

Natural-language approval is sufficient only for the exact requirement revision represented by that preview.

## Revision-bound approval

Flow 2 readiness is not a loose boolean. `status: ready_for_prd` is valid only when:

```text
current requirement-register bytes
→ shown coherent model
→ user approval
→ approved_requirement_sha256
```

Any later requirement-register edit changes the digest and makes the old approval stale.

Do not maintain duplicate state such as `ready_for_prd: true`, `next_step`, or another approval flag beyond the canonical state contract.

## Readiness boundary

Flow 3 may start only when:

- current material authority is sufficiently inspected;
- retained source bytes/provenance are current;
- no material requirement is blocked/pending/rejected-active;
- topology/lifecycle/quantities/terminology/role ownership are coherent;
- all material Proposals were represented and approved;
- the approval digest matches exact current requirement-register bytes.

If any of these become stale, reopen only the affected Flow 2 slice and approve the updated requirement revision before downstream authoring continues.
