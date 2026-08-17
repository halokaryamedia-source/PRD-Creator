# Unified PRD Creator Kit — M0 Live Path Inventory

Updated: 2026-08-17
Status: M0 complete; no package files moved
Migration plan: `unified-prd-creator-kit-migration.md`
Pinned branch: `Local`
Pinned HEAD: `fca07b15c322298163005195302a3c5026603175`
Pinned tree: `3010617b10218c628d46e80f8e4e8e42cdeb265a`

## Purpose

This note is the durable M0 evidence for the user-approved migration from two historical implementation packages:

```text
kits/project-document-generator/
kits/voice-production-kit/
```

to one categorized product package:

```text
kits/prd-creator/
```

It identifies live path consumers, separates historical evidence, locks collision/version decisions, and defines the exact assumptions M1 may rely on. It does not move files or change product behavior.

## Baseline integrity

Current M0 evidence confirms the original migration integrity markers are still unchanged after the planning-only commits:

```text
Golden / runtime template blob
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1

Clockwork current delivery
prd.html    dac955a4a482ad9dc2035f0c5714c87ae4de05c5
context.md  003cc0068505339b8406b445601b7350bffa70a5
index.json  c205422dc0d639b5d0bf9081364321c318e23d22
```

The implementation baseline content is therefore still the same product/runtime state that existed at `9c55aaf36786ca55c26d4158d8d6c938c8b7a795`; `404a106...` and `fca07b15...` only persisted migration continuity/planning.

## M0 key result

The migration does **not** require a broad Python refactor.

Current executable implementation mostly depends on local sibling topology rather than the literal old kit root names:

```text
renderer/render.py
→ HERE = renderer directory
→ imports sibling _engine / production_assets_objective
→ template = HERE.parent / template

renderer/delivery.py
→ imports sibling render
→ template = HERE.parent / template

validator/validate.py
→ imports sibling _engine

validator/validate_handoff.py
→ imports sibling _engine

renderer/production_assets_objective.py
→ imports sibling core / production_assets

Voice validator
→ standalone file; no dependency on the Voice-kit directory name
```

Because the target keeps `renderer/`, `validator/`, and `template/` as sibling directories under `kits/prd-creator/`, these relative assumptions remain valid after a path-root move. The only required executable filename collision is the Voice validator rename to `validator/validate_voice.py`.

Therefore M1 must prefer byte-preserving moves for Python implementation and reserve edits for actual path consumers.

## Live path consumer inventory

### A. Repository/root routing — MUST UPDATE

These are current authorities or current navigation surfaces. Old package identity/path text must not remain active after migration.

```text
AGENTS.md
CONTEXT.md
README.md
```

Required migration effect:

- replace two-kit production-front-door wording with one `kits/prd-creator/` package;
- preserve the two semantic specialists (`project-document-production`, `voice-production`);
- root README reports one current kit version rather than two package versions;
- no product/output semantics change.

### B. Durable foundation policy — MUST UPDATE WHERE PATH/NAMING IS LIVE

Confirmed live path/name consumers:

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

Concrete path-sensitive examples confirmed during M0:

```text
Flow 2 detailed procedure
kits/project-document-generator/SOURCE-INTAKE.md
→ kits/prd-creator/intake/SOURCE-INTAKE.md

Flow 3 content owner
kits/project-document-generator/CONTENT-CONTRACT.md
→ kits/prd-creator/document/CONTENT-CONTRACT.md

Flow 4 owners
kits/project-document-generator/{CONTENT-CONTRACT,PRODUCTION-ASSETS,VALIDATION}.md
→ categorized unified-kit owners

Flow 5 handoff CLI
kits/project-document-generator/validator/validate_handoff.py
→ kits/prd-creator/validator/validate_handoff.py

Flow 7 Voice CLI
kits/voice-production-kit/validator/validate.py
→ kits/prd-creator/validator/validate_voice.py
```

Flow 6 currently uses short owner names such as `SOUNDMAKER.md`. After migration, foundation policy should identify `kits/prd-creator/voice/SOUNDMAKER.md` when a fully qualified owner is needed.

M0 also found stale DOCX language in current `docs/foundation/README.md`. DOCX is already retired. Remove that stale current-policy wording during M4; do not revive or replace the export.

### C. Current knowledge/routing owners — MUST UPDATE

Confirmed current owners whose package map or current paths/names must change:

```text
docs/knowledge/ownership.md
docs/knowledge/source-authority.md
docs/knowledge/work-routing.md
docs/knowledge/skills/activation-matrix.md
docs/knowledge/skills/README.md
docs/knowledge/reviews/current-validation.md
```

Key M0 findings:

- `ownership.md` currently maps responsibilities to both old kit roots;
- `source-authority.md` points Flow 2 to the old `SOURCE-INTAKE.md` path;
- `source-authority.md` also still contains stale retired-DOCX wording; clean it as current-authority drift during M4;
- work-routing and skill-navigation text still describes two nearest kit packages;
- current-validation still records separate Project Document Generator and Voice Production Kit versions; after migration it must record one unified package version while keeping Voice scope distinct.

