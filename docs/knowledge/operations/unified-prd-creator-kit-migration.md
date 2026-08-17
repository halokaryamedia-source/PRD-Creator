# Unified PRD Creator Kit Migration Plan

Updated: 2026-08-17
Status: user-approved architecture improvement; implementation not started
Baseline branch: `Local`
Baseline commit: `9c55aaf36786ca55c26d4158d8d6c938c8b7a795`

## Goal

Replace the historical two-package implementation shape:

```text
kits/
├─ project-document-generator/
└─ voice-production-kit/
```

with one product package whose internal folders explain the current product domains clearly:

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

The purpose is not to merge all responsibilities into one file. The purpose is to make the repository match the current product reality: one PRD-Creator product, one project workspace, one final project HTML, with clear internal domains for requirement recovery, PRD core, Production Assets, Voice, rendering, validation, and templates.

## Product model to preserve

The migration must preserve this authority and production shape:

```text
source + current user instruction + approved decisions
→ approved project model / requirement state
→ PRD core 01–03
→ 04 Production Assets when required
→ Voice requirements when required
→ canonical Voice Production
→ one versioned project HTML
→ acceptance / delivery evidence
```

The package merge must not collapse semantic ownership. Project/PRD judgment and Voice judgment remain distinct domains even though they live in one implementation package.

## Target package structure

```text
kits/prd-creator/
├─ README.md
├─ AGENTS.md
├─ SKILL.md
│
├─ intake/
│  └─ SOURCE-INTAKE.md
│
├─ document/
│  ├─ CONTENT-CONTRACT.md
│  ├─ GLOSSARY.md
│  └─ VALIDATION.md
│
├─ production-assets/
│  └─ CONTRACT.md
│
├─ voice/
│  ├─ EXTRACTION.md
│  ├─ SOUNDMAKER.md
│  ├─ VALIDATION.md
│  ├─ CHANGELOG.md
│  ├─ LICENSE
│  └─ references/
│
├─ renderer/
│  ├─ CONTRACT.md
│  ├─ core.py
│  ├─ pages.py
│  ├─ render.py
│  ├─ delivery.py
│  ├─ production_assets.py
│  └─ production_assets_objective.py
│
├─ validator/
│  ├─ _engine.py
│  ├─ validate.py
│  ├─ validate_handoff.py
│  └─ validate_voice.py
│
└─ template/
   ├─ golden-reference.html
   └─ runtime-template.html
```

### Root-file rule

The unified kit root should remain scan-first. Current active Markdown owners at the root are limited to:

```text
README.md  → package navigation + Requirement Map
AGENTS.md  → file/mechanical routing + context economy
SKILL.md   → end-to-end Flow 2–7 Production Execution router
```

Domain contracts/procedures belong under the category folder that owns them. Do not move domain details back into root merely to preserve old filenames.

## Requirement Map to expose in the new README

The new root `README.md` must make the source/requirement map explicit so a new reader can immediately answer where each kind of requirement lives.

| Requirement / canonical meaning | Project artifact | System owner after migration |
|---|---|---|
| Project/gameplay requirement state | `state/requirement-register.yaml` | `intake/SOURCE-INTAKE.md` + current Flow 2 policy |
| Canonical PRD-core meaning | `work/content.md` | `document/CONTENT-CONTRACT.md` |
| Non-Voice Production Asset requirements | `work/asset-requirements.md` | `production-assets/CONTRACT.md` |
| Voice requirements | `work/voice-requirements.md` | `voice/EXTRACTION.md` |
| Canonical Voice production | `work/voice-production.md` | root `SKILL.md` Flow 6 routing + `voice/SOUNDMAKER.md` craft owner |
| PRD/Voice acceptance and state | `work/*acceptance.md` + `state/*state.yaml` | corresponding validation owner |

Do not create a generic `requirements/` directory merely for naming symmetry. Requirement instances remain project artifacts; system contracts remain in the domain that owns them.

## Exact old → new path map

### Project Document package

| Current path | Target path | Migration rule |
|---|---|---|
| `kits/project-document-generator/README.md` | `kits/prd-creator/README.md` | merge unique package/navigation meaning; do not copy duplicate routing text |
| `kits/project-document-generator/AGENTS.md` | `kits/prd-creator/AGENTS.md` | merge with Voice kit AGENTS; preserve exact implementation ownership |
| `kits/project-document-generator/SKILL.md` | `kits/prd-creator/SKILL.md` | become the unified Flow 2–7 execution router; preserve unique Flow 2–4 procedure |
| `SOURCE-INTAKE.md` | `intake/SOURCE-INTAKE.md` | path move; no semantic rewrite by default |
| `CONTENT-CONTRACT.md` | `document/CONTENT-CONTRACT.md` | path move; preserve exact contract |
| `GLOSSARY.md` | `document/GLOSSARY.md` | path move |
| `VALIDATION.md` | `document/VALIDATION.md` | path move |
| `PRODUCTION-ASSETS.md` | `production-assets/CONTRACT.md` | rename to reflect folder-owned domain contract |
| `RENDERING.md` | `renderer/CONTRACT.md` | rename to reflect renderer contract owner |
| `renderer/*` | `renderer/*` | path-root move; keep implementation filenames unchanged |
| `validator/_engine.py` | `validator/_engine.py` | path-root move |
| `validator/validate.py` | `validator/validate.py` | path-root move; remains PRD validator CLI |
| `validator/validate_handoff.py` | `validator/validate_handoff.py` | path-root move |
| `template/*` | `template/*` | path-root move; Golden bytes must remain exact |

