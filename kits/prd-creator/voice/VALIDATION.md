# Voice Validation & Delivery Procedure

Flow 7 validates the exact current Voice revision and decides whether the requested production scope is ready.

The default human-facing presentation is the same `output/v<document.version>/prd.html` project document used by the PRD.

## Entry

Start from the current Voice state and read only the canonical requirements/script plus `output/v<document.version>/prd.html` when consolidated HTML is in scope. Reopen accepted PRD only when a project fact needs verification.

For a requested multi-ID Voice revision/generation batch, enter Flow 7 after the requested canonical Voice state is stable. Do not rerun full project validation or consolidated HTML delivery after each intermediate Voice ID unless the user explicitly requests per-line handoff.

## Stable Voice section identity

Each `##` gameplay section in `work/voice-production.md` must declare one stable `Owner ID` before its Voice entries:

```text
Owner ID: journey:<gameplay_flow.id>
Owner ID: package:<package.id>
```

The Owner ID determines where canonical Voice is presented in 04 Production Assets. Display titles may change without changing identity. Duplicate or unknown Owner IDs are invalid; the compositor does not map Voice to the PRD by normalized title matching.

Voice entry IDs (`VO-...`) remain the identity for individual canonical lines.

## Mechanical validation

Run:

```bash
python kits/prd-creator/validator/validate_voice.py \
  workspace/active/<project>/
```

Mechanical validation checks current Voice ID/Type/Speaker parity, stable section Owner IDs, and canonical script structure. It also checks that the current accepted PRD handoff, `voice-state.yaml.source_prd_revision`, `render-data.document.version`, the Flow 5 `Source PRD revision`, and the Flow 6 source revision agree. The `Source Voice Requirements` SHA-256 in `voice-production.md` must match the exact current `work/voice-requirements.md` bytes.

Machine-owned `*.yaml` state is parsed as YAML, not with line-regex emulation.

When `output/v<document.version>/prd.html` exists, validation also checks Voice section/prompt identity and exact canonical payload parity. The shared PRD Creator 04 regression owns the visible AUDIO field/layout contract; do not duplicate that compositor contract inside the Voice validator.

Mechanical PASS does not prove semantic or visual quality.

## Communication Conservation

PASS only when required communication remains present, exclusions are respected, project meaning remains intact, and production polish has not introduced or deleted material meaning.

Record one result:

```text
Communication Conservation: PASS | FAIL
```

## Integrated Voice Script Readiness

Review Communication, Listener, Character, Performance, Timing, Continuity, and Operator concerns once as one integrated result:

```text
Voice Script Readiness: PASS | FAIL
```

Do not create separate persisted scorecards for these lenses.

## Production Assets HTML review

The exact visible `04 Production Assets` AUDIO presentation contract is owned by `../production-assets/CONTRACT.md` and implemented by the shared renderer/compositor. Flow 7 verifies current Voice parity against that owner; it does not redefine the field schema or layout here.

When consolidated project HTML is claimed visually current, verify only the Voice-specific delivery invariants:

- accepted PRD sidebar hierarchy/page identities remain unchanged;
- Voice appears under the page resolved from its stable Owner ID;
- the rendered Voice resource maps to the correct canonical Voice entry;
- rendered/copied Prompt preserves the exact canonical performance payload;
- Flow 5 requirements, source refs, reasoning, QA, and other non-presentation metadata do not leak into the visible resource;
- no clipping/overlap or obvious visual break prevents the current 04 AUDIO contract from being read correctly.

Record:

```text
Project HTML Visual: PASS | FAIL | NOT PROVEN
```

Static inspection cannot establish visual PASS without actual rendered/browser evidence.

## Optional scope

Audio evidence is separate from non-audio script/project-HTML readiness and must be reported honestly.

## First wrong owner

```text
project/gameplay/story fact → PRD authority
Voice scope/context → Flow 5
canonical Voice wording/duration/Owner ID → Flow 6
correct canonical data + wrong Production Assets HTML → renderer/compositor owner
```

## Acceptance record

Keep `work/voice-acceptance.md` compact:

```text
# Voice Acceptance
Status: needs_revision | voice_delivery_ready
Mechanical: PASS | FAIL
Voice Script Readiness: PASS | FAIL
Communication Conservation: PASS | FAIL
Project HTML Visual: PASS | FAIL | NOT PROVEN
Audio Evidence: not_provided | partial_review | reviewed_passed | reviewed_with_findings
Findings: <only when findings exist>
Critical: N
Major: N
```

Critical or Major findings block delivery.

## Delivery gate

For default non-audio delivery, `voice_delivery_ready` requires Mechanical PASS, Communication Conservation PASS, Voice Script Readiness PASS, current consolidated project HTML, visual PASS when claimed, zero Critical/Major findings, and truthful evidence boundaries.

It does not imply client sign-off, implementation completion, or release.
