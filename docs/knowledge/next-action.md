# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Current Status

`PRD_CONTENT_USABILITY_REFINED_REAL_SAMPLE_REVIEW_NEXT`

Working branch: **`Local` only**.

## Completed — PRD writing quality refinement

Source:

`a1c59f45c52d4213adff41a236ae0265dcf91868` — `docs: improve PRD writing quality rules`

The useful Humanizer-style behavior was merged into the existing PRD owner instead of adding another root skill.

## Completed — PRD content/usability refinement

Source:

`2c8cc015ec5d544d2899f554b9a4b9378d221456` — `docs: simplify PRD intake and content density`

Final integration:

`3841c21e4ec723acc3664723bad585ce44d5c7b7` — `docs: finalize PRD usability integration`

The remaining PRD review found three real usability gaps and fixed them without adding a new skill, workflow, validator, or framework:

- Flow 2 requirement granularity now tracks production-relevant requirements, constraints, conflicts, and decisions instead of mirroring every source sentence/fact into `REQ-###` entries;
- `work/review.md` is explicitly decision-focused, so detailed traceability stays in the requirement register while the user sees confirmed scope, meaningful completion/clarification, and only Proposal/Blocked items that need attention;
- Flow 3 uses minimum sufficient detail: include content when it helps a role understand, build, implement, validate, or avoid guessing; do not fill optional fields/sections merely because the template has a place for them.

Changed owners:

```text
.agents/skills/project-document-production/SKILL.md
kits/project-document-generator/SOURCE-INTAKE.md
kits/project-document-generator/CONTENT-CONTRACT.md
```

No renderer, validator, CI, schema, new root skill, or additional persistent project state was added.

## Current quality boundary

The PRD skill now explicitly protects:

- source fidelity and supported completion;
- decision economy during intake;
- production-relevant requirement granularity;
- context before detail;
- Gameplay / Level Design / Developer ownership separation;
- minimum sufficient detail and information density;
- plain, concrete, non-promotional technical prose;
- stable terminology and technical values;
- development-readiness from the existing four Flow 4 perspectives.

## Current limitation

`workspace/active/` and `workspace/saved/` currently contain no real PRD project package to use as a before/after quality sample.

Do not create synthetic prose/usability scoring or detector machinery to fill this gap.

## Current direction

PRD policy/skill refinement is complete enough to stop adding rules speculatively.

Voice skill review remains intentionally deferred until the PRD side is checked against a real project/sample or the user explicitly chooses to proceed.

Continue using the anti-overdevelopment rule:

```text
real source/project
→ use current PRD flow
→ observe actual friction or quality gap
→ smallest owner/fix only when needed
```

## Next Step

Use the refined PRD skill on one real PRD/project sample and review the actual result for clarity, completeness, information density, and role usability. If the result is good, do not add more PRD machinery; move on to the Voice skill review only after that practical check or explicit user direction.
