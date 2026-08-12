# Production + Operating Validation Report

Updated: 2026-08-12

This file records the **current evidence state only**. Historical debugging and superseded preview detail belong in Git history and review evidence.

## Current system state

Working branch: `Local`.

Project Document Generator is **v1.13.0**. Current PRD production remains:

```text
source / approved decisions
→ normalized requirement state
→ one Content Purity + Humanize pass
→ canonical content.md
→ direct render-data projection
→ deterministic approved-Golden render
→ mechanical/content-purity validation
→ integrated semantic review
→ targeted desktop visual sanity
→ handoff
```

The approved Golden Sample remains the canonical visible page prototype. Generated HTML is derived and is never patched to hide an upstream defect.

## Current Clockwork acceptance proof

The user approved the final Clockwork preview on 2026-08-12.

Accepted bindings:

```text
source
f4d58341ce3cb7fb17bfc9986b5df67a23058d1b94a0bc78c1dad09abdd445d0

content.md
5aa7bacab594b98e062fbca035583df78e7691c680ee2654e15bfa17cecf65de

render-data.json
bf3e0eccf2cf5495c489e843bd27be99fbf547b51d4c7de321969868f7706bd0

final.html
0502e3cb78e5c834e540d9715d78cb3fbdf1f8519ab5b6a8c976c257a59d7024
```

Current artifact proof:

- Flow 2 state has no material open decision;
- 30 expected Golden pages are present in the required order;
- HTML IDs are unique and fragment navigation is reachable;
- canonical-content → render-data → HTML bindings match;
- four scored objectives retain the approved 0–100 scale and 100% component-weight totals;
- content-purity validation reports no observed project/document-process leakage or generic filler-note data;
- approved Clockwork mechanics remain materially conserved;
- targeted Chromium desktop review passed on the representative affected pages;
- no clipping, collision, horizontal overflow, or concrete readability defect was observed;
- Golden CSS was not changed.

## Repository evidence boundary

The accepted Clockwork package is now persisted on `Local` under:

```text
workspace/active/the-clockwork-vault/
```

That package is the sole current Clockwork production authority. Its canonical content, render-data projection, final HTML, acceptance state, and handoff state are stored together in the active workspace.

The authoritative source HTML remains externally retained with its exact filename and SHA-256 recorded in `state/source-inventory.yaml`; duplicating the large source file in Git is not required for current production.

Standalone review HTML, recovery scripts, screenshots, one-off transport workflows, and earlier integration proof are supporting or historical evidence only and must not be used as current project authority.

Current continuation is owned by `docs/knowledge/next-action.md`.
