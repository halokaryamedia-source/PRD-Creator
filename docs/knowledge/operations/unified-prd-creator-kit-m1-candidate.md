# Unified PRD Creator Kit — M1 Candidate Tree

Updated: 2026-08-17
Status: M1 complete; detached candidate only; not publishable
Migration plan: `unified-prd-creator-kit-migration.md`
M0 inventory: `unified-prd-creator-kit-m0-inventory.md`
Candidate parent: `d42b404f76c62731212f1dc717799f992fa05a60`
Candidate commit: `abb80eef10208b5aad30101f5539646d4a3988e3`
Candidate tree: `39cdecda62d23c30ccddc5a943aa84c6f9c7a188`

## Purpose

M1 materializes the approved categorized `kits/prd-creator/` layout as a detached Git candidate without changing the `Local` working branch to a half-migrated architecture.

The candidate is construction evidence for M2–M5. It is deliberately not the final migration state.

## Candidate shape

```text
kits/prd-creator/
├─ README.md                 # provisional Project Document copy; M2 must reconcile
├─ AGENTS.md                 # provisional Project Document copy; M2 must reconcile
├─ SKILL.md                  # provisional Project Document copy; M2 must reconcile
├─ intake/
│  └─ SOURCE-INTAKE.md
├─ document/
│  ├─ CONTENT-CONTRACT.md
│  ├─ GLOSSARY.md
│  └─ VALIDATION.md
├─ production-assets/
│  └─ CONTRACT.md
├─ voice/
│  ├─ EXTRACTION.md
│  ├─ SOUNDMAKER.md
│  ├─ VALIDATION.md
│  ├─ CHANGELOG.md
│  ├─ LICENSE
│  └─ references/
├─ renderer/
│  ├─ CONTRACT.md
│  ├─ _engine.py
│  ├─ core.py
│  ├─ delivery.py
│  ├─ pages.py
│  ├─ production_assets.py
│  ├─ production_assets_objective.py
│  └─ render.py
├─ validator/
│  ├─ _engine.py
│  ├─ validate.py
│  ├─ validate_handoff.py
│  └─ validate_voice.py
└─ template/
   ├─ golden-reference.html
   └─ runtime-template.html
```

## Construction result

Comparison against the M0-complete `Local` parent proves:

```text
files added     33
files modified   0
files deleted    0
```

Every M1 target file reuses an existing current-source Git blob directly. No source blob was rewritten to create this package tree.

This means the following category moves are byte-preserving in M1:

- source-intake procedure;
- PRD content/glossary/validation contracts;
- Production Assets contract;
- Voice extraction, SoundMaker, validation, license, changelog, and references;
- renderer contract and all renderer Python implementation;
- PRD validator/handoff validator implementation;
- Voice validator implementation under the collision-safe target filename `validate_voice.py`;
- Golden/runtime templates.

## Critical identity checks

```text
Golden template target blob
kits/prd-creator/template/golden-reference.html
→ e1dccd77d7a5335213caea7a09d74ba78b2ae8e1

Runtime template target blob
kits/prd-creator/template/runtime-template.html
→ e1dccd77d7a5335213caea7a09d74ba78b2ae8e1

PRD validator target blob
kits/prd-creator/validator/validate.py
→ 0badef1291a6aeea3ce285572d8ac5858d49d139

Voice validator target blob
kits/prd-creator/validator/validate_voice.py
→ d44dcf18bed8771fa44e5fc5ead2d7eff9f1a3f6

Production Assets target contract blob
kits/prd-creator/production-assets/CONTRACT.md
→ 33b7fd27570d0d1ea33e9a3e915df72950cf26e5

Renderer target contract blob
kits/prd-creator/renderer/CONTRACT.md
→ 52cf4e07e964194382c5d52d2cb2420428e39cb0
```

## Provisional root-owner rule

M1 does **not** resolve the three root-owner collisions.

For structural completeness only, the detached candidate currently uses the Project Document package blobs as provisional root files:

```text
README.md
→ 2396868cea5fc9d42fcff7e98b0d8de5d46091bd

AGENTS.md
→ 1b4ab70ce035b2bcb93d0dce4f3ef67fee689f12

SKILL.md
→ e52396a143eef500a24acdd366f00a53faa3f508
```

These are **not** approved final unified root owners.

The unique current Voice root sources remain available at the old package until M2:

```text
kits/voice-production-kit/README.md
kits/voice-production-kit/AGENTS.md
kits/voice-production-kit/SKILL.md
```

M2 must reconcile unique Voice routing/procedure into the three unified root files while keeping them scan-first. It must not concatenate both documents wholesale.

## Old roots intentionally retained

The detached M1 candidate still contains:

```text
kits/project-document-generator/
kits/voice-production-kit/
```

This is intentional. M5 owns retirement only after M2 root consolidation, M3 runtime/path work, and M4 routing synchronization are complete.

No compatibility stubs or symlinks are introduced.

## Why the candidate is not publishable

The M1 tree is structurally correct but intentionally incomplete as a current architecture because:

1. root `README.md`, `AGENTS.md`, and `SKILL.md` have not yet been semantically reconciled;
2. moved contract files still contain old sibling/current-owner path prose where M3/M4 must update it;
3. tests still point to the old package roots;
4. CLI examples still point to old package roots;
5. PRD/Voice/Repository workflow path filters still point to old package roots;
6. repository verifier still requires the old package layout;
7. current top-level routing/ownership docs still identify two packages;
8. both old kit roots are still active.

Therefore no branch ref should point to this candidate as the final product state.

## M1 preservation boundary

M1 did not alter:

- Golden/runtime bytes;
- PRD or Production Assets semantics;
- Voice requirements or canonical wording/performance;
- renderer or validator code bytes;
- current Clockwork state, acceptance, or generated delivery;
- root tests/tools organization;
- CI/workflow definitions;
- old package roots.

## Recovery rule

If a session ends before M2:

1. pin current `Local`;
2. read `next-action.md`, migration plan, M0 inventory, and this M1 note;
3. treat `abb80eef10208b5aad30101f5539646d4a3988e3` as **detached construction evidence**, not the working branch;
4. do not fast-forward `Local` to that candidate;
5. construct the M2 candidate from current `Local`, reusing the recorded M1 blob/path map and then replacing only the three provisional root owner blobs with reconciled versions;
6. if old source package blobs changed since M1, re-pin only the affected mappings before proceeding.

## M2 entry contract

M2 may assume the categorized file map itself is valid and byte-preserving. Its job is limited to the three current package-owner collisions:

```text
Project README + Voice README
→ kits/prd-creator/README.md

Project AGENTS + Voice AGENTS
→ kits/prd-creator/AGENTS.md

Project SKILL + Voice SKILL
→ kits/prd-creator/SKILL.md
```

The unified root metadata remains locked to:

```text
name: prd-creator
version: 1.14.0
```

M2 should keep detailed contracts in their category folders and remove duplicate/superseded root prose only when another named current owner already preserves that rule.