### Voice package

| Current path | Target path | Migration rule |
|---|---|---|
| `kits/voice-production-kit/README.md` | `kits/prd-creator/README.md` | merge only unique Voice navigation/boundaries |
| `kits/voice-production-kit/AGENTS.md` | `kits/prd-creator/AGENTS.md` | merge exact Voice routing into one technical owner |
| `kits/voice-production-kit/SKILL.md` | `kits/prd-creator/SKILL.md` | merge unique Flow 5–7 execution procedure without creating a giant duplicated contract |
| `VOICE-EXTRACTION.md` | `voice/EXTRACTION.md` | path move + shorter filename because folder supplies domain context |
| `SOUNDMAKER.md` | `voice/SOUNDMAKER.md` | path move |
| `VOICE-VALIDATION.md` | `voice/VALIDATION.md` | path move + shorter filename |
| `references/**` | `voice/references/**` | path move; preserve reference content |
| `CHANGELOG.md` | `voice/CHANGELOG.md` | preserve historical record; not a current routing owner |
| `LICENSE` | `voice/LICENSE` | preserve bytes/scope with Voice material |
| `validator/validate.py` | `validator/validate_voice.py` | rename only because unified validator directory already has PRD `validate.py` |

The retired DOCX builder/contract/dependency must remain absent. Do not recreate an empty `builder/` or compatibility stub.

## Root-owner consolidation rules

The three merged root owners require content reconciliation rather than simple file concatenation.

### `README.md`

Own only:

- what PRD-Creator produces;
- top-level package map;
- Requirement Map;
- where detailed domain owners live;
- one clear statement that the human-facing output is the versioned project HTML.

Do not duplicate detailed Flow contracts, validator matrices, Voice writing rules, or Golden rules.

### `AGENTS.md`

Own only:

- unified kit file/mechanical routing;
- semantic vs technical boundary;
- implementation owner map;
- context economy;
- verification routing;
- anti-overdevelopment boundaries.

Project semantic judgment remains in `.agents/skills/project-document-production/`; Voice semantic judgment remains in `.agents/skills/voice-production/`.

### `SKILL.md`

Own one end-to-end Production Execution sequence for Flow 2–7. It should route to the smallest domain owner instead of copying each contract in full.

Unique current procedure that exists only in either legacy kit `SKILL.md` must be retained. Duplicate/superseded prose may be removed only after confirming another named owner already owns the same rule.

Do not create a new `GENERATION.md`, parser framework, manifest, registry, or compatibility layer merely to make the merge easier.

## Migration execution phases

These are implementation phases inside one product migration. They are not permission for per-file commit spam.

### M0 — Baseline + path inventory

Before moving anything:

1. pin `Local` HEAD;
2. record the exact current tree and Golden/runtime blob identity;
3. search the current tree for every active reference to:
   - `kits/project-document-generator`
   - `kits/voice-production-kit`
4. classify each occurrence as:
   - current routing/runtime/CLI/import;
   - current documentation owner;
   - historical evidence only;
5. identify Python path/import assumptions and CI path filters affected by the move;
6. inspect current version-coupling rules before deciding unified kit version metadata.

Historical prose may retain historical package names when it is genuinely evidence about the old architecture. Live paths, relative links, commands, routing tables, and current-owner statements must move to the new paths.

### M1 — Build unified package tree

Create the complete `kits/prd-creator/` candidate tree from current source bytes and the approved mapping.

Rules:

- move before rewriting;
- preserve implementation bytes where a path-only move is sufficient;
- only rename files listed in the approved map;
- do not change Golden/runtime bytes;
- do not change project/workspace artifacts;
- do not create old-path compatibility wrappers.

### M2 — Consolidate root owners

Reconcile the two README/AGENTS/SKILL sets into the three unified root files.

Acceptance for this phase:

- no duplicate current authority;
- no lost unique Flow procedure;
- root remains scan-first;
- detailed contracts stay in domain folders;
- `.agents/skills/` remain separate semantic specialists.

### M3 — Runtime and validator path migration

Update only path/import/CLI references required by the new location.

Key collision handling:

```text
legacy PRD validator/validate.py
→ validator/validate.py

legacy Voice validator/validate.py
→ validator/validate_voice.py
```

Renderer internals keep current filenames during this migration unless a real collision requires otherwise. Do not bundle aesthetic internal renames.

### M4 — Repository routing synchronization

Update current routing in the smallest necessary owners, including as applicable:

```text
AGENTS.md
CONTEXT.md
docs/foundation/*
docs/knowledge/ownership.md
docs/knowledge/work-routing.md
docs/knowledge/skills/*
.agents/skills/project-document-production/SKILL.md
.agents/skills/voice-production/SKILL.md
workspace/README.md
.github/workflows/prd-verify.yml
.github/workflows/voice-verify.yml
tests/* path constants/imports
tools/verify_repository.py
```

