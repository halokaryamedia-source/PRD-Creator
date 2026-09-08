# Work Routing

Compact human reference only. Root `AGENTS.md` is the canonical work-mode, boot, authority, and skill-budget owner. Use this file only when a short routing reminder is useful.

## Mode map

| User intent | Mode | Primary route |
|---|---|---|
| Inspect, understand, decide, or recover context | Plan | current authority + smallest relevant owner |
| Create/revise project PRD or non-Voice 04 | Production Execution | smallest PRD owner; add `project-document-production` only when semantic judgment is needed |
| Create/revise accepted Voice work | Production Execution | smallest Voice owner; add `voice-production` only when semantic/performance judgment is needed |
| Change PRD-Creator itself | Development | `development-brief` + first wrong owner |
| Fix bounded defect/regression/stale behavior | Maintenance | concrete failure or explicit target + first wrong owner |

Production Flow and agent mode are separate layers. Bounded work does not replay the full production stack unless the change invalidates it.

## Owner rule

Route by what is wrong, not by file type:

```text
project / PRD meaning wrong
→ project-document-production + nearest semantic owner

Voice meaning / communication contract wrong
→ voice-production + nearest Voice semantic owner

meaning correct; renderer / template / validator / CLI behavior wrong
→ kits/prd-creator/AGENTS.md → exact implementation owner

shared dependency / test / CI wrong
→ repository engineering owner
```

If the owner is already obvious, use it directly. Consult `ownership.md`, `source-authority.md`, or `skills/activation-matrix.md` only when the direct route remains genuinely ambiguous.

## Continuity

```text
current continuation → next-action.md
future / non-active work → operations/backlog.md
historical evidence → reviews/history/
durable rationale → decisions/
```

Historical TODOs, reviews, and backlog items do not become active work unless current user intent or current continuation promotes them.

## Related

- [Development Workflow](work-modes/development.md)
- [Maintenance Workflow](work-modes/maintenance.md)
- [Skill Activation Matrix](skills/activation-matrix.md)
- [Repository Ownership](ownership.md)
- [Source Authority](source-authority.md)
