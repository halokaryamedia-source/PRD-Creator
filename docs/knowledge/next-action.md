# Next Action

## Current Status

`CLOCKWORK_CANONICAL_REVISION_READY_FOR_PROJECTION`

The Clockwork Vault bounded gameplay revision for Objectives 1-4 is approved and persisted in current requirement state and canonical `workspace/active/the-clockwork-vault/work/content.md`.

Objective 1 now uses the approved partial-display clue model: the door display reveals only Middle = Brown; the hidden final state is Left Orange + pulse, Middle Brown + steady, Right Purple + steady. Twelve books are scattered without reading order and use a 2 mechanic-rule + 8 useful clue + 2 harmless decoy structure. The books help recover missing target information rather than teach all twelve lever-to-color mappings; the fixed color mapping is learned through lever experimentation and immediate lamp feedback. A player who finds useful books earlier by chance may solve faster, and reading all twelve is not required.

The non-Voice `work/asset-requirements.md` is current for the canonical revision and includes the final twelve book texts, partial target display, instruction UI, required custom gameplay objects, and authored presentation events.

The supplied Objective 4 HTML remains a supporting technical-layout source only. Its coordinates and preview implementation are not copied into player-facing PRD content.

The previous `work/render-data.json`, versioned `prd.html`, AI context/index, and Voice canonical sources intentionally remain stale because they still reflect the previous gameplay projection. Handoff therefore remains `revision_in_progress` rather than being falsely restored to ready.

## Next Step

Regenerate `work/render-data.json` and the versioned delivery bundle from the current canonical Clockwork revision, then run the relevant PRD validation before restoring `handoff_ready` and reopening the affected Voice Production scope.
