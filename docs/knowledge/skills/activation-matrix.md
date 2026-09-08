# Skill Activation Matrix

Use only when root `AGENTS.md` plus the nearest obvious owner still leave the semantic/technical boundary ambiguous. Do not load this file by default.

Root `AGENTS.md` owns work-mode routing and skill budget. This note answers only whether a root semantic specialist adds judgment.

## Activation

| Actual problem | Add specialist? |
|---|---|
| Source recovery, PRD-core meaning, non-Voice 04 meaning, PRD readiness/handoff meaning | `project-document-production` |
| Voice scope, communication intent, wording/performance meaning, Voice readiness/delivery meaning | `voice-production` |
| Semantics correct; renderer/template/validator/compositor/CLI mechanics wrong | No → `kits/prd-creator/AGENTS.md` |
| Shared dependency/test/CI mechanics wrong | No → repository engineering |

Do not select a semantic specialist merely because HTML, Python, ElevenLabs, renderer, validator, or another implementation technology appears in the task.

For non-trivial repository/system Development, `development-brief` remains the front door. Add at most one semantic specialist when it materially changes the judgment. Normal Production Execution and bounded Maintenance do not load `development-brief` merely because tools or generated files are involved.

## Ambiguity test

Ask only:

1. What exact contract is wrong?
2. Is the defect about meaning or executable mechanics?
3. Which owner would still own it if the file format/language changed?
4. Does a root specialist add judgment beyond root policy + nearest owner?

If the owner is obvious, stop here and route directly.

## Root skill set

```text
.agents/skills/development-brief
.agents/skills/project-document-production
.agents/skills/voice-production
```

Do not add/split/rename a root skill unless repeated work proves a distinct reusable semantic ownership gap that existing root policy, package procedure, repository engineering, and current specialists cannot represent cleanly.
