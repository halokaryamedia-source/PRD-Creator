# System Integration Proof — The Clockwork Vault

Status: `PASSED_WITH_RESOLVED_FINDING`
Proof revision: `integration-1`
Evidence owner: `docs/knowledge/operations/system-integration-proof.md`
Scope: Flow 2 → Flow 7 replacement pipeline on one real project

## Source Boundary

- `SRC-001` — `The Clockwork Vault - Adventure Map - Final Review.html`; authoritative mature project source for this migration proof; SHA-256 `f4d58341ce3cb7fb17bfc9986b5df67a23058d1b94a0bc78c1dad09abdd445d0`.
- `SRC-002` — legacy `The Clockwork Vault - Voice Production v2.docx`; generated/reference-only and never allowed to supply missing upstream facts; SHA-256 `5b331ba213e9a045398fd7edfc4765f915545c744a0504aca525a5ff5e60a056`.

This proof intentionally tests the replacement system using an existing real production project rather than a synthetic fixture.

## Flow 2 — Source Intake & Requirement Recovery

**PASS**

- 2 sources inventoried with explicit authority roles;
- 129 material requirements recovered from the mature PRD;
- material conflicts: 0;
- unresolved proposals: 0;
- blocked requirements: 0;
- result: `ready_for_prd`.

Because the source was already mature, Flow 2 mainly proved provenance, authority, persistence, and clean separation from the legacy downstream Voice artifact.

## Flow 3 — Canonical PRD Generation

**PASS**

- canonical `work/content.md` created from accepted project facts;
- derived `work/render-data.json` created without using the legacy Voice artifact as authority;
- active approved-template renderer produced `output/final.html`;
- 6 gameplay packages + 4 global development pages migrated;
- renderer output produced 29 expected project pages.

### Integration observation `INT-001`

Current renderer has no dedicated `Area Size` column. Source area-size values were preserved losslessly inside Build & Visual (`Area Size: …`). This is a Suggestion only; no production meaning was lost and no renderer redesign was justified by this project.

## Flow 4 — PRD Validation & Team Handoff

**PASS**

Mechanical validator:

- file/placeholder checks passed;
- HTML IDs unique;
- all 29 expected pages present;
- fragment navigation reachable;
- browser title correct.

Semantic perspectives:

- New Reader: PASS;
- Level Designer: PASS;
- Developer: PASS;
- Project Consistency: PASS.

Result: `handoff_ready` with Critical=0, Major=0, Minor=0, Suggestion=1 (`INT-001`).

Browser screenshot/interaction proof is not claimed because the current container cannot start headless Chromium cleanly without DBus. This is recorded as environment evidence, not hidden as a project pass.

## Flow 5 — Voice Requirement Extraction

**PASS**

- accepted PRD defines Custodian Vex as persistent in-world guide/dialogue;
- no accepted radio/communicator exists, so **no Radio Communication was invented**;
- 21 justified voice requirements extracted across 6 gameplay sections;
- types: 12 Main Story + 9 Direct NPC Dialogue;
- every moment has accepted speaker/channel/trigger/purpose and source traceability.

During extraction, one candidate wording attempted to expose an internal platform-scoring/independent-progress bonus rule. Flow 5 correctly rejected that as non-player-facing implementation detail before script production. No upstream project decision was changed.

## Flow 6 — ElevenLabs Performance Script Production

**PASS after downstream visual fix**

- 21 canonical performance entries created with exact Flow 5 Voice ID/Type parity;
- no extra/missing Voice ID;
- no radio layer introduced;
- `output/Voice Production.docx` built from canonical `work/voice-production.md`.

The legacy Voice Production v2 file remained comparison/reference-only throughout scripting.

## Flow 7 — Voice Validation & Delivery

**PASS after one real finding → root fix → rebuild → revalidation cycle**

Mechanical validation initially passed. Mandatory rendered-page visual QA then found a real builder defect:

### `INT-002` — blank page before Ending

- Severity: Major while unresolved;
- Owner: Flow 6 `builder/build_docx.py`;
- Cause: explicit `add_page_break()` paragraph before each later section could create an empty page when the previous section already ended at a natural page boundary;
- Fix: apply `page_break_before = True` to the following section heading instead of inserting a break paragraph;
- Rebuild: completed;
- Current DOCX: 8 rendered pages;
- Every page inspected after final rebuild;
- Blank-page/clipping/overlap/missing-content findings: 0;
- Flow 7 mechanical validator rerun: PASS.

Final state: `voice_delivery_ready`, delivery scope `script_docx`, audio evidence `not_provided`.

No claim is made about generated ElevenLabs audio quality because no actual generated audio was supplied.

## System Result

The active replacement architecture has now been exercised on one real project through **Flow 2 → Flow 7**.

The proof demonstrated both success paths and a real corrective loop:

```text
real source
→ recovered state
→ canonical PRD
→ rendered PRD
→ PRD acceptance/handoff
→ voice requirements
→ performance script/DOCX
→ mechanical voice validation
→ visual defect found
→ root builder fix
→ rebuild
→ revalidation
→ voice_delivery_ready
```

This satisfies the required precondition for the final `Production Document Builder/` retirement audit. The Archived package must still be audited against active owners before deletion; this proof alone is not permission to delete an unexamined dependency.

## Evidence Storage Boundary

The real project was exercised with full source, canonical content, rendered HTML, canonical Voice script, and generated DOCX in the execution workspace. This repository note is the durable proof owner; transient project copies and generated binary/page-image QA artifacts are not promoted into reusable repository architecture. Source hashes and all material pass/fail/revision evidence needed for continuity are recorded here.
