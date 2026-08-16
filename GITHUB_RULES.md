# GitHub Rules

Canonical operating rules for AI/ChatGPT working with GitHub in this repository.

Repository-specific `AGENTS.md` rules may narrow domain behavior, but they must not weaken the safety, integrity, proof, or STOP boundaries here.

## How to use this file

For normal repository work, apply **Core Rules 1–7**. The **Conditional GitHub Surfaces** section applies only when the task actually touches that surface. Do not load or reason through PR, release, runner, LFS, or deployment rules for a bounded text edit that does not involve them.

```text
PIN
→ READ MINIMUM
→ DIAGNOSE
→ TOOL FIT
→ WRITE ONCE
→ VERIFY MINIMUM
→ STOP
```

# Core Rules

## 1. PIN — establish exact current authority

Before a material change, know the repository, intended working branch/ref, current HEAD, requested scope, and whether the target is writable.

- Use direct branch/file fetches for current state. Search is discovery, not current-state authority.
- Never silently fall back to the default branch.
- Every GitHub write must explicitly target the intended branch/ref when the tool supports it.
- Treat repository-designated default, protected, production, or release branches as read-only unless repository policy or explicit user instruction authorizes the write.
- An archived/read-only repository is not a write target. Do not search for a bypass.
- Re-check HEAD only when concurrent movement is plausible or immediately before a write that could overwrite newer work.
- For replacement/deletion, use the current blob/content SHA from the exact target branch. If GitHub rejects a stale SHA, refetch once and rebuild the intended final state; never guess or substitute another identifier type.

## 2. READ MINIMUM — read only what can change the decision

Default budget:

```text
owner files      1–3
history reads    0
broad scans      0
```

- Open more only when a concrete unresolved question requires it.
- Do not read history, review archives, generated output, or adjacent owners merely to feel safer.
- Search/list output that is truncated, paginated, partial, or capped is incomplete evidence, not proof that an item does not exist.
- Continue pagination or narrow a query only when the unseen portion can materially change the decision; do not exhaustively page through data by default.
- A missing result may mean missing, stale ref, or inaccessible. Verify the exact repository/ref/access once before concluding absence; do not guess alternate branches or paths.

## 3. DIAGNOSE — fix the first wrong owner

Before writing, establish actual vs expected behavior and identify the first owner that is wrong.

```text
requirement / meaning wrong
→ semantic owner

requirement correct + implementation wrong
→ implementation owner

implementation correct + test stale
→ test

implementation/test correct + CI routing wrong
→ workflow / repository policy

derived artifact wrong
→ upstream canonical owner
```

- Do not widen Maintenance into redesign.
- Do not perform unrelated cleanup, refactors, compatibility work, documentation synchronization, dependency upgrades, or framework creation unless they block the requested result.
- CI failure is evidence to diagnose, not permission to change whatever is easiest.
- Historical failures are not active work unless the current system still reproduces their root cause.
- `No change required` is valid when current behavior already satisfies the requirement.

## 4. TOOL FIT — use a tool that natively fits the operation

```text
current branch / exact file state
→ direct GitHub fetch

one small bounded UTF-8 file + one logical delivery + complete current file
→ GitHub Contents API / update_file

coherent multi-file logical delivery / commit atomicity matters /
large file / many precise hunks / coordinated refactor /
binary / Git LFS / true patch semantics
→ Local or Codex-style git workspace, or another known-safe atomic Git capability

CI diagnosis
→ run → failing job/step → exact relevant log

browser / audio / local runtime claim
→ actual matching capability
```

Do not choose a per-file Contents API merely because it is available when doing so would turn one logical delivery into several repository commits.

Hard stops:

- Never full-replace a file from partial file context.
- Never split `update_file` into chunks. It replaces the whole file; it does not append or patch.
- Keep blob/content SHA, commit SHA, tree SHA, tag/ref, workflow-run IDs, and other GitHub identifiers distinct; use only the identifier required by the operation.
- Low-level Git blob/tree/commit/ref operations are not the default editor. Use them only when the task genuinely requires those semantics and the capability is known to be available.
- Force-push, history rewrite, destructive reset, or equivalent ref manipulation is never a workaround for stale SHA, CI failure, connector limits, commit spam, or messy history.
- Permission, safety, or capability denial ends that operation immediately. Do not retry through Git gymnastics, helper files, temporary workflows, or branch switching.
- Do not use GitHub Actions as a remote shell or as a substitute for missing local/browser/audio/runtime capability.
- Do not change repository structure merely to make the connector easier to use.
- If the current channel cannot perform the change safely or preserve the required history quality, report/use the suitable channel instead of forcing completion.

## 5. WRITE ONCE — deliver meaningful repository state

Prepare the intended logical result before the first write.

