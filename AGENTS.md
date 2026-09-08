# Workspace Agent Routing

PRD-Creator is repository-backed system memory. Current explicit user intent and current repository/project authority outrank chat history. Use the smallest owner and proof set that can settle the task.

## Core routing

| Intent | Mode | Start |
|---|---|---|
| Inspect, understand, recover, decide | Plan | current state + smallest owner; read-only unless change requested |
| Create/revise project PRD or Voice deliverables | Production Execution | matching production skill + smallest active owner |
| Change PRD-Creator policy, workflow, renderer, validator, schema, tooling, repository mechanics | Development | `development-brief` + exact owner |
| Fix bounded bug, regression, stale routing/docs, behavior-preserving defect | Maintenance | concrete failure → first wrong owner |

Production work does not become Development merely because tools or generated files are involved.

## Boot

### Observe / recover

```text
AGENTS.md
→ CONTEXT.md
→ docs/knowledge/next-action.md
→ smallest owner needed
→ report current understanding
→ STOP
```

Read `GITHUB_RULES.md` only when GitHub execution, mutation, history, CI, promotion, or transfer behavior can affect the task.

### Development

```text
AGENTS.md
→ CONTEXT.md
→ docs/knowledge/next-action.md
→ development-brief
→ exact semantic / implementation owner
→ GITHUB_RULES.md before material GitHub mutation
```

### Production Execution

```text
PRD / non-Voice 04
→ project-document-production
→ kits/prd-creator/SKILL.md
→ smallest PRD owner

Voice
→ voice-production
→ kits/prd-creator/SKILL.md
→ smallest Voice owner
```

Do not broad-read the repository or kit. Expand context only for a real unresolved dependency or contradiction.

## Authority

Use the nearest authority for each claim:

1. current explicit user instruction;
2. approved project-specific decisions;
3. authoritative project source;
4. normalized current project/requirement state;
5. accepted canonical PRD / Voice source for downstream scope;
6. durable repository/foundation policy;
7. active package procedure;
8. Golden/reference material for demonstrated representation/quality only;
9. generated output, reviews, Git history, and chat as supporting evidence.

Material conflicts remain `UNKNOWN` until reconciled. Golden/reference material never supplies another project's facts.

## Action and steering

An explicit request to create, change, fix, continue, or apply work authorizes the requested reversible scope through completion. Ask only when a material decision cannot be recovered responsibly, the target is genuinely ambiguous, or a destructive/security/publishing/promotion boundary requires approval.

When the user changes direction mid-task, preserve completed work that still satisfies the new instruction, invalidate only affected scope, and continue from actual state.

## First wrong owner

```text
meaning / requirement wrong       → semantic owner
meaning correct, implementation wrong → implementation owner
implementation correct, test stale    → test
implementation/test correct, CI wrong → workflow / repository policy
derived artifact wrong            → upstream canonical owner
```

Do not repair upstream defects with renderer defaults, generated-file patches, or extra compatibility layers.

## Canonical and derived state

Preserve the authority chain:

```text
source / approved decisions
→ normalized state
→ canonical work
→ derived artifact
→ acceptance evidence
```

Never hand-patch generated `prd.html`, `context.md`, or `index.json` to hide an upstream defect.

## Repository continuity

- `CONTEXT.md` → stable product/repository orientation.
- `docs/knowledge/next-action.md` → active continuation only.
- `docs/knowledge/decisions/` → durable rationale.
- `docs/foundation/` → durable production policy.
- `kits/prd-creator/` → detailed production procedure and implementation.
- project package → project facts/state/output.
- reviews/history → evidence only when needed.

If `next-action.md` disagrees with current implementation, inspect the current owner, correct the stale side, then continue from actual state. Historical TODOs/audits/backlog are inactive unless current user intent promotes them.

## Branches

```text
develop  → active repository development
Local    → verified integration baseline; develop→Local uses squash
main     → stable history; Local→main requires explicit stable promotion
```

After an approved `develop → Local` squash, synchronize `develop` to the resulting `Local` HEAD before new development. Version tags/releases are separate publishing actions for approved feature/capability changes.

## Execution channel

`GITHUB_RULES.md` owns GitHub tool fit, transfer safety, write/commit discipline, verification, retries, recovery, and STOP behavior. Repository-specific branch narrowing remains:

- routine `develop` iteration uses selective proof;
- `develop → Local` requires the full Local promotion gate;
- `Local → main` requires the stable release gate;
- browser/audio/runtime claims require the matching capability;
- never bypass a failed gate by editing another branch directly.

## User-facing communication

Default to concise result-first reporting. Expose repository machinery only when it explains a real decision, limitation, risk, or next action.

For repository/system work, a compact brief is sufficient when useful:

```text
Tujuan:
Hasil yang dituju:
Tidak diubah:
Cara memastikan benar:
```

Final system report:

```text
Status: Selesai | Perlu pemeriksaan | Terhenti
Hasil:
Bukti:
Batasan:
Next step:
```

Use one next step. Do not expose scratch reasoning.

## Product boundaries

- `kits/prd-creator/` is the single product package for Flow 2–7 plus bounded non-Voice `04 Production Assets`.
- Project/PRD and Voice remain separate semantic domains.
- Root skills own reusable semantic judgment; package owners hold detailed procedure.
- `kits/prd-creator/AGENTS.md` owns package file/mechanical routing.
- Repository engineering owns shared dependency, regression, CI, and governance contracts.
- Live project packages are not tracked in the public system repository; `workspace/` is a local/external mount convention.
- Production Flow and agent work mode are separate layers.

Stop when requested scope is complete and the cheapest sufficient evidence supports the claim.