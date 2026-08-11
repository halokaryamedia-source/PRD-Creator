# Next Action

Updated: 2026-08-11

## Current Status

`PRD_SEMANTIC_QUALITY_CONTRACT_REVISED_NEXT_DESKTOP_REPRESENTATIVE_PROOF`

Working branch: **`Local` only**.

## Why PRD Flow 2–4 was reopened

Direct review of the representative AFTERSHOCK final sample found that the previous semantic threshold was too permissive even though renderer/mechanical/browser checks passed.

Concrete failures included:

- `score is not displayed/exported` was incorrectly interpreted as `No Objective Score`;
- Gameplay Flow became task summaries instead of the chronological player journey/context needed by the team;
- Level Design, Developer, and Global Development lost material production detail;
- prose was too compressed/database-like and insufficiently humanized;
- semantic acceptance did not trace material source/requirement meaning deeply enough before declaring PASS.

The previous AFTERSHOCK run remains diagnostic/mechanical evidence only. It is **not** current semantic-quality proof.

## Completed semantic contract revision

### Flow 2

- do not broaden negative statements beyond their actual scope;
- `do not display score`, `do not export score`, and `No Objective Score` are distinct meanings;
- every gameplay package resolves its Scoring / Result model as Objective Score or explicit No Objective Score;
- internal score/result, player-facing display, and telemetry/export remain separate when authority distinguishes them;
- a source/file labelled `FINAL` does not silently override higher-authority current instruction or approved decisions.

### Flow 3

- target changed from minimum-looking output to **minimum complete production detail**;
- Golden is now an explicit **functional quality floor**, not just hierarchy/template;
- Gameplay Flow must be chronological player-story production narrative;
- Level Design must carry complete material build-relevant meaning;
- Developer must carry complete material runtime/state/scoring-or-result/data/interruption/reset/handoff meaning;
- Global Development must preserve important shared ownership;
- every package must visibly state its Scoring / Result contract;
- one bounded PRD Humanize pass is required before projection.

### Flow 4

- semantic acceptance now performs bounded material source/requirement → PRD coverage review;
- if Level Design or Developer must reopen original source for a material rule that belongs in the PRD, that is Major;
- Golden quality is judged by production function, not word/row count;
- default visual proof is **desktop-only**;
- representative browser smoke is limited to Overview + one Gameplay Flow + one Level Design + one dense Developer page unless a specific defect requires more.

## Deliberately not added

- no word-count validator;
- no minimum row/note count;
- no generic schema/coverage matrix;
- no semantic similarity engine;
- no additional hash/checksum chain;
- no mobile QA by default;
- no Voice changes yet.

## Proof economy

Do not rerun unchanged checks merely because documentation changed.

Use:

```text
semantic contract change
→ repository/CI gate where automatically applicable
→ one representative real-project authoring/review proof
→ targeted desktop visual smoke
→ stop
```

The existing `content.md → render-data.json` SHA remains unchanged in this semantic slice. Its later simplification is still a separate candidate because it does not prove semantic equivalence.

## Next Step

Run one **new representative PRD Flow 2–4 production proof** using the revised semantic quality floor.

The proof must specifically verify:

1. correct Objective Score vs explicit No Objective Score interpretation, including display/export distinctions;
2. Gameplay Flow reads as a complete chronological player journey rather than a task summary;
3. Level Design / Developer / Global Development preserve all material production meaning needed by their roles;
4. prose is humanized and readable without changing exact technical facts;
5. the Golden Sample is matched as a functional quality floor without copying project-specific facts.

Use **desktop-only targeted visual sanity**. Do not run mobile QA or unrelated Voice validation unless the test exposes a concrete reason.
