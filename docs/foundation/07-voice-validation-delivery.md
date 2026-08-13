# Voice Validation & Delivery

Status: active Flow 7 policy

## Purpose

Flow 7 decides whether the current `voice_script_ready` revision is safe to deliver as a Voice Production script/DOCX and, when audio is in scope, whether the reviewed audio corresponds to the current canonical Eleven v3 prompt.

Flow 7 does **not** assume generated ElevenLabs audio exists or sounds correct. Audio is reviewed only when actual evidence is supplied and explicitly included in delivery scope.

## Canonical sequence

```text
voice_script_ready
↓
mechanical Voice ID / Type / Speaker parity + DOCX integrity
↓
requirement coverage + factual fidelity
↓
terminology / pronunciation risk
↓
Speaker / Channel / Trigger consistency
↓
SoundMaker v3 project continuity / notation
↓
DOCX render + visual QA
↓
optional exact-prompt ↔ actual-audio review
↓
voice_delivery_ready | needs_revision | blocked
```

## Entry gate

Use the same current revision of:

- `work/voice-requirements.md`;
- `work/voice-production.md`;
- `output/Voice Production.docx` when DOCX is in scope;
- `state/voice-state.yaml`;
- actual generated prompt/audio evidence when audio is in scope.

If PRD meaning, Flow 5 scope, or canonical Flow 6 wording changed after prior acceptance, do not validate stale artifacts. Reopen the owning upstream flow first.

## Mechanical validation

Run:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation checks required files, placeholders, exact Voice ID/Type/**Speaker** parity, canonical script structure, DOCX content parity, and Letter-page structure. Mechanical pass cannot establish semantic, visual, pronunciation, or audio quality by itself.

## Semantic acceptance

### 1. Requirement coverage and factual fidelity

For every Voice ID, verify that spoken text:

- fulfills Flow 5 Purpose;
- communicates all material required facts;
- respects `Must not add/repeat` guardrails;
- preserves approved names, Speaker, sequence, mechanic, result, reward, Trigger, and state;
- introduces no new Voice moment or upstream project fact.

Paraphrase is allowed. Changed meaning is not.

### 2. Terminology / pronunciation

Verify official terms are consistent with accepted PRD and Voice Requirements.

Flag only material risk such as fantasy/proper names, unusual acronyms, multilingual phrases, or genuinely ambiguous terminology.

Use one status where needed:

- `confirmed` — explicit approved pronunciation evidence exists;
- `accepted_as_written` — creative owner intentionally accepts written form;
- `needs_confirmation` — delivery cannot yet claim pronunciation-ready.

Never claim pronunciation is verified without evidence.

### 3. Speaker / Channel / Trigger consistency

Verify the canonical `Speaker` matches Flow 5 and final wording remains plausible for the approved Speaker, Channel, Trigger, and communication function.

Route defects upstream instead of inventing metadata during review.

### 4. SoundMaker v3 project continuity

Review the whole project and check:

- narrator/character identity remains coherent;
- emotional changes follow scene/communication reasons rather than random escalation;
- nearby lines do not look mechanically templated;
- information progresses instead of repeatedly re-briefing the same facts;
- direction vocabulary is concise/compatible;
- punctuation, line breaks, ellipses/em dashes, and CAPS are purposeful;
- Estimated Duration remains plausible as an estimate;
- no unsupported v3 notation such as SSML `<break>`.

Detailed one-line construction belongs to `SOUNDMAKER.md`; do not duplicate its prompting checklist here.

## DOCX visual QA

Render current `output/Voice Production.docx` to page images and inspect every page when DOCX is in scope.

Check:

- clipping/overlap;
- correct `Type · Speaker` association for each Voice ID;
- readable section/title hierarchy;
- script-panel legibility and preserved line breaks;
- glyph, spacing, and shading defects.

A successful `python-docx` load is not visual proof.

## Audio evidence

Default delivery scope remains **script + DOCX for ElevenLabs use**. Audio is not required to set `voice_delivery_ready` unless current task explicitly includes generated audio delivery.

Record:

- `not_provided`;
- `partial_review`;
- `reviewed_passed`;
- `reviewed_with_findings`.

When audio is in scope, also verify:

1. the exact prompt actually generated is known;
2. if the user edited it before generation, that exact version is synchronized into `work/voice-production.md`;
3. actual audio was heard/reviewed for clarity, performance, pronunciation, and duration as applicable;
4. no older canonical script/DOCX acceptance is being presented as current against a newer approved prompt.

Do not infer generated-audio quality from script quality, tags, or estimated duration.

## Severity

- **Critical** — wrong/missing Voice ID, Type or Speaker; wrong project fact; wrong Channel/Trigger; missing required communication; or canonical/generated prompt drift that would produce the wrong asset.
- **Major** — material wording, v3 performance, continuity, pronunciation, or layout problem requiring production guesswork.
- **Minor** — delivery remains correct/usable but clarity/notation/layout can improve without changing meaning.
- **Suggestion** — optional polish.

Critical and Major block `voice_delivery_ready`.

## Finding ownership

- Voice scope/Purpose/Speaker/Channel/Trigger defect → Flow 5 `work/voice-requirements.md`;
- wording/performance/duration/SoundMaker defect → Flow 6 `work/voice-production.md` + `SOUNDMAKER.md`;
- DOCX presentation defect → Flow 6 builder / `DOCX-FORMAT.md`, then rebuild;
- upstream project fact defect → PRD/requirement owner;
- actual-audio-only defect with correct script → voice/settings/generation evidence, not silent script rewrite.

Never edit final DOCX or audio as canonical project meaning.

## Acceptance record

Create/update `work/voice-acceptance.md` with the existing compact Mechanical / Coverage / Terminology-Pronunciation / Speaker-Channel-Trigger / Performance / DOCX Visual / Audio Evidence / Findings / Gate structure.

Keep it concise; do not duplicate the full script.

## Voice state

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

If actual audio is the requested delivery scope, use `script_docx_audio` only after the current prompt/audio evidence is actually reviewed and passed.

Allowed Flow 7 statuses:

- `voice_validation`
- `needs_revision`
- `voice_delivery_ready`
- `blocked`

`no_voice_required` remains a valid upstream terminal outcome and does not require an empty script/DOCX.

## Delivery gate

Set `voice_delivery_ready` only when:

- mechanical validation passes;
- requirement coverage/factual fidelity passes;
- terminology/pronunciation risks are resolved or explicitly accepted;
- Speaker/Channel/Trigger consistency passes;
- SoundMaker v3 project continuity/notation passes;
- current DOCX visual QA passes when DOCX is in scope;
- Critical = 0;
- Major = 0;
- no stale upstream revision is being delivered;
- audio evidence state is truthful;
- if audio is included, exact generated prompt and canonical wording are synchronized and actual audio was reviewed.

## Revisions after delivery-ready

Any change to Voice Requirements, canonical script, exact approved/generated prompt, or DOCX-builder behavior invalidates previous acceptance for affected content:

```text
change
→ reopen owning flow
→ synchronize/regenerate/rebuild affected artifacts
→ state = voice_validation
→ rerun affected checks
→ issue current acceptance
```

Do not keep an old `voice_delivery_ready` state against newer canonical wording or approved generated audio.
