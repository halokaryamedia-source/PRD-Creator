# Workspace Agent Routing

This repository is PRD-Creator system memory. Current repository/project sources are authority for repository state; chat history is supporting context only.

## Branch and boot

```text
develop  → active repository development; working commits may be numerous
Local    → verified integration / stable working baseline; one commit per approved update
main     → clean stable release history
```

- Normal repository Development happens on `develop`.
- `Local` is not a routine edit target. Promote `develop` to `Local` only through the verified integration boundary.
- Every `develop` → `Local` promotion must use **squash merge** so one approved update adds exactly one commit to `Local`.
- After a squash promotion, synchronize/reset `develop` to the resulting `Local` HEAD before starting the next development cycle.
- `main` is release-only. Promote `Local` to `main` only through an explicitly approved release PR after `Stable release gate` passes.
- A `main` release merge commit is a release marker and is not synchronized back into `Local` or `develop`.
- Tags and GitHub Releases are separate publishing actions and require explicit user instruction.

Choose the smallest sufficient boot for the task.

### Observe / recover context

When the user only asks to inspect, understand, study, or recover repository context:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules when GitHub work is material
→ CONTEXT.md
→ docs/knowledge/next-action.md
→ smallest owner needed to explain current state
→ report understanding
→ STOP
```

This is read-only Plan behavior. Do not edit, advance `next-action`, promote backlog work, or start the recorded next step unless the user also asks to continue.

### Non-trivial Development

Before changing PRD-Creator itself:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules
→ CONTEXT.md
→ docs/knowledge/next-action.md
→ development-brief
→ smallest relevant owner/source
```

### Bounded Maintenance

A clearly bounded defect may start from the exact failing owner when wider product context cannot change the decision. Do not turn Maintenance into a repository-wide redesign.

## Work modes

| Intent | Mode | Front door |
|---|---|---|
| Understand/decide/recover before editing | Plan | inspect evidence + owner; no edit until requested |
| Create/revise project PRD or Voice deliverables | Production Execution | matching production owner |
| Change PRD-Creator policy/workflow/renderer/validator/repository mechanics | Development | `development-brief` + at most one useful specialist |
| Bug/regression/cleanup/stale docs/behavior-preserving correction | Maintenance | concrete failure → first wrong owner |

Creating project artifacts during normal production does not make the task Development.

## Production front doors

```text
new/revised PRD
→ project-document-production
→ smallest active Project/PRD owner in kits/prd-creator/

accepted PRD → Voice production
→ voice-production
→ smallest active Voice owner in kits/prd-creator/
```

### Project package resolution

Project packages are production data, not system-repository content. They may be mounted or copied locally under ignored `workspace/active/<project>/` paths, or retained in a separate authorized repository/location.

```text
user names a project
→ use that exact package

current conversation unambiguously establishes one project
→ continue that project

multiple available projects + request is ambiguous
→ ask which project before changing project state
```

Never infer project focus from directory order, recency, or whichever package is easiest to open.

## Authority and conflict

Use the nearest authoritative owner for each claim:

1. current explicit user instruction for task intent;
2. approved project-specific decisions;
3. authoritative project source;
4. normalized requirement/project state;
5. accepted canonical PRD;
6. accepted Voice requirements / canonical Voice production for downstream scope;
7. durable repository/foundation policy;
8. active `kits/prd-creator/` domain procedure;
9. Golden/reference material for demonstrated structure/quality only;
10. generated output, prior review, or chat/history as supporting evidence only.

Material conflicts remain `UNKNOWN` until reconciled. Golden/reference samples never supply another project's mechanics, counts, story, scoring, speakers, or implementation facts unless explicitly approved.

### Continuity reconciliation

`next-action.md` owns active continuation while current source/state owns actual implementation state.

```text
detect mismatch
→ inspect current source/owner
→ identify stale continuity vs stale implementation
→ reconcile the correct owner
→ continue from actual state
```

Historical TODOs, audits, backlog entries, and Git history are not active work unless current user intent or `next-action` promotes them.

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

Never patch generated `prd.html`, `context.md`, or `index.json` to hide an upstream defect.

## Repository continuity

Canonical current-state owners:

- stable product/repository orientation → `CONTEXT.md`;
- active continuation → `docs/knowledge/next-action.md`;
- durable decisions → `docs/knowledge/decisions/`;
- durable production policy → `docs/foundation/`;
- detailed production procedure/mechanics → affected `kits/prd-creator/` owner;
- project facts/state/output → current external/local project package;
- historical reviews → review files / Git history only when needed.

Update `next-action.md` only when status, active boundary, blocker, deferred boundary, or next meaningful step actually changes.

## Skill budget

Canonical root skills remain:

```text
.agents/skills/development-brief
.agents/skills/project-document-production
.agents/skills/voice-production
```

- Production Execution → one matching production specialist + smallest kit procedure.
- Development → mandatory `development-brief` + at most one useful semantic specialist.
- Maintenance → specialist optional.
- Plan → no specialist by default.

Do not create renderer/validator/Python/research/evidence-gate skills merely because those surfaces exist.

## Execution channel

[GITHUB_RULES.md](GITHUB_RULES.md) owns GitHub tool selection, transfer safety, write/commit/history discipline, verification, retries, recovery, and STOP behavior.

Repository branch-specific narrowing:

- `develop` CI is the active regression safety net for repository development.
- `develop` → `Local` requires the Local promotion gate before integration.
- A successful `develop` → `Local` promotion uses squash merge and adds exactly one Local commit.
- After promotion, `develop` must be synchronized/reset to the resulting `Local` HEAD before new development begins.
- `Local` → `main` requires the Stable release gate and explicit release approval.
- A resulting `main` release merge commit remains on `main`; do not reset lower branches to it.
- Do not bypass a failed gate by editing another branch directly.
- Browser, audio, and runtime claims require the actual matching capability; GitHub/static checks prove only repository/static contracts.

## User-facing communication

Normal Production Execution should expose the requested artifact, material changes/decisions, and real attention items—not repository machinery.

For repository/system Development, a compact brief may use:

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

Use one next step. Explain decisions rather than internal scratch work.

## Product boundaries

- `kits/prd-creator/` is the single product package for Flow 2–7 plus bounded 04 Production Assets completion.
- Project/PRD and Voice remain separate semantic domains inside that package.
- Root skills own reusable semantic judgment, not detailed package procedure.
- `kits/prd-creator/AGENTS.md` owns package module/file routing and pure technical Maintenance.
- Repository engineering owns shared dependency/regression/CI contracts.
- Live project packages are not tracked in the public PRD-Creator system repository; `workspace/` is a local/external mount convention only.
- Production Flows and agent work modes are separate layers.
