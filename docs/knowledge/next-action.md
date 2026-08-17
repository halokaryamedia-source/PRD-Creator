# Next Action

## Current Status

`UNIFIED_PRD_CREATOR_KIT_M3_RUNTIME_PATH_PROVEN`

The user-approved migration from the two historical implementation packages to one categorized `kits/prd-creator/` package remains active.

Durable migration evidence:

```text
operations/unified-prd-creator-kit-migration.md
operations/unified-prd-creator-kit-m0-inventory.md
operations/unified-prd-creator-kit-m1-candidate.md
operations/unified-prd-creator-kit-m2-root-consolidation.md
operations/unified-prd-creator-kit-m3-runtime-proof.md
```

Repository continuity:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules
→ CONTEXT.md
→ next-action.md
→ development-brief for non-trivial Developing
→ migration plan
→ M0 inventory
→ M1 candidate
→ M2 root consolidation
→ M3 runtime proof
→ smallest relevant current owner/source
```

## Active Boundary

### Target package

```text
kits/prd-creator/
├─ README.md
├─ AGENTS.md
├─ SKILL.md
├─ intake/
├─ document/
├─ production-assets/
├─ voice/
├─ renderer/
├─ validator/
└─ template/
```

Project/PRD and Voice remain separate semantic responsibilities inside one implementation package.

### Phase state

```text
M0 Baseline + live path inventory             COMPLETE
M1 Build unified package candidate tree       COMPLETE
M2 Consolidate root README/AGENTS/SKILL       COMPLETE
M3 Runtime + validator path migration         COMPLETE — no code change required
M4 Repository routing synchronization         NEXT
M5 Retire both old package roots              pending
M6 Full proof + atomic publish                pending
```

M1–M5 are still construction phases for one final migration. Do not publish a half-migrated architecture.

## Current construction baseline

M2 detached candidate remains the package implementation baseline because M3 required no executable edits:

```text
candidate commit
 e1523e22f90a666ec14bf4f0d260bb9238305537

candidate tree
 00687140e2d47596a38bdac666a84d8218642ab2

kits/prd-creator subtree
 e56566a73ea9d2729f671411abae06d467206337
```

Unified root blobs remain:

```text
README.md  42f1f031f58f2be0e2a8e4a85f1818025e29cc1d
AGENTS.md  96caa183c9d5e0f4ebb7f3ee0cb88f4700972681
SKILL.md   70cd976fd27a2561c52f1b44f1ea6e4a6e094e2a
```

Golden/runtime remain:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

## M3 result

Actual candidate source confirms the new package preserves the executable topology already expected by current code:

```text
renderer/render.py
→ HERE = renderer/
→ sibling _engine.py
→ sibling production_assets_objective.py
→ ../template/runtime-template.html

renderer/_engine.py
→ sibling core.py + pages.py

renderer/production_assets_objective.py
→ sibling core.py + production_assets.py

renderer/delivery.py
→ sibling render.py
→ ../template/runtime-template.html

validator/validate.py
→ sibling _engine.py

validator/validate_handoff.py
→ sibling _engine.py under normal script execution

validator/validate_voice.py
→ standalone; former Voice kit root name is not required
```

An isolated executable topology smoke using the approved `kits/prd-creator/{renderer,validator,template}` relationships passed compile/import/template-resolution checks for renderer, delivery, PRD validator, handoff validator, and Voice validator.

Therefore M3 outcome is:

```text
NO EXECUTABLE CODE CHANGE REQUIRED
```

Do not add compatibility imports, package aliases, symlinks, or wrappers merely for relocation.

## Proof boundary

M3 proves relocation mechanics only. Full regressions and actual Clockwork validation are intentionally reserved until repository consumers have moved to the new package in M4/M5 and are part of M6.

Do not claim M6-level proof from the M3 topology smoke.

## M4 Scope

Synchronize **live current repository consumers** from the old paths to the unified package.

Expected affected areas from M0 inventory include, as applicable:

```text
README.md
AGENTS.md
CONTEXT.md

