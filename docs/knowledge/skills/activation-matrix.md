# Skill Activation Matrix

Use this note only to choose the **smallest correct semantic owner**. Detailed production procedure lives in the selected root `SKILL.md` and affected kit; proof/evidence/anti-slop behavior lives in root `AGENTS.md`.

## Default Budget

| Mode | Default |
|---|---|
| Plan | no repository skill by default; inspect owners and decide before editing |
| Developing | mandatory `development-brief` + **at most one** specialist |
| Maintenance | root-cause-first; add the smallest owning specialist only when it adds material procedure |

Do not activate a skill merely because a file format or implementation technology appears in the task.

## Developing Front Door

Every non-trivial create/change task starts with:

`.agents/skills/development-brief/SKILL.md`

It owns:

- goal vs suggested-method separation;
- sample/reference vs generic-requirement separation;
- execution-channel detection;
- development necessity;
- input authority / expected output;
- Build POV and Acceptance POV;
- minimal scope;
- 2–5 acceptance criteria;
- proof budget;
- final contract re-check.

## Canonical Specialist Routing

| Primary semantic owner | Skill | Trigger examples | Do not select merely because… |
|---|---|---|---|
| Source → requirements → canonical PRD → PRD acceptance/handoff | `project-document-production` | Flow 2 intake/recovery, PRD structure/content, renderer/template contract, PRD validator, team handoff, PRD artifact defect | task contains HTML/JSON/Markdown or is called “documentation” |
| Accepted PRD → Voice requirements → performance script/DOCX → Voice acceptance/delivery | `voice-production` | Flow 5 extraction, narrator/dialogue scope, ElevenLabs performance wording, DOCX builder, Voice validator, delivery evidence | task mentions ElevenLabs, dialogue, DOCX, or audio |

Canonical paths:

```text
.agents/skills/development-brief/SKILL.md
.agents/skills/project-document-production/SKILL.md
.agents/skills/voice-production/SKILL.md
```

## Boundary Resolution

Choose by the **actual wrong contract/root owner**:

```text
source authority / recovered requirement / PRD meaning wrong
→ project-document-production

PRD meaning correct, HTML projection/rendering wrong
→ project-document-production

PRD accepted, Voice moment scope wrong
→ voice-production

Voice scope correct, final wording/performance wrong
→ voice-production

Canonical Voice script correct, DOCX builder/render wrong
→ voice-production

Acceptance evidence is wrong because upstream artifact is wrong
→ fix upstream semantic owner first; do not patch acceptance prose
```

Do not stack both specialists for one boundary. If investigation exposes a second independent issue, finish or explicitly reframe the first before switching owner.

## Production Kits Are Not Root Specialists

`kits/project-document-generator/SKILL.md` and `kits/voice-production-kit/SKILL.md` remain the detailed production procedures.

Root `.agents/skills/` controls **how the agent frames, routes, owns, and validates repository work**. It does not duplicate every Flow instruction.

## Renderer / Validator / DOCX Are Not Separate Skills

Do not create root skills named after implementation surfaces such as:

```text
renderer
html-validator
docx-builder
voice-validator
research
evidence-gate
```

A renderer defect belongs to the semantic product owner whose output it derives. Evidence classification is root behavior, not another specialist slot.

## Evidence Is Not A Skill

Material uncertainty uses root `AGENTS.md` labels:

- `CURRENT-PROJECT VERIFIED`;
- `AUTHORITATIVE-SOURCE VERIFIED`;
- `LOCAL PROOF REQUIRED`;
- `UNSUPPORTED`;
- `UNKNOWN`.

This does not consume the specialist slot and should not be applied ceremonially to routine work.

## Conditional Helpers

External/global/user helpers may be used only when actually available and when their distinct function is needed, for example:

- focused discovery for unresolved high-impact requirements;
- adversarial critique before a major decision;
- independent code/content review after implementation;
- primary-source research when public/current facts materially affect the result;
- test-first workflow when a regression boundary genuinely benefits from it.

Do not copy generic helper skills into this repository solely to increase skill count.

## Location And Freeze Rule

- `.agents/skills/` is the only canonical repository-wide skill root.
- Production kit `SKILL.md` files remain inside their kits; they are not alternate root skill directories.
- Current root skill set is frozen after this Phase 1 consolidation.
- Do not rename, merge, split, duplicate, or add another repository skill unless current work proves a distinct reusable ownership gap that cannot be represented by root policy, foundation policy, a kit procedure, or one existing specialist.

## Skill Audit Rule

For a proposed capability/skill decide one of:

```text
KEEP    → clear unique reusable function
RENAME  → useful function, misleading owner/name
MERGE   → useful behavior overlaps an existing owner
MOVE    → useful behavior belongs in foundation/kit/operations instead of a skill
DROP    → no distinct value after existing owners
RECOVER → trusted historical behavior is missing from the current canonical owner
```

A useful capability does **not** automatically become a root skill.

## Final Routing Check

Before loading a specialist ask:

```text
What exact meaning/behavior/contract is wrong?
Which owner would still be responsible if the file format/tool changed?
Does the specialist add domain procedure beyond AGENTS + development-brief?
Can one specialist cover this boundary without stacking?
```

If no specialist adds material value, use `development-brief` alone.
