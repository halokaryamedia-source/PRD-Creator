# Work Routing

This file is a compact human reference. Root `AGENTS.md` is the canonical work-mode and boot authority; do not duplicate its full procedure here.

## Mode map

| User intent | Mode | Primary route |
|---|---|---|
| Inspect, understand, decide, or recover context | Plan | current authority + smallest relevant owner |
| Create/revise project PRD or non-Voice 04 | Production Execution | `project-document-production` + exact PRD owner |
| Create/revise accepted Voice work | Production Execution | `voice-production` + exact Voice owner |
| Change PRD-Creator itself | Development | `development-brief` + first wrong owner |
| Fix bounded defect/regression/stale behavior | Maintenance | concrete failure + first wrong owner |

Production Flow and agent mode are separate layers. A Maintenance task can repair one Flow without replaying upstream production, and Development changes the system rather than producing a project.

## Owner rule

Route by what is wrong, not by file type:

```text
project/PRD meaning wrong
→ project-document-production / semantic owner

Voice meaning wrong
→ voice-production / semantic owner

meaning correct; renderer/template/validator behavior wrong
→ kits/prd-creator/AGENTS.md / exact implementation owner

shared dependency, test, or CI wrong
→ repository engineering owner
```

Use `ownership.md`, `source-authority.md`, or `skills/activation-matrix.md` only when the direct route remains genuinely ambiguous.

## Continuity

```text
current continuation → next-action.md
future/non-active work → operations/backlog.md
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
