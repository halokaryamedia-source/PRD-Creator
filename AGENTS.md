# Workspace Agent Routing

This repository is project memory. Chat history is useful context, but it is never the authority for current project state.

## Branch Policy

- `Local` is the permanent working/development authority.
- Perform normal implementation/documentation work directly on `Local`.
- Do not create per-task/per-flow branches or routine pull requests.
- `main` remains stable and changes only when the user explicitly requests it.
- Older non-`Local` branches are non-authoritative unless explicitly reactivated.

## Mandatory Boot

At the start of every material PRD-Creator session:

1. read `CONTEXT.md` for stable facts and product boundaries;
2. read `docs/knowledge/next-action.md` for the single active task/state;
3. read only the relevant `docs/foundation/` rule or affected source/kit;
4. read `docs/knowledge/skills/activation-matrix.md` only when selecting a workflow/skill;
5. use `docs/knowledge/minimal-nav.md` when ownership is unclear.

Do not broad-scan saved projects, all references, generated output, review history, or retired Git history by default.

## Session Continuity

A new session must resume from repository state before asking the user to reconstruct prior work.

- `CONTEXT.md` owns stable workspace facts and terminology.
- `docs/knowledge/next-action.md` owns the current goal, status, blockers, completed boundary, and one next step.
- `docs/knowledge/decision-log.md` owns durable decisions and reasons.
- `docs/foundation/` owns durable production policy.
- `docs/knowledge/modules/module-map.md` owns repository-area responsibility routing.
- `docs/knowledge/sources/source-map.md` owns authority/source routing.
- `docs/knowledge/implementation-map.md` owns exact current implementation/procedure routing.
- `docs/knowledge/reviews/review-graph.md` owns the current meaning of historical reviews/evidence.
- affected kit/source + relevant proof own actual behavior.

Before ending material work, update only the canonical owner whose state actually changed.

If current user instruction conflicts with stored state, current user intent wins for the task, but reconcile the conflict explicitly instead of silently rewriting history.

## Mode Selection

Infer the work mode from intent:

- unclear problem, architecture question, or pre-implementation decision → **Plan**;
- create/change/extend request → **Developing**;
- bug, regression, review, cleanup, stale docs, or behavior-preserving correction → **Maintenance**.

The user may explicitly override the mode. If editing is risky and the mode is genuinely unclear, use Plan first.

## Prompt Assistance

The user's prompt defines intent; it does not need to be a complete production specification.

Before asking for more information:

1. inspect repository/project sources for discoverable facts;
2. preserve already-authoritative decisions;
3. separate the real goal from a suggested method;
4. distinguish a sample/reference from a generic requirement;
5. complete low-risk gaps only when current Flow policy permits it;
6. ask only unresolved high-impact decisions that materially change the result;
7. persist the resolved decision in its existing owner.

Do not force a user to restate context the repository already owns.

## Independent Judgment

The user owns the **goal**. The agent is responsible for the quality and safety of the **method**.

Do not agree with a proposed method merely because it was requested. Reject or redirect a method when current evidence shows that it:

- contradicts authoritative project decisions;
- repeats a disproven approach;
- invents unsupported project behavior;
- damages downstream usability;
- bypasses the owning Flow;
- adds disproportionate complexity or parallel architecture.

When rejecting a method:

1. state the concrete reason;
2. identify the project rule/evidence behind it;
3. recommend the smallest supported path that still serves the goal.

Do not challenge harmless preferences or equally valid choices.

## Source Precedence

Use the matching authority for the claim:

1. current explicit user instruction for task intent;
2. approved project-specific decisions;
3. authoritative project source;
4. normalized requirement state;
5. accepted canonical PRD;
6. accepted Voice Requirements;
7. canonical Voice Production Script for spoken/performance wording only;
8. durable workspace/foundation policy;
9. active kit procedure;
10. approved sample/reference for demonstrated structure/quality only;
11. generated output/chat/history as supporting context only.

Material conflicts are `UNKNOWN` until reconciled; never choose silently.

Use `docs/knowledge/sources/source-map.md` when the correct source/authority is unclear.

## Developing Front Door

Every non-trivial Developing task uses:

`.agents/skills/development-brief/SKILL.md`

`development-brief` must establish the smallest grounded contract before implementation:

- real goal vs suggested method;
- observed sample/fixture vs generic requirement;
- execution channel;
- input authority;
- expected output;
- Build POV and Acceptance POV;
- interface constraints;
- in-scope / out-of-scope boundary;
- 2–5 provable acceptance criteria;
- minimum useful proof budget;
- unresolved high-impact decisions.

