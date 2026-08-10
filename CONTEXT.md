# PRD-Creator Context

## Stable workspace facts

- `Local` is the permanent development/working authority.
- `main` changes only when explicitly requested.
- Repository state is authoritative for continuation; chat is supporting context.
- Production Flow remains 1–7: repository boot → source intake/recovery → PRD generation → PRD validation/handoff → Voice requirements → ElevenLabs performance script/DOCX → Voice validation/delivery.

## Current PRD direction

The PRD side is intentionally optimized for simple, high-quality production use rather than maximum process detail.

Core principles:

```text
source fidelity
→ production-relevant requirement recovery
→ decision-focused review
→ canonical PRD with minimum sufficient detail
→ approved HTML render
→ existing four-perspective development-readiness review
```

The active `project-document-production` skill includes PRD-specific anti-AI-slop writing guidance. It prefers plain, concrete technical prose and stable terminology while protecting IDs, names, numbers, timings, scoring, triggers, states, formulas, and other authoritative values.

Flow 2 does not mirror source text sentence-by-sentence into requirement IDs. The requirement register tracks production-relevant requirements, constraints, conflicts, and decisions. `work/review.md` remains a concise user-facing decision view rather than a duplicate register.

Flow 3 uses minimum sufficient detail. Optional sections/fields are not filled just because the template provides a place for them. Content stays when it helps a target role understand, build, implement, validate, or avoid guessing.

## Anti-overdevelopment boundary

BuildIT remains a reference for discipline, ownership, proof, and anti-slop behavior, not a feature checklist.

Do not add checksum/revision protocols, generic schema/profile frameworks, new root skills, extra gates, writing detectors/scores, test infrastructure, or similar machinery without a concrete current project need.

`No change required` is a valid result.

## Current verification boundary

Repository/Production Verify prove repository and executable consistency only. They do not prove subjective writing quality, browser visual quality, DOCX visual quality, or audio quality.

PRD writing/usability quality should be checked against a real project/sample when available, not via synthetic AI-writing scoring machinery.

## Current continuation

Read `docs/knowledge/next-action.md` for the single active next step.
