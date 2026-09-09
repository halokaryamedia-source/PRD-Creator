# Execution and cost control

Read before any potentially paid action. This is an **agent/operator policy, not an executable billing firewall**. No billing enforcement service, generation wrapper, SDK dependency or new canonical schema is introduced.

## Authorization gate

Preparation, implementation, research and tests make **zero paid requests**. A request to improve this skill is not a request to synthesize audio. Require explicit generation authorization and recoverable finite limits for the named batch before invoking any generator.

Recover the approved targets, exact surface/model, maximum provider requests, maximum requested seconds per request or explicit bounded-auto policy, and any monetary/credit ceiling. Include rights/privacy readiness, selected output and review capability. Existing explicit limits may be reused; do not ask for approval at every call inside them. Missing authorization or a missing finite cap means prepare the handoff and stop, not assume unlimited usage.

A budget is a maximum, never a target. Quality approval does not renew it. Another chat/session resumes from prior evidence rather than resetting counters. Expanded scope, extra attempts, top-ups, subscriptions or a switch to another paid provider require authorization; never auto-top-up or upgrade.

## Preflight before reserving a request

1. Check existing approved/licensed assets and already-generated candidates; prefer sufficient reuse/editing over another generation. Do not reduce a required audible distinction to save a request.
2. Verify the actual executor supports SFX and the needed controls. A skill file is instructions, not a connected tool. Use a supported official skill/API/SDK/CLI or confirmed MCP capability; do not assume hosted MCP parity or install the deprecated local MCP.
3. Validate prompt/body/query, duration, loop/model compatibility and format entitlement without a paid probe. Use the relevant [contract](elevenlabs-contracts-and-sources.md). No TTS tags, unsupported seed/reference fields or guessed SDK parameters.
4. Inspect automatic SDK/transport/agent retries and fan-out. Disable automatic generation retries, or prove every attempt is surfaced and budget-gated. If hidden attempts cannot be bounded, do not execute through that adapter.
5. Confirm a safe project-local output path, no overwrite of approved audio, credentials kept outside repo/logs, and a way to hear the result or obtain operator review. With no review capability, at most finish an explicitly authorized unreviewed sample; stop further iteration.

Default to serial execution. A wrapper that turns one tool call into several provider requests must expose that count before authorization. Do not parallelize speculative family states. Parent and delegated agents share the same remaining budget; delegation is not a new quota.

## Reserve, reconcile, resume

Before dispatch, reserve the next request slot and its worst-case authorized duration/cost exposure. Count all dispatched provider attempts, including retries. Retain unknown/failed outcomes conservatively until authoritative evidence resolves their charge; do not treat exceptions as refunds.

In existing execution notes, keep one compact batch record: scope/approval, limits, attempted and in-flight/unknown requests, measured charges with units when available, selected files and remaining allowance. It is execution evidence, never a field addition to `work/asset-requirements.md` or a new SFX database. Save enough before dispatch to recover an interruption safely; do not log secrets.

Unknown timeout or broken stream: inspect the known request/history/output when the surface permits. Do not automatically resend. A recoverable output should be downloaded/reviewed, not regenerated. If outcome/charge cannot be reconciled, stop paid work and disclose uncertainty. Never invent a history ID or assume SFX history access because speech has it.

For a hard monetary ceiling, reserve a verified upper-bound charge in the same currency/unit or use a confirmed provider-side cap. If the next maximum charge cannot be established, stop before dispatch. A finite request/seconds cap controls exposure but is not a guaranteed dollar cap. When there is no hard money ceiling, an explicit user-approved bounded request/seconds exposure with acknowledged unknown price may be used; never describe it as an exact cost estimate.

Auto duration is permitted only when its documented worst-case duration and billing exposure fit the approved policy. Otherwise propose a useful explicit duration. Do not remove a needed decay or identity-bearing texture simply to request fewer seconds.

### Request-accounting examples

These are arithmetic illustrations, not generation authorization. Attempted excludes separately reserved in-flight/unknown slots; count each attempt once. ALLOW below means the request-count check alone passes; every other gate must still pass.

| Case | Cap | Attempted | Reserved | Next | Count gate |
|---|---|---|---|---|---|
| Fresh | 3 | 0 | 0 | 1 | ALLOW |
| One remaining | 3 | 2 | 0 | 1 | ALLOW |
| In-flight fills cap | 3 | 2 | 1 | 1 | STOP |
| Exhausted | 3 | 3 | 0 | 1 | STOP |

