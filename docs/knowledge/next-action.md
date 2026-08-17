# Next Action

## Current Status

`UNIFIED_PRD_CREATOR_KIT_M1_CANDIDATE_READY`

The user-approved migration from two historical implementation packages to one categorized `kits/prd-creator/` package remains active.

Durable migration evidence:

```text
operations/unified-prd-creator-kit-migration.md
operations/unified-prd-creator-kit-m0-inventory.md
operations/unified-prd-creator-kit-m1-candidate.md
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

### Completed phases

```text
M0 Baseline + live path inventory             COMPLETE
M1 Build unified package candidate tree       COMPLETE
M2 Consolidate root README/AGENTS/SKILL       NEXT
M3 Runtime + validator path migration         pending
M4 Repository routing synchronization         pending
M5 Retire both old package roots              pending
M6 Full proof + atomic publish                pending
```

M1–M5 remain construction phases for one final migration. Do not publish an intermediate half-migrated architecture.

### M1 candidate

M1 was built as a detached candidate from the M0-complete branch state:

```text
candidate commit
abb80eef10208b5aad30101f5539646d4a3988e3

candidate tree
39cdecda62d23c30ccddc5a943aa84c6f9c7a188
```

Compare result:

```text
33 files added under kits/prd-creator/
0 files modified
0 files deleted
```

All 33 target files reuse current source blobs directly. Golden/runtime templates remain the exact approved blob:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

The Voice validator is staged byte-identically at:

```text
kits/prd-creator/validator/validate_voice.py
```

No runtime implementation refactor has occurred.

### Provisional root-owner boundary

The M1 detached tree uses the Project Document `README.md`, `AGENTS.md`, and `SKILL.md` only as provisional structural copies.

They are not final unified owners.

M2 must reconcile:

```text
Project README + Voice README
→ one scan-first README.md

Project AGENTS + Voice AGENTS
→ one technical/file-routing AGENTS.md

Project SKILL + Voice SKILL
→ one Flow 2–7 Production Execution SKILL.md
```

Root contract remains:

```text
README.md → package map + Requirement Map
AGENTS.md → technical/file routing + context economy
SKILL.md  → Flow 2–7 execution router
```

Detailed domain rules stay in categorized folders.

Unified metadata remains locked:

```text
name: prd-creator
version: 1.14.0
```

Do not concatenate both legacy root files wholesale and do not create another root contract merely to avoid reconciliation.

### Candidate is not publishable yet

The detached M1 candidate must not become `Local` because current tests, CLI examples, workflows, repository verifier, routing docs, and several moved internal owner references still use the old package paths. Both old kit roots also remain intentionally active until M5.

M2/M3/M4/M5 must complete before the final migration candidate is allowed to replace the current architecture.

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
2. read this file + migration plan + M0 + M1 notes;
3. do **not** fast-forward `Local` to detached M1 commit `abb80eef...`;
4. use M1 as verified blob/path construction evidence;
5. build the next detached candidate from current `Local` and replace the three provisional root owner files with M2 reconciled versions;
6. re-pin an M1 source blob only if current source actually changed.

## Next Step

**M2 — consolidate the unified root `README.md`, `AGENTS.md`, and `SKILL.md`.** Compare the two current package root-owner sets, preserve every unique active Flow/routing responsibility, remove only true duplication or superseded prose, set unified metadata to `prd-creator` v1.14.0, keep the root scan-first, and build the next detached candidate without changing runtime/domain semantics or publishing the half-migrated package.