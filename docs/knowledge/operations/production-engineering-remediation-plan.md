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

Findings:

- P1-F01 — stale/current render revision was not mechanically linked;
- P1-F02 — malformed render-data could escape structured validator failure.

Source:

`04f306f8589528ccc8cb03e89333dba174a3d276` — `fix: enforce PRD render revision integrity`

Implemented:

- fail-closed root collection/item/stable-ID preflight;
- deterministic render-data SHA-256 embedded into generated HTML;
- validator rejection when current render-data and HTML revision differ;
- exact generated page order/set validation;
- focused stale-artifact/malformed-shape regressions.

Proof:

```text
Production Verify 31377375929  PASS
Repository Verify 31377377036  PASS
```

P1-F01 and P1-F02 are implemented at the mechanical level claimed.

## P1.2 — PRD Renderer Script/Shell Safety — COMPLETE

Findings:

- P1-F03 — glossary script-context escape / alias-shape runtime failure;
- P1-F07 — shell/metadata contract only partially enforced.

Source:

`802904856b69fd50008999f196cb72d48303e0ba` — `fix: harden PRD renderer script and shell safety`

Implemented:

- script-context-safe glossary JSON serialization;
- alias preflight for `list[str]` and supported `en`/`id` list objects;
- exact required shell-marker uniqueness checks;
- explicit description/specification-version metadata replacement contracts;
- required local-storage namespace token checks;
- controlled renderer CLI failure for covered contract errors;
- focused `</script>`, malformed-alias, missing/ambiguous-shell, metadata, and happy-path regressions.

Proof:

```text
Repository Verify 31378603894  PASS
Production Verify 31378603848  PASS
```

P1-F03 and P1-F07 are implemented at the static/mechanical level claimed. Browser runtime/visual approval remains separate evidence.

## P1.3 — Voice Revision + DOCX Entry Integrity — ACTIVE NEXT

Findings:

- P1-F04 — Voice Requirements/script/DOCX revision identity is not mechanically linked;
- P1-F05 — DOCX validator checks global presence rather than per-entry binding.

Scope:

- require a current Voice Requirements revision/fingerprint contract in canonical script/build/validation;
- keep requirements and canonical script as authorities, never DOCX;
- reject stale requirements/script/DOCX combinations;
- parse generated DOCX into the current visible section/entry structure;
- validate Type + Voice ID/title + duration + performance as one bound entry;
- add stale-requirement and swapped-entry regressions.

Out of scope:

- semantic `Must communicate` sentence matching;
- pronunciation/performance judgement;
- rendered-page visual approval;
- audio verification;
- general Markdown/DOCX parser framework.

Acceptance:

- current requirements + script + DOCX PASS mechanically;
- changed requirements without downstream rebuild FAIL;
- swapped/misbound DOCX entries FAIL even when global tokens remain;
- existing Voice regressions PASS;
- both repository gates PASS.

## P1.4 — Voice Parser / Failure-State Hardening

Finding:

- P1-F06 — empty section can raise uncaught `IndexError`.

Scope:

- choose explicit Flow 6 empty-section rule;
- reject or safely omit invalid zero-entry script sections before build;
- return controlled builder failure;
- inspect only directly adjacent builder/validator exception paths exposed by the same regression.

Do not use this slice to create a general Markdown parser framework.

## P1.5 — Contract Test Discovery

Finding:

- P1-F08 — Production Verify names current test modules explicitly.

Scope:

- make canonical `tests/test_*.py` modules execute by default;
- retain clear failure output;
- avoid duplicate test execution;
- keep the suite focused on high-risk contracts rather than coverage targets.

## P1.6 — Derived Output Atomicity — CONDITIONAL

Finding:

- P1-F09 — final HTML/DOCX writes are direct, not atomic.

Run only if, after P1.1–P1.5, a small same-directory temp-write + replace solution is clearly cross-platform and does not add disproportionate complexity.

`No change required` is valid if the implementation cost/risk exceeds the current failure evidence.

---

## Re-audit Gate

After all required P1 slices:

1. rerun full `Production Verify`;
2. rerun `Repository Verify`;
3. re-read P1 audit findings against current source;
4. mark each finding `implemented`, `no change required`, or `remaining` in review graph/validation report;
5. only then advance to top-level P1.5 Module Governance.

Do not claim full relevant BuildIT parity merely because P1 source fixes pass CI.
