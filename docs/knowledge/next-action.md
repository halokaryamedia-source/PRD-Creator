# Next Action

## Current Status

`P1_FRESHNESS_INTEGRITY_COMPLETE`

P0 Current Authority Integrity and both bounded P1 remediations are complete: Canonical 04/Voice Source Normalization and Freshness Integrity.

Repository continuity remains:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules for material GitHub work
→ CONTEXT.md
→ next-action.md
→ development-brief for non-trivial Developing
→ smallest relevant owner/source
```

## Active Boundary

The audited same-version false-PASS gaps are closed without adding a revision registry or new workflow layer.

Current handoff integrity:

- `validate_handoff.py` reuses the existing Project Document mechanical validator before authorizing Flow 5;
- `handoff_ready` therefore requires the current canonical content, render projection, current versioned HTML, and current Production Asset source binding to pass the existing mechanical/freshness gate now, not only when acceptance was previously recorded;
- a same-version edit to canonical PRD bytes without regeneration is mechanically rejected.

Current Voice revision identity:

- `voice-state.yaml.source_handoff` must resolve to a current handoff state;
- upstream handoff status must be `handoff_ready`;
- `voice-state.yaml.source_prd_revision`, handoff `accepted_prd_version`, `render-data.document.version`, Flow 5 `Source PRD revision`, and Flow 6 source revision must agree;
- `voice-production.md` binds directly to the exact current `work/voice-requirements.md` bytes through its existing `Source Voice Requirements` header plus SHA-256;
- the Voice project HTML path must point to the same accepted PRD revision;
- a same-ID / same-Type / same-Speaker requirement edit can no longer leave an older Voice script mechanically valid.

Clockwork remains current after this change:

- PRD handoff validation: PASS;
- Voice mechanical validation: PASS (`19` requirements = `19` script entries, consolidated project HTML parity PASS);
- Project HTML Visual remains `NOT PROVEN` and Audio Evidence remains `not_provided`; those evidence boundaries were not changed or inflated.

No Golden bytes, protected 01–03 output, gameplay, Voice wording/performance payload, generated PRD HTML, acceptance result, or project readiness state changed in this freshness remediation.

## Last Completed

- Completed P0 Current Authority Integrity without redesign.
- Completed P1 Canonical 04/Voice Source Normalization and regenerated/revalidated the Clockwork delivery bundle.
- Closed F09 current-handoff freshness by reusing the current Project Document mechanical validator at handoff entry.
- Added regression proof that same-version stale PRD bytes cannot authorize Flow 5.
- Closed F10 Voice revision identity by binding current handoff/PRD/requirements/script identity and exact Flow 5 requirement bytes.
- Added regression proof for stale same-version Voice requirement bytes, stale Voice PRD revision, and non-ready upstream handoff.
- Revalidated the actual Clockwork handoff and Voice delivery against the new gates.
- Repository verification remains green locally.

## Deferred / Do Not Continue

- Do not create a generic revision registry, manifest, schema framework, freshness service, or extra workflow layer.
- Do not remove compatibility parser fields/helpers merely because current Clockwork no longer uses legacy metadata until P2 re-triage proves that cleanup is still worthwhile.
- Do not broaden DOCX validation, renderer/CSS cleanup, test-discovery work, atomic-write work, or other P2/P3 findings into this completed P1 change.
- Do not change Golden bytes, protected 01–03 behavior, gameplay, Voice wording, or audio evidence.

## Next Step

Begin only **P2 — Mechanical Cleanup triage**: re-check the promoted P2 findings against the current `Local` implementation, identify which defects still reproduce after P0/P1, and select one smallest worthwhile fix before changing code. Do not bundle compatibility-parser, DOCX, CSS, renderer, or unrelated cleanup into one delivery.
