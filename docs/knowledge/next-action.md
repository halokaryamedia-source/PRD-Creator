# Next Action

Updated: 2026-08-11

## Status

`PRD_PRE_SAMPLE_READY_HTML_CONTEXT_EFFICIENCY_REFINED`

Working branch: **`Local` only**.

## Current PRD contract

- Golden Sample remains the required hierarchy, page-composition, component-language, and presentation authority.
- Normal PRD creation/revision is Production Execution; no `development-brief`.
- User burden stays low: automatic bootstrap, inspect source first, grouped material decisions only when needed, delta-first revisions, concise delivery.
- PRD prose uses plain technical writing without AI-style filler or invented detail.
- English-only is default unless EN + ID is intentionally produced.
- Journey/Flow grids adapt item count within existing Golden capacities.
- Package Terms Used are role-specific instead of repeated on every role page.

## HTML/context efficiency

Normal production treats HTML rendering as deterministic runtime work:

```text
content.md
→ compact render-data.json
→ renderer
→ Golden template
→ final.html
```

Rules:

- do not hand-author `final.html`;
- do not load the ~794 KB Golden template into model context during normal production;
- do not load full `final.html` for semantic review;
- let renderer/validator consume large HTML files at runtime;
- inspect HTML source only for a concrete bounded defect;
- finish canonical content before the main projection;
- patch only affected render-data subtree during bounded revisions;
- use scalar strings for EN-only projection instead of duplicated localized values when appropriate;
- load only the active Flow owner/procedure, not the whole PRD skill/document stack.

## Latest proof

Implementation head: `07bb8cd8919ce9fb9c1f6041ab3448af15d8a494`

- Repository Verify #52 — PASS
- Production Verify #18 — PASS

No manual/real-project visual test has been run for this refined PRD system yet.

## Do not add now

No new template/profile framework, HTML schema, pixel/screenshot scoring, AI detector, generic parser, checksum/revision machinery, or `content.md → render-data.json` architecture rewrite without real evidence.

Handoff-state simplification remains deferred to the later PRD → Voice boundary review.

## Next Step

Run **one real project through Flow 2 → 4** as the first coherent practical sample. Measure actual user friction, context usage, Golden visual fidelity, and output usability; fix only defects that appear in that run.