`docs/knowledge/next-action.md` and this operations note are migration continuity and may intentionally mention old paths while describing the migration.

### D. Root semantic specialists — MUST UPDATE PATH ROUTING ONLY

```text
.agents/skills/project-document-production/SKILL.md
.agents/skills/voice-production/SKILL.md
```

Both semantic specialists remain separate.

Only detailed-owner routing changes:

```text
project-document-production
→ kits/prd-creator/intake|document|production-assets|renderer/... as appropriate

voice-production
→ kits/prd-creator/voice/... and unified production-assets/renderer owners as appropriate
```

Do not merge the semantic skills or change their semantic responsibilities as part of this migration.

### E. Workspace/package guidance — MUST UPDATE

```text
workspace/README.md
```

Current command examples use the old Project Document renderer path. Change the normal delivery command to:

```bash
python kits/prd-creator/renderer/delivery.py \
  workspace/active/<project>/
```

Project artifact paths under `workspace/active/<project>/` do not move.

Current Clockwork state/output must remain byte-identical through the structural migration unless a proof step demonstrates an unavoidable generated metadata path (none is currently expected).

### F. Package documentation — MOVE + RECONCILE

Current Project Document package owners:

```text
kits/project-document-generator/README.md
kits/project-document-generator/AGENTS.md
kits/project-document-generator/SKILL.md
kits/project-document-generator/SOURCE-INTAKE.md
kits/project-document-generator/CONTENT-CONTRACT.md
kits/project-document-generator/GLOSSARY.md
kits/project-document-generator/PRODUCTION-ASSETS.md
kits/project-document-generator/RENDERING.md
kits/project-document-generator/VALIDATION.md
```

Current Voice package owners:

```text
kits/voice-production-kit/README.md
kits/voice-production-kit/AGENTS.md
kits/voice-production-kit/SKILL.md
kits/voice-production-kit/VOICE-EXTRACTION.md
kits/voice-production-kit/SOUNDMAKER.md
kits/voice-production-kit/VOICE-VALIDATION.md
kits/voice-production-kit/CHANGELOG.md
kits/voice-production-kit/LICENSE
kits/voice-production-kit/references/**
```

M1 may path-move domain files using the approved mapping. M2 must reconcile only the root README/AGENTS/SKILL collisions.

Important relative-link/topology notes:

- Voice ElevenLabs reference links remain naturally valid when the whole `references/` tree moves under `voice/references/` (for example `../../SOUNDMAKER.md` still resolves to `voice/SOUNDMAKER.md`);
- the Aftershock reference is historical evidence and may retain discussion of the former DOCX benchmark, but must not be treated as a current DOCX owner or current delivery route;
- current package docs that use sibling owner names (`CONTENT-CONTRACT.md`, `PRODUCTION-ASSETS.md`, `RENDERING.md`, `VALIDATION.md`, `SOUNDMAKER.md`) need relative-owner reconciliation after categorization.

### G. Python/runtime implementation — MOVE; MINIMAL EDIT

Path-root moves, preserving filenames/bytes where possible:

```text
kits/project-document-generator/renderer/*
→ kits/prd-creator/renderer/*

kits/project-document-generator/validator/_engine.py
→ kits/prd-creator/validator/_engine.py

kits/project-document-generator/validator/validate.py
→ kits/prd-creator/validator/validate.py

kits/project-document-generator/validator/validate_handoff.py
→ kits/prd-creator/validator/validate_handoff.py

kits/project-document-generator/template/*
→ kits/prd-creator/template/*

kits/voice-production-kit/validator/validate.py
→ kits/prd-creator/validator/validate_voice.py
```

No compatibility wrapper/symlink/stub may remain at the old roots.

### H. Tests — PATH CONSTANTS MUST UPDATE; ROOT TEST LAYOUT STAYS

Direct old-path consumers confirmed:

```text
tests/test_prd_contracts.py
  RENDERER
  DELIVERY
  VALIDATOR
  RUNTIME_TEMPLATE
  GOLDEN_TEMPLATE

tests/test_prd_content_purity.py
  VALIDATOR

tests/test_prd_delivery.py
  RENDERER directory import path

tests/test_prd_handoff_contracts.py
  HANDOFF_VALIDATOR
  RENDERER

tests/test_prd_flow2_state_contracts.py
  SOURCE_INTAKE
  KIT_SKILL

tests/test_prd_golden_reference.py
  KIT / GOLDEN / RUNTIME

tests/test_voice_contracts.py
  VALIDATOR
```

Indirect consumers that inherit path constants from the files above must continue to pass, including:

```text
tests/test_prd_voice_assets.py
tests/test_prd_hierarchy_contracts.py
```

Root `tests/` organization is intentionally unchanged.

### I. CI workflows — MUST UPDATE; REMAIN SEPARATE

```text
.github/workflows/prd-verify.yml
.github/workflows/voice-verify.yml
.github/workflows/repository-verify.yml
```

