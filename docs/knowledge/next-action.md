# Next Action

## Current Status

`P1_3_VOICE_DOCX_PATH_RETIRED`

P0 Current Authority Integrity, the bounded P1 freshness/source remediations, and P2 mechanical cleanup remain complete. The historical P1.3 DOCX integrity branch has now been reconciled with the current product architecture by retiring DOCX instead of hardening an unused optional export.

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

Current Voice delivery has one canonical production source and one normal human-facing derived presentation:

```text
accepted PRD / handoff
→ work/voice-requirements.md
→ exact revision + SHA-bound work/voice-production.md
→ output/v<document.version>/prd.html → 04 Production Assets → AUDIO
→ work/voice-acceptance.md + state/voice-state.yaml
```

The former DOCX export was not referenced by the current Clockwork Voice state and was not required by the default Voice delivery gate. Keeping a builder, validator branch, dependency chain, tests, and documentation solely for that unused optional path added maintenance surface without current product value.

The retirement therefore removes the active DOCX path instead of implementing the historical DOCX per-entry hardening item:

- `kits/voice-production-kit/builder/build_docx.py` removed;
- `kits/voice-production-kit/DOCX-FORMAT.md` removed;
- Voice validator no longer imports `python-docx`, looks for `Voice Production.docx`, validates DOCX, or reports DOCX status;
- Voice regression coverage now validates the canonical Requirements → Script → project-HTML chain directly and preserves controlled empty-section failure without the retired builder;
- `python-docx` and its lock-only support dependencies are removed from the active verification environment;
- `kits/voice-production-kit/requirements.txt` is removed because the Voice kit has no current direct third-party Python dependency;
- current Flow/ownership/workspace/routing docs no longer advertise DOCX as a supported or optional delivery surface;
- repository verification records the former DOCX owner paths as retired boundaries so they do not silently return.

Historical CHANGELOG/review/audit evidence may still mention past DOCX work. Those files are historical evidence, not current routing or product authority, and are not rewritten merely to erase history.

No Golden bytes, protected PRD 01–03 behavior, gameplay, Voice requirements, canonical Voice wording/performance, Clockwork state, acceptance result, or current project HTML are changed by this retirement.

## Proof

- focused Voice validator regression: PASS (`12/12`) without `python-docx`;
- empty Voice section still fails in a controlled way through the current validator;
- current revision identity, Voice ID/Type/Speaker parity, Source Voice Requirements SHA binding, and project-HTML prompt parity remain covered;
- Voice/Repository CI must pass on the final `Local` delivery before this status is considered fully proven.

## Deferred / Do Not Continue

- Do not replace DOCX with another export format, PDF generator, portable-document framework, or second Voice HTML.
- Do not reintroduce `python-docx`, a DOCX builder, or DOCX validation without a new explicit product requirement.
- Do not rewrite historical audits/CHANGELOG entries solely because they record former DOCX evidence.
- Do not advance to P1.5 test-discovery or other historical TODOs automatically; the user explicitly limited this work to P1.3.
- Do not change Golden bytes, gameplay, Voice wording, or evidence/readiness claims.

## Next Step

Stop P1.3 after final Voice Verify and Repository Verify pass. Resume only from a new explicit user-approved requirement or reproduced defect; do not automatically continue to P1.5.
