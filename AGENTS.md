# Workspace Agent Routing

This repository is project memory. Current repository/project sources are authority; chat history is supporting context only.

## Branch and boot

- `Local` is the permanent working authority.
- Work directly on `Local`; do not create routine task branches/PRs.
- `main` changes only when the user explicitly requests it.

For every material session, boot with only:

1. `CONTEXT.md` — stable product/boundary facts;
2. `docs/knowledge/next-action.md` — current status + one next step;
3. the smallest owner required by the task.

Open `docs/knowledge/skills/activation-matrix.md` only when the correct skill/owner is genuinely ambiguous. Use `docs/knowledge/README.md`, `docs/knowledge/ownership.md`, or `docs/knowledge/source-authority.md` only when direct ownership is unclear. Do not broad-read saved projects, all docs, review history, generated output, or Git history by default.

## GitHub Operating Discipline

For ChatGPT ↔ GitHub work, use this sequence and stop when it is satisfied:

```text
PIN
→ READ MINIMUM
→ DIAGNOSE
→ TOOL FIT
→ WRITE ONCE
→ VERIFY MINIMUM
→ STOP
```

This is the canonical repository-working discipline. Domain sections below only narrow it; they do not add extra ceremony.

### 1. PIN — establish current authority

Before a material repository change, know the repository, working branch, current HEAD, and requested scope.

- Use direct branch/file fetches for current state; search is for discovery, not authority.
- Do not silently fall back to the default branch.
- Do not repeatedly poll HEAD. Re-check only when concurrent movement is plausible or immediately before a material write that could overwrite newer work.

### 2. READ MINIMUM — load only what can change the decision

- Default read budget: **1–3 owner files, 0 history reads, 0 broad repository scans**.
- Open history, review archives, secondary routing indexes, generated output, or adjacent owners only when a concrete unresolved question requires them.
- Current explicit user intent and current authoritative source beat stale stored state.
- `No change required` is valid.

### 3. DIAGNOSE — find the first wrong owner

Before writing, establish actual vs expected behavior and fix the first owner that is wrong.

```text
semantic / product meaning wrong
→ matching semantic owner

semantic contract correct + renderer / validator / builder mechanics wrong
→ exact implementation owner

implementation correct + test stale
→ test

implementation/test correct + CI routing wrong
→ workflow

derived artifact wrong
→ upstream canonical owner
```

- Maintenance does not become redesign because adjacent issues are visible.
- Do not widen scope into compatibility layers, frameworks, refactors, broad cleanup, or documentation synchronization unless they block the requested result.
- Do not patch downstream generated artifacts to hide an upstream defect.
- Do not write while the cause is still guesswork; report the missing evidence instead.

### 4. TOOL FIT — use the channel that natively fits the operation

Tool availability is a constraint, not a challenge to work around.

```text
current branch / exact file state
→ direct GitHub fetch

small bounded UTF-8 edit + complete current file available
→ GitHub Contents API / update_file

large file / many precise hunks / coordinated multi-file refactor /
atomic multi-file requirement / binary work / true patch semantics
→ Local or Codex-style git workspace

CI diagnosis
→ run → failing job/step → exact relevant log

browser / audio / local runtime claim
→ the actual matching capability
```

Hard stops:

- never full-replace a file from partial file context;
- never split `update_file` into chunks; it replaces the whole file, it does not append or patch;
- keep blob/content SHA, commit SHA, and tree SHA distinct;
- a permission, safety, or capability denial ends that operation immediately; do not retry it through Git gymnastics, helper files, or temporary workflows;
- do not change repository structure merely to make the connector easier to use;
- if the current channel cannot do the work safely, report the required channel instead of forcing completion.

### 5. WRITE ONCE — commit meaningful state, not thought steps

Prepare the intended final state before the first write.

- One intentional write per file is the default. Same-file writes are serial, never parallel.
- Prefer one coherent logical change over chains of `try`, `rerun`, `trigger`, `sync`, or `final proof` commits.
- Do not create commits only to trigger CI, align proof, rerun a workflow, or make the connector easier to operate.
- Do not treat intermediate connector commits as independent milestones that each require validation.
- New files, workflows, abstractions, compatibility layers, fixtures, reports, and persistent state default to **zero** unless the current requirement proves a durable need.
- Update `next-action.md` only when the active milestone, blocker, pause point, or next meaningful objective actually changes.

### 6. VERIFY MINIMUM — validation follows the claim

Validation is evidence, not ceremony.

- Run the cheapest check that can falsify the changed claim.
- Targeted checks are the default during iteration. A full suite is for a materially relevant final gate, not every edit.
- Documentation/routing changes require only the checks that actually own those files.
- Do not rerun unchanged checks or chase every verifier to green when they cannot falsify the current change.
- CI failure means `diagnose first`, not `edit first`: inspect the failing job/step and only the relevant error, then identify the first wrong owner.
- Same-cause retry budget: **maximum 2 attempts**. A permission/capability denial has **0 retries** unless new evidence changes the condition.
- Regression tests are for material, realistically recurring invariants—not every typo, one-time migration, cosmetic wording change, or temporary state.
- Do not use exact natural-language prose as a test contract unless the exact string itself is a machine requirement.
- Historical failures are not active work unless the current system still reproduces their root cause.

### GitHub Actions rules

GitHub Actions is verification infrastructure, not a background development engine.

- Automatic workflows run only on the working branch and paths their checks can actually falsify.
- Markdown, routing, planning, status, or normal project-production changes do not justify a full domain suite unless a check explicitly owns them.
- Prefer fail-fast gates when downstream checks are meaningless after an upstream failure.
- Cancel superseded runs when repeated pushes can overlap.
- Verification workflows are read-only: they do not commit or push back into the working branch.
- Publishing/release bundling is an explicit release action, not a side effect of every development push.
- Do not create temporary/one-shot workflows to repeat existing checks or compensate for a missing local capability.
- Do not rerun an unchanged failed workflow merely to seek a green badge.

