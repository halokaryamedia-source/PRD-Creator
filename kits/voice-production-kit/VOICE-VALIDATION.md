# Voice Validation & Delivery Procedure

Flow 7 validates the exact current Voice revision and decides whether the requested production scope is ready.

The default human-facing presentation is the same `output/v<document.version>/prd.html` project document used by the PRD. DOCX is optional export only.

## Entry

Start from the current Voice state and read only the canonical requirements/script plus `output/v<document.version>/prd.html` when consolidated HTML is in scope. Reopen accepted PRD only when a project fact needs verification.

## Mechanical validation

Run:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation always checks current Voice ID/Type/Speaker parity and canonical script structure.

When `output/v<document.version>/prd.html` exists, it also checks section/page parity, per-line position/context presentation, exact Flow 5 Trigger Context, and exact canonical prompt payload. DOCX is checked only when that optional export exists.

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

When the consolidated project HTML is claimed current, verify:

- the accepted PRD sidebar hierarchy/page identities remain unchanged;
- gameplay/objective sections remain under `03 Development`;
- `04 Production Assets` is additive and links the matching gameplay/shared pages rather than a separate Voice category;
- a gameplay page containing Voice shows `Audio → Voice Production`;
- every matching Production Assets navigation link shows gameplay section title + accepted PRD package label;
- sidebar labels wrap naturally and are not clipped at the desktop widths being claimed;
- section order matches canonical Voice order;
- each gameplay page with Voice shows title, accepted PRD label/context, Voice line count, Primary Speaker, and compact Voice Setup;
- each line shows title, `<PRD package label> · Voice Line X/Y`, exact Flow 5 Trigger as Context, Speaker, Estimated Duration, exact canonical prompt, and Copy Prompt;
- the copied payload remains exact;
- Flow 5 Purpose/requirements/source refs/reasoning/QA stay out of the visible page;
- no clipping/overlap or obvious visual break from the PRD design language exists.

Record:

```text
Project HTML Visual: PASS | FAIL | NOT PROVEN
```

Static inspection cannot establish visual PASS without actual rendered/browser evidence.

## Optional scopes

DOCX is reviewed only when that export exists/is claimed. Audio evidence is separate from non-audio script/project-HTML readiness and must be reported honestly.

## First wrong owner

```text
project/gameplay/story fact → PRD authority
Voice scope/context → Flow 5
canonical Voice wording/duration → Flow 6
correct canonical data + wrong Production Assets HTML → PRD renderer compositor
optional DOCX-only issue → Voice DOCX builder
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
DOCX Visual: PASS | FAIL | NOT PROVEN   # only when DOCX exists/is claimed
Findings: <only when findings exist>
Critical: N
Major: N
```

Critical or Major findings block delivery.

## Delivery gate

For default non-audio delivery, `voice_delivery_ready` requires Mechanical PASS, Communication Conservation PASS, Voice Script Readiness PASS, current consolidated project HTML, visual PASS when claimed, zero Critical/Major findings, and truthful evidence boundaries.

It does not imply client sign-off, implementation completion, or release.
