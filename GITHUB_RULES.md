# GitHub Rules

Canonical operating rules for AI/ChatGPT working with GitHub in this repository.

Repository-specific `AGENTS.md` rules may narrow domain behavior, but they must not weaken the safety, integrity, proof, efficiency, or STOP boundaries here.

## How to use this file

For normal repository work, apply **Core Rules 1–7 in order**. Read a section under **Conditional GitHub Surfaces** only when the current task actually touches that surface.

```text
PIN
→ READ MINIMUM
→ DIAGNOSE
→ TOOL + TRANSFER GATE
→ WRITE ONCE
→ VERIFY + FAILURE POLICY
→ STOP
```

Each concept has one primary owner in this file:

```text
branch/ref/current-state authority     → Rule 1
read/search economy                    → Rule 2
scope + first wrong owner              → Rule 3
tool fit + artifact transfer/handoff   → Rule 4
atomic writes + commit history         → Rule 5
verification + retries + recovery      → Rule 6
completion boundary                    → Rule 7
```

Do not reinterpret repeated references in conditional sections as separate policies; the Core Rule owner remains authoritative.

# Core Rules

## 1. PIN — establish exact current authority

Before a material change, know the repository, intended working branch/ref, current HEAD when materially relevant, requested scope, and whether the target is writable.

- Use direct branch/file fetches for current state. Search is discovery, not current-state authority.
- Never silently fall back to the default branch.
- Every GitHub write must explicitly target the intended branch/ref when the tool supports it.
- Treat repository-designated default, protected, production, or release branches as read-only unless repository policy or explicit user instruction authorizes the write.
- An archived/read-only repository is not a write target. Do not search for a bypass.
- Re-check HEAD only when concurrent movement is plausible or immediately before a write that could overwrite newer work.
- For replacement/deletion, use the current blob/content SHA from the exact target branch. If GitHub rejects a stale SHA, follow Rule 6; never guess or substitute another identifier type.

## 2. READ MINIMUM — read only what can change the decision

Default budget:

```text
owner files      1–3
history reads    0
broad scans      0
```

- Open more only when a concrete unresolved question requires it.
- When the exact path is known, prefer direct fetch over repository search.
- Do not read history, review archives, generated output, or adjacent owners merely to feel safer.
- Search/list output that is truncated, paginated, partial, or capped is incomplete evidence, not proof that an item does not exist.
- Continue pagination or narrow a query only when unseen results can materially change the decision.
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

## 4. TOOL + TRANSFER GATE — choose a method that natively fits

Use the simplest capability that safely produces the required final state.

```text
current branch / exact file state
→ direct GitHub fetch

one small bounded UTF-8 file
+ one logical delivery
+ complete current file available
→ GitHub Contents API / update_file

coherent multi-file logical delivery /
commit atomicity matters /
large file / many precise hunks /
coordinated refactor / binary / Git LFS /
true patch or Git semantics required
→ Local or Codex-style git workspace,
  or another known-safe atomic Git capability

final artifact cannot be transferred safely/natively
by the available GitHub capability
→ Manual Handoff

CI diagnosis
→ run → failing job/step → exact relevant log

browser / audio / local runtime claim
→ actual matching capability
```

Do not choose a per-file Contents API merely because it is available when doing so would turn one logical delivery into several repository commits.

### Transfer gate before the first write

For a generated artifact, existing-file replacement, binary/binary-heavy output, or coherent multi-file delivery, establish before writing:

```text
final artifact/content ready and validated?
exact repository/ref/path known?
file type and practical transfer characteristics known?
existing-file replacement understood?
complete logical file set known?
active method natively carries the final payload?
active method preserves acceptable repository history?
```

If readiness is missing, prepare the final result first. If capability/history fit is missing, do not start the repository write; choose a genuinely fitting capability or Manual Handoff.

Large size, binary content, existing generated-file replacement, and multi-file packages are **risk signals**, not separate workflows. The deciding question is always:

