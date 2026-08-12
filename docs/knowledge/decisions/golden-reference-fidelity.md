# Golden Reference Fidelity and Material Conservation

Date: 2026-08-12
Status: current

## Context

A representative AFTERSHOCK v2.4 regeneration kept the expected 30-page family and reused the Golden visual CSS/runtime, yet materially diverged from the approved document. The generated `<main>` was substantially thinner: dense requirement lists, table rows/cells, glossary coverage, and multi-paragraph gameplay explanation were compressed or omitted even though the outer page shell still matched.

Git history also showed two independent drift sources:

1. the full approved Golden HTML had been replaced in the active runtime template path by a cleaned/reconstructed interpretation;
2. renderer helpers/tests had normalized Golden IDs/classes (`phase-*`, `quarry-*`, exact global IDs) into generic aliases and then tested those aliases as if they were correct.

That allowed a generated document to look approximately related to the reference while no longer using the same approved composition contract.

## Decision

The exact approved Golden artifact is both the canonical reference and the runtime template source.

The repository keeps two paths for clarity, but they intentionally point to identical bytes:

```text
template/golden-reference.html
→ canonical Golden evidence

template/runtime-template.html
→ default runtime alias
```

Current approved Git blob:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

A cleaned, normalized, reconstructed, or generic alternative is not an acceptable replacement for either path.

The renderer may make only non-visual project-specific changes in a temporary copy during generation: sample identity metadata removal, localStorage namespacing, project metadata binding, navigation replacement, page-content replacement, glossary-data replacement, and render revision binding. The checked-in Golden CSS/runtime/DOM vocabulary remains unchanged.

The Golden Sample remains **presentation/structure authority only**. It never supplies project-specific mechanics, story, scoring, counts, or implementation facts.

Flow 3 must separately conserve every independently actionable material rule recovered from project authority. Humanize/concise writing may shorten wording, but may not delete or flatten distinct conditions, values, exceptions, recovery behavior, scoring/reset rules, build constraints, glossary meaning, or observable results.

Flow 4 therefore requires both:

```text
Material Conservation: PASS
Golden Fidelity: PASS
```

before a new handoff can be accepted.

## Why exact runtime reuse is required

The earlier idea of keeping a separate “maintainable runtime shell” was still too permissive. In practice it invited silent normalization of:

- `flow-start` into alternate IDs;
- `shared-systems`, `shared-data-reset`, and `phase-development` into `global-*` aliases;
- `phase-nav-*` into `package-nav-*`;
- `phase-context-grid` and `quarry-*` component names into generic grids/tables;
- package glossary coverage into role-filtered subsets.

Those changes were not harmless internals because the Approved CSS/JS targets those exact names and because they changed what the sample actually demonstrated.

Using the exact Golden bytes as the runtime source avoids a second presentation implementation. Project facts remain safely dynamic because the renderer replaces only project-owned surfaces (`<main>`, navigation, glossary data, document metadata) rather than treating sample facts as authority.

## Material-detail conservation

Page-count and component-presence checks can prove a shell while missing destructive semantic compression. Therefore shape parity alone is not enough.

For every independent source rule recovered in Flow 2, Flow 3 must retain one owned readable representation. Structured multi-rule content stays structured rather than being flattened into a single summary sentence for convenience.

## Supersedes / refines

This decision supersedes:

- the shorthand that the “approved PRD template is preserved as a shell” when that wording permits a reduced reconstruction;
- the initial 2026-08-12 split where `golden-reference.html` was exact but `runtime-template.html` could remain a separate cleaned runtime interpretation.

It refines “Golden Samples are references, not project requirements”:

- still true for project facts/mechanics;
- **not** true for the explicitly approved visible document composition, runtime DOM vocabulary, interaction behavior, and demonstrated information-density standard.

## Proof boundary

Repository and PRD CI prove exact artifact retention, Golden DOM projection contracts, material-conservation handoff gating, and deterministic generation behavior.

A freshly regenerated real AFTERSHOCK document still requires an actual browser/visual comparison before representative visual parity can be claimed. Static checks do not claim that proof.
