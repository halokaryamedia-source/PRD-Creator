# Next Action

## Current Status

`UNIFIED_PRD_CREATOR_KIT_MIGRATION_PLANNED`

P0 Current Authority Integrity, bounded P1 remediation including DOCX retirement, and P2 mechanical cleanup remain complete. A new user-approved Developing objective is now active: replace the historical two-kit package split with one categorized `kits/prd-creator/` product package without changing product semantics or generated output.

Canonical migration plan:

`operations/unified-prd-creator-kit-migration.md`

Repository continuity remains:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules for material GitHub work
→ CONTEXT.md
→ next-action.md
→ development-brief for non-trivial Developing
→ operations/unified-prd-creator-kit-migration.md
→ smallest relevant current owner/source
```

## Active Boundary

### User-approved architecture direction

Current top-level implementation:

```text
kits/
├─ project-document-generator/
└─ voice-production-kit/
```

Target top-level implementation:

```text
kits/
└─ prd-creator/
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

The migration merges **package ownership**, not semantic domains. Project/PRD and Voice remain distinct responsibilities inside one product package.

Root-file rule:

```text
README.md → package map + Requirement Map
AGENTS.md → technical/file routing
SKILL.md  → Flow 2–7 Production Execution router
```

Detailed contracts/procedures stay under their category folders.

### Requirement mapping principle

Do not create a generic `requirements/` folder. Requirement instances remain project artifacts and their system contracts stay with the domain that owns them:

```text
project/gameplay requirement state
→ state/requirement-register.yaml
→ intake/SOURCE-INTAKE.md

canonical PRD meaning
→ work/content.md
→ document/CONTENT-CONTRACT.md

non-Voice Production Asset requirements
→ work/asset-requirements.md
→ production-assets/CONTRACT.md

Voice requirements
→ work/voice-requirements.md
→ voice/EXTRACTION.md

canonical Voice production
→ work/voice-production.md
→ Flow 6 routing + voice/SOUNDMAKER.md
```

### Migration phase state

```text
M0 Baseline + live path inventory             NEXT
M1 Build unified package tree                 pending
M2 Consolidate root README/AGENTS/SKILL       pending
M3 Runtime + validator path migration         pending
M4 Repository routing synchronization         pending
M5 Retire both old package roots              pending
M6 Full proof + atomic publish                pending
```

The detailed old→new path map, collision rule, proof budget, baseline blob markers, non-goals, commit strategy, and session-recovery procedure are recorded in the migration plan. Do not recreate those decisions from chat memory.

## Safety / Non-Goals

This migration must not change:

- Golden/runtime template bytes;
- PRD 01–03 meaning, hierarchy, or presentation;
- 04 Production Assets reader-facing contract;
- gameplay/project facts;
- Voice requirements or canonical Voice wording/performance;
- current Clockwork state/acceptance/generated delivery;
- root `tests/` organization;
- root `tools/` organization;
- the separate PRD Verify and Voice Verify proof surfaces;
- the separate root semantic specialists `project-document-production` and `voice-production`.

Do not create compatibility stub kits, generic requirement/parser/schema/manifest/registry frameworks, a second HTML/export surface, or aesthetic renderer refactors.

Historical review/CHANGELOG prose may retain historical package names when it is genuine evidence. Current paths, commands, relative links, routing owners, imports, workflows, and runtime references must use the unified package after migration.

## Baseline

User-approved planning baseline:

```text
Local HEAD
9c55aaf36786ca55c26d4158d8d6c938c8b7a795

Golden/runtime template blob
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1

Clockwork current delivery blobs
prd.html    dac955a4a482ad9dc2035f0c5714c87ae4de05c5
context.md  003cc0068505339b8406b445601b7350bffa70a5
index.json  c205422dc0d639b5d0bf9081364321c318e23d22
```

If `Local` moves before implementation, re-pin and reconcile the new source state with the migration plan before writing.

## Session Recovery

If a session ends during this work:

1. boot from current repository authority, not chat memory;
2. read this file and `operations/unified-prd-creator-kit-migration.md`;
3. pin `Local` and compare actual tree state to the recorded phase state;
4. never assume temporary candidate blobs/trees survived or were published;
5. do not publish a knowingly half-migrated package merely to preserve progress.

The migration plan and `next-action.md` are the durable recovery point.

## Next Step

**M0 — Baseline + live path inventory.** Pin current `Local`, enumerate every live reference/import/CLI/workflow/test/tool dependency on `kits/project-document-generator` and `kits/voice-production-kit`, classify historical-only references separately, resolve the unified-kit version/collision decisions from current owners, and only then prepare the complete atomic migration candidate. Do not move files before this inventory is complete.