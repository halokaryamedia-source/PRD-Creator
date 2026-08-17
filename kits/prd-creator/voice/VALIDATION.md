# Voice Validation & Delivery Procedure

Flow 7 validates the exact current Voice revision and decides whether the requested production scope is ready.

The default human-facing presentation is the same `output/v<document.version>/prd.html` project document used by the PRD.

## Entry

Start from the current Voice state and read only the canonical requirements/script plus `output/v<document.version>/prd.html` when consolidated HTML is in scope. Reopen accepted PRD only when a project fact needs verification.

## Mechanical validation

Run:

```bash
python kits/prd-creator/validator/validate_voice.py \
  workspace/active/<project>/
```

Mechanical validation always checks current Voice ID/Type/Speaker parity and canonical script structure. It also checks that the current accepted PRD handoff, `voice-state.yaml.source_prd_revision`, `render-data.document.version`, the Flow 5 `Source PRD revision`, and the Flow 6 source revision agree. The `Source Voice Requirements` SHA-256 in `voice-production.md` must match the exact current `work/voice-requirements.md` bytes.

When `output/v<document.version>/prd.html` exists, it also checks Voice section/prompt identity and exact canonical payload parity. The shared PRD Creator 04 regression owns the current visible AUDIO field/layout contract; do not duplicate that compositor contract inside the Voice validator.

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

When the consolidated project HTML is claimed visually current, verify:

- the accepted PRD sidebar hierarchy/page identities remain unchanged;
- gameplay/objective sections remain under `03 Development`;
- `04 Production Assets` is additive and links matching gameplay/shared pages rather than a separate Voice category;
- Voice appears as `AUDIO` inside the correct natural gameplay moment;
- the resource title is `<Character> — <Line Title>`;
- visible fields are Function, Voice Preset, ElevenLabs Model, Estimated Duration, and Prompt;
- `ElevenLabs Model` displays `Eleven v3`;
- the copied Prompt remains exact canonical performance content;
- performance-direction tags remain visually distinct from spoken dialogue;
- separate visible Speaker, Flow 5 Context/Trigger, line-count, Primary Speaker, and Voice Setup presentation is absent under the current 04 contract;
- Flow 5 Purpose/requirements/source refs/reasoning/QA stay out of the visible resource;
- no clipping/overlap or obvious visual break from the PRD design language exists.

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
canonical Voice wording/duration → Flow 6
correct canonical data + wrong Production Assets HTML → kits/prd-creator/ renderer/compositor owner
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