> Can the active capability deliver the actual final result safely, directly, and with clean repository state/history?

### Hard transfer prohibitions

Connector limitations must not change repository/product architecture.

Never create or use the following solely to bypass a transfer limitation:

- placeholder content at the final destination;
- temporary loaders or bootstrap files;
- artificial HTML/content fragments;
- base64/text stand-ins for normal binary assets;
- transfer-only helper manifests;
- temporary branches/workflows;
- alternate repository structures;
- blob/tree/commit/ref chains that merely carry the same unsupported payload.

Also:

- Never full-replace a file from partial file context.
- Never split `update_file` into chunks. It replaces the whole file; it does not append or patch.
- Keep blob/content SHA, commit SHA, tree SHA, tag/ref, workflow-run IDs, and other GitHub identifiers distinct; use only the identifier required by the operation.
- Low-level Git blob/tree/commit/ref operations are valid only when the task genuinely requires those Git semantics and the capability is known to fit; they are not a connector-bypass mechanism.
- Force-push, history rewrite, destructive reset, or equivalent ref manipulation is never a workaround for stale SHA, CI failure, connector limits, commit spam, or messy history.
- Do not use GitHub Actions as a remote shell or as a substitute for missing local/browser/audio/runtime capability.
- A final destination path may be created only when the real intended content for that path is ready.

### Manual Handoff

Manual Handoff is a valid completion path when direct GitHub transfer would be slower, less reliable, unsafe, unavailable, or harmful to repository history.

When selected:

1. Stop the unsupported GitHub write path.
2. Finish and validate the exact final artifact locally.
3. Compress assets when appropriate without changing approved meaning or required readability.
4. Prepare the exact replacement file or a repository-ready ZIP with intentional relative paths.
5. Give the file/ZIP directly to the user in chat.
6. Give an exact placement contract.
7. State what is already present in GitHub, if anything.
8. Do not claim the repository contains the handoff artifact until the user or a capable tool actually uploads it.

Placement contract:

```text
repository:        owner/repo
branch/ref:        exact intended ref
repo root:         where placement starts
destination:       exact relative path
action:            upload | replace | merge | extract
expected result:   key final path(s) after placement
repo state:        unchanged | partially changed (list exact paths)
```

Do not give vague instructions such as “put this in the repo.” For a repository-ready ZIP, make the archive root intentional so placement does not require hunting through individual files.

When a capability mismatch is confirmed, tell the user promptly what is blocked, why the active method does not fit, what fallback is being used, and what the user must do, if anything. Do not silently spend multiple tool calls on connector workarounds.

## 5. WRITE ONCE — deliver one meaningful logical state

Prepare the complete intended logical result and delivery method before the first write.

- One intentional write per file is the default, but **WRITE ONCE does not mean COMMIT EVERY WRITE**.
- Same-file and overlapping repository mutations are serial, never parallel.
- For coordinated multi-file work, know the complete intended file set and ensure the selected method can deliver the hardest required artifact before any repository mutation starts.
- Do not partially synchronize a baseline that is required to be coherent. If one required artifact cannot be delivered by the chosen method, return to Rule 4 before writing the rest.
- Do not mix Contents API writes, low-level Git-object writes, and manual partial delivery merely to force one logical package through incompatible methods.
- A successful mutation response is usable current state. Reuse returned commit/content identifiers and authored state; do not immediately refetch the same state merely for reassurance.
- If HEAD moves materially during coordinated work, refetch affected current state and reassess; do not blindly overwrite, merge, or rebase around concurrent work.
- Keep one canonical owner for each durable rule/state where practical; avoid synchronization cascades across duplicate contracts.
- Update status/continuity/release metadata only when the milestone, blocker, next meaningful objective, capability boundary, or actual release state changed.
- Preserve repository-declared lockfiles, runtime/version files, dependency constraints, and action references unless they are the actual owner of the requested change.
- New files, workflows, abstractions, compatibility layers, fixtures, reports, branches, PRs, issues, comments, labels, releases, and other persistent side effects default to zero unless the task/repository workflow proves a real need.

