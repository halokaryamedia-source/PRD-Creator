# Voice Validation & Delivery Procedure

Flow 7 validates the exact current Voice chain and decides whether the requested scope is ready. The default human-facing delivery remains the same versioned project HTML used by the PRD.

## Canonical owners

- Flow 5 fields / Owner ID / Moment ID → `EXTRACTION.md` + `work/voice-requirements.md`;
- Flow 6 wording/performance/duration/selection → `PERFORMANCE-WRITING.md` + `work/voice-production.md`;
- 04 presentation → `../production-assets/CONTRACT.md`;
- lifecycle machine validation → `validator/validate_voice.py`;
- final Voice acceptance → `work/voice-acceptance.md`.

Do not redefine those schemas here.

## Mechanical validation

Run:

```bash
python kits/prd-creator/validator/validate_voice.py \
  workspace/active/<project>/
```

The validator is lifecycle-aware:

```text
voice_requirements_ready
→ validate Flow 5 requirement/revision/topology only

voice_script_ready | voice_validation | needs_revision
→ also validate production source binding + Owner/Type/Speaker parity + HTML freshness when provided

voice_delivery_ready
→ additionally require current HTML, cast selection/profile for every speaker, and exact Voice Acceptance SHA
```

Mechanical validation proves:

- accepted PRD revision identity is current;
- Voice state uses the one strict schema and safe project-relative paths;
- Flow 5 requirements use valid Owner ID + Moment ID topology;
- Flow 6 binds exact current requirement bytes;
- Owner ID / Type / Speaker parity is intact;
- HTML binds exact current Voice requirements + production bytes;
- each Voice ID renders on its Owner page inside its stable Moment ID group;
- Prompt bytes match canonical performance text;
- final Voice acceptance binds exact current production bytes.

Mechanical PASS does not prove semantic or visual quality.

## Communication Conservation

PASS only when required communication remains present, exclusions are respected, project meaning is intact, source timing truth remains honored, and production polish introduced/deleted no material meaning.

```text
Communication Conservation: PASS | FAIL
```

## Integrated Voice Script Readiness

Review Communication, Listener, Character, Performance, Timing, Continuity, and Operator concerns once:

```text
Voice Script Readiness: PASS | FAIL
```

Do not persist per-lens scorecards.

## Project HTML review

Flow 7 does not redefine 04 layout. When visual readiness is claimed, verify Voice-specific invariants:

- accepted 01–03 navigation/page identity remains unchanged;
- Voice is under the page resolved from Owner ID;
- `Moment ID` resolves to the correct natural moment;
- rendered resource maps to the correct Voice ID;
- copied Prompt remains exact;
- internal Flow 5/reasoning fields do not leak;
- no clipping/overlap prevents reading the current 04 AUDIO presentation.

```text
Project HTML Visual: PASS | FAIL | NOT PROVEN
```

Static inspection cannot establish visual PASS.

## Acceptance record

`work/voice-acceptance.md`:

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
Accepted Voice Production SHA256: <exact current work/voice-production.md SHA-256>
```

The production SHA is required for `voice_delivery_ready`. Any canonical production edit after review invalidates final acceptance.

## First wrong owner

```text
project/gameplay/story fact
→ PRD authority

Voice scope / Owner ID / Moment ID / Speaker / Channel / Trigger / Purpose / required communication / source timing
→ Flow 5

wording / performance / Estimated Duration / cast selection
→ Flow 6

correct canonical Voice + stale/wrong 04
→ renderer/compositor

generated-audio-only issue
→ Generation Mode evidence/settings
```

## Delivery gate

Default non-audio `voice_delivery_ready` requires:

- lifecycle Mechanical PASS;
- Communication Conservation PASS;
- Voice Script Readiness PASS;
- current consolidated project HTML;
- cast selection/profile for every represented speaker;
- exact accepted Voice Production SHA;
- Project HTML Visual PASS when visual readiness is claimed;
- Critical = 0 and Major = 0;
- truthful optional audio evidence.

It does not imply client sign-off, implementation completion, generated-audio approval, or release.
