# Voice Validation & Delivery

Status: active Flow 7 policy

## Purpose

Flow 7 decides whether the current Voice production chain is safe to deliver. Default non-audio delivery is the same versioned project HTML containing PRD core + `04 Production Assets → matching Owner ID → Moment → AUDIO`.

## Canonical sequence

```text
voice_script_ready
→ mechanical lifecycle validation
→ Communication Conservation
→ integrated Voice Script Readiness
→ current consolidated HTML
→ visual evidence when claimed
→ optional generated-audio evidence
→ voice_delivery_ready | needs_revision | blocked
```

## One lifecycle-aware mechanical validator

Run:

```bash
python kits/prd-creator/validator/validate_voice.py \
  workspace/active/<project>/
```

The same validator is used from Flow 5 onward. At Flow 7 it proves:

```text
accepted PRD handoff revision
= voice-state source_prd_revision
= render-data document.version
= voice-requirements Source PRD revision
= voice-production Source Voice Requirements revision

voice-production Source Voice Requirements SHA
= exact current voice-requirements.md bytes

Voice requirement Owner ID / Type / Speaker
= Voice Production Owner ID / Type / Speaker

Voice Owner IDs
∈ current accepted PRD topology
```

When project HTML exists it additionally proves:

- HTML binds exact current `voice-requirements.md` SHA-256;
- HTML binds exact current `voice-production.md` SHA-256;
- each Voice ID appears on the Production Assets page owned by its exact Owner ID;
- each prompt is byte-equivalent to canonical performance text after HTML escaping;
- the natural Flow 5 `Moment` is present in that page;
- compact Voice identity remains current.

Mechanical PASS does not establish semantic or visual quality.

## Canonical state

Flow 7 continues the same `state/voice-state.yaml` schema used by Flow 5/6:

```yaml
status: voice_validation
source_handoff: state/handoff-state.yaml
source_prd_revision: <accepted document.version>
canonical_prd: work/content.md
requirements: work/voice-requirements.md
production: work/voice-production.md
project_html: output/v<accepted document.version>/prd.html
```

Do not add `delivery_scope`, `source_revision`, `flow`, `next_step`, or another lifecycle alias. Historical archived files may retain retired metadata, but current state must use the canonical schema.

## Communication Conservation

PASS only when every material `Must communicate` fact remains clear, every `Must not add/repeat` guardrail remains respected, project meaning is intact, authoritative timing truth remains honored, and Flow 6 polish did not introduce or delete material meaning.

Record:

```text
Communication Conservation: PASS | FAIL
```

## Integrated Voice Script Readiness

Review Communication, Listener, Character, Performance, Timing, Continuity, and Operator concerns once as one integrated result:

```text
Voice Script Readiness: PASS | FAIL
```

Do not create per-lens scorecards.

## Production Assets HTML

When visual readiness is claimed, verify:

- accepted 01–03 page/navigation identity remains intact;
- 04 is additive rather than a separate Voice document;
- each Voice resource is under its accepted Owner ID and natural Moment;
- resource identity is `<Character> — <Line Title>`;
- Function, Voice selection/profile, ElevenLabs Model = `Eleven v3`, Estimated Duration, and Prompt are readable;
- Flow 5 Trigger/Purpose/requirement bullets/source refs and internal reasoning do not leak into reader-facing 04;
- copied Prompt remains exact canonical production bytes;
- layout is readable at the browser widths being claimed.

Record:

```text
Project HTML Visual: PASS | FAIL | NOT PROVEN
```

Static validation proves structure/freshness only. Visual PASS requires rendered/browser evidence.

## Voice selection boundary

Preparation may use an explicit target profile before a commercial actor voice is selected. However `voice_delivery_ready` requires a non-empty Voice Cast selection/profile for every speaker represented in canonical production.

Actual Generation Mode requires the intended generation voice, not merely an abstract profile.

## Audio evidence

Audio remains a separate optional evidence scope:

```text
Audio Evidence: not_provided | partial_review | reviewed_passed | reviewed_with_findings
```

Do not infer heard quality or measured duration from script/HTML appearance.

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

Critical/Major findings block delivery.

## First wrong owner

```text
project/gameplay/story fact
→ PRD authority

Voice Owner ID / Moment / scope / Speaker / Channel / Trigger / Purpose / required communication / source timing
→ Flow 5

wording / performance / Estimated Duration / Voice Cast selection
→ Flow 6

correct canonical Voice but stale/wrong 04 HTML
→ shared renderer/compositor

generated-audio-only issue
→ Generation Mode evidence/settings
```

## Bounded revision

```text
change
→ first wrong owner
→ affected Voice scope
→ regenerate downstream canonical/HTML only where invalidated
→ mechanical lifecycle validation
→ semantic/visual review only where invalidated
→ stop
```

Voice-only production changes do not reopen PRD acceptance while accepted PRD meaning remains unchanged.

## Delivery gate

`voice_delivery_ready` requires:

- lifecycle-aware Mechanical PASS;
- exact requirement/production/HTML freshness bindings;
- Owner ID / Type / Speaker parity;
- a Voice Cast selection/profile for every represented speaker;
- Communication Conservation PASS;
- Voice Script Readiness PASS;
- current consolidated project HTML;
- Project HTML Visual PASS when visual readiness is claimed;
- Critical = 0 and Major = 0;
- truthful optional audio evidence;
- no stale upstream PRD revision.

It does not imply audio approval, client sign-off, implementation completion, or release.