### Commit discipline — history must remain meaningful

A repository commit is a **categorized logical delivery**. It is not a file save, tool call, checkpoint, reasoning step, CI trigger, transfer experiment, or proof marker.

Default flow:

```text
prepare complete logical change
→ pass Rule 4 transfer gate
→ cheapest relevant pre-commit proof
→ review final intended state/diff
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
delivery method covers the whole logical result?
message explains repository outcome?
reviewable/revertable as one logical unit?

any NO
→ DO NOT COMMIT YET
```

Default message format:

```text
<type>(<optional-scope>): <concise logical outcome>
```

Categories:

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

- A `fix:` may include its tests and supporting docs when they prove/document the same fix.
- Split commits only for genuinely independent logical deliveries that can be reviewed, reverted, and landed separately.
- Do not split by file, directory, layer, tool call, work order, discovery order, or transfer limitation.
- More than one commit for one requested task requires a concrete logical boundary.
- Vague messages such as `update`, `changes`, `fix again`, `sync`, `final`, `try`, or `misc` are not acceptable history.
- Do not create local checkpoint commits by default; use working tree/staging until the logical delivery is ready.
- If unpublished local commits already exist, they may be consolidated before first push when safe. Never rewrite published/shared history or force-push merely to make history prettier without explicit authority.
- If the available method would create one commit per file for one coherent package, return to Rule 4 and choose an atomic capability or Manual Handoff instead of accepting commit spam.

## 6. VERIFY + FAILURE POLICY — prove only what matters, then handle failure deterministically

### Minimum verification

Validation is evidence, not ceremony.

- Run the cheapest check that can falsify the changed claim.
- Targeted checks are the default during iteration.
- Use a full suite only when the changed executable/public contract can actually be affected and a final full gate is materially useful.
- When CI is relevant, prefer the relevant gate on the final logical state.
- Only a completed successful run is PASS. `queued`, `in_progress`, `pending`, `cancelled`, `skipped`, neutral, or superseded runs are not PASS.
- Superseded runs do not need to be waited on when a newer relevant run replaces them.
- Do not rerun unchanged checks or chase verifiers that cannot falsify the current change.
- On CI failure, inspect the failing job/step and only the relevant error before editing.
- Do not weaken, delete, bypass, or broaden a valid test/workflow merely to obtain green status. Change it only when evidence shows it is itself the first wrong owner.
- Regression tests are for material, realistically recurring invariants, not every typo, one-time migration, cosmetic wording change, or temporary state.
- Do not use exact natural-language prose as a test contract unless the exact string itself is a machine requirement.
- Static inspection and CI prove only the contracts they actually exercise. They do not prove browser visuals, audio quality, local runtime behavior, deployment success, or another capability that was not executed.
- For Manual Handoff, proof is the validated local artifact/package plus an exact placement contract; repository presence remains unverified until upload occurs.

### Canonical failure and retry matrix

**Retry budgets are ceilings, never quotas. A known failure class stops earlier than any remaining retry/time budget.**

| Failure class | Required action |
|---|---|
| Known capability mismatch / unsupported payload or transfer mode | STOP that method immediately; **0 retries**; use Rule 4 fallback |
| Permission or safety denial | STOP that operation; **0 retries** unless new evidence changes the condition |
| Capability genuinely uncertain | At most **1 bounded probe** |
| Malformed but still-valid request / 422 | Correct **once** only if the operation still passes Rule 4 |
| Missing/inaccessible / 404 | Verify the exact repository/ref/target **once** before concluding absence |
| Conflict or stale SHA / 409 | Refetch relevant current state **once** and retry only from that state |
| Rate limit / 429 | Respect `Retry-After` or reset; do not probe repeatedly |
| 5xx / timeout / unknown mutation outcome | Inspect target state first; retry only when the intended mutation is confirmed absent |
| Same-cause operational failure where new evidence can plausibly change outcome | Maximum **2 attempts** for that valid method |

