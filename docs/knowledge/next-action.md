# Next Action

## Current Status

`P2_MECHANICAL_CLEANUP_COMPLETE`

P0 Current Authority Integrity and both bounded P1 remediations remain complete. P2 Mechanical Cleanup is complete after the reproduced Production Assets / Voice residue was removed and F16 duplicated parsing was re-triaged against the post-F15 implementation.

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

### F15 / legacy compositor residue

Closed in the previous bounded deliveries:

- retired Voice compositor helpers removed;
- legacy Voice dashboard/card/setup CSS removed;
- dead `data-voice-copy` JavaScript payload removed;
- current `data-pa-copy` / `OBJECTIVE_COPY_SCRIPT` remains the single active 04 copy path.

The intentionally empty `VOICE_COPY_SCRIPT` compatibility symbol/callsite remains harmless and should not receive a separate cleanup commit.

### F16 / duplicated Voice parsing

Re-check found that a cross-kit canonical parser is **not worthwhile** under the current contracts:

- the PRD renderer needs presentation data only: cast, section, Speaker, duration, and performance payload;
- the Voice validator additionally owns Type parity, revision identity, validation errors, project-HTML/DOCX gates, and stricter mechanical checks;
- the optional DOCX builder additionally owns document title/version/source metadata and export-specific structure;
- forcing those owners through one shared parser would add a cross-kit dependency/model and more moving parts than it removes.

One small residue was still objectively removable without introducing a shared parser: `production_assets.py` retained three field-specific Voice Requirement scanners for legacy `Trigger`, `Flow`, and `For` metadata. Repository reference inspection found no production caller; current objective-first rendering reads `Function` through its own bounded `_voice_requirement_meta()` owner. The three orphan scanners are removed.

No generic Markdown/parser framework was created. The remaining parser separation is intentional and recorded as **not worthwhile**, not as an open defect.

## Proof

- `tests.test_prd_voice_assets`: PASS (`12/12`);
- PRD core/content/delivery regression batch: PASS (`22/22`);
- Flow 2 / Golden / handoff / hierarchy regression batch: PASS (`20/20`);
- Repository Verify: PASS;
- current Voice `Function` rendering and missing-Function failure behavior remain covered by existing 04 regressions;
- protected-core additive 04 behavior remains PASS.

No Golden bytes, protected 01–03 behavior, gameplay, Production Asset resource meaning, Voice wording/performance, project state, acceptance result, or evidence/readiness claim changed.

## Deferred / Do Not Continue

- Do not create a shared/generic Markdown parser framework for renderer + validator + DOCX builder.
- Do not create a separate commit merely to remove the empty `VOICE_COPY_SCRIPT` compatibility symbol/callsite.
- Do not refactor `_engine.STORAGE_PREFIX_TOKEN` or other conditional concurrency/reentrancy concerns without a reproduced failure.
- Do not add test-discovery, atomic-write, registry, manifest, schema, or workflow frameworks without a concrete defect.
- Do not clean `.regen-transfer`, supersession history, DOCX internals, unrelated CSS, or dense functions merely for aesthetics.
- Do not change Golden bytes, gameplay, Voice wording, or evidence/readiness claims.

## Next Step

Stop automatic audit/cleanup work. Resume only from a new concrete user-approved product/document requirement or a reproduced defect; diagnose its first wrong owner and apply the smallest relevant fix rather than promoting deferred P3/theoretical cleanup.
