# Source Intake & Requirement Recovery

Status: active Flow 2 policy

## Purpose

Turn uneven project material into a trustworthy, **complete reviewable project model** before PRD drafting. Flow 2 recovers explicit authority, project structure, exclusions, terminology, necessary production implications, material gaps/conflicts, and practical resolutions; it then presents the complete model through the Simple Chat Preview for user approval.

Detailed procedure lives in `kits/project-document-generator/SOURCE-INTAKE.md`. This foundation page owns only durable policy.

## Canonical sequence

```text
inventory source/instruction evidence
→ authority/relevance triage + sufficient inspection
→ recover facts/rules/exclusions/topology/terminology
→ one integrated production-completeness pass
→ authority / Completion / concrete Proposal / Blocked
→ propagate affected production meaning
→ complete Simple Chat Preview
→ user correction / approval
→ promote represented pending proposals
→ ready_for_prd
```

Flow 2 should **solve before asking**. It does not stop at listing gaps when a responsible coherent proposal can be formed.

## Authority

Precedence:

1. current explicit user/creative-owner instruction;
2. approved project decisions;
3. current authoritative project source;
4. normalized current requirement state;
5. supporting/generated evidence for context only;
6. Golden/reference material for demonstrated document structure/quality only.

A polished filename such as `FINAL` does not override higher authority by itself. Same-authority material conflicts remain explicit until resolved; do not silently select the more convenient sentence.

Material user instructions must be persisted even when no file exists.

## Source retention

Source identity/provenance is mandatory; **duplicating every source file into Git is not**.

Keep a supplied original under `source/originals/` when later direct inspection/reproduction materially benefits from in-repo bytes. A large/static source may remain externally retained when:

- relevant authority has already been inspected to sufficient depth;
- source inventory records its exact identity/provenance and retention boundary;
- filename and SHA-256 are recorded for file sources when available/useful for exact continuity;
- recovered/approved production meaning is persisted in requirement/canonical state.

External retention cannot be used to avoid reading material authority or to replace source with generated output.

## Completion / Proposal / Blocked

Use the smallest truthful recovery class:

```text
Existing authority resolves it
→ recover.

One necessary evidence-backed answer exists
→ Completion.

AI must choose among plausible product/design/development answers
→ one concrete Proposal.

No responsible answer can be formed from authority + known constraints
→ Blocked/direct decision.
```

A Proposal may choose material gameplay, quantities, timing, scoring/recovery behavior, naming, build expectations, runtime behavior, or implementation rules at PRD abstraction level. It is **not project truth until the user approves/corrects the relevant preview**.

The objective is not to avoid AI decisions. It is to give the user one coherent model to approve without misrepresenting unsupported choices as source facts.

## Production completeness

Before preview, inspect only applicable material concerns:

- topology: ordered packages/stages, global/local ownership, transitions, final result/handoff;
- Gameplay: objective, start, player actions/feedback, completion, fail/retry/recovery, result;
- Level Design: areas/objects/routes, relationships, spatial constraints, gameplay function;
- Developer: activation, state/progression, timing/quantities, completion/result, data, interruption/reset, handoff;
- Production Assets: concrete MODEL / ITEM / UI / TEXT / standalone AUDIO / standalone PARTICLE resources that are explicit, necessarily implied, or materially approved; shared vs local ownership; exact player-facing copy when known;
- lifecycle: precondition → trigger → active → success/fail/interruption → result → retry/reset;
- quantitative coherence: related timings/counts/capacities/scoring values can coexist;
- global/local coherence: shared defaults and legitimate exceptions agree;
- authoritative known constraints: no silent conflict with required behavior;
- operational clarity: competent production roles should not reasonably build materially different behavior from the approved model.

Optional/decorative detail is not a gap merely because it could be specified. Do not invent asset style, lore, dimensions, animations, VFX, or sound to make the project model look complete.

Production Asset coverage is a meaning check, not another Flow or preview artifact. The Simple Chat Preview does not need to list every resource. It only needs to expose material AI-chosen decisions that require approval.

## Golden-guided completeness

The Reverse-derived Golden fill map in `CONTENT-CONTRACT.md` is the finite guide for what the PRD core must eventually be able to answer.

Golden supplies **questions, placement, page family, labels, and presentation behavior**. It never supplies another project's mechanics, counts, timings, lore, scoring values, implementation facts, or asset style.

When a material Golden-required answer is absent, resolve it through current authority, Completion, Proposal, Explicit No / Not Applicable where truthful, or Blocked as last resort. Do not leave a material future slot empty merely because source is incomplete.

## Propagation

Every recovered Completion or proposed/approved decision must reconcile all actually affected meaning:

```text
requirement
→ topology/global ownership
→ Gameplay
→ Level Design
→ Developer
→ Production Asset implications
→ timing/quantities/scoring
→ transition/handoff
→ retry/interruption/reset
```

Production Asset implications remain separate from Developer behavior: concrete resources go to the 04 model; runtime logic stays in Developer meaning.

Do not create a dependency graph merely to record this propagation.

## Simple Chat Preview

The initial Flow 2 user checkpoint is one complete, objective-based **Simple Chat Preview**. It is chat output, not another file/Flow.

Default information:

```text
Project Overview
Objective N
  Tujuan
  Apa yang Player Lakukan
  Hasil
  Level Design
  Developer
  Saran AI       # required when material AI-chosen Proposals exist
```

Keep internal SRC/REQ/YAML/provenance/Golden DOM jargon out of the user's way. Do not dump a production-asset inventory into the preview by default. `Perlu Konfirmasi` is reserved for the rare genuinely user/external-only blocker.

Every **material AI-chosen Proposal** must appear once in the preview's `Saran AI` block before approval. Material means a chosen default that changes gameplay behavior or scope, including timing, quantity, progression, scoring, fail/recovery, reward, build scope, runtime behavior, or a Production Asset choice that changes project meaning. State the chosen default concisely; do not turn this into a question-by-question approval flow. Omit `Saran AI` only when the reviewed slice contains no material AI-chosen Proposal.

Approval of the complete preview promotes the represented pending Proposals unless the user corrects/rejects them. A bounded revision previews only the affected slice when interpretation changed; an unambiguous current user instruction may itself approve that slice.

## Persistent readiness

Repository-backed Flow 2 keeps:

- `state/source-inventory.yaml`;
- `state/requirement-register.yaml`;
- `state/intake-state.yaml`;
- `work/review.md` only when useful.

`ready_for_prd` requires real stable source/requirement evidence, sufficient inspection, approved preview meaning, production-complete implications including justified 04 resource needs, and no current unambiguous blocker such as `approval_status: pending`, `recovery_class: blocked`, or current authoritative source `inspection: blocked` affecting scope.

After Flow 2 completes, do not preserve a stale Flow-2 `next_step` merely because the schema once allowed it; later continuation belongs to current canonical/handoff state and repository `next-action.md`.

## Stop rule

Once current scope is complete, approved, and truthfully `ready_for_prd`, stop. Flow 2 is not an endless redesign workshop and must not generate optional hardening, extra artifacts, or additional approval layers for ceremony.
