# Next Action

Updated: 2026-08-11

## Current Status

`PRD_GITHUB_FALSE_GREEN_GUARDS_STRENGTHENED_LOCAL_TEST_DEFERRED`

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

Repository-level static safeguards continue to protect:

- mandatory root `AGENTS.md` tail sections (`Execution channel`, `User-facing communication`, `Product boundaries`);
- Project Document Generator `SKILL.md` / kit `README.md` version parity.

PRD production contracts now additionally protect these concrete false-green cases:

- Flow 4 fails when `state/intake-state.yaml` is missing, ambiguous, or does not explicitly report both `status: ready_for_prd` and `ready_for_prd: true`;
- `render-data.json` carries `canonical_content_sha256`; Flow 4 rejects a missing/invalid binding or a projection left stale after `work/content.md` changes;
- weighted scoring accepts numeric values or numeric percentage strings, but every declared component weight must parse and weighted totals must equal 100;
- intentional EN + ID rendering requires explicit localized values for user-visible text instead of silently treating a scalar English string as Indonesian; structural/non-linguistic fields remain scalar where defined;
- Journey grids beyond six items and Flow grids beyond four items preserve wrapped-row separator mechanics and reset the false left-edge divider on the first item of each wrapped row.

These are narrow guards for observed defects. They are not a generic document schema, semantic parser, visual snapshot system, or new framework.

## Evidence boundary

This correction batch was performed through repository inspection and GitHub Actions only.

GitHub/static/CI evidence can prove repository routing, documentation consistency, current-revision binding, renderer/validator static contracts, and regression tests. It does **not** prove:

- practical Flow 2 recovery quality on a real project;
- semantic equivalence between arbitrary canonical prose and projection beyond current-revision binding plus the existing Flow 4 semantic review;
- browser/visual fidelity, including the actual appearance of wrapped grids;
- local render/runtime behavior or measured usage.

## Deliberately not changed

No broader mechanism is justified by current evidence:

- no broad Flow 2 documentation consolidation without a new concrete owner-drift defect;
- no mass rename/refactor of inherited Aftershock/`quarry-*` renderer vocabulary without a functional defect;
- no generic content parser/schema or automatic semantic-comparison framework;
- no generalization beyond the current gameplay PRD document family;
- no handoff-state gate added without evidence that the current Flow 4 sequencing is wrong;
- no local/manual real-project or browser testing until the user explicitly allows it.

## Testing boundary

Per current user direction, **do not run local/manual real-project tests yet**.

## GitHub audit result

The concrete GitHub-side false-green defects found in the current PRD Flow 2 → Flow 3 → Flow 4 path have been corrected with focused regression coverage. Remaining limitations require either new concrete repository evidence or the deferred real-project/browser proof; they should not be converted into preventive architecture.

## Next Step

Wait for the next user-directed GitHub-side task or explicit permission for local/manual real-project/browser proof.
