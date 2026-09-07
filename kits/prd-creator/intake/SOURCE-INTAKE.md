# Source Intake & Requirement Recovery

Flow 2 converts uneven project evidence into one approved requirement state before Flow 3 writes the canonical PRD. It owns source provenance, material requirement recovery, AI proposals, cross-role coherence, and the Simple Chat Preview approval boundary.

## Canonical state

Only these files are machine-owned Flow 2 truth:

```text
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
```

`work/review.md` is optional human-readable support. The Simple Chat Preview stays in chat and is never another canonical artifact.

The machine contract is implemented by `shared/intake.py`. Do not create alternate state fields or compatibility aliases in documentation or generated projects.

## 1. Source inventory

Every material source/instruction receives one stable `SRC-###` identity.

```yaml
sources:
  - id: SRC-001
    type: file
    role: authoritative
    status: current
    origin: client brief
    summary: Current gameplay design authority.
    inspection: full
    retention: repository
    path: source/originals/design.pdf
    sha256: <exact current file sha256>
```

Supported roles:

```text
authoritative | supporting | reference | generated
```

Supported source status:

```text
current | superseded
```

Supported inspection:

```text
full | targeted | blocked
```

`targeted` requires `inspection_scope`. A current `blocked` source prevents readiness.

Retention is either:

```text
repository | external
```

When `retention: repository`, `path` is project-relative, the retained file must exist, and its current SHA-256 must match the recorded digest. External retention is valid only after the relevant authority has been inspected sufficiently and its production meaning is persisted.

Do not ask the user for SRC IDs, file paths, YAML, or workspace mechanics.

## 2. Requirement register

Create one `REQ-###` for each material production rule, constraint, exclusion, topology rule, conflict resolution, completion, or proposal that must survive into PRD/acceptance.

Source-backed requirement:

```yaml
requirements:
  - id: REQ-001
    area: gameplay
    statement: Player must cross the bridge before collapse.
    provenance: [SRC-001]
    impact: high
```

Material AI proposal:

```yaml
  - id: REQ-014
    area: gameplay
    statement: The first target appears after 90 seconds of free experimentation.
    provenance: [SRC-001]
    impact: high
    recovery_class: proposal
    approval_status: pending
    resolution: Recommended preview default that preserves experiment-before-explanation.
```

Every requirement must have at least one valid `SRC-###` provenance reference. Dangling provenance is invalid. A requirement must retain at least one `current` provenance source at readiness.

Use `recovery_class: proposal` when the AI chooses among materially different project answers. Proposal requirements require an explicit `approval_status` and remain non-authoritative until preview approval. Use `recovery_class: blocked` only when no responsible answer can be formed; blocked requirements prevent readiness.

Optional fields such as `affects` and `evidence_locator` are allowed only when they materially improve propagation or later source verification. Do not create a separate dependency graph.

## 3. Recover meaning before filling gaps

Recover explicit facts, removals, exclusions, topology, terminology, quantitative rules, lifecycle behavior, and necessary Production Asset implications first.

Negative statements are first-class requirements:

```text
remove | no longer use | do not use | only | must not | replaced by
```

Distinguish product meaning from incidental implementation evidence:

```text
required gameplay/build/runtime behavior
→ canonical requirement

explicit approved technical constraint
→ canonical requirement at PRD abstraction level

incidental coordinate/tag/UUID/function path/debug setup
→ evidence only unless explicitly promoted by authority
```

Preserve approved spatial intent such as dimensions, relationships, route constraints, readability, and functional placement; do not promote final map-instance coordinates into PRD meaning.

## 4. Integrated completeness pass

Before preview, reason once across the complete model:

```text
player journey
→ Gameplay
→ Level Design
→ Developer lifecycle/state/data
→ Production Asset implications
→ success/fail/interruption/retry/reset/result/handoff
```

Check only applicable concerns, especially package/topology order, objective lifecycle, build relationships, runtime state/data/reset, required resources, quantitative consistency, terminology, and role ownership.

Routine grouping, wording, ordering, and decomposition are downstream craft. Escalate only materially different product/design/runtime/scope choices as Proposals.

## 5. Resolution ladder

For a material gap or conflict:

```text
existing authority settles it
→ recover

one necessary evidence-backed result exists
→ Completion

multiple plausible material answers exist
→ choose one concrete Proposal for preview

no responsible proposal is possible
→ Blocked / direct user decision
```

Do not minimize AI decisions artificially, but never present a Proposal as source truth.

## 6. Propagation rule

Every recovered Completion or Proposal must be coherent across every affected owner:

```text
requirement
→ topology
→ Gameplay
→ Level Design
→ Developer
→ Production Assets
→ timing/quantity/result
→ transition/retry/reset
```

Do not compensate for an upstream inconsistency with downstream prose.

## 7. Simple Chat Preview

Use one compact objective-based preview:

```text
Project Overview

Objective N — <Name>
Tujuan
Apa yang Player Lakukan
Hasil
Level Design
Developer
Saran AI        # only when material Proposals exist
```

Show each material AI Proposal once in `Saran AI`. Do not expose SRC/REQ IDs, YAML, Golden internals, or a duplicate full PRD by default.

Natural-language user approval is sufficient. After approval, promote the represented pending Proposals to approved requirement state unless the user corrected/rejected them.

## 8. Revision-bound approval

`intake-state.yaml` has exactly one readiness truth: `status`.

Before approval:

```yaml
status: audit_in_progress
preview_approved: false
```

After the requirement register has been updated to the exact approved model:

```yaml
status: ready_for_prd
preview_approved: true
approved_requirement_sha256: <sha256 of exact current state/requirement-register.yaml bytes>
```

Do **not** add redundant fields such as:

```text
ready_for_prd
next_step
flow
```

The approval hash is mandatory. If `requirement-register.yaml` changes after approval:

```text
requirement bytes change
→ SHA changes
→ prior preview approval is stale
→ Flow 3 must not start until affected meaning is reviewed/approved again
```

This prevents blanket approval from surviving a later hidden requirement edit.

## 9. Readiness

`ready_for_prd` requires:

- current material sources are sufficiently inspected;
- repository-retained source bytes still match recorded hashes;
- every requirement ID and provenance link is valid;
- no current blocked source/requirement remains;
- no Proposal remains pending or rejected-active;
- topology, lifecycle, quantities, terminology, and role ownership are coherent;
- the Simple Chat Preview represents every material Proposal;
- the user approved the represented model;
- `approved_requirement_sha256` matches the exact current requirement-register bytes.

Flow 3 consumes this approved requirement revision. It must not create new project meaning to repair an incomplete Flow 2 state.
