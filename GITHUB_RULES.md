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
→ TRANSFER PREFLIGHT
→ WRITE ONCE
→ VERIFY MINIMUM
→ STOP
```

The transfer preflight is mandatory before the first repository write for generated artifacts, existing-file replacement, binary-heavy output, or coherent multi-file delivery. Its purpose is to prevent a connector limitation from turning a simple delivery into repeated retries, placeholder files, helper structures, commit spam, or low-level Git workarounds.

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
- When the exact path is already known, prefer direct fetch over repository search. Do not use broad discovery to re-prove a known target.

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

large generated artifact / binary-heavy package /
difficult existing generated-file replacement /
active connector cannot transfer the final artifact natively
→ finish + validate locally
→ prepare repository-ready file or ZIP
→ give it to the user in chat with exact destination
→ user performs the manual upload/replace

CI diagnosis
→ run → failing job/step → exact relevant log

browser / audio / local runtime claim
→ actual matching capability
```

Do not choose a per-file Contents API merely because it is available when doing so would turn one logical delivery into several repository commits.

### Transfer preflight — decide before the first write

Before uploading, replacing, or committing a generated artifact/package, establish:

```text
final artifact already exists?          YES / NO
final content validated?                YES / NO
exact target repository/ref known?      YES / NO
exact destination path known?           YES / NO
file type known?                        YES / NO
final size known?                       YES / NO
binary or binary-heavy?                 YES / NO
existing file replacement?              YES / NO
multi-file logical delivery?            YES / NO
active tool accepts payload natively?   YES / NO
clean logical history can be preserved? YES / NO
```

Any material `NO` in readiness/capability means **DO NOT START THE REPOSITORY WRITE**. Resolve the missing information, choose a fitting channel, or use manual handoff.

The preflight is not a reason to speculate about arbitrary size thresholds. The question is practical tool fit: can the current capability transfer the final artifact safely, directly, and without distorting repository structure/history?

### Manual handoff is a valid completion path

Manual handoff is not a failure when direct connector transfer would be slower, less reliable, unsafe, or destructive to repository history.

When the active GitHub capability cannot natively perform the final transfer:

1. Stop the GitHub write attempt immediately.
2. Finish and validate the exact final artifact locally.
3. Compress images/assets when appropriate without changing approved meaning or necessary readability.
4. Prepare either the exact replacement file or a repository-ready ZIP that preserves relative paths.
5. Give the file/ZIP directly to the user in chat.
6. State the exact repository destination and whether the user should upload, replace, merge, or extract it.
7. Treat that handoff as the terminal delivery for the blocked GitHub operation unless the user explicitly asks to try a different capable channel.

If the user can perform a simple drag-and-drop/replace faster than the connector can safely transfer the artifact, prefer the user handoff instead of consuming time on connector workarounds.

### Existing generated-artifact replacement

Replacing an existing generated artifact is a hard transfer check, not an invitation to force a full-file text write.

If replacement through the active connector would require a large full-file inline payload, binary conversion, fragmentation, repeated retransmission, or low-level Git gymnastics:

```text
STOP repository write
→ generate/validate replacement locally
→ give replacement file to user
→ state exact repository path
```

Do not partially overwrite an existing generated artifact. Do not create the destination early as a placeholder.

### Multi-file logical delivery

Before the first write, know the complete intended file set for one logical delivery.

- One logical package should remain one reviewable/revertable delivery where practical.
- If the available connector would create one commit per file for a coherent package, use a proper atomic git workspace/capability or manual repository-ready handoff instead.
- Do not begin by updating easy Markdown files and only later discover that the required final binary/large artifact cannot be transferred. The delivery plan must cover the hardest required artifact before any repository mutation starts.
- Do not mix Contents API writes, low-level Git object writes, and manual partial delivery for the same logical package merely to force completion. Choose one suitable delivery strategy before writing.

### Connector-workaround prohibition

Connector limitations must not change product/repository architecture.

Do not create any of the following solely to make transfer possible:

- placeholder content at the final destination;
- temporary loaders or bootstrap files;
- artificial HTML/content fragments;
- base64 text files standing in for normal binary assets;
- temporary branches/workflows;
- helper manifests with no product/repository purpose;
- alternate repository structures;
- blob/tree/commit/ref chains that exist only to bypass the active connector.

A final destination path may be created only when the real intended content for that path is ready.

Hard stops:

