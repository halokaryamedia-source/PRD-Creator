---
name: prd-creator
description: End-to-end Production Execution router for PRD-Creator Flow 2–7: recover project requirements, resolve only material uncertainty, produce canonical PRD meaning and deterministic projection, materialize 04 Production Assets, validate handoff, then produce Voice when required without inventing upstream facts.
version: 3.0.0
---

# PRD Creator

Use for normal project Production Execution and bounded production revisions. Changes to PRD-Creator itself route to repository Development.

## Route first

```text
new / materially uncertain project meaning
→ Flow 2

approved bounded change
→ first changed canonical owner
→ only actually invalidated downstream owners

meaning complete but presentation grammar wrong
→ document/DESIGN-CONTRACT.md

contracts correct but implementation wrong
→ package AGENTS.md → technical owner
```

Start with the smallest owner that can settle the issue. Expand context only for a real dependency or contradiction.

## Canonical sequence

```text
source / instruction
→ Flow 2 source + material requirement recovery
→ integrated cross-role synthesis
→ material Proposal/conflict?
   yes → compact preview → approval/correction
   no  → continue automatically
→ exact requirement-revision binding
→ Flow 3 canonical content.md
→ strict render-data projection + content freshness binding
→ deterministic 01–03 render
→ required non-Voice 04 source when justified
→ Flow 4 semantic/mechanical acceptance
→ minimal handoff revision state
→ handoff_ready
→ Flow 5 Voice requirements when justified
→ Flow 6 canonical Voice Production
→ Flow 7 Voice acceptance/delivery
```

04 is a bounded capability, not another numbered Flow. Voice is optional and starts only from `handoff_ready`.

## Canonical owners

| Boundary | Owner |
|---|---|
| Flow 2 procedure/state | `intake/SOURCE-INTAKE.md` + `shared/intake.py` |
| PRD semantic meaning | `document/CONTENT-CONTRACT.md` |
| Golden page/component grammar | `document/DESIGN-CONTRACT.md` |
| strict render-data schema | `shared/render_schema.py` |
| Flow 4 validation/handoff | `document/VALIDATION.md` |
| non-Voice 04 | `production-assets/CONTRACT.md` + `shared/assets.py` |
| rendering/composition/delivery | `renderer/CONTRACT.md` |
| Voice lifecycle/state | `voice/EXTRACTION.md` + `shared/lifecycle.py` |
| Flow 6 performance craft | `voice/PERFORMANCE-WRITING.md` |
| Flow 7 validation | `voice/VALIDATION.md` |
| technical/file routing | `AGENTS.md` |

Do not redefine machine schemas elsewhere.

## Cross-flow invariants

### Authority decreases downstream

```text
current user instruction
→ approved decisions
→ current authoritative evidence
→ current Flow 2 requirement revision
→ canonical content / asset / Voice sources
→ derived render/context/index/HTML/evidence
```

Derived output never repairs or outranks its canonical owner.

### Approval is exception-driven

Flow 2 always binds the exact requirement revision consumed by Flow 3:

```text
requirement-register bytes
→ intake-state.approved_requirement_sha256
```

A Simple Chat Preview and `preview_approved: true` are required only when a **material AI Proposal** needs user approval. When current authority already settles the model, Flow 2 may become `ready_for_prd` directly without a preview round-trip.

Any later requirement edit invalidates the revision binding. If the changed scope contains a material Proposal, only that affected decision must be reviewed again.

### Projection is strict

```text
content.md bytes
→ render-data.canonical_content_sha256
→ one supported field vocabulary
→ deterministic renderer
```

No historical aliases, unknown keys, or renderer-side semantic recovery. Gameplay result meaning is explicit through `gameplay.result_model.mode = scored | completion_only` and must agree with Developer scoring/completion data.

### Stable Production Assets identity

```text
Owner ID
→ Moment ID: MOM-...
→ Asset ID: AST-... | Voice ID: VO-...
```

Display titles never perform machine joins.

### Freshness bindings stay machine-owned

Flow 4 acceptance binds the exact current render-data and optional non-Voice asset source. Final Voice acceptance binds the exact Voice Production source. These hashes are implementation metadata, not project versions or operator bookkeeping.

### Handoff state stays minimal

```yaml
status: handoff_ready
accepted_prd_version: X.Y.Z
```

Do not persist deterministic artifact paths in `state/handoff-state.yaml`. Flow 4 derives canonical work/output locations from the accepted revision and verifies those artifacts directly.

### Persisted paths are project-relative

Where machine state does contain path references, they use normalized POSIX project-relative refs only. Absolute paths, backslashes, `..`, and path escapes are invalid.

### Proof stays truthful

Mechanical checks prove mechanical contracts. Semantic review proves reviewed meaning. Visual PASS requires rendered/browser evidence. Audio quality requires actual audio evidence.