Current old-root dependencies confirmed:

- PRD Verify path filters and compile target use `kits/project-document-generator/...`;
- Voice Verify path filters and compile target use `kits/voice-production-kit/...`;
- Repository Verify watches both old kit Markdown roots.

Target proof routing:

```text
PRD Verify
→ unified intake/document/production-assets/renderer/PRD-validator surfaces + PRD tests

Voice Verify
→ unified voice/ + validator/validate_voice.py + Voice tests

Repository Verify
→ unified kit Markdown/routing + repository invariant checks
```

Do not merge the workflows.

### J. Repository verifier — MUST UPDATE

`tools/verify_repository.py` currently hard-codes the two-kit architecture in:

```text
REQUIRED_PATHS
MARKDOWN_ROOTS
CURRENT_DELIVERY_OWNER_PATHS
Project Document SKILL/README version check
retired-path rules
```

M5 target invariants:

```text
kits/prd-creator/ exists
kits/project-document-generator/ absent
kits/voice-production-kit/ absent

kits/prd-creator/ root active Markdown owners:
README.md
AGENTS.md
SKILL.md

required categorized folders:
intake/
document/
production-assets/
voice/
renderer/
validator/
template/
```

Do not overconstrain every possible future subdirectory.

## Historical-only / preserve-as-history classification

Do not rewrite historical evidence merely to erase former package names.

Default historical category:

```text
docs/knowledge/reviews/* historical review/audit records
historical sections of docs/knowledge/decisions/*
voice/CHANGELOG.md after move
migration plan old→new mapping
historical Voice reference prose when explicitly describing old artifacts
Git history
```

Exception: `docs/knowledge/reviews/current-validation.md` is a **current** evidence owner, not historical, and must use the unified package identity after migration.

If a historical Markdown link would become mechanically broken after the move, prefer the smallest truthful update or convert it to explicit historical path wording. Do not create compatibility files solely to preserve historical links.

## Version decision — LOCKED FOR M1–M6

The unified package will keep the current Project Document package version **1.14.0** for this migration.

Target metadata:

```yaml
name: prd-creator
version: 1.14.0
```

Target unified README:

```text
**Version:** 1.14.0
```

Reason:

- the migration is structural/package ownership cleanup, not a product capability release;
- current PRD/04/Voice behavior already exists before the move;
- changing the version would create unrelated release state during a behavior-preserving migration;
- repository rules prefer not to change release/version metadata without a real release requirement.

The former Voice Production Kit `1.11.2` remains historical provenance in `voice/CHANGELOG.md`; it stops being presented as a separate current package version after M2/M4.

`tools/verify_repository.py` must replace the old Project-Document-specific version pairing check with one unified `kits/prd-creator/SKILL.md` ↔ `kits/prd-creator/README.md` version check.

## Collision decisions — LOCKED

### Root owner collision

```text
project README + voice README
→ one kits/prd-creator/README.md

project AGENTS + voice AGENTS
→ one kits/prd-creator/AGENTS.md

project SKILL + voice SKILL
→ one kits/prd-creator/SKILL.md
```

These are semantic reconciliations, not concatenations.

### Validator filename collision

```text
Project validator/validate.py
→ validator/validate.py

Voice validator/validate.py
→ validator/validate_voice.py
```

PRD validator keeps the generic `validate.py` name because the kit's primary document gate remains the PRD/document validation entry point; Voice is a downstream domain-specific gate.

### Domain-file naming

Locked approved renames:

```text
PRODUCTION-ASSETS.md
→ production-assets/CONTRACT.md

RENDERING.md
→ renderer/CONTRACT.md

VOICE-EXTRACTION.md
→ voice/EXTRACTION.md

VOICE-VALIDATION.md
→ voice/VALIDATION.md
```

Do not add further aesthetic renames during this migration.

### Voice-only historical/support files

```text
CHANGELOG.md
LICENSE
references/**
```

move under `voice/` and do not become unified root owners.

## M1 input contract

M1 may now build the complete candidate `kits/prd-creator/` tree using these rules:

1. use current `Local` as source authority, not the original planning commit;
2. preserve Python/template/reference bytes when the move alone is sufficient;
3. build all categorized target paths before retiring either old root;
4. do not publish a half-migrated tree;
5. do not create compatibility wrappers;
6. defer current routing/test/workflow/tool rewrites to the same complete migration candidate (M3/M4/M5), not separate production commits;
7. preserve Golden/runtime blob identity and current Clockwork delivery bytes;
8. root README/AGENTS/SKILL consolidation follows the locked root-file rule and version decision above.

## M0 completion statement

M0 is complete.

No package/runtime source was moved or changed. The next implementation phase is **M1 — build the complete unified package candidate tree**, using this inventory plus `unified-prd-creator-kit-migration.md` as durable authority.

This note supersedes the migration plan's original bottom-line instruction to start M0; do not repeat M0 in a new session unless `Local` has materially changed in a way that invalidates this inventory.