Do not relocate `docs/foundation/`, `.agents/skills/`, `tests/`, or `tools/` as part of this migration.

PRD Verify and Voice Verify remain separate proof surfaces. Unifying the package does not justify merging workflows.

### M5 — Retire old package roots

After all current references resolve through the unified package:

```text
kits/project-document-generator/  → must not exist
kits/voice-production-kit/        → must not exist
```

Add narrow repository verification so both old roots are retired boundaries and cannot silently return.

Also enforce the intended unified shape without overconstraining future directories:

- `kits/prd-creator/` must exist;
- required domain folders must exist;
- active root Markdown owners are `README.md`, `AGENTS.md`, and `SKILL.md`;
- do not introduce another top-level production kit without an explicit product decision.

### M6 — Proof + publish

The migration must be reviewed as one coherent product-structure outcome.

Minimum proof:

1. Python compile for moved implementation/tests;
2. current PRD regression suites PASS;
3. current Voice regression suite PASS;
4. Repository Verify PASS;
5. actual Clockwork PRD validator/handoff validator PASS using new paths;
6. actual Clockwork Voice validator PASS using `validator/validate_voice.py`;
7. Golden/runtime template bytes remain identical;
8. current Clockwork generated delivery bytes remain unchanged unless an unavoidable path-only metadata field is proven to be part of the generated output contract;
9. PRD Verify PASS on GitHub;
10. Voice Verify PASS on GitHub;
11. Repository Verify PASS on GitHub.

Only after the full candidate passes should `Local` move to the migration commit. Use non-force fast-forward only.

## Baseline integrity markers

At plan creation, the user-approved migration baseline is:

```text
Local HEAD
9c55aaf36786ca55c26d4158d8d6c938c8b7a795

Golden + runtime template blob
 e1dccd77d7a5335213caea7a09d74ba78b2ae8e1

Clockwork current versioned delivery blobs
prd.html     dac955a4a482ad9dc2035f0c5714c87ae4de05c5
context.md   003cc0068505339b8406b445601b7350bffa70a5
index.json   c205422dc0d639b5d0bf9081364321c318e23d22
```

These markers are evidence baselines, not authority for project meaning. If `Local` changes before migration execution, re-pin and determine whether the change materially affects the map before continuing.

## Explicit non-goals

Do not use this migration to:

- change PRD/Golden layout or bytes;
- change gameplay, project facts, requirement meaning, or Voice wording/performance;
- change 04 reader-facing fields or moment organization;
- reorganize root `tests/`;
- reorganize root `tools/`;
- merge PRD Verify and Voice Verify;
- merge `.agents/skills/project-document-production` and `.agents/skills/voice-production`;
- create generic requirement/parser/schema/manifest/registry systems;
- rename renderer internals for aesthetics;
- revive DOCX or create another export format;
- rewrite historical audits/CHANGELOG merely to erase old names;
- regenerate current project output unless required for deterministic proof.

## Failure / session-recovery protocol

If a chat/session ends during implementation:

1. start from `AGENTS.md → GITHUB_RULES.md → CONTEXT.md → next-action.md`;
2. open this migration plan;
3. pin current `Local` HEAD;
4. determine the last completed M-phase from `next-action.md` and actual current tree;
5. if no migration commit has landed, discard assumptions about temporary candidate blobs/trees and rebuild the candidate from current source;
6. if a migration commit has landed, continue only from the recorded post-migration next step;
7. never infer progress from chat history alone.

Do not publish a knowingly half-migrated tree solely to preserve session progress. The durable plan + current repository state are the recovery mechanism.

## Commit strategy

Preferred implementation delivery:

```text
one coherent migration candidate
→ full relevant local proof
→ review exact changed-file set
→ one categorized migration commit
→ re-pin Local
→ non-force fast-forward
→ relevant CI
→ stop
```

A separate preparatory implementation commit is allowed only if it is independently valid, necessary to make the migration safe, and would remain useful even if the structural migration were abandoned. Do not split commits by moved directory or file type.

## Acceptance criteria

The migration is complete only when all are true:

1. `kits/` exposes one active product package: `kits/prd-creator/`;
2. the unified kit root is immediately understandable and contains only the three active root Markdown owners plus categorized folders;
3. requirement ownership is obvious from the README Requirement Map and has no duplicate system owner;
4. old package roots are absent and guarded as retired paths;
5. all current runtime/import/CLI/routing links resolve through the unified package;
6. PRD core, Production Assets, and Voice semantics remain unchanged;
7. current Clockwork project state and generated delivery are not rewritten by the migration;
8. Golden/runtime bytes remain unchanged;
9. PRD Verify, Voice Verify, and Repository Verify all pass.

## Next execution step

Start with **M0 — Baseline + path inventory**. Produce an exact current-reference inventory and collision/version decision note from the current `Local` snapshot, then prepare the complete atomic migration candidate from that evidence. Do not move files before M0 confirms all live path consumers.