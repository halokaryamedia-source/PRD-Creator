# Skill Activation Matrix

Use this note only to choose the **smallest correct owner**. A correct owner may be a root semantic specialist, a nearest kit implementation owner, or the repository-engineering layer. Detailed production procedure lives in the affected `SKILL.md` / kit; proof/evidence/anti-slop behavior lives in root `AGENTS.md`.

## Default Budget

| Mode | Default |
|---|---|
| Plan | no repository skill by default; inspect owners and decide before editing |
| Developing | mandatory `development-brief` + **at most one** specialist |
| Maintenance | root-cause-first; a root specialist is optional and used only when its semantic procedure adds material value |

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

## Canonical Semantic Specialist Routing

| Primary semantic/product contract | Skill | Trigger examples | Do not select merely because… |
|---|---|---|---|
| Source → requirements → canonical PRD → PRD acceptance/handoff | `project-document-production` | Flow 2 recovery, canonical PRD meaning, what render projection/pages must represent, approved-template product contract, readiness/handoff semantics | task contains HTML/JSON/Markdown/Python or a renderer/validator file fails mechanically |
| Accepted PRD → Voice requirements → performance wording/artifact contract → Voice acceptance/delivery | `voice-production` | Flow 5 Voice scope, Voice ID/Type contract, performance wording, what DOCX must represent, delivery/evidence semantics | task mentions ElevenLabs/DOCX/audio/Python or builder/validator mechanics fail |

Canonical paths:

```text
.agents/skills/development-brief/SKILL.md
.agents/skills/project-document-production/SKILL.md
.agents/skills/voice-production/SKILL.md
```

## Semantic vs Technical Boundary Resolution

Choose by the **proved first wrong contract**, not by the filename.

```text
source authority / recovered requirement / canonical PRD meaning wrong
→ project-document-production

PRD meaning is correct but what pages/data are supposed to represent is wrong
→ project-document-production

PRD semantic contract is correct, renderer/template/validator mechanics are wrong
→ kits/project-document-generator/AGENTS.md
→ exact renderer/template/validator owner
→ no root specialist required by default

accepted PRD is correct but Voice moment scope/ID/Type/speaker/channel/trigger is wrong
→ voice-production

Voice scope is correct but final spoken/performance wording is wrong
→ voice-production

Voice semantics/artifact contract is correct, DOCX builder/validator mechanics are wrong
→ kits/voice-production-kit/AGENTS.md
→ exact builder/validator owner
→ no root specialist required by default

shared dependency / contract-test / CI behavior is wrong
→ requirements.lock.txt / tests/ / tools/ / .github/workflows/
→ no production specialist required by default
```

If investigation exposes both semantic and mechanical defects, finish/reframe them as separate boundaries rather than stacking specialists.

## Technical Maintenance Is Not A Root Skill By Default

P0.2 audited a possible `production-tooling` / `artifact-engineering` / Python specialist and rejected it as a root skill for the current repository.

Current rule:

- PRD renderer/template/validator mechanics stay module-local;
- Voice builder/validator mechanics stay module-local;
- shared dependency/test/CI behavior stays repository-engineering owned;
- a root semantic specialist is used only when the semantic/product contract itself is wrong or materially uncertain.

Do not create root skills named after implementation surfaces such as:

```text
renderer
html-validator
docx-builder
voice-validator
python-tooling
artifact-engineering
research
evidence-gate
```

A future technical specialist requires repeated evidence of one distinct reusable technical contract/procedure that is not represented cleanly by nearest module owners or repository engineering.

## Production Kits Are Not Root Specialists

`kits/project-document-generator/SKILL.md` and `kits/voice-production-kit/SKILL.md` remain detailed production procedures.

Nearest kit `AGENTS.md` files own scoped contributor/verification rules and pure technical Maintenance routing inside their modules.

Root `.agents/skills/` controls reusable semantic work framing/judgment; it is not a catalog of every executable implementation surface.

## Repository Engineering Owner

Current repository-wide executable engineering owners:

```text
requirements.lock.txt
tests/
tools/verify_repository.py
.github/workflows/repository-verify.yml
.github/workflows/production-verify.yml
```

They own repeatable dependency, regression, static repository, and CI contracts. They do not own project semantics or visual/audio acceptance.

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
- diagnostic/test-first workflow when a regression boundary genuinely benefits from it.

Do not copy generic helper skills into this repository solely to increase skill count.

## Location And Freeze Rule

- `.agents/skills/` is the only canonical repository-wide skill root.
- Production kit `SKILL.md` files remain inside their kits; they are not alternate root skill directories.
- P0.2 re-audited the three-skill set after executable production verification and **kept** it.
- The freeze applies to root reusable semantic specialists, not to module-local implementation ownership.
- Do not rename, merge, split, duplicate, or add another repository skill unless current repeated work proves a distinct reusable ownership gap that cannot be represented by root policy, foundation policy, nearest kit procedure/AGENTS, repository engineering, or one existing specialist.

## Skill Audit Rule

For a proposed capability/skill decide one of:

```text
KEEP    → clear unique reusable function
RENAME  → useful function, misleading owner/name
MERGE   → useful behavior overlaps an existing owner
MOVE    → useful behavior belongs in foundation/kit/operations/repository engineering instead of a skill
DROP    → no distinct value after existing owners
RECOVER → trusted historical behavior is missing from the current canonical owner
```

A useful capability does **not** automatically become a root skill.

## Final Routing Check

Before loading a specialist ask:

```text
What exact meaning/behavior/contract is wrong?
Is the failure semantic/product-contract or executable mechanics?
Which owner would still be responsible if the implementation language/file format changed?
Does the specialist add reusable semantic procedure beyond AGENTS + nearest module rules?
Can Maintenance reach the exact implementation owner without loading a root specialist?
```

If no specialist adds material value, use `development-brief` alone for Developing or direct root-cause Maintenance for repairs.