A trivial, unambiguous change may use its fast path, but the same goal/scope/proof gate still applies.

After the brief, add **at most one** repository specialist when it provides real domain procedure.

## Mode Skill Budget

- **Plan:** repository-grounded analysis first; use no repository specialist by default.
- **Developing:** mandatory `development-brief` + at most one specialist.
- **Maintenance:** diagnose the concrete failure first; use the smallest owning specialist only when its procedure adds material value.

Do not stack specialists merely because a task touches several file types or implementation surfaces.

Detailed routing lives in `docs/knowledge/skills/activation-matrix.md`.

Maintenance procedure lives in `docs/knowledge/maintenance/maintenance-flow.md`.

## Execution Channels

### ChatGPT → GitHub

Repository reads/writes and static artifact inspection may be available. Do not assume arbitrary local runtime, browser, audio generation, or external application execution.

Static repository work may prepare a runtime change. If a material claim requires local/browser/audio/runtime proof that is unavailable, report the exact remaining proof instead of inventing a substitute.

### Local / Codex-style execution

Local shell/build/render/runtime capabilities may be available. Verify availability before relying on them. Run only checks that materially test the changed boundary.

The goal, scope, authority, Acceptance POV, and criteria do not change between channels; only available proof changes.

## Root-Cause And Edit Gate

Before changing behavior, establish:

- what actually happens;
- which owner/cause is responsible;
- why the proposed change addresses that cause;
- what proof could falsify the change.

If the cause/contract remains unknown, do not patch around it. Report `Perlu pemeriksaan` or `Terhenti` with the missing evidence.

Before creating or moving a file:

- search current owners/helpers/tests/docs first;
- use `docs/knowledge/modules/module-map.md` when repository-area ownership is unclear;
- reuse or extend before creating;
- create only when the canonical owner is clear and the file is required now;
- do not create README/index/schema/config/fallback/abstraction for hypothetical future use;
- keep source, state, canonical work, derived data, evidence, and final output separate.

`No change required` is a valid result.

## Sample / Reference Rule

A sample demonstrates structure, presentation, density, tone, or quality only to the extent explicitly defined by its owner.

Do not promote sample-specific objective counts, characters, mechanics, scoring, voice counts, durations, speakers, channels, tags, lines, or pronunciation into generic policy.

## Review Evidence Rule

A review/audit is evidence captured at a point in time. It is not automatically current policy or task state.

- review bodies preserve what was observed/reasoned at capture time;
- `docs/knowledge/reviews/review-graph.md` owns the **current meaning** of historical reviews;
- durable choices move into `decision-log.md` / `decisions/`;
- active work order remains in `next-action.md`;
- do not rewrite old review bodies merely so they appear current after implementation.

Create a dedicated review only when it adds durable evidence beyond an ordinary task diff/validation note.

## Durable Decision / Cross-Owner Change Rule

Use `docs/knowledge/decisions/change-decision-guide.md` to decide whether a choice belongs in the decision log, a dedicated decision note, review evidence, next-action, or task board.

Do not create a formal cross-owner change plan for ordinary bounded work. Escalate only when several semantic owners/migration phases genuinely need one coordinated durable contract.

## Anti-Slop Baseline

- Think before editing; surface important assumptions/tradeoffs.
- Prefer the minimum complete solution.
- Every changed file/line must trace to the declared goal.
- Do not widen scope because adjacent improvements are visible.
- Do not add compatibility/fallback layers without a proved need.
- Do not hide uncertainty behind polished prose.
- Do not use rendering, voice writing, or audit prose to solve an upstream definition problem.
- Do not repeatedly patch symptoms when the owning content/rule/code is wrong.
- Stop the same failed direction after two attempts without new evidence.
- Do not create tests, screenshots, builds, fixtures, reports, or review notes solely to look rigorous.
- Never claim approval, validation, runtime behavior, visual quality, audio quality, or delivery that was not actually obtained.

## Minimum Useful Proof

Validation is evidence, not ceremony. Use the cheapest check that can disprove the likely failure, then stop when the acceptance criteria have enough evidence.

