# Next Action

## Current Status

`UNIFIED_PRD_CREATOR_KIT_MIGRATION_COMPLETE`

The user-approved migration from two historical implementation packages to one categorized `kits/prd-creator/` package is complete.

Durable migration evidence:

```text
operations/unified-prd-creator-kit-migration.md
operations/unified-prd-creator-kit-m0-inventory.md
operations/unified-prd-creator-kit-m1-candidate.md
operations/unified-prd-creator-kit-m2-root-consolidation.md
operations/unified-prd-creator-kit-m3-runtime-proof.md
operations/unified-prd-creator-kit-m4-routing-candidate.md
operations/unified-prd-creator-kit-m5-retirement-candidate.md
```

Repository continuity:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules
→ CONTEXT.md
→ next-action.md
→ development-brief for non-trivial Developing
→ smallest relevant current owner/source
```

The migration operation notes are now historical implementation evidence. Do not replay M0–M6 unless a new reproduced defect specifically requires forensic comparison.

## Active Boundary

### Current production package

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

The old package roots are retired:

```text
kits/project-document-generator/
kits/voice-production-kit/
```

Do not restore them as compatibility paths, aliases, wrappers, or duplicate owners.

## Ownership model

One implementation package does **not** mean one giant semantic owner.

```text
Project / PRD / non-Voice 04 semantics
→ .agents/skills/project-document-production
→ categorized Project/PRD owners under kits/prd-creator/

Voice semantics
→ .agents/skills/voice-production
→ categorized Voice owners under kits/prd-creator/voice/

shared implementation mechanics
→ kits/prd-creator/renderer/
→ kits/prd-creator/validator/
→ kits/prd-creator/template/

repository engineering
→ tests/
→ tools/
→ .github/workflows/
```

Root `README.md`, `AGENTS.md`, and `SKILL.md` inside the kit remain scan-first navigation/routing owners rather than duplicate detailed contracts.

## Requirement map

```text
project/gameplay requirement state
→ state/requirement-register.yaml
→ intake/SOURCE-INTAKE.md

canonical PRD core 01–03
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
→ voice/SOUNDMAKER.md + Flow 6 policy
```

Do not create a generic `requirements/` framework merely for naming symmetry.

## Protected boundaries after migration

The migration intentionally changes package/routing structure only. It does not authorize changes to:

- product/gameplay meaning;
- PRD 01–03 semantic or visible Golden contract;
- Production Assets reader-facing resource contract;
- Voice requirements or canonical wording/performance;
- Golden/runtime bytes;
- current Clockwork project source/state/acceptance/output;
- root `tests/` / `tools/` organization;
- separate PRD Verify and Voice Verify proof surfaces;
- separate root semantic specialists.

The former DOCX delivery path remains retired. Do not replace it with PDF, another export framework, or a second Voice HTML without a new explicit product requirement.

## Migration result

```text
M0 Baseline + live path inventory             COMPLETE
M1 Build unified package candidate tree       COMPLETE
M2 Consolidate root README/AGENTS/SKILL       COMPLETE
M3 Runtime + validator path migration         COMPLETE — no executable code change required
M4 Repository routing synchronization         COMPLETE
M5 Retire both old package roots              COMPLETE
M6 Full proof + atomic publish                COMPLETE
```

M3 established that renderer/validator relocation does not require Python compatibility code because current implementation resolves sibling/local topology.

Golden/runtime identity remains the approved blob:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

Current Clockwork delivery remains protected at:

```text
prd.html    dac955a4a482ad9dc2035f0c5714c87ae4de05c5
context.md  003cc0068505339b8406b445601b7350bffa70a5
index.json  c205422dc0d639b5d0bf9081364321c318e23d22
```

## Continuation rule

There is no automatic follow-on architecture work.

Historical P1.5, conditional backlog items, old audits, BuildIT-parity findings, and migration-phase TODOs are not active merely because they still exist as evidence.

A future session should start from the current repository owners above and only promote new work when:

- the user explicitly requests a new requirement/change; or
- a current defect is reproduced and has a clear first wrong owner.

## Next Step

**STOP.** Resume only from a new explicit user-approved requirement or a reproduced current defect. Do not automatically continue into historical P1.5/backlog work, post-migration cleanup, package renaming, test-folder reorganization, export replacement, or additional architecture polishing.