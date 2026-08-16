# Next Action

## Current Status

`P1_CANONICAL_SOURCE_NORMALIZATION_IMPLEMENTED_LOCAL_REGEN_REQUIRED`

The bounded P1 source/compositor migration is implemented on top of completed P0. Canonical Clockwork 04/Voice sources follow their current contracts, and the shared 04 compositor no longer depends on retired Voice `Flow`, `Moment`, or `For` presentation metadata or English wording such as `throughout` to order moments.

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

P1 source/code normalization is implemented and its repository-level contracts pass, but the **stored Clockwork delivery bundle is intentionally not marked current yet** because it still predates the normalized canonical source bytes.

Current source/code state:

- `work/asset-requirements.md` uses the compact current `PRODUCTION-ASSETS.md` fields, preserves all 34 concrete resources and exact player-facing copy, and retains material production detail in concise Visual/Audio Briefs rather than legacy gameplay metadata;
- `work/voice-requirements.md` retains Flow 5 communication fields and removes retired `Flow`, `Create`, `Used`, `Moment`, `Group`, and `For` metadata;
- dialogue Function presentation comes from canonical Flow 5 `Function`; `Purpose` remains internal and is not rendered as the visible 04 Function;
- dialogue moment/order comes from canonical Voice Production title/source order instead of undocumented Voice presentation fields;
- non-Voice moment order follows declared Flow order plus source order, not natural-language keyword heuristics;
- protected PRD-core 01–03, gameplay, Golden bytes, Voice scripts, and production semantics were not intentionally changed.

Repository proof on commit `253fe1f1fe43cc5b48a81b3fd1531b1a73cf2d27`:

- `PRD Verify` run `62` — PASS;
- `Repository Verify` run `611` — PASS.

Current derived-state boundary:

- `output/v1.0.0/prd.html`, `context.md`, and `index.json` remain stale until regenerated from the normalized sources;
- PRD and Voice acceptance remain `needs_revision` only because current derived delivery has not been regenerated/revalidated;
- semantic readiness, material conservation, Voice script readiness, and communication conservation remain PASS for the unchanged meaning/script scope.

### Execution-channel blocker

The current GitHub connector session can read/write repository state and inspect CI but cannot materialize a repository checkout/archive into the executable container. Direct container `git clone` also has no network access. Therefore the canonical renderer/delivery cannot be honestly executed in this channel.

Do **not** revive historical `.tmp-clockwork` / `.regen-transfer` staging-finalizer hacks, create temporary transfer commits, or use GitHub Actions as a remote shell to bypass this boundary. Those are historical implementation evidence, not current workflow authority.

This is `LOCAL PROOF REQUIRED`, not evidence that more source/compositor redesign is needed.

## Last Completed

- Completed P0 Current Authority Integrity without redesign.
- Removed legacy-heavy 04 planning/gameplay metadata from the current Clockwork Production Asset source while preserving concrete resources, player text, and material production detail.
- Removed retired 04 presentation metadata from current Clockwork Voice Requirements.
- Removed shared 04 compositor dependence on Voice `Flow`, `Moment`, and `For` fields.
- Visible dialogue Function now uses the canonical Flow 5 `Function` field without exposing internal `Purpose`.
- Replaced the English `throughout` moment-order special case with deterministic declared-flow/source ordering.
- Added focused regression coverage for canonical Voice Function presentation, missing-Function failure, Purpose non-display, and source-order moment behavior.
- Confirmed the relevant PRD and repository CI gates pass on the P1 source/code commit.
- Kept compatibility parser cleanup, old Voice helper/CSS cleanup, freshness strengthening, and other P2/P3 work outside this change.

## Deferred / Do Not Continue

- Do not start handoff/Voice revision-identity freshness hardening yet.
- Do not remove compatibility parser fields/helpers merely because current Clockwork no longer needs them; that remains a separate audited boundary.
- Do not perform broad renderer/module/CSS refactors, generic parser/schema work, test-discovery work, atomic-write work, or unrelated cleanup.
- Do not change Golden bytes, protected 01–03 behavior, gameplay, Voice wording, or audio evidence.
- Do not treat historical transfer/finalizer helpers as an approved workaround for an unavailable checkout runtime.

## Next Step

In an actual checkout of the current `Local` HEAD, run the existing Clockwork delivery regeneration (`renderer/delivery.py`) and current PRD + Voice validators, compare protected 01–03 before/after the additive 04 regeneration, restore handoff/Voice delivery readiness only if those checks pass, then audit the bounded P1 result before any freshness or P2 cleanup work.
