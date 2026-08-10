# Next Action

Updated: 2026-08-11

## Current Status

`PRD_FLOW2_GITHUB_STATIC_AUDIT_COMPLETE_LOCAL_TEST_DEFERRED`

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

## Flow 2 → Flow 3/4 boundary

Flow 3 may organize/clarify approved meaning, but it must return material gaps to Flow 2 when drafting exposes topology/lifecycle/numeric/operational-clarity/global-local/known-constraint/cross-role/exclusion/terminology ambiguity or another unresolved product/design choice.

Flow 4 uses the same fallback rule if review finds one of these issues later. Wording may be fixed downstream only when the underlying approved meaning is already clear.

## GitHub-side safeguards now active

`tools/verify_repository.py` now protects two concrete repository invariants demonstrated by this audit:

- mandatory root `AGENTS.md` retains its required tail sections (`Execution channel`, `User-facing communication`, `Product boundaries`);
- Project Document Generator `SKILL.md` and kit `README.md` must report the same version.

These are small static guards based on observed defects, not a generic documentation-schema framework.

## Efficiency boundary

Do not add topology/coverage/lifecycle/quantitative/clarity reports, dependency graphs, mandatory checklists, source indexers, Humanize skill layers, new validators, or documentation schemas merely to represent reasoning already owned by Flow 2.

## Testing boundary

Per current user direction, **do not run local/manual real-project tests yet**.

GitHub/static/CI evidence can prove repository routing, documentation consistency, static invariants, and existing regression contracts. It cannot prove practical recovery quality, local render behavior, browser visual fidelity, or measured usage.

## GitHub audit result

The current Flow 2 → Flow 3 → Flow 4 semantic/routing owners have been aligned for the strengthened recovery/problem-solving boundary. High-level README/context/foundation/skill/procedure wording and the small observed static invariants are synchronized.

No additional GitHub-side Flow 2 mechanism is currently justified without a new concrete defect. Do not add preventive architecture merely because more checks are imaginable.

## Next Step

Wait for the next user-directed GitHub-side task or new concrete repository evidence. Do **not** start local/manual real-project testing until the user explicitly allows it.