Do not reinterpret a known capability mismatch as malformed-request debugging.

### Transfer experimentation ceiling

Normal target: **one strategy**.

A second strategy is exceptional and allowed only when concrete evidence shows it **natively removes the diagnosed root limitation**.

Valid examples:

```text
inline-text-only connector
→ genuine local-file/binary upload capability

per-file Contents API causing commit fragmentation
→ proper atomic git workspace
```

Not valid strategy changes:

```text
update_file
→ blob/tree/commit/ref to carry the same unsupported payload

large HTML
→ fragments / loader / base64 transfer artifacts

binary unsupported
→ encode the same binary as repository text solely for transfer
```

Hard ceilings for one logical delivery:

```text
per valid transfer method   <= 2 attempts or 2 minutes active experimentation
transfer strategies         1 default, 2 maximum
whole-delivery experiment   <= 3 minutes active experimentation total
```

Whichever STOP condition is reached first wins. Switching tools, endpoints, encodings, or helper structures does not reset a ceiling. If Manual Handoff is already the clearly faster fitting path, use it immediately rather than consuming the remaining budget.

### Interrupted or partial-delivery recovery — exception only

Use this only when repository writes from the current task already occurred before the delivery became blocked.

Perform at most **one bounded recovery pass**:

1. Stop new transfer experiments.
2. Identify the exact current-task paths/commits already changed.
3. Separate legitimate durable changes from accidental placeholders, fragments, loaders, or transfer-only helpers.
4. Remove/correct only accidental current-task artifacts when safe, directly supported, and not dependent on history rewrite or another transfer architecture.
5. Preserve legitimate changes unless the required all-or-nothing baseline would otherwise be materially misleading.
6. If coherent cleanup cannot be achieved quickly, stop and disclose the exact remaining repository state instead of layering on more fixes.
7. Build any Manual Handoff against the actual resulting repository state.
8. Tell the user exactly what is already in GitHub and what remains to upload/replace.

Do not force-push or rewrite published/shared history merely to hide an interrupted delivery. Recovery is bounded state repair, not history beautification.

## 7. STOP — completion is a valid terminal state

Stop when any valid terminal condition is reached:

```text
requested outcome + relevant proof satisfied
→ STOP

confirmed capability mismatch + fallback/handoff delivered
→ STOP

Manual Handoff selected and placement contract provided
→ STOP

operation blocked by authoritative permission/safety/policy boundary
→ report boundary → STOP
```

Do not automatically:

- audit another layer;
- synchronize unrelated documentation;
- run another verifier;
- create proof-of-proof;
- fix adjacent non-blocking issues;
- create branches/PRs/issues/comments merely to document completed work;
- continue because more tooling is available;
- resume GitHub transfer experimentation after a valid Manual Handoff.

## Default efficiency budget

```text
owner reads                    1–3
history reads                  0
broad scans                    0
transfer strategy              1 default; 2 maximum only when root limitation is removed
uncertain-capability probe      <= 1
malformed-request correction    <= 1
same-cause valid-method retry   <= 2 attempts
capability-denial retry         0
whole-delivery transfer trial   <= 3 minutes active experimentation
intentional writes/file         1
logical commits/task            1 by default
relevant CI                     0–1
placeholder/transfer hacks      0
adjacent cleanup                0
repository side effects         0 unless required
high-impact mutations           0 unless explicitly authorized
```

The budgets are default efficiency boundaries. The failure/transfer ceilings in Rule 6 are hard stops and are not reset by changing tools or representations.

# Conditional GitHub Surfaces

