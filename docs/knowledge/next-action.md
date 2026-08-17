# Next Action

## Current Status

`P2_F15_RETIRED_VOICE_HELPER_CSS_COMPLETE`

P0 Current Authority Integrity and both bounded P1 remediations remain complete. P2 Mechanical Cleanup has started with one reproduced defect only: the F15 retired Voice helper/CSS residue.

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

F15 reproduced on current `Local` before this cleanup:

- `production_assets.py` still contained retired `_section_speakers()`, `_section_setup_html()`, and `_entry_html()` compositor helpers with no production caller;
- `tests/test_prd_voice_assets.py` explicitly required `_section_setup_html()` and `_entry_html()` to remain;
- the `VOICE_STYLE` payload still carried the old Voice dashboard/card/setup selector set even though current 04 rendering is owned by `production_assets_objective.py`.

The bounded cleanup now:

- removes the unused retired helper functions and their now-unused imports;
- keeps the current Voice parsing/presentation primitives used by the objective-first compositor;
- reduces `VOICE_STYLE` to only the four shared rules still consumed by current 04 output: Production Assets nav wrapping plus performance-cue grouping;
- updates the regression test so retired compositor helpers must stay absent while current primitives remain present;
- proves generated Voice pages contain no retired `voice-script-card` or `voice-page-setup` markup.

No Golden bytes, protected 01–03 behavior, gameplay, Production Asset resource meaning, Voice wording, Voice state, handoff state, or generated Clockwork bundle changed. This is source-only mechanical cleanup; the next normal render uses the reduced CSS payload.

The existing legacy `VOICE_COPY_SCRIPT` remains a separate small residue because current objective code still references it. It is not bundled into this F15 helper/CSS delivery.

## Proof

- `tests.test_prd_voice_assets`: PASS (`12/12`);
- Project Document contract/content/delivery regressions exercised for the changed renderer boundary: PASS;
- handoff / Flow 2 / hierarchy / Golden regressions: PASS (`20/20` final batch);
- repository verification: PASS;
- protected-core additive 04 regression remains PASS.

## Deferred / Do Not Continue

- Do not bundle F16 parser consolidation into this delivery.
- Do not refactor `_engine.STORAGE_PREFIX_TOKEN` or other conditional concurrency/reentrancy concerns without a reproduced failure.
- Do not add test-discovery, atomic-write, generic parser/schema, registry, manifest, or workflow frameworks.
- Do not clean `.regen-transfer`, supersession history, DOCX, unrelated CSS, or dense functions merely for aesthetics.
- Do not change Golden bytes, gameplay, Voice wording, or evidence/readiness claims.

## Next Step

Continue only **P2 — smallest remaining mechanical residue triage**: first verify whether the legacy `VOICE_COPY_SCRIPT` is truly unreferenced by current generated controls; remove it only if current `data-pa-copy` handling fully replaces it. If that closes cleanly, then re-check F16 parser duplication and consolidate only when one tiny existing-owner parser produces a real net simplification.
