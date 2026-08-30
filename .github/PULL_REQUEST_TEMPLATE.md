## Purpose

Describe the one logical outcome this pull request delivers.

## Target boundary

- [ ] `develop` work / review only
- [ ] `develop` → `Local` verified integration promotion
- [ ] `Local` → `main` explicit stable/release promotion

## Scope

**Changed owners:**

**Intentionally not changed:**

## Verification

- [ ] Cheapest relevant local/static proof completed
- [ ] Repository Verify when applicable
- [ ] PRD Verify when applicable
- [ ] Voice Verify when applicable
- [ ] Local promotion gate for `develop` → `Local`
- [ ] Stable release gate for `Local` → `main`

Evidence / relevant result:

## Repository hygiene

- [ ] No credentials, private client/source material, or live project package data added
- [ ] No generated/transfer-only artifact was promoted to source of truth
- [ ] No unrelated cleanup/refactor was bundled into this change
- [ ] Package version was changed only if the product/contract version rule requires it

## Promotion synchronization

For promotion PRs, state the required post-merge sync:

```text
resulting promoted commit
→ synchronize back to lower branch(es)
```

Do not continue independent development from stale branch ancestry after promotion.
