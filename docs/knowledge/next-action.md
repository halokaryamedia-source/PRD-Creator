# Next Action

Updated: 2026-08-12

## Current Status

`PRD_GOLDEN_REVERSE_FILL_CONTRACT_LOCKED_REGEN_PROOF_NEEDED`

Working branch: **`Local` only**.

## Current system state

The approved AFTERSHOCK Golden HTML remains retained verbatim at both runtime/reference paths:

```text
kits/project-document-generator/template/golden-sample.html
kits/project-document-generator/template/approved-document.html
```

Both files remain intentionally byte-identical to approved Git blob:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

The default renderer uses that exact Golden artifact as the presentation source. Project-specific metadata, storage namespace, navigation, page content, glossary data, and revision binding are applied only to a temporary render copy; checked-in Golden CSS/runtime/DOM stays unchanged.

Golden projection preserves the approved runtime vocabulary, including:

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

Flow 3 has an explicit material-detail conservation rule: independent source conditions, values, exceptions, recovery behavior, scoring/reset rules, build constraints, glossary meaning, and observable results may be rewritten more directly but may not be deleted or flattened merely to make the PRD shorter.

## Reverse-derived Golden fill contract

Golden is now interpreted in the correct direction:

```text
exact approved Reference
→ map the fixed visible slots and the question each slot answers
→ fill those slots from current project authority
→ preserve material detail inside the owning slot
→ generate through the exact Golden runtime
→ validate the result against the same fill map
```

The reverse map locks only what the Sample actually demonstrates as presentation/authoring structure. It does **not** turn AFTERSHOCK-specific mechanics or numbers into global requirements.

Fixed Golden authoring pattern includes:

- Overview: 3 fixed fact slots plus one journey card per gameplay package;
- Gameplay Flow: story-page reading pattern with data-driven narrative depth;
- four Global Development pages: 4 Development Flow cards + requirements + 4 notes + Terms Used;
- Gameplay Overview: 3 context cards + 6 fixed Gameplay Information rows + 5 compact flow beats + Terms Used;
- Level Design: 4 Design Flow cards + Golden Build Requirements columns + 4 notes;
- Developer: 4 Development Flow cards + Golden Development Requirements columns + 4 notes;
- table group/row counts and glossary term counts remain data-driven where Golden demonstrates variable content.

`CONTENT-CONTRACT.md` now defines what each of these slots is responsible for answering so future generation does not merely reproduce the right boxes with the wrong or incomplete content.

Golden fidelity proof is now explicitly bidirectional:

```text
Reference → Fill Map
Project Authority → Filled Golden
```

`tests/test_prd_golden_reference.py` contains the focused reverse-reference regression proof. Existing renderer/validator contract tests remain the forward projection proof.

Flow 4/handoff still requires both:

```text
Material Conservation: PASS
Golden Fidelity: PASS
```

## Why this refinement was needed

The failed AFTERSHOCK v2.4 regeneration exposed two different classes of failure:

1. a page can use the correct shell/CSS while detailed source meaning is compressed or omitted;
2. a generator can gradually redefine what it thinks the Golden structure is unless the contract is first derived from the exact approved Sample itself.

Therefore neither page-count/CSS parity nor a manually imagined generic PRD schema is enough.

## Proof boundary

Repository/static proof can verify:

- exact Golden artifact retention;
- the reverse-derived Sample signature;
- fixed Golden DOM/component/cardinality rules;
- generated projection contracts;
- material-conservation handoff gating.

A freshly regenerated real AFTERSHOCK v2.4 under the corrected contract has **not** yet been produced and browser-compared because the current authoritative AFTERSHOCK Flow 2/Flow 3 source/render-data is not present in the active repository evidence available here.

Static checks do not claim browser/visual parity.

## Next Step

**Regenerate AFTERSHOCK v2.4 from its current authoritative project content/render-data when that authority is available, then perform one targeted desktop page-family comparison against `template/golden-sample.html`; fix only concrete remaining fidelity/readability defects.**
