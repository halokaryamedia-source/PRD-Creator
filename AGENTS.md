# Workspace Agent Routing

This repository is project memory. Current repository/project sources are authority for repository state; chat history is supporting context only.

## Branch and boot

- `Local` is the permanent development / working authority.
- Routine work happens directly on `Local`; do not create routine task branches/PRs.
- `main` is the stable / release branch and is not a routine development target.
- Promote `Local` to `main` only when the user explicitly declares a stable/release promotion and the relevant release proof passes.
- A dedicated `Local` → `main` PR is valid at that release boundary only; it does not change the normal direct-to-`Local` workflow.
- A verified merge into `main` is the stable promotion. Git tags and GitHub Releases are separate publishing actions and must never be created automatically without an explicit user request.

Choose the smallest **sufficient** boot for the task. Efficiency must not remove context that prevents wrong work.

### Observe / recover context

When the user only asks to `amati`, inspect, understand, study, or recover repository context:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules for material GitHub work
→ CONTEXT.md
→ docs/knowledge/next-action.md
→ smallest owner needed to explain the current state
→ report understanding
→ STOP
```

This is read-only Plan behavior. Do **not** edit, advance `next-action`, promote backlog work, run CI, or start the recorded next step unless the user also asks to continue/implement.

### Non-trivial Development

Before changing PRD-Creator itself, read:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules
→ CONTEXT.md
→ docs/knowledge/next-action.md
→ development-brief
→ smallest relevant owner/source
```

`CONTEXT.md` and `next-action.md` are mandatory here because repository development must survive new-chat/session boundaries without asking the user to reconstruct prior work.

### Bounded Maintenance / mechanical work

A clearly bounded defect may use a smaller boot when stable product context and active continuation cannot change the decision. Start from the exact defect/owner; do not turn this exception into broad context skipping for Development work.

Open `docs/knowledge/skills/activation-matrix.md` only when the correct specialist is genuinely ambiguous. Use `docs/knowledge/ownership.md` or `docs/knowledge/source-authority.md` only when direct ownership/authority is unclear. Do not broad-read saved projects, reviews, decisions, generated output, or Git history by default.

## GitHub work

[GITHUB_RULES.md](GITHUB_RULES.md) is the canonical ChatGPT ↔ GitHub operating policy. It owns GitHub branch/ref authority, tool + transfer gate, manual handoff, write/commit/history discipline, verification/failure/recovery policy, CI/API safety, and STOP behavior.

Repository-specific rules here may narrow domain behavior but do not duplicate or weaken that policy.

### Local CI narrowing

For this repository, CI on `Local` is an asynchronous regression safety net, not a blocking permission gate for ordinary development.

- Use the cheapest relevant proof before the logical commit.
- After a normal `Local` commit, do not poll or wait for `queued` / `in_progress` CI before continuing or reporting the completed change.
- Diagnose only a failure on the current relevant `Local` HEAD. Cancelled or superseded runs do not need recovery.
- `Repository Verify`, `PRD Verify`, and `Voice Verify` remain targeted by their workflow paths and may run in the background.
- `Release Verify` on the explicit `Local` → `main` release PR is blocking and must complete successfully before merge.

This narrows the general verification policy for the repository branch model; it does not convert incomplete CI into PASS or weaken the `main` release gate.

## Work modes

| Intent | Mode | Front door |
|---|---|---|
| Understand/decide/recover context before editing | Plan | inspect evidence + owner; no edit until requested |
| Create/revise PRD or Voice deliverables with the existing system | Production Execution | matching production owner directly |
| Change PRD-Creator policy/skills/workflow/renderer/validator/repository mechanics | Development | `development-brief` + at most one useful specialist |
| Bug/regression/cleanup/stale docs/behavior-preserving correction | Maintenance | concrete failure → first wrong owner |

Creating files during normal project production does **not** make the task Development.

## Production front doors

```text
new/revised PRD
→ project-document-production
→ kits/prd-creator/ smallest active Project/PRD owner

accepted PRD → Voice production
→ voice-production
→ kits/prd-creator/ smallest active Voice owner
```

### Active project resolution

Multiple packages may legitimately remain under `workspace/active/` at the same time.

