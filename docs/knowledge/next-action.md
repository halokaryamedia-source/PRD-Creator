# Next Action

## Current Status

`WORKFLOW_NAMING_3_1_3_READY`

The active PRD-Creator workflow now uses one canonical human naming system across root routing, foundation policy, package owners, Project/PRD semantics, Production Assets, and Voice.

```text
Project Setup
→ Project Requirements
→ PRD Production
   └─ Production Assets when required
→ PRD Handoff
→ Voice Requirements when Voice is justified
→ Voice Production
→ Voice Delivery
```

Completed:

1. retired numbered `Flow N` terminology from current operating language;
2. retired `04` as a capability/process alias; the capability name is always Production Assets;
3. retained generated PRD section numbers only as visual document ordinals;
4. kept all machine statuses, IDs, SHA bindings, artifact paths, schemas, parsers, renderer identity, and lifecycle behavior unchanged;
5. kept Package 3.1.3 Voice preparation architecture intact: naturalness, Expression Coverage, actor continuity, pronunciation/language strategy, and candidate iteration;
6. aligned Project Requirements → PRD Production → Production Assets → PRD Handoff ownership;
7. aligned Voice Requirements → Voice Production → Voice Delivery ownership;
8. added repository verification protection against reintroducing legacy numbered stage names in current policy surfaces.

## Active Boundary

Keep current work on `develop`.

- Package version remains **3.1.3** because this is a naming/clarity cleanup with no machine-contract change.
- `work/voice-production.md` remains the sole canonical Voice wording/performance source.
- `work/asset-requirements.md` remains the canonical non-Voice Production Assets source when required.
- `handoff_ready`, `voice_requirements_ready`, `voice_script_ready`, and `voice_delivery_ready` remain machine lifecycle states, not human workflow names.
- Owner ID / Moment ID / AST / VO identity remains unchanged.
- Golden visual grammar remains unchanged.
- `Local` and `main` remain untouched until explicitly promoted.

## Next Step

Use the canonical workflow names above for all future project work. Do not add new aliases unless a real product boundary requires a genuinely different meaning.