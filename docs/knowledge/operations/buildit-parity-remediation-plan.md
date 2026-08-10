# BuildIT Parity Remediation

Updated: 2026-08-10
Status: **closed as an automatic remediation program**

## Why this changed

BuildIT was used to improve PRD-Creator's operating discipline. That was useful for repository memory, work-mode routing, ownership, root-cause Maintenance, and focused verification.

The later remediation track began treating differences from BuildIT as gaps that should be engineered away even when PRD-Creator did not need the same machinery. That conflicts with the repository's anti-overdevelopment rules.

Current durable decision:

`../decisions/anti-overdevelopment-simplification.md`

## What remains adopted

- repository-first continuity;
- Plan / Developing / Maintenance routing;
- small ownership surfaces;
- `development-brief` for non-trivial Developing work;
- root-cause-first Maintenance;
- at most one relevant specialist;
- focused executable verification;
- explicit semantic / mechanical / visual / audio proof boundaries;
- `No change required` as a valid result.

## What is not a parity requirement

PRD-Creator does not need to reproduce BuildIT's:

- domain-specific skills;
- module depth;
- review count;
- test architecture;
- revision/checksum machinery;
- generated-doc freshness systems;
- CI depth;
- planning layers;
- tooling stack.

Those may only be introduced when a real PRD-Creator task independently proves the need.

## Current result

The overdeveloped checksum/revision additions were removed in:

`08b6f9d6a98641c5f93932df015cb0d2dffe9a42`

with:

```text
Repository Verify 31381677940  PASS
Production Verify 31381677946  PASS
```

## Future rule

Do not create another numbered parity phase by default.

Use BuildIT as a comparison source when useful, then ask:

1. does PRD-Creator have a real failure or repeated friction here?
2. can the current owner solve it more simply?
3. will this make normal project production easier or harder?
4. what is the minimum useful proof?

If there is no concrete benefit, the result is **No change required**.
