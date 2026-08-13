# Voice Validation & Delivery

Status: active Flow 7 policy

## Purpose

Flow 7 decides whether the current `voice_script_ready` revision is safe to deliver for the requested Voice Production scope.

Default non-audio delivery is the **same project HTML** containing PRD core + `Production Assets → Voice`. Audio and DOCX are optional scopes.

## Canonical sequence

```text
voice_script_ready
↓
mechanical Voice ID / Type / Speaker + derived-output parity
↓
Communication Conservation
↓
one integrated Voice Script Readiness review
↓
Project HTML visual QA when claimed
↓
optional DOCX QA
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

Mechanical validation always checks canonical requirements/script parity.

When consolidated `output/final.html` exists, it checks that Production Assets Voice prompt panels contain the exact current canonical performance text.

When optional DOCX exists, it validates that export too.

Mechanical PASS cannot establish semantic readiness, visual quality, pronunciation, or audio quality.

## Communication Conservation

Compare each changed/current prepared line to its Flow 5 requirement.

PASS only when every material `Must communicate` fact remains clear, `Must not add/repeat` remains respected, project meaning is intact, authoritative Timing Constraint remains honored when present, and production polish did not introduce or delete material meaning.

Record:

```text
Communication Conservation: PASS | FAIL
```

Do not persist a requirement-to-sentence matrix.

## Integrated Voice Script Readiness

Review once through:

| Lens | Ready when... |
|---|---|
| Communication | Purpose/required meaning is clear and no unsupported fact was added. |
| Listener | The line fits approved Trigger/player state and communicates the right amount at that moment. |
| Character | Speaker identity remains coherent without accidental template sameness. |
| Performance | Beat/emotional/textual direction serves the scene. |
| Timing | Estimated Duration is plausible, source timing truth is honored, and required meaning was not sacrificed. |
| Continuity | Information progresses and related lines avoid accidental repeated structures. |
| Operator | Actor assignment, duration, exact prompt, and any special action are unambiguous. |

During the same review verify terminology/pronunciation risk, Function/Purpose/Channel/Trigger compatibility, and absence of unsupported v3 notation.

Record one semantic result:

```text
Voice Script Readiness: PASS | FAIL
```

Do not create separate persisted scores/review ceremonies for the lenses.

## Production Assets HTML

When project HTML readiness is claimed, inspect the Voice section for:

- `Production Assets → Voice` after PRD core content;
- Voice Cast shown once;
- gameplay/canonical order preserved;
- per-line title, Actor, Estimated Duration, exact script, and Copy Text;
- no Flow 5 requirement/reasoning/QA leakage;
- readable line breaks and density;
- no clipping/overlap or obvious break from PRD visual language.

Record:

```text
Project HTML Visual: PASS | FAIL | NOT PROVEN
```

Static inspection can prove structure/text parity but cannot establish visual PASS without actual rendered/browser evidence.

## Voice Cast / generation readiness

Preparation Mode may remain script-ready while an actor voice is pending.

Before actual Generation Mode for a Voice ID:

- active Speaker's intended ElevenLabs voice is selected;
- selection is synchronized into canonical `Voice Cast`;
- consolidated HTML is rerendered when selection changed.

Never invent a commercial voice merely to clear a pending field.

## Optional DOCX

DOCX is not a default delivery gate.

When it exists/is claimed, verify Type/Speaker association, hierarchy, exact script, line breaks, glyphs, spacing, shading, and pagination.

Record only then:

```text
DOCX Visual: PASS | FAIL | NOT PROVEN
```

## Audio evidence

Default non-audio delivery may use:

```text
Audio Evidence: not_provided
```

When actual audio is in scope, use `partial_review`, `reviewed_passed`, or `reviewed_with_findings`; verify actual actor voice and exact generated prompt alignment before accepting audio scope.

Never infer audio quality from script appearance, tags, or Estimated Duration.

## First wrong owner

```text
project/gameplay/story fact → PRD authority
Voice moment/Speaker/Channel/Trigger/Purpose/required communication/source timing → Flow 5
wording/performance/Estimated Duration/actor selection → Flow 6 / SoundMaker
correct canonical Voice + wrong Production Assets HTML → PRD renderer compositor
optional DOCX-only issue → Voice DOCX builder
audio-only issue with correct canonical production → Generation Mode
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

Critical and Major findings block delivery.

## State compatibility

New/current default state may point to:

```yaml
project_html: output/final.html
delivery_scope: project_html
```

Existing fields such as `coverage`, `terminology_pronunciation`, `speaker_channel_trigger`, and `performance_continuity` remain compatibility summaries of the integrated review, not independent review passes.

Existing projects may retain `docx`/`docx_visual` when that optional export exists. Do not create migration work merely to erase harmless compatibility data.

## Severity

- **Critical** — wrong/missing Voice ID/Type/Speaker, wrong project fact/Channel/Trigger, missing required communication, ignored timing truth, stale project HTML prompt, or canonical/generated prompt drift that would produce the wrong asset.
- **Major** — material conservation, actor assignment, wording, v3 performance, continuity, pronunciation, operator-readiness, or layout defect requiring production guesswork.
- **Minor** — correct/usable delivery with non-blocking clarity/notation/layout polish.
- **Suggestion** — optional improvement.

## Bounded revision

```text
change
→ first wrong owner
→ affected Voice/Speaker scope only
→ Communication Conservation
→ integrated readiness on affected scope
→ rerender same final.html
→ recheck affected Production Assets view
→ stop
```

Voice-only production changes do not reopen PRD acceptance when PRD canonical meaning remains unchanged.

## Delivery gate

For default non-audio Voice Production delivery, `voice_delivery_ready` requires:

- Mechanical PASS;
- Communication Conservation PASS;
- Voice Script Readiness PASS;
- consolidated project HTML current;
- Project HTML Visual PASS when visual readiness is claimed;
- Critical = 0;
- Major = 0;
- truthful audio evidence;
- no stale upstream PRD revision.

It does not imply generated-audio approval, client sign-off, implementation completion, or release.