## Flow 2 → Flow 3

Flow 2 owns source/provenance, material Completion/Proposal/Blocked judgment, cross-role coherence, Production Asset implications, and conditional review.

`ready_for_prd` requires:

- current authority sufficiently inspected;
- retained source hashes/provenance valid;
- no current blocker/pending/rejected-active Proposal;
- every material Proposal approved/corrected when one exists;
- `approved_requirement_sha256` equals exact current requirement-register bytes.

Do not create a review stop merely because Flow 2 exists. If authoritative evidence already settles the project model, continue directly to Flow 3.

Flow 3 must return upstream rather than silently invent missing meaning.

## Flow 3 → Flow 4

```text
current Flow 2 requirement revision
→ work/content.md
→ strict work/render-data.json + content freshness binding
→ DESIGN-CONTRACT grammar
→ deterministic PRD-core render
```

Preserve semantic cardinality. Do not fill or compress content to sample counts.

Materialize `work/asset-requirements.md` before Flow 4 when approved meaning requires non-Voice resources.

## Flow 4 handoff

Use one canonical mechanical validator, one integrated semantic readiness/reconciliation review, Material Conservation, and visual evidence only when claimed.

When `Visual sanity: PASS` is claimed, run:

```bash
python tools/prd.py browser workspace/active/<project>/
```

After acceptance, `state/handoff-state.yaml` stores only `status` and `accepted_prd_version`. The validator derives and checks canonical `work/` + `output/v<version>/` paths, delivery revision metadata, and exact acceptance bindings.

Only `handoff_ready` crosses into Flow 5. Browser evidence is downstream proof and must never authorize stale or mechanically invalid PRD state.

## Flow 5–7

Flow 5 owns Voice scope, Owner ID, Moment ID, Speaker/Channel/Trigger/Purpose, communication payload/exclusions, and authoritative timing truth.

Flow 6 preserves that identity and owns wording, performance, Estimated Duration, and voice/profile selection.

Flow 7 validates revision/identity/source/HTML parity. Voice-only changes do not reopen PRD acceptance when upstream PRD/04 meaning is unchanged.

## First wrong owner

```text
project fact / gameplay / story / project-level production choice
→ Flow 2 / PRD authority

canonical PRD meaning wrong
→ CONTENT-CONTRACT / content.md

meaning correct; page grammar wrong
→ DESIGN-CONTRACT

non-Voice resource meaning / Owner-Moment-Asset identity
→ production-assets / asset-requirements.md

Voice scope / communication intent
→ Flow 5 / voice-requirements.md

Voice wording / performance / duration / cast selection
→ Flow 6 / voice-production.md

canonical sources correct; generated presentation wrong
→ renderer/compositor

mechanical parity defect
→ matching validator/shared schema owner
```

## Mechanical operator shortcut

Prefer the repository facade for routine mechanical work:

```bash
python tools/prd.py status workspace/active/<project>/
python tools/prd.py build workspace/active/<project>/
python tools/prd.py validate workspace/active/<project>/
python tools/prd.py browser workspace/active/<project>/
python tools/prd.py handoff workspace/active/<project>/
python tools/prd.py voice workspace/active/<project>/
```

Use `status --json` when an agent needs compact machine-readable routing. It reports mechanical state and the first structured wrong owner; it does not prove semantic, visual, audio, or approval quality.

Use `browser` only after current canonical PRD validation passes and only when browser/visual evidence is required.

## Artifact lifecycle

```text
Flow 2
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
work/review.md                    # optional

Flow 3
work/content.md
work/render-data.json

04 when required
work/asset-requirements.md

Flow 4
work/acceptance.md
state/handoff-state.yaml          # status + accepted_prd_version only

Voice when used
work/voice-requirements.md
work/voice-production.md
work/voice-acceptance.md
state/voice-state.yaml

Derived
output/README.md
output/v<version>/prd.html
output/v<version>/context.md
output/v<version>/index.json
```

Do not create parallel schemas, registries, dashboards, extra approval layers, alternate default HTML, or speculative frameworks.

## Context and proof economy

- Start narrow and expand progressively.
- Use `tools/prd.py status` first for mechanical status/debug routing.
- Do not load the large Golden HTML unless template/DOM/runtime/visual evidence requires it.
- Batch canonical edits before regeneration.
- Use exact owner/state/schema errors instead of rereading unrelated context.
- Do not turn semantic review into word-count, similarity, scorecard, or checksum ceremony.
- Do not ask the user to repeat recoverable state or reapprove already-authoritative facts.

## Stop condition

Stop when requested scope is complete and evidence supports the claim. Do not continue into unrelated cleanup or speculative abstraction merely because more work is possible.
