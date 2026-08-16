# Next Action

## Current Status

`P1_CANONICAL_SOURCE_NORMALIZATION_IMPLEMENTED_REGEN_REQUIRED`

The bounded P1 source/compositor migration is implemented on top of completed P0. Canonical Clockwork 04/Voice sources now follow their current contracts, and the shared 04 compositor no longer depends on retired Voice `Flow`, `Moment`, or `For` presentation metadata or English wording such as `throughout` to order moments.

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

P1 source normalization is implemented but **not yet delivery-complete** because the stored Clockwork versioned bundle was generated from the previous canonical source bytes.

Current source/code state:

- `work/asset-requirements.md` uses the compact current `PRODUCTION-ASSETS.md` fields, preserves all 34 concrete resources and exact player-facing copy, and retains material production detail in concise Visual/Audio Briefs rather than legacy gameplay metadata;
- `work/voice-requirements.md` retains Flow 5 communication fields and removes retired `Flow`, `Create`, `Used`, `Moment`, `Group`, and `For` metadata;
- dialogue Function presentation comes from canonical Flow 5 `Function`; `Purpose` remains internal and is not rendered as the visible 04 Function;
- dialogue moment/order comes from canonical Voice Production title/source order instead of undocumented Voice presentation fields;
- non-Voice moment order follows declared Flow order plus source order, not natural-language keyword heuristics;
- protected PRD-core 01–03, gameplay, Golden bytes, Voice scripts, and production semantics were not intentionally changed.

Current derived-state boundary:

- `output/v1.0.0/prd.html`, `context.md`, and `index.json` are marked stale until regenerated;
- PRD and Voice acceptance are `needs_revision` only because current derived delivery has not been regenerated/revalidated;
- semantic readiness, material conservation, Voice script readiness, and communication conservation remain PASS for the unchanged meaning/script scope.

Do not claim P1 complete or restore handoff/Voice delivery readiness until the canonical renderer/delivery and validators have actually run on these current sources.

## Last Completed

- Completed P0 Current Authority Integrity without redesign.
- Removed legacy-heavy 04 planning/gameplay metadata from the current Clockwork Production Asset source while preserving concrete resources, player text, and material production detail.
- Removed retired 04 presentation metadata from current Clockwork Voice Requirements.
- Removed shared 04 compositor dependence on Voice `Flow`, `Moment`, and `For` fields.
- Visible dialogue Function now uses the canonical Flow 5 `Function` field without exposing internal `Purpose`.
- Replaced the English `throughout` moment-order special case with deterministic declared-flow/source ordering.
- Added focused regression coverage for canonical Voice Function presentation, missing-Function failure, Purpose non-display, and source-order moment behavior.
- Kept compatibility parser cleanup, old Voice helper/CSS cleanup, freshness strengthening, and other P2/P3 work outside this change.

## Deferred / Do Not Continue

- Do not start handoff/Voice revision-identity freshness hardening yet.
- Do not remove compatibility parser fields/helpers merely because current Clockwork no longer needs them; that remains a separate audited boundary.
- Do not perform broad renderer/module/CSS refactors, generic parser/schema work, test-discovery work, atomic-write work, or unrelated cleanup.
- Do not change Golden bytes, protected 01–03 behavior, gameplay, Voice wording, or audio evidence.

## Next Step

Regenerate only the current Clockwork versioned `prd.html` / `context.md` / `index.json` / `output/README.md` from the normalized canonical sources using the existing renderer/delivery owners, run the current PRD mechanical validation and relevant Voice validation, confirm protected 01–03 remain unchanged, then audit this bounded P1 result before any freshness or P2 cleanup work.
