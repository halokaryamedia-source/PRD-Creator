# Next Action

Updated: 2026-08-11

## Current Status

`PRD_FLOW2_GITHUB_BOUNDARY_REFINED_LOCAL_TEST_DEFERRED`

Working branch: **`Local` only**.

## Current PRD contract

- Golden Sample remains the required hierarchy, page-composition, component-language, and presentation authority.
- Normal PRD creation/revision is Production Execution; no `development-brief`.
- Flow 2 is the production-recovery/problem-solving stage, not only source extraction/provenance.
- Flow 3 receives resolved production meaning and must not silently decide material Flow 2 gaps.
- Flow 4 may expose missed recovery defects but returns new product/design choices to Flow 2.

## Flow 2 recovery + problem-solving contract

```text
source inventory + inspection
→ explicit facts/rules/exclusions
→ topology + terminology
→ cross-role implications
→ production coverage
→ lifecycle + quantitative + operational clarity
→ global/local coherence + known-constraint feasibility
→ problem framing
→ Resolution Ladder
→ impact propagation
→ humanized grouped decision package only if needed
→ ready_for_prd
```

Key boundaries:

- persist material user instructions even when no file exists;
- keep removals/exclusions as first-class requirements;
- recover topology/global ownership/transitions/final result when relevant;
- recover necessary Gameplay / Level Design / Developer implications;
- detect material lifecycle gaps and numeric contradictions;
- resolve materially vague wording only when it would create different product behavior; do not invent fake metrics;
- reconcile shared/global defaults with explicit local exceptions;
- check authoritative known project/platform constraints without turning generic best practice into authority;
- solve before asking: authority → safe Completion → supported recommendation → balanced tradeoff → Blocked/direct decision;
- use `Recommended` only when evidence/goals/constraints genuinely favor one option;
- propagate approved/recovered resolutions to all actually affected meaning;
- group only truly related decisions;
- keep optional advisory ideas out of the user's way;
- stop Flow 2 once production-ready instead of continuing speculative design optimization.

## Humanized Flow 2 communication

When one recommendation is justified:

```text
Masalah
Saran
Kenapa
Dampak
Alternatif — only when meaningful
```

When no clear default exists, use a concise `Pilihan` + tradeoff explanation instead of pretending one option is recommended.

Humanize is presentation behavior only. It must not alter official terminology, quantities, timings, formulas, mechanics, triggers, uncertainty, provenance, or approval status. No new Humanize root skill is added.

## Flow 2 → Flow 3 boundary

Flow 3 may organize/clarify approved meaning, but it must return material gaps to Flow 2 when drafting exposes:

- topology/global-local ownership/transition/final-result ambiguity;
- lifecycle gaps;
- contradictory numbers/timing/scoring;
- materially vague behavior;
- shared/global rule versus package-exception conflict;
- authoritative known-constraint conflict;
- missing cross-role implication;
- exclusion/terminology ambiguity;
- another unresolved product/design choice.

Flow 4 uses the same fallback rule if review finds one of these issues later. Wording may be fixed downstream only when the underlying approved meaning is already clear.

## Efficiency boundary

Do not add topology/coverage/lifecycle/quantitative/clarity reports, dependency graphs, mandatory checklists, source indexers, Humanize skill layers, or new validators merely to represent these checks. Keep them as reasoning over existing source/requirement state.

No local/manual real-project test is allowed yet per current user direction.

## Evidence boundary

Current GitHub-side work changes semantic/procedure contracts only. Golden HTML, renderer behavior, Flow 4 validator code, `content.md → render-data.json`, handoff semantics, and Voice behavior remain unchanged.

GitHub CI can prove repository/procedure consistency only. It does not prove practical recovery quality, local render behavior, visual fidelity, or measured usage.

## Next Step

Continue **GitHub-only static audit** for remaining Flow 2/3/4 owner drift or low-cost repository safeguards. If no concrete GitHub-side defect remains, record that boundary as complete and wait; do not start local/manual testing until the user explicitly allows it.
