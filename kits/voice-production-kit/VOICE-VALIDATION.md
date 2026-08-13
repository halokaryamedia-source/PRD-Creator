# Voice Validation & Delivery Procedure

Flow 7 validates the exact current Flow 6 revision and decides whether the requested Voice production scope is ready.

The default human-facing presentation is now the **same `output/final.html` project document** used by the PRD. DOCX is optional export only.

## Entry

Start from `state/voice-state.yaml: voice_script_ready` for the current Voice Requirements revision.

Read only:

1. `work/voice-requirements.md`;
2. `work/voice-production.md`;
3. `output/final.html` when the consolidated project HTML is in scope;
4. `SOUNDMAKER.md` when wording/performance quality is in scope;
5. `DOCX-FORMAT.md` only when DOCX export exists/is requested;
6. accepted PRD only when a project fact/term needs verification.

# 1. Mechanical validation

Run:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation always checks current Voice ID / Type / Speaker parity and canonical script structure.

When `output/final.html` exists, it also checks that the consolidated HTML contains the current Production Assets Voice prompt panels with exact canonical performance text.

When `output/Voice Production.docx` exists, it validates that optional export too.

Mechanical PASS does not prove semantic readiness, visual quality, pronunciation, or audio quality.

# 2. Communication Conservation

For every changed/current prepared Voice ID, compare canonical wording back to Flow 5.

PASS only when:

- every independently actionable `Must communicate` fact that belongs in the moment remains clearly represented;
- every `Must not add/repeat` guardrail is respected;
- approved names, mechanics, result/state, sequence, and terminology retain meaning;
- any authoritative Flow 5 `Timing Constraint` remains respected;
- duration/performance polish did not silently remove required communication;
- no unsupported project fact was introduced.

Record one result:

```text
Communication Conservation: PASS | FAIL
```

Do not create a requirement-to-sentence matrix.

# 3. Integrated Voice Script Readiness

Review the current prepared scope once.

| Lens | Ready when... |
|---|---|
| Communication | Purpose and required meaning are clear without reopening source. |
| Listener | Each line fits the approved Trigger/player state and communicates the right amount at that moment. |
| Character | Speaker identity stays coherent without accidental template sameness. |
| Performance | Every standalone line has an intentional starting direction; transition tags, beat shape, punctuation, and emphasis serve the scene rather than decorating it. |
| Timing | Estimated Duration is plausible, source timing constraints are honored, and no required fact was sacrificed. |
| Continuity | Information progresses and nearby lines avoid accidental repeated structures. |
| Operator | Actor assignment, exact prompt, duration, and any special setup are clear enough to use without guessing. |

During the same review verify terminology, material pronunciation risk, Channel/Trigger/Function compatibility, and absence of unsupported v3 notation such as SSML `<break>`.

Record one result:

```text
Voice Script Readiness: PASS | FAIL
```

Do not create separate persisted scores/gates for the lenses.

# 4. Production Assets HTML review

When the consolidated project HTML is claimed current, inspect the Voice section as a production surface.

Ready when:

- `Production Assets → Voice` appears after PRD core content;
- Voice Setup is shown once with the selected ElevenLabs voice prominent, not repeated per line;
- sections and scripts follow canonical gameplay order;
- each line clearly shows title, secondary Speaker/Estimated Duration metadata, exact script panel, and an integrated Copy action;
- performance-direction tags are visually distinct from spoken text without changing the copied canonical payload;
- internal Flow 5/reasoning/QA metadata is absent from the visible Voice page;
- exact script line breaks remain readable;
- no clipping/overlap or obvious visual break from the PRD design language exists.

Record:

```text
Project HTML Visual: PASS | FAIL | NOT PROVEN
```

Static HTML inspection can prove structure/text parity but cannot claim visual PASS without rendered/browser evidence.

# 5. Voice Cast / actor selection

Preparation Mode may remain script-ready with `Voice selection pending` for a Speaker.

Before actual Generation Mode for a Voice ID:

