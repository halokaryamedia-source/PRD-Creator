# Next Action

## Current Status

`CURRENT_AUTHORITY_P0_COMPLETE`

The repository-quality audit performed against `Local` at `e5c1a483454937fc2be4512d4a8e172fcb227bd8` was explicitly promoted by the user from historical audit evidence into active development scope. The first bounded remediation, **P0 — Current Authority Integrity**, is now complete.

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

P0 corrected stale current authority/state without redesigning the product:

- current Voice owners use the versioned delivery/handoff paths;
- the existing repository guard covers those current Voice owners;
- Clockwork requirement state keeps only the current approved 04 design truth rather than several superseded redesigns;
- completed Flow 2 and handoff state no longer advertise executable next steps after Voice has already reached Flow 7;
- `state/voice-state.yaml` remains the furthest project-local continuation owner.

Do not reopen Golden PRD-core design, gameplay, renderer/compositor architecture, or unrelated repository governance as part of this completed P0.

For an observe-only new chat, recover context and report it without executing the recorded next step. For explicit Developing, use the normal continuity chain and start only from the boundary below.

## Last Completed

- Replaced retired `output/team-handoff.md` / `output/final.html` guidance in current Voice procedure with `output/README.md` plus the current versioned project bundle.
- Corrected the optional DOCX owner to point at `output/v<document.version>/prd.html` as the default human-facing project surface.
- Extended `CURRENT_DELIVERY_OWNER_PATHS` so the current Flow 5 and DOCX owners cannot silently regress to retired delivery paths.
- Removed superseded Clockwork Production Assets redesign requirements `REQ-017` through `REQ-023`; stable IDs were not renumbered and current approved `REQ-024` remains the final 04 design truth.
- Removed stale `next_step` fields from completed Clockwork Flow 2 and handoff state; current Flow 7 continuation remains unchanged.
- P0 made no gameplay, Golden, canonical PRD content, Production Asset source, Voice script, renderer/compositor, generated HTML, or DOCX changes.

## Deferred / Do Not Continue

- Do not broaden P1 into freshness hardening, parser frameworks, broad renderer refactors, dead-code cleanup, test-discovery work, atomic-write work, or other P2/P3 findings.
- Do not change fixed Golden counts, Golden bytes, or protected 01–03 behavior as maintenance.
- Do not create a generic schema/parser/compatibility framework to replace the bounded migrations already identified.
- Historical reviews, backlog items, and unrelated TODOs remain non-active unless current user intent or this file promotes them.

## Next Step

Begin only **P1 — Canonical 04/Voice Source Normalization**: migrate Clockwork `work/asset-requirements.md` to the current compact `PRODUCTION-ASSETS.md` contract, remove retired presentation metadata from `work/voice-requirements.md`, and change only the compositor dependencies that are proven necessary to stop relying on undocumented legacy fields or natural-language ordering heuristics; audit that bounded result before any freshness or cleanup work.
