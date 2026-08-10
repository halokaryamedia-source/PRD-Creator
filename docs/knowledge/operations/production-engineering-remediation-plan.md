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

Source head:

`04f306f8589528ccc8cb03e89333dba174a3d276`

Implemented:

- root collection/item/stable-ID preflight before expected-page calculation;
- structured FAIL for malformed collection items;
- deterministic SHA-256 of canonical sorted render-data;
- `final.html` embeds exactly one `render-data-sha256` marker;
- validator requires exact current render fingerprint;
- generated document section list must exactly match current expected pages/order;
- focused stale-artifact, malformed-item, and stale-extra-page regressions.

Proof:

```text
Production Verify 31377375929  PASS
Repository Verify 31377377036  PASS
```

P1-F01 and P1-F02 are implemented at the mechanical contract level claimed. Semantic `content.md` → render-data correctness and browser visual approval remain separate.

## P1.2 — PRD Renderer Script/Shell Safety — ACTIVE NEXT

Findings:

- P1-F03 — glossary script-context escape / alias-shape runtime failure;
- P1-F07 — shell/metadata contract only partially enforced.

Scope:

- safe deterministic glossary serialization for HTML `<script>` context;
- narrow alias shape preflight required by glossary runtime;
- define/check a small stable shell marker set;
- make intended metadata replacement explicit or remove unsupported/dead contract;
- add focused regressions for `</script>` content, malformed aliases, and required shell markers.

Out of scope:

- sanitizer framework;
- full template snapshot tests;
- redesign of the approved shell.

Acceptance:

- glossary content cannot terminate/inject the inherited script block;
- malformed glossary alias shape fails in a controlled way;
- required shell marker absence/ambiguity fails clearly;
- current happy render + validator PASS;
- focused PRD regressions + both repository gates PASS.

## P1.3 — Voice Revision + DOCX Entry Integrity

Findings:

- P1-F04 — Voice Requirements/script/DOCX revision identity is not mechanically linked;
- P1-F05 — DOCX validator checks global presence rather than per-entry binding.

Scope:

- require a current Voice Requirements revision/fingerprint contract in canonical script/state/mechanical validation;
- keep requirements and script as authorities, not DOCX;
- parse generated DOCX into section/entry blocks using current visible builder structure;
- validate Type + Voice ID/title + duration + performance as one bound entry;
- add stale-requirement and swapped-entry regressions.

Out of scope:

- semantic `Must communicate` sentence matching;
- pronunciation/performance judgement;
- rendered-page visual approval;
- audio verification.

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
5. only then advance to P1.5 Module Governance from the top-level BuildIT parity plan.

Do not claim full relevant BuildIT parity merely because P1 source fixes pass CI.
