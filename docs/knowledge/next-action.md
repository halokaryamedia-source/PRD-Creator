# Next Action

Updated: 2026-08-11

## Current Status

`PRD_FLOW2_RECOVERY_ENGINE_STRENGTHENED_PRE_SAMPLE_READY`

Working branch: **`Local` only**.

## Current PRD contract

- Golden Sample remains the required hierarchy, page-composition, component-language, and presentation authority.
- Normal PRD creation/revision is Production Execution; no `development-brief`.
- Flow 2 now treats requirement recovery as a production-completeness task, not only source extraction/provenance.
- Flow 3 must not invent material topology, cross-role requirements, exclusions, terminology, or product decisions that Flow 2 should have recovered.
- Flow 4 keeps one-read multi-lens review plus mechanical validation and truthful visual evidence.

## Flow 2 recovery contract

Normal Flow 2 sequence:

```text
source inventory + inspection
→ explicit facts/rules/exclusions
→ topology + terminology
→ cross-role implications
→ production coverage scan
→ safe Clarification / Completion
→ grouped Proposal / Blocked decisions only if needed
→ ready_for_prd
```

Key rules:

- material user instructions are persisted as source authority even when no file exists;
- source inspection coverage can be recorded as targeted/full for resumability;
- source-level supersession applies only when the whole source is replaced;
- removals/exclusions are first-class requirements;
- topology includes package order, global ownership, dependencies/transitions, and final result when relevant;
- material mechanics are checked for necessary Gameplay / Level Design / Developer / result-reset implications;
- coverage scan checks only applicable production concerns and does not force optional fields;
- Completion requires one reliable evidence-backed result without choosing among multiple designs;
- a missing detail is material only when a downstream role would otherwise have to choose product behavior/scope.

## Efficiency boundary

Flow 2 improvement must not become user ceremony or a new artifact framework:

- no topology file;
- no coverage-report file;
- no mandatory checklist filled for every project;
- no source indexer/RAG/vector store;
- no fake file for chat instructions;
- no rereading unchanged source during bounded revisions;
- no question for optional/irrelevant detail.

Topology, exclusions, terminology, and implications remain normal `REQ-###` state. Inspection coverage remains in source inventory.

## Mechanical intake guard

No new Flow 2 validator was added. The existing validator is a Flow 4 owner and requires canonical/rendered artifacts; expanding it backward or creating another validator would add lifecycle/tooling complexity without a demonstrated state-contradiction failure. Flow 2 readiness is strengthened semantically first; add a mechanical intake sanity guard only if real project evidence proves it is needed.

## Existing context/HTML efficiency

- mandatory boot remains compact and progressive;
- load only the smallest active Flow owner;
- renderer/validator consume large HTML at runtime rather than model context;
- canonical content is completed before the main projection;
- bounded revisions patch only affected scope;
- internal state is sparse but non-default conflicts/approvals/blockers/supersession/readiness remain explicit.

## Evidence boundary

This Flow 2 batch changes semantic/procedure contracts only. It does not change Golden HTML, renderer behavior, Flow 4 validator mechanics, `content.md → render-data.json`, handoff semantics, or Voice behavior.

No new real-project sample has yet exercised the strengthened Flow 2 against genuinely incomplete source. CI can prove repository/procedure consistency, not the quality of future recovery judgment.

## Next Step

Run **one real project with genuinely incomplete/uneven source through Flow 2 → 4**. Evaluate whether Flow 2 correctly recovers topology, exclusions, terminology, cross-role implications, and material gaps before Flow 3; fix only defects demonstrated by that run.