Apply only the sections relevant to the current task. These sections add surface-specific constraints; they do not redefine the Core Rules.

## API failures, pagination, rate limits, and ambiguous mutations

HTTP/API interpretation:

```text
401   authentication problem
403   permission / policy / rate-limit condition
404   missing or inaccessible/stale target
409   conflict / stale state
422   invalid request / policy failure
429   rate limited
5xx   server failure; mutation outcome may be unknown
```

Retry/STOP behavior is owned by **Rule 6**.

- Do not create request storms or parallel mutation bursts.
- Respect retry/rate-limit signals instead of repeatedly probing.
- If a mutating request has an unknown outcome, inspect target state before any retry so branches, issues, comments, releases, or writes are not duplicated.

## Special files, Git LFS, binaries, submodules, generated artifacts, and large transfers

Before treating repository content as ordinary UTF-8 text, distinguish regular files from symlinks, submodules, Git LFS pointers, generated artifacts, binaries, binary-heavy documents, and files outside the practical limits of the active tool.

- Never hand-edit a Git LFS pointer as though it were the large-file content.
- Do not rewrite a symlink/submodule/binary through a plain-text replacement path unless that representation is explicitly the intended source.
- Generated/derived artifacts follow their canonical source; fix the source and regenerate unless repository policy explicitly defines the artifact as authored source.
- Compress generated image-heavy artifacts when appropriate and when required readability/quality is preserved.
- Compression does not change tool fit: a smaller artifact that the active capability still cannot natively carry must return to **Rule 4**.
- A local final file plus a GitHub action that accepts only inline text is a transfer-capability constraint, not permission to encode, split, or restructure the artifact.

All delivery decisions for these files are owned by **Rule 4**.

## Pull requests, branch protection, rulesets, reviews, and merge queues

When a task actually involves a PR or merge decision:

- Refresh current PR head SHA, base branch, mergeability, required reviews/CODEOWNERS state, required checks, and relevant deployment/environment gates before the high-impact action.
- A new commit can make prior approvals/check assumptions stale. Do not act from an old PR snapshot.
- Required human review, CODEOWNERS approval, branch protection, rulesets, signed-commit requirements, linear-history rules, merge queue, and deployment requirements are repository authority, not errors to bypass.
- If a merge queue requires GitHub Actions support, fix the workflow event/routing contract rather than bypassing the queue.
- Force-push/history rewrite, branch/tag deletion, PR merge/close, release/tag publication or deletion, environment/deployment bypass, repository settings changes, permission/ruleset changes, and similar externally visible mutations require explicit task authority and an exact current target.
- Perform only the requested high-impact mutation. Do not create, merge, close, publish, delete, bypass, or reconfigure GitHub objects as cleanup, ceremony, proof, or workaround.

## GitHub Actions

GitHub Actions is verification/deployment infrastructure, not a background development engine.

- Automatic workflows run only on intended branches/events and paths their checks can actually falsify.
- Documentation/routing/planning/status changes do not justify a full executable suite unless a check explicitly owns them.
- If a workflow correctly does not trigger because changed paths are irrelevant, that is not missing technical proof. Do not manufacture unrelated changes to trigger it.
- If a skipped workflow is required for merge, treat the pending/missing required check as CI/ruleset routing, not a reason to change unrelated code.
- For unusually large diffs, do not infer correctness solely from the absence of a path-filtered run.
- Prefer fail-fast gates when downstream checks are meaningless after an upstream failure.
- Cancel superseded runs when older results are no longer useful.
- Verification workflows are read-only by default; they do not commit or push back into the working branch.
- Publishing/release bundling is explicit release work, not a side effect of every development push.
- Do not create temporary/one-shot workflows to compensate for a missing capability or transfer limitation.
- Do not rerun an unchanged failed workflow merely to seek a green badge.
- Do not assume automation-created events will always retrigger, or never retrigger, another workflow. Understand the event and credential semantics first.
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