Use evidence labels only when material uncertainty remains:

```text
CURRENT-PROJECT VERIFIED
AUTHORITATIVE-SOURCE VERIFIED
LOCAL PROOF REQUIRED
UNSUPPORTED
UNKNOWN
```

Static inspection cannot upgrade a browser/audio/runtime claim to current-project verified.

### 7. STOP — completion is a valid terminal state

When the requested outcome, relevant acceptance criteria, and minimum relevant proof are satisfied, **stop**.

Do not automatically:

- audit another layer;
- synchronize unrelated documentation;
- run another verifier;
- create proof-of-proof;
- fix adjacent non-blocking issues;
- continue because more tooling is available.

### Default efficiency budget

```text
owner reads               1–3
history reads             0
new files                 0
new workflows             0
new abstractions          0
intentional writes/file   1
relevant CI               0–1
same-cause retry          <= 2
capability-denial retry   0
adjacent cleanup          0
```

Exceed a budget only because the current task produces concrete evidence that more work is necessary—not because extra work feels safer.

## Work modes

| Intent | Mode | Front door |
|---|---|---|
| Understand/decide before editing | Plan | inspect evidence + owner first |
| Create/revise PRD or Voice deliverables with existing system | Production Execution | matching production owner directly |
| Change PRD-Creator policy/skills/workflow/renderer/validator/builder/repository mechanics | Developing | `development-brief` + at most one useful specialist |
| Bug/regression/cleanup/stale docs/behavior-preserving correction | Maintenance | concrete failure → first wrong owner |

Creating files during normal project production does **not** make the task Developing.

## Production front doors

```text
new/revised PRD
→ project-document-production
→ kits/project-document-generator/ smallest active Flow owner

accepted PRD → Voice production
→ voice-production
→ kits/voice-production-kit/ smallest active Flow owner
```

Production Execution rules:

- bootstrap project/workspace/internal IDs automatically;
- inspect repository/project evidence before asking the user;
- triage source relevance/authority before deep reading;
- for Flow 2, solve before asking: existing authority → safe Completion → responsible recommended Proposal or honest tradeoff → Blocked/direct decision;
- batch only unresolved material decisions after that recovery/problem-solving pass;
- use bounded revision fast paths instead of replaying unchanged work;
- keep internal state/evidence internal unless requested or needed to explain a blocker;
- deliver the requested artifact plus concise material changes/attention items.

## Authority and conflict

Use the nearest authoritative owner for each claim:

1. current explicit user instruction for task intent;
2. approved project-specific decisions;
3. authoritative project source;
4. normalized requirement/project state;
5. accepted canonical PRD;
6. accepted Voice requirements / canonical Voice script for their own downstream scope;
7. durable repository/foundation policy;
8. active kit procedure;
9. Golden/reference material for demonstrated structure/quality only;
10. generated output, prior review, or chat/history as supporting evidence only.

Material conflicts remain `UNKNOWN` until reconciled. Do not choose silently. A Golden/reference sample never supplies project-specific mechanics, counts, story, scoring, speakers, or other facts unless explicitly approved.

## Derived-artifact rule

Preserve the authority chain:

```text
original source / approved decisions
→ normalized state
→ canonical work
→ derived projection/artifact
→ acceptance evidence
```

Never patch `prd.html`, DOCX, or another derived artifact to hide an upstream defect. Regenerate only invalidated derived artifacts.

## Repository continuity

Canonical current-state owners:

- stable facts/terminology → `CONTEXT.md`;
- active continuation → `docs/knowledge/next-action.md`;
- durable decisions/reasons → `docs/knowledge/decisions/README.md` + `docs/knowledge/decisions/`;
- durable production policy → `docs/foundation/`;
- detailed production procedure/mechanics → affected `kits/*` owner;
- project facts/state/output → current project package;
- historical reviews → review files / Git history, only when needed.

Before ending material work, update only the canonical owner whose current state actually changed. Current user intent wins over stale stored state, but reconcile the conflict explicitly.

## Skill budget

Canonical root skills remain:

```text
.agents/skills/development-brief
.agents/skills/project-document-production
.agents/skills/voice-production
```

- Production Execution → one matching production specialist + smallest active kit procedure.
- Developing → mandatory `development-brief` + at most one useful specialist.
- Maintenance → specialist optional; use only if it adds material semantic procedure.
- Plan → no specialist by default.

Do not create renderer/validator/Python/DOCX/research/evidence-gate skills merely because those implementation surfaces exist.

## User-facing communication

Normal Production Execution does not show repository machinery. Default delivery is the requested artifact plus concise material changes/decisions and any real remaining attention item.

For repository/system Developing work use a compact brief when useful:

```text
Tujuan:
Cara berpikir:
Hasil yang dituju:
Tidak diubah:
Cara memastikan benar:
```

Final repository/system report:

```text
Status: Selesai | Perlu pemeriksaan | Terhenti
Hasil:
Bukti:
Batasan:
Next step:
```

Use exactly one next step. Explain decisions, not internal machinery, unless the user asks for details.

## Product boundaries

- Project Document Generator owns Flow 2–4.
- Voice Production Kit owns Flow 5–7.
- Root skills own reusable semantic routing/judgment.
- Nearest kit `AGENTS.md` owns module mechanics and pure technical Maintenance.
- Repository engineering owns shared dependency/regression/CI contracts.

Production Flows and agent work modes are separate layers; do not confuse them.