docs/foundation/*
docs/knowledge/ownership.md
docs/knowledge/work-routing.md
docs/knowledge/source-authority.md
docs/knowledge/skills/*
current review/routing owners when they contain active package paths

.agents/skills/project-document-production/SKILL.md
.agents/skills/voice-production/SKILL.md

workspace/README.md

.github/workflows/prd-verify.yml
.github/workflows/voice-verify.yml
.github/workflows/repository-verify.yml

tests/* live path constants/import targets

tools/verify_repository.py
```

Use the M0 inventory to distinguish live routing from historical evidence. Genuine historical reviews/CHANGELOG may keep historical package names.

### M4 required current-path mapping

```text
kits/project-document-generator/SOURCE-INTAKE.md
→ kits/prd-creator/intake/SOURCE-INTAKE.md

kits/project-document-generator/CONTENT-CONTRACT.md
→ kits/prd-creator/document/CONTENT-CONTRACT.md

kits/project-document-generator/PRODUCTION-ASSETS.md
→ kits/prd-creator/production-assets/CONTRACT.md

kits/project-document-generator/RENDERING.md
→ kits/prd-creator/renderer/CONTRACT.md

kits/project-document-generator/VALIDATION.md
→ kits/prd-creator/document/VALIDATION.md

kits/project-document-generator/renderer/**
→ kits/prd-creator/renderer/**

kits/project-document-generator/validator/validate.py
→ kits/prd-creator/validator/validate.py

kits/project-document-generator/validator/validate_handoff.py
→ kits/prd-creator/validator/validate_handoff.py

kits/project-document-generator/template/**
→ kits/prd-creator/template/**

kits/voice-production-kit/VOICE-EXTRACTION.md
→ kits/prd-creator/voice/EXTRACTION.md

kits/voice-production-kit/SOUNDMAKER.md
→ kits/prd-creator/voice/SOUNDMAKER.md

kits/voice-production-kit/VOICE-VALIDATION.md
→ kits/prd-creator/voice/VALIDATION.md

kits/voice-production-kit/validator/validate.py
→ kits/prd-creator/validator/validate_voice.py

both legacy root README/AGENTS/SKILL routes
→ kits/prd-creator/{README.md,AGENTS.md,SKILL.md}
```

### Current stale DOCX wording

M0 found current-authority DOCX drift outside historical evidence, including `docs/foundation/README.md` and `docs/knowledge/source-authority.md`. M4 must remove current statements that still present DOCX as an optional/current derived surface. Do not rewrite historical evidence solely to erase the old feature.

## Safety / Non-Goals

Do not change during M4:

- product/gameplay meaning;
- PRD 01–03 semantics or presentation;
- Production Assets reader-facing contract;
- Voice requirements or canonical wording/performance;
- renderer/validator behavior unless a concrete routing defect is reproduced;
- Golden/runtime bytes;
- current Clockwork project files/output;
- root tests/tools folder organization;
- separate PRD Verify and Voice Verify proof surfaces;
- separate semantic root specialists.

Do not create compatibility kit stubs or a second path hierarchy.

Both historical package roots remain until M5.

## Recovery

If a session resumes from here:

1. pin current `Local`;
2. read this file + migration plan + M0 + M1 + M2 + M3 notes;
3. treat M3 as `NO EXECUTABLE CODE CHANGE REQUIRED` unless current source changed materially;
4. use the M2 unified package subtree as the implementation baseline;
5. perform M4 as one coherent current-routing synchronization candidate;
6. do not delete old package roots until M5.

## Next Step

**M4 — repository routing synchronization.** Build one detached candidate that rewrites every live current package path/CLI/test/workflow/verifier/routing owner identified by M0 to `kits/prd-creator/`, updates the renamed domain/validator targets exactly, removes current stale DOCX routing language, and preserves historical evidence. Do not remove the two old package roots yet; M5 owns retirement after M4 proves there are no live consumers left.