- One intentional write per file is the default, but **WRITE ONCE does not mean COMMIT EVERY WRITE**.
- Same-file and overlapping repository mutations are serial, never parallel.
- A successful mutation response is usable current state. Reuse returned commit/content identifiers and authored state; do not immediately refetch the same file/HEAD/commit merely for reassurance. Refetch only when concurrency or a required proof can materially change the decision.
- For a coordinated multi-file change, establish the intended complete patch before the first repository commit. If HEAD moves materially, refetch affected state and reassess; do not blindly overwrite, merge, or rebase around concurrent work.
- Keep one canonical owner for each durable rule/state where practical; do not copy the same contract across many docs and create synchronization cascades.
- Update status/continuity/release metadata only when the milestone, blocker, next meaningful objective, capability boundary, or actual release state changed—not after every micro-step.
- Preserve repository-declared lockfiles, runtime/version files, dependency constraints, and action references. Change them only when dependency/version drift is the actual first wrong owner or the task explicitly requests it.
- New files, workflows, abstractions, compatibility layers, fixtures, reports, branches, PRs, issues, comments, labels, releases, and other persistent side effects default to zero unless the current task/repository workflow proves a real need.

### Commit discipline — history must remain meaningful

A repository commit is a **categorized logical delivery**. It is not a file save, tool call, checkpoint, reasoning step, CI trigger, or proof marker.

Default delivery flow:

```text
prepare complete logical change
→ cheapest relevant pre-commit proof available
→ review final intended diff/state
→ one categorized logical commit
→ push once
→ only relevant CI
→ STOP
```

Commit gate:

```text
one coherent outcome?
primary category clear?
intended file set complete?
message explains repository outcome?
reviewable/revertable as one logical unit?

any NO
→ DO NOT COMMIT YET
```

Default message format:

```text
<type>(<optional-scope>): <concise logical outcome>
```

Use the primary outcome, not file type or work order:

```text
feat:      new user/repository capability
fix:       wrong behavior or regression
docs:      documentation/policy-only change
refactor:  internal restructuring without intended behavior change
test:      test-contract-only change
ci:        CI/workflow routing or execution change
build:     build/dependency/toolchain change
release:   explicit release/publish state
chore:     bounded maintenance that genuinely fits none above; use sparingly
```

Rules:

- A `fix:` may include its tests and supporting docs in the same commit when they prove/document the same fix.
- Split commits only for genuinely independent logical deliveries that can be reviewed, reverted, and landed separately.
- Do not split by file, directory, backend/frontend layer, tool call, work order, or discovery order.
- More than one commit for one requested task requires a concrete logical boundary, not convenience.
- Vague messages such as `update`, `changes`, `fix again`, `sync`, `final`, `try`, or `misc` are not acceptable history.
- Do not create local checkpoint commits by default; use working tree/staging until the logical delivery is ready.
- If unpublished local commits already exist, they may be consolidated before first push when safe. Never rewrite published/shared history or force-push merely to make history prettier without explicit authority.
- When one logical change touches multiple files and the active tool would produce one commit per file, use a workspace/known-safe atomic Git operation or report the required channel instead of accepting commit spam.

## 6. VERIFY MINIMUM — validation follows the claim

Validation is evidence, not ceremony.

- Run the cheapest check that can falsify the changed claim.
- Targeted checks are the default during iteration.
- Use a full suite only when the changed executable/public contract can actually be affected and a final full gate is materially useful.
- When CI is relevant, prefer the relevant gate on the final logical state; do not treat an intermediate commit/run as final proof.
- Only a completed successful run is PASS. `queued`, `in_progress`, `pending`, `cancelled`, `skipped`, neutral, or superseded runs are not PASS.
- Superseded runs do not need to be waited on when a newer relevant run replaces them.
- Do not rerun unchanged checks or chase every verifier to green when they cannot falsify the current change.
- On CI failure, inspect the failing job/step and only the relevant error before editing.
- Do not weaken, delete, bypass, or broaden a valid test/workflow merely to obtain a green result. Change it only when evidence shows it is itself the first wrong owner.
- Same-cause retry budget: maximum 2 attempts.
- Permission/capability denial retry budget: 0 unless new evidence changes the condition.
- Regression tests are for material, realistically recurring invariants—not every typo, one-time migration, cosmetic wording change, or temporary state.
- Do not use exact natural-language prose as a test contract unless the exact string itself is a machine requirement.
- Static inspection and CI prove only the contracts they actually exercise. They do not prove browser visuals, audio quality, local runtime behavior, deployment success, or another capability that was not actually executed.

## 7. STOP — completion is a valid terminal state

When the requested outcome, relevant acceptance criteria, and minimum relevant proof are satisfied, stop.

Do not automatically:

- audit another layer;
- synchronize unrelated documentation;
- run another verifier;
- create proof-of-proof;
- fix adjacent non-blocking issues;
- create branches/PRs/issues/comments merely to document work already completed;
- continue because more tooling is available.

## Default efficiency budget

```text
owner reads               1–3
history reads             0
broad scans               0
new files                 0
new workflows             0
new abstractions          0
intentional writes/file   1
logical commits/task      1 by default
uncategorized commits     0
intermediate commits      0
CI-trigger commits        0
proof-only commits        0
pushes/task               1 by default
relevant CI               0–1
same-cause retry          <= 2
capability-denial retry   0
adjacent cleanup          0
repository side effects   0 unless required
high-impact mutations     0 unless explicitly authorized
```

