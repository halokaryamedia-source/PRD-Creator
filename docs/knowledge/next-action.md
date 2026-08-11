# Next Action

Updated: 2026-08-12

## Current Status

`PRD_EXACT_GOLDEN_RUNTIME_AND_MATERIAL_CONSERVATION_LOCKED_REGEN_PROOF_NEEDED`

Working branch: **`Local` only**.

## Current system state

The approved AFTERSHOCK Golden HTML is retained verbatim at both runtime/reference paths:

```text
kits/project-document-generator/template/golden-sample.html
kits/project-document-generator/template/approved-document.html
```

Both files are intentionally byte-identical to approved Git blob:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

The default renderer now uses that exact Golden artifact as the presentation source. It no longer renders through a cleaned/generic PRD shell. Project-specific metadata, storage namespace, navigation, page content, glossary data, and revision binding are applied only to a temporary render copy; checked-in Golden CSS/runtime/DOM stays unchanged.

Golden projection now preserves the approved runtime vocabulary rather than generic aliases, including:

```text
flow-start
shared-systems
shared-data-reset
phase-development
phase-navigation
phase-nav-item
phase-nav-main
phase-page-link
phase-context-grid
quarry-*
data-phase="dev-*"
```

Flow 3 also has an explicit material-detail conservation rule: independent source conditions, values, exceptions, recovery behavior, scoring/reset rules, build constraints, glossary meaning, and observable results may be rewritten more directly but may not be deleted or flattened merely to make the PRD shorter.

Flow 4/handoff requires both:

```text
Material Conservation: PASS
Golden Fidelity: PASS
```

## Audit result that caused this correction

The failed AFTERSHOCK v2.4 regeneration exposed two independent failure modes:

1. the outer 30-page shell and visual CSS/runtime could match while dense lists, requirement rows, glossary terms, and multi-paragraph gameplay meaning were compressed or omitted;
2. the runtime generator had normalized exact Golden IDs/classes/components into generic aliases, while its own regression tests treated those aliases as the desired result.

Therefore page count, headings, CSS similarity, or generic component presence alone are no longer accepted as Golden fidelity.

## Current proof

Implemented correction chain:

```text
f3422e29  fix: prevent lossy Golden PRD regeneration
b6c05583  fix: project PRDs through exact Golden DOM
db59c7ff  fix: make Golden glossary validation source-aware
```

Latest contract proof:

```text
PRD Verify #124        — PASS
Repository Verify #220 — PASS
```

Regression coverage now verifies:

- both runtime/reference template paths are byte-identical to the approved Golden blob;
- generated page IDs and Golden component/navigation classes use the approved DOM vocabulary;
- generic `package-*`/renamed projection aliases are rejected;
- project storage keys are namespaced at render time without modifying the Golden file;
- package glossary data is not silently reduced by role filtering;
- handoff cannot pass without Material Conservation and Golden Fidelity.

Static/CI proof is complete for the generator correction.

A freshly regenerated real AFTERSHOCK v2.4 under the corrected contract has **not** yet been produced and browser-compared. The repository/current uploads provide the approved HTML and failed generated HTML, but not the current authoritative AFTERSHOCK Flow 2/Flow 3 source/render-data required to regenerate without treating generated output as project authority.

No mobile or Voice proof is required for this correction.

## Next Step

**Regenerate AFTERSHOCK v2.4 from its current authoritative project content/render-data when that authority is available, then perform one targeted desktop page-family comparison against `template/golden-sample.html`; fix only concrete remaining fidelity/readability defects.**
