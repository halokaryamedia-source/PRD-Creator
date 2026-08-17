# Unified PRD Creator Kit — M2 Root Consolidation

Updated: 2026-08-17
Status: M2 complete; detached candidate only; not publishable
Migration plan: `unified-prd-creator-kit-migration.md`
M0 inventory: `unified-prd-creator-kit-m0-inventory.md`
M1 candidate note: `unified-prd-creator-kit-m1-candidate.md`
Current working parent: `db9cefef71f93905e22f5d42c11b9dacb8fd2277`
M2 candidate commit: `e1523e22f90a666ec14bf4f0d260bb9238305537`
M2 candidate tree: `00687140e2d47596a38bdac666a84d8218642ab2`
Unified package subtree: `e56566a73ea9d2729f671411abae06d467206337`

## Purpose

M2 resolves the only semantic/root-file collisions left by M1:

```text
Project README + Voice README
→ kits/prd-creator/README.md

Project AGENTS + Voice AGENTS
→ kits/prd-creator/AGENTS.md

Project SKILL + Voice SKILL
→ kits/prd-creator/SKILL.md
```

The result is one scan-first product root without flattening Project/PRD, Production Assets, and Voice into one semantic domain.

## Root owner identities

```text
README.md
→ 42f1f031f58f2be0e2a8e4a85f1818025e29cc1d

AGENTS.md
→ 96caa183c9d5e0f4ebb7f3ee0cb88f4700972681

SKILL.md
→ 70cd976fd27a2561c52f1b44f1ea6e4a6e094e2a
```

Unified `SKILL.md` metadata is locked to:

```yaml
name: prd-creator
version: 1.14.0
```

The historical Voice Kit version `1.11.2` is not promoted into a second current package version; it remains historical provenance in `voice/CHANGELOG.md`.

## Consolidation result

### README.md — package map + Requirement Map

The new README answers only the navigation questions a new reader needs first:

- what PRD Creator produces;
- the end-to-end product shape;
- what each category folder owns;
- where Project/gameplay requirements, PRD meaning, Production Asset requirements, Voice requirements, Voice Production, and acceptance/state live;
- which artifacts are canonical vs derived;
- that `prd.html` is the single normal human-facing project document;
- that DOCX remains retired.

It does not duplicate detailed Flow procedures, validation matrices, Golden rules, or Voice writing rules.

### AGENTS.md — unified technical/file routing

The new AGENTS owner preserves the semantic separation explicitly:

```text
Project/PRD/non-Voice 04 semantic judgment
→ .agents/skills/project-document-production/

Voice semantic judgment
→ .agents/skills/voice-production/

correct semantics + executable defect
→ exact implementation owner inside kits/prd-creator/
```

It also consolidates implementation ownership for renderer, templates, PRD validator, handoff validator, and Voice validator under one package while preserving separate PRD Verify / Voice Verify proof surfaces.

### SKILL.md — Flow 2–7 execution router

The new root skill preserves the unique active responsibilities from both legacy kit skills while routing exact detail to categorized owners:

```text
Flow 2 → intake/SOURCE-INTAKE.md
Flow 3 → document/CONTENT-CONTRACT.md
Flow 4 → document/VALIDATION.md
04     → production-assets/CONTRACT.md
Flow 5 → voice/EXTRACTION.md
Flow 6 → docs/foundation/06-elevenlabs-script-production.md + voice/SOUNDMAKER.md
Flow 7 → voice/VALIDATION.md
```

It retains the important end-to-end behavior from the former Project skill:

- complete project model rather than gap listing;
- Completion / Proposal / Blocked boundary;
- Simple Chat Preview approval boundary;
- protected PRD core 01–03;
- Content Purity + Humanize boundary;
- same-model Production Asset recovery;
- bounded revision fast path;
- artifact lifecycle and stop discipline.

It also retains the important end-to-end behavior from the former Voice skill:

- Voice downstream from accepted project/PRD meaning;
- Flow 5 communication requirement boundary;
- canonical Voice Production ownership;
- Preparation vs Generation Mode;
- shared 04 AUDIO presentation rather than second Voice HTML;
- Communication Conservation / readiness proof boundary;
- audio evidence only from actual audio;
- retired DOCX boundary.

Exact field-level contracts and craft rules remain in their named domain owners instead of being copied wholesale into root.

## Structural preservation proof

M1 package subtree:

`b25d953c28065c067359262a044755a5ed766705`

M2 package subtree:

`e56566a73ea9d2729f671411abae06d467206337`

All categorized subtrees are unchanged between M1 and M2:

```text
document          ce80bde4502403c85444f1069bc991409642e6ce
intake            27e50e7b43ca1ff275c32e5c1430f972780d542b
production-assets c2224da60ef04b36405314d2d6982dcb950798e7
renderer          16a2dd8b1f80d897e924b2bb64535d8bcb9d321b
template          0af49666cca3b5f8adb35b312060e70b03d54409
validator         75d47d4d40a6382d1924373a7717e2713cf6b78a
voice             83344f312d42a22c4aa5c4caf31e8e7e9cc669b3
```

Therefore M2 changes only the three intended root owner blobs. Golden/runtime, renderer, validator, domain contracts, Voice references, and license/changelog bytes are untouched.

## Candidate still not publishable

M2 is a construction candidate, not current architecture. It still cannot replace `Local` because:

1. moved domain Markdown still contains old relative/current-owner path prose that must be reconciled where live;
2. current CLI examples outside the candidate still point to the old package roots;
3. tests still use old package-root path constants;
4. PRD/Voice/Repository workflow filters and compile targets still use old roots;
5. `tools/verify_repository.py` still requires and scans the two old kit roots;
6. current root/foundation/knowledge/workspace routing still identifies the historical packages;
7. both old package roots remain intentionally active until M5.

Do not fast-forward `Local` to the M2 candidate.

## Preservation boundary

M2 does not change:

- Golden/runtime bytes;
- PRD 01–03 meaning/hierarchy/presentation;
- Production Assets reader-facing contract;
- gameplay/project facts;
- Voice requirements or canonical wording/performance;
- current Clockwork state/acceptance/generated delivery;
- renderer/validator Python bytes;
- root tests/tools organization;
- workflow definitions;
- the two separate root semantic specialists.

## Recovery rule

If a session ends before M3:

1. pin current `Local`;
2. read `next-action.md`, migration plan, M0, M1, and this M2 note;
3. treat `e1523e22f90a666ec14bf4f0d260bb9238305537` as detached construction evidence only;
4. do not publish it directly;
5. reuse unified package subtree `e56566a73ea9d2729f671411abae06d467206337` as the M2 construction baseline if current source owners have not materially changed;
6. if current source changed, reconcile only the affected source before continuing.

## M3 entry contract

M3 owns **runtime/validator path migration and executable viability only**.

Start from the M2 unified package candidate and verify the moved Python topology under `kits/prd-creator/`. Update only executable path/import assumptions actually required by the new package layout. Preserve bytes when sibling-relative behavior already works.

Do not begin repository-wide routing synchronization, tests/workflow path migration, or old-root retirement until the executable package itself is proven viable.