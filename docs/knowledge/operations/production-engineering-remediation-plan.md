# Production Engineering Remediation Plan

Updated: 2026-08-10
Status: approved ordered execution direction after P1 audit

Governing evidence:

`../reviews/production-engineering-quality-audit.md`

This plan converts the P1 audit into bounded source slices. `../next-action.md` owns the one active slice.

## Principle

Fix trust boundaries in dependency order. Do not combine unrelated findings merely because they are all Python.

Every source slice must:

1. fix the smallest first wrong owner;
2. add/adjust focused regression only for the changed contract;
3. keep semantic/visual/audio proof boundaries truthful;
4. pass `Repository Verify` and `Production Verify` when production source/tests are affected;
5. avoid generic schema/parser/framework revival.

---

## P1.1 — PRD Mechanical Revision Integrity — COMPLETE

Findings P1-F01/F02.

Source: `04f306f8589528ccc8cb03e89333dba174a3d276`

Implemented fail-closed projection preflight, current render-data SHA-256 linkage to generated HTML, exact generated page order/set checks, and focused stale/malformed regressions.

```text
Production Verify 31377375929  PASS
Repository Verify 31377377036  PASS
```

## P1.2 — PRD Renderer Script/Shell Safety — COMPLETE

Findings P1-F03/F07.

Source: `802904856b69fd50008999f196cb72d48303e0ba`

Implemented script-context-safe glossary serialization, alias-shape preflight, exact required shell-marker/metadata contracts, controlled covered renderer failures, and focused safety regressions.

```text
Repository Verify 31378603894  PASS
Production Verify 31378603848  PASS
```

Browser runtime/visual approval remains separate evidence.

## P1.3 — Voice Revision + DOCX Entry Integrity — COMPLETE

Findings:

- P1-F04 — Voice Requirements/script/DOCX revision identity was not mechanically linked;
- P1-F05 — DOCX validator checked global presence rather than per-entry binding.

Source:

`dcb9bdf54a5749d04be2362b9d33918ab332f4f2` — `fix: bind voice revisions and DOCX entries`

Implemented:

- canonical script declares `Source Voice Requirements SHA-256` for the current normalized requirements text;
- builder requires the current requirements file and rejects stale declared revision before writing DOCX;
- builder computes current script SHA-256 and stores requirements + script fingerprints in the DOCX core identifier;
- Flow 7 rejects stale requirements/script/DOCX combinations;
- DOCX parser validates exact section order and Voice-entry order from the builder's visible structure;
- every entry is compared as section + Type + Voice ID/title + duration + performance;
- focused stale-requirement, stale-script, and swapped-performance regressions;
- existing Voice ID/Type and section page-break regressions preserved.

Proof:

```text
Repository Verify 31379718341  PASS
Production Verify 31379718339  PASS
```

P1-F04 and P1-F05 are implemented at the mechanical revision/entry-binding level claimed. Semantic, visual, pronunciation/performance, and audio evidence remain separate.

## P1.4 — Voice Parser / Failure-State Hardening — ACTIVE NEXT

Finding:

- P1-F06 — empty section can reach builder logic that assumes at least one entry and raise an uncontrolled `IndexError` path.

Scope:

- establish one explicit Flow 6 zero-entry `##` section rule from current product semantics;
- reject or intentionally omit invalid zero-entry sections before presentation helpers assume entries exist;
- return controlled non-zero builder failure instead of traceback/`IndexError`;
- inspect only directly adjacent parser/builder exception paths exposed by the same focused regression;
- add focused empty-section/failure-state regression;
- preserve P1.3 revision/entry-binding contracts.

Out of scope:

- general Markdown parser framework;
- Voice format redesign;
- semantic `Must communicate` automation;
- DOCX visual/audio proof;
- P1.5 test discovery;
- P1.6 output atomicity.

Acceptance:

- zero-entry section has explicit controlled behavior;
- covered adjacent malformed parser state does not traceback;
- current Voice happy path and P1.3 regressions PASS;
- both repository gates PASS.

## P1.5 — Contract Test Discovery

Finding P1-F08.

Scope:

- make canonical `tests/test_*.py` modules execute by default;
- retain clear failure output;
- avoid duplicate test execution;
- keep the suite focused on high-risk contracts rather than coverage targets.

## P1.6 — Derived Output Atomicity — CONDITIONAL

Finding P1-F09.

Run only if, after P1.1–P1.5, a small same-directory temp-write + replace solution is clearly cross-platform and does not add disproportionate complexity.

`No change required` is valid if implementation cost/risk exceeds current failure evidence.

---

## Re-audit Gate

After all required P1 slices:

1. rerun full `Production Verify`;
2. rerun `Repository Verify`;
3. re-read P1 audit findings against current source;
4. mark each finding `implemented`, `no change required`, or `remaining` in review graph/validation report;
5. only then advance to top-level P1.5 Module Governance.

Do not claim full relevant BuildIT parity merely because P1 source fixes pass CI.