- **Text/docs/routing:** exact changed paths + link/ownership consistency.
- **Bounded repository source change:** changed owner + directly affected contract/caller + targeted check where available.
- **PRD content change:** canonical content + requirement traceability + role/readiness gate relevant to the change.
- **Renderer/HTML change:** structural validation; browser/live visual claims require actual browser/visual proof.
- **Voice requirement/script change:** exact requirement/script parity + relevant semantic review.
- **DOCX change:** builder/mechanical validation + rendered-page inspection for visual acceptance.
- **Generated audio claim:** actual audio must exist and be reviewed.
- **Cross-owner change:** verify only the boundaries that actually changed.

Do not rerun unchanged checks after they already established the needed evidence.

## Evidence Status Escalation

Use evidence labels only for material support/feasibility/runtime uncertainty:

- **CURRENT-PROJECT VERIFIED** — exact/equivalent claim has sufficient proof in the current project/environment.
- **AUTHORITATIVE-SOURCE VERIFIED** — current authoritative project/source documentation supports the claim, but current execution/output success may still be unproven.
- **LOCAL PROOF REQUIRED** — implementation/support is plausible enough to proceed, but a material local/browser/audio/runtime check remains before the claim can be reported as verified.
- **UNSUPPORTED** — available evidence shows the requested method/capability should not be relied on.
- **UNKNOWN** — evidence is insufficient or materially conflicting; do not guess.

Static inspection cannot upgrade a live/browser/audio claim to `CURRENT-PROJECT VERIFIED`.

## Production Boundaries

- Project Document Generator owns Flow 2–4.
- Voice Production Kit owns Flow 5–7.
- Root `.agents/skills/` owns agent work routing/judgment, not the detailed production procedure.
- Production Flow 1–7 and agent work modes are separate layers; do not confuse them.

## Canonical Skill Architecture

The frozen repository-wide skill set is:

- `.agents/skills/development-brief/` — mandatory Developing front door;
- `.agents/skills/project-document-production/` — semantic specialist for Flow 2–4 and their renderer/validator surfaces;
- `.agents/skills/voice-production/` — semantic specialist for Flow 5–7 and their builder/validator surfaces.

Do not create separate renderer, validator, DOCX, research, evidence-gate, or generic writing skills merely because those implementation surfaces exist.

Do not rename, split, merge, duplicate, or add a repository skill unless current work proves a distinct reusable ownership gap that cannot be represented cleanly by this baseline, foundation policy, a kit procedure, or one existing specialist.

Skill inventory/lineage: `docs/knowledge/skills/skill-map.md`.
Skill routing: `docs/knowledge/skills/activation-matrix.md`.

## Voice Production Boundary

- Flow 5 defines `work/voice-requirements.md` from a current `handoff_ready` PRD.
- Flow 6 preserves the exact Voice ID/type set and creates `work/voice-production.md` + derived DOCX.
- Flow 7 validates the exact current script/DOCX revision through `VOICE-VALIDATION.md`.
- Flow 7 may reopen a root owner when a defect is found; it must not hide the fix in acceptance prose or patch the DOCX directly.
- Critical/Major findings block `voice_delivery_ready`.
- DOCX visual acceptance requires rendered-page inspection.
- generated-audio quality is never claimed unless actual audio was supplied and reviewed.

## User-Facing Communication

For non-trivial Developing work, keep the visible brief simple:

```text
Tujuan:
Cara berpikir:
Hasil yang dituju:
Tidak diubah:
Cara memastikan benar:
```

Final report:

```text
Status: Selesai | Perlu pemeriksaan | Terhenti
Hasil:
Bukti:
Batasan:
Next step:
```

Use exactly one next step. Explain decisions, not internal machinery, unless the user asks for the detailed process.

## Source Of Truth

- stable facts/terminology → `CONTEXT.md`;
- active continuation state → `docs/knowledge/next-action.md`;
- durable decisions/reasons → `docs/knowledge/decision-log.md` + `docs/knowledge/decisions/`;
- production policy → `docs/foundation/`;
- agent routing → `docs/knowledge/flow.md`;
- module ownership → `docs/knowledge/modules/module-map.md` + `implementation-map.md`;
- source authority routing → `docs/knowledge/sources/source-map.md`;
- review evidence current meaning → `docs/knowledge/reviews/review-graph.md`;
- Maintenance procedure → `docs/knowledge/maintenance/maintenance-flow.md`;
- skill inventory → `docs/knowledge/skills/skill-map.md`;
- skill routing → `docs/knowledge/skills/activation-matrix.md`;
- production procedures → affected `kits/*` owner;
- actual project behavior/content → project source/state/canonical work + relevant proof.
