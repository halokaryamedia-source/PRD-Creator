# Unified PRD Creator Kit — M4 Routing Candidate

Updated: 2026-08-17
Status: M4 complete; detached candidate only; not publishable
Migration plan: `unified-prd-creator-kit-migration.md`
M0 inventory: `unified-prd-creator-kit-m0-inventory.md`
M1 candidate: `unified-prd-creator-kit-m1-candidate.md`
M2 root consolidation: `unified-prd-creator-kit-m2-root-consolidation.md`
M3 runtime proof: `unified-prd-creator-kit-m3-runtime-proof.md`
Current Local parent: `d42d5c93b20cc5441e24db4ebf8b63a8e119086b`
M4 detached candidate commit: `1ec47764dae410803f1c899462ec364c2c4aa320`
M4 candidate tree: `c3b73337679e56c1194c2ecb84726249ef58b539`
Unified package subtree: `9b14038c6ac6f9b4d3a568856cdaf1a9b512cb3d`

## Purpose

M4 synchronizes every confirmed **live current consumer** of the historical kit paths to the approved unified package:

```text
kits/prd-creator/
```

It also prepares repository verification, test path constants, and CI path filters for the final one-kit architecture.

M4 does not retire the old package roots. M5 owns that one remaining structural step.

## Current path contract after M4

```text
Flow 2
→ kits/prd-creator/intake/SOURCE-INTAKE.md

PRD core 01–03
→ kits/prd-creator/document/CONTENT-CONTRACT.md

Flow 4
→ kits/prd-creator/document/VALIDATION.md

non-Voice 04
→ kits/prd-creator/production-assets/CONTRACT.md

renderer / delivery
→ kits/prd-creator/renderer/

PRD mechanical validation
→ kits/prd-creator/validator/validate.py

PRD → Voice handoff
→ kits/prd-creator/validator/validate_handoff.py

Flow 5 / Flow 6 / Flow 7
→ kits/prd-creator/voice/

Voice mechanical validation
→ kits/prd-creator/validator/validate_voice.py
```

Project/PRD and Voice remain separate semantic responsibilities inside the package.

## Routing surfaces synchronized

### Repository/root

Updated current routing/orientation:

```text
AGENTS.md
CONTEXT.md
README.md
```

The root no longer presents Project Document Generator and Voice Production Kit as two current product packages.

### Durable foundation policy

Updated current package/CLI owner paths across:

```text
docs/foundation/00-product-boundaries.md
docs/foundation/01-production-flow.md
docs/foundation/02-source-intake-recovery.md
docs/foundation/03-prd-generation.md
docs/foundation/04-prd-validation-handoff.md
docs/foundation/05-voice-requirement-extraction.md
docs/foundation/06-elevenlabs-script-production.md
docs/foundation/07-voice-validation-delivery.md
docs/foundation/README.md
```

The stale current statement that DOCX remained an optional/current export was removed. Historical DOCX evidence is not rewritten merely to erase history.

### Knowledge/current ownership

Updated:

```text
docs/knowledge/ownership.md
docs/knowledge/source-authority.md
docs/knowledge/work-routing.md
docs/knowledge/skills/activation-matrix.md
docs/knowledge/skills/README.md
docs/knowledge/reviews/current-validation.md
```

`source-authority.md` no longer presents DOCX as a current derived surface.

### Root semantic specialists

Updated path routing only:

```text
.agents/skills/project-document-production/SKILL.md
.agents/skills/voice-production/SKILL.md
```

The two semantic specialists remain separate and their semantic ownership did not change.

### Workspace guidance

`workspace/README.md` now uses:

```bash
python kits/prd-creator/renderer/delivery.py \
  workspace/active/<project>/
```

and routes Voice validation to:

```text
kits/prd-creator/validator/validate_voice.py
```

Project artifact locations under `workspace/active/<project>/` are unchanged.

## Unified package internal routing

The M2 root owners remain unchanged:

```text
README.md  → package map + Requirement Map
AGENTS.md  → technical/file routing + context economy
SKILL.md   → Flow 2–7 execution router
```

M4 only reconciles categorized domain procedure/contract references that still used legacy sibling/package names:

```text
intake/SOURCE-INTAKE.md
document/VALIDATION.md
production-assets/CONTRACT.md
renderer/CONTRACT.md
voice/EXTRACTION.md
voice/SOUNDMAKER.md
voice/VALIDATION.md
```

`document/CONTENT-CONTRACT.md` required no path rewrite and retains its existing blob.

## Runtime preservation

M3 established that relocation requires no Python patch. M4 preserves that result.

Current M4 package still uses the exact existing implementation blobs for:

```text
renderer/_engine.py
renderer/core.py
renderer/delivery.py
renderer/pages.py
renderer/production_assets.py
renderer/production_assets_objective.py
renderer/render.py
validator/_engine.py
validator/validate.py
validator/validate_handoff.py
validator/validate_voice.py
```

