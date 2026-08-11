# Golden Reference Fidelity and Material Conservation

Date: 2026-08-12
Status: current

## Context

A representative AFTERSHOCK v2.4 regeneration kept the expected 30-page family and reused the Golden visual CSS/runtime, yet materially diverged from the approved document. The generated `<main>` was substantially thinner: dense requirement lists, table rows/cells, glossary coverage, and multi-paragraph gameplay explanation were compressed or omitted even though the outer page shell still matched.

Git history also showed that the exact approved Golden HTML had been replaced in the active template path by a cleaned runtime interpretation. That made the repository capable of testing a reconstructed shell without retaining the full approved reference as current evidence.

## Decision

Keep two separate artifacts with separate authority:

```text
template/golden-sample.html
→ exact approved Golden reference artifact
→ canonical evidence for visible composition, interaction behavior, spacing, and representative information density

template/approved-document.html
→ maintained runtime shell used by the renderer
→ implementation may be refactored only when projection remains faithful to the Golden reference
```

The Golden Sample remains **presentation/structure authority only**. It does not supply project-specific mechanics, story, scoring, counts, or implementation facts.

Flow 3 must also conserve every independently actionable material rule recovered from project authority. Humanize/concise writing may shorten wording, but may not delete or flatten distinct conditions, values, exceptions, recovery behavior, scoring/reset rules, build constraints, or observable results.

Flow 4 therefore requires a separate `Material Conservation: PASS` in addition to `Golden Fidelity: PASS` before a new handoff can be accepted.

## Why

Page-count and component-presence checks can prove the shell while missing destructive semantic compression. Conversely, making the full approved document the runtime source would unnecessarily couple project facts to presentation. Separating the canonical reference from the runtime shell keeps the implementation maintainable while preserving exact evidence of what the renderer is required to reproduce.

## Supersedes

This decision supersedes the earlier shorthand that the “approved PRD template is preserved as a shell” when that wording is interpreted as allowing a reduced reconstruction to replace the full approved reference.

It also refines “Golden Samples are references, not project requirements”:

- still true for project facts/mechanics;
- **not** true for the approved PRD's visible document composition and demonstrated information-density standard, which are binding representation requirements for this generator until the user explicitly approves a new Golden design.

## Proof boundary

Repository and PRD CI may prove artifact retention, contract enforcement, and handoff gating. A regenerated project's visual parity still requires an actual browser/visual comparison; static checks do not claim that proof.
