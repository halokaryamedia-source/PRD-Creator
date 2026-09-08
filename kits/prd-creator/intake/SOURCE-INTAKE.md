# Source Intake & Requirement Recovery

Flow 2 converts project evidence into one production-ready requirement state before Flow 3 writes the canonical PRD. It owns source authority, material requirement recovery, unresolved material choices, cross-role coherence, and the approval boundary only when a real Proposal requires it.

## Canonical state

Machine-owned Flow 2 truth is limited to:

```text
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
```

`work/review.md` is optional human-readable support. A Simple Chat Preview is conditional review material, not another canonical artifact.

The machine contract is implemented by `shared/intake.py`. Do not add compatibility aliases, duplicate readiness fields, or a second approval registry.

## 1. Source inventory

Give every material source/instruction one stable `SRC-###` identity.

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

Repository-retained sources must use project-relative paths and matching SHA-256 bytes. External retention is valid after the relevant authority has been inspected sufficiently and its production meaning is preserved upstream.

Do not ask the user for SRC IDs, YAML, hashes, or workspace mechanics.

## 2. Requirement register

Create `REQ-###` entries only for **material rules that benefit from explicit traceability**. Typical examples:

- high-impact gameplay or production constraints;
- exclusions / negative requirements;
- quantitative invariants;
- topology/lifecycle rules that must survive handoff;
- conflict resolutions;
- AI Completion or Proposal decisions.

Do **not** turn ordinary descriptive detail, wording, grouping, or every sentence from the source into separate requirement records. Those details can live in the canonical project model/content once their authority is clear.

Source-backed requirement:

```yaml
requirements:
  - id: REQ-001
    area: gameplay
    statement: Player must cross the bridge before collapse.
    provenance: [SRC-001]
    impact: high
```

Material AI Proposal:

```yaml
  - id: REQ-014
    area: gameplay
    statement: The first target appears after 90 seconds of free experimentation.
    provenance: [SRC-001]
    impact: high
    recovery_class: proposal
    approval_status: pending
    resolution: Recommended default preserving experiment-before-explanation.
```

Every requirement needs valid source provenance. A normal source-backed/Completion requirement must retain current authoritative grounding. An explicitly approved Proposal may cross that authority boundary through user approval.

Use `recovery_class: proposal` only when the AI chooses among materially different project answers. Use `recovery_class: blocked` only when no responsible answer can be formed.

Optional fields such as `affects` and `evidence_locator` are allowed only when they materially improve propagation or source verification. Do not build a dependency graph merely for symmetry.

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

Preserve approved spatial intent such as dimensions, relationships, route constraints, readability, and functional placement; do not promote final map-instance coordinates into general PRD meaning.

## 4. Integrated completeness pass

Before Flow 3, reason once across the complete applicable model:

```text
player journey
→ Gameplay
→ Level Design
→ Developer lifecycle/state/data
→ Production Asset implications
→ success/fail/interruption/retry/reset/result/handoff
```

Check only concerns that can materially affect implementation. Routine wording, grouping, ordering, and decomposition remain downstream craft.

## 5. Resolution ladder

For a material gap or conflict:

```text
existing authority settles it
→ recover

one necessary evidence-backed result exists
→ Completion

multiple plausible material answers exist
→ choose one concrete Proposal

no responsible proposal is possible
→ Blocked / direct user decision
```

Do not present a Proposal as source truth.

## 6. Propagation rule

Every recovered Completion or approved Proposal must remain coherent across affected owners:

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

## 7. Conditional Simple Chat Preview

A preview is required **only when material user review is actually needed**.

### No material Proposal or unresolved conflict

If current authority already settles the project model and no material AI Proposal remains:

```text
recover requirements
→ bind the current requirement revision
→ status: ready_for_prd
→ continue directly to Flow 3
```

Do not stop merely to ask the user to approve information they already supplied or previously approved.

Minimal ready state:

```yaml
status: ready_for_prd
approved_requirement_sha256: <sha256 of exact current state/requirement-register.yaml bytes>
```

`preview_approved` may be omitted (or remain `false`) in this authoritative-only path.

### Material Proposal exists

When the AI has selected among materially different answers, show one compact objective-based preview containing the decision under `Saran AI` and request approval/correction once.

```text
Project Overview

Objective N — <Name>
Tujuan
Apa yang Player Lakukan
Hasil
Level Design
Developer
Saran AI        # only for material Proposals
```

After the represented Proposal is approved/corrected, update the requirement register to the exact accepted state and record:

```yaml
status: ready_for_prd
preview_approved: true
approved_requirement_sha256: <sha256 of exact current state/requirement-register.yaml bytes>
```

Do not expose SRC/REQ IDs, YAML, hashes, or Golden internals to the user during normal production.

## 8. Revision binding

`approved_requirement_sha256` is a machine-owned freshness binding for the exact Flow 2 requirement revision consumed by Flow 3. It is not a second project version and operators should not maintain it manually.

If `requirement-register.yaml` changes after readiness:

```text
requirement bytes change
→ SHA changes
→ prior Flow 2 revision binding is stale
→ affected meaning must be reconciled before Flow 3 continues
```

If the changed requirement includes a material Proposal, the affected Proposal must also cross the review/approval boundary again.

## 9. Readiness

`ready_for_prd` requires:

- current material sources are sufficiently inspected;
- repository-retained source bytes still match recorded hashes;
- requirement IDs/provenance are valid;
- normal requirements have current authoritative grounding;
- material Proposals are explicitly approved;
- no current blocked source/requirement remains;
- no Proposal remains pending or rejected-active;
- topology, lifecycle, quantities, terminology, and role ownership are coherent;
- `approved_requirement_sha256` matches the exact current requirement-register bytes;
- `preview_approved: true` only when approval evidence is required for an accepted material Proposal.

Flow 3 consumes this exact ready requirement revision. It must not invent new project meaning to repair incomplete Flow 2 state.