No Python compatibility wrapper, alias, import framework, or behavior change was added.

Golden/runtime template identity remains:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

Both template files still use that exact blob.

## Tests synchronized

Direct old-path consumers now point to `kits/prd-creator/`:

```text
tests/test_prd_contracts.py
tests/test_prd_content_purity.py
tests/test_prd_delivery.py
tests/test_prd_handoff_contracts.py
tests/test_prd_flow2_state_contracts.py
tests/test_prd_golden_reference.py
tests/test_voice_contracts.py
```

Indirect tests continue to consume those shared constants.

### Flow 2 root-skill regression reconciliation

M2 intentionally changed the unified root `SKILL.md` into a Flow 2–7 router instead of concatenating the legacy Project skill.

The Flow 2 regression was therefore updated to prove the current equivalent routing contract:

```text
SIMPLE CHAT PREVIEW
→ Flow 3 BUILD PRD CORE 01–03
```

while exact Proposal/preview behavior continues to be proved by `intake/SOURCE-INTAKE.md` and `docs/foundation/02-source-intake-recovery.md`.

The test was not weakened to remove the approval boundary and no legacy copy was reintroduced merely to satisfy a literal string assertion.

## CI routing synchronized

The three workflows remain separate:

```text
PRD Verify
→ unified intake/document/production-assets/renderer/template/PRD-validator surfaces

Voice Verify
→ unified voice/ + validator/validate_voice.py

Repository Verify
→ unified package/current repository routing invariants
```

No combined mega-workflow was introduced.

## Repository verifier target state

`tools/verify_repository.py` now describes the **final M5 architecture**:

```text
active kits directory set
→ exactly kits/prd-creator/

required unified domains
→ intake/
→ document/
→ production-assets/
→ voice/
→ renderer/
→ validator/
→ template/

active root Markdown owners
→ README.md
→ AGENTS.md
→ SKILL.md
```

It also treats both old roots as retired boundaries:

```text
kits/project-document-generator/
kits/voice-production-kit/
```

and validates one unified `SKILL.md` ↔ `README.md` version pair.

Because M4 intentionally retains the old roots until M5, this final-target verifier is expected to reject the M4 construction tree on that structural condition. Do not weaken the verifier to make the intermediate candidate pass.

## Historical evidence boundary

Historical audits/reviews/decisions, the moved Voice CHANGELOG, migration notes, and the Aftershock Voice reference may continue to describe the former package/artifact names when they are genuinely historical evidence.

After the old roots are removed, any **actual relative Markdown link** that becomes broken must be fixed minimally or converted to truthful historical path wording. Do not create compatibility directories solely to preserve old links.

## Candidate shape and remaining blocker

The detached M4 candidate currently contains all three directories:

```text
kits/prd-creator/
kits/project-document-generator/
kits/voice-production-kit/
```

This is deliberate construction state, not final architecture.

The only planned structural blocker before full proof is retirement of the two historical roots.

## Protected project state

The M4 compare contains no changes under:

```text
workspace/active/
```

Therefore current Clockwork source/state/acceptance/generated delivery is untouched by M4.

Protected baseline delivery markers remain:

```text
prd.html    dac955a4a482ad9dc2035f0c5714c87ae4de05c5
context.md  003cc0068505339b8406b445601b7350bffa70a5
index.json  c205422dc0d639b5d0bf9081364321c318e23d22
```

## Superseded detached candidate

An earlier M4 construction commit `d4a0412f1493ad30bd370b3ef3ffb4fbde41fa4a` was replaced before publication because the Flow 2 regression still asserted legacy root-SKILL wording.

Use only this M4 candidate going forward:

```text
1ec47764dae410803f1c899462ec364c2c4aa320
```

The superseded detached commit never became `Local`.

## Proof boundary

M4 proves routing synchronization by exact candidate construction/inspection. It does **not** claim the final regression/Clockwork/Repository Verify result yet because the candidate intentionally still contains the two old roots.

M6 owns full executable/project/CI proof after M5 produces the one-kit final candidate.

## Recovery rule

If a session ends before M5:

1. pin current `Local`;
2. read `next-action.md`, migration plan, M0, M1, M2, M3, and this M4 note;
3. treat `1ec47764dae410803f1c899462ec364c2c4aa320` as the only current detached M4 construction candidate;
4. do not publish it directly;
5. do not re-add compatibility paths or weaken the final-target repository verifier;
6. continue with M5 by removing the two old package roots from the M4 candidate and handling only mechanically broken historical links if found.

## M5 entry contract

M5 is a retirement step, not another redesign pass.

Starting from the M4 candidate:

```text
remove kits/project-document-generator/
remove kits/voice-production-kit/
→ inspect exact final kits/ shape
→ inspect current routing for accidental old-path consumers
→ repair only actual broken historical relative links
→ produce one detached one-kit candidate
```

Do not change runtime behavior, Golden bytes, project meaning, Voice wording, workspace project state, test organization, tool organization, or workflow separation during M5.
