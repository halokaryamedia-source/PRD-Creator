# Next Action

Updated: 2026-08-11

## Current Status

`PRD_PRE_SAMPLE_READY_SOURCE_STATE_LIFECYCLE_EFFICIENCY_REFINED`

Working branch: **`Local` only**.

## Current PRD contract

- Golden Sample remains the required hierarchy, page-composition, component-language, and presentation authority.
- Normal PRD creation/revision is Production Execution; no `development-brief`.
- User burden stays low: automatic bootstrap, source-first recovery, grouped material decisions only when needed, delta-first revisions, concise delivery.
- PRD prose uses plain technical writing without AI-style filler or invented detail.
- English-only is default unless EN + ID is intentionally produced.
- Journey/Flow grids adapt item count within existing Golden capacities.
- Package Terms Used are role-specific instead of repeated on every role page.

## Efficiency rules

### Source reading

```text
inventory
→ relevance/authority triage
→ deep-read material authoritative source
→ targeted-read supporting/reference/generated source as needed
```

Inventory completeness does not require loading every byte. If uncertain material could change the PRD, inspect it rather than assuming irrelevance.

### Internal state

Use sparse state where defaults are defined:

- omit empty/default fields;
- persist conflicts, pending approvals, blocked/superseded state, and other exceptions explicitly;
- keep positive `ready_for_prd: true` explicit;
- do not let sparse storage weaken traceability.

### Artifact lifecycle

Create artifacts only when their owning Flow needs them:

```text
Core        → current Flow authority/state
Conditional → review/project note only when useful
Derived     → render-data / final HTML generated from canonical meaning
Downstream  → Voice files only after entering Voice Flow
```

Do not pre-create empty files merely to match an eventual full-project tree.

### HTML/context

```text
content.md
→ compact render-data.json
→ renderer
→ Golden template
→ final.html
```

- do not hand-author `final.html`;
- do not load the large Golden template or full generated HTML into model context during normal production;
- let renderer/validator consume large HTML files at runtime;
- inspect HTML source only for a concrete bounded defect;
- finish canonical content before the main projection;
- patch only affected projection/review scope during bounded revisions;
- load only the active Flow owner/procedure.

## Evidence boundary

Repository/production CI is the repeatable engineering proof for repository changes. Actual new-project Golden visual quality still requires the planned coherent real-project Flow 2 → 4 run; no manual/real-project visual test has been run yet for this refined system.

## Do not add now

No new source indexer/RAG/vector store, state schema framework, artifact manager, template/profile framework, HTML schema, pixel/screenshot scoring, AI detector, generic parser, checksum/revision machinery, or `content.md → render-data.json` architecture rewrite without real evidence.

Handoff-state simplification remains deferred to the later PRD → Voice boundary review.

## Next Step

Run **one real project through Flow 2 → 4** as the first coherent practical sample. Measure actual user friction, source-reading/context cost, state/artifact overhead, Golden visual fidelity, and output usability; fix only defects that appear in that run.