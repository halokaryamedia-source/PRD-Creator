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

## Smallest-owner rule

Before editing, identify the **first wrong owner**.

```text
semantic/product meaning wrong
→ matching semantic owner

semantic contract correct + renderer/validator/builder mechanics wrong
→ nearest kit AGENTS + exact implementation owner

shared dependency/test/CI wrong
→ requirements.lock.txt / tests / tools / workflows
```

Do not keep a semantic specialist loaded merely as a Python/HTML/DOCX wrapper. If a task exposes two independent boundaries, finish/reframe one before switching owner.

## Root-cause and edit gate

Before changing behavior establish:

- what actually happens;
- what requirement/contract is expected;
- which owner is first wrong;
- why the proposed change fixes that cause;
- what evidence could falsify the fix.

If the cause remains unknown, report `Perlu pemeriksaan` / `Terhenti` with the missing evidence instead of patching symptoms.

Before creating/moving a file, search existing owners first. Reuse/extend before creating. Do not create README/schema/config/fallback/abstraction for hypothetical future use. `No change required` is valid.

## Anti-overdevelopment baseline

- Prefer the minimum complete solution.
- Every changed line must trace to the declared goal.
- Do not widen scope because adjacent improvements are visible.
- Do not add compatibility/fallback layers without a proved need.
- Do not hide uncertainty behind polished prose or rendering.
- Do not repeatedly patch downstream symptoms when upstream meaning/code is wrong.
- Stop the same failed direction after two attempts without new evidence.
- Do not create tests, screenshots, builds, fixtures, reports, or review notes merely to look rigorous.
- Never claim approval, runtime behavior, visual/audio quality, or delivery that was not actually obtained.

## Proof economy

Validation is evidence, not ceremony. Use the cheapest check that can disprove the likely failure, then stop when the claimed status has enough support.

- docs/routing → changed owners + link/ownership consistency;
- PRD content → relevant requirement traceability + role/readiness review;
- renderer/HTML → focused contract/mechanical validation; visual PASS needs actual rendered/browser evidence;
- Voice semantics → requirement/script parity + relevant semantic review;
- DOCX mechanics → focused builder/validator proof; visual PASS still needs rendered-page inspection;
- shared dependency/test/CI → repository engineering gate exercising the changed contract;
- generated audio → actual audio must exist and be reviewed.

Do not rerun unchanged checks after they already established the required evidence.

GitHub Actions must follow the same economy:

- `Repository Verify` is for repository/routing/shared-engineering changes, not normal `workspace/active/**` project production or domain Python already owned by PRD/Voice gates;
- PRD/Voice workflows must be path-scoped to files their tests can actually falsify; a markdown-only change does not justify a full domain test unless an explicit test contracts that markdown;
- prefer the final relevant automatic gate on the final SHA; do not create a temporary workflow merely to repeat an existing gate, and do not wait for superseded runs when workflow concurrency cancels them.

Use evidence labels only when material uncertainty exists:

- `CURRENT-PROJECT VERIFIED` — current project/environment proof exists;
- `AUTHORITATIVE-SOURCE VERIFIED` — authoritative source supports the claim but execution may remain unproven;
- `LOCAL PROOF REQUIRED` — implementation is plausible but local/browser/audio/runtime proof remains;
- `UNSUPPORTED` — evidence says not to rely on the method/capability;
- `UNKNOWN` — evidence is insufficient/conflicting.

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

## Execution channel and tool fit

Choose the execution channel and GitHub tool **before writing**. Tool availability is a constraint, not a challenge to work around.

Default routing:

- current branch/HEAD/exact file state → direct GitHub fetch with explicit `Local`; use search for discovery, not as authority for current state;
- small bounded UTF-8 text edit where the complete current file is available → GitHub Contents API / `update_file`; prepare the final file first and use one intentional write per file by default;
- large file, many precise hunks, multi-file refactor, atomic multi-file requirement, binary edit, or work that needs true patch semantics → Local/Codex-style git workspace; do not emulate patching with repeated full-file replacements;
- CI diagnosis → workflow run → failing job/step → exact relevant log; do not broad-read logs or retry a failed direction without new evidence;
- browser, audio, or local runtime proof → use the actual browser/audio/runtime capability only; GitHub Actions is not a fallback execution shell.

Hard stops:

- never full-replace a file from partial file context;
- never split `update_file` into chunks: it replaces the entire file, it does not append or patch a chunk;
- keep blob/content SHA, commit SHA, and tree SHA distinct; use the identifier required by the specific operation only;
- a permission, safety, or capability denial ends that operation immediately; do not retry it through Git gymnastics, helper files, or a temporary workflow unless the user explicitly changes the execution channel or requests a durable capability;
- do not change repository structure merely to make the current connector easier to use;
- when the current channel cannot perform the requested change safely, report the required channel instead of forcing completion.

GitHub/static inspection can prove repository state and static contracts. Local/browser/audio/runtime claims require those capabilities to be actually available. Goal, authority, scope, and acceptance criteria do not change with execution channel; only available execution and proof do.

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
