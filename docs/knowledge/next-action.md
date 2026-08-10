# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Execute **P1.4 — Voice Parser / Failure-State Hardening** from the Production Engineering Remediation Plan.

Close the remaining known Voice parser/build failure-state gap without creating a generic Markdown parser: a `##` Voice section with zero entries can currently reach builder logic that assumes at least one entry.

## Current Status

`BUILD_IT_PARITY_P1_3_COMPLETE_P1_4_VOICE_PARSER_FAILURE_STATE_NEXT`

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

Source:

`04f306f8589528ccc8cb03e89333dba174a3d276`

```text
Production Verify 31377375929  PASS
Repository Verify 31377377036  PASS
```

P1-F01 and P1-F02 are implemented at the mechanical boundary claimed.

## Completed P1.2 — PRD Renderer Script/Shell Safety

Source:

`802904856b69fd50008999f196cb72d48303e0ba`

```text
Production Verify 31378603848  PASS
Repository Verify 31378603894  PASS
```

P1-F03 and P1-F07 are implemented at the static/mechanical boundary claimed. Browser runtime/visual approval remains separate evidence.

## Completed P1.3 — Voice Revision + DOCX Entry Integrity

Source:

`dcb9bdf54a5749d04be2362b9d33918ab332f4f2` — `fix: bind voice revisions and DOCX entries`

Implemented revision chain:

```text
current work/voice-requirements.md
→ normalized-text SHA-256
→ canonical work/voice-production.md declares Source Voice Requirements SHA-256
→ builder requires exact current hash + Flow 5 ID/Type parity
→ builder computes current script SHA-256
→ derived DOCX core identifier stores requirements + script fingerprints
→ Flow 7 validator requires current requirements == script declaration == DOCX identifier
```

The state YAML remains lifecycle/readiness ownership; hashes are not duplicated into another revision registry.

DOCX validation now parses the builder's visible structure and validates every entry as one bound unit:

```text
section
→ Type
→ Voice ID + title
→ Estimated Duration
→ performance paragraph
```

It also requires section order and Voice-entry order to match the canonical script.

Focused regressions now prove:

- current requirements + script + DOCX → PASS;
- builder rejects a stale requirements hash before writing DOCX;
- requirements changed after build → Flow 7 FAIL;
- script changed after build → Flow 7 FAIL;
- swapping two DOCX performance blocks fails even though all global Voice ID/content tokens remain present;
- existing ID/Type parity and section page-break regressions remain active.

### P1.3 proof

```text
Repository Verify
run: 31379718341
head: dcb9bdf54a5749d04be2362b9d33918ab332f4f2
result: PASS

Production Verify
run: 31379718339
head: dcb9bdf54a5749d04be2362b9d33918ab332f4f2
result: PASS
```

Production Verify sub-gates all passed: locked dependencies, compile, Project Document contracts, Voice Production contracts, and fail-closed aggregate.

P1-F04 and P1-F05 are therefore **implemented** at the mechanical revision/entry-binding level claimed. Semantic, visual, pronunciation/performance, and audio evidence remain separate.

## P1.4 Boundary

Finding:

- **P1-F06 MEDIUM** — canonical Voice Markdown may contain a section heading with zero entries; current parser accepts the section but later builder subtitle logic assumes `section.entries` is non-empty, producing an uncontrolled failure path.

Owners:

```text
kits/voice-production-kit/builder/build_docx.py
kits/voice-production-kit/validator/validate.py only if the same explicit section rule must be checked at Flow 7
tests/test_voice_contracts.py
kits/voice-production-kit/SCRIPT-PRODUCTION.md only where the canonical section rule must be documented
```

Required P1.4 work:

1. establish one explicit Flow 6 rule for zero-entry `##` sections from current product semantics;
2. reject or intentionally omit them **before** builder presentation helpers assume entries exist;
3. return a controlled non-zero builder failure for invalid canonical script shape rather than `IndexError`/traceback;
4. inspect only directly adjacent parser/builder exception paths exposed by the same focused regression;
5. add focused empty-section/failure-state regressions;
6. preserve P1.3 revision and per-entry integrity contracts;
7. pass both repository gates.

## Explicit Out Of Scope

- general Markdown parser framework;
- redesigning the Voice Markdown format;
- semantic `Must communicate` automation;
- DOCX visual approval;
- pronunciation/performance or audio validation;
- P1.5 test-discovery change;
- P1.6 output atomicity;
- root skill changes;
- `main` changes.

## Acceptance

P1.4 is complete only when:

```text
zero-entry section → explicit controlled behavior, never IndexError
covered malformed adjacent parser state → controlled failure
current Voice happy path → PASS
P1.3 stale-revision and per-entry regressions → PASS
Production Verify → PASS
Repository Verify → PASS
```

## Next Step

Implement **P1.4 — Voice Parser / Failure-State Hardening** only: establish the explicit zero-entry section contract at the smallest parser/builder owner, add focused regression, and run both gates before proceeding to P1.5.
