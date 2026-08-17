# Next Action

## Current Status

`UNIFIED_PRD_CREATOR_KIT_M2_ROOTS_READY`

The user-approved migration from two historical implementation packages to one categorized `kits/prd-creator/` package remains active.

Durable migration evidence:

```text
operations/unified-prd-creator-kit-migration.md
operations/unified-prd-creator-kit-m0-inventory.md
operations/unified-prd-creator-kit-m1-candidate.md
operations/unified-prd-creator-kit-m2-root-consolidation.md
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
→ M1 candidate note
→ M2 root consolidation note
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

The package merge does not merge semantic domains. Project/PRD and Voice remain separate responsibilities inside one implementation package.

### Phase state

```text
M0 Baseline + live path inventory             COMPLETE
M1 Build unified package candidate tree       COMPLETE
M2 Consolidate root README/AGENTS/SKILL       COMPLETE
M3 Runtime + validator path migration         NEXT
M4 Repository routing synchronization         pending
M5 Retire both old package roots              pending
M6 Full proof + atomic publish                pending
```

M1–M5 remain construction phases for one final migration. Do not publish an intermediate half-migrated architecture.

## M2 candidate

M2 detached candidate:

```text
commit
 e1523e22f90a666ec14bf4f0d260bb9238305537

tree
 00687140e2d47596a38bdac666a84d8218642ab2

kits/prd-creator subtree
 e56566a73ea9d2729f671411abae06d467206337
```

Unified root blobs:

```text
README.md  42f1f031f58f2be0e2a8e4a85f1818025e29cc1d
AGENTS.md  96caa183c9d5e0f4ebb7f3ee0cb88f4700972681
SKILL.md   70cd976fd27a2561c52f1b44f1ea6e4a6e094e2a
```

M2 changed only those three package-root owners from the M1 construction baseline. All categorized subtrees remain byte/tree-identical to M1, including Golden/runtime, renderer, validator, domain contracts, Voice references, and license/changelog.

### Root owner contract now resolved

```text
README.md
→ package orientation + Requirement Map + canonical/derived map

AGENTS.md
→ unified technical/file routing + context economy

SKILL.md
→ end-to-end Flow 2–7 Production Execution router
```

Unified metadata is locked:

```yaml
name: prd-creator
version: 1.14.0
```

The root skill keeps Project/PRD and Voice procedures connected but not semantically collapsed. Exact rules remain in categorized owners:

```text
Flow 2 → intake/SOURCE-INTAKE.md
Flow 3 → document/CONTENT-CONTRACT.md
Flow 4 → document/VALIDATION.md
04     → production-assets/CONTRACT.md
Flow 5 → voice/EXTRACTION.md
Flow 6 → docs/foundation/06-elevenlabs-script-production.md + voice/SOUNDMAKER.md
Flow 7 → voice/VALIDATION.md
```

Separate root semantic specialists remain:

```text
.agents/skills/project-document-production/
.agents/skills/voice-production/
```

## Candidate is still not publishable

Do not fast-forward `Local` to the M2 candidate yet. Live current architecture still depends on the old package paths through tests, commands, workflows, repository verification, current routing docs, and old-root ownership.

Both historical package roots remain intentionally active until M5.

## Safety / Non-Goals

Do not change during this migration:

- Golden/runtime template bytes;
- PRD 01–03 meaning/hierarchy/presentation;
- 04 reader-facing Production Assets contract;
- gameplay/project facts;
- Voice requirements or canonical Voice wording/performance;
- current Clockwork state/acceptance/generated delivery;
- root `tests/` or `tools/` organization;
- separate PRD Verify and Voice Verify proof surfaces;
- separate semantic root specialists.

Do not create compatibility kit stubs, symlinks, generic requirement/parser/schema/manifest/registry frameworks, another export surface, or aesthetic renderer refactors.

## Recovery

If a session resumes from here:

1. pin current `Local`;
2. read this file + migration plan + M0 + M1 + M2 notes;
3. do not fast-forward `Local` to detached M2 commit `e1523e22...`;
4. use the recorded `kits/prd-creator` subtree as construction evidence;
5. rebuild only if a current source owner materially changed;
6. continue with M3 before touching repository-wide routing or retiring old roots.

## Next Step

**M3 — runtime + validator path migration.** Starting from the M2 unified package candidate, prove the moved renderer/validator/template topology is executable under `kits/prd-creator/`. Update only real Python path/import/CLI assumptions required by the new package layout; preserve byte-identical implementation wherever sibling-relative behavior already works. Verify PRD renderer/delivery, PRD validator/handoff validator, and Voice validator through the new paths before advancing to M4. Do not yet update repository-wide tests/workflow/routing paths or remove the old kit roots.