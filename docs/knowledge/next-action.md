# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Execute **P1.2 — PRD Renderer Script/Shell Safety** from the Production Engineering Remediation Plan.

Close the remaining PRD renderer trust gaps around project glossary data entering executable `<script>` context and around the minimum approved-shell markers/metadata that the renderer assumes.

## Current Status

`BUILD_IT_PARITY_P1_1_COMPLETE_P1_2_RENDERER_SCRIPT_SHELL_SAFETY_NEXT`

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

Implemented contract:

```text
current render-data.json
→ canonical sorted JSON serialization
→ SHA-256 render fingerprint
→ final.html render-data-sha256 marker
→ Flow 4 validator requires exact fingerprint match
```

The validator now also:

- preflights `gameplay_flow`, `global_development`, and `packages` array/item/stable-ID shape before expected-page calculation;
- returns structured `status: fail` for malformed collection items instead of allowing a traceback path;
- requires exactly one render revision marker;
- requires the generated `<main class="document-main">` section list to match the current expected page list exactly, including order and no stale extra pages.

Focused regressions cover:

- current happy render + validator PASS;
- render-data changed without rerender → FAIL;
- malformed collection item → structured FAIL;
- stale extra generated page → FAIL;
- existing scoring/completion + weight regression remains intact.

### P1.1 proof

```text
Production Verify
run: 31377375929
head: 04f306f8589528ccc8cb03e89333dba174a3d276
result: PASS

Repository Verify
run: 31377377036
head: 04f306f8589528ccc8cb03e89333dba174a3d276
result: PASS
```

Production Verify sub-gates all passed: locked dependencies, compile, Project Document contracts, Voice Production contracts, and fail-closed aggregate.

P1-F01 and P1-F02 are therefore **implemented** at the mechanical contract level claimed.

## P1.2 Boundary

Findings:

- **P1-F03 MAJOR** — glossary JSON is inserted directly into HTML `<script>` context without script-safe serialization; malformed alias shape can also violate the runtime contract;
- **P1-F07 MEDIUM** — renderer/template shell and metadata assumptions are only partially enforced.

Owners:

```text
kits/project-document-generator/renderer/render.py
kits/project-document-generator/renderer/pages.py only if glossary shape normalization belongs there
kits/project-document-generator/template/approved-document.html only if the shell itself is defective
tests/test_prd_contracts.py
```

Required P1.2 work:

1. serialize project glossary data safely for JavaScript `<script>` context, including content containing `</script>`;
2. preflight the alias shape actually required by the inherited glossary runtime instead of allowing malformed shapes to reach browser execution;
3. define the smallest stable approved-shell marker set required by the renderer;
4. fail clearly when a required shell marker is absent or ambiguous;
5. make intended metadata replacement explicit and tested; do not invent new shell metadata merely for coverage;
6. add focused regressions for script-context content, malformed aliases, and required shell markers;
7. keep browser visual/runtime approval separate from static mechanical proof.

## Explicit Out Of Scope

- sanitizer/framework rewrite;
- full HTML snapshot testing;
- approved-template redesign;
- semantic content validation;
- Voice revision/DOCX work (P1.3+);
- output atomicity (P1.6 conditional);
- root skill changes;
- `main` changes.

## Acceptance

P1.2 is complete only when:

```text
glossary text containing </script> → generated HTML remains script-safe
malformed glossary alias shape → controlled failure
missing/ambiguous required shell marker → controlled failure
current happy PRD render + validator → PASS
focused PRD regressions → PASS
Production Verify → PASS
Repository Verify → PASS
```

Browser visual/runtime behavior remains separate evidence where that level is claimed.

## Next Step

Implement **P1.2 — PRD Renderer Script/Shell Safety** only: harden glossary script-context serialization and the minimum renderer shell-marker contract, add focused regressions, then run both repository gates before proceeding to P1.3.
