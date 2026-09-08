---
name: prd-creator
description: End-to-end Production Execution router for PRD-Creator Flow 2–7: recover current project meaning, produce canonical PRD + justified Production Assets, validate handoff, then produce optional Voice without inventing upstream facts.
version: 3.0.0
---

# PRD Creator

Use for normal project Production Execution and bounded production revisions. Changes to PRD-Creator itself route to repository Development.

## Route first

```text
new / materially uncertain project meaning
→ Flow 2

bounded approved revision
→ first changed canonical owner
→ only invalidated downstream owners

meaning complete, presentation grammar wrong
→ document/DESIGN-CONTRACT.md

contracts correct, executable behavior wrong
→ package AGENTS.md → exact technical owner
```

This is one production system, not separate fast/full paths. The same authority, invariants, acceptance, and quality requirements apply at every task size; only relevant context, execution, and proof scale with the affected scope.

Start from the smallest owner that can settle the issue. Expand context only for a real dependency or contradiction.

## Proportional execution

For bounded current work, do not replay the end-to-end sequence unless the change actually invalidates it.

```text
explicit approved target or concrete failure
→ exact current owner
→ coherent canonical change
→ only invalidated downstream work
→ cheapest proof that can falsify the changed claim
→ STOP
```

- Use `status` when the current mechanical stage or first structured wrong owner is unclear; skip it when the authoritative target is already known.
- Use `impact` when changed paths span domains or the required proof set is unclear; skip it when one obvious targeted check already settles the change.
- Load a semantic specialist only when semantic judgment is actually required.
- Load adjacent owners only when an unresolved dependency can change the result.
- Batch related canonical edits before regenerating derived output once.
- Do not run unrelated cleanup, regeneration, approval, browser/audio proof, or full regression merely because those capabilities exist.
- Full integration/promotion gates remain unchanged and are never replaced by proportional iteration proof.

## Canonical sequence

Use the full sequence for new, materially uncertain, or genuinely end-to-end production work:

```text
source / instruction
→ Flow 2 recover material requirements
→ material Proposal/conflict?
   yes → compact review → approval/correction
   no  → continue
→ exact requirement-revision binding
→ Flow 3 work/content.md
→ strict render-data + content freshness binding
→ deterministic 01–03 render
→ justified non-Voice 04 source when required
→ Flow 4 acceptance + minimal handoff state
→ optional Flow 5 Voice requirements
→ Flow 6 canonical Voice Production
→ Flow 7 Voice acceptance/delivery
```

`04 Production Assets` is a bounded capability, not another numbered Flow. Voice begins only from `handoff_ready`.

## Owners

| Boundary | Owner |
|---|---|
| Flow 2 source/requirement state | `intake/SOURCE-INTAKE.md` + `shared/intake.py` |
| canonical PRD meaning | `document/CONTENT-CONTRACT.md` |
| Golden page/component grammar | `document/DESIGN-CONTRACT.md` |
| render-data schema | `shared/render_schema.py` |
| Flow 4 acceptance/handoff | `document/VALIDATION.md` |
| non-Voice 04 | `production-assets/CONTRACT.md` + `shared/assets.py` |
| rendering/delivery | `renderer/CONTRACT.md` |
| Voice Flow 5 | `voice/EXTRACTION.md` |
| Voice Flow 6 | `voice/PERFORMANCE-WRITING.md` |
| Voice Flow 7 | `voice/VALIDATION.md` |
| file/mechanical routing | `AGENTS.md` |

Do not redefine machine schemas elsewhere.

## Non-negotiable invariants

### Authority decreases downstream

```text
user instruction / approved decisions / authoritative source
→ current requirement state
→ canonical PRD / Asset / Voice sources
→ derived render/context/index/HTML/evidence
```

Derived output never repairs or outranks canonical meaning.

### Approval is exception-driven

Flow 2 always binds exact current requirement bytes to `approved_requirement_sha256`. User review is required only for a material AI Proposal/conflict; authoritative facts and evidence-backed Completions continue without redundant approval.

A later material requirement edit invalidates the revision binding. Reopen only affected scope.

