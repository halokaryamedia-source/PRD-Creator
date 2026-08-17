# Unified PRD Creator Kit — M5 Retirement Candidate

Updated: 2026-08-17
Status: M5 complete; detached one-kit candidate ready for M6 proof
Migration plan: `unified-prd-creator-kit-migration.md`
M0 inventory: `unified-prd-creator-kit-m0-inventory.md`
M1 candidate: `unified-prd-creator-kit-m1-candidate.md`
M2 root consolidation: `unified-prd-creator-kit-m2-root-consolidation.md`
M3 runtime proof: `unified-prd-creator-kit-m3-runtime-proof.md`
M4 routing candidate: `unified-prd-creator-kit-m4-routing-candidate.md`
Current Local parent for checkpoint continuity: `867c8e971f27cecbd69a347ea3d6df70662172dd`
M4 detached input: `1ec47764dae410803f1c899462ec364c2c4aa320`
M5 detached candidate: `0dc7a244f3871de7933e4ac80705919cbc63ea48`
M5 candidate tree: `43210aa301610419a2687d12338ceeff540415fc`
Final `kits/` tree: `24f34a02cc8adb571aae7d3d7a003941727cdb2b`
Unified package subtree: `9b14038c6ac6f9b4d3a568856cdaf1a9b512cb3d`

## Purpose

M5 performs the final structural retirement step before full proof:

```text
remove kits/project-document-generator/
remove kits/voice-production-kit/
keep only kits/prd-creator/
```

It also reconciles one current-facing decision-memory drift discovered only after the old roots were removed. No runtime/product behavior is changed.

## Final package shape

The detached M5 candidate exposes exactly one production kit:

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

`kits/project-document-generator/` and `kits/voice-production-kit/` are absent.

## M4 → M5 diff boundary

The final atomic M5 commit changes only:

```text
36 removed files
→ complete contents of kits/project-document-generator/
→ complete contents of kits/voice-production-kit/

1 modified file
→ docs/knowledge/decisions/README.md
```

No file under `workspace/active/`, renderer/validator implementation, tests, workflows, root semantic skills, or Golden/runtime templates is modified during M5.

## Decision-memory reconciliation

Deleting the old roots exposed a current-facing drift in `docs/knowledge/decisions/README.md` that M4 had not classified separately:

- the `Current-use guard` still pointed to the old Production Assets owner;
- the current Golden path still named the old Project Document kit;
- the current Flow 4 replacement still named the old validation owner;
- the old separate top-level Project Document / Voice package decision had no supersession status;
- several DOCX decisions still used `Current replacement` wording that could imply DOCX remained current.

M5 fixes only that current interpretation layer while preserving capture-time history.

The decision register now records the approved architecture explicitly:

```text
kits/prd-creator/
= one current implementation package

Project/PRD
≠ Voice semantic ownership
```

The package is unified, but the semantic domains and root specialists remain separate.

Historical DOCX and former-kit paths remain where they are clearly labeled as historical/capture-time evidence. No history was rewritten merely to erase old names.

## Historical link audit

M5 specifically inspected the historical/current-memory surfaces most likely to mention the retired roots, including:

```text
docs/knowledge/decisions/README.md
docs/knowledge/reviews/README.md
docs/knowledge/reviews/archived-retirement-audit.md
docs/knowledge/reviews/production-engineering-quality-audit.md
docs/knowledge/reviews/repository-quality-audit-2026-08-14.md
docs/knowledge/reviews/technical-ownership-refinement-audit.md
docs/knowledge/reviews/operating-parity-acceptance.md
docs/knowledge/reviews/system-integration-proof.md
```

Observed retired-root mentions in historical review bodies are capture-time text/code-path evidence, not current routing. No compatibility directory is kept for them.

No mechanically broken old-kit Markdown link was identified in this targeted retirement audit. Full repository relative-link verification remains part of M6 `Repository Verify`; M5 does not claim that final executable gate before the final candidate is published/proven.

## Runtime and Golden preservation

M3 remains authoritative for relocation mechanics:

```text
NO EXECUTABLE CODE CHANGE REQUIRED
```

M5 does not modify any unified renderer/validator Python blob.

Golden/runtime templates remain exact blob:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

Unified package subtree remains the M4 subtree:

```text
9b14038c6ac6f9b4d3a568856cdaf1a9b512cb3d
```

## Project preservation

M5 does not modify current Clockwork project source/state/acceptance/output.

Protected current delivery markers remain expected for M6 verification:

```text
prd.html    dac955a4a482ad9dc2035f0c5714c87ae4de05c5
context.md  003cc0068505339b8406b445601b7350bffa70a5
index.json  c205422dc0d639b5d0bf9081364321c318e23d22
```

## Superseded construction commit

A deletion-only detached commit was created during M5 inspection:

```text
545e641acf7bc1f03c581e479700a35fc7ca0bed
```

It is superseded because the current-facing decision register drift was then reconciled. It never became `Local`.

Use only:

```text
0dc7a244f3871de7933e4ac80705919cbc63ea48
```

as the M5 input for M6.

## Proof boundary

M5 proves the intended final **repository structure** and closes known current-routing drift discovered during retirement.

It does not yet claim:

- full Python compile;
- PRD regression suite PASS;
- Voice regression suite PASS;
- Repository Verify PASS on the one-kit architecture;
- actual Clockwork PRD validator PASS through the migrated paths;
- actual Clockwork handoff validator PASS through the migrated paths;
- actual Clockwork Voice validator PASS through the migrated paths;
- final PRD Verify / Voice Verify / Repository Verify CI PASS.

Those are M6.

## Recovery rule

If a session ends before M6:

1. pin current `Local`;
2. read `next-action.md`, migration plan, and M0–M5 notes;
3. do not repeat M0–M5;
4. use detached M5 candidate `0dc7a244f3871de7933e4ac80705919cbc63ea48` as the final structural source;
5. rebuild the final publish commit from current `Local` so continuity/checkpoint docs are retained while the detached candidate tree changes are applied atomically;
6. do not publish if any M6 proof gate fails.

## M6 entry contract

M6 owns full proof and final atomic publication only.

Build one final migration commit on top of the current `Local` continuity HEAD that applies the M5 one-kit architecture plus final continuity status. Then prove the relevant repository/product gates. If a concrete regression is found, fix the first wrong owner and rerun only the invalidated proof before completion.

Do not add new architecture, compatibility paths, export surfaces, or cleanup beyond defects reproduced by M6 proof.