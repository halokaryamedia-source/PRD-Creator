# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Execute **P1.3 — Voice Revision + DOCX Entry Integrity** from the Production Engineering Remediation Plan.

Make the Voice mechanical chain prove that the current Flow 5 requirements, Flow 6 canonical script, and derived DOCX belong to the same current revision, and that every DOCX entry remains mechanically bound to the correct Voice ID rather than merely containing the right tokens somewhere in the document.

## Current Status

`BUILD_IT_PARITY_P1_2_COMPLETE_P1_3_VOICE_REVISION_DOCX_INTEGRITY_NEXT`

Execution channel: **ChatGPT → GitHub**.  
Working branch: **`Local` only**.

## Governing Evidence

P1 Production Engineering Quality Audit:

`docs/knowledge/reviews/production-engineering-quality-audit.md`

Ordered P1 remediation:

`docs/knowledge/operations/production-engineering-remediation-plan.md`

P0.2 ownership decision:

`docs/knowledge/decisions/technical-ownership-boundary.md`

Top-level parity plan:

`docs/knowledge/operations/buildit-parity-remediation-plan.md`

## Completed P1.1 — PRD Mechanical Revision Integrity

Source commit:

`04f306f8589528ccc8cb03e89333dba174a3d276` — `fix: enforce PRD render revision integrity`

Proof:

```text
Production Verify 31377375929  PASS
Repository Verify 31377377036  PASS
```

Implemented:

- structured render-data collection/item/stable-ID preflight;
- deterministic render-data SHA-256 embedded in `final.html`;
- stale render-data ↔ HTML mismatch rejection;
- exact generated page order/set validation.

P1-F01 and P1-F02 are implemented at the mechanical level claimed.

## Completed P1.2 — PRD Renderer Script/Shell Safety

Source commit:

`802904856b69fd50008999f196cb72d48303e0ba` — `fix: harden PRD renderer script and shell safety`

Implemented:

- glossary JSON uses script-context-safe serialization before insertion into the inherited executable `<script>` block;
- literal `<`, `>`, `&`, U+2028, and U+2029 are escaped in the script payload, so project text such as `</script>` remains data;
- package glossary aliases are preflighted as `list[str]` or an `en`/`id` object whose supplied values are `list[str]`;
- required unique shell surfaces now fail closed when missing or ambiguous;
- description and specification-version metadata replacements are explicit required contracts;
- inherited local-storage namespace tokens must exist before project namespacing;
- renderer contract failures return controlled non-zero CLI failure instead of a traceback for the covered paths;
- `RENDERING.md` now documents the exact script/shell contract.

Focused PRD regressions cover:

- raw `</script>` glossary payload remains script-safe;
- malformed aliases fail in a controlled way;
- missing/ambiguous sidebar navigation marker fails;
- missing description metadata marker fails;
- current happy render + validator still passes;
- all P1.1 regressions remain active.

### P1.2 proof

```text
Repository Verify
run: 31378603894
head: 802904856b69fd50008999f196cb72d48303e0ba
result: PASS

Production Verify
run: 31378603848
head: 802904856b69fd50008999f196cb72d48303e0ba
result: PASS
```

Production Verify sub-gates all passed: locked dependencies, compile, Project Document contracts, Voice Production contracts, and fail-closed aggregate.

P1-F03 and P1-F07 are therefore **implemented** at the static/mechanical contract level claimed. Browser runtime/visual acceptance remains separate evidence.

## P1.3 Boundary

Findings:

- **P1-F04 MAJOR** — Voice Requirements, canonical script, and DOCX revision identity are not mechanically linked strongly enough;
- **P1-F05 MAJOR** — DOCX validation currently proves global token presence rather than binding each Voice ID to its own Type/title/duration/performance block.

Owners:

```text
kits/voice-production-kit/builder/build_docx.py
kits/voice-production-kit/validator/validate.py
kits/voice-production-kit/SCRIPT-PRODUCTION.md / VOICE-VALIDATION.md only where the mechanical revision contract must be documented
tests/test_voice_contracts.py
state/voice-state.yaml format only if a narrow current-revision field is actually required
```

Required P1.3 work:

1. define the smallest deterministic current Voice Requirements revision/fingerprint contract;
2. require the canonical script/build path to identify the exact current requirements revision without making DOCX authoritative;
3. make Flow 7 mechanical validation reject stale requirements/script/DOCX combinations;
4. parse the generated DOCX into the builder's current visible section/entry structure;
5. validate each entry as one bound unit: Type + Voice ID/title + duration + performance;
6. reject swapped/misbound entry content even when all expected tokens still exist globally;
7. add focused regressions for stale requirements and swapped DOCX entry content;
8. preserve the current happy path and existing Voice ID/Type/page-break regressions.

## Explicit Out Of Scope

- semantic `Must communicate` sentence matching;
- pronunciation or performance-quality judgement;
- rendered-page visual approval;
- generated audio verification;
- general Markdown/DOCX parser framework;
- P1.4 empty-section hardening unless directly required by P1.3 evidence;
- output atomicity;
- root skill changes;
- `main` changes.

## Acceptance

P1.3 is complete only when:

```text
current requirements + script + DOCX → mechanical PASS
requirements changed without rebuilding downstream artifacts → FAIL
DOCX entries swapped/misbound while global tokens remain → FAIL
existing Voice ID/Type regressions → PASS
Production Verify → PASS
Repository Verify → PASS
```

Semantic, visual, pronunciation/performance, and audio evidence remain separate.

## Next Step

Implement **P1.3 — Voice Revision + DOCX Entry Integrity** only: add the smallest current-revision contract and per-entry DOCX mechanical binding, add focused regressions, then run both repository gates before proceeding to P1.4.