- the active Speaker's intended ElevenLabs voice must be selected;
- the selected voice should be synchronized into the canonical `Voice Cast` block;
- the same actor assignment should appear in the consolidated project HTML after rerender.

Do not invent a commercial voice merely to remove a pending state.

# 6. Optional DOCX export

DOCX is no longer a default delivery requirement.

When explicitly produced, render/inspect it for correct Type · Speaker association, section hierarchy, script text, line breaks, glyphs, spacing, and pagination.

Record only when DOCX exists:

```text
DOCX Visual: PASS | FAIL | NOT PROVEN
```

A DOCX defect is fixed in the builder/canonical source and rebuilt; never hand-edit the DOCX as source truth.

# 7. Audio evidence

If audio is not supplied:

```text
Audio Evidence: not_provided
```

This blocks audio-quality claims, not non-audio Voice Production readiness.

When actual audio is in scope:

1. identify the exact generated prompt;
2. identify the actual actor voice / Surface / Stability when relevant;
3. synchronize any user/UI-edited generated wording into `work/voice-production.md`;
4. rerender `output/final.html` when canonical actor/prompt changed;
5. review the heard take using SoundMaker Generation Mode diagnosis;
6. record only what was actually reviewed.

Use:

- `partial_review`;
- `reviewed_passed`;
- `reviewed_with_findings`.

# 8. First wrong owner

```text
project/gameplay/story fact
→ upstream PRD authority

Voice moment / Speaker / Channel / Trigger / Purpose / required communication / source timing truth
→ Flow 5 voice-requirements.md

wording / performance / Estimated Duration / actor-voice selection
→ Flow 6 / SoundMaker / voice-production.md

correct canonical data but wrong Production Assets HTML
→ PRD renderer Production Assets compositor

optional DOCX-only issue
→ Voice DOCX builder

actual audio-only issue with correct canonical production
→ Generation Mode evidence/settings/voice
```

# 9. Acceptance record

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

# 10. State compatibility

Use `project_html: output/final.html` for new/current Voice production state.

```yaml
flow: 7
status: voice_delivery_ready
requirements: work/voice-requirements.md
script: work/voice-production.md
project_html: output/final.html
acceptance: work/voice-acceptance.md
mechanical: passed
coverage: passed
terminology_pronunciation: passed
speaker_channel_trigger: passed
performance_continuity: passed
audio_evidence: not_provided
delivery_scope: project_html
next_step: complete_or_soundmaker_v3_generation
```

Existing projects may retain `docx` / `docx_visual` fields when that export exists. Do not create a migration merely to delete harmless historical compatibility metadata.

# Severity

- **Critical** — wrong/missing Voice ID/Type/Speaker; missing initial performance-direction tag; wrong project fact/Channel/Trigger; missing required communication; ignored authoritative timing constraint; stale project HTML prompt; or canonical/generated prompt drift that would produce the wrong asset.
- **Major** — material wording, actor assignment, v3 performance, continuity, pronunciation, conservation, operator-readiness, or layout problem requiring production guesswork.
- **Minor** — correct/usable delivery with non-blocking clarity/notation/layout polish.
- **Suggestion** — optional improvement.

# Bounded revision

```text
change
→ first wrong owner
→ affected Voice ID / Speaker scope only
→ Communication Conservation
→ integrated readiness on materially affected scope
→ rerender same final.html
→ recheck affected Production Assets view
→ stop
```

Do not replay unaffected Voice IDs, PRD acceptance, or audio checks for ceremony.

# Final boundary

For default non-audio Voice Production delivery, `voice_delivery_ready` requires:

- Mechanical PASS;
- Communication Conservation PASS;
- Voice Script Readiness PASS;
- consolidated project HTML current;
- Project HTML Visual PASS when visual readiness is claimed;
- Critical = 0;
- Major = 0;
- truthful audio evidence state;
- no stale upstream PRD revision.

It does not imply generated-audio approval, client sign-off, implementation completion, or release.
