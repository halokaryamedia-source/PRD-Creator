# Next Action

## Current Status

`P2_LEGACY_COPY_PAYLOAD_REMOVED`

P0 and both bounded P1 remediations remain complete. P2 has now closed the reproduced F15 retired Voice helper/CSS residue and the immediately adjacent legacy Voice copy-script payload without expanding into parser consolidation or broader cleanup.

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

The legacy Voice copy handler was re-checked against the current objective-first 04 compositor before changing code.

Current truth:

- current Voice and non-Voice copy buttons are emitted by `_copy_button()` as `data-pa-copy` controls;
- `OBJECTIVE_COPY_SCRIPT` is the active shared copy handler and listens to `[data-pa-copy]`;
- current objective-first rendering emits no `data-voice-copy` controls;
- the former `VOICE_COPY_SCRIPT` listened only to `[data-voice-copy]`, so its JavaScript payload was unreachable runtime code.

The bounded cleanup therefore removes the legacy JavaScript payload while keeping `VOICE_COPY_SCRIPT` as an intentionally empty compatibility symbol because the current objective compositor still appends that attribute. Do not spend a separate refactor solely deleting the empty symbol/callsite unless an already-needed change touches that owner.

Fresh-render proof from the current renderer boundary:

- current Voice prompt control is present as `data-pa-copy="voice-prompt-vo-intro-01"`;
- `production-assets-flow-copy-script` remains present;
- retired `production-assets-copy-script` is absent;
- retired `data-voice-copy` markup is absent;
- `tests.test_prd_voice_assets`: PASS (`12/12`);
- PRD contract/delivery/Golden regression batch: PASS (`23/23`);
- Repository Verify: PASS.

No Golden bytes, protected 01–03 behavior, gameplay, Production Asset meaning, Voice wording, readiness/evidence state, or accepted Clockwork source changed. The checked-in Clockwork HTML is not regenerated for this source-only runtime cleanup; the next normal render will omit the dead legacy payload.

## Deferred / Do Not Continue

- Do not create a separate commit merely to remove the empty `VOICE_COPY_SCRIPT` compatibility symbol/callsite.
- Do not refactor `_engine.STORAGE_PREFIX_TOKEN` or other conditional concurrency/reentrancy concerns without a reproduced failure.
- Do not add test-discovery, atomic-write, generic parser/schema, registry, manifest, or workflow frameworks.
- Do not clean `.regen-transfer`, supersession history, DOCX, unrelated CSS, or dense functions merely for aesthetics.
- Do not change Golden bytes, gameplay, Voice wording, or evidence/readiness claims.

## Next Step

Re-check only **P2 / F16 — duplicated Voice parsing** against the current post-F15 implementation. Consolidate only if one small existing-owner parser can replace duplicated parsing with fewer moving parts and unchanged contracts; otherwise record F16 as not worthwhile and stop P2 rather than inventing a parser framework.
