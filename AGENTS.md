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

## GitHub work

For any material GitHub read/write, read and follow [GITHUB_RULES.md](GITHUB_RULES.md) before editing.

`GITHUB_RULES.md` is the canonical ChatGPT ↔ GitHub operating policy. Repository-specific rules here may narrow domain behavior, but they do not duplicate or weaken its safety, tool-fit, validation, retry, or STOP rules.

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

## Evidence boundary

Use evidence labels only when material uncertainty remains:

```text
CURRENT-PROJECT VERIFIED
AUTHORITATIVE-SOURCE VERIFIED
LOCAL PROOF REQUIRED
UNSUPPORTED
UNKNOWN
```

Static inspection cannot upgrade a browser/audio/runtime claim to current-project verified.

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

## Execution channel

GitHub execution/tool-selection rules are owned by [GITHUB_RULES.md](GITHUB_RULES.md). GitHub/static inspection proves repository state and static contracts only; browser, audio, and local runtime claims require the actual matching capability.

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
