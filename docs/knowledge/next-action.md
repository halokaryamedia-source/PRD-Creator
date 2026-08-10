# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Execute **P1.1 — PRD Mechanical Revision Integrity** from the Production Engineering Remediation Plan.

Make the Flow 4 mechanical validator fail closed on malformed current render-data and prove that `output/final.html` belongs to the current `work/render-data.json` revision before it can mechanically PASS.

## Current Status

`BUILD_IT_PARITY_P1_AUDIT_COMPLETE_P1_1_PRD_REVISION_INTEGRITY_NEXT`

Execution channel: **ChatGPT → GitHub**.  
Working branch: **`Local` only**.

## Governing Evidence

Current BuildIT comparison:

`docs/knowledge/reviews/buildit-current-parity-gap-audit.md`

P0.2 ownership decision:

`docs/knowledge/decisions/technical-ownership-boundary.md`

P1 Production Engineering Quality Audit:

`docs/knowledge/reviews/production-engineering-quality-audit.md`

Ordered P1 remediation:

`docs/knowledge/operations/production-engineering-remediation-plan.md`

Top-level parity plan:

`docs/knowledge/operations/buildit-parity-remediation-plan.md`

## Completed Baseline

### P0.1 — Executable Production Verify

```text
Production Verify 31372363843  PASS
Repository Verify 31372363802  PASS
```

### P0.2 — Technical Ownership Refinement

```text
source head        a0a51d97523ab07f87ef6deeffdafc8094febea4
Repository Verify  31374226049  PASS
Production Verify  31374226078  PASS
```

Current ownership remains:

```text
semantic/product contract wrong
→ matching root semantic specialist

semantic contract correct + executable mechanics wrong
→ nearest kit AGENTS + exact implementation owner

shared dependency/test/CI wrong
→ requirements.lock.txt / tests / tools / workflows
```

## Completed P1 Audit

The source-backed audit found nine material/conditional findings.

Highest-priority current findings:

1. **P1-F01 MAJOR** — stale PRD HTML can mechanically PASS when current render-data text changed but title/page IDs stayed the same;
2. **P1-F02 MAJOR** — malformed render-data shapes can escape the validator's structured failure result and crash during expected-page calculation;
3. **P1-F03 MAJOR** — project glossary JSON is inserted directly into a template `<script>` context without script-safe escaping;
4. **P1-F04 MAJOR** — Voice requirements/script/DOCX revision identity is not mechanically linked;
5. **P1-F05 MAJOR** — Voice DOCX validation checks global token presence rather than per-entry binding;
6. additional medium/conditional findings cover empty Voice sections, shell/metadata integrity, contract-test discovery, and output atomicity.

No generic schema/parser/tooling framework is authorized by the audit.

## P1.1 Boundary

Owners:

```text
kits/project-document-generator/validator/validate.py
kits/project-document-generator/renderer/render.py only if a small render fingerprint must be emitted
tests/test_prd_contracts.py
```

Required changes:

1. validate root arrays/items/stable IDs before any page-ID calculation;
2. malformed `gameplay_flow`, `global_development`, or `packages` data must return structured validator FAIL rather than traceback;
3. add the smallest deterministic render revision/fingerprint derived from current render-data;
4. mechanical validator must reject `final.html` when its render identity does not match current render-data;
5. reject stale extra generated pages/sections where the current generated-page set no longer matches;
6. add focused regressions for stale artifact + malformed shape;
7. preserve current happy path.

## Explicit Out Of Scope

- semantic `content.md` → render-data meaning automation;
- browser visual approval;
- template redesign;
- glossary/script-context fix (P1.2);
- Voice fixes (P1.3+);
- generic JSON Schema/profile/freeze framework;
- root skill changes;
- `main` changes.

## Acceptance

P1.1 is complete only when:

```text
malformed render-data → structured FAIL
stale render-data vs final.html → FAIL
current generated page set mismatch → FAIL
current happy render + validator → PASS
focused PRD regressions → PASS
Production Verify → PASS
Repository Verify → PASS
```

Browser visual quality remains separate evidence.

## Next Step

Implement **P1.1 — PRD Mechanical Revision Integrity** only: harden the current PRD validator/render identity contract and add the smallest focused regressions, then run both repository gates before proceeding to P1.2.
