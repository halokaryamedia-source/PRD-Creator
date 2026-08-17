# Next Action

## Current Status

`UNIFIED_PRD_CREATOR_KIT_M5_ONE_KIT_READY`

The user-approved migration from the two historical implementation packages to one categorized `kits/prd-creator/` package remains active and is structurally complete in a detached candidate.

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
→ migration plan
→ M0 inventory
→ M1 candidate
→ M2 root consolidation
→ M3 runtime proof
→ M4 routing candidate
→ M5 retirement candidate
→ smallest relevant current owner/source
```

## Active Boundary

### Final target package

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

Project/PRD and Voice remain separate semantic responsibilities inside one implementation package.

### Phase state

```text
M0 Baseline + live path inventory             COMPLETE
M1 Build unified package candidate tree       COMPLETE
M2 Consolidate root README/AGENTS/SKILL       COMPLETE
M3 Runtime + validator path migration         COMPLETE — no code change required
M4 Repository routing synchronization         COMPLETE
M5 Retire both old package roots              COMPLETE
M6 Full proof + atomic publish                NEXT
```

## Current M5 structural candidate

Use only:

```text
candidate commit
0dc7a244f3871de7933e4ac80705919cbc63ea48

candidate tree
43210aa301610419a2687d12338ceeff540415fc

kits tree
24f34a02cc8adb571aae7d3d7a003941727cdb2b

kits/prd-creator subtree
9b14038c6ac6f9b4d3a568856cdaf1a9b512cb3d
```

A deletion-only M5 construction commit `545e641acf7bc1f03c581e479700a35fc7ca0bed` is superseded and must not be used.

## M5 result

The detached candidate now has exactly one production kit:

```text
kits/prd-creator/
```

The following roots are fully absent:

```text
kits/project-document-generator/
kits/voice-production-kit/
```

M4 → M5 changes are limited to:

```text
36 removed files from the two historical kit roots
1 modified file: docs/knowledge/decisions/README.md
```

The decision register modification is a current-memory reconciliation, not a product redesign. It records:

```text
one implementation package
→ kits/prd-creator/

separate semantic domains
→ Project/PRD
→ Voice
```

It also updates current Golden/Flow 4/Production Assets owner paths and clearly marks retired DOCX/package decisions as historical where needed. Historical capture-time paths remain when they are explicitly historical evidence.

## Preserved boundaries

M5 changes no:

- renderer/validator Python behavior;
- Golden/runtime bytes;
- PRD 01–03 semantics or presentation;
- Production Assets reader-facing contract;
- gameplay/project facts;
- Voice requirements or canonical wording/performance;
- current Clockwork source/state/acceptance/generated output;
- root `tests/` or `tools/` organization;
- separate PRD Verify and Voice Verify workflows;
- separate root semantic specialists.

M3 result remains:

```text
NO EXECUTABLE CODE CHANGE REQUIRED
```

Golden/runtime remain:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

Protected Clockwork delivery markers to re-prove in M6:

```text
prd.html    dac955a4a482ad9dc2035f0c5714c87ae4de05c5
context.md  003cc0068505339b8406b445601b7350bffa70a5
index.json  c205422dc0d639b5d0bf9081364321c318e23d22
```

## M6 Scope

M6 is **proof + final atomic publication**, not another architecture phase.

Starting from current `Local` plus detached M5 structural source:

1. build one final migration commit on top of current `Local` so M0–M5 continuity notes remain in history/current tree;
2. apply the complete one-kit architecture atomically;
3. run the cheapest full proof that can falsify the migration claims;
4. verify Golden/runtime and current Clockwork delivery identity;
5. run actual Clockwork PRD, handoff, and Voice validators through the migrated paths;
6. run PRD regression suite, Voice regression suite, and repository verification;
7. publish/update `Local` only as one coherent final migration delivery;
8. confirm PRD Verify, Voice Verify, and Repository Verify on the published HEAD;
9. if a proof gate fails, fix only the first wrong owner and rerun the invalidated proof;
10. finish by recording the migration as complete and setting the next action to STOP unless the user supplies a new requirement/defect.

### Required proof claims

```text
Python compile
PRD regression suite
Voice regression suite
Repository Verify
actual Clockwork PRD validator
actual Clockwork handoff validator
actual Clockwork Voice validator
Golden/runtime identity
current Clockwork prd.html/context.md/index.json identity
PRD Verify
Voice Verify
Repository Verify
```

Do not use static inspection as browser/audio proof; those are not migration claims here.

## Safety / Non-Goals

Do not during M6:

- add compatibility kit stubs/symlinks/wrappers;
- create a generic requirement/parser/schema/manifest/registry layer;
- merge the root semantic specialists;
- merge PRD Verify and Voice Verify;
- change Golden/runtime bytes;
- change gameplay or Voice wording;
- regenerate Clockwork merely because the package path moved unless a real proof step demonstrates an invalidated derived output;
- introduce PDF/DOCX/new export replacement;
- perform unrelated cleanup.

## Recovery

If a session resumes from here:

1. pin current `Local`;
2. read this file + migration plan + M0–M5 notes;
3. do not repeat M0–M5;
4. use detached M5 candidate `0dc7a244f3871de7933e4ac80705919cbc63ea48` as the structural source;
5. perform M6 proof/final publication only.

## Next Step

**M6 — full proof + atomic publish.** Build the final one-kit migration commit on top of current `Local` using detached M5 candidate `0dc7a244f3871de7933e4ac80705919cbc63ea48` as the structural source, prove repository/PRD/Voice/Clockwork integrity through the migrated paths, verify Golden and current Clockwork delivery identities, then publish the coherent migration to `Local` only if the required gates pass. After final CI succeeds, record the migration complete and STOP unless a new explicit user requirement or reproduced defect exists.