- Never full-replace a file from partial file context.
- Never split `update_file` into chunks. It replaces the whole file; it does not append or patch.
- Keep blob/content SHA, commit SHA, tree SHA, tag/ref, workflow-run IDs, and other GitHub identifiers distinct; use only the identifier required by the operation.
- Low-level Git blob/tree/commit/ref operations are not the default editor. Use them only when the task genuinely requires those semantics and the capability is known to be available; never use them merely to bypass connector transfer limits.
- Force-push, history rewrite, destructive reset, or equivalent ref manipulation is never a workaround for stale SHA, CI failure, connector limits, commit spam, or messy history.
- Permission, safety, or capability denial ends that operation immediately. Do not retry through Git gymnastics, helper files, temporary workflows, branch switching, payload fragmentation, or repository restructuring.
- Do not use GitHub Actions as a remote shell or as a substitute for missing local/browser/audio/runtime capability.
- Do not change repository structure merely to make the connector easier to use.
- If the current channel cannot perform the change safely or preserve the required history quality, report/use the suitable channel instead of forcing completion.

### Immediate blocker disclosure

When a GitHub capability mismatch is confirmed, tell the user **before** attempting another delivery strategy.

State concisely:

1. what operation is blocked;
2. why the active capability does not fit;
3. what fallback will be used;
4. what the user needs to do, if anything.

Do not silently spend multiple tool calls trying transfer workarounds while the user is waiting for completion.

## 5. WRITE ONCE — deliver meaningful repository state

Prepare the intended logical result before the first write.

- One intentional write per file is the default, but **WRITE ONCE does not mean COMMIT EVERY WRITE**.
- Same-file and overlapping repository mutations are serial, never parallel.
- A successful mutation response is usable current state. Reuse returned commit/content identifiers and authored state; do not immediately refetch the same file/HEAD/commit merely for reassurance. Refetch only when concurrency or a required proof can materially change the decision.
- For a coordinated multi-file change, establish the intended complete patch and delivery method before the first repository commit. If HEAD moves materially, refetch affected state and reassess; do not blindly overwrite, merge, or rebase around concurrent work.
- Do not perform partial canonical synchronization when the task requires a complete synchronized baseline. If one required artifact cannot be delivered by the selected method, stop before writing the rest and choose a complete delivery strategy.
- Keep one canonical owner for each durable rule/state where practical; do not copy the same contract across many docs and create synchronization cascades.
- Update status/continuity/release metadata only when the milestone, blocker, next meaningful objective, capability boundary, or actual release state changed—not after every micro-step.
- Preserve repository-declared lockfiles, runtime/version files, dependency constraints, and action references. Change them only when dependency/version drift is the actual first wrong owner or the task explicitly requests it.
- New files, workflows, abstractions, compatibility layers, fixtures, reports, branches, PRs, issues, comments, labels, releases, transfer helpers, and other persistent side effects default to zero unless the current task/repository workflow proves a real need.

### Commit discipline — history must remain meaningful

A repository commit is a **categorized logical delivery**. It is not a file save, tool call, checkpoint, reasoning step, CI trigger, transfer experiment, or proof marker.

Default delivery flow:

