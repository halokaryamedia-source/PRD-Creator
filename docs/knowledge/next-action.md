# Next Action

Updated: 2026-08-12

## Current Status

`PRD_GOLDEN_REFERENCE_RETAINED_MATERIAL_CONSERVATION_ENFORCED_REGEN_PROOF_NEEDED`

Working branch: **`Local` only**.

## Current system state

The AFTERSHOCK Approved Doc is now retained verbatim at:

```text
kits/project-document-generator/template/golden-sample.html
```

That file is canonical evidence for the approved visible document composition, behavior, spacing, and representative information density. It is deliberately separate from the maintained runtime shell:

```text
kits/project-document-generator/template/approved-document.html
```

Flow 3 now has an explicit material-detail conservation rule: independent source conditions, values, exceptions, recovery behavior, scoring/reset rules, build constraints, glossary meaning, and observable results may be rewritten more directly but may not be deleted or flattened merely to make the PRD shorter.

Flow 4/handoff now requires both:

```text
Material Conservation: PASS
Golden Fidelity: PASS
```

The PRD CI also locks retention of the exact Golden reference artifact and representative Golden DOM markers/examples.

## Audit result that caused this correction

The failed AFTERSHOCK v2.4 regeneration retained the expected 30-page family and reused the Golden visual CSS/runtime, but its generated main document was materially thinner than the Approved Doc. Dense lists, table rows/cells, glossary coverage, and multi-paragraph gameplay meaning were compressed or omitted. Therefore matching page shells/classes alone is no longer accepted as Golden fidelity.

## Current proof

Commit `f3422e29` introduced the production/validation changes.

```text
Repository Verify #215 — PASS
PRD Verify #122       — PASS
```

The exact Approved Golden artifact is present on `Local` with Git blob:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

Static/CI proof is complete for this contract correction.

A freshly regenerated AFTERSHOCK v2.4 under the corrected material-conservation contract has **not** yet been produced and visually compared, so representative browser parity remains unproven.

No mobile or Voice proof is required for this correction.

## Next Step

**Regenerate AFTERSHOCK v2.4 from current project authority under the new material-conservation contract, then perform one targeted desktop page-family comparison against `template/golden-sample.html`; fix only concrete remaining fidelity/readability defects.**
