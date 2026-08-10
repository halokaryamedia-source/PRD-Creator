# Skill Activation Matrix

Use this file **only when the correct owner is ambiguous**. If root `AGENTS.md`, current project state, or nearest kit owner already resolves the task, do not load this matrix.

## Default budget

| Mode | Default owner budget |
|---|---|
| Plan | no specialist by default |
| Production Execution | one matching production specialist + smallest active kit procedure |
| Developing | `development-brief` + at most one useful specialist |
| Maintenance | root-cause-first; specialist optional |

Do not select skills by file format or implementation language.

## Fast routing

```text
create/revise PRD with existing system
→ Production Execution
→ project-document-production
→ Project Document Generator active Flow owner

create/revise Voice output from accepted PRD
→ Production Execution
→ voice-production
→ Voice Production active Flow owner

change PRD-Creator policy/workflow/skills/renderer/validator/builder/repository mechanics
→ Developing
→ development-brief
→ add one semantic specialist only if it materially helps

bug/regression/cleanup/stale docs
→ Maintenance
→ first wrong owner
```

## Semantic specialist routing

| Wrong semantic/product contract | Owner |
|---|---|
| source recovery, canonical PRD meaning, Golden representation requirement, PRD readiness/handoff meaning | `project-document-production` |
| Voice requirement scope, Voice ID/Type/speaker/channel/trigger meaning, performance wording, Voice delivery meaning | `voice-production` |

Do **not** load those skills merely because HTML/Python/DOCX/ElevenLabs appears in the task.

## Semantic vs technical boundary

```text
PRD meaning/representation requirement wrong
→ project-document-production

PRD semantic contract correct; renderer/template/validator mechanics wrong
→ kits/project-document-generator/AGENTS.md
→ exact implementation owner

Voice meaning/artifact contract wrong
→ voice-production

Voice semantic contract correct; DOCX builder/validator mechanics wrong
→ kits/voice-production-kit/AGENTS.md
→ exact implementation owner

shared dependency / test / CI wrong
→ requirements.lock.txt / tests / tools / workflows
```

If both semantic and mechanical defects exist, resolve/reframe them as separate boundaries instead of stacking specialists.

## Developing front door

`development-brief` is required for non-trivial repository/system Developing. It establishes goal vs method, authority, Build/Acceptance POV, minimal scope, 2–5 acceptance criteria, and proof budget.

It does **not** apply to normal Flow 2–7 project production.

## Root skill set

```text
.agents/skills/development-brief
.agents/skills/project-document-production
.agents/skills/voice-production
```

Production kit `SKILL.md` files are procedures, not alternate root specialists. Nearest kit `AGENTS.md` files own module mechanics/technical Maintenance.

Do not add renderer, HTML-validator, DOCX-builder, Python-tooling, artifact-engineering, research, or evidence-gate root skills without repeated evidence of a distinct reusable semantic ownership gap.

## Final ambiguity check

Before loading a specialist ask:

1. Is this normal project production or a change to PRD-Creator?
2. What exact contract is wrong?
3. Is it semantic/product meaning or executable mechanics?
4. Which owner would still own the problem if the file format/language changed?
5. Does a specialist add useful reusable judgment beyond root policy + nearest module rules?

If the owner is already obvious, stop here and use that owner directly.