```text
prepare complete logical change
→ transfer preflight
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
transfer strategy covers hardest required artifact?
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
- Do not split by file, directory, backend/frontend layer, tool call, work order, discovery order, or transfer limitation.
- More than one commit for one requested task requires a concrete logical boundary, not convenience.
- Vague messages such as `update`, `changes`, `fix again`, `sync`, `final`, `try`, or `misc` are not acceptable history.
- Do not create local checkpoint commits by default; use working tree/staging until the logical delivery is ready.
- If unpublished local commits already exist, they may be consolidated before first push when safe. Never rewrite published/shared history or force-push merely to make history prettier without explicit authority.
- When one logical change touches multiple files and the active tool would produce one commit per file, use a workspace/known-safe atomic Git operation or manual repository-ready handoff instead of accepting commit spam.

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
- Same-cause retry budget: maximum 2 attempts only when the operation remains valid and new evidence can plausibly change the outcome.
- Permission/capability denial retry budget: 0 unless new evidence changes the condition.
- Unsupported large/binary transfer retry budget with the same connector/method: 0.
- Existing-artifact replacement that fails because the connector cannot natively carry the required final payload: 0 workaround retries; use a fitting channel or manual handoff.
- A malformed request may be corrected once only if the underlying operation still passes TOOL FIT and transfer preflight.
- Regression tests are for material, realistically recurring invariants—not every typo, one-time migration, cosmetic wording change, or temporary state.
- Do not use exact natural-language prose as a test contract unless the exact string itself is a machine requirement.
- Static inspection and CI prove only the contracts they actually exercise. They do not prove browser visuals, audio quality, local runtime behavior, deployment success, or another capability that was not actually executed.
- For manual handoff, proof means the local artifact/package was validated and the repository destination is exact. Do not falsely claim the repository contains it until the user or a capable tool actually uploads it.

## 7. STOP — completion is a valid terminal state

When the requested outcome, relevant acceptance criteria, and minimum relevant proof are satisfied, stop.

Do not automatically:

- audit another layer;
- synchronize unrelated documentation;
- run another verifier;
- create proof-of-proof;
- fix adjacent non-blocking issues;
- create branches/PRs/issues/comments merely to document work already completed;
- continue because more tooling is available;
- keep trying GitHub after a valid manual handoff has been selected for a connector-blocked transfer.

A confirmed capability mismatch is also a valid STOP boundary for that operation. Stop the unsupported write, disclose the blocker, and deliver through the chosen fallback.

## Default efficiency budget

```text
owner reads                    1–3
history reads                  0
broad scans                    0
artifact transfer preflight    1 when applicable
new files                      0
new workflows                  0
new abstractions               0
transfer-only helper files     0
placeholder writes             0
intentional writes/file        1
logical commits/task           1 by default
uncategorized commits          0
intermediate commits           0
CI-trigger commits             0
proof-only commits             0
pushes/task                    1 by default
relevant CI                    0–1
same-cause retry               <= 2 when operation remains valid
capability-denial retry        0
unsupported-transfer retry     0
connector-workaround retry     0
adjacent cleanup               0
repository side effects        0 unless required
high-impact mutations          0 unless explicitly authorized
```

Exceed a budget only when the current task provides concrete evidence that more work is necessary.

# Conditional GitHub Surfaces

Apply only the sections relevant to the current task. These are not extra boot requirements.

## API failures, pagination, rate limits, and ambiguous mutations

```text
401        authentication problem → stop until credentials/access change
403        permission / policy / rate-limit investigation
404        missing OR inaccessible / stale target → verify exact target once
409        conflict / stale state → refetch relevant state once
422        invalid request / policy failure → correct once only if operation still fits
429        rate limited → respect Retry-After/reset before another request
5xx/timeout mutation outcome may be unknown → inspect current state before retry
capability mismatch / unsupported payload type or transfer mode → 0 retries; choose fallback
```

- Do not create request storms or parallel mutation bursts.
- Respect retry/rate-limit signals instead of repeatedly probing.
- If a mutating request has an unknown outcome, refetch the target state first. Retry only when the intended mutation is confirmed absent; this prevents duplicate branches, issues, comments, releases, or writes.
- Do not reinterpret a capability mismatch as a malformed-request debugging exercise. If the tool cannot natively carry the required artifact/package, stop that method.
- Do not respond to repeated 422/transfer failures by changing repository structure, introducing placeholders/fragments/loaders, or descending into low-level Git object manipulation merely to bypass the connector.

## Special files, Git LFS, binaries, submodules, generated artifacts, and large transfers

Before treating repository content as ordinary UTF-8 text, distinguish regular files from symlinks, submodules, Git LFS pointers, generated artifacts, binaries, binary-heavy documents, and files outside the practical limits of the active tool.

- Never hand-edit a Git LFS pointer as though it were the large-file content.
- Do not rewrite a symlink/submodule/binary through a plain text replacement path unless that representation is explicitly the intended source.
- Generated/derived artifacts follow their canonical source; fix the source and regenerate unless repository policy explicitly defines the artifact as authored source.
- Compress generated image-heavy artifacts before delivery when doing so preserves required readability/quality.
- A compressed artifact can still be a capability mismatch. Smaller size does not justify forcing a connector that still lacks native file/binary/replacement support.
- When local final files exist but the active GitHub action accepts only inline text rather than a local-file parameter, treat that as a transfer-capability constraint, not as permission to encode/split/restructure the artifact.
- For a binary-heavy or generated package that the active connector cannot transfer safely, prepare a repository-ready ZIP/file and hand it to the user with the exact destination instead of converting repository architecture around the connector.

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
- Do not create temporary/one-shot workflows to compensate for a missing capability or transfer limitation.
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