### Projection is strict

```text
content.md bytes
→ canonical_content_sha256
→ one supported render-data vocabulary
→ deterministic renderer
```

No historical aliases or renderer-side semantic recovery. Gameplay result mode is explicit: `scored | completion_only`, and Developer data must agree.

### Stable 04 identity

```text
Owner ID → Moment ID → Asset ID | Voice ID
```

Display titles never perform machine joins.

### Acceptance stays exact

Flow 4 binds current Render Data and optional Asset Requirements. Final Voice acceptance binds current Voice Production. These hashes are freshness metadata, not user-managed project versions.

### Handoff stays minimal

```yaml
status: handoff_ready
accepted_prd_version: X.Y.Z
```

Canonical work/output paths are derived and verified, not persisted redundantly.

### Proof stays truthful

Mechanical checks prove mechanical contracts. Semantic review proves meaning. Visual PASS requires actual browser/render evidence. Audio quality requires actual audio evidence.

## Flow boundaries

Flow 2 owns source/provenance, material Completion/Proposal/Blocked judgment, cross-role coherence, and requirement revision binding. Flow 3 must not invent missing project meaning.

Flow 3 produces canonical `content.md` and strict `render-data.json`, preserving semantic cardinality instead of filling sample counts. Materialize `work/asset-requirements.md` only when approved meaning requires non-Voice resources.

Flow 4 validates current PRD state, semantic readiness, exact acceptance bindings, delivery parity, and browser evidence only when claimed/required. Only `handoff_ready` crosses to Voice.

Flow 5 owns Voice scope/context/communication intent. Flow 6 owns final wording/performance within that contract. Flow 7 proves revision/identity/source/HTML parity. Voice-only changes do not reopen accepted PRD meaning when upstream scope is unchanged.

## First wrong owner

```text
project fact/gameplay/story/production choice → Flow 2 / project authority
canonical PRD meaning                       → content owner
meaning correct, page grammar wrong         → DESIGN-CONTRACT
non-Voice 04 meaning/identity               → Production Assets owner
Voice scope/intent                          → Flow 5
Voice wording/performance                   → Flow 6
canonical sources correct, render wrong     → renderer/compositor
mechanical parity wrong                     → validator/shared owner
```

## Operator facade

Prefer:

```bash
python tools/prd.py impact <changed-path> ... --json
python tools/prd.py impact --git-base <ref> --json
python tools/prd.py status workspace/active/<project>/ --json
python tools/prd.py build workspace/active/<project>/
python tools/prd.py validate workspace/active/<project>/
python tools/prd.py browser workspace/active/<project>/
python tools/prd.py handoff workspace/active/<project>/
python tools/prd.py voice workspace/active/<project>/
```

`impact` selects the smallest proof domains for iteration and flags direct derived-output edits. It does not replace the full `develop → Local` promotion gate.

`status` starts from the deepest present validator and reuses upstream proof. It reports mechanical state and the first structured wrong owner; it does not prove semantic, visual, audio, or approval quality.

Use `browser` only after canonical PRD validation passes and when browser/visual evidence is required.

## Artifact lifecycle

```text
Flow 2  state/source-inventory.yaml
        state/requirement-register.yaml
        state/intake-state.yaml
        work/review.md                 # optional

Flow 3  work/content.md
        work/render-data.json

04      work/asset-requirements.md     # when required

Flow 4  work/acceptance.md
        state/handoff-state.yaml

Voice   work/voice-requirements.md
        work/voice-production.md
        work/voice-acceptance.md
        state/voice-state.yaml

Derived output/README.md
        output/v<version>/prd.html
        output/v<version>/context.md
        output/v<version>/index.json
```

## Context and stop

- Start narrow; expand progressively.
- Batch canonical edits before regeneration.
- Prefer structured owner/state/schema errors over rereading unrelated context.
- Do not load Golden HTML for ordinary semantic work.
- Do not create duplicate schemas, registries, dashboards, approval layers, speculative modes, or compatibility frameworks.
- Stop when requested scope is complete and evidence supports the claim.