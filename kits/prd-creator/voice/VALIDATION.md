# Voice Validation & Delivery Procedure

Flow 7 validates the exact current Voice chain and decides whether the requested scope is ready. The default human-facing delivery remains the same versioned project HTML used by the PRD.

## Canonical owners

- Flow 5 fields / Owner ID / Moment ID → `EXTRACTION.md` + `work/voice-requirements.md`;
- Flow 6 wording/performance/duration/selection → `PERFORMANCE-WRITING.md` + `work/voice-production.md`;
- 04 presentation → `../production-assets/CONTRACT.md`;
- lifecycle/domain mechanical validation → `../validator/voice_validation.py`;
- validation CLI/public entrypoint → `../validator/validate_voice.py`;
- shared acceptance field/SHA parsing → `../shared/acceptance.py`;
- final Voice acceptance → `work/voice-acceptance.md`.

Do not redefine those schemas here.

## Mechanical validation

Run:

```bash
python kits/prd-creator/validator/validate_voice.py \
  workspace/active/<project>/
```

Every validatable Voice state first reruns the canonical PRD handoff validator. Voice cannot remain current when Flow 4 acceptance/delivery is stale.

Voice source identity is exact:

```text
source_prd_revision
+ source_prd_sha256
```

`source_prd_sha256` must equal the exact current accepted `work/render-data.json` bytes. This applies to `no_voice_required` as well as Voice-producing states.

The validator is lifecycle-aware:

```text
voice_requirements_ready
→ validate current upstream handoff + exact PRD bytes + Flow 5 requirement/topology only

voice_script_ready | voice_validation | needs_revision
→ also validate production source binding + Owner/Type/Speaker parity + HTML freshness when provided

voice_delivery_ready
→ additionally require current HTML, cast selection/profile for every speaker, and exact Voice Acceptance SHA
```

Mechanical validation proves:

- canonical PRD handoff still passes in full;
- accepted PRD version **and exact render-data SHA** remain current;
- Voice state uses the one strict schema and safe project-relative paths;
- Flow 5 requirements use valid Owner ID + Moment ID topology;
- Flow 6 binds exact current requirement bytes;
- Owner ID / Type / Speaker parity is intact;
- HTML binds exact current Voice requirements + production bytes;
- each Voice ID renders on its Owner page inside its stable Moment ID group;
- Prompt bytes match canonical performance text;
- final Voice acceptance binds exact current production bytes.

Mechanical PASS does not prove semantic, naturalness, actor-continuity, expression, pronunciation, visual, or generated-audio quality.

## Semantic / craft readiness

Flow 7 consumes the Flow 6 craft result; it does not create another schema for it.

### Communication Conservation

PASS only when required communication remains present, exclusions are respected, project meaning is intact, source timing truth remains honored, and production polish introduced/deleted no material meaning.

```text
Communication Conservation: PASS | FAIL
```

### Voice Script Readiness

`Voice Script Readiness` is the single persisted semantic/craft decision. Internally it must cover the current preparation model:

```text
Communication Conservation
+ Naturalness
+ Expression Conservation
+ Character Continuity Conservation when applicable
+ Pronunciation Conservation
+ timing / continuity / operator readiness
→ Voice Script Readiness
```

Do **not** add separate persisted acceptance fields for Expression, Character Continuity, Pronunciation, or candidate history merely to mirror Flow 6 reasoning.

Review the following concerns once, proportionally to the represented Voice scope:

- **Communication** — required meaning survives and unsupported meaning was not added;
- **Listener** — wording fits the player's state and communication job;
- **Naturalness** — speech is speakable and register-correct rather than accidental PRD prose;
- **Actor / Character Continuity** — recurring Speakers remain inside the established actor baseline/range/no-drift boundary;
- **Expression** — material emotion, subtext, projection, pacing, reactions, and transitions have sufficient direction;
- **Pronunciation / Language** — critical names, project terms, acronyms, numbers, symbols, and code-switched material have an intentional strategy when risk is material;
- **Performance** — thought groups, punctuation, Audio Tags, and landings serve the approved moment;
- **Timing** — density/duration planning respects source timing truth without sacrificing communication or acting;
- **Continuity** — narrative/dialogue and acting arcs survive clip/turn boundaries;
- **Operator** — exact prompt, cast/voice, duration, surface, pronunciation setup, and special generation context are usable without guessing.

```text
Voice Script Readiness: PASS | FAIL
```

Do not persist per-lens scorecards.

Preparation may establish semantic/craft readiness from text and current production planning. Actual pronunciation approval and generated-audio quality still require heard evidence.

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

`work/voice-acceptance.md` remains intentionally compact:

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

Expression/character/pronunciation readiness remains contained inside the one `Voice Script Readiness` result rather than expanding the machine acceptance format.

## First wrong owner

```text
project/gameplay/story fact or stale PRD handoff
→ PRD / Flow 4 authority

Voice scope / Owner ID / Moment ID / Speaker / Channel / Trigger / Purpose / required communication / source timing
→ Flow 5

wording / actor fit / expression direction / pronunciation strategy / Estimated Duration / cast selection
→ Flow 6

one weak generated take with otherwise-correct canonical production
→ candidate variance review before canonical rewrite

correct canonical Voice + stale/wrong 04
→ renderer/compositor

generated-audio-only issue
→ Generation Mode evidence/settings/voice/surface/context
```

## Delivery gate

Default non-audio `voice_delivery_ready` requires:

- current upstream handoff Mechanical PASS;
- exact Voice source PRD revision + render-data SHA match;
- lifecycle Mechanical PASS;
- Communication Conservation PASS;
- Voice Script Readiness PASS, including all applicable naturalness/expression/character/pronunciation concerns above;
- current consolidated project HTML;
- cast selection/profile for every represented speaker;
- exact accepted Voice Production SHA;
- Project HTML Visual PASS when visual readiness is claimed;
- Critical = 0 and Major = 0;
- truthful optional audio evidence.

It does not imply client sign-off, implementation completion, generated-audio approval, pronunciation approval, or release.
