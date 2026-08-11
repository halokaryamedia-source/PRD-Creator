# Next Action

Updated: 2026-08-11

## Current Status

`PRD_ARCHITECTURAL_CLEANUP_COMPLETE_AWAIT_USER_DIRECTION`

Working branch: **`Local` only**.

## Current system

Single semantic owner:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

Current production path:

```text
Flow 2
source authority
→ requirement truth
→ one integrated readiness pass
→ resolve material gaps
→ ready_for_prd

Flow 3
content.md
→ Humanize
→ render-data.json
→ generic approved template
→ final.html

Flow 4
mechanical validation
→ integrated semantic review
→ targeted desktop visual sanity only when required/available
→ handoff
```

## Cleanup now complete

The active PRD Generator now avoids the main AI-slop patterns found during review:

- no reference-project naming in active template/component/runtime hooks;
- no internal presentation patch/version history in the template;
- no stacked UI patch layers;
- no stale package-presentation terminology inherited from old project-specific implementations;
- no semantic-reference naming inside generic mechanical composition checks;
- no ritualized multi-scan Flow 2 sequence;
- no duplicate detailed PRD procedure across skill/workflow/rules/validation owners;
- no unused legacy table helper kept for hypothetical compatibility;
- current evidence/continuation docs do not act as debugging-history logs.

The real project `document.version` remains valid document metadata.

## Current proof

```text
PRD Verify #99 — PASS
```

This is repository/regression evidence only, not representative semantic/browser proof.

## Hold boundary

Do not run representative project/browser/mobile/Voice proof unless explicitly requested. The current user direction remains architectural/content cleanup first.

## Next Step

Wait for the user's next concrete PRD Generator review request or explicit approval to begin the representative semantic + targeted desktop proof.