Exceed a budget only when the current task provides concrete evidence that more work is necessary.

# Conditional GitHub Surfaces

Apply only the sections relevant to the current task. These are not extra boot requirements.

## API failures, pagination, rate limits, and ambiguous mutations

```text
401        authentication problem
403        permission / policy / rate-limit investigation
404        missing OR inaccessible / stale target
409        conflict / stale state → refetch relevant state
422        invalid request / policy failure → fix request, do not repeat blindly
429        rate limited → respect Retry-After/reset before another request
5xx/timeout mutation outcome may be unknown → inspect current state before retry
```

- Do not create request storms or parallel mutation bursts.
- Respect retry/rate-limit signals instead of repeatedly probing.
- If a mutating request has an unknown outcome, refetch the target state first. Retry only when the intended mutation is confirmed absent; this prevents duplicate branches, issues, comments, releases, or writes.

## Special files, Git LFS, binaries, submodules, and generated artifacts

Before treating repository content as ordinary UTF-8 text, distinguish regular files from symlinks, submodules, Git LFS pointers, generated artifacts, binaries, and files outside the practical limits of the active tool.

- Never hand-edit a Git LFS pointer as though it were the large-file content.
- Do not rewrite a symlink/submodule/binary through a plain text replacement path unless that representation is explicitly the intended source.
- Generated/derived artifacts follow their canonical source; fix the source and regenerate unless repository policy explicitly defines the artifact as authored source.

## Pull requests, branch protection, rulesets, reviews, and merge queues

When a task actually involves a PR or merge decision:

- Refresh current PR head SHA, base branch, mergeability, required reviews/CODEOWNERS state, required checks, and relevant deployment/environment gates before the high-impact action.
- A new commit can make prior approvals/check assumptions stale. Do not act from an old PR snapshot.
- Required human review, CODEOWNERS approval, branch protection, rulesets, signed-commit requirements, linear-history rules, merge queue, and deployment requirements are repository authority—not errors to bypass.
- If a merge queue requires GitHub Actions support, fix the workflow event/routing contract rather than bypassing the queue.
- Force-push/history rewrite, branch/tag deletion, PR merge/close, release/tag publication or deletion, environment/deployment bypass, repository settings changes, permission/ruleset changes, and similar externally visible mutations require explicit task authority and an exact current target.
- Perform only the requested high-impact mutation. Do not create, merge, close, publish, delete, bypass, or reconfigure GitHub objects as cleanup, ceremony, proof, or workaround.

## GitHub Actions

GitHub Actions is verification/deployment infrastructure, not a background development engine.

- Automatic workflows run only on intended branches/events and paths their checks can actually falsify.
- Documentation/routing/planning/status changes do not justify a full executable suite unless a check explicitly owns them.
- If a workflow correctly does not trigger because changed paths are irrelevant, that is not missing technical proof. Do not manufacture unrelated changes to trigger it.
- If a skipped workflow is required for merge, treat the pending/missing required check as CI/ruleset routing—not a reason to change unrelated code.
- For unusually large diffs, do not infer correctness solely from the absence of a path-filtered run.
- Prefer fail-fast gates when downstream checks are meaningless after an upstream failure.
- Cancel superseded runs when older results are no longer useful.
- Verification workflows are read-only by default; they do not commit or push back into the working branch.
- Publishing/release bundling is explicit release work, not a side effect of every development push.
- Do not create temporary/one-shot workflows to compensate for a missing capability.
- Do not rerun an unchanged failed workflow merely to seek a green badge.
- Do not assume automation-created events will always retrigger—or never retrigger—another workflow. Understand the event and credential semantics first.
- Use least-privilege workflow/token permissions. Do not widen permissions, expose secrets, or switch credentials merely to make CI pass.
- Preserve repository-declared action versions. For new third-party actions, prefer trusted sources and immutable/pinned revisions where practical; never move to `latest` as an opportunistic fix.
- Treat issue/PR titles and bodies, branch names, labels, commit messages, workflow inputs, and other event-derived strings as untrusted input. Do not interpolate them directly into privileged shell/script code.
- Treat `pull_request_target` and similar privileged base-context workflows as a security boundary. Never execute untrusted PR code in a privileged secret/write-token context without an explicitly safe design.
- Fork PRs may intentionally lack secrets/write tokens. Do not weaken policy merely to make fork CI green.
- Do not route untrusted PR code to a privileged/persistent self-hosted runner merely to gain missing capabilities.

## Secrets, releases, and deployment environments

- Never commit, paste, echo, or move secrets such as API keys, access tokens, passwords, private keys, authorization headers, or `.env` credentials into source, workflows, issues, PRs, comments, logs, or documentation.
- If a secret is discovered, do not reproduce its value. Report only the affected location/type and treat exposure as a security issue.
- Masking/redaction in logs is not a reason to print a secret intentionally.
- Environment/release/deployment approval gates are authoritative constraints, not ordinary CI failures. Do not bypass reviewers or protection rules for convenience.