If a failed/unknown attempt is already in Attempted, do not also add it to Reserved. Moving an in-flight slot to Attempted does not restore allowance. All duration and monetary reservations follow the same no-double-count/no-reset discipline.

## Candidate and repair economy

A website Generate may return a group; the API is a different execution unit. Read the current surface contract rather than multiplying quoted prices by guessed candidate counts. Compare available takes first. A selected adequate take ends the search; unused allowance is not a reason to generate alternatives.

First fix demonstrably invalid parameters or mistranslated prompts without paying for repeat failure. For an otherwise valid isolated odd take, compare existing candidates; only then consider a same-configuration request inside the remaining budget. For repeated acoustic defects, state one hypothesis and change one variable class. Do not run broad grids, mandatory A/B sweeps, fixed take quotas or regenerate the whole family for one failed state.

Try a bounded non-destructive edit for excess silence, level, or an edit point when source identity is good. New material, heavy distortion or missing information may justify another take. Do not apply speech isolation to SFX as a universal cleanup step. Do not lower the acceptance bar when budget runs out: report the unmet requirement.

## Failure decisions

| Observation | Required action |
|---|---|
| Invalid parameters / confirmed rejection | Correct locally; any further provider call still needs remaining allowance |
| Authentication, quota or entitlement failure | Stop; resolve authorization/account issue, no paid fallback |
| Rate limit | Honor retry guidance; no tight-loop retries; recheck allowance before a later authorized attempt |
| Timeout / 5xx / partial audio / unknown charge | Reconcile known outcome; no blind retry |
| File save failed after successful response | Recover received bytes/history if available; no regeneration as a file-transfer fix |
| Accepted audio | Stop generation and preserve exact evidence |
| No budget or no safe executor | Preparation-only handoff with explicit boundary |

## Cost evidence and surface choice

Rates and units belong to the active account and dated official sources, not hard-coded historical credit tables. A shorter prompt saves context/readability effort but does not establish a lower SFX charge. Do not assume free narration retries apply to SFX, or that a button labelled preview is free.

Website exploration, direct API automation, and timeline composition are different jobs; select the smallest adequate route. Studio Agent chat or automatically generated other media can add charges. Local editing of existing bytes does not require a new ElevenLabs generation; verify cloud-editor actions rather than assuming the same.

Useful metric after an actual batch: verified generation expenditure / accepted deliverables, with unit and review scope. Keep editing effort separate. Do not report an improvement percentage without comparable measured batches. Report prepared prompts, paid attempts, accepted assets, unresolved charges and remaining allowance only as evidenced; omit invented precision.

## Offline request check

From the repository root, use the existing operator CLI with a native SFX-v2 JSON body (one example body from the prompting reference may be saved as `request.json`):

```bash
python tools/prd.py sfx-check request.json --request-limit 3 --requests-used 0 --unresolved-requests 0 --max-duration-seconds 2
```

These numbers are illustrative, not authorization. Supply actual current limits and counters from the existing execution record. `requests-used` includes every dispatched retry and unresolved attempt; `unresolved-requests` is its subset. Convert the table above as used = Attempted + Reserved, unresolved = unresolved portion; never reset either to zero merely to pass.

The checker rejects duplicate/unsupported fields, invalid types/ranges, exhausted slots and any unresolved outcome. Auto duration is evaluated at the API's 30-second upper bound. It does not impose the website's 450-character limit on API text. Its 64 KiB file and 32-bit counter bounds are local parser safeguards, not provider limits.

Exit 0 means only mechanical PASS; exit 1 means a request/snapshot blocker; exit 2 means invalid CLI arguments. No network, credential read, file write or reservation occurs. The report omits full prompts and returns an exact request-file SHA256. A changed request or snapshot needs another check. Query format/entitlement, accepted AST meaning, ledger freshness, consent, concurrency and monetary limits still require the checks above. **Do not use this stateless preview as a spending lock.**

## Operator-ready handoff

Return the target AST IDs, exact prompts, intended surface/model, duration/loop/influence, output choice, review criteria and proposed finite budget. Clearly separate proposal from approval. One worked suggestion may be up to three API attempts of at most two seconds each for a short cue; this is an example ceiling, not a default entitlement. A first accepted take stops at one. Resume from the existing record before any later call.
