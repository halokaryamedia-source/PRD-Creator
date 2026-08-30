# BuildIT Current Parity Gap Audit

Updated: 2026-08-10
Status: active execution evidence

## Compared Baselines

- BuildIT `Local`: `e4330f769486bcd0cee96d76fbce10f694cba2ba`
- PRD-Creator `Local` before this remediation: `4d2de64c46a2359508d4814834f4e42b774cd80f`

This audit compares **operating mechanisms**, not BuildIT's MCP/Blockbench domain content.

## Reassessment

The prior `OPERATING_PARITY_ACCEPTED` conclusion was too broad. PRD-Creator had reached strong parity for agent governance/routing, but not for the full relevant repository operating system.

The prior acceptance body remains historical evidence. This audit supersedes only its **overall parity conclusion**.

## What Is Already Strong

- repository-first memory and deterministic boot;
- Plan / Developing / Maintenance separation;
- mandatory non-trivial `development-brief`;
- goal vs suggested-method separation;
- Build POV + Acceptance POV;
- at most one semantic specialist;
- root-cause-first Maintenance;
- module/source/implementation routing;
- review graph and historical-evidence integrity;
- one active `next-action.md`;
- static `Repository Verify` gate;
- production Flow 2→7 real-project proof.

## Material Gaps

### P0 — Production engineering enforcement

BuildIT's current MCP gate executes a frozen dependency install, typecheck, focused contract tests, production build, generated-doc freshness, and a fail-closed aggregator.

PRD-Creator before this slice had only structural/link/skill/Python-syntax verification. It had no committed focused contract test suite and no locked dependency environment.

Required correction:

- exact dependency lock for the executable Voice path;
- focused PRD renderer/validator regression;
- focused Voice builder/validator regression;
- real CLI execution in GitHub Actions;
- fail-closed aggregate result.

### P0.2 — Technical ownership refinement

PRD-Creator currently has two broad product specialists after `development-brief`:

- `project-document-production` absorbs source/PRD semantics plus renderer/validator;
- `voice-production` absorbs Voice semantics plus DOCX builder/validator.

BuildIT separates product/domain judgement from technical/toolchain owners when the proved cause is technical. The current three-skill freeze must therefore be **audited**, not automatically expanded. A new skill is justified only if repeated work proves a distinct reusable owner.

### P1 — Production engineering quality audit

BuildIT routinely turns deep quality audits into ordered remediation plans. PRD-Creator still lacks an equivalent deep audit of its renderer, validators, builder, dependency/fixture contracts, and generated-artifact failure modes.

### P1.5 — Module governance depth

BuildIT's complex executable module has nearest `AGENTS.md` rules covering structure, commands, build/test contracts, generated outputs, coding constraints, and proof boundaries. PRD-Creator local agent files are still mostly routing/authority notes.

### P2 — Knowledge/operations maturity

Still thinner than BuildIT:

- operations index/role contract;
- roadmap separate from task board and next action;
- meaningful knowledge change log;
- trigger-based broad documentation audit;
- repository-wide glossary;
- optional actual Obsidian vault ergonomics.

### P3 — Conditional helper routing

BuildIT explicitly routes optional external/global helpers such as diagnosis, test-first work, independent review, research, domain modelling, codebase design, and skill authoring. PRD-Creator currently expresses these only generically.

## Not Gaps

Do not copy BuildIT's domain-specific surfaces merely for structural similarity:

- MCP/Blockbench/Bedrock skills and source layout;
- TypeScript/Bun names as such;
- MCP generated API documentation;
- Blockbench runtime/security rules;
- CodeRabbit/Claude/issue-template files without a PRD-Creator need.

## Current Decision

Overall relevant BuildIT parity is **reopened**.

Agent-governance/routing acceptance remains useful evidence, but full parity is not current truth until the material engineering/module/operations gaps above are addressed and re-audited.

Ordered remediation is owned by:

`../operations/buildit-parity-remediation-plan.md`