```text
user names a project
→ use that exact project package

current conversation unambiguously establishes one project
→ continue that project

multiple active projects + request is ambiguous
→ ask which project before changing project state
```

Never infer the active project from directory order, filename order, repository recency, or whichever package happens to be easiest to open.

Production Execution rules:

- bootstrap project/workspace/internal IDs automatically;
- inspect repository/project evidence before asking the user;
- recover existing context before asking the user to repeat it;
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
6. accepted Voice requirements / canonical Voice production for their downstream scope;
7. durable repository/foundation policy;
8. active `kits/prd-creator/` domain procedure;
9. Golden/reference material for demonstrated structure/quality only;
10. generated output, prior review, or chat/history as supporting evidence only.

Material conflicts remain `UNKNOWN` until reconciled. Do not choose silently. A Golden/reference sample never supplies project-specific mechanics, counts, story, scoring, speakers, or other facts unless explicitly approved.

### Continuity reconciliation

`next-action.md` owns **active continuation**, while current source/state owns **actual implementation state**.

If they materially disagree:

```text
detect mismatch
→ inspect the current source/owner
→ identify stale continuity vs stale implementation
→ reconcile the correct owner
→ continue from actual current state
```

Do not blindly implement a stale next step, and do not ignore `next-action` to pick an unrelated TODO/review finding. Old TODOs, backlog entries, audit findings, comments, and Git history are not active work unless current user intent or `next-action` promotes them.

## Evidence boundary

Use evidence labels only when material uncertainty remains:

```text
CURRENT-PROJECT VERIFIED
AUTHORITATIVE-SOURCE VERIFIED
LOCAL PROOF REQUIRED
UNSUPPORTED
UNKNOWN
```

Static inspection cannot upgrade browser/audio/runtime claims to current-project verified.

## Derived-artifact rule

Preserve the authority chain:

```text
original source / approved decisions
→ normalized state
→ canonical work
→ derived projection/artifact
→ acceptance evidence
```

Never patch `prd.html` or another derived artifact to hide an upstream defect. Regenerate only invalidated derived artifacts.

## Repository continuity

Canonical current-state owners:

- stable product/repository orientation → `CONTEXT.md`;
- active continuation/resume checkpoint → `docs/knowledge/next-action.md`;
- durable decisions/reasons → `docs/knowledge/decisions/README.md` + `docs/knowledge/decisions/`;
- durable production policy → `docs/foundation/`;
- detailed production procedure/mechanics → affected `kits/prd-creator/` domain owner;
- project facts/state/output → current project package;
- historical reviews → review files / Git history, only when needed.

Read `next-action.md` for Development/context recovery, but write it only when status, active boundary, blocker, deferred boundary, or the next meaningful step actually changes.

Before ending material work, update only the canonical owner whose current state actually changed. Current user intent wins over stale stored state, but reconcile the conflict explicitly.

## Skill budget

Canonical root skills remain:

```text
.agents/skills/development-brief
.agents/skills/project-document-production
.agents/skills/voice-production
```

- Production Execution → one matching production specialist + smallest active `kits/prd-creator/` procedure.
- Development → mandatory `development-brief` + at most one useful specialist.
- Maintenance → specialist optional; use only if it adds material semantic procedure.
- Plan → no specialist by default.

Do not create renderer/validator/Python/research/evidence-gate skills merely because those implementation surfaces exist.

## Execution channel

GitHub execution/tool-selection rules are owned by [GITHUB_RULES.md](GITHUB_RULES.md). GitHub/static inspection proves repository state and static contracts only; browser, audio, and local runtime claims require the actual matching capability.

## User-facing communication

Normal Production Execution does not show repository machinery. Default delivery is the requested artifact plus concise material changes/decisions and any real remaining attention item.

For repository/system Development work use a compact brief when useful:

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

- `kits/prd-creator/` is the single product package for Flow 2–7 plus bounded 04 Production Assets completion.
- Project/PRD and Voice remain separate semantic domains inside that package.
- Root skills own reusable semantic judgment, not detailed package procedure.
- `kits/prd-creator/AGENTS.md` owns package module/file routing and pure technical Maintenance.
- Repository engineering owns shared dependency/regression/CI contracts.

Production Flows and agent work modes are separate layers; do not confuse them.
