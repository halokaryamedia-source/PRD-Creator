# Voice Validation & Delivery Procedure

Flow 7 validates the exact current Flow 6 revision and decides whether the requested delivery scope is ready.

## Entry

Start from `state/voice-state.yaml: voice_script_ready` for the current Voice Requirements revision.

Read only:

1. `work/voice-requirements.md`;
2. `work/voice-production.md`;
3. `SOUNDMAKER.md` when v3 wording/performance quality is in scope;
4. `DOCX-FORMAT.md` when DOCX presentation is in scope;
5. accepted PRD only when a project fact/term needs verification.

# 1. Mechanical validation

Run:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation checks current Voice ID, Type, Speaker, required canonical fields, DOCX content parity, and Letter-page structure.

Mechanical PASS proves parity/integrity only. It does not prove semantic readiness, conservation, visual quality, pronunciation, or audio quality.

# 2. Communication Conservation

For every changed/current prepared Voice ID, compare canonical wording back to Flow 5.

PASS only when:

- every independently actionable `Must communicate` fact that belongs in the moment remains clearly represented;
- every `Must not add/repeat` guardrail is respected;
- approved names, mechanics, result/state, sequence, and terminology retain their meaning;
- any authoritative Flow 5 `Timing Constraint` remains respected by the planned wording/timing approach;
- duration/polish did not silently remove required communication;
- no unsupported project fact was introduced.

Paraphrase and concise merging are allowed. Material thinning is not.

Record one result: **Communication Conservation: PASS | FAIL**.

Do not create a requirement-to-sentence matrix merely to prove this gate.

# 3. Integrated Voice Script Readiness

Review the current prepared scope once. The lenses below are questions inside one semantic review, not separate workflow stages.

| Lens | Ready when... |
|---|---|
| Communication | Purpose and required meaning are understandable without reopening source. |
| Listener | Each line fits the approved Trigger/player state and gives the right amount of information/action at that moment. |
| Character | Speaker identity stays coherent across lines without accidental template sameness. |
| Performance | Emotional movement, beat shape, punctuation, CAPS, tags, and reactions serve the scene rather than decorate it. |
| Timing | Estimated Duration/density is plausible, any authoritative Flow 5 timing constraint is honored, and no required fact was sacrificed to fit it. |
| Continuity | Briefing/reminder/success information progresses and nearby lines avoid accidental repeated openings, beat chains, tag positions, rhythms, CAPS climaxes, or closings. |
| Operator | Type/Speaker ownership, duration, exact prompt, and any special timing/pronunciation/setup action are clear enough to use without production guesswork. |

During this same review also verify:

- exact `Type` and `Speaker` remain compatible with Flow 5;
- wording remains plausible for approved Function, Purpose, Channel, and Trigger;
- optional `Timing Constraint` is treated as upstream truth, not as the same thing as Estimated Duration;
- terminology is consistent;
- material pronunciation risks are `confirmed`, `accepted_as_written`, or honestly left as `needs_confirmation`;
- no unsupported Eleven v3 notation such as SSML `<break>` exists.

`needs_confirmation` may remain during Preparation Mode / `voice_script_ready`, but blocks `voice_delivery_ready` until resolved or explicitly accepted.

Record one result: **Voice Script Readiness: PASS | FAIL**.

Do not persist seven lens scores or run separate review ceremonies for them.

# 4. First wrong owner

When a finding exists, fix the earliest owner that is actually wrong:

```text
project/gameplay/story fact
→ upstream PRD authority

Voice moment / Speaker / Channel / Trigger / Purpose / required communication / authoritative timing truth
→ Flow 5 voice-requirements.md

correct requirement but weak wording/performance/Estimated Duration
→ Flow 6 / SOUNDMAKER.md / voice-production.md

correct canonical script but wrong DOCX
→ builder / DOCX-FORMAT.md

correct script but actual generated-audio-only issue
→ Generation Mode evidence/settings/voice
```

Do not patch DOCX/audio or complicate the prompt to hide an upstream defect.

# 5. DOCX visual QA

When DOCX is in scope, render and inspect every page for:

- clipping/overlap;
- readable hierarchy;
- correct `Type · Speaker` association for each Voice ID;
- script-panel legibility and preserved line breaks;
- glyph, spacing, and shading defects.

Fix the canonical/builder owner and rebuild; never patch the DOCX as the source fix.

Record: **DOCX Visual: PASS | FAIL | NOT PROVEN**.

# 6. Audio evidence

If audio is not supplied:

```text
Audio Evidence: not_provided
```

This blocks audio-quality claims, not script/DOCX delivery when all non-audio gates pass.

When audio is in scope:

1. identify the exact generated prompt;
2. synchronize any user/UI-edited generated wording into `work/voice-production.md`;
3. identify actual voice/surface/Stability when relevant;
4. review the heard take using SoundMaker's Generation Mode diagnosis;
5. record only what was actually reviewed.

Use:

- `partial_review`;
- `reviewed_passed`;
- `reviewed_with_findings`.

Do not infer immersion from tag count or prompt appearance.

# 7. Acceptance file

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

This compact record replaces duplicated persisted semantic-review headings. The review still checks Communication, Listener, Character, Performance, Timing, Continuity, Operator, terminology/pronunciation, and Speaker/Channel/Trigger compatibility; it records one integrated decision.

Critical or Major findings block delivery.

# 8. Existing state schema

Keep `state/voice-state.yaml` compatible; do not add another state schema for this interface model.

For script + DOCX delivery, existing fields may remain:

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

These compatibility fields summarize the integrated review; they do **not** require separate review passes.

If audio is included, readiness additionally requires canonical prompt ↔ exact generated prompt alignment and actual heard-audio review.

# Severity

- **Critical** — wrong/missing Voice ID, Type or Speaker; wrong project fact; wrong Channel/Trigger; missing required communication; ignored authoritative timing constraint; or canonical/generated prompt drift that would produce the wrong asset.
- **Major** — material wording, v3 performance, continuity, pronunciation, conservation, or layout problem requiring production guesswork.
- **Minor** — delivery remains correct/usable but clarity/notation/layout can improve without changing meaning.
- **Suggestion** — optional polish.

# Bounded revision

Revalidate only invalidated scope plus any adjacent/project continuity materially affected by the change.

Do not replay unaffected Voice IDs, full source review, or audio checks for ceremony.

# Final boundary

`voice_delivery_ready` means only the current requested delivery scope is ready.

For script/DOCX delivery it requires:

- Mechanical PASS;
- Communication Conservation PASS;
- Voice Script Readiness PASS;
- DOCX Visual PASS when DOCX is claimed ready;
- Critical = 0;
- Major = 0;
- truthful audio evidence state;
- no stale upstream revision.

It does not imply generated-audio approval, client sign-off, implementation completion, or release.
