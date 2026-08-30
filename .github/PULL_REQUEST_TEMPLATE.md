## Purpose

Describe the one logical outcome this pull request delivers.

## Target boundary

- [ ] `develop` work / review only
- [ ] `develop` → `Local` verified integration promotion
- [ ] `main` migration/release work explicitly requested

## Scope

**Changed owners:**

**Intentionally not changed:**

## Verification

- [ ] Cheapest relevant local/static proof completed
- [ ] Repository Verify when applicable
- [ ] PRD Verify when applicable
- [ ] Voice Verify when applicable
- [ ] Local promotion gate for `develop` → `Local`

Evidence / relevant result:

## Repository hygiene

- [ ] No credentials, private client/source material, or live project package data added
- [ ] No generated/transfer-only artifact was promoted to source of truth
- [ ] No unrelated cleanup/refactor was bundled into this change
- [ ] Package version was changed only if the product/contract version rule requires it

## Local promotion contract

For `develop` → `Local` promotion:

- [ ] This PR represents one approved logical update
- [ ] Merge method will be **Squash and merge**
- [ ] Result must add exactly **one** new commit to `Local`
- [ ] After merge, `develop` will be synchronized/reset to the resulting `Local` HEAD before new work begins

Do not continue development from the pre-squash commit chain after promotion.

`main` remains outside the current clean-history lineage until an explicit main migration/release decision says otherwise.
