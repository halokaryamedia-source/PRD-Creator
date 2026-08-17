# Next Action

## Current Status

`UNIFIED_PRD_CREATOR_KIT_M0_COMPLETE`

The user-approved migration from two historical implementation packages to one categorized `kits/prd-creator/` product package remains active.

Canonical plan:

`operations/unified-prd-creator-kit-migration.md`

Completed M0 evidence / locked decisions:

`operations/unified-prd-creator-kit-m0-inventory.md`

Repository continuity:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules for material GitHub work
→ CONTEXT.md
→ next-action.md
→ development-brief for non-trivial Developing
→ unified-prd-creator-kit-migration.md
→ unified-prd-creator-kit-m0-inventory.md
→ smallest relevant current owner/source
```

## Active Boundary

### Target architecture

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

The package merge does not merge semantic domains. Project/PRD judgment and Voice judgment remain distinct responsibilities inside one implementation package.

Root-file contract remains locked:

```text
README.md → package map + Requirement Map
AGENTS.md → unified technical/file routing
SKILL.md  → Flow 2–7 Production Execution router
```

Detailed domain contracts stay in categorized folders.

### M0 result

M0 pinned the current implementation baseline and inventoried live consumers of:

```text
kits/project-document-generator/
kits/voice-production-kit/
```

Key finding: current Python runtime code primarily uses sibling-relative topology, not literal old kit-root strings. `renderer/`, PRD `validator/`, and `template/` can therefore be moved with bytes preserved in most cases. The Voice validator is standalone and moves to `validator/validate_voice.py` only to resolve the filename collision.

Path-sensitive work is concentrated in:

- current root/foundation/knowledge routing docs;
- current package README/AGENTS/SKILL and domain-owner links;
- CLI examples;
- test path constants;
- PRD/Voice/Repository workflow filters and compile targets;
- `tools/verify_repository.py` architecture/version invariants;
- workspace guidance.

Historical review/audit/CHANGELOG prose may retain historical package names when it is genuine evidence. Current routing/commands/owners must use the unified package after migration.

M0 also identified a few current stale DOCX references left outside the previous retirement scope (`docs/foundation/README.md`, `docs/knowledge/source-authority.md`). They are current-authority drift and must be removed during M4; DOCX must not be revived or replaced.

### Locked version/collision decisions

Unified package metadata for this behavior-preserving structural migration:

```text
name: prd-creator
version: 1.14.0
README Version: 1.14.0
```

Do not create a new release/version bump merely for the path migration. Legacy Voice Kit `1.11.2` remains historical provenance in moved `voice/CHANGELOG.md`, not a separate current package version.

Locked collisions:

```text
Project README + Voice README → one root README.md
Project AGENTS + Voice AGENTS → one root AGENTS.md
Project SKILL + Voice SKILL → one root SKILL.md

PRD validator/validate.py   → validator/validate.py
Voice validator/validate.py → validator/validate_voice.py
```

Approved domain renames remain only:

```text
PRODUCTION-ASSETS.md → production-assets/CONTRACT.md
RENDERING.md         → renderer/CONTRACT.md
VOICE-EXTRACTION.md  → voice/EXTRACTION.md
VOICE-VALIDATION.md  → voice/VALIDATION.md
```

No additional aesthetic Python/file renames.

### Phase state

```text
M0 Baseline + live path inventory             COMPLETE
M1 Build unified package candidate tree       NEXT
M2 Consolidate root README/AGENTS/SKILL       pending
M3 Runtime + validator path migration         pending
M4 Repository routing synchronization         pending
M5 Retire both old package roots              pending
M6 Full proof + atomic publish                pending
```

M1–M5 are construction phases for **one complete migration candidate**. Do not publish intermediate half-migrated package states merely because one phase is internally complete.

## Safety / Non-Goals

Do not change during this migration:

- Golden/runtime template bytes;
- PRD 01–03 meaning, hierarchy, presentation, or page identities;
- 04 reader-facing Production Assets contract;
- gameplay/project facts;
- Voice requirements or canonical Voice wording/performance;
- current Clockwork state/acceptance/generated delivery;
- root `tests/` organization;
- root `tools/` organization;
- separate PRD Verify and Voice Verify proof surfaces;
- separate semantic root specialists.

Do not create compatibility stub kits, symlinks, generic requirement/parser/schema/manifest/registry frameworks, another export surface, or aesthetic renderer refactors.

## Baseline / Recovery

M0 evidence was produced from:

```text
Local HEAD
fca07b15c322298163005195302a3c5026603175

tree
3010617b10218c628d46e80f8e4e8e42cdeb265a
```

Protected markers remain:

```text
Golden/runtime template
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1

Clockwork delivery
prd.html    dac955a4a482ad9dc2035f0c5714c87ae4de05c5
context.md  003cc0068505339b8406b445601b7350bffa70a5
index.json  c205422dc0d639b5d0bf9081364321c318e23d22
```

If a future session resumes this work:

1. pin current `Local`;
2. read this file + the migration plan + M0 inventory;
3. if `Local` only advanced by this M0 documentation commit, continue to M1;
4. if unrelated implementation changed, reconcile only the affected inventory/map before M1;
5. never assume unpublished candidate blobs/trees survived the prior session.

## Next Step

**M1 — build the complete unified package candidate tree.** Using current `Local` bytes and the locked M0 inventory/path map, construct `kits/prd-creator/` with all categorized domain/runtime/template files in their approved target paths. Preserve bytes for path-only moves, do not retire either old package root yet, do not publish a half-migrated tree, and do not begin unrelated semantic/refactor work. The resulting candidate is input to M2/M3/M4/M5 before one final migration publish.