# Voice Validation & Delivery

Status: active Flow 7 policy

## Purpose

Flow 7 decides whether the current `voice_script_ready` revision is safe to deliver for the requested Voice scope. Audio is optional evidence and is reviewed only when actual generated audio is in scope.

## Canonical sequence

```text
voice_script_ready
↓
mechanical Voice ID / Type / Speaker parity + DOCX integrity
↓
Communication Conservation
↓
one integrated Voice Script Readiness review
↓
DOCX visual QA when claimed
↓
optional exact-prompt ↔ actual-audio review
↓
voice_delivery_ready | needs_revision | blocked
```

## Mechanical validation

Run:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation checks required files, placeholders, exact Voice ID/Type/Speaker parity, canonical script structure, DOCX content parity, and Letter-page structure.

Mechanical PASS cannot establish semantic readiness, Communication Conservation, visual quality, pronunciation, or audio quality.

## Communication Conservation

Compare each changed/current prepared line to its Flow 5 requirement.

PASS only when every independently actionable `Must communicate` fact remains clearly represented, every `Must not add/repeat` guardrail remains respected, approved meaning remains intact, and duration/performance polish did not silently thin communication.

Record one result:

```text
Communication Conservation: PASS | FAIL
```

Do not persist a requirement-to-sentence matrix.

## Integrated Voice Script Readiness

Review the current scope once using these lenses:

| Lens | Ready when... |
|---|---|
| Communication | Purpose/required meaning is clear and no unsupported fact was added. |
| Listener | The line fits approved Trigger/player state and communicates the right amount at that moment. |
| Character | Speaker identity is coherent without accidental template sameness. |
| Performance | Beat/emotional/textual direction serves the scene rather than decorating it. |
| Timing | Estimated density is plausible without sacrificing required meaning. |
| Continuity | Information progresses and related lines avoid accidental repeated structures. |
| Operator | Type/Speaker ownership, duration, exact prompt, and special setup are unambiguous. |

During this same review verify terminology, material pronunciation risk, Channel/Trigger/Function compatibility, and absence of unsupported v3 notation such as SSML `<break>`.

A material pronunciation risk may remain at Flow 6 `voice_script_ready`, but `voice_delivery_ready` requires it to be `confirmed` or explicitly `accepted_as_written`.

Record one result:

```text
Voice Script Readiness: PASS | FAIL
```

Do not create separate persisted scores or review ceremonies for the seven lenses.

## First wrong owner

Fix the earliest wrong owner:

```text
project/gameplay/story fact → upstream PRD authority
Voice moment/Speaker/Channel/Trigger/required communication → Flow 5
wording/performance/duration → Flow 6 / SoundMaker
DOCX-only presentation → builder / DOCX-FORMAT.md
audio-only issue with correct script → Generation Mode evidence/settings/voice
```

## DOCX visual QA

When DOCX is in scope, render and inspect every page for clipping/overlap, correct `Type · Speaker` association, readable hierarchy, script-panel legibility, preserved line breaks, glyphs, spacing, and shading.

Record:

```text
DOCX Visual: PASS | FAIL | NOT PROVEN
```

## Audio evidence

Default script/DOCX delivery may use:

```text
Audio Evidence: not_provided
```

When actual audio is in scope, use `partial_review`, `reviewed_passed`, or `reviewed_with_findings`, and verify exact generated prompt alignment before accepting audio scope.

Never infer audio quality from script quality, tags, or Estimated Duration.

## Acceptance record

Keep `work/voice-acceptance.md` compact:

```text
# Voice Acceptance
Status: needs_revision | voice_delivery_ready
Mechanical: PASS | FAIL
Voice Script Readiness: PASS | FAIL
Communication Conservation: PASS | FAIL
DOCX Visual: PASS | FAIL | NOT PROVEN
Audio Evidence: not_provided | partial_review | reviewed_passed | reviewed_with_findings
Findings: <only when findings exist>
Critical: N
Major: N
```

The integrated review still considers communication, listener state, character, performance, timing, continuity, operator clarity, terminology/pronunciation, and Speaker/Channel/Trigger compatibility. It simply records one semantic decision instead of many duplicated fields.

## Existing state compatibility

Keep the current `state/voice-state.yaml` schema. Existing fields such as `coverage`, `terminology_pronunciation`, `speaker_channel_trigger`, and `performance_continuity` remain compatibility summaries of the integrated review; they are **not** instructions to run four independent review passes.

## Severity

- **Critical** — wrong/missing Voice ID/Type/Speaker, wrong project fact/Channel/Trigger, missing required communication, or canonical/generated prompt drift that would produce the wrong asset.
- **Major** — material conservation, wording, v3 performance, continuity, pronunciation, operator-readiness, or layout defect requiring production guesswork.
- **Minor** — correct/usable delivery with non-blocking clarity/notation/layout polish.
- **Suggestion** — optional improvement.

Critical and Major block `voice_delivery_ready`.

## Bounded revision

```text
change
→ first wrong owner
→ affected Voice ID/speaker scope only
→ Communication Conservation
→ integrated readiness on materially affected scope
→ rebuild/recheck affected derived output
→ stop
```

Do not replay unaffected Voice IDs or audio checks for ceremony.

## Delivery gate

For script/DOCX delivery, `voice_delivery_ready` requires:

- Mechanical PASS;
- Communication Conservation PASS;
- Voice Script Readiness PASS;
- DOCX Visual PASS when DOCX is claimed ready;
- Critical = 0;
- Major = 0;
- truthful audio evidence state;
- no stale upstream revision.

It does not imply generated-audio approval, client sign-off, implementation completion, or release.
