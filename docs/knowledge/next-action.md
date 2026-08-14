# Next Action

## Current Status

`VERSIONED_AI_HANDOFF_READY`

Project Document Generator v1.14.0 now produces one versioned delivery package from the same accepted project truth:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

`prd.html` remains the human-facing PRD. `context.md` is the AI reasoning surface. `index.json` is a compact heading graph with exact context line ranges, so an AI can locate scope before reading prose. `output/README.md` is the stable resume entry point for a project reopened later.

The design intentionally has no Obsidian/Graphify dependency, knowledge database, second PRD authority, duplicate JSON prose, compatibility alias, or extra workflow layer.

Clockwork is migrated as the first real package at PRD version `1.0.0`; Voice remains semantically unchanged and points to the versioned project HTML.

## Next Step

Use the versioned delivery bundle as the default handoff on the next new or revised real PRD, and adjust only if that real usage exposes a concrete navigation/context defect.
