# Voice Validation & Delivery Procedure

Flow 7 validates the current Flow 6 script/DOCX revision and, when audio is in scope, verifies that reviewed audio corresponds to the current canonical Eleven v3 prompt.

## Entry

Start from `state/voice-state.yaml: voice_script_ready` for the current Voice Requirements revision.

Read in this order:

1. `VOICE-VALIDATION.md`;
2. `work/voice-requirements.md`;
3. `work/voice-production.md`;
4. `SOUNDMAKER.md` when v3 performance quality or generated-prompt alignment is in scope;
5. `DOCX-FORMAT.md` when DOCX is in scope;
6. accepted PRD only when a project fact/term needs verification.

## Step 1 — Mechanical validator

Run:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

A pass proves parity/integrity only. It does not approve wording, v3 performance, pronunciation, layout, or audio.

## Step 2 — Requirement-by-requirement review

For each Voice ID, compare canonical performance text to Flow 5 requirement.

PASS only when:

- Purpose is satisfied;
- all material `Must communicate` facts are present;
- `Must not add/repeat` guardrails are respected;
- Type is correct;
- approved speaker/channel/trigger remain compatible;
- no project fact was invented during SoundMaker/script polish.

Do not demand literal sentence matching. Meaning and production function are the test.

## Step 3 — Terminology / pronunciation

Audit official project terms across the full script.

Create pronunciation notes only for material risk. Use:

- `confirmed` — explicit approved pronunciation evidence exists;
- `accepted_as_written` — creative owner accepts written form;
- `needs_confirmation` — do not claim pronunciation-ready.

Do not claim a spelling guarantees Eleven v3 pronunciation.

## Step 4 — speaker/channel/trigger continuity

Check dialogue perspective and wording against approved speaker/channel/trigger/function.

Route defects to the owning upstream source rather than inventing metadata in the audit.

## Step 5 — SoundMaker v3 performance continuity

Review the whole project, not each line in isolation.

Check:

- consistent narrator/character identity;
- emotional changes follow scene reasons rather than random escalation;
- long lines use meaningful spoken beats rather than one dense specification paragraph;
- direction vocabulary is concise/compatible;
- no contradictory/redundant tag stacking dominates the prompt;
- CAPS is selective;
- ellipses/em dashes/line breaks are purposeful;
- reactions occur at sensible timeline positions;
- duration labels remain estimates rather than audio claims;
- no SSML `<break>` is used for v3.

If a wording/notation defect exists, reopen canonical `work/voice-production.md`; never patch DOCX/audio as the authoritative fix.

## Step 6 — DOCX visual QA

Render `output/Voice Production.docx` and inspect every page when DOCX is in scope.

Check clipping/overlap, orphaned labels, hierarchy, panel legibility, line breaks, glyphs, spacing, and shading.

## Step 7 — audio evidence

If no audio is supplied:

```text
Audio Evidence: not_provided
```

This does not block script/DOCX delivery. It only blocks audio-quality claims.

If audio is in scope:

1. identify the exact prompt actually generated;
2. identify the actual v3 voice and Stability/visible generation setting when relevant to the finding;
3. if the user edited the prompt before generation, synchronize that exact version into `work/voice-production.md`;
4. review the actual audio against the current Voice Requirement and SoundMaker quality contract;
5. do not preserve an older script/DOCX acceptance as current against newer approved prompt/audio evidence.

### Actual audio quality gate

For each reviewed take, check only dimensions material to the line:

- **meaning / intelligibility** — required information is clearly understood;
- **voice identity** — the intended narrator/character remains coherent without material persona/timbre drift;
- **emotional movement** — intended scene-driven state changes are audible and a long line does not remain one flat tone when the script requires real movement;
- **pacing / breath** — important beats have enough space to land without damaging urgency or clarity;
- **emphasis / landing** — important words and the final beat receive the intended stress/payoff;
- **naturalness** — tags, reactions, CAPS, punctuation, and pauses do not create obvious overacting, robotic segmentation, or artificial jumps;
- **pronunciation** — material names/terms/numbers are acceptable and consistent;
- **duration** — the actual file meets the requested timing constraint when timing is part of the task.

Disposition:

```text
all material dimensions pass
→ reviewed_passed / approve

one odd take + prompt/voice/settings still sound
→ review alternative / eligible regeneration

same point repeatedly fails
→ reopen Flow 6 / revise SoundMaker prompt

required performance consistently exceeds selected voice
→ voice-fit finding
```

Do not infer immersion from tag count or script appearance. Audio-quality PASS requires the heard performance itself.

## Acceptance file

Create/update `work/voice-acceptance.md` using the compact format defined by `docs/foundation/07-voice-validation-delivery.md`.

Critical or Major findings always block delivery.

## State transition

For script + DOCX only:

```yaml
flow: 7
status: voice_delivery_ready
requirements: work/voice-requirements.md
script: work/voice-production.md
docx: output/Voice Production.docx
acceptance: work/voice-acceptance.md
mechanical: passed
coverage: passed
terminology_pronunciation: passed
speaker_channel_trigger: passed
performance_continuity: passed
docx_visual: passed
audio_evidence: not_provided
delivery_scope: script_docx
next_step: complete_or_soundmaker_v3_generation
```

If findings remain, use `needs_revision` and name the owning upstream file/flow.

## Final boundary

`voice_delivery_ready` means the accepted current delivery scope is ready.

It does **not** mean generated Eleven v3 audio has been heard unless audio evidence says so.

When audio is included, current readiness additionally requires canonical prompt ↔ exact generated prompt alignment and actual audio review against the quality gate above.
