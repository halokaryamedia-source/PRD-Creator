# Voice Validation & Delivery

Status: active Flow 7 policy

## Purpose

Flow 7 decides whether the current `voice_script_ready` revision is safe to deliver for the requested Voice Production scope.

Default non-audio delivery is the **same project HTML** containing PRD core + `04 Production Assets → matching gameplay moment → AUDIO`. DOCX and audio are optional scopes.

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
optional DOCX / audio evidence
↓
voice_delivery_ready | needs_revision | blocked
```

## Mechanical validation

Run:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation always checks canonical requirements/script parity. It also proves current revision identity: `voice-state.yaml.source_prd_revision`, the current accepted PRD handoff, `render-data.document.version`, `voice-requirements.md` `Source PRD revision`, and the source revision declared by `voice-production.md` must agree. The canonical script's `Source Voice Requirements` SHA-256 must match the exact current `work/voice-requirements.md` bytes.

When consolidated `output/v<document.version>/prd.html` exists, it also checks current Production Assets Voice section/prompt identity and exact canonical performance text. Current visible AUDIO-field/layout behavior is owned by the Project Document 04 compositor regression rather than duplicated as another Voice HTML schema.

When optional DOCX exists, it validates that export too.

Mechanical PASS cannot establish semantic readiness or visual quality.

## Communication Conservation

Compare each changed/current prepared line to its Flow 5 requirement.

PASS only when every material `Must communicate` fact remains clear, `Must not add/repeat` remains respected, project meaning is intact, source timing truth remains honored when present, and production polish did not introduce or delete material meaning.

Record:

```text
Communication Conservation: PASS | FAIL
```

Do not persist a requirement-to-sentence matrix.

## Integrated Voice Script Readiness

Review once through Communication, Listener, Character, Performance, Timing, Continuity, and Operator lenses. Keep this as one integrated result rather than separate scorecards.

Record:

```text
Voice Script Readiness: PASS | FAIL
```

## Production Assets HTML

When project HTML visual readiness is claimed, inspect the Voice presentation for:

- accepted PRD sidebar hierarchy/page identity remains intact;
- gameplay/objective sections stay under `03 Development`;
- `04 Production Assets` is additive and links matching gameplay/shared pages rather than a separate Voice category;
- Voice appears as `AUDIO` inside the correct natural gameplay moment;
- each dialogue resource title identifies `<Character> — <Line Title>`;
- each dialogue resource visibly includes Function, Voice Preset, ElevenLabs Model = `Eleven v3`, Estimated Duration, and Prompt;
- a separate visible Speaker row, Flow 5 Context/Trigger row, line-count summary, Primary Speaker summary, and Voice Setup block are absent unless a future approved contract explicitly reintroduces them;
- performance-direction tags remain visually distinct without changing the copied canonical payload;
- Flow 5 Purpose, Trigger, `Must communicate`, `Must not add/repeat`, source refs, reasoning, WPM math, QA, and other internal fields stay out of the visible 04 resource;
- navigation labels wrap naturally and no clipping/overlap or obvious break from the PRD visual language exists at the desktop widths being claimed.

Record:

```text
Project HTML Visual: PASS | FAIL | NOT PROVEN
```

Static inspection can prove structure/text parity but cannot establish visual PASS without actual rendered/browser evidence.

## Optional DOCX

DOCX is not a default delivery gate. When it exists/is claimed, verify it as an optional derived export.

## Audio evidence

Default non-audio delivery may use:

```text
Audio Evidence: not_provided
```

Do not infer audio quality from script appearance, tags, or Estimated Duration.

## First wrong owner

```text
project/gameplay/story fact → PRD authority
Voice moment/Speaker/Channel/Trigger/Purpose/required communication/source timing → Flow 5
wording/performance/Estimated Duration/production selection → Flow 6
correct canonical Voice + wrong Production Assets HTML → PRD renderer compositor
optional DOCX-only issue → Voice DOCX builder
audio-only issue → audio evidence scope
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
project_html: output/v<document.version>/prd.html
delivery_scope: project_html
```

Existing compatibility summary fields may remain. Existing projects may retain `docx`/`docx_visual` when that optional export exists; do not create migration work merely to remove harmless historical metadata.

## Bounded revision

```text
change
→ first wrong owner
→ affected Voice/Speaker scope only
→ Communication Conservation
→ integrated readiness on affected scope
→ rerender current versioned prd.html
→ recheck affected 04 AUDIO view
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
- truthful evidence boundaries;
- no stale upstream PRD revision.

It does not imply audio approval, client sign-off, implementation completion, or release.
