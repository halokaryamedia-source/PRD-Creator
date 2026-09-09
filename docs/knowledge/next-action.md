# Next Action

## Current Status

`SFX_OFFLINE_PREFLIGHT_IMPLEMENTED`

Non-dialogue SFX remains inside Production Assets. The researched coordinator and seven selectively loaded references remain in use. An executable, read-only request preflight now complements the operator policy; no ElevenLabs generation adapter or billing service was added.

## Implemented Boundary

- `tools/prd.py sfx-check` reads one native SFX-v2 API request and an explicit operator-supplied batch snapshot.
- `kits/prd-creator/shared/sfx.py` owns strict JSON/body checks and next-attempt request/duration checks. It reuses shared structured issues, not a second canonical asset parser.
- Reject duplicate/unsupported request fields, invalid numeric/boolean values, invalid model, exhausted allowance, and unresolved earlier outcomes. Auto duration is checked against the documented 30-second maximum.
- The result contains the exact request-file SHA256, compact settings, blockers and explicit unchecked boundaries. It never reads credentials, calls an API, rewrites a prompt, writes project state, or reserves allowance.
- Used includes every dispatched attempt; unresolved is a subset, not a second debit. Snapshot freshness, consent, concurrency, format entitlement, monetary limits and actual audio remain outside mechanical proof.
- Existing six preparation examples are checked by the same native-request validator. Dedicated offline tests exercise invalid input, budget boundaries, no-network/read-only behavior and CLI success/failure.

## Preserved

Canonical workflow names, existing project/Voice data and acceptance schemas, Owner/Moment/AST/VO identity, Golden UI and runtime dependencies are unchanged. Package authoring-contract version remains **3.1.3**; this additive mechanical check changes no project contract. No root skill, SFX database, paid execution, promotion or release is implied.

The preflight is not an executable billing firewall. Its PASS is not SFX Production Readiness, semantic acceptance, generation permission, a budget reservation, or heard evidence. The existing execution/cost-control policy still applies.

## Next Step

For a real approved SFX target, prepare the exact request and recover current limits/counters from the existing execution record. Run the offline check, resolve blockers, then separately verify the remaining production/authorization gates. Reserve in the shared record before any explicitly authorized paid call. Never reset counters to obtain PASS.

No further paid calibration is authorized by this implementation. Keep work on `develop`; `Local` and `main` remain untouched until explicitly promoted under existing gates.
