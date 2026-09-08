---
name: prd-creator
description: End-to-end Production Execution router for PRD-Creator Flow 2–7: recover and approve project requirements, produce canonical PRD meaning and strict deterministic projection, materialize 04 Production Assets, validate exact-byte handoff, then produce and validate Voice when required without inventing upstream facts.
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

Start with the smallest owner that can settle the issue. Expand context only for a real dependency/contradiction.

## Canonical sequence

```text
source / instruction
→ Flow 2 source + requirement recovery
→ integrated cross-role synthesis
→ Simple Chat Preview
→ exact requirement-revision approval
→ Flow 3 canonical content.md
→ strict render-data projection + content SHA
→ deterministic 01–03 render
→ required non-Voice 04 source
→ Flow 4 semantic/mechanical acceptance + exact byte bindings
→ handoff_ready
→ Flow 5 Voice requirements when justified
→ Flow 6 canonical Voice Production
→ Flow 7 exact Voice acceptance/delivery
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

### 1. Authority decreases downstream

```text
current user instruction
→ approved decisions
→ current authoritative evidence
→ exact approved requirement revision
→ canonical content / asset / Voice sources
→ derived render/context/index/HTML/evidence
```

Derived output never repairs or outranks its canonical owner.

### 2. Approval is revision-bound

Flow 2 readiness is:

```text
requirement-register bytes
→ Simple Chat Preview
→ user approval
→ intake-state.approved_requirement_sha256
```

Any later requirement edit invalidates approval. Do not use redundant `ready_for_prd: true` or `next_step` state.

### 3. Projection is strict

```text
content.md bytes
→ render-data.canonical_content_sha256
→ one supported field vocabulary
→ deterministic renderer
```

No historical field aliases, unknown keys, or renderer-side semantic recovery. Gameplay result meaning is explicit through `gameplay.result_model.mode = scored | completion_only` and must agree with Developer scoring/completion data.

### 4. Stable Production Assets identity

```text
Owner ID
→ Moment ID: MOM-...
→ Asset ID: AST-... | Voice ID: VO-...
```

`package:<id>` owns a package and matching gameplay-flow meaning. `journey:<id>` is for non-package journey nodes only. Display titles never perform machine joins.

### 5. Exact acceptance bytes

Flow 4 acceptance binds:

```text
Accepted Render Data SHA256
Accepted Asset Requirements SHA256   # sha or none
```

Final Voice acceptance binds:

```text
Accepted Voice Production SHA256
```

Semantic version is not an edit counter.

### 6. Persisted paths are project-relative

Machine state accepts normalized POSIX project-relative refs only. Absolute paths, backslashes, `..`, and path escapes are invalid.

### 7. Proof stays truthful

Mechanical checks prove mechanical contracts. Semantic review proves reviewed meaning. Visual PASS requires rendered/browser evidence. `tools/prd.py browser` proves real-Chrome structural, layout, navigation, language-control, and console sanity at the supported desktop viewports; it does not prove subjective aesthetics or semantic correctness. Audio quality requires actual audio evidence.

## Flow 2 → Flow 3

Flow 2 owns source/provenance, material Completion/Proposal/Blocked judgment, cross-role coherence, Production Asset implications, and preview approval.

`ready_for_prd` requires:

- current authority sufficiently inspected;
- retained source hashes and provenance valid;
- no current blocker/pending/rejected-active Proposal;
- every material AI Proposal represented in preview and approved/corrected;
- `approved_requirement_sha256` equals exact current requirement-register bytes.

Flow 3 must return upstream rather than silently invent missing meaning.

## Flow 3 → Flow 4

```text
approved requirement revision
→ work/content.md
→ strict work/render-data.json + content SHA
→ DESIGN-CONTRACT grammar
→ deterministic PRD-core render
```

Preserve semantic cardinality. Do not fill or compress content to sample counts.

Materialize `work/asset-requirements.md` before Flow 4 when approved meaning requires non-Voice resources.

## Flow 4 handoff

Use one canonical mechanical validator, one integrated semantic readiness/reconciliation review, Material Conservation, and visual evidence only when claimed.

When `Visual sanity: PASS` is claimed, run `python tools/prd.py browser workspace/active/<project>/` against the current validated delivery. Browser evidence is downstream proof and must never authorize a stale or mechanically invalid PRD.

Only `handoff_ready` crosses into Flow 5. `state/handoff-state.yaml` uses its strict canonical paths and acceptance must bind exact current render-data + asset-requirements bytes.

## Flow 5–7

Flow 5 owns Voice scope, Owner ID, Moment ID, Speaker/Channel/Trigger/Purpose, communication payload/exclusions, and authoritative timing truth.

Flow 6 preserves that identity and owns exact wording, performance, Estimated Duration, and voice/profile selection.

Flow 7 validates revision/identity/source/HTML parity. `voice_delivery_ready` additionally requires current Voice Acceptance bound to exact `voice-production.md` bytes.

Voice-only production changes do not reopen PRD acceptance when upstream PRD/04 meaning is unchanged.

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

Voice scope / Owner-Moment identity / communication intent
→ Flow 5 / voice-requirements.md

Voice wording / performance / duration / cast selection
→ Flow 6 / voice-production.md

canonical sources correct; generated presentation wrong
→ renderer/compositor

mechanical parity defect
→ matching validator/shared schema owner
```

## Mechanical operator shortcut

For routine build/status/validation work, prefer the thin repository facade instead of memorizing individual renderer/validator script paths:

```bash
python tools/prd.py status workspace/active/<project>/
python tools/prd.py build workspace/active/<project>/
python tools/prd.py validate workspace/active/<project>/
python tools/prd.py browser workspace/active/<project>/
python tools/prd.py handoff workspace/active/<project>/
python tools/prd.py voice workspace/active/<project>/
```

Use `status --json` when an agent needs a compact machine-readable result. It reports only mechanical state and the first structured wrong owner; it does not create another authority or prove semantic, visual, audio, or approval readiness.

Use `browser` only after the current canonical PRD mechanically validates. It inspects the current versioned `prd.html` without rebuilding it, tests 1440×1200 and 1024×900 desktop layouts in real Chrome, exercises navigation/language controls, checks console errors and DOM/accessibility invariants, and returns screenshot SHA evidence. Optional `--screenshot <path>` persists the primary PNG evidence.

When `status` identifies a first issue, open that exact owner/path first. Do not broad-read the kit merely because a downstream stage is blocked.

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
state/handoff-state.yaml

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

## Context economy

- Start narrow and expand progressively.
- Use `tools/prd.py status` first when the task is mechanical status/debug routing.
- Use `tools/prd.py browser` only when browser/visual evidence is actually required; do not load or inspect the full rendered HTML manually first unless browser evidence reports a defect that needs owner diagnosis.
- Do not load the large Golden HTML unless template/DOM/runtime/visual evidence is required.
- Batch canonical edits before regeneration.
- Use exact owner/state/schema errors to avoid rereading unrelated context.
- Do not turn semantic review into word-count/similarity/scorecard machinery.
- Do not ask the user to repeat recoverable current state.

## Stop condition

Stop when requested scope is complete and evidence supports the claim. Do not continue into unrelated cleanup or speculative abstraction merely because more work is possible.
