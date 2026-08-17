# Next Action

## Current Status

`UNIFIED_PRD_CREATOR_KIT_M4_ROUTING_READY`

The user-approved migration from the two historical implementation packages to one categorized `kits/prd-creator/` package remains active.

Durable migration evidence:

```text
operations/unified-prd-creator-kit-migration.md
operations/unified-prd-creator-kit-m0-inventory.md
operations/unified-prd-creator-kit-m1-candidate.md
operations/unified-prd-creator-kit-m2-root-consolidation.md
operations/unified-prd-creator-kit-m3-runtime-proof.md
operations/unified-prd-creator-kit-m4-routing-candidate.md
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
M4 Repository routing synchronization         COMPLETE
M5 Retire both old package roots              NEXT
M6 Full proof + atomic publish                pending
```

M1–M5 remain detached construction phases. Do not publish a half-migrated architecture.

## Current M4 construction candidate

Use only:

```text
candidate commit
1ec47764dae410803f1c899462ec364c2c4aa320

candidate tree
c3b73337679e56c1194c2ecb84726249ef58b539

kits/prd-creator subtree
9b14038c6ac6f9b4d3a568856cdaf1a9b512cb3d
```

An earlier detached M4 candidate `d4a0412f1493ad30bd370b3ef3ffb4fbde41fa4a` is superseded and must not be used.

## M4 result

Live current routing is synchronized to `kits/prd-creator/` across:

```text
root AGENTS / CONTEXT / README
foundation Flow 2–7 policy
knowledge ownership / authority / work-routing / skill navigation / current validation
root Project and Voice semantic specialists
workspace guidance
unified package domain procedures/contracts
PRD and Voice direct-path regression constants
PRD Verify / Voice Verify / Repository Verify path filters
repository verifier final-target invariants
```

Current non-historical DOCX drift found during M0 was removed from current authority/policy. Historical evidence may continue to describe retired DOCX/package artifacts truthfully.

M3's executable result remains unchanged:

```text
NO EXECUTABLE CODE CHANGE REQUIRED
```

Renderer/validator Python blobs in the unified package remain the existing implementation bytes.

Golden/runtime remain:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

Current Clockwork project files/output remain untouched by the M4 compare.

## Why M4 is still not publishable

The detached candidate intentionally still contains:

```text
kits/prd-creator/
kits/project-document-generator/
kits/voice-production-kit/
```

The updated repository verifier already describes the final architecture and treats both old roots as retired. Therefore do not weaken verification or publish M4 merely to make the intermediate state look complete.

M5 owns exactly this remaining structural retirement.

## M5 Scope

Starting from M4 candidate `1ec47764...`:

1. remove the complete `kits/project-document-generator/` tree;
2. remove the complete `kits/voice-production-kit/` tree;
3. confirm `kits/` exposes only `prd-creator/`;
4. inspect for accidental **live current** old-path consumers;
5. preserve historical textual references when they remain truthful;
6. if deleting the roots breaks an actual historical relative Markdown link, repair only that link or convert it to explicit historical path wording;
7. do not add compatibility directories, aliases, symlinks, wrappers, or migration shims;
8. produce one detached final-structure candidate for M6 proof.

### M5 must not change

- renderer/validator behavior;
- Golden/runtime bytes;
- PRD 01–03 semantics/presentation;
- Production Assets reader-facing contract;
- gameplay/project facts;
- Voice requirements or canonical wording/performance;
- current Clockwork project state/output;
- root tests/tools organization;
- separate PRD Verify and Voice Verify workflows;
- separate root semantic specialists.

## M6 reserved proof

Do not claim full migration completion before M6 proves the one-kit candidate with the relevant executable/project gates, including:

```text
Python compile
PRD regression suite
Voice regression suite
Repository Verify
actual Clockwork PRD validator
actual Clockwork handoff validator
actual Clockwork Voice validator
Golden/runtime identity
current Clockwork delivery identity
PRD Verify
Voice Verify
Repository Verify
```

## Recovery

If a session resumes from here:

1. pin current `Local`;
2. read this file + migration plan + M0–M4 notes;
3. do not repeat M0–M4;
4. use detached candidate `1ec47764dae410803f1c899462ec364c2c4aa320` as the M5 input unless current authoritative source materially changed;
5. do not publish it directly;
6. proceed only with M5 retirement.

## Next Step

**M5 — retire the two historical package roots.** Starting from detached M4 candidate `1ec47764dae410803f1c899462ec364c2c4aa320`, remove `kits/project-document-generator/` and `kits/voice-production-kit/` completely, verify that `kits/` contains only `prd-creator/`, and repair only any mechanically broken historical relative Markdown links caused by the deletion. Do not change runtime/product semantics or add compatibility paths. Produce the detached one-kit final-structure candidate for M6 proof; do not publish the migration to `Local` yet.
