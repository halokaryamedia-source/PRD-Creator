# Skill Activation Matrix

Use this file **only when the correct semantic/technical owner remains ambiguous** after root `AGENTS.md` and the nearest obvious owner are considered. Do not load it by default.

Root `AGENTS.md` owns work-mode routing and skill budget. This matrix only resolves **which specialist, if any, adds reusable semantic judgment**.

## Semantic vs technical boundary

| Wrong contract | Route |
|---|---|
| Source recovery, PRD-core meaning, non-Voice 04 requirement meaning, Golden representation requirement, PRD readiness/handoff meaning | `project-document-production` |
| Voice scope, Speaker/Channel/Trigger/Purpose meaning, canonical Voice wording/performance meaning, Voice readiness/delivery meaning | `voice-production` |
| PRD/04 semantics correct; renderer/template/PRD-validator/compositor mechanics wrong | `kits/prd-creator/AGENTS.md` → exact Project/PRD implementation owner |
| Voice semantics correct; Voice validator/project-HTML integration mechanics wrong | `kits/prd-creator/AGENTS.md` → exact Voice/shared implementation owner |
| Shared dependency / test / CI mechanics wrong | repository engineering owner |

Do **not** select a semantic specialist merely because HTML, Python, ElevenLabs, renderer, validator, or another implementation technology appears in the task.

## Development front door

For non-trivial repository/system Development:

```text
development-brief
+ at most one semantic specialist when it materially helps
```

Normal project Production Execution does not use `development-brief`.

Maintenance begins root-cause-first; a root specialist is optional when the semantic contract is already correct.

## Current root skill set

```text
.agents/skills/development-brief
.agents/skills/project-document-production
.agents/skills/voice-production
```

`kits/prd-creator/SKILL.md` and `kits/prd-creator/AGENTS.md` are detailed production/contributor procedure and module routing, not alternate root specialists.

## Ambiguity questions

Before loading a specialist ask:

1. Is the user using the existing product, changing PRD-Creator itself, or repairing a concrete defect?
2. What exact contract is wrong?
3. Is the defect about product/semantic meaning or executable mechanics?
4. Which owner would still own the problem if the file format/language changed?
5. Does a specialist add judgment beyond root policy + nearest module rules?

If the owner is already obvious, stop here and use it directly.

## New-skill guard

Do not add renderer, validator, Production Asset, Python-tooling, artifact-engineering, research, or evidence-gate root skills merely because those surfaces exist.

A new/split/renamed root skill requires repeated evidence of a distinct reusable semantic ownership/procedure gap that cannot be represented by root policy, foundation policy, `kits/prd-creator/` procedure/AGENTS, repository engineering, or one existing specialist.
