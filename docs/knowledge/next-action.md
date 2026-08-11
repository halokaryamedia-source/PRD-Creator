# Next Action

Updated: 2026-08-11

## Current Status

`PRD_GOLDEN_MANDATORY_CONTRACT_IMPLEMENTED_NEXT_REPRESENTATIVE_PROOF`

Working branch: **`Local` only**.

## What changed

PRD Flow 2–4 no longer relies on scattered Golden guidance.

The single semantic owner is now:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

It defines the complete mandatory gameplay PRD family:

```text
Overview
Gameplay Flow
  The Journey Begins
  one flow page per gameplay package
Global Development
  Development Overview
  Game System
  Data and Reset
  Gameplay Development
Gameplay Packages
  Gameplay Overview
  Level Design
  Developer
```

For `N` gameplay packages the fixed shell produces `6 + 4N` pages.

## Mandatory concern rule

A required concern may resolve only as:

```text
Defined
Explicit No
Not Applicable
Blocked
```

A mandatory concern may not silently disappear because source or render data omitted it.

Examples of important explicit negative states:

```text
No Objective Score
No hard timeout
No permanent fail
Do not display score to the player
Do not export score in telemetry
```

These meanings remain distinct.

## Result/scoring behavior

Every package explicitly carries:

- Objective Score **or** `No Objective Score`;
- calculation/completion rule;
- final-result relationship;
- player-facing display behavior;
- telemetry/export behavior.

The renderer now exposes these distinctions rather than compressing them away.

## Authoring and review behavior

- Gameplay Flow is a chronological player journey, not a task summary.
- Global Development always preserves its four fixed functions.
- Level Design always preserves Overview, Design Flow, Build Requirements, and Important Build Notes.
- Developer always preserves Overview, Development Flow, Development Requirements, Scoring/Result, reset/interruption behavior, and Important Development Notes.
- Flow 3 applies one bounded Humanize pass after meaning is complete.
- Flow 4 checks semantic usability against the same single contract; it does not maintain another checklist.

## Deterministic enforcement

The renderer fails before writing HTML when the fixed mandatory shell is structurally incomplete.

Focused PRD regression coverage now uses a complete Golden-contract fixture rather than a minimal skeleton.

Current implementation proof:

```text
PRD Verify #68 — PASS
```

Voice verification is now independent:

```text
Voice Verify #1 — PASS
```

PRD-only work no longer reruns Voice tests by default.

## Deliberately not added

- no word-count or row-count quality gate;
- no semantic similarity engine;
- no permanent source-to-output matrix;
- no generic schema framework;
- no new checksum chain;
- no mobile QA as a default;
- no Voice feature changes.

The existing `content.md → render-data.json` SHA remains unchanged in this slice and is still a separate simplification candidate.

## Evidence boundary

The previous AFTERSHOCK sample remains diagnostic/mechanical evidence only. It is not semantic-quality proof for this new contract.

The new fixed contract still needs one representative real-project run to prove that Flow 2 fills the shell correctly and Flow 3 produces complete, human-readable content in practice.

## Next Step

Run **one new representative PRD Flow 2–4 production proof** using the Golden Mandatory Contract, then inspect the generated HTML with the user before closing PRD Flow 2–4. Review semantic quality first and use only targeted **desktop** visual sanity; do not run mobile QA or unrelated Voice